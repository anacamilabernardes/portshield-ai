# Qwen evaluation after prefix leakage removal

## Outcome and scope

The existing V1 QLoRA adapter outperformed the base Qwen model on the corrected-prefix test,
but its performance decreased relative to the original evaluation. No retraining was performed.
This is a prefix-change diagnostic, not validation on a new independent domain test set.

The user supplied two completed Colab evaluation reports and the evaluated dataset in
`portshield-prefix-v2-evaluation.zip`. Original reports are preserved in
[results/prefix-v2](../../results/prefix-v2/README.md). Documentation recorded on 2026-10-12;
the reports do not contain machine-readable run timestamps.

Model: Qwen/Qwen2.5-1.5B-Instruct. The restoration workflow selected base revision
`989aa7980e4cf806f80c7fef2b1adb7bc71aa306` from the saved provenance file.
The user confirmed CUDA availability on a Tesla T4. These details come from the run workflow
and screenshots, not embedded metadata in the uploaded aggregate reports. Adapter weights
and an adapter checksum were not supplied in this evidence ZIP.

## Comparison

Each evaluation contains 240 records. Rates below use all attempts as the denominator unless
the metric definition specifies a conditional denominator.

| Metric | Base, old prefix | Adapter, old prefix | Base, corrected prefix | Adapter, corrected prefix |
|---|---:|---:|---:|---:|
| JSON parse validity | 100.00% | 100.00% | 82.08% | 100.00% |
| Schema validity | 66.67% | 100.00% | 48.75% | 100.00% |
| Event macro-F1 | 0.6667 | 1.0000 | 0.2825 | 0.8609 |
| All-field exact match | 0.00% | 83.33% | 0.00% | 70.42% |
| Abstention precision | 100.00% | 100.00% | 100.00% | 100.00% |
| Abstention recall | 100.00% | 100.00% | 5.00% | 100.00% |
| Answerable coverage | 60.00% | 100.00% | 57.50% | 100.00% |
| Mean client latency, seconds | 2.251 | 3.878 | 2.352 | 4.189 |
| P95 client latency, seconds | 2.687 | 4.649 | 2.828 | 5.037 |

Historical reports: [base](../../results/qlora-v1/qwen-before-training.json) and
[adapter](../../results/qlora-v1/qwen-after-training.json). New reports:
[base](../../results/prefix-v2/qwen-base-prefix-v2.json) and
[adapter](../../results/prefix-v2/qwen-adapter-prefix-v2.json).

The corrected-prefix base run yielded 197 parseable responses and 117 schema-valid responses.
It correctly abstained on 2 of 40 reference cases requiring abstention. Its 100% abstention
precision must therefore be read alongside its 5% recall, not as broad uncertainty competence.

The corrected-prefix adapter yielded 240 schema-valid responses, 169 all-field exact matches,
and correct abstention on all 40 reference abstention cases. Its exact matches decreased from
200 to 169 relative to the old-prefix evaluation (a 12.92 percentage-point decrease).

## Adapter field-level results on corrected prefixes

| Field | Correct / 240 | Incorrect / 240 |
|---|---:|---:|
| event_type | 211 | 29 |
| affected_function | 200 | 40 |
| operational_status | 240 | 0 |
| road_access | 238 | 2 |
| equipment_failure | 240 | 0 |
| information_sufficiency | 240 | 0 |
| human_review_required | 240 | 0 |

These counts are derived from the uploaded aggregate metrics, not individual predictions.
There are 71 incorrect records and 71 total field mismatches. Because all adapter outputs
passed the schema, those totals imply one incorrect field per incorrect record. The reports
do not identify which classes were confused, which records failed, or whether the 40 function
errors are the same examples as in the old-prefix diagnostic.

## Dataset identity

SHA-256 of the evaluated JSONL:
`7c2d7b063ca152302e8e234480da68bfc5c939ec0e002575b8e7cac53cbf0fbe`.

This matches the corrected test set at repository commit
`8ae9a22f82138bccf94e7deeb377c4cadbe78d6f`. The model-visible class/split prefix was
replaced with an opaque deterministic reference. Labels and scenario bodies were retained.
There are still only six distinct scenario bodies, repeated 40 times each.

## Interpretation and limitations

- The adapter retains an observed advantage over the base model on these corrected inputs.
- The lower scores are consistent with sensitivity to the prefix change. They do not isolate
  the causal contribution of the exposed class name: the replacement uses opaque codes,
  and the historical and current evaluations ran in different sessions.
- The adapter was trained on V1 data containing label-bearing prefixes. Correcting evaluation
  inputs does not remove that training history.
- Repeated scenario bodies and fixed cause/function associations remain. Do not treat 240 rows
  as 240 independent situations or derive independent-sample confidence intervals from them.
- Schema validity measures structural consistency, not factual correctness.
- Aggregate JSON parse failures cannot identify truncation, malformed generation or execution
  errors individually. Raw predictions and error logs are required for diagnosis.
- Latency is the evaluator's client-side measurement. This is not a controlled efficiency
  benchmark; TTFT, throughput, memory and groundedness were not measured.
- This evidence does not establish operational readiness, general maritime capability or
  on-premise sovereignty.

## Next steps

Preserve this run separately from V1. Collect per-example predictions in a separately named
diagnostic rerun with model/dataset hashes, prompt and environment metadata. Do not present
newly generated predictions as the original run's missing outputs. Inspect event confusion
and road-access errors, then implement the reviewed annotation policy and diverse independent
scenario groups before deciding on another training run.

## Subsequent diagnostic evidence

A separate per-example rerun is now available in [the diagnostic analysis](prefix-v2-diagnostic-analysis.md).
It matches these aggregate adapter quality scores and identifies concrete error patterns.
It does not recover the original evaluation's missing individual responses. Prefix sensitivity
remains a hypothesis pending controlled comparison; no retraining was performed.
