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
    metrics['note'] = 'New diagnostic rerun; not the missing individual outputs of the earlier evaluation.'
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
    lines = ['# Corrected-prefix adapter diagnostic rerun', '',
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
    if not DATA.exists():
        raise FileNotFoundError('Restore the session and prepare test-prefix-v2.jsonl first.')
    if digest(DATA) != EXPECTED_SHA:
        raise ValueError('Dataset hash differs from the published corrected-prefix test. Stop and inspect.')
    adapter = ROOT / 'models/adapter'
    for path in (adapter / 'adapter_model.safetensors', adapter / 'adapter_config.json',
                 ROOT / 'models/base/config.json'):
        if not path.exists():
            raise FileNotFoundError(path)
    from portshield_ai.inference import HFClient
    from portshield_ai.schema import EventAnalysis
    import torch
    if not torch.cuda.is_available():
        raise RuntimeError('CUDA GPU required for comparison with the previous Colab runs.')
    rows = [json.loads(line) for line in DATA.read_text().splitlines() if line.strip()]
    for row in rows:
        assert row['data_class'] == 'synthetic'
        EventAnalysis.model_validate(row['target'])
    run_id = datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ') + '-' + uuid4().hex[:8]
    out = ROOT / 'results/runs' / ('adapter-prefix-v2-diagnostic-' + run_id)
    out.mkdir(parents=True, exist_ok=False)
    metadata = {'run_id': run_id, 'started_at_utc': datetime.now(timezone.utc).isoformat(),
                'status': 'running', 'dataset_sha256': EXPECTED_SHA, 'records_expected': len(rows),
                'gpu': torch.cuda.get_device_name(0), 'python': sys.version,
                'packages': {name: importlib.metadata.version(name) for name in
                             ['torch', 'transformers', 'peft', 'accelerate', 'pydantic']},
                'adapter_hashes': {p.name: digest(p) for p in adapter.iterdir() if p.is_file()},
                'code_hashes': {name: digest(ROOT / 'src/portshield_ai' / name)
                                for name in ['inference.py', 'prompts.py', 'schema.py', 'evaluation.py']}}
    provenance = ROOT / 'models/base/provenance.json'
    if provenance.exists():
        metadata['base_acquisition_provenance'] = json.loads(provenance.read_text())
    save(out / 'run-metadata.json', metadata)
    (out / 'test-prefix-v2.jsonl').write_bytes(DATA.read_bytes())
    print(f'Output directory: {out}', flush=True)
    print('Loading base model and saved adapter. No training.', flush=True)
    model = HFClient(str(ROOT / 'models/base'), adapter=str(adapter))
    save(out / 'generation-config.json', model.model.generation_config.to_dict())
    metadata['generation_overrides'] = {'max_new_tokens': 256, 'do_sample': False,
                                       'pad_token_id': model.tokenizer.eos_token_id}
    save(out / 'run-metadata.json', metadata)
    records = []
    with (out / 'predictions.jsonl').open('w', encoding='utf-8', newline='\n') as stream:
        for index, row in enumerate(rows, 1):
            rec = {'id': row['id'], 'template_family': row['template_family'],
                   'text': row['text'], 'expected': row['target'], 'raw_response': None,
                   'prediction': None, 'json_valid': False, 'schema_valid': False,
                   'differences': None, 'inference_error': None, 'validation_error': None}
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
    metadata.update(status='completed', completed_at_utc=datetime.now(timezone.utc).isoformat(),
                    records_processed=len(records))
    save(out / 'run-metadata.json', metadata)
    (out / 'diagnose_prefix_v2.py').write_bytes(Path(__file__).read_bytes())
    save(out / 'artifact-hashes.json', {p.name: digest(p) for p in out.iterdir() if p.is_file()})
    archive = out.with_suffix('.zip')
    with ZipFile(archive, 'w', ZIP_DEFLATED) as package:
        for p in out.iterdir():
            if p.is_file():
                package.write(p, arcname=p.name)
    Path('/content/portshield-diagnostic-latest.txt').write_text(str(archive), encoding='utf-8')
    print(f'Diagnostic completed. ZIP: {archive}', flush=True)


if __name__ == '__main__':
    main()
