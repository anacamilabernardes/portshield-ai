# PortShield AI

**Sovereign Maritime Critical Infrastructure Resilience**

An independent Applied AI engineering reference for structured maritime event analysis on controlled
infrastructure. PortShield explores whether domain specialization of a small open-weight model can
preserve useful task quality while reducing compute relative to larger general-purpose models.
**All included data is public or independently generated synthetic material. No sensitive MPOR data is included.**

[Português](README.pt-BR.md) · [Architecture](docs/architecture.md) · [Evaluation](docs/evaluation-plan.md)
· [Runbook](docs/deployment-runbook.md) · [Model card](docs/model-card.md) · [Disclaimer](DISCLAIMER.md)

## What you can run

| Capability | Implementation and validation boundary |
|---|---|
| CPU baseline and synthetic event generator | Runnable, with schema validation and conservative abstention |
| LoRA / QLoRA for Qwen2.5-1.5B-Instruct | Assistant-only supervised loss, held-out template validation; requires CUDA |
| NF4 quantization and adapter merge | Local workflows; GPU execution not validated in this delivery |
| vLLM and FastAPI | Private serving profile, JWT/demo auth, validated outputs and metrics |
| Private RAG | Offline lexical retrieval; optional local vLLM generation limited to cited exact quotes |
| Evaluation | JSON/schema validity, field accuracy, macro F1, abstention, quote support proxy |
| Streaming benchmark | Concurrent latency, TTFT, request/token throughput; external server VRAM sampling |
| Monitoring / MLOps | Prometheus metrics/rules; opt-in local MLflow aggregate logging |
| SVD / MPO / Tensor Train | Runnable 16x16 toy experiment; no proprietary compression reproduction |
| Forecasting, graphs, review | Existing transparent demo retained in `portshield/`; research only |
| Production IAM, lakehouse, agents | Architecture and deployment examples; readiness gates remain open |

No model weights or trained adapter is bundled. See `results/validation.json` for actual local checks,
and `results/baseline-cpu.json` for measured synthetic scores. No fabricated GPU measurements.

## QLoRA V1 experimental evidence

A QLoRA adapter was trained and restored in Colab. Exact match improved from 0% to 83.3%
and event macro-F1 from 0.667 to 1.000 on the original 240-row synthetic test. However,
those records contain only six distinct scenario texts and their input identifiers expose
target labels. These scores do not establish generalization or operational readiness.
A three-case exploratory comparison yielded only one schema-valid, checked-field-correct
response per model. No additional training or production deployment is claimed.

- [Reviewed results and limitations](docs/experiments/qlora-v1-reviewed-results.md)
- [V1 dataset audit and V2 plan](docs/data/dataset-v1-audit-and-v2-plan.md)
- [Proposed annotation policy](docs/data/annotation-policy-v2.md)
- [Full-field evaluation protocol](docs/evaluation-v2-protocol.md)
- [Original reports and diagnostic evidence](results/qlora-v1/README.md)

## Local quickstart (Python 3.11 or 3.12)

Run all commands from repository root. Linux/macOS:

```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e '.[dev,toy]'
portshield-ai generate --seed 42 --per-class 40
portshield-ai classify "Strong winds temporarily restricted vessel manoeuvres. Road access remains normal. No equipment failures."
portshield-ai evaluate --out results/runs/baseline.json
portshield-ai rag "public data opening plan"
portshield-ai rag-evaluate
python experiments/tensor_network_compression/toy.py
python -m pytest -q
```

Windows PowerShell: activate with `.\.venv\Scripts\Activate.ps1`; use `pip install -e ".[dev,toy]"`.
The CPU paths work on Windows. Use Linux/WSL2 plus supported NVIDIA CUDA hardware for the GPU profile.

```bash
export AUTH_MODE=demo
export PORTSHIELD_DEMO_TOKEN=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
uvicorn portshield_ai.api:app --host 127.0.0.1 --port 8000
# In another terminal with the same token:
curl http://127.0.0.1:8000/v1/events/analyze -H "Authorization: Bearer $PORTSHIELD_DEMO_TOKEN" -H 'Content-Type: application/json' -d '{"text":"Normal operations. Road access normal. No equipment failure."}'
```

PowerShell equivalents: `$env:AUTH_MODE="demo"`; set `$env:PORTSHIELD_DEMO_TOKEN` to a generated random
value of at least 24 characters. Demo mode is for public/synthetic localhost exercises only.
Default JWT mode requires `OIDC_ISSUER`, `OIDC_AUDIENCE`, `OIDC_JWKS_URL`; see runbook.

## SLM experiment: baseline → QLoRA → NF4 → vLLM

Model choice is a small, Apache-2.0 open-weight instruction model. Acquisition resolves an immutable
Hub revision and hashes local files; inference and training use `local_files_only=True`, remote code disabled.
The pinned research environment is a reproducibility starting point, not an assertion of current security approval.
Review dependency vulnerabilities and create an environment lock before institutional deployment.

```bash
python -m pip install -e '.[train]'
# Only on an approved connected acquisition machine:
python scripts/acquire_model.py
# Transfer reviewed snapshot to an isolated GPU machine, then:
portshield-ai evaluate --backend hf --model models/base --out results/runs/slm-base.json
portshield-ai train --config configs/qlora.json
portshield-ai evaluate --backend hf --model models/base --adapter models/adapter --four-bit --out results/runs/slm-qlora.json
portshield-ai merge --base models/base --adapter models/adapter --out models/merged
portshield-ai quantize --model models/merged --out models/nf4
portshield-ai evaluate --backend hf --model models/nf4 --four-bit --out results/runs/slm-nf4.json
```

For LoRA use `configs/lora.json`. Training and serving use separate environments because vLLM
has its own torch/CUDA constraints. An optional larger local model can be acquired with `--repo`
after its own license review; evaluate on the identical frozen test file. Never train on the test split.
NF4 model weight compression does not imply equivalent KV-cache or total VRAM reduction.

```bash
# Install serving separately in a Linux CUDA environment, or use docker/compose.gpu.yml:
python -m pip install vllm==0.8.5 bitsandbytes==0.45.5
export VLLM_API_KEY=$(python -c 'import secrets; print(secrets.token_urlsafe(32))')
HF_HUB_OFFLINE=1 vllm serve models/nf4 --served-model-name portshield --host 127.0.0.1 --port 8001 --quantization bitsandbytes --load-format bitsandbytes --max-model-len 2048 --gpu-memory-utilization 0.8 --api-key "$VLLM_API_KEY" --disable-log-requests
portshield-ai evaluate --backend vllm --out results/runs/vllm-quality.json
portshield-ai benchmark --concurrency 4 --out results/runs/vllm-benchmark.json
```

Run `scripts/sample_gpu_memory.py` on the serving host concurrently with the benchmark and pass
`--gpu-memory-file results/runs/gpu-memory.jsonl` to report peak device allocation. The file must cover
the benchmark interval and the GPU must be exclusive. Without it, footprint is null.
Use a new output per configuration. Warmup, prompt corpus, concurrency, GPU, precision, context length,
driver, snapshot, adapter and dependency freeze must be recorded for meaningful comparisons.

## RAG and MLOps

The included corpus is a tiny set of original summaries of public ANTAQ and technical pages, with
source URLs, checksums and approval metadata. `portshield-ai rag 'public data opening plan'` runs
extractive retrieval; add `--generative` for local vLLM quote selection. This is a minimal RAG path,
not a validated maritime advice system. See [data provenance](data/README.md).

```bash
python -m pip install -e '.[tracking]'
export MLFLOW_TRACKING_URI=file:./mlruns
portshield-ai evaluate --mlflow --out results/runs/tracked.json
mlflow ui --host 127.0.0.1 --port 5000
```

## Delivery and governance

Fine-tuning teaches stable task behavior; retrieval supplies changing authorized evidence.
Quantitative models own numeric forecasts. Human reviewers own decisions. No operational action
is executed. The reference architecture aligns with supplied PIDP principles: open-source-first,
shared platform, Bronze–Silver–Gold, institutional ownership, lineage, IAM, MLOps and sovereignty.
Institutional documents and internal programme details are excluded from the public artifact.

| Version | Scope and promotion gate |
|---|---|
| V1 | Baseline + QLoRA + benchmark; frozen evaluation, measured quality/efficiency, reproducible model artifacts |
| V2 | Reviewed public RAG; citation/abstention evaluation, no unauthorized retrieval, human relevance review |
| V3 | Forecasting/anomaly detection; temporal backtests, leakage checks, calibrated uncertainty and drift |
| V4 | Constrained agentic workflow + authenticated human review; replayable audit, approval before any action |

Engineering Lead owns delivery and ADRs; Data Owner/Steward owns source approval; Applied AI Lead
owns evaluation and model cards; Platform/Security owners own deployment controls. See
[product requirements](docs/product-requirements.md), [risk register](docs/risk-register.md),
[roadmap](docs/roadmap.md), [contributing](CONTRIBUTING.md) and [security](SECURITY.md).
For first publication from the ZIP, use the [clean-archive GitHub guide](docs/github-publication.md).

```text
src/portshield_ai/  API, contracts, generator, inference, training, RAG, evaluation, benchmarks
portshield/        Retained dependency-free forecast/graph/human-review demo
data/              Approved public summaries, synthetic splits, JSON schemas
configs/           Model, training, source approval examples
notebooks/         Six executable workflow notebooks (heavy stages explicitly gated)
docs/adr/          Architectural decisions and consequences
docker/            CPU API and private CUDA vLLM profiles
deploy/k8s/        Restricted example deployment and default-deny networking
monitoring/        Prometheus configuration and alert rules
experiments/       Educational SVD and MPO/TT compression
tests/             Behavioral, boundary, contract and authorization tests
.github/workflows/ CPU CI, build, Docker validation and publication-content check
results/           Real CPU verification; GPU comparison template with null measurements
```

MIT for original repository content. External weights and dependencies retain their licenses.
No claim of CompactifAI reproduction or performance equivalence is made.
Technical sources: [Qwen model card](https://huggingface.co/Qwen/Qwen2.5-1.5B-Instruct),
[PEFT quantization](https://huggingface.co/docs/peft/developer_guides/quantization),
[Transformers 4.51.3 bitsandbytes](https://huggingface.co/docs/transformers/v4.51.3/quantization/bitsandbytes),
[vLLM 0.8.5 bitsandbytes](https://docs.vllm.ai/en/v0.8.5/features/quantization/bnb.html).

## Corrected-prefix evaluation update

The existing V1 adapter achieved **0.861 event macro-F1 and 70.4% all-field exact match**
on the corrected-prefix test, compared with **0.283 and 0%** for the base Qwen model.
Adapter schema validity and abstention recall remained 100%. The test still contains only
six scenario bodies repeated across 240 records, and the adapter was trained on V1 inputs.
These results do not establish independent domain generalization.

See the [four-way comparison and limitations](docs/experiments/prefix-v2-comparison.md)
and [original corrected-prefix reports](results/prefix-v2/README.md).
