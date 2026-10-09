# Evaluation plan

## Checks implemented now

The automated suite checks source access filtering, abstention without accessible evidence, forecast input validation and trailing-window behavior, graph disruption scenarios, review binding to the assessed report, and detection of a modified audit record. These are software behavior checks, not model quality or institutional security certifications.

## Experimental evaluation before pilot admission

Compare four configurations: base SLM; base SLM plus private RAG; fine-tuned SLM; fine-tuned SLM plus RAG and quantitative analytics. Use the same held-out public/synthetic scenarios and document all model, adapter, dataset, hardware, and serving versions.

| Component | Measures |
| --- | --- |
| Event tasks | Macro F1, per-class recall, field accuracy, JSON/schema validity |
| Retrieval and answers | Recall@K, citation correctness, evidence coverage, supported-answer rate, abstention quality |
| Forecasting | Rolling-origin MAE and seasonal-naive comparison; interval coverage only for calibrated models |
| Graph scenarios | Independently checked connectivity, route validity and scenario consistency |
| Operations | VRAM, throughput, P95 latency, failure rate on declared hardware |
| Governance | Permission violations, injection/leakage cases, review and audit completeness |

Set acceptance thresholds with responsible analysts before measuring. Do not infer validated operational value from the synthetic demonstration. No performance numbers or claims of model improvement have been measured here.

Temporal evaluations must exclude future observations from both training and feature computation. Keep scenario families out of training when they appear in held-out tests. Include ambiguous, conflicting, insufficient, inaccessible, and malicious-source cases.
