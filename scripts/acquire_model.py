"""Explicit connected acquisition. Production uses reviewed offline snapshots."""
import argparse, hashlib, json
from pathlib import Path
from huggingface_hub import HfApi, snapshot_download
p=argparse.ArgumentParser();p.add_argument("--repo",default="Qwen/Qwen2.5-1.5B-Instruct");p.add_argument("--revision",default="main");p.add_argument("--out",default="models/base");a=p.parse_args()
sha=HfApi().model_info(a.repo, revision=a.revision).sha
snapshot_download(a.repo, revision=sha, local_dir=a.out, allow_patterns=["*.json", "*.safetensors", "*.txt", "*.model", "LICENSE", "README.md"])
files={str(f.relative_to(a.out)):hashlib.sha256(f.read_bytes()).hexdigest() for f in Path(a.out).rglob("*") if f.is_file() and ".cache" not in f.parts}
Path(a.out,"provenance.json").write_text(json.dumps({"repo":a.repo,"revision":sha,"files":files},indent=2)+"\n")
print("Snapshot stored. Review license and scan before transfer to isolated environment.")
