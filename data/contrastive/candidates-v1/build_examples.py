import hashlib
import json
from pathlib import Path

OUT = Path(__file__).resolve().parent
rows, notes, groups = [], [], []
FIELDS = ('event_type', 'affected_function', 'operational_status', 'road_access',
          'equipment_failure', 'information_sufficiency', 'human_review_required')

def add(group, text, event, function, status, road, equipment, evidence):
    target = dict(zip(FIELDS, (event, function, status, road, equipment,
        'insufficient' if event == 'unknown' else 'sufficient', True)))
    row_id = f'SYN-CONTRAST-{len(rows)+1:04d}'
    rows.append({'id': row_id, 'template_family': group, 'facility_id': 'SYNTH-PORT-9001',
                 'data_class': 'synthetic', 'text': text, 'target': target})
    evidence['information_sufficiency'] = ('The event type is unresolved; known impact fields remain populated.'
        if event == 'unknown' else 'The primary event type is explicitly established; roads may still be unknown.')
    evidence['human_review_required'] = 'Always true under the research annotation policy.'
    assert set(evidence) == set(FIELDS)
    notes.append({'id': row_id, 'group': group, 'evidence_and_rationale': evidence,
        'review_status': 'assistant_authored_pending_independent_review'})
    return row_id

def pair(group, rumor, confirmed, event, status, equipment, road='unknown'):
    ids = []
    for confirmed_flag, text in ((False, rumor), (True, confirmed)):
        ev = event if confirmed_flag else 'unknown'
        ids.append(add(group, text, ev, 'cargo_handling' if confirmed_flag else 'unknown',
            status if confirmed_flag else 'unknown', road, equipment if confirmed_flag else None,
            {'event_type': ('The report confirms the cause.' if event != 'unknown' else 'The cause remains unverified.') if confirmed_flag else 'The alleged event is explicitly unverified.',
             'affected_function': 'Cargo impact is confirmed.' if confirmed_flag else 'Cargo is mentioned only as an unverified claim.',
             'operational_status': 'The stated cargo impact is confirmed.' if confirmed_flag else 'No confirmed cargo operational state is provided.',
             'road_access': 'A separate verified statement establishes normal roads.' if road == 'normal' else 'No road condition is reported.',
             'equipment_failure': ('A fault is confirmed.' if equipment is True else 'Equipment condition is not established.') if confirmed_flag else 'An unverified fault or disruption is not a confirmed failure or an explicit exclusion.'}))
    groups.append({'id': group, 'records': ids, 'contrast': 'unverified claim versus confirmed cargo impact',
        'must_remain_equal': ['road_access', 'human_review_required']})

pair('contrast-01',
    'An unverified message claims that cargo handling has stopped. The cause has not been established.',
    'The operations supervisor verified that cargo handling has stopped. The cause has not been established.',
    'unknown', 'suspended', None)
pair('contrast-02',
    'An unverified message claims that strong winds have reduced cargo handling capacity. No operational impact has been verified.',
    'The operations supervisor verified that strong winds have reduced cargo handling capacity. Cargo handling continues at reduced capacity.',
    'weather_disruption', 'partial_restriction', None)
pair('contrast-03',
    'An unverified message claims that a conveyor fault has stopped cargo handling. Separately, the access supervisor verified that road access remains normal.',
    'The maintenance supervisor verified that a conveyor fault has stopped cargo handling. Separately, the access supervisor verified that road access remains normal.',
    'equipment_failure', 'suspended', True, 'normal')

def triple(group, body, event, status, equipment):
    ids = []
    for road, clause in [('normal', ' Road access is confirmed normal.'),
                         ('restricted', ' Road access is confirmed restricted.'),
                         ('unknown', '')]:
        ids.append(add(group, body + clause, event, 'cargo_handling', status, road, equipment,
            {'event_type': 'The cargo incident and its cause are explicitly identified as primary. The road condition does not replace the primary event type.',
             'affected_function': 'The text explicitly confirms an impact on cargo handling.',
             'operational_status': 'Use the stated cargo state, independently of the road condition.',
             'road_access': 'Explicit road evidence: ' + clause.strip() if clause else 'Roads are not mentioned; retain unknown rather than copying the cargo restriction.',
             'equipment_failure': 'An equipment fault is explicitly confirmed.' if equipment else 'An inspection explicitly excludes equipment failure; weather alone would not justify false.'}))
    groups.append({'id': group, 'records': ids, 'contrast': 'normal versus restricted versus unmentioned road access',
        'must_remain_equal': [f for f in FIELDS if f != 'road_access']})

triple('contrast-04', 'A confirmed conveyor fault partially restricted cargo handling. This cargo incident is explicitly identified as the primary event.',
       'equipment_failure', 'partial_restriction', True)
triple('contrast-05', 'Strong winds partially restricted cargo handling. This weather-related cargo incident is explicitly identified as the primary event. An inspection confirmed that no equipment had failed.',
       'weather_disruption', 'partial_restriction', False)
triple('contrast-06', 'A confirmed crane motor fault suspended cargo handling completely. This cargo incident is explicitly identified as the primary event.',
       'equipment_failure', 'suspended', True)

def write(name, value):
    (OUT / name).write_bytes(value.encode('utf-8'))

write('examples.jsonl', ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in rows))
write('annotations.jsonl', ''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in notes))
write('contrast-groups.json', json.dumps(groups, indent=2) + '\n')
lines = ['# Contrastive examples for annotation review', '',
    'Status: assistant-authored synthetic development candidates; independent annotation review pending. Created 2026-10-12. Language: English.', '',
    '15 unique examples: three rumor/confirmation pairs and three road-condition triples. No examples were added to the existing splits, used for training, or treated as an independent test.', '',
    '## Contract and intended use', '',
    '- Only the `text` field is model input. IDs and group names are metadata, never prompt prefixes.',
    '- A verified cargo impact can coexist with `event_type=unknown` when its cause/type remains unresolved. Under the existing contract, `information_sufficiency=insufficient` concerns event type, not the completeness of every field.',
    '- An independent verified road statement remains usable even when a cargo allegation is unverified.',
    '- Road triples explicitly identify a primary cargo incident to avoid ambiguity in the current single-event schema. Without a stated primary event, multiple confirmed event types would require separate adjudication.',
    '- False equipment failure labels have explicit inspection evidence. Unverified or unstated condition is null.',
    '- Preserve each contrast group in a single future split to avoid near-duplicate train/test contamination. These disclosed cases are development material, not a blind holdout.',
    '- These deliberately small contrasts do not solve the diversity gap. Independently reviewed paraphrases and new scenarios remain necessary before further training.', '',
    '## Examples and targets', '']
for row in rows:
    lines += [f"### {row['id']} ({row['template_family']})", '', row['text'], '',
              '```json', json.dumps(row['target'], indent=2), '```', '']
lines += ['## Files and validation', '',
    '- [Model-compatible examples](examples.jsonl)',
    '- [Per-field annotation rationale](annotations.jsonl)',
    '- [Contrast groups and invariant fields](contrast-groups.json)',
    '- [Integrity manifest](manifest.json)', '',
    'Review every target independently before training. Evaluate all-field exact match and per-field accuracy; separately count unverified impact assertions and road restrictions inferred without evidence. Schema validity and event F1 alone do not establish success.', '']
write('README.md', '\n'.join(lines))
manifest = {'version': 'contrastive-candidates-1', 'date': '2026-10-12', 'records': len(rows),
    'contrast_groups': len(groups), 'license': 'MIT', 'data_class': 'synthetic',
    'split': 'unassigned-development-only', 'review_status': 'pending_independent_review',
    'historical_data_modified': False, 'files': {n: hashlib.sha256((OUT/n).read_bytes()).hexdigest()
        for n in ('examples.jsonl', 'annotations.jsonl', 'contrast-groups.json', 'README.md', 'build_examples.py')}}
write('manifest.json', json.dumps(manifest, indent=2) + '\n')
print(json.dumps({'records': len(rows), 'groups': len(groups)}))
