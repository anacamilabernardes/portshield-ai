"""Content guardrails, not a complete sensitive-data detector."""
import json
from pathlib import Path
root=Path(__file__).resolve().parents[1]
bad=[]
for p in root.rglob("*"):
    if not p.is_file() or any(x in p.parts for x in (".git",".venv","__pycache__",".pytest_cache","build","dist")):
        continue
    rel=p.relative_to(root)
    if p.suffix.lower() in {".pdf", ".docx", ".safetensors", ".pem", ".key"} or p.name in {".env", "prometheus-token"}:
        bad.append(str(rel))
for doc in json.loads((root/'data/public/corpus.json').read_text()):
    if doc['data_class'] not in {'public','synthetic'} or not doc['approved']:
        bad.append(doc['id'])
for p in (root/'notebooks').glob('*.ipynb'):
    for cell in json.loads(p.read_text())['cells']:
        if cell.get('outputs') or cell.get('execution_count') is not None:
            bad.append(str(p.relative_to(root))+':outputs')
if bad:
    raise SystemExit('Publication review failed: '+', '.join(bad))
print('Publication guardrails passed. Manual source and secret review remains required.')
