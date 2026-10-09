# Aggregate observability

API emits requests_total(task,status) and task_seconds(task), with no prompts, identities or source text.
Prometheus also exports Python process metrics (API process only, not vLLM server VRAM).
Example alert thresholds are research defaults. Configure private Alertmanager/Grafana only after
owners and notification policy are agreed. vLLM metrics remain internal to the serving network;
GPU allocations are measured on host, not inferred from API process memory.

Recommended dashboard: request/error/abstention rates, p95 latency from histogram, upstream readiness,
GPU allocation and independent evaluation drift by approved model/dataset version. Domain drift
needs a reviewed label sample and changes in event distribution; it is not implemented by these alerts.
MLflow evaluation logging is opt-in and should use an internal tracking service with authorization
before multiuser use. No request payloads or user tokens belong in MLflow.
