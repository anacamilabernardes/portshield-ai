# Evaluation V2 protocol — proposal before further training

## Comparability and evidence

Freeze the dataset, annotation policy, prompt, decoding settings and code revision. Record
hashes for base model, adapter and datasets, dependency versions, hardware, execution dates
and run commands. Evaluate the base and current adapter before deciding on another fine-tune.
Keep adapter loading/precision comparable; distinguish adapter, merged FP16 and NF4 runs.
Publish failures and exclusions, not only successful predictions.

## Quality metrics

1. JSON parse validity over all attempted responses, without automatic repairs.
2. Complete schema validity, including enum and cross-field validation, over all attempts.
3. Accuracy for each of all seven fields, using the same denominator and invalid-output rule.
4. Exact match for all seven fields together.
5. Macro-F1 and confusion matrices for event_type, with a fixed class list.
6. Abstention precision/recall and answerable coverage; separate unknown cause from known impact.
7. Confusions for true/false/null equipment_failure and unsupported assertions per field.
8. Breakdown by causal family, affected function, evidence sufficiency, negation and mixed events.

The current evaluator marks every field wrong when whole-record validation fails. Retain that
strict metric for continuity. Optionally add a separately named raw-field diagnostic for
parseable but schema-invalid outputs; never mix the two definitions. The existing three-case
checked_fields_correct flag is not an all-field measure.

No record-level confidence intervals should treat repeated paraphrases as independent.
For a sufficiently large new set, estimate uncertainty over independent scenario groups and
report both group-level and row-level scores. Human reviewers assess evidence entailment;
schema validity alone is not groundedness.

## Performance measurements

Report warmup, repetitions, prompt/output token lengths, precision, batch/concurrency and
hardware. Measure end-to-end latency, streaming TTFT, request/token throughput and device
memory independently. Mark unavailable measurements as not measured. Adapter overhead is a
hypothesis until controlled comparison; the existing latency difference is one observation.

## Gates and implementation status

Retain the repository's provisional independent-set research targets (schema validity >=99%,
event macro-F1 >=0.90, abstention recall >=0.95, answerable coverage >=0.90). Require reviewed
all-field errors and resolved severe unsupported assertions before considering promotion.
These targets have not been demonstrated on an independent, nonleaking set and are not an
operational approval. Agree any new exact-match target before results are inspected.

Current code already supplies strict schema validity, per-field accuracy and exact match.
The new semantic checks, broader dataset, evidence annotations, group analyses and controlled
performance study are planned work, not implemented or executed by this documentation package.
