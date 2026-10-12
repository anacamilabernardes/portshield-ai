"""Validate frozen candidate files. Uses pydantic>=2; never trains a model."""
from pathlib import Path
import collections
import hashlib
import importlib.util
import json
import re
import sys

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data/training-v2-candidate-v1'
# Optional local dependency directory; normal installations use installed pydantic.
deps=ROOT.parent/'tmp/portshield-testdeps'
if deps.exists():sys.path.insert(0,str(deps))
spec=importlib.util.spec_from_file_location('frozen_schema',ROOT/'schema_snapshot.py')
schema=importlib.util.module_from_spec(spec);spec.loader.exec_module(schema)

def read(p):return [json.loads(x) for x in p.read_text(encoding='utf-8').splitlines() if x.strip()]
def normalized(s):return re.sub(r'\s+',' ',re.sub(r'^Fictional exercise [^:]+:\s*','',s)).strip().casefold()

def main():
    split={s:read(DATA/(s+'.jsonl')) for s in ['train','validation']}
    allrows=sum(split.values(),[]); byid={r['id']:r for r in allrows}
    assert len(byid)==len(allrows)==54
    assert len({normalized(r['text']) for r in allrows})==54
    assert not {r['template_family'] for r in split['train']} & {r['template_family'] for r in split['validation']}
    labels=set(schema.EventAnalysis.model_json_schema()['properties']['event_type']['enum'])
    fields=set(schema.EventAnalysis.model_fields)
    for s,rs in split.items():
        assert {r['target']['event_type'] for r in rs}==labels
        for r in rs:
            schema.EventRecord.model_validate(r)
            assert r['id'] not in r['text'] and r['template_family'] not in r['text']
            assert not r['text'].startswith('Fictional exercise ')
            assert r['target']['event_type']!='suspended'
    annotations=read(DATA/'annotations.jsonl')
    assert {a['id'] for a in annotations}==set(byid)
    splitof={r['id']:s for s,rs in split.items() for r in rs}
    for a in annotations:
        assert a['split']==splitof[a['id']]
        assert set(a['field_rationales'])==fields
        assert all(a['field_rationales'].values())
    groups=json.loads((DATA/'contrast-groups.json').read_text())
    assert len(groups)==24
    assert collections.Counter(i for g in groups for i in g['ids'])==collections.Counter(byid.keys())
    for g in groups:
        rs=[byid[i] for i in g['ids']]
        assert all(r['template_family']==g['group'] and splitof[r['id']]==g['split'] for r in rs)
        varied={k for k in fields if len({json.dumps(r['target'][k]) for r in rs})>1}
        assert varied and varied<=set(g['allowed_changed_fields'])
        if g['theme']=='verification_of_impact':
            assert rs[0]['target']['affected_function']=='unknown'
            assert rs[0]['target']['operational_status']=='unknown'
            assert rs[1]['target']['affected_function']=='cargo_handling'
        elif g['theme']=='field_specific_road_evidence':
            assert varied=={'road_access'}
            assert {r['target']['road_access'] for r in rs}=={'normal','restricted','unknown'}
        elif g['theme']=='equipment_unknown_vs_excluded':
            assert varied=={'equipment_failure'}
            assert [r['target']['equipment_failure'] for r in rs]==[None,False]
        elif g['theme']=='event_type_vs_operational_state':
            assert varied=={'operational_status'}
            assert {r['target']['operational_status'] for r in rs}=={'partial_restriction','suspended'}
    # Historical exclusions were measured when assembled; those files are not distributed here.
    excluded=[]; source_checks=[]
    sources=[ROOT.parent/'src/p/data/synthetic'/f'{s}.jsonl' for s in ['train','validation','test']]
    sources += [ROOT.parent/'contrastive-examples/examples.jsonl',ROOT.parent/'evaluation-reserve/github-publication/records.jsonl']
    for p in sources:
        if p.exists():
            rs=read(p); excluded.extend(normalized(r['text']) for r in rs)
            source_checks.append({'path':str(p.relative_to(ROOT.parent)).replace('\\','/'),'rows':len(rs),'sha256':hashlib.sha256(p.read_bytes()).hexdigest()})
    if excluded:assert not {normalized(r['text']) for r in allrows} & set(excluded)
    for p in DATA.glob('*.json*'):
        assert b'\r' not in p.read_bytes()
    report={'schema_valid_records':54,'train_records':36,'validation_records':18,'contrast_groups':24,'shared_families':0,'duplicate_texts':0,'all_seven_fields_have_rationales':True,'contrast_invariants_checked':True,'historical_sources_checked':source_checks,'exact_overlap_with_checked_sources':0 if excluded else None,'semantic_independence_proven':False,'independent_human_review_completed':False,'class_counts':{s:dict(collections.Counter(r['target']['event_type'] for r in rs)) for s,rs in split.items()}}
    (ROOT/'validation.json').write_bytes((json.dumps(report,indent=2)+'\n').encode())
    print(json.dumps(report,indent=2))

if __name__=='__main__':main()
