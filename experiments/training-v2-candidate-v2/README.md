# Family-level split and full-field review — training V2 candidate 2

This revision supersedes the **split**, not the historical evidence, of candidate 1. The original 54 texts and their seven target fields are unchanged. The previously published package remains preserved. No model training or inference was run.

## Finding

Candidate 1 kept each minimal contrast group intact, but did not keep broader narrative families intact. Examples include e01/e04 versus e06 (paraphrased global normal operations), r01 versus r05 (unverified/verified weather stoppage of cargo), r02 versus r06 (unverified/verified mechanical cargo slowdown), a01 versus a05 (confirmed cargo-system fault with independent roads), and a03/a04 versus a06 (navigation restrictions with road triples). Status contrasts s02/s05 and s03/s06 also used the same reasoning structure across splits. Distinct object names or group IDs are not sufficient separation.

## Corrective split

- **Training: 54 existing examples, grouped into nine broader families.** The 18 former development-validation rows move into training with all their siblings. This is an explicit role change, not an independent-evaluation claim. The package had not been trained before this reassignment.
- **Validation: 12 new examples in six separate structural families.** These cover superseding bulletins, rail-only land disruption, an equipment incident affecting manoeuvring rather than cargo, a lifted total navigation stop with a continuing restriction, recovery after an outage, and conflicting current reports. Each pair stays entirely in validation.
- All six event labels remain represented in both splits. No independent test set is included. The 12 previously evaluated reserve cases and other historical diagnostics are not included.

The validation families were deliberately made different in narrative structure, not merely renamed. Shared task concepts such as weather, roads and equipment are unavoidable and are not by themselves duplicate scenarios. This small synthetic split does not prove semantic independence or real-world generalization. The 12 new validation rows are disclosed development material; reserve a fresh independent final test later.

## Seven-field audit

Reviewed all 378 target values in the existing 54 records: **zero label changes**. Reviewed 84 values for the 12 newly authored validation records, for 462 field decisions in total. `REVIEW.md` and `field-review.jsonl` record every decision and its rationale.

Rumor does not establish affected cargo operations; independent roads remain usable. Unassessed equipment stays null, explicitly excluded failure is false, and confirmed failure is true. A confirmed impact with unresolved cause retains its known function/status but unknown event type. `information_sufficiency` concerns event type under the existing schema. `suspended` belongs only to operational_status. Human review remains required in every record.

New edge-case conventions are explicit in the narratives: the latest superseding bulletin governs current conditions; operational_status is scoped to the primary affected service (rail service can be stopped while roads operate); historical faults do not automatically imply a current fault; restored operations do not independently establish the condition of replaced equipment. In the conflicting-primary-report case, independently known road restrictions do not replace the explicitly selected primary subject.

## Evidence and reproducibility

`data/training-v2-candidate-v2/` contains train/validation JSONL, per-field audit, per-record split changes, family map, validation report, and the top cross-split word-overlap pairs. Word overlap is a screening aid, not proof that two stories are independent. `source/` preserves the candidate-1 inputs and annotations for audit only; never pass those files to training as additional rows.

Run `python build_revision.py` with Pydantic 2 installed to reproduce the revision, assertions, review and ZIP. Only `text` is model input. IDs, families, annotations and expected targets must not be concatenated into prompts. The manifest records byte hashes. No active training configuration is changed.

The user's reported review of candidate 1 remains historical; it is not represented as approval of the new validation examples or this new split. This revision has assistant review only. Future edits to narratives or labels need a versioned change record. Do not tune against these validation examples and later describe them as an independent test.
