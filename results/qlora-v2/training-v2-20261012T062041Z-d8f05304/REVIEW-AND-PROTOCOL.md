# V2 pre-training review and frozen pilot protocol

Source: family-split candidate 2, published at commit `9e3a16fc4b9e6861646509c7553f13eac20f7cec`.

The 54 training records were reread against all seven target fields. No further label changes were identified. The 12 development-validation records remain separate by narrative family. The seven-field rationale audit is preserved in the published candidate package. This is an assistant review, not an independent human annotation study.

The key conventions remain: an unverified allegation does not establish the affected service; a confirmed effect may have an unknown cause; road status requires its own evidence; unassessed equipment is null and an explicitly excluded fault is false; a stopped service maps to operational_status=suspended, never an event class. Human review is always required. Independently established fields remain usable even when the primary event is unresolved.

## Frozen experiment

- Train a fresh adapter from the same Qwen2.5-1.5B-Instruct base revision. Do not resume or overwrite the current adapter.
- Use 54 training examples, three epochs, seed 42, rank 16, alpha 32, dropout 0.05, learning rate 0.0002, batch size 1 and gradient accumulation 8. This is a small pilot, not a claim of an optimal configuration.
- Execution correction: Transformers 4.51.3 inferred 18 updates and stopped the first attempt at epoch 2.59. Preserve that attempt as execution evidence. The corrected fresh run explicitly requests 21 updates (seven per epoch, including the partial accumulation group) and asserts that the recorded final epoch is exactly 3.0. This correction preceded task-output comparison; it is not checkpoint selection based on task performance.
- Use assistant-only loss. Check that every serialized target is present in the supervised tokens and that prompt tokens are masked. A 2,048-token ceiling fails on overlength examples rather than truncating them; actual token lengths are reported before training.
- Use development validation for loss reporting. Select the final epoch by this predeclared rule; do not choose a checkpoint after inspecting task metrics.
- Compare current and new adapters on the same 12 development-validation examples and, separately, the 12 previously evaluated diagnostic cases. Neither collection is an independent final test. No evaluation text or label is added to the training split.
- Use the same FP16 base, prompt, greedy generation and 256-new-token limit for both adapters. Preserve generation configurations, source snapshots, input hashes, adapter hashes, environment, individual responses and errors.

## Assessment priorities

Primary outcomes are errors in affected_function and road_access, plus exact agreement across all seven fields. Report schema-gated accuracy and strict individual-field comparisons separately, so a schema failure does not conceal the source of the error. Missing fields remain incorrect; false and null are different values.

For every field, preserve paired corrections and regressions and a confusion table. Inspect equipment_failure, operational_status, information_sufficiency, human_review_required and event_type alongside the primary outcomes. Event macro F1 is supplementary and cannot select a winner by itself. A gain in one field does not cancel an unreported regression in another.

This comparison changes the training dataset and uses a fresh adapter. It does not isolate the causal effect of each new example or establish real-world generalization. The 54 examples are intentionally related contrasts; row counts overstate the number of independent scenarios. New final-test families will be required after development decisions are frozen.
