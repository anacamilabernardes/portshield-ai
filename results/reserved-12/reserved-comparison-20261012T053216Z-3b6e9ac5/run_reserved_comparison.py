import collections, gc, hashlib, importlib.metadata, inspect, json, os, shutil, sys, time, uuid
from datetime import datetime, timezone
from pathlib import Path
import torch
from portshield_ai.inference import HFClient
from portshield_ai.schema import EventAnalysis, EventRecord
from portshield_ai.prompts import messages
from portshield_ai.evaluation import score

ROOT = Path('/content/portshield-ai')
DATA = Path('/content/reserved-evaluation-input')
def sha(p):
    h=hashlib.sha256()
    with p.open('rb') as f:
        for block in iter(lambda:f.read(8*1024*1024), b''): h.update(block)
    return h.hexdigest()
def dump(p, value): p.write_text(json.dumps(value,indent=2,ensure_ascii=False)+'\n',encoding='utf-8')
assert torch.cuda.is_available(), 'GPU required for this frozen comparison'
rows=[json.loads(x) for x in (DATA/'records.jsonl').read_text().splitlines()]
assert len(rows)==12 and len({r['id'] for r in rows})==12
assert sha(DATA/'records.jsonl')=='57b1bbf66994c827fe7cb61433092e038ce3fdf16b8ba3b6f5306a8ae61839b0'
for r in rows: EventRecord.model_validate(r)
base=ROOT/'models/base'; adapter=ROOT/'models/adapter'
assert sha(adapter/'adapter_model.safetensors')=='32fbfa11cb627c4444df25a1d5087805bc1ba2a67837b62e89ac1568bb56a0b9', 'Unexpected adapter weights'
assert sha(base/'model.safetensors')=='dd924a11b4c220f385b51ffa522daea7c9f3d850e31b162bb5661df483c6d3ee', 'Unexpected base weights'
run=datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8]
out=ROOT/'results/runs'/('reserved-comparison-'+run); out.mkdir(parents=True,exist_ok=False)
shutil.copy2(__file__,out/'run_reserved_comparison.py')
shutil.copytree(DATA,out/'evaluation-input')
fields=list(EventAnalysis.model_fields)
meta={'run_id':run,'status':'running','started_at_utc':datetime.now(timezone.utc).isoformat(),
 'dataset_commit':'7bfd2b4f2839522d1d9505e22c10f3a98bfefb18','n':12,'order':['base','adapter'],
 'model':'Qwen/Qwen2.5-1.5B-Instruct','revision':'989aa7980e4cf806f80c7fef2b1adb7bc71aa306',
 'generation_overrides':{'do_sample':False,'max_new_tokens':256},'four_bit':False,'seed':42,
 'gpu':torch.cuda.get_device_name(0),'python':sys.version,
 'packages':{p:importlib.metadata.version(p) for p in ['torch','transformers','peft','accelerate','pydantic']},
 'artifact_hashes':{str(p.relative_to(ROOT)):sha(p) for folder in [base,adapter] for p in folder.iterdir() if p.is_file()},
 'code_hashes':{n:sha(ROOT/'src/portshield_ai'/n) for n in ['inference.py','prompts.py','schema.py','evaluation.py']},
 'decision_protocol':{'primary':['affected_function errors','road_access errors','all-field exact match'],'secondary':'all other fields, schema validity, abstention; event macro F1 complementary only','selection':'No automatic winner; document paired corrections and regressions.'},
 'limitations':'12 exposed synthetic cases, two per class; sequential paired run, not blinded or real-world validation. No training. Schema-gated metrics and separate raw-field diagnostics are both reported.'}
dump(out/'run-metadata.json',meta)
dump(out/'rendered-messages.json',[{'id':r['id'],'messages':messages(r['text'])} for r in rows])
for name in ['inference.py','prompts.py','schema.py','evaluation.py']:
    shutil.copy2(ROOT/'src/portshield_ai'/name,out/name)
results={}; metrics={}
for label,ad in [('base',None),('adapter',str(adapter))]:
    torch.manual_seed(42);torch.cuda.manual_seed_all(42)
    print('Loading',label,flush=True)
    client=HFClient(str(base),adapter=ad,four_bit=False)
    config=client.model.generation_config.to_dict()
    config.pop('_from_model_config',None)
    if label=='base': frozen=config
    else: assert config==frozen,'Generation configurations differ'
    dump(out/(label+'-generation-config.json'),config)
    records=[]
    with (out/(label+'-predictions.jsonl')).open('x',encoding='utf-8') as f:
        for row in rows:
            raw=None;obj=None;pred=None;error=None;validation=None
            start=time.perf_counter()
            try: raw=client.predict(row['text'])
            except Exception as exc: error=type(exc).__name__+': '+str(exc)
            elapsed=time.perf_counter()-start
            try:
                obj=json.loads(raw) if raw is not None else None
                pred=EventAnalysis.model_validate(obj).model_dump()
            except (ValueError,TypeError) as exc: validation=str(exc)
            correct={k:pred is not None and type(pred[k]) is type(v) and pred[k]==v for k,v in row['target'].items()}
            # Preserve usable individual fields even when another field makes the schema invalid.
            raw_correct={k:isinstance(obj,dict) and k in obj and type(obj[k]) is type(v) and obj[k]==v for k,v in row['target'].items()}
            diff={k:{'expected':v,'predicted':obj.get(k) if isinstance(obj,dict) else None,'present':isinstance(obj,dict) and k in obj} for k,v in row['target'].items() if not raw_correct[k]}
            rec={'id':row['id'],'text':row['text'],'expected':row['target'],'raw_response':raw,'parsed_json':obj,'prediction':pred,'schema_valid':pred is not None,'inference_error':error,'validation_error':validation,'seconds':elapsed,'field_correct':correct,'raw_field_correct':raw_correct,'differences':diff,'exact_match':all(correct.values())}
            records.append(rec);f.write(json.dumps(rec,ensure_ascii=False)+'\n');f.flush();os.fsync(f.fileno())
            print(label,len(records),'/12',flush=True)
    # Existing evaluator scores only fully schema-valid predictions; inference errors stay invalid.
    m=score(rows,[r['raw_response'] if r['raw_response'] is not None else '' for r in records])
    m['field_errors']={k:sum(not r['field_correct'][k] for r in records) for k in fields}
    m['raw_field_errors']={k:sum(not r['raw_field_correct'][k] for r in records) for k in fields}
    m['exact_match_count']=sum(r['exact_match'] for r in records)
    m['inference_errors']=sum(r['inference_error'] is not None for r in records)
    m['schema_invalid_count']=sum(not r['schema_valid'] for r in records)
    m['unsupported_assertions']={k:[r['id'] for r in records if r['expected'][k]=='unknown' and isinstance(r['parsed_json'],dict) and r['parsed_json'].get(k) in vals] for k,vals in {'affected_function':['cargo_handling','land_access','navigation','vessel_manoeuvring'],'road_access':['normal','restricted']}.items()}
    dump(out/(label+'-metrics.json'),m);results[label]=records;metrics[label]=m
    del client;gc.collect();torch.cuda.empty_cache()
pairs=[]
for a,b in zip(results['base'],results['adapter']):
    assert a['id']==b['id']
    state='correct_in_both' if a['exact_match'] and b['exact_match'] else 'corrected' if b['exact_match'] else 'regressed' if a['exact_match'] else 'incorrect_in_both'
    pairs.append({'id':a['id'],'category':state,'corrected_fields':[k for k in fields if not a['field_correct'][k] and b['field_correct'][k]],'regressed_fields':[k for k in fields if a['field_correct'][k] and not b['field_correct'][k]],'raw_corrected_fields':[k for k in fields if not a['raw_field_correct'][k] and b['raw_field_correct'][k]],'raw_regressed_fields':[k for k in fields if a['raw_field_correct'][k] and not b['raw_field_correct'][k]]})
comparison={'counts':dict(collections.Counter(p['category'] for p in pairs)),'records':pairs,'metrics':metrics}
dump(out/'comparison.json',comparison)
labels=['weather_disruption','land_access_disruption','equipment_failure','navigation_restriction','normal_operations','unknown']
for name,recs in results.items():
    matrix={a:{b:0 for b in labels+['INVALID']} for a in labels}
    for r in recs:matrix[r['expected']['event_type']][r['prediction']['event_type'] if r['schema_valid'] else 'INVALID']+=1
    dump(out/(name+'-event-confusion.json'),matrix)
meta.update(status='completed',completed_at_utc=datetime.now(timezone.utc).isoformat());dump(out/'run-metadata.json',meta)
dump(out/'artifact-hashes.json',{str(p.relative_to(out)):sha(p) for p in out.rglob('*') if p.is_file()})
archive=shutil.make_archive(str(out),'zip',out)
Path('/content/portshield-reserved-comparison-latest.txt').write_text(archive)
print('COMPLETED',out,flush=True)
print(json.dumps({'counts':comparison['counts'],'metrics':metrics},indent=2),flush=True)
