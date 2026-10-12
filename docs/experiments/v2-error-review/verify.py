import hashlib,json,sys
from pathlib import Path
from pydantic import ValidationError
p=Path(__file__).resolve().parent
sys.path.insert(0,str(p/'evidence'))
from schema import EventAnalysis
for name,h in json.loads((p/'source-hashes.json').read_text()).items():
    assert hashlib.sha256((p/'evidence'/name).read_bytes()).hexdigest()==h,name
audit=[json.loads(s) for s in (p/'annotation-review.jsonl').read_text().splitlines()]
assert len(audit)==78 and sum(len(r['field_review']) for r in audit)==546
for role in ['train','validation','diagnostic']:
    records={r['id']:r for r in map(json.loads,(p/'evidence'/f'{role}.jsonl').read_text().splitlines())}
    for r in [x for x in audit if x['role']==role]:
        assert r['text']==records[r['id']]['text'] and r['expected']==records[r['id']]['target']
        EventAnalysis.model_validate(r['expected'])
        assert not r['label_changes']
metrics=json.loads((p/'metrics-recount.json').read_text());errors=[]
for role in ['validation','diagnostic']:
    for model in ['current','v2']:
        rows=list(map(json.loads,(p/'evidence'/f'{model}-{role}-predictions.jsonl').read_text().splitlines()))
        exact=invalid=0;counts={k:0 for k in rows[0]['expected']}
        for r in rows:
            obj=json.loads(r['raw_response'])
            try: EventAnalysis.model_validate(obj); valid=True
            except ValidationError: valid=False
            assert valid==r['schema_valid'];invalid+=not valid
            flags={k:k in obj and type(obj[k]) is type(v) and obj[k]==v for k,v in r['expected'].items()}
            assert flags==r['raw_field_correct'];exact+=valid and all(flags.values())
            for k,correct in flags.items():
                if not correct: counts[k]+=1;errors.append((role,model,r['id'],k))
        assert metrics[role][model]==dict(n=12,exact_match_count=exact,schema_invalid_count=invalid,raw_field_errors=counts)
ledger=list(map(json.loads,(p/'field-errors.jsonl').read_text().splitlines()))
assert sorted(errors)==sorted((r['role'],r['model'],r['id'],r['field']) for r in ledger)
assert len(errors)==84
print('PASS: 78 records, 546 retained fields, 48 response checks, 84 error entries and evidence hashes.')
