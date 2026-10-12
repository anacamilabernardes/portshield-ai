# Evaluation plan and metric semantics

## Hypothesis and comparison

Compare (A) optional larger local general model, (B) small base model, (C) SLM+QLoRA, (D) merged
SLM+NF4+vLLM. Freeze `test.jsonl`, its hash, prompt contract and decode budget before tuning. Select
epochs/rank only on validation. Same hardware/context/concurrency where possible; report differences.
Retain raw prediction files only for synthetic evaluation if needed; never log institutional prompts.

Dataset splits are disjoint by authored paraphrase family, not random rows. There are only 18 unique
semantic templates: a high score proves plumbing, not field generalization. Build an independently
reviewed public/synthetic domain holdout with negatives, negation, mixed events, uncertainty, multilingual
reports and adversarial instructions before model promotion. Estimate uncertainty via bootstrap grouped
by independent event/source family on that larger holdout; do not treat repeated IDs as independent samples.

| Metric | Definition / implementation |
|---|---|
| JSON validity | Successfully parsed raw JSON / all attempts; no fences or repair removed |
| Schema validity | Strict complete EventAnalysis validation / all attempts |
| Macro F1 | Mean of per-class 2TP/(2TP+FP+FN), six fixed classes; absent class gets 0; invalid outputs are failures |
| Field accuracy / exact match | Correct field or entire record / all attempts, including invalid |
| Abstention | Insufficient evidence flag; precision/recall against unknown target; no automatic error-to-abstention in evaluator |
| Answerable coverage | Valid nonabstained output / answerable reports; prevents all-abstain gaming |
| Groundedness proxy | Fraction of nonempty exact quotes present in cited authorized source; null for abstention |
| Groundedness human | Independent assessment of entailment, relevance, completeness and currentness; not automated here |
| Latency | Request dispatch to final streamed response; report mean/p50/p95 and sample count |
| TTFT | Dispatch to first nonempty content delta, not initial role/usage chunk; includes transport, excludes semaphore queue |
| Throughput | Completed requests / benchmark wall time; generated token usage / wall time, null if usage absent |
| Memory footprint | HF model footprint when quantizing; peak device allocation from external nvidia-smi on exclusive GPU |

Memory includes weights, cache, runtime reservations and CUDA overhead in the server measurement.
Client RSS cannot substitute for server VRAM. A sampled peak can miss spikes. Stream benchmark errors
abort rather than reporting throughput for a hidden subset. Record failures and retries separately.

## Provisional research gates (targets, not achieved results)

V1: schema validity ≥99%, macro F1 ≥.90, abstention recall ≥.95 and answerable coverage ≥.90 on
an independent domain set; NF4 event F1 decrease ≤.02 compared with merged FP16; lower measured
footprint. V2: no ACL leakage, exact citation support=1, human evidence relevance ≥.90, unanswerable
recall ≥.95. Resource budgets must be chosen after capacity tests; no unmeasured latency SLA is asserted.
The small generator cannot establish these gates. Domain and security owners sign off pilot readiness.

Run `portshield-ai evaluate` per backend, `benchmark` at concurrency 1/4/8 with fixed warmup and prompts,
and notebook06 for RAG. Include signed JWT negative tests and source poisoning/injection cases.
MLflow logging is opt-in and local; only scalar metrics and synthetic report artifacts are uploaded.


## V1 evidence review and V2 follow-up

V1 model-visible identifiers contain target-class names, creating direct label leakage.
Its 240 test rows contain six distinct scenario texts. See the [dataset audit](data/dataset-v1-audit-and-v2-plan.md)
and [V2 evaluation protocol](evaluation-v2-protocol.md). Previously inspected test and diagnostic
cases are development material; a new independent holdout is required after changes informed
by their errors. V1 aggregate scores do not satisfy independent-set research gates.
