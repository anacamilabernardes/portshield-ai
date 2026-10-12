# Targeted training revision V2 — candidate 1

Prepared 2026-10-12. **54 newly authored synthetic English examples: 36 training and 18 validation, in 24 contrast groups.** All six event labels occur in both splits. This is a small development candidate, not a replacement for a diverse operational corpus or evidence that another training run will improve the model. The project owner reported completing review and authorized publication; see `review-record.json`. Independent reviewer status has not been verified. No training, model selection or final-test evaluation was performed.

## Changes from the historical dataset

Historical labels were not changed: the observed failures were model errors, not a reason to relabel valid targets. This package creates new narratives rather than appending repeated copies of the six historical scenarios. IDs, split names and class names are not added as input prefixes. Only `text` is input; `target` is the supervised output. Annotation rationales and grouping metadata must not enter prompts.

| Contrast | Groups | Examples | Intended distinction |
|---|---:|---:|---|
| Unverified versus verified impact | 6 | 12 | Mentioning cargo in a rumor does not establish affected cargo operations |
| Independent road condition | 6 | 18 | Cargo/navigation restrictions coexist with normal, restricted or unstated roads |
| Equipment unassessed versus fault excluded | 6 | 12 | `null` is unknown; `false` needs explicit negative evidence |
| Partial versus suspended operation | 6 | 12 | Event identity stays fixed while only operational status changes |

The first four scenario groups in each category are training; the remaining two are validation. No contrast group crosses the split. Different physical scenarios are used across splits, but common task concepts and some construction patterns remain; group separation does not prove semantic independence. Validation is disclosed development material, not a blind test. There is deliberately no test split in this package.

## Annotation rules for all fields

- `event_type`: use the supported primary cause/type. Unverified allegations and confirmed impacts with unresolved cause remain `unknown`. `suspended` is never an event type.
- `affected_function`: use the function whose impact is confirmed. An allegation alone leaves `unknown`; confirmed normal operations use `none`.
- `operational_status`: confirmed complete stoppage uses `suspended`, ongoing reduced operation uses `partial_restriction`, explicit normal service uses `normal`, unverified impact uses `unknown`.
- `road_access`: use an independent road/gate statement or the explicit road event itself. Cargo and navigation restrictions do not establish road conditions.
- `equipment_failure`: confirmed defect is `true`; explicit inspection excluding failures is `false`; no assessment or an unverified alleged fault is `null`.
- `information_sufficiency`: follows the existing contract's event-type decision. It is `insufficient` for an unresolved type even if some other fields are known. An unmentioned road condition alone does not make a confirmed event insufficient.
- `human_review_required`: always `true`, including normal operations, under project policy.

Road triples identify a primary incident so the secondary road statement does not create an ambiguous single-event target. In normal-operation examples, normal service does not itself prove normal equipment condition or road access.

## Files

- `data/training-v2-candidate-v1/train.jsonl` and `validation.jsonl`: existing `EventRecord` format.
- `annotations.jsonl` in that directory: seven per-field rationales for every example.
- `contrast-groups.json`: split assignment, members and permitted label changes.
- `REVIEW.md`: all examples and annotations in readable form.
- `build_dataset.py`: deterministic source of the new cases; no random duplication.
- `schema_snapshot.py`: existing schema used for validation, preserved unchanged.
- `validate_dataset.py`, `validation.json`, `manifest.json`: checks, coverage and byte hashes.

The 720 historical records, the 15 earlier contrastive cases, and the 12 examined reserve cases are excluded from the new rows. Exact normalized-text overlap is checked against the local snapshots listed in validation.json. This is not a paraphrase-contamination guarantee: the known failure patterns intentionally informed authoring. The 12 examined cases remain diagnostics, not training or validation rows.

## Before another training run

Review the narratives and all seven targets in REVIEW.md, especially unresolved causes and multiple independent facts. Do not interpret machine validation or assistant review as independent human adjudication. Keep any corrected annotations in a new version with an explicit change log.

The project owner has reported completing annotation review; preserve that record with any future training run. This package does not change active training configuration or select hyperparameters. Preserve the current adapter; any future adapter needs a new output directory. Investigate the previously near-zero training loss and verify response-only label masking before launching a new run. Compare affected-function errors, road errors, all-field exact match, and every other field's regressions. Event F1 alone is insufficient. Reserve fresh independently reviewed examples for the final comparison; do not use these disclosed cases as an independent test.

To rebuild, run `python build_dataset.py`. To validate, run `python validate_dataset.py` with Pydantic 2 installed. Rebuilding data requires regenerating the manifest before publication.
