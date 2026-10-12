"""Run on Colab with the PortShield Python environment; public/synthetic only."""
import csv
import hashlib
import importlib.metadata
import json
import os
from pathlib import Path
import sys
import time
from datetime import datetime, timezone
from uuid import uuid4
from zipfile import ZipFile, ZIP_DEFLATED

ROOT = Path('/content/portshield-ai')
DATA = ROOT / 'data/synthetic/test-prefix-v2.jsonl'
EXPECTED_SHA = '7c2d7b063ca152302e8e234480da68bfc5c939ec0e002575b8e7cac53cbf0fbe'


def digest(path):
    h = hashlib.sha256()
    with path.open('rb') as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b''):
            h.update(chunk)
    return h.hexdigest()


def save(path, obj):
    path.write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')


def summarize(rows, records, out):
    from portshield_ai.evaluation import LABELS, score
    # Empty strings keep failed attempts invalid even with the older V1 evaluator.
    metrics = score(rows, [r['raw_response'] if r['raw_response'] is not None else '' for r in records])
    metrics['inference_error_count'] = sum(r['inference_error'] is not None for r in records)
    metrics['note'] = 'New no-prefix run compared with a prior opaque-prefix diagnostic; not a simultaneous controlled experiment.'
    save(out / 'metrics.json', metrics)
    errors = [r for r in records if not r['schema_valid'] or r['differences']]
    save(out / 'errors.json', errors)
    columns = LABELS + ['INVALID']
    matrix = {label: {pred: 0 for pred in columns} for label in LABELS}
    for row, record in zip(rows, records):
        pred = record['prediction']['event_type'] if record['schema_valid'] else 'INVALID'
        matrix[row['target']['event_type']][pred] += 1
    with (out / 'event_confusion_matrix.csv').open('w', newline='', encoding='utf-8') as stream:
        writer = csv.writer(stream)
        writer.writerow(['expected / predicted'] + columns)
        for label in LABELS:
            writer.writerow([label] + [matrix[label][pred] for pred in columns])
    field_counts = {}
    for field in rows[0]['target']:
        invalid = sum(not r['schema_valid'] for r in records)
        mismatches = sum(r['schema_valid'] and field in r['differences'] for r in records)
        field_counts[field] = {'mismatches_in_valid_outputs': mismatches,
                               'invalid_outputs': invalid,
                               'strict_total_errors': invalid + mismatches}
    save(out / 'field_errors.json', field_counts)
    lines = ['# No-prefix adapter diagnostic rerun', '',
             f'Examples: {len(rows)}. Fully correct: {len(rows) - len(errors)}.',
             f'Schema-valid: {sum(r["schema_valid"] for r in records)}.', '',
             '## Field errors', '', '| Field | Valid-output mismatches | Invalid outputs |',
             '|---|---:|---:|']
    for field, counts in field_counts.items():
        lines.append(f'| {field} | {counts["mismatches_in_valid_outputs"]} | {counts["invalid_outputs"]} |')
    lines += ['', '## Event confusion matrix', '',
              'Rows are expected classes; columns are predictions. INVALID includes schema and inference failures.', '',
              '| Expected | ' + ' | '.join(columns) + ' |',
              '|---|' + '---:|' * len(columns)]
    for label in LABELS:
        lines.append('| ' + label + ' | ' + ' | '.join(str(matrix[label][p]) for p in columns) + ' |')
    lines += ['', '## Interpretation limits', '',
              'This is a new run, not recovery of earlier predictions. Counts may differ from the previous reports.',
              'Only six distinct scenario bodies are repeated 40 times. The adapter was trained on V1 data.',
              'All-field metrics count whole-record validation failures as errors for every field.',
              'For invalid outputs, differences are not computed; raw_response and validation_error remain available.',
              'No raw-response repair, retraining, TTFT, throughput or memory benchmark is performed.',
              'The per-record duration is a diagnostic measurement, not a controlled performance benchmark.',
              'Do not use these inspected examples as a future independent holdout.', '',
              'See predictions.jsonl for every input, expected target, original response and field difference.',
              'See errors.json for only failed or mismatched records.']
    (out / 'report.md').write_text('\n'.join(lines) + '\n', encoding='utf-8')



def main():
    import re
    source_zip = Path('/content/adapter-prefix-v2-diagnostic-20261012T041428Z-f48de04f.zip')
    if not source_zip.exists():
        raise FileNotFoundError('Upload the original diagnostic ZIP to /content first.')
    with ZipFile(source_zip) as package:
        assert package.testzip() is None
        hashes = json.loads(package.read('artifact-hashes.json'))
        for name, expected in hashes.items():
            assert hashlib.sha256(package.read(name)).hexdigest() == expected, name
        original_bytes = package.read('test-prefix-v2.jsonl')
        previous = [json.loads(line) for line in package.read('predictions.jsonl').splitlines()]
        old_meta = json.loads(package.read('run-metadata.json'))
        old_generation = json.loads(package.read('generation-config.json'))
        original_rows = [json.loads(line) for line in original_bytes.splitlines()]
    assert hashlib.sha256(original_bytes).hexdigest() == EXPECTED_SHA
    assert old_meta['status'] == 'completed'
    assert len(original_rows) == len(previous) == 240
    rows = []
    for row, prior in zip(original_rows, previous):
        assert row['id'] == prior['id'] and row['text'] == prior['text'] and row['target'] == prior['expected']
        assert row['data_class'] == 'synthetic'
        text, count = re.subn(r'^Fictional exercise [0-9a-f]{10}: ', '', row['text'], count=1)
        assert count == 1, row['id']
        rows.append({**row, 'text': text})
    adapter = ROOT / 'models/adapter'
    for name, expected in old_meta['adapter_hashes'].items():
        assert digest(adapter / name) == expected, f'Adapter file differs: {name}'
    for name, expected in old_meta['code_hashes'].items():
        assert digest(ROOT / 'src/portshield_ai' / name) == expected, f'Code differs: {name}'
    base_provenance = old_meta['base_acquisition_provenance']
    for name, expected in base_provenance['files'].items():
        assert digest(ROOT / 'models/base' / name) == expected, f'Base file differs: {name}'
    for name, expected in old_meta['packages'].items():
        assert importlib.metadata.version(name) == expected, f'Package version differs: {name}'
    from portshield_ai.inference import HFClient
    from portshield_ai.schema import EventAnalysis
    import torch
    assert torch.cuda.is_available(), 'Restore the GPU environment first.'
    assert torch.cuda.get_device_name(0) == old_meta['gpu'], 'GPU model differs from the prior diagnostic.'
    for row in rows:
        EventAnalysis.model_validate(row['target'])
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid4().hex[:8]
    out = ROOT / 'results/runs' / ('adapter-no-prefix-diagnostic-' + run_id)
    out.mkdir(parents=True, exist_ok=False)
    dataset = ''.join(json.dumps(row, sort_keys=True) + '\n' for row in rows).encode('utf-8')
    # Use real newline characters, not escaped text, in the JSONL artifact.
    dataset = b'\n'.join(json.dumps(row, sort_keys=True).encode('utf-8') for row in rows) + b'\n'
    (out / 'test-no-prefix.jsonl').write_bytes(dataset)
    metadata = {
        'run_id': run_id, 'status': 'running', 'started_at_utc': datetime.now(timezone.utc).isoformat(),
        'comparison_run_id': old_meta['run_id'], 'source_archive_sha256': digest(source_zip),
        'dataset_sha256': digest(out / 'test-no-prefix.jsonl'), 'original_dataset_sha256': EXPECTED_SHA,
        'change': 'Removed only the leading Fictional exercise <opaque reference>: prefix.',
        'adapter_hashes': old_meta['adapter_hashes'], 'base_acquisition_provenance': base_provenance,
        'code_hashes': old_meta['code_hashes'], 'packages': old_meta['packages'],
        'python': sys.version, 'gpu': torch.cuda.get_device_name(0),
        'comparison_limit': 'Historical paired comparison; timing/order and numerical variation are not isolated.'}
    save(out / 'run-metadata.json', metadata)
    print('All artifact, package and GPU checks passed. No training.', flush=True)
    print(f'Output: {out}', flush=True)
    model = HFClient(str(ROOT / 'models/base'), adapter=str(adapter))
    current_generation = model.model.generation_config.to_dict()
    assert current_generation == old_generation, 'Generation configuration differs; stop before inference.'
    overrides = {'max_new_tokens': 256, 'do_sample': False, 'pad_token_id': model.tokenizer.eos_token_id}
    assert overrides == old_meta['generation_overrides'], 'Generation overrides differ.'
    metadata['generation_overrides'] = overrides
    save(out / 'run-metadata.json', metadata)
    save(out / 'generation-config.json', current_generation)
    records = []
    with (out / 'predictions.jsonl').open('w', encoding='utf-8', newline='\n') as stream:
        for index, row in enumerate(rows, 1):
            rec = {'id': row['id'], 'template_family': row['template_family'], 'text': row['text'],
                   'expected': row['target'], 'raw_response': None, 'prediction': None,
                   'json_valid': False, 'schema_valid': False, 'differences': None,
                   'inference_error': None, 'validation_error': None}
            start = time.perf_counter()
            try:
                rec['raw_response'] = model.predict(row['text'])
            except Exception as exc:
                rec['inference_error'] = type(exc).__name__
            rec['inference_seconds'] = time.perf_counter() - start
            if rec['inference_error'] is None:
                try:
                    parsed = json.loads(rec['raw_response'])
                    rec['json_valid'] = True
                    rec['prediction'] = EventAnalysis.model_validate(parsed).model_dump()
                    rec['schema_valid'] = True
                    rec['differences'] = {k: {'expected': v, 'predicted': rec['prediction'][k]}
                                          for k, v in row['target'].items() if rec['prediction'][k] != v}
                except (ValueError, TypeError) as exc:
                    rec['validation_error'] = str(exc)
            stream.write(json.dumps(rec, ensure_ascii=False) + '\n')
            stream.flush()
            os.fsync(stream.fileno())
            records.append(rec)
            if index % 20 == 0:
                print(f'Processed {index}/{len(rows)}', flush=True)
    summarize(rows, records, out)
    paired = []
    counts = {'correct_in_both': 0, 'corrected': 0, 'regressed': 0, 'incorrect_in_both': 0}
    for old, new in zip(previous, records):
        before = old['schema_valid'] and not old['differences']
        after = new['schema_valid'] and not new['differences']
        category = ('correct_in_both' if after else 'regressed') if before else ('corrected' if after else 'incorrect_in_both')
        counts[category] += 1
        paired.append({'id': new['id'], 'category': category, 'expected': new['expected'],
                       'with_prefix_text': old['text'], 'without_prefix_text': new['text'],
                       'with_prefix_response': old['raw_response'], 'without_prefix_response': new['raw_response'],
                       'with_prefix_differences': old['differences'], 'without_prefix_differences': new['differences'],
                       'with_prefix_schema_valid': old['schema_valid'], 'without_prefix_schema_valid': new['schema_valid']})
    save(out / 'paired-comparison.json', {'counts': counts, 'records': paired,
        'limitation': 'Comparison against the prior run; not a same-session randomized causal experiment.'})
    from portshield_ai.evaluation import score
    save(out / 'reference-metrics.json', score(original_rows, [r['raw_response'] if r['raw_response'] is not None else '' for r in previous]))
    metadata.update(status='completed', completed_at_utc=datetime.now(timezone.utc).isoformat(), records_processed=len(records))
    save(out / 'run-metadata.json', metadata)
    (out / 'compare_no_prefix.py').write_bytes(Path(__file__).read_bytes())
    save(out / 'artifact-hashes.json', {p.name: digest(p) for p in out.iterdir() if p.is_file()})
    archive = out.with_suffix('.zip')
    with ZipFile(archive, 'w', ZIP_DEFLATED) as package:
        for p in out.iterdir():
            if p.is_file(): package.write(p, arcname=p.name)
    Path('/content/portshield-no-prefix-latest.txt').write_text(str(archive), encoding='utf-8')
    print('Comparison counts:', counts, flush=True)
    print(f'Completed. ZIP: {archive}', flush=True)


if __name__ == '__main__':
    main()
