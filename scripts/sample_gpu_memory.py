"""Run on inference host during benchmark; writes only VRAM allocation."""
import argparse, json, subprocess, time
from pathlib import Path
p = argparse.ArgumentParser(); p.add_argument("--seconds", type=int, default=120); p.add_argument("--gpu", default="0"); p.add_argument("--out", default="results/runs/gpu-memory.jsonl")
a = p.parse_args(); Path(a.out).parent.mkdir(parents=True,exist_ok=True)
with open(a.out,"w") as f:
    end = time.monotonic() + a.seconds
    while time.monotonic() < end:
        result = subprocess.run(["nvidia-smi", "--id="+a.gpu, "--query-gpu=memory.used", "--format=csv,noheader,nounits"], check=True, capture_output=True, text=True)
        f.write(json.dumps({"timestamp":time.time(), "memory_used_mib":float(result.stdout.strip())})+"\n"); f.flush(); time.sleep(.5)
