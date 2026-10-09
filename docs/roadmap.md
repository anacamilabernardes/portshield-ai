# Version roadmap

| Release | Delivery | Exit evidence | Dependencies |
|---|---|---|---|
| V1 | Synthetic contract, CPU/SLM baselines, LoRA/QLoRA, quantization, private serving and benchmarks | Frozen tests, model/provenance hashes, measured quality and resource comparison | GPU and reviewed snapshot |
| V2 | Public-corpus RAG, provenance, ACLs and citation/abstention review | Independent relevance review, missing-evidence/injection cases, no unauthorized retrieval | Data Steward and IAM |
| V3 | Forecasting/anomaly product integrated with structured explanation | Temporal backtest, seasonal-naive comparator, horizon-wise MAE/RMSE, calibrated intervals, false-positive budget | Approved public time series |
| V4 | Constrained workflow, authenticated human review, replayable audit | Role separation, idempotency, bounded steps, failure/rollback drill, no action without approval | Domain governance and immutable audit |

The retained `portshield/` mean forecast, fictional graph and local review are transparent demo baselines,
not completion of V3/V4. Future anomaly detection compares residual/seasonal baselines before ML;
LLM explanations cite numeric artifacts rather than generate forecasts. V4 agent uses explicit typed
read-only tools and bounded planning; human approval precedes any authorized external effect.

Engineering checkpoints: problem/metric acceptance → provenance → baseline errors → model specialization
tradeoff → source/identity controls → capacity and security → pilot usefulness → promote or stop.
No calendar commitment is asserted without staffing and infrastructure. Larger architecture components
are added only when bottlenecks and governance requirements justify them.
