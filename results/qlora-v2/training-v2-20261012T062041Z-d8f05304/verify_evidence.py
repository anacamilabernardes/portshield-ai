import hashlib,json
from pathlib import Path

p=Path(__file__).resolve().parent/'results/training-v2-20261012T062041Z-d8f05304'
c=json.loads((p/'comparison.json').read_text())
count=0
for role in ['validation','diagnostic']:
    inputs={r['id']:r for r in map(json.loads,(p/'input'/f'{role}.jsonl').read_text().splitlines())}
    records={}
    for label in ['current','v2']:
        rs=[json.loads(s) for s in (p/f'{label}-{role}-predictions.jsonl').read_text().splitlines()]
        assert len(rs)==12 and len({r['id'] for r in rs})==12
        records[label]=rs
        for r in rs:
            assert r['text']==inputs[r['id']]['text'] and r['expected']==inputs[r['id']]['target']
            obj=json.loads(r['raw_response']);assert obj==r['parsed_json']
            flags={k:isinstance(obj,dict) and k in obj and type(obj[k]) is type(v) and obj[k]==v for k,v in r['expected'].items()}
            assert flags==r['raw_field_correct']
            assert set(r['differences'])=={k for k,v in flags.items() if not v}
            assert r['exact_match']==(r['schema_valid'] and all(flags.values()))
            count+=1
        m=c[role][label]
        assert m['exact_match_count']==sum(r['exact_match'] for r in rs)
        assert m['raw_field_errors']=={k:sum(not r['raw_field_correct'][k] for r in rs) for k in rs[0]['expected']}
        assert m['schema_invalid_count']==sum(not r['schema_valid'] for r in rs)
        assert m['inference_errors']==0
    for a,b,pair in zip(records['current'],records['v2'],c[role]['pairs']):
        assert a['id']==b['id']==pair['id']
        assert pair['raw_corrected_fields']==[k for k in a['expected'] if not a['raw_field_correct'][k] and b['raw_field_correct'][k]]
        assert pair['raw_regressed_fields']==[k for k in a['expected'] if a['raw_field_correct'][k] and not b['raw_field_correct'][k]]
original=json.loads((p/'artifact-hashes.json').read_text())
verified=[]
for n,h in original.items():
    if n.startswith('adapter/') or n=='comparison-console.log':continue
    assert (p/n).exists(),n
    assert hashlib.sha256((p/n).read_bytes()).hexdigest()==h,n
    verified.append(n)
report={'status':'passed','individual_responses_rechecked':count,'paired_cases_rechecked':24,'original_manifest_matches':len(verified),'console_log_note':'Final console output continues after original manifest was written; final hash separately checked against Colab.','adapter_weights_local_backup_confirmed':json.loads((p/'backup-verification.json').read_text())['zip_crc_check']=='passed','backup_evidence':'backup-verification.json'}
(p/'local-verification.json').write_text(json.dumps(report,indent=2)+'\n',encoding='utf-8')
print(json.dumps(report,indent=2))
