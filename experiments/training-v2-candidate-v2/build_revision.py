"""Versioned family-level revision; no training and no historical file edits."""
from pathlib import Path
from collections import Counter
from itertools import combinations
import hashlib
import importlib.util
import json
import re
import sys
from zipfile import ZipFile, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'data/training-v2-candidate-v2'
FIELDS=['event_type','affected_function','operational_status','road_access','equipment_failure','information_sufficiency','human_review_required']
def dump(p,x):p.write_bytes((json.dumps(x,indent=2,ensure_ascii=False)+'\n').encode())
def jsonl(p,x):p.write_bytes((''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in x)).encode())
def read(p):return [json.loads(l) for l in p.read_text(encoding='utf-8').splitlines() if l.strip()]
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def t(ev,fn,st,rd,eq):return dict(zip(FIELDS,[ev,fn,st,rd,eq,'insufficient' if ev=='unknown' else 'sufficient',True]))

# Broader families consolidate sibling contrasts, not just individual minimal pairs.
FAMILIES={
 'weather_claim_verification':['r01','r05'],
 'mechanical_claim_verification':['r02','r06'],
 'unresolved_cargo_claim':['r03','r04'],
 'confirmed_cargo_fault':['a01','a05','s01','s04'],
 'weather_cargo_road_scope':['a02'],
 'navigation_restriction_scope':['a03','a04','a06','s02','s05'],
 'global_normal_operation':['e01','e04','e06'],
 'weather_manoeuvre_equipment_scope':['e02','e05'],
 'road_access_disruption':['e03','s03','s06'],
}
NEW=[
 ('weather_current_bulletin',
  'The 06:00 bulletin attributed a halt in vessel docking to a tug fault. At 07:00 the duty officer withdrew that attribution: inspection found the tug sound, and instrument readings confirmed a lightning exclusion remains the sole reason docking is stopped. Classify the situation at 07:00. Road access is not covered.',
  t('weather_disruption','vessel_manoeuvring','suspended','unknown',False),
  'Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence.'),
 ('weather_current_bulletin',
  'The 06:00 bulletin attributed a halt in vessel docking to a tug fault. At 07:00 the duty officer withdrew that attribution: inspection found the tug sound, and instrument readings confirmed a lightning exclusion remains the sole reason docking is stopped. Classify the situation at 07:00. A separate 07:00 access check reports the approach roads open without limits.',
  t('weather_disruption','vessel_manoeuvring','suspended','normal',False),
  'The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded.'),
 ('rail_only_land_disruption',
  'The terminal receives freight by rail and road. A rail operator has confirmed a track occupation by a stalled external train, stopping all terminal rail arrivals; no terminal equipment defect has been assessed. This rail-access incident is the primary event. The dispatcher confirms road vehicles still enter without limits.',
  t('land_access_disruption','land_access','suspended','normal',None),
  'The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault.'),
 ('rail_only_land_disruption',
  'The terminal receives freight by rail and road. A rail operator has confirmed a track occupation by a stalled external train, stopping all terminal rail arrivals; no terminal equipment defect has been assessed. This rail-access incident is the primary event. The dispatcher provides no current road-access information.',
  t('land_access_disruption','land_access','suspended','unknown',None),
  'The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred.'),
 ('tug_fault_primary_vs_cargo',
  'The assessment concerns vessel manoeuvring, not the terminal cargo line. A tug engineer verified a steering-actuator failure, and the pilot confirms all assisted vessel turns are stopped. Cargo unloading continues normally. No road-access assessment is available.',
  t('equipment_failure','vessel_manoeuvring','suspended','unknown',True),
  'Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed.'),
 ('tug_fault_primary_vs_cargo',
  'The assessment concerns vessel manoeuvring, not the terminal cargo line. A tug engineer verified a steering-actuator failure, and the pilot confirms assisted vessel turns continue at reduced capacity using a spare tug. Cargo unloading continues normally. No road-access assessment is available.',
  t('equipment_failure','vessel_manoeuvring','partial_restriction','unknown',True),
  'The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate.'),
 ('navigation_lifted_order',
  'An earlier notice stopped all ships at the river crossing. The current signed order lifts the total stop and permits only vessels below the published air-draft limit to pass under the fixed bridge. Passage has resumed for eligible vessels. The bridge has no reported malfunction, but no equipment inspection was performed. Road conditions are not supplied.',
  t('navigation_restriction','navigation','partial_restriction','unknown',None),
  'The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false.'),
 ('navigation_lifted_order',
  'An earlier notice stopped all ships at the river crossing. The current signed order lifts the total stop and permits only vessels below the published air-draft limit to pass under the fixed bridge. Passage has resumed for eligible vessels. A technical inspection explicitly ruled out equipment failures relevant to this event. Road conditions are not supplied.',
  t('navigation_restriction','navigation','partial_restriction','unknown',False),
  'Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown.'),
 ('normal_after_recovery',
  'Yesterday a sorter breakdown halted cargo processing. The current shift report confirms the repair is complete, all terminal services have returned to normal, and a post-repair inspection found no remaining equipment failures. Classify current conditions, not the historical outage. Road access is not described.',
  t('normal_operations','none','normal','unknown',False),
  'Current recovery supersedes yesterday\'s failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported.'),
 ('normal_after_recovery',
  'Yesterday a sorter breakdown halted cargo processing. The current shift report confirms all terminal services have returned to normal using a replacement processing line. The condition of the original sorter has not been checked. Classify current conditions, not the historical outage. Road access is not described.',
  t('normal_operations','none','normal','unknown',None),
  'Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown.'),
 ('conflicting_current_sources',
  'Two equally current authorized reports disagree: the dispatch log says cargo weighing is stopped, while the weighing supervisor says it is running at full capacity. No reconciliation or cause assessment is available. A separate access inspector confirms normal roads.',
  t('unknown','unknown','unknown','normal',None),
  'Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available.'),
 ('conflicting_current_sources',
  'Two equally current authorized reports disagree: the dispatch log says cargo weighing is stopped, while the weighing supervisor says it is running at full capacity. No reconciliation or cause assessment is available. A separate access inspector confirms restricted road access. Classify the disputed cargo report as the primary subject; the road check is a separate field observation.',
  t('unknown','unknown','unknown','restricted',None),
  'The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case.'),
]

def main():
 OUT.mkdir(parents=True,exist_ok=True)
 old=read(ROOT/'source/original-records.jsonl'); oldann={a['id']:a for a in read(ROOT/'source/annotations.jsonl')}
 groupmap={g:f for f,gs in FAMILIES.items() for g in gs}
 train=[];review=[];changes=[]
 for item in old:
  r=item['record']; g=r['template_family']; new=dict(r,template_family=groupmap[g]);train.append(new)
  a=oldann[r['id']]
  checks={k:{'previous':v,'reviewed':v,'decision':'retain','rationale':a['field_rationales'][k]} for k,v in r['target'].items()}
  review.append({'id':r['id'],'split':'train','family':new['template_family'],'field_review':checks,'reviewer':'assistant','independent_review':False})
  changes.append({'id':r['id'],'old_split':item['original_split'],'new_split':'train','old_family':g,'new_family':new['template_family'],'text_changed':False,'labels_changed':False})
 val=[]
 for i,(family,text,target,note) in enumerate(NEW,1):
  r={'id':f'SYN-V2R-{i:04d}','template_family':family,'facility_id':'SYNTH-PORT-9101','data_class':'synthetic','text':text,'target':target};val.append(r)
  review.append({'id':r['id'],'split':'validation','family':family,'reviewer':'assistant','independent_review':False,'field_review':{k:{'previous':None,'reviewed':v,'decision':'new_annotation','rationale':('Human review is mandatory under project policy.' if k=='human_review_required' else ('Event type remains unresolved; other independent fields can still be used.' if v=='insufficient' else 'Event type is supported; missing secondary fields do not negate this.' ) if k=='information_sufficiency' else note)} for k,v in target.items()}})
 jsonl(OUT/'train.jsonl',train);jsonl(OUT/'validation.jsonl',val);jsonl(OUT/'field-review.jsonl',review);jsonl(OUT/'split-changes.jsonl',changes)
 dump(OUT/'family-map.json',{'train':FAMILIES,'validation':{f:[r['id'] for r in val if r['template_family']==f] for f in sorted({r['template_family'] for r in val})}})
 deps=ROOT.parent/'tmp/portshield-testdeps'
 if deps.exists():sys.path.insert(0,str(deps))
 spec=importlib.util.spec_from_file_location('snapshot',ROOT/'schema_snapshot.py');mod=importlib.util.module_from_spec(spec);spec.loader.exec_module(mod)
 for r in train+val:mod.EventRecord.model_validate(r)
 assert len(train)==54 and len(val)==12
 assert not {r['template_family'] for r in train}&{r['template_family'] for r in val}
 assert len({r['id'] for r in train+val})==66
 norm=lambda s:re.sub(r'\s+',' ',s.casefold()).strip()
 assert len({norm(r['text']) for r in train+val})==66
 assert all(new['text']==o['record']['text'] and new['target']==o['record']['target'] for new,o in zip(train,old))
 assert all(set(r['field_review'])==set(FIELDS) for r in review)
 byid={r['id']:r for r in train}
 for g in json.loads((ROOT/'source/contrast-groups.json').read_text()):
  members=[byid[i] for i in g['ids']]
  assert len({r['template_family'] for r in members})==1
  varied={k for k in FIELDS if len({json.dumps(r['target'][k]) for r in members})>1}
  assert varied<=set(g['allowed_changed_fields'])
 for pair,expected in zip([val[i:i+2] for i in range(0,12,2)],[{'road_access'},{'road_access'},{'operational_status'},{'equipment_failure'},{'equipment_failure'},{'road_access'}]):
  assert pair[0]['template_family']==pair[1]['template_family']
  assert {k for k in FIELDS if pair[0]['target'][k]!=pair[1]['target'][k]}==expected
 assert all(r['target']['event_type']!='suspended' and r['target']['human_review_required'] is True for r in train+val)
 assert {r['target']['event_type'] for r in train}=={r['target']['event_type'] for r in val}
 # Lexical screening is only a supporting check, not the definition of a family.
 tokens=lambda s:set(re.findall(r'[a-z]+',s.lower()))
 ranked=sorted([{'train_id':a['id'],'validation_id':b['id'],'token_jaccard':len(tokens(a['text'])&tokens(b['text']))/len(tokens(a['text'])|tokens(b['text']))} for a in train for b in val],key=lambda x:x['token_jaccard'],reverse=True)
 dump(OUT/'cross-split-similarity.json',{'method':'set-of-word Jaccard; no threshold proves semantic independence','top_pairs':ranked[:20]})
 # Re-check previously inspected material when available; retain source hashes.
 excluded=[];sources=[]
 for p in [ROOT.parent/'evaluation-reserve/github-publication/records.jsonl',ROOT.parent/'contrastive-examples/examples.jsonl']+[ROOT.parent/'src/p/data/synthetic'/f'{s}.jsonl' for s in ['train','validation','test']]:
  if p.exists():
   rs=read(p);excluded += [norm(re.sub(r'^Fictional exercise [^:]+:\s*','',r['text'])) for r in rs];sources.append({'path':str(p.relative_to(ROOT.parent)),'sha256':sha(p),'n':len(rs)})
 assert not {norm(r['text']) for r in train+val}&set(excluded)
 stats={'records':66,'field_decisions':462,'existing_records_reviewed':54,'existing_field_decisions':378,'existing_label_changes':0,'old_validation_rows_moved_to_train':18,'new_validation_rows':12,'train_families':9,'validation_families':6,'shared_families':0,'duplicate_texts':0,'excluded_sources':sources,'exact_overlap_with_available_exclusions':0 if excluded else None,'semantic_independence_proven':False,'independent_human_review_completed':False,'class_counts':{s:dict(Counter(r['target']['event_type'] for r in rs)) for s,rs in [('train',train),('validation',val)]}}
 dump(OUT/'validation-report.json',stats)
 lines=['# Full field and family review','','Assistant review; new split and 12 new labels have not been reviewed by the user.','']
 for r,a in zip(train+val,review):
  lines += [f"## {r['id']} — {a['split']} / {a['family']}",'',r['text'],'','| Field | Reviewed value | Rationale |','|---|---|---|']
  lines += [f"| {k} | `{json.dumps(v)}` | {a['field_review'][k]['rationale']} |" for k,v in r['target'].items()];lines.append('')
 (ROOT/'REVIEW.md').write_bytes(('\n'.join(lines)+'\n').encode())
 files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='manifest.json']
 dump(ROOT/'manifest.json',{'version':'training-v2-candidate-v2','parent_version':'training-v2-candidate-v1','parent_commit':'ab3e80cc1931daef1c7334c430dc0fbc76f20e98','status':'assistant_reviewed_new_split_and_new_validation_pending_user_review','trained':False,'files':{str(p.relative_to(ROOT)).replace('\\','/'):sha(p) for p in files}})
 archive=ROOT.parent/'portshield-training-v2-candidate-v2.zip'
 with ZipFile(archive,'w',ZIP_DEFLATED) as z:
  for p in files+[ROOT/'manifest.json']:z.write(p,arcname='training-v2-candidate-v2/'+p.relative_to(ROOT).as_posix())
 with ZipFile(archive) as z:
  assert z.testzip() is None
  for p in files:assert hashlib.sha256(z.read('training-v2-candidate-v2/'+p.relative_to(ROOT).as_posix())).hexdigest()==sha(p)
 print(json.dumps(stats,indent=2));print(archive)

if __name__=='__main__':main()
