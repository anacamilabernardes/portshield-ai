# Corrected-prefix adapter diagnostic: error analysis

## Scope and provenance

This document reviews diagnostic run `20261012T041428Z-f48de04f`, completed on 2026-10-12.
The user supplied the original Colab archive. Its internal file hashes were verified before
publication. The original files, including the generated report and execution script, are
preserved in [the run evidence directory](../../results/prefix-v2/diagnostic-20261012T041428Z-f48de04f/).

This was a new inference run with the existing V1 QLoRA adapter, not recovery of the earlier
evaluation's individual outputs. There was no retraining. Aggregate quality metrics match
the previous corrected-prefix adapter report; this alone does not prove response-by-response
identity with that earlier run, whose individual predictions were not saved.

## Verified results

- 240 records processed; zero recorded inference errors.
- JSON parse validity and complete schema validity: 100%.
- Fully correct records: 169/240 (70.42%).
- Event-type macro-F1: 0.860886.
- Abstention precision and recall: 100% on this set.
- 71 records have errors; each has exactly one differing field.

| Scenario family | Records | Fully correct | Observed mismatch |
|---|---:|---:|---|
| weather_disruption-2 | 40 | 11 | 29 event types predicted as navigation_restriction |
| land_access_disruption-2 | 40 | 40 | None |
| equipment_failure-2 | 40 | 38 | 2 unsupported road_access=restricted |
| navigation_restriction-2 | 40 | 40 | None |
| normal_operations-2 | 40 | 40 | None |
| unknown-2 | 40 | 0 | 40 affected_function=cargo_handling instead of unknown |

All four remaining fields—equipment_failure, information_sufficiency, operational_status
and human_review_required—matched their reference labels in all records. These scores are
specific to the supplied synthetic annotations, not an assessment of real operational safety.

## Pattern 1: weather cause versus navigation restriction

Scenario body:

> Gale conditions partially restricted vessel manoeuvring. Road access remains normal. No equipment failures.

Expected event_type: `weather_disruption`. The adapter returned `navigation_restriction`
in 29/40 records, while preserving the other six fields.

Under the reviewed annotation policy, an explicitly stated weather cause should determine
the event type; the operational impact belongs in affected_function and operational_status.
The pattern is consistent with confusion between cause and impact, but it does not reveal
the model's internal reasoning. Label semantics should be independently reviewed before tuning.

## Pattern 2: mentioned activity versus verified impact

Scenario body:

> A rumour about cargo operations has no verified status.

All 40 records correctly used event_type=unknown and information_sufficiency=insufficient.
However, all assigned affected_function=cargo_handling instead of unknown. The text mentions
cargo operations but does not confirm that they are affected. Event-level abstention therefore
did not ensure evidence-based uncertainty in every field.

## Pattern 3: unsupported road restriction

Scenario body:

> Equipment failure partially restricted cargo handling.

Two records returned road_access=restricted. Road conditions are not supplied, so the
reference value is unknown. The word "restricted" describes cargo handling, not road access.
The other 38 records with the same scenario body returned the expected full target.

## Prefix sensitivity: hypothesis, not established cause

Within each family, the model-visible scenario body is identical; the opaque reference prefix
varies. Weather records split into 11 correct and 29 incorrect classifications. Equipment
records split into 38 correct responses and two unsupported road restrictions.

This is an observed association between varying input references and differing outputs.
**Sensitivity to irrelevant prefix tokens is a hypothesis, not a demonstrated cause.**
Greedy decoding (do_sample=false) does not by itself exclude numerical execution variation.
The current run contains no controlled no-prefix condition or repeated identical-input
comparison that would isolate the prefix's effect. Do not present this as proof that the
hash alone caused the errors or that removing it will improve performance.

A proposed follow-up should preserve model/adapter artifacts, report bodies, targets, prompt,
generation configuration and precision while removing only the prefix. Save it as a new run.
Repeated identical-input checks within the same environment should help quantify execution
variation. If feasible, compare both conditions in that same environment and record execution
order. This follow-up has not yet been executed or included in this publication.

## Evidence and reproducibility

- Dataset SHA-256: `7c2d7b063ca152302e8e234480da68bfc5c939ec0e002575b8e7cac53cbf0fbe`.
- Hardware recorded: Tesla T4; Python 3.12.15; PyTorch 2.6.0+cu124;
  Transformers 4.51.3; PEFT 0.15.2; Accelerate 1.6.0; Pydantic 2.11.3.
- Recorded generation overrides: max_new_tokens=256, do_sample=false, pad_token_id=151645.
- Metadata records adapter-file hashes, evaluator/prompt code hashes and base acquisition provenance.
  Preserving these records is not an independent rehash of the Colab model files by the reviewer.
- predictions.jsonl contains every input, original response, expected target, validated output,
  field differences and diagnostic duration.
- errors.json contains the 71 nonmatching records.
- event_confusion_matrix.csv uses expected classes as rows and predicted classes as columns.
  INVALID represents schema or inference failures; no such failures occurred in this run.
- artifact-hashes.json authenticates internal byte consistency, not authorship or an external signature.

## Limits and decision

The 240 records represent only six distinct scenario bodies repeated 40 times each.
The adapter was trained on V1 data with label-bearing prefixes. Replacing test prefixes does
not remove training history or establish an independent holdout. No raw responses were repaired.
These inspected examples are development diagnostics, not a future blind test.

The run measures no streaming TTFT, throughput, GPU memory or groundedness benchmark.
Per-record durations should not be presented as a controlled serving-performance study.

Preserve the results; investigate the no-prefix condition before another training run. Continue
reviewing annotation semantics and building diverse, independently reviewed scenario groups.
The model remains research-only with required human review.
