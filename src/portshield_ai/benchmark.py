"""Concurrent streaming benchmark. TTFT starts at request dispatch."""
import asyncio
import json
import os
import platform
import time
from pathlib import Path
from .prompts import messages

def parse_sse(line):
    if not line.startswith("data:") or line[5:].strip() == "[DONE]":
        return None
    return json.loads(line[5:].strip())

async def benchmark(url, model, prompts, output, concurrency=1, warmup=2, gpu_memory_file=None):
    import httpx
    if concurrency < 1 or not prompts:
        raise ValueError("Positive concurrency and nonempty prompts required")
    semaphore = asyncio.Semaphore(concurrency)
    async with httpx.AsyncClient(timeout=120, trust_env=False) as client:
        async def one(text):
            async with semaphore:
                start = time.perf_counter(); first = None; tokens = None; content = ""
                async with client.stream("POST", url.rstrip("/") + "/chat/completions", headers={"Authorization": "Bearer " + os.getenv("VLLM_API_KEY", "")},
                    json={"model": model, "messages": messages(text), "temperature": 0, "max_tokens": 256, "stream": True, "stream_options": {"include_usage": True}}) as r:
                    r.raise_for_status()
                    async for line in r.aiter_lines():
                        chunk = parse_sse(line)
                        if not chunk:
                            continue
                        for choice in chunk.get("choices", []):
                            delta = choice.get("delta", {}).get("content", "") or ""
                            if delta and first is None:
                                first = time.perf_counter()-start
                            content += delta
                        if chunk.get("usage"):
                            tokens = chunk["usage"].get("completion_tokens")
                return {"ttft_seconds": first, "latency_seconds": time.perf_counter()-start, "completion_tokens": tokens, "raw": content}
        for i in range(warmup):
            await one(prompts[i % len(prompts)])
        start = time.perf_counter()
        rows = await asyncio.gather(*(one(p) for p in prompts))
        elapsed = time.perf_counter()-start
    def stats(values):
        values = sorted(v for v in values if v is not None)
        return {"n": len(values), "mean": sum(values)/len(values), "p50": values[len(values)//2], "p95": values[min(len(values)-1,int(.95*len(values)))]} if values else None
    memory = None
    if gpu_memory_file:
        # External sampler records server GPU allocations; client RSS is not server VRAM.
        measurements = [json.loads(line)["memory_used_mib"] for line in Path(gpu_memory_file).read_text().splitlines()]
        memory = max(measurements) if measurements else None
    report = {"model": model, "concurrency": concurrency, "warmup": warmup, "requests": len(rows), "elapsed_seconds": elapsed,
        "requests_per_second": len(rows)/elapsed, "completion_tokens_per_second": sum(r["completion_tokens"] for r in rows)/elapsed if all(r["completion_tokens"] is not None for r in rows) else None,
        "latency_seconds": stats([r["latency_seconds"] for r in rows]), "ttft_seconds": stats([r["ttft_seconds"] for r in rows]),
        "peak_server_gpu_memory_mib": memory, "client_platform": platform.platform(),
        "notes": "Memory is external nvidia-smi device allocation, may include other processes; use an exclusive GPU. Null means unmeasured. TTFT excludes local concurrency queue, includes transport. All errors fail the benchmark."}
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report,indent=2)+"\n")
    return report
