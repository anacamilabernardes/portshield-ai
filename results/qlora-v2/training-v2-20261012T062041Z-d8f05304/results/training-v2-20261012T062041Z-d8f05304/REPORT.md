# Fresh V2 adapter versus the current adapter

## Scope

One fixed QLoRA pilot on 54 synthetic training records. The current adapter was preserved. Both adapters were evaluated using identical base weights, prompts and generation settings. The two evaluation collections are reported separately; neither is a new independent final test.

Training metrics: `{"epoch": 3.0, "total_flos": 581673922900992.0, "train_loss": 0.049183481062451996, "train_runtime": 143.8475, "train_samples_per_second": 1.168, "train_steps_per_second": 0.146}`.

Primary criteria are affected_function and road_access errors plus all-field exact match. Event macro F1 alone does not determine adoption. Raw-field errors below count missing or type-mismatched fields as incorrect, while preserving correct fields in otherwise schema-invalid responses. Full schema-gated metrics are retained in the JSON evidence.

## Development validation (12 examples)

| Measure | Current adapter | V2 adapter |
|---|---:|---:|
| All-field exact matches | 0/12 | 1/12 |
| Schema-invalid responses | 7 | 2 |
| Event macro F1 (schema-gated) | 0.2778 | 0.6667 |
| event_type errors | 6 | 3 |
| affected_function errors | 8 | 8 |
| operational_status errors | 5 | 7 |
| road_access errors | 5 | 3 |
| equipment_failure errors | 5 | 3 |
| information_sufficiency errors | 4 | 2 |
| human_review_required errors | 0 | 0 |

### Paired corrections and regressions

| Record | Fields corrected | Fields regressed | Exact match: current → V2 |
|---|---|---|---|
| SYN-V2R-0001 | event_type | operational_status, equipment_failure | False → False |
| SYN-V2R-0002 | — | operational_status, equipment_failure | False → False |
| SYN-V2R-0003 | road_access, equipment_failure | affected_function, operational_status | False → False |
| SYN-V2R-0004 | equipment_failure | affected_function | False → False |
| SYN-V2R-0005 | information_sufficiency | — | False → False |
| SYN-V2R-0006 | information_sufficiency | — | False → True |
| SYN-V2R-0007 | affected_function, equipment_failure | — | False → False |
| SYN-V2R-0008 | affected_function | — | False → False |
| SYN-V2R-0009 | operational_status, road_access, equipment_failure | — | False → False |
| SYN-V2R-0010 | — | — | False → False |
| SYN-V2R-0011 | event_type | — | False → False |
| SYN-V2R-0012 | event_type | — | False → False |

## Previously examined diagnostic cases (12 examples)

| Measure | Current adapter | V2 adapter |
|---|---:|---:|
| All-field exact matches | 3/12 | 7/12 |
| Schema-invalid responses | 2 | 1 |
| Event macro F1 (schema-gated) | 0.6111 | 0.9444 |
| event_type errors | 5 | 0 |
| affected_function errors | 2 | 2 |
| operational_status errors | 2 | 1 |
| road_access errors | 2 | 1 |
| equipment_failure errors | 4 | 3 |
| information_sufficiency errors | 2 | 1 |
| human_review_required errors | 0 | 0 |

### Paired corrections and regressions

| Record | Fields corrected | Fields regressed | Exact match: current → V2 |
|---|---|---|---|
| SYN-RESERVE-0001 | event_type, equipment_failure | — | False → True |
| SYN-RESERVE-0002 | — | equipment_failure | True → False |
| SYN-RESERVE-0003 | equipment_failure | — | False → True |
| SYN-RESERVE-0004 | event_type | — | False → False |
| SYN-RESERVE-0005 | — | — | True → True |
| SYN-RESERVE-0006 | — | — | True → True |
| SYN-RESERVE-0007 | road_access, equipment_failure | — | False → True |
| SYN-RESERVE-0008 | event_type | equipment_failure | False → False |
| SYN-RESERVE-0009 | — | equipment_failure | False → False |
| SYN-RESERVE-0010 | equipment_failure | — | False → True |
| SYN-RESERVE-0011 | event_type, operational_status, information_sufficiency | — | False → False |
| SYN-RESERVE-0012 | event_type | — | False → True |

## Findings and decision

The V2 adapter is an experimental candidate, not an accepted replacement. It improves road_access in both collections, but affected_function does not improve in aggregate. On development validation, operational_status worsens from five to seven errors and only one of twelve records is entirely correct. The diagnostic improvement from three to seven exact matches includes a previously correct record becoming incorrect (SYN-RESERVE-0002). Neither adapter has demonstrated operational readiness.

Specific remaining patterns:

- SYN-RESERVE-0011 still assigns cargo_handling to an unverified allegation. SYN-V2R-0011 and 0012 similarly infer cargo impact from unresolved conflicting reports.
- SYN-V2R-0003 and 0004 regress from land_access to cargo_handling for an explicitly scoped rail-access incident.
- SYN-V2R-0007 and 0008 still infer normal roads when roads are not supplied.
- Explicitly excluded equipment failures become null in SYN-V2R-0001/0002 and SYN-RESERVE-0002/0008/0009. An increase in null predictions must not be described as correct uncertainty when evidence explicitly excludes a fault.
- Temporal interpretation remains weak: SYN-V2R-0009/0010 retain an equipment-failure event despite the current recovery report.
- Partial restriction and suspension remain confused: the stopped tug-assisted service in SYN-V2R-0005 becomes partial_restriction; reduced truck access in SYN-RESERVE-0004 becomes suspended.

Before another candidate, develop additional training families for corroboration, source conflict, scope of the primary affected service, explicit negation and current versus historical conditions. Preserve these examined evaluation cases as development diagnostics; do not move their texts or close paraphrases into training and later claim independence. Freeze a new final evaluation collection after development choices are fixed.

## Interpretation boundaries

This is a small synthetic development experiment. Training data, adapter initialization and optimization history differ from the old adapter, so improvements cannot be attributed to one annotation rule alone. The final epoch was preselected; no model was chosen by examining event F1. Previously examined examples remain diagnostics. Do not call these results operational validation or use the same exposed examples as an independent future test.

All raw responses, expected values, per-field differences, paired transitions and confusion tables are preserved. Any adoption decision must consider the primary metrics alongside regressions in every remaining field.

The first attempt ended at epoch 2.59 because the library inferred only 18 updates. A fresh corrected run used 21 updates and completed epoch 3.0 before paired comparison. Its predecessor is preserved as execution evidence, not as a competing evaluated model. The original artifact-hashes.json was generated before the comparison process finished printing to comparison-console.log; the export verification records the final log hash without rewriting the original manifest. The current adapter reproduced all twelve historical diagnostic responses byte for byte.

## Reproducibility and evidence index

- [Frozen protocol](../../REVIEW-AND-PROTOCOL.md) and [training configuration](training-config.json): fresh adapter; seed 42; rank 16; alpha 32; dropout 0.05; learning rate 0.0002; batch size 1; accumulation 8; 21 updates, three epochs; assistant-only supervision.
- [Base provenance](base-provenance.json), [environment](environment.json), [preflight checks](preflight.json), [token audit](token-audit.json), [adapter hashes](adapter-hashes.json), and [verified model backup](backup-verification.json).
- [Input hashes](input/input-hashes.json), [54 training records](input/train.jsonl), [12 development-validation records](input/validation.jsonl), and [12 historical diagnostic records](input/diagnostic.jsonl). Dataset source commit: `9e3a16fc4b9e6861646509c7553f13eac20f7cec`.
- Individual responses include the input text, raw response, parsed values, expected values, schema errors, strict field correctness and per-field differences: [current validation](current-validation-predictions.jsonl), [V2 validation](v2-validation-predictions.jsonl), [current diagnostics](current-diagnostic-predictions.jsonl), [V2 diagnostics](v2-diagnostic-predictions.jsonl).
- [Paired comparison](comparison.json), all four `*-confusion.json` files, [current generation configuration](current-generation-config.json), [V2 generation configuration](v2-generation-config.json), and [rendered prompts](rendered-messages.json) preserve the comparison conditions.
- [Local verification](local-verification.json) independently recounts 48 responses and 24 pairs. [Publication hashes](../../publication-manifest.json) identify every published evidence file except the manifest itself. Original evidence files retain their bytes; added reporting and verification files have publication hashes.

The separate model ZIP passed integrity verification after download. This publication contains evidence and configuration, not weights, and does not change the active adapter. The decision remains **do not replace the current adapter**. These exposed collections are development/regression material; improvements do not establish an independent final-test result.
