"""Build a small, targeted synthetic training revision; no inference or training."""
from pathlib import Path
import collections
import hashlib
import json

ROOT = Path(__file__).resolve().parent
OUT = ROOT / 'data/training-v2-candidate-v1'
FIELDS = ['event_type','affected_function','operational_status','road_access','equipment_failure','information_sufficiency','human_review_required']
rows, annotations, groups = [], [], []

def target(event, function, status, road='unknown', equipment=None):
    return dict(zip(FIELDS,[event,function,status,road,equipment,'insufficient' if event=='unknown' else 'sufficient',True]))

def add(group, theme, split, variants, allowed):
    ids=[]
    for text,t,evidence in variants:
        ident=f'SYN-V2-{len(rows)+1:04d}'
        rows.append(dict(id=ident,template_family=group,facility_id='SYNTH-PORT-9100',data_class='synthetic',text=text,target=t))
        ids.append(ident)
        reasons={
          'event_type': evidence['event'],
          'affected_function': evidence['function'],
          'operational_status': evidence['status'],
          'road_access': evidence.get('road','No road or gate-access evidence; unknown is retained.'),
          'equipment_failure': evidence.get('equipment','No verified equipment assessment; absence of a fault report does not exclude a fault.'),
          'information_sufficiency': 'Event type is unresolved; other independently verified fields remain usable.' if t['event_type']=='unknown' else 'The primary event type is supported; this does not imply every field is known.',
          'human_review_required':'Required by the project policy, including normal operations.'}
        annotations.append(dict(id=ident,group=group,split=split,theme=theme,field_rationales=reasons,review_status='assistant_reviewed_independent_review_pending'))
    groups.append(dict(group=group,theme=theme,split=split,ids=ids,allowed_changed_fields=allowed))

# Each pair changes verification status while retaining a distinct physical scenario.
rumors=[
 ('r01','train','A forwarded chat alleges that lightning stopped pallet loading at the east shed. The control room has not verified the message.','The control room verified that lightning stopped pallet loading at the east shed.','weather_disruption','cargo_handling','suspended',None),
 ('r02','train','An unsigned note claims a seized gearbox has slowed sack unloading at the bagging station. Neither the fault nor the slowdown has been checked.','A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station.','equipment_failure','cargo_handling','partial_restriction',True),
 ('r03','train','A caller alleges that parcel sorting has ceased at the dispatch shed. The call remains uncorroborated and the cause is unresolved.','The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved.','unknown','cargo_handling','suspended',None),
 ('r04','train','A social post alleges that smoke from a nearby grass fire has slowed freight packing. The post has not been corroborated; its proposed cause remains unverified.','The packing supervisor confirmed slower freight packing. The proposed cause remains unverified.','unknown','cargo_handling','partial_restriction',None),
 ('r05','validation','An anonymous radio relay says hail has halted bulk-bag stacking at the inland warehouse. Operations staff cannot verify the claim.','The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse.','weather_disruption','cargo_handling','suspended',None),
 ('r06','validation','A handwritten complaint alleges a snapped drive chain has reduced carton loading at the rail shed. No inspection or operational check has corroborated it.','Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result.','equipment_failure','cargo_handling','partial_restriction',True),
]
for g,split,unverified,confirmed,ev,fun,status,eq in rumors:
    road='normal' if g in ['r02','r05'] else 'unknown'
    suffix=' Independently, the gate officer confirmed unrestricted road access.' if road=='normal' else ''
    common={'road':'The independent gate report establishes normal road access.'} if suffix else {}
    add(g,'verification_of_impact',split,[(unverified+suffix,target('unknown','unknown','unknown',road),dict(common,event='The alleged cause has not been verified.',function='Cargo activity occurs only inside the unverified claim.',status='No operational impact is verified.')),
      (confirmed+suffix,target(ev,fun,status,road,eq),dict(common,event='The cause remains unresolved.' if ev=='unknown' else confirmed,function=confirmed,status=confirmed,**({'equipment':confirmed} if eq is True else {})))],['event_type','affected_function','operational_status','equipment_failure','information_sufficiency'])

# The only changing target in each road triple is road_access.
road_specs=[
 ('a01','train','A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident.','equipment_failure','cargo_handling',True),
 ('a02','train','A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident.','weather_disruption','cargo_handling',None),
 ('a03','train','A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues.','navigation_restriction','navigation',None),
 ('a04','train','A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event.','navigation_restriction','navigation',None),
 ('a05','validation','Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident.','equipment_failure','cargo_handling',True),
 ('a06','validation','The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident.','navigation_restriction','navigation',None),
]
for g,split,body,ev,fun,eq in road_specs:
    variants=[]
    for road,suffix in [('normal',' Separately, the access desk confirms all approach roads are open without restrictions.'),('restricted',' Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.'),('unknown','')]:
        evidence=dict(event=body,function=body,status=body)
        if suffix:evidence['road']=suffix.strip()
        if eq is True:evidence['equipment']=body
        variants.append((body+suffix,target(ev,fun,'partial_restriction',road,eq),evidence))
    add(g,'field_specific_road_evidence',split,variants,['road_access'])

# Explicit no-failure evidence changes only equipment_failure, not event classification.
equipment_specs=[
 ('e01','train','The duty log confirms every terminal service is operating normally.','normal_operations','none','normal'),
 ('e02','train','Observed dense fog has stopped vessel turning in the maneuvering basin.','weather_disruption','vessel_manoeuvring','suspended'),
 ('e03','train','An official closure of the northern approach road has stopped truck access.','land_access_disruption','land_access','suspended'),
 ('e04','train','The supervisor verifies all terminal services continue at their usual capacity.','normal_operations','none','normal'),
 ('e05','validation','Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations.','weather_disruption','vessel_manoeuvring','partial_restriction'),
 ('e06','validation','The audited overnight summary confirms all terminal services are running at normal capacity.','normal_operations','none','normal'),
]
for g,split,body,ev,fun,status in equipment_specs:
    road='restricted' if ev=='land_access_disruption' else 'unknown'
    variants=[]
    for eq,suffix in [(None,' Equipment condition has not been assessed.'),(False,' A completed technical inspection explicitly ruled out equipment failures relevant to this report.')]:
        evidence=dict(event=body,function=body,status=body,equipment=suffix.strip())
        if road=='restricted':evidence['road']=body
        variants.append((body+suffix,target(ev,fun,status,road,eq),evidence))
    add(g,'equipment_unknown_vs_excluded',split,variants,['equipment_failure'])

# Same event and evidence, different degree of operational impact.
status_specs=[
 ('s01','train','Technicians confirmed a failed winch controller at the timber quay.','Timber unloading continues at reduced capacity.','Timber unloading is fully suspended.','equipment_failure','cargo_handling',True,'unknown'),
 ('s02','train','The authority confirmed a navigation restriction due to loose floating logs in the channel.','Vessel passage continues under an escort restriction.','Vessel passage is fully suspended.','navigation_restriction','navigation',None,'unknown'),
 ('s03','train','The eastern approach-road bridge is under a confirmed emergency traffic restriction.','Trucks can still reach the terminal at a reduced rate.','Truck access to the terminal is fully suspended.','land_access_disruption','land_access',None,'restricted'),
 ('s04','train','An inspected power-supply fault affects the cargo palletizer.','Pallet handling continues using reduced capacity.','Pallet handling is fully suspended.','equipment_failure','cargo_handling',True,'unknown'),
 ('s05','validation','The port authority confirmed a navigation restriction around a damaged breakwater.','Vessel transit continues in controlled batches.','Vessel transit is fully suspended.','navigation_restriction','navigation',None,'unknown'),
 ('s06','validation','A verified washout has restricted the service road used by inbound trucks.','Inbound truck access continues at reduced capacity.','Inbound truck access is fully suspended.','land_access_disruption','land_access',None,'restricted'),
]
for g,split,body,partial,stopped,ev,fun,eq,road in status_specs:
    variants=[]
    for status,clause in [('partial_restriction',partial),('suspended',stopped)]:
        evidence=dict(event=body,function=clause,status=clause)
        if eq is True:evidence['equipment']=body
        if road=='restricted':evidence['road']=body
        variants.append((body+' '+clause,target(ev,fun,status,road,eq),evidence))
    add(g,'event_type_vs_operational_state',split,variants,['operational_status'])

def write(name,data):
    (OUT/name).write_bytes(data.encode('utf-8'))

def main():
    OUT.mkdir(parents=True,exist_ok=True)
    split_of={a['id']:a['split'] for a in annotations}
    for split in ['train','validation']:
        write(split+'.jsonl',''.join(json.dumps(r,ensure_ascii=False)+'\n' for r in rows if split_of[r['id']]==split))
    write('annotations.jsonl',''.join(json.dumps(a,ensure_ascii=False)+'\n' for a in annotations))
    write('contrast-groups.json',json.dumps(groups,indent=2)+'\n')
    print(dict(collections.Counter(split_of.values())))

if __name__=='__main__':main()
