# Deployment runbook

## Local CPU demonstration

From root install `pip install -e '.[dev,toy]'`, generate data and run pytest. Configure a random token
at least 24 characters long; `AUTH_MODE=demo` is explicit, never production. Start uvicorn on 127.0.0.1.
`/healthz` is liveness; `/readyz` checks corpus startup and upstream model availability when enabled.
`/metrics` requires auth; use aggregate labels only. No prompt/reply logs are emitted by app code.

`docker compose -f docker/compose.yml up --build` requires `PORTSHIELD_DEMO_TOKEN` in the shell.
API binds host 127.0.0.1:8000; container runs as UID10001 with read-only filesystem and tmpfs /tmp.
For Prometheus, supply `monitoring/prometheus-token` containing the same token, chmod600, and start
profile `monitoring`. The token file is ignored by Git. Do not expose localhost demo services publicly.

## GPU research profile

Use Linux or WSL2, supported NVIDIA driver/container toolkit and an exclusive GPU. Acquire exact
Qwen snapshot on approved connected host, scan dependencies/license, record hashes, transfer offline.
Training uses its own environment (`.[train]`); serving uses vLLM0.8.5/bitsandbytes0.45.5 separately.
Train, evaluate, merge into fresh FP16, quantize, reevaluate. Set `VLLM_API_KEY` before starting
`docker compose -f docker/compose.gpu.yml up`. Models directory is read-only, Hub offline flags set,
request logs disabled. Host vLLM endpoint binds localhost. API connects using internal service DNS.
Follow README benchmark commands; memory sampler runs on serving host during measured interval.
If saved NF4 checkpoint interoperability fails, serve merged weights with in-flight bitsandbytes loading
and separately evaluate that path; never silently relabel precision or measured results.

## Institutionally controlled target (example, not production deployment)

Assign Data Owner, Applied AI approver, platform and security owner. Verify no nonpublic repository
content; classify sources; produce SBOM and frozen environment; scan/sign images; pin image/model
digests. Establish internal HTTPS gateway with body/rate/concurrency limits, Keycloak realm,
RS256 issuer/audience and `portshield-analyst` role. OIDC_JWKS_URL is a trusted internal URL;
TLS verification stays enabled. Default auth is JWT and missing/invalid config fails closed.

Kubernetes examples require approved `portshield/api:<digest>` image, corpus/model volumes and a
ConfigMap specifying operator-reviewed OIDC settings. The namespace has restricted Pod Security
and default-deny ingress/egress; extend policies for gateway, private vLLM, DNS and internal IAM,
never public internet. Example CIDRs/selectors are intentionally not institutional topology.
Do not claim on-prem sovereignty solely because a container runs locally: verify egress,
telemetry, licenses, ownership, storage encryption, secrets and external dependencies.

## Promotion, rollback and recovery

1. Freeze data/prompt/schema/model versions and write evaluated model card.
2. Run negative-auth/ACL tests, independent domain evaluation and resource capacity benchmark.
3. Verify source currentness, reviewer workflow, immutable minimized audit export and restore drill.
4. Canary to authorized analysts; compare schema failures, abstention, latency and usefulness.
5. Promote only after domain/security/platform acceptance; otherwise preserve baseline.

Rollback: stop admission; switch to previously approved model+adapter+corpus+schema bundle; restart
and check readiness; run frozen smoke cases; restore access gradually. A schema mismatch blocks rollback
until compatible API version is deployed. Never patch weights live. Snapshot hashes are validated.
Recovery: restore approved model and corpus from encrypted backup, verify hash manifest, replay only
authorized synthetic test cases, validate IAM and metrics, then reopen. Conduct a restore drill before pilot.

Incident triage: readiness503 → upstream/credentials; schema failures → incompatible model/contract;
VRAM pressure → reduce concurrency/context or rollback; high abstention → corpus freshness/taxonomy;
access anomaly → isolate/revoke tokens and preserve minimized metadata. Do not log payloads for debugging.
Retention and audit evidence must follow designated institutional policy; no arbitrary compliance claim.
