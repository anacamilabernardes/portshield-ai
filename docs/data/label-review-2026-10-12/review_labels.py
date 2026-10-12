import hashlib
import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parent
source = json.loads((ROOT / 'source-snapshot.json').read_text(encoding='utf-8'))
files = source['files']
manifest = json.loads(files['data/synthetic/manifest.json'])
# Manually reviewed decisions, keyed by complete narrative, not record IDs or predictions.
# Event, confirmed function, operational state, road state, equipment state, rationale.
decisions = [
 ('An unconfirmed report mentions a possible disruption.', 'unknown', 'unknown', 'unknown', 'unknown', None, 'An unconfirmed possible disruption establishes neither a function nor road conditions.'),
 ('Contradictory reports: normal operations and crane failed.', 'unknown', 'unknown', 'unknown', 'unknown', None, 'The narrative explicitly presents contradictory reports; neither impact nor equipment condition is resolved. Roads are unmentioned.'),
 ('A rumour about cargo operations has no verified status.', 'unknown', 'unknown', 'unknown', 'unknown', None, 'Cargo is mentioned only within an unverified rumor. No confirmed affected function or road condition is established.'),
 ('Crane failed and cargo handling suspended.', 'equipment_failure', 'cargo_handling', 'suspended', 'unknown', True, 'Cargo handling is explicitly suspended after crane failure. No road evidence is supplied.'),
 ('Equipment fault: cargo handling halted.', 'equipment_failure', 'cargo_handling', 'suspended', 'unknown', True, 'Cargo handling is explicitly halted with an equipment fault. No road evidence is supplied.'),
 ('Equipment failure partially restricted cargo handling.', 'equipment_failure', 'cargo_handling', 'partial_restriction', 'unknown', True, 'Restriction applies explicitly to cargo handling. It cannot be transferred to road access.'),
 ('Strong winds temporarily restricted vessel manoeuvres. Road access remains normal. No equipment failures.', 'weather_disruption', 'vessel_manoeuvring', 'partial_restriction', 'normal', False, 'Wind restricts vessel manoeuvres; separate clauses explicitly establish normal roads and no equipment failures.'),
 ('A storm caused partial restriction of vessel manoeuvring. Road access remains normal. No equipment failures.', 'weather_disruption', 'vessel_manoeuvring', 'partial_restriction', 'normal', False, 'The storm and manoeuvring impact are explicit; roads and absence of equipment failures have their own evidence.'),
 ('Gale conditions partially restricted vessel manoeuvring. Road access remains normal. No equipment failures.', 'weather_disruption', 'vessel_manoeuvring', 'partial_restriction', 'normal', False, 'Gale conditions affect manoeuvring. Explicit independent clauses support normal roads and no equipment failures.'),
 ('Road access is blocked; land access operations suspended.', 'land_access_disruption', 'land_access', 'suspended', 'restricted', None, 'Blocked roads and suspended land access are explicit. Equipment condition is not stated.'),
 ('Road restricted with land access partially restricted.', 'land_access_disruption', 'land_access', 'partial_restriction', 'restricted', None, 'Both road and land-access restrictions are explicitly stated. Equipment condition is not stated.'),
 ('Rail closure: land access operations suspended; road access restricted.', 'land_access_disruption', 'land_access', 'suspended', 'restricted', None, 'Road restriction has an explicit clause; it is not inferred from rail closure. Equipment condition is unstated.'),
 ('Channel restriction partially restricted navigation. Road access remains normal. No equipment failures.', 'navigation_restriction', 'navigation', 'partial_restriction', 'normal', False, 'Navigation restriction is explicit. Separate road and equipment statements justify their labels.'),
 ('Navigation restriction: navigation suspended. Road access remains normal. No equipment failures.', 'navigation_restriction', 'navigation', 'suspended', 'normal', False, 'Navigation is explicitly suspended. Roads remain normal and equipment failure is explicitly excluded.'),
 ('Restricted draft partially restricted navigation. Road access remains normal. No equipment failures.', 'navigation_restriction', 'navigation', 'partial_restriction', 'normal', False, 'Draft restriction affects navigation. Normal road access and no equipment failures are explicitly stated.'),
 ('Normal operations. Road access normal. No equipment failure.', 'normal_operations', 'none', 'normal', 'normal', False, 'Normal operations, normal roads and absence of equipment failure are explicit.'),
 ('All operations normal. Road access remains normal. No crane failures.', 'normal_operations', 'none', 'normal', 'normal', False, 'All operations and roads are explicitly normal; no crane failures supplies the relevant equipment exclusion in this synthetic scope.'),
 ('Operations remain normal. Road access is normal. No equipment failures.', 'normal_operations', 'none', 'normal', 'normal', False, 'Operations, roads and equipment condition each have explicit evidence.'),
]
reviewed = {}
for text, event, function, status, roads, equipment, rationale in decisions:
    reviewed[text] = ({'event_type': event, 'affected_function': function,
        'operational_status': status, 'road_access': roads, 'equipment_failure': equipment,
        'information_sufficiency': 'insufficient' if event == 'unknown' else 'sufficient',
        'human_review_required': True}, rationale)
assert len(reviewed) == 18
records, groups, hashes = [], {}, {}
for split in ('train', 'validation', 'test'):
    path = f'data/synthetic/{split}.jsonl'
    raw = files[path].encode('utf-8')
    sha = hashlib.sha256(raw).hexdigest()
    assert sha == manifest['files'][split]['sha256'], path
    hashes[path] = sha
    rows = [json.loads(line) for line in raw.splitlines()]
    assert len(rows) == manifest['files'][split]['rows'] == 240
    for row in rows:
        body = re.sub(r'^Fictional exercise [0-9a-f]{10}: ', '', row['text'])
        target, rationale = reviewed[body]
        differences = {key: {'before': row['target'].get(key), 'after': value}
                       for key, value in target.items() if row['target'].get(key) != value}
        assert set(row['target']) == set(target)
        records.append({'id': row['id'], 'split': split, 'template_family': row['template_family'],
            'text': row['text'], 'original_target': row['target'], 'reviewed_target': target,
            'changes': differences, 'rationale': rationale, 'review_status': 'assistant_review_only'})
        key = (split, row['template_family'])
        group = groups.setdefault(key, {'text': body, 'target': target, 'rationale': rationale, 'count': 0})
        assert group['text'] == body and group['target'] == target
        group['count'] += 1
assert len(records) == 720 and len({r['id'] for r in records}) == 720
assert len(groups) == 18 and all(g['count'] == 40 for g in groups.values())
changed = [r for r in records if r['changes']]
summary = {'source_commit': source['commit'], 'review_date': '2026-10-12',
    'records_reviewed': len(records), 'distinct_bodies': len(groups),
    'changed_records': len(changed), 'changed_fields': sum(len(r['changes']) for r in records),
    'source_sha256': hashes, 'changes': changed,
    'status': 'Assistant review complete; independent domain annotation review remains pending.'}
(ROOT / 'label-review-records.jsonl').write_bytes((''.join(json.dumps(r, ensure_ascii=False) + '\n' for r in records)).encode('utf-8'))
(ROOT / 'label-review-summary.json').write_bytes((json.dumps(summary, indent=2) + '\n').encode('utf-8'))
lines = ['# Existing-label review: rumor versus impact and field-specific evidence', '',
    'Review date: 2026-10-12. Source commit: `' + source['commit'] + '`.', '',
    '## Outcome', '',
    f'Reviewed 720 records across train, validation and test (240 each), covering all 18 distinct scenario bodies. **{len(changed)} records require label changes under this review.** All seven stored target fields were compared with narrative-based decisions. The two priority fields are `affected_function` and `road_access`.', '',
    'The expected labels already distinguish rumor from confirmed impact and do not transfer cargo restrictions to roads. The observed diagnostic failures are prediction-versus-target errors; these findings do not justify relabeling the targets to match model outputs.', '',
    '## Rules applied', '',
    '- A function mentioned only in rumor or unresolved contradictory reports is not a confirmed affected function: use `unknown`.',
    '- Assign a specific affected function only when the text establishes actual impact; explicitly normal operations support `none`.',
    '- Road access requires its own evidence. Cargo or navigation restrictions alone leave road access `unknown`.',
    '- Preserve other independently supported fields. A missing road condition does not erase confirmed cargo impact.',
    '- Equipment failure is `false` only with explicit exclusion, and `null` when unreported or unresolved. Human review remains required by policy.', '',
    '## Review of all narrative families', '',
    '| Split / family | Rows | Affected function retained | Road access retained | Rationale |',
    '| --- | ---: | --- | --- | --- |']
for (split, family), g in sorted(groups.items()):
    lines.append(f"| {split} / {family} | {g['count']} | {g['target']['affected_function']} | {g['target']['road_access']} | {g['rationale']} |")
lines += ['', '## Priority cases and coverage gaps', '',
    '- Test rumor: "A rumour about cargo operations has no verified status." All 40 labels already use `affected_function=unknown`, `operational_status=unknown`, `road_access=unknown`, and `equipment_failure=null`.',
    '- Test cargo restriction: "Equipment failure partially restricted cargo handling." All 40 labels already use `affected_function=cargo_handling`, `operational_status=partial_restriction`, and `road_access=unknown`.',
    '- The three equipment-failure families all leave roads unknown: 120 records total. Road restrictions occur only where roads are explicitly restricted or blocked.',
    '- The rumor explicitly mentioning cargo appears only in test. Training uses a generic unconfirmed report and has no matched rumor/confirmed-impact contrast for the same activity.',
    '- The equipment family always has unknown roads; the current set lacks matched cargo-impact cases with independently normal or restricted roads. Repeating labels is not equivalent to teaching these distinctions across varied evidence.', '',
    '## Change log and preservation', '',
    'No label changes were applied. No dataset regeneration, training, model-selection change or historical-result rewrite was performed. Source hashes match the published dataset manifest. Prefix-bearing and no-prefix diagnostic targets remain frozen.', '',
    'See [record-level review](label-review-records.jsonl) for every input, original and reviewed target, explicit change map and rationale. See [summary and source hashes](label-review-summary.json). The [source snapshot](source-snapshot.json) also preserves the fetched policy and generator at the reviewed commit.', '',
    '## Limits and next work', '',
    'This is an assistant review against the stated policy, not independent domain-expert adjudication. There are 18 authored bodies, not 720 independent situations. In particular, the validation contradiction is explicitly designated contradictory and remains unresolved; future examples should identify evidence provenance more precisely. The validation normal-operations family excludes crane failures; broader equipment taxonomy should be clarified in a future dataset rather than silently changing historical targets.', '',
    'Before further training, add separately versioned contrastive training examples and obtain independent annotation review. Keep the already inspected test cases as diagnostics. Reserve newly authored independent cases for final evaluation, and assess all-field exact match, per-field errors, unsupported assertions and abstention alongside event F1.', '']
(ROOT / 'label-review.md').write_bytes('\n'.join(lines).encode('utf-8'))
print(json.dumps(summary, indent=2))
