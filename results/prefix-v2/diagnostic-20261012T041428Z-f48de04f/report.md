# Corrected-prefix adapter diagnostic rerun

Examples: 240. Fully correct: 169.
Schema-valid: 240.

## Field errors

| Field | Valid-output mismatches | Invalid outputs |
|---|---:|---:|
| affected_function | 40 | 0 |
| equipment_failure | 0 | 0 |
| event_type | 29 | 0 |
| human_review_required | 0 | 0 |
| information_sufficiency | 0 | 0 |
| operational_status | 0 | 0 |
| road_access | 2 | 0 |

## Event confusion matrix

Rows are expected classes; columns are predictions. INVALID includes schema and inference failures.

| Expected | weather_disruption | land_access_disruption | equipment_failure | navigation_restriction | normal_operations | unknown | INVALID |
|---|---:|---:|---:|---:|---:|---:|---:|
| weather_disruption | 11 | 0 | 0 | 29 | 0 | 0 | 0 |
| land_access_disruption | 0 | 40 | 0 | 0 | 0 | 0 | 0 |
| equipment_failure | 0 | 0 | 40 | 0 | 0 | 0 | 0 |
| navigation_restriction | 0 | 0 | 0 | 40 | 0 | 0 | 0 |
| normal_operations | 0 | 0 | 0 | 0 | 40 | 0 | 0 |
| unknown | 0 | 0 | 0 | 0 | 0 | 40 | 0 |

## Interpretation limits

This is a new run, not recovery of earlier predictions. Counts may differ from the previous reports.
Only six distinct scenario bodies are repeated 40 times. The adapter was trained on V1 data.
All-field metrics count whole-record validation failures as errors for every field.
For invalid outputs, differences are not computed; raw_response and validation_error remain available.
No raw-response repair, retraining, TTFT, throughput or memory benchmark is performed.
The per-record duration is a diagnostic measurement, not a controlled performance benchmark.
Do not use these inspected examples as a future independent holdout.

See predictions.jsonl for every input, expected target, original response and field difference.
See errors.json for only failed or mismatched records.
