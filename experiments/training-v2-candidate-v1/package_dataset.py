"""Create the readable review, byte manifest and portable archive."""
from pathlib import Path
import hashlib
import json
from zipfile import ZipFile, ZIP_DEFLATED

ROOT=Path(__file__).resolve().parent
DATA=ROOT/'data/training-v2-candidate-v1'
rows=[]
for split in ['train','validation']:
    rows.extend(json.loads(x) for x in (DATA/(split+'.jsonl')).read_text().splitlines())
ann={a['id']:a for a in map(json.loads,(DATA/'annotations.jsonl').read_text().splitlines())}
lines=['# Training revision V2: annotation review','',
       '54 assistant-authored synthetic examples. Review status: project owner reported completing review; independent reviewer status unverified. See review-record.json. These are development data, not a final test.','']
for r in rows:
    a=ann[r['id']]
    lines += [f"## {r['id']} — {a['split']} / {a['group']}",'',r['text'],'',
              '| Field | Target | Rationale |','|---|---|---|']
    for k,v in r['target'].items():
        lines.append(f"| `{k}` | `{json.dumps(v)}` | {a['field_rationales'][k]} |")
    lines.append('')
(ROOT/'REVIEW.md').write_bytes(('\n'.join(lines)+'\n').encode())
files=[p for p in ROOT.rglob('*') if p.is_file() and '__pycache__' not in p.parts and p.name!='manifest.json']
manifest={'version':'training-v2-candidate-v1','date':'2026-10-12','status':'user_reported_review_completed','independent_review_verified':False,'language':'en','data_class':'synthetic','train':36,'validation':18,'contrast_groups':24,'test_split':None,'trained':False,'historical_labels_modified':False,'source_of_design':'Observed field-level errors in prior diagnostic comparisons; no diagnostic rows copied.','schema_snapshot_sha256':hashlib.sha256((ROOT/'schema_snapshot.py').read_bytes()).hexdigest(),'files':{p.relative_to(ROOT).as_posix():hashlib.sha256(p.read_bytes()).hexdigest() for p in sorted(files)}}
(ROOT/'manifest.json').write_bytes((json.dumps(manifest,indent=2)+'\n').encode())
archive=ROOT.parent/'portshield-training-v2-candidate-v1.zip'
with ZipFile(archive,'w',ZIP_DEFLATED) as z:
    for p in files+[ROOT/'manifest.json']:
        z.write(p,arcname='training-v2/'+p.relative_to(ROOT).as_posix())
with ZipFile(archive) as z:
    assert z.testzip() is None
    for name,h in manifest['files'].items():
        assert hashlib.sha256(z.read('training-v2/'+name)).hexdigest()==h
print(f'Packaged {len(files)+1} files; all archive hashes verified: {archive}')
