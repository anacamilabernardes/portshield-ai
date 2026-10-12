# PortShield annotation and error review

## Decision and closure boundary

Retain the existing adapter. The assistant-assisted review of 78 source records (54 training, 12 development-validation and 12 historical diagnostic records) found no mandatory target changes under the existing conventions. All 546 field decisions are retained provisionally. Independent human annotation approval remains open; this document closes the evidence analysis, not that approval or production readiness.

Historical datasets, labels, predictions and reported metrics are unchanged. The record-level review is in [annotation-review.jsonl](annotation-review.jsonl); [annotation-change-log.json](annotation-change-log.json) records zero changes. Retaining a label under an existing convention does not establish that the convention matches a real customer's needs.

## Recounted results

Counts use strict individual-field comparison, including types and missing fields, even if other fields invalidate the schema. All-field exact match additionally requires schema validity. false, null and a missing field are distinct. Schema-gated metrics remain in the original comparison and must not be mixed with these raw-field counts.

| Collection | Measure | Existing | V2 |
|---|---|---:|---:|
| Development validation, 12 | affected_function errors | 8 | 8 |
| Development validation, 12 | road_access errors | 5 | 3 |
| Development validation, 12 | operational_status errors | 5 | 7 |
| Development validation, 12 | equipment_failure errors | 5 | 3 |
| Development validation, 12 | event_type errors | 6 | 3 |
| Development validation, 12 | information_sufficiency errors | 4 | 2 |
| Development validation, 12 | human_review_required errors | 0 | 0 |
| Development validation, 12 | All-field exact matches | 0 | 1 |
| Development validation, 12 | Schema-invalid responses | 7 | 2 |
| Historical diagnostics, 12 | affected_function errors | 2 | 2 |
| Historical diagnostics, 12 | road_access errors | 2 | 1 |
| Historical diagnostics, 12 | operational_status errors | 2 | 1 |
| Historical diagnostics, 12 | equipment_failure errors | 4 | 3 |
| Historical diagnostics, 12 | event_type errors | 5 | 0 |
| Historical diagnostics, 12 | information_sufficiency errors | 2 | 1 |
| Historical diagnostics, 12 | human_review_required errors | 0 | 0 |
| Historical diagnostics, 12 | All-field exact matches | 3 | 7 |
| Historical diagnostics, 12 | Schema-invalid responses | 2 | 1 |

## Findings and targeted actions

The ledger contains 84 wrong-field instances across both adapters and collections; this is not 84 separate records. V2 has nine schema-valid but incomplete/incorrect records among the 12 validation cases, and four among the 12 diagnostic cases. A successful schema check is therefore insufficient evidence of semantic correctness.

| Observed error | Concrete evidence | Next action |
|---|---|---|
| Mentioned activity becomes asserted impact | V2 assigns cargo_handling in SYN-V2R-0011/0012 and SYN-RESERVE-0011 despite conflicting or unverified reports | Add new source-conflict and corroboration families; retain independently known fields |
| Primary service is confused with another service | V2 regresses from land_access to cargo_handling in SYN-V2R-0003/0004; normal cargo distracts from rail scope | Review the service-scope convention, then create different multi-service narratives |
| Roads are inferred without evidence | V2 returns normal in SYN-V2R-0007/0008 and SYN-RESERVE-0009; restricted in SYN-V2R-0004 | Contrast explicit normal/restricted roads with omission; neither normal operations nor a bridge mention determines roads |
| Full stop and reduced capacity are confused | V2 returns partial_restriction in SYN-V2R-0001/0002/0003/0005 and suspended in SYN-RESERVE-0004 | Contrast full stop, partial continuity and recovery within the explicitly scoped service |
| Explicit fault exclusion becomes unknown | V2 returns null in SYN-V2R-0001/0002 and SYN-RESERVE-0002/0008/0009 where the target is false | Separate explicit inspected exclusion from unassessed equipment; do not reward more null outputs unconditionally |
| Historical fault persists after recovery | Both adapters retain equipment_failure as event type in SYN-V2R-0009/0010 | Add superseded-report and recovery families, with inspected repair versus unassessed replacement |
| Internal contract inconsistency | V2 schema fails on SYN-V2R-0004/0010 and SYN-RESERVE-0008 | Preserve exact validation errors; teach that insufficient information concerns event type under this schema |

These are observed patterns, not established causal mechanisms. Dataset changes, initialization and optimization differ between adapters. No claim that more examples alone will fix the errors is warranted.

## Annotation conventions requiring human adjudication

| ID | Convention retained for this review | Why confirmation is needed | Records to inspect |
|---|---|---|---|
| P1 | land_access includes rail; status concerns the primary stopped rail service even while roads work | A customer might instead expect whole-terminal status; those are different tasks | SYN-V2R-0003/0004 |
| P2 | Current normal operations can coexist with an unknown equipment condition after replacement | Scope of equipment_failure must specify current assessment and relevant assets; past failure is not automatically current | SYN-V2R-0009/0010 |
| P3 | Global normal operations does not assess roads unless roads/gates are explicit | Everyday language could be interpreted more broadly; document field-specific evidence boundaries | SYN-V2-0031/0032/0037/0038/0041/0042; SYN-RESERVE-0009 |
| P4 | Conflicting reports leave affected_function unknown even when both mention cargo | The field means confirmed impacted service, not topic mentioned in the report | SYN-V2R-0011/0012; rumor cases |
| P5 | information_sufficiency describes event-type evidence; other fields can remain known | Its name may suggest completeness of the whole record; rename or document in a future version if needed | SYN-V2-0006/0008; SYN-RESERVE-0012; all unknown-event rows |

None is resolved by changing targets to agree with predictions. If adjudication changes a convention, create a new annotation version with before/after values and reasons, and rescore both adapters consistently. Preserve the old results; do not silently compare metrics from different target versions.

## Limits and evidence

All human_review_required labels are true. Zero errors on that field does not demonstrate calibrated human-review decisions. Families contain correlated contrasts, so 12 rows are not 12 independent real-world scenarios. These examined cases remain development/regression diagnostics; their bodies and close paraphrases must not become training examples while retaining an independence claim.

[field-errors.jsonl](field-errors.jsonl) lists every observed wrong field across 48 responses. [paired-transitions.json](paired-transitions.json) includes corrections and regressions, including unchanged cases. [metrics-recount.json](metrics-recount.json) matches the preserved comparison; [verification.json](verification.json) records checks. Full source inputs and responses are in evidence/, identified by [source-hashes.json](source-hashes.json).

**Closure:** evidence analysis and provisional annotation review complete; independent human adjudication and the next experiment's approval gates remain pending. No training or promotion is authorized by passing a documentation check.
