"""Frozen V2 pilot: preflight, fresh-base QLoRA, paired regression evaluation."""
import argparse, collections, gc, hashlib, importlib.metadata, inspect, json, os, shutil, sys, time, uuid
from pathlib import Path
from datetime import datetime, timezone

ROOT = Path('/content/portshield-ai')
HERE = Path(__file__).resolve().parent
BASE = ROOT / 'models/base'
OLD = ROOT / 'models/adapter'
OLD_HASH = '32fbfa11cb627c4444df25a1d5087805bc1ba2a67837b62e89ac1568bb56a0b9'
BASE_HASH = 'dd924a11b4c220f385b51ffa522daea7c9f3d850e31b162bb5661df483c6d3ee'

def sha(p):
    h = hashlib.sha256()
    with Path(p).open('rb') as f:
        for b in iter(lambda: f.read(8388608), b''): h.update(b)
    return h.hexdigest()

def dump(p, obj):
    Path(p).write_text(json.dumps(obj, indent=2, ensure_ascii=False) + '\n', encoding='utf-8')

def rows(name):
    return [json.loads(s) for s in (HERE / (name + '.jsonl')).read_text(encoding='utf-8').splitlines()]

def preflight(out):
    from transformers import AutoTokenizer
    from portshield_ai.schema import EventRecord
    from portshield_ai.training import encode_example
    from portshield_ai.prompts import messages
    import torch
    assert torch.cuda.is_available()
    assert sha(OLD / 'adapter_model.safetensors') == OLD_HASH
    assert sha(BASE / 'model.safetensors') == BASE_HASH
    expected = json.loads((HERE / 'input-hashes.json').read_text())
    for name, digest in expected.items(): assert sha(HERE/name) == digest, name
    sets = {k: rows(k) for k in ['train', 'validation', 'diagnostic']}
    assert [len(sets[k]) for k in sets] == [54, 12, 12]
    assert not ({r['template_family'] for r in sets['train']} & {r['template_family'] for r in sets['validation']})
    assert len({r['id'] for rs in sets.values() for r in rs}) == 78
    assert len({r['text'] for rs in sets.values() for r in rs}) == 78
    tok = AutoTokenizer.from_pretrained(BASE, local_files_only=True, trust_remote_code=False)
    audit = []
    for role, rs in sets.items():
        for r in rs:
            EventRecord.model_validate(r)
            enc = encode_example(tok, r, 2048)
            labels = enc['labels']; start = next(i for i,x in enumerate(labels) if x != -100)
            target = tok.decode(labels[start:], skip_special_tokens=True).strip()
            assert json.loads(target) == r['target'], r['id']
            assert all(x == -100 for x in labels[:start])
            assert labels[start:] == enc['input_ids'][start:]
            assert len(enc['input_ids']) <= 2048
            audit.append({'id': r['id'], 'role': role, 'tokens': len(labels), 'masked_prompt_tokens': start, 'supervised_tokens': len(labels)-start, 'target_matches': True})
    dump(out/'token-audit.json', audit)
    dump(out/'rendered-messages.json', [{'id':r['id'], 'messages':messages(r['text'])} for rs in sets.values() for r in rs])
    report = {'status':'passed','counts':{k:len(v) for k,v in sets.items()},'shared_train_validation_families':0,'exact_overlap':0,'min_tokens':min(x['tokens'] for x in audit),'max_tokens':max(x['tokens'] for x in audit),'all_assistant_targets_intact':True,'current_adapter_sha256':OLD_HASH,'base_sha256':BASE_HASH,'gpu':torch.cuda.get_device_name(0)}
    dump(out/'preflight.json',report)
    print(json.dumps(report,indent=2),flush=True)

def train(out):
    import torch
    from datasets import Dataset
    from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig, Trainer, TrainingArguments, set_seed
    from peft import LoraConfig, get_peft_model, prepare_model_for_kbit_training
    from portshield_ai.training import encode_example
    assert json.loads((out/'preflight.json').read_text())['status']=='passed'
    config = {'initialization':'fresh base, not resumed from current adapter','seed':42,'epochs':3,'learning_rate':0.0002,'rank':16,'alpha':32,'dropout':0.05,'max_length':2048,'batch_size':1,'gradient_accumulation_steps':8,'selection':'final epoch; no checkpoint selection or test tuning','dataset_commit':'9e3a16fc4b9e6861646509c7553f13eac20f7cec','validation_role':'exposed development validation','diagnostic_role':'previously evaluated 12 cases, not independent test'}
    dump(out/'training-config.json',config)
    set_seed(42)
    tok=AutoTokenizer.from_pretrained(BASE,local_files_only=True,trust_remote_code=False);tok.pad_token=tok.eos_token
    model=AutoModelForCausalLM.from_pretrained(BASE,local_files_only=True,trust_remote_code=False,torch_dtype=torch.float16,device_map={'':0},quantization_config=BitsAndBytesConfig(load_in_4bit=True,bnb_4bit_quant_type='nf4',bnb_4bit_use_double_quant=True,bnb_4bit_compute_dtype=torch.float16))
    model.config.use_cache=False
    model=prepare_model_for_kbit_training(model)
    model=get_peft_model(model,LoraConfig(task_type='CAUSAL_LM',r=16,lora_alpha=32,lora_dropout=0.05,target_modules=['q_proj','k_proj','v_proj','o_proj','gate_proj','up_proj','down_proj'],bias='none'))
    model.enable_input_require_grads()
    datasets=[Dataset.from_list([encode_example(tok,r,2048) for r in rows(k)]) for k in ['train','validation']]
    def collate(rs):
        width=max(len(r['input_ids']) for r in rs)
        return {k:torch.tensor([r[k]+[(-100 if k=='labels' else tok.pad_token_id if k=='input_ids' else 0)]*(width-len(r[k])) for r in rs]) for k in ['input_ids','attention_mask','labels']}
    args=TrainingArguments(output_dir=str(out/'checkpoints'),seed=42,num_train_epochs=3,per_device_train_batch_size=1,per_device_eval_batch_size=1,gradient_accumulation_steps=8,learning_rate=0.0002,fp16=True,gradient_checkpointing=True,gradient_checkpointing_kwargs={'use_reentrant':False},eval_strategy='epoch',save_strategy='epoch',save_total_limit=2,logging_steps=1,logging_nan_inf_filter=False,report_to='none',label_names=['labels'])
    # Transformers 4.51.3 floors the inferred update count for a partial final batch.
    # Seven updates per 54-row epoch (including the final six rows), three epochs.
    args.max_steps = 21
    config['max_steps'] = 21
    dump(out/'training-config.json', config)
    trainer=Trainer(model=model,args=args,train_dataset=datasets[0],eval_dataset=datasets[1],data_collator=collate)
    result=trainer.train()
    import math
    assert math.isfinite(result.training_loss)
    assert trainer.state.global_step == 21 and abs(trainer.state.epoch - 3.0) < 1e-6
    assert all(math.isfinite(e['loss']) for e in trainer.state.log_history if 'loss' in e)
    model.save_pretrained(out/'adapter',safe_serialization=True);tok.save_pretrained(out/'adapter')
    dump(out/'training-metrics.json',result.metrics)
    dump(out/'training-history.json',trainer.state.log_history)
    assert sha(OLD/'adapter_model.safetensors')==OLD_HASH
    dump(out/'adapter-hashes.json',{p.name:sha(p) for p in (out/'adapter').iterdir() if p.is_file()})
    print('TRAINING_COMPLETED',out/'adapter',flush=True)

def compare(out):
    import torch
    from portshield_ai.inference import HFClient
    from portshield_ai.schema import EventAnalysis
    from portshield_ai.evaluation import score
    fields=list(EventAnalysis.model_fields); results={}; summaries={}; frozen=None
    for label,adapter in [('current',OLD),('v2',out/'adapter')]:
        torch.manual_seed(42);torch.cuda.manual_seed_all(42)
        client=HFClient(str(BASE),adapter=str(adapter),four_bit=False)
        config=client.model.generation_config.to_dict()
        if frozen is None:frozen=config
        else:assert config==frozen
        dump(out/(label+'-generation-config.json'),config)
        for role in ['validation','diagnostic']:
            rs=rows(role);recs=[]
            with (out/(label+'-'+role+'-predictions.jsonl')).open('x',encoding='utf-8') as f:
                for row in rs:
                    raw=None;obj=None;pred=None;error=None;validation=None;t=time.perf_counter()
                    try:raw=client.predict(row['text'])
                    except Exception as exc:error=repr(exc)
                    try:
                        obj=json.loads(raw)
                        pred=EventAnalysis.model_validate(obj).model_dump()
                    except (ValueError,TypeError) as exc:validation=str(exc)
                    raw_correct={k:isinstance(obj,dict) and k in obj and type(obj[k]) is type(v) and obj[k]==v for k,v in row['target'].items()}
                    correct={k:pred is not None and raw_correct[k] for k in fields}
                    diffs={k:{'expected':v,'predicted':obj.get(k) if isinstance(obj,dict) else None,'present':isinstance(obj,dict) and k in obj} for k,v in row['target'].items() if not raw_correct[k]}
                    rec={'id':row['id'],'text':row['text'],'expected':row['target'],'raw_response':raw,'parsed_json':obj,'prediction':pred,'schema_valid':pred is not None,'inference_error':error,'validation_error':validation,'seconds':time.perf_counter()-t,'field_correct':correct,'raw_field_correct':raw_correct,'differences':diffs,'exact_match':all(correct.values())}
                    recs.append(rec);f.write(json.dumps(rec,ensure_ascii=False)+'\n');f.flush();os.fsync(f.fileno());print(label,role,len(recs),'/12',flush=True)
            m=score(rs,[r['raw_response'] or '' for r in recs])
            m.update(raw_field_errors={k:sum(not r['raw_field_correct'][k] for r in recs) for k in fields},field_errors={k:sum(not r['field_correct'][k] for r in recs) for k in fields},exact_match_count=sum(r['exact_match'] for r in recs),schema_invalid_count=sum(not r['schema_valid'] for r in recs),inference_errors=sum(r['inference_error'] is not None for r in recs))
            results[label,role]=recs;summaries[label,role]=m;dump(out/(label+'-'+role+'-metrics.json'),m)
            confusion={k:dict(collections.Counter(json.dumps([r['expected'][k],r['parsed_json'].get(k,'MISSING') if isinstance(r['parsed_json'],dict) else 'INVALID']) for r in recs)) for k in fields}
            dump(out/(label+'-'+role+'-confusion.json'),confusion)
        del client;gc.collect();torch.cuda.empty_cache()
    comparison={}
    for role in ['validation','diagnostic']:
        pairs=[]
        for a,b in zip(results['current',role],results['v2',role]):
            assert a['id']==b['id']
            pairs.append({'id':a['id'],'old_exact':a['exact_match'],'new_exact':b['exact_match'],'raw_corrected_fields':[k for k in fields if not a['raw_field_correct'][k] and b['raw_field_correct'][k]],'raw_regressed_fields':[k for k in fields if a['raw_field_correct'][k] and not b['raw_field_correct'][k]]})
        comparison[role]={'current':summaries['current',role],'v2':summaries['v2',role],'pairs':pairs}
    dump(out/'comparison.json',comparison)
    assert sha(OLD/'adapter_model.safetensors')==OLD_HASH
    dump(out/'artifact-hashes.json',{str(p.relative_to(out)):sha(p) for p in out.rglob('*') if p.is_file() and 'checkpoints' not in p.parts})
    print('COMPARISON_COMPLETED',out,flush=True)
    print(json.dumps({role:{name:{k:m[k] for k in ['exact_match_count','raw_field_errors','schema_invalid_count']} for name,m in comparison[role].items() if name!='pairs'} for role in comparison},indent=2),flush=True)

if __name__=='__main__':
    a=argparse.ArgumentParser();a.add_argument('stage',choices=['preflight','train','compare']);a.add_argument('--run');opts=a.parse_args()
    if opts.stage=='preflight':
        out=ROOT/'results/runs'/('training-v2-'+datetime.now(timezone.utc).strftime('%Y%m%dT%H%M%SZ')+'-'+uuid.uuid4().hex[:8]);out.mkdir(parents=True,exist_ok=False)
        shutil.copytree(HERE,out/'input')
        Path('/content/training-v2-latest.txt').write_text(str(out))
        import portshield_ai.training, portshield_ai.inference, portshield_ai.prompts, portshield_ai.schema, portshield_ai.evaluation
        for module in [portshield_ai.training,portshield_ai.inference,portshield_ai.prompts,portshield_ai.schema,portshield_ai.evaluation]:shutil.copy2(inspect.getfile(module),out/(module.__name__.split('.')[-1]+'.py'))
        dump(out/'environment.json',{'python':sys.version,'packages':{k:importlib.metadata.version(k) for k in ['torch','transformers','peft','bitsandbytes','accelerate','datasets','pydantic']}})
    else:out=Path(opts.run or Path('/content/training-v2-latest.txt').read_text())
    print('RUN',out,flush=True)
    globals()[opts.stage](out)
