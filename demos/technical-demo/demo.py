"""Replay measured model responses and rerun the original schema and field checks."""
import hashlib
import html
import json
from pathlib import Path

from pydantic import ValidationError
from schema_snapshot import EventAnalysis

ROOT = Path(__file__).resolve().parent
SOURCE = 'https://github.com/anacamilabernardes/portshield-ai/tree/6dc029640681e7b6a3110be91257dd52c8e2eb6c/results/qlora-v2/training-v2-20261012T062041Z-d8f05304/results/training-v2-20261012T062041Z-d8f05304'


def verify():
    manifest = json.loads((ROOT / 'evidence-manifest.json').read_text())
    for name, digest in manifest.items():
        assert hashlib.sha256((ROOT / name).read_bytes()).hexdigest() == digest, name
    records = {}
    for label in ('current', 'v2'):
        rows = [json.loads(line) for line in (ROOT / 'evidence' / f'{label}-validation-predictions.jsonl').read_text().splitlines()]
        assert len(rows) == 12
        records[label] = {r['id']: r for r in rows}
        for r in rows:
            parsed = json.loads(r['raw_response'])
            assert parsed == r['parsed_json']
            try:
                EventAnalysis.model_validate(parsed)
                valid = True
            except ValidationError:
                valid = False
            assert valid == r['schema_valid'], r['id']
            flags = {k: k in parsed and type(parsed[k]) is type(v) and parsed[k] == v for k, v in r['expected'].items()}
            assert flags == r['raw_field_correct'], r['id']
            assert r['exact_match'] == (valid and all(flags.values()))
            assert r['differences'] == {k: {'expected': v, 'predicted': parsed.get(k), 'present': k in parsed} for k, v in r['expected'].items() if not flags[k]}
    for key, r in records['current'].items():
        assert r['text'] == records['v2'][key]['text']
        assert r['expected'] == records['v2'][key]['expected']
    assert records['v2']['SYN-V2R-0006']['exact_match']
    assert records['v2']['SYN-V2R-0001']['schema_valid']
    assert set(records['v2']['SYN-V2R-0001']['differences']) == {'affected_function', 'operational_status', 'equipment_failure'}
    return records


def main():
    records = verify()
    esc = html.escape
    def code(obj):
        return '<pre>' + esc(json.dumps(obj, indent=2, ensure_ascii=False)) + '</pre>'
    parts = ['''<!doctype html><html lang="en"><meta charset="utf-8"><title>PortShield AI — Evidence replay</title>
<style>body{font:17px/1.55 system-ui,sans-serif;max-width:1000px;margin:40px auto;padding:0 24px;color:#182638;background:#f7f9fc}h1,h2{color:#123b59}section{background:white;border:1px solid #ccd7e1;border-radius:12px;padding:24px;margin:24px 0}pre{background:#edf2f6;padding:16px;overflow:auto;font-size:14px}table{border-collapse:collapse;width:100%;font-size:14px}td,th{padding:10px;text-align:left;border-bottom:1px solid #ddd}.bad{background:#fff1ed}.good{background:#effaf2}a{color:#165c91}blockquote{border-left:4px solid #4485aa;padding-left:16px}.notice{background:#e7effa;padding:16px}small{overflow-wrap:anywhere}@media print{body{background:white;font-size:12px}section{break-inside:avoid}pre{white-space:pre-wrap}}</style>
<h1>PortShield AI: a short technical demonstration</h1>
<p>Ana Camila Bernardes · October 2026 · Suggested duration: 4–5 minutes</p>
<p class="notice"><strong>Recorded inference; live local verification.</strong> Inputs and raw responses come from completed Colab runs. Opening this page does not call a model. Running <code>python demo.py</code> rechecks the original Pydantic schema, field comparisons and evidence hashes. No GPU or model weights are required for this replay.</p>
<p><strong>What runs:</strong> recorded input → preserved adapter output → schema validation → strict comparison with synthetic reference labels → investigation of differences. Reference labels are available for this evaluation; they would require annotation in real use.</p>''']
    for key, heading in [('SYN-V2R-0006', '1. A fully correct recorded response'), ('SYN-V2R-0001', '2. A schema-valid response with three substantive errors')]:
        new = records['v2'][key]
        old = records['current'][key]
        parts += ['<section><h2>' + heading + '</h2>', '<p><strong>Record:</strong> ' + key + ' · V2 adapter · development validation</p>', '<h3>Input report</h3><blockquote>' + esc(new['text']) + '</blockquote>', '<h3>Structured response</h3>' + code(new['parsed_json']), '<details><summary>Original response, exactly as saved</summary><pre>' + esc(new['raw_response']) + '</pre></details>', '<h3>Validation and comparison</h3><p>JSON parsing: PASS · Original schema: PASS · All-field match: <strong>' + ('PASS' if new['exact_match'] else 'FAIL') + '</strong></p>', '<table><tr><th>Field</th><th>Expected</th><th>Existing adapter</th><th>V2 adapter</th><th>V2 check</th></tr>']
        for field, expected in new['expected'].items():
            correct = new['raw_field_correct'][field]
            parts.append('<tr class="' + ('good' if correct else 'bad') + '"><td>' + field + '</td><td>' + esc(json.dumps(expected)) + '</td><td>' + esc(json.dumps(old['parsed_json'].get(field))) + '</td><td>' + esc(json.dumps(new['parsed_json'].get(field))) + '</td><td>' + ('Correct' if correct else 'Incorrect') + '</td></tr>')
        parts.append('</table>')
        if not new['exact_match']:
            parts.append('''<h3>Investigating the error</h3><ol>
<li><strong>Scope:</strong> docking is explicitly stopped. The affected function should be <code>vessel_manoeuvring</code>, rather than <code>none</code>.</li>
<li><strong>Status:</strong> “docking is stopped” supports <code>suspended</code>. V2 returns <code>partial_restriction</code>.</li>
<li><strong>Equipment evidence:</strong> the updated inspection found the tug sound. The label is <code>false</code>; <code>null</code> would mean unknown.</li>
</ol><p>The existing adapter already got status and equipment right here. V2 corrected the event type but regressed on those two fields, while affected function remained incorrect. Schema validation accepts all these values: it cannot determine whether the narrative supports them.</p>
<p><strong>Evidence, not a causal claim:</strong> the saved text and responses establish the observed mismatches. They do not prove why the model produced them. Investigate temporal updates, field scope and explicit negation in additional reviewed development examples.</p>''')
        parts.append('<p><a href="' + SOURCE + '/v2-validation-predictions.jsonl">Published V2 responses</a> · <a href="' + SOURCE + '/current-validation-predictions.jsonl">Published existing-adapter responses</a></p></section>')
    parts.append('''<section><h2>3. Why one successful example is not enough</h2>
<p>Across all 12 validation examples, affected-function errors stayed at 8; road-access errors fell from 5 to 3; operational-status errors rose from 5 to 7; fully correct records increased from 0 to 1. The successful case above is that single V2 exact match, deliberately paired with a known failure for explanation.</p>
<p><strong>Decision: do not promote the V2 adapter.</strong> These are synthetic development cases, not an independent final test. Neither adapter has demonstrated operational readiness.</p>
<h3>Evidence trail</h3><p>The record ID connects the input, expected labels, original output and field differences. The source snapshot identifies the validation rules. The saved generation settings, training configuration and hashes identify the experiment. The local replay verifies all 24 validation responses, not just the two selected for display.</p>''')
    parts.append('<p><a href="' + SOURCE + '/REPORT.md">Full report</a> · <a href="' + SOURCE + '/training-config.json">Training configuration</a> · <a href="' + SOURCE + '/v2-generation-config.json">Generation settings</a> · <a href="evidence-manifest.json">Local evidence hashes</a></p>')
    parts.append('<p>AI assistance was used to prepare this demonstration and its verification code. Outputs shown here are preserved model responses; they have not been rewritten to improve the demonstration.</p></section></html>')
    (ROOT / 'DEMO.html').write_bytes('\n'.join(parts).encode('utf-8'))
    print('PASS: evidence hashes, original schema validation, and strict field differences for 24 responses / 12 pairs.')
    print('DEMO.html generated. This is recorded inference replay, not a live model endpoint.')


if __name__ == '__main__':
    main()
