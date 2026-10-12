# PortShield next experiment work plan and approval criteria

## Objective and status

Reduce confirmed-service and road-evidence errors while improving all-field correctness, without concealing regressions in other fields. Keep the current adapter unchanged. The steps and numerical gates below are proposed engineering acceptance criteria for a future experiment, not user-approved thresholds or demonstrated production performance. Agree and freeze them before running that experiment; do not relax them after seeing its results.

## Work packages and responsibility

Roles are proposed assignments, not staffed commitments. One person may fill several development roles; independent annotation review requires a person other than the author/AI assistant. Effort ranges are planning estimates, not deadlines.

| Step | Deliverable and owner | Dependency and estimated effort | Completion gate |
|---|---|---|---|
| 1. Adjudicate conventions | Data owner plus independent domain reviewer: resolve P1–P5, review 78 records without model predictions, log disagreement and resolution | Current review; 1–2 person-days | All seven fields reviewed, every disagreement resolved with rationale or explicitly excluded in a new version; reviewer identity/role and date recorded |
| 2. Freeze task and acceptance | Project lead plus evaluation owner: sign task scope, field rules, baselines, thresholds, compute/time ceiling and promotion authority | Step 1; half a day | No unresolved policy choices; hashes and version fixed; no test-driven threshold changes |
| 3. Build new development families | Data author and independent reviewer: target corroboration, service scope, degree of restriction, temporal updates, equipment evidence and independent roads | Step 2; 2–3 person-days | At least three genuinely different new training families per weakness as an initial design target; each minimal contrast stays intact; all labels reviewed; no copies/close paraphrases of examined evaluation bodies |
| 4. Audit splits and prepare evaluation | Evaluation owner: family map, duplicate/near-duplicate screening with manual decisions, label coverage, new development validation and separately reserved final families | Step 3; 1–2 person-days | Zero exact cross-split duplicates and zero family overlap by the reviewed definition; disclose conceptual overlap; include every event label and all three equipment states; no label-bearing prefixes or metadata in model prompts |
| 5. One bounded pilot | ML engineer: a fresh candidate with frozen settings, assistant-only mask/truncation checks and separate output directory | Steps 1–4 passed; GPU time estimated only after configuration freeze | Baseline and candidate use identical evaluation inputs, base revision, prompts and generation settings; complete raw outputs, environment/configuration/weights hashes; no checkpoint selection on final-test performance |
| 6. Paired assessment | Evaluation owner and project lead: per-field confusion, paired corrections/regressions, full-record match, model decision and independent final review | Step 5; 1 day analysis | All development gates below pass; then run the frozen final evaluation once under the predeclared policy. Failure retains the incumbent and triggers a documented next-cycle decision |

Planning envelope: approximately 5.5–8.5 person-days plus reviewer availability and GPU execution. These are elapsed task-effort estimates; additional independent-review staffing can increase total person-days. Do not book compute or promise delivery until resources and scope are agreed. If no independent reviewer is available, close the pilot documentation but keep independent approval pending.

## Proposed gates on the existing frozen development collections

These are advancement gates for another research candidate, not deployment gates. Compare against the **existing adapter**, not merely the weaker fields of V2. Apply each collection separately; improvement on historical diagnostics cannot offset failure on validation. All conditions are conjunctive.

| Criterion | 12 development-validation cases | 12 historical diagnostic cases |
|---|---:|---:|
| affected_function errors | At most 6 (existing 8) | At most 2 (existing 2) |
| road_access errors | At most 3 (existing 5) | At most 2 (existing 2) |
| All-field exact matches | At least 4 (existing 0) | At least 3 (existing 3) |
| operational_status errors | At most 5 | At most 2 |
| equipment_failure errors | At most 5 | At most 4 |
| event_type errors | At most 6 | At most 5 |
| information_sufficiency errors | At most 4 | At most 2 |
| human_review_required errors | 0 | 0 |
| Invalid JSON, schema-invalid responses, inference errors | 0 | 0 |

Additional paired gate: no newly incorrect affected_function or road_access value on a case where the existing adapter was correct; no previously exact record may become incorrect. For other fields, enumerate every individual regression even if its aggregate ceiling passes; unresolved severe regressions block advancement. Preserve false/null distinction and treat missing/type-invalid fields as wrong. Exact match requires valid schema and all seven fields correct. Event F1 is reported but cannot override any gate.

These thresholds deliberately require improvement in both primary error counts and complete-record correctness, plus recovery from the status regression. They are practical research targets on small exposed sets, not statistically established safety limits. A future label-version change requires rescoring the incumbent and explicitly redefining these gates before the next candidate is evaluated.

For this proposed gate, a severe regression means newly asserting confirmed impact from an unverified/conflicting report, reporting normal or partial operation for an explicitly fully stopped primary service, asserting a known equipment state when unassessed (or unknown when explicitly excluded), suppressing required human review, or returning no usable response. A newly introduced severe regression relative to the incumbent blocks advancement even if averages improve. Freeze this definition with the task owner before the run.

## New validation and independent final evaluation

Do not infer final acceptance from the 24 examined cases. Before training, the evaluation owner must specify new-validation sample size, family coverage and numerical thresholds; without these the experiment is not ready. Use family-level reporting and paired uncertainty estimates; small correlated samples cannot support broad generalization claims.

For a final evaluation, freeze tasks, family definitions, source permissions, sample-size rationale, per-field minimums, severe-error limits and resource requirements before model predictions are exposed. Sample size depends on the precision and error tolerance required by the intended use; no sufficient final-test size has been established here. Keep its text/labels out of training, prompt tuning and checkpoint selection. Run the incumbent alongside the candidate under identical conditions. After examining final errors to guide development, retire that set to diagnostics and reserve a new final set for the next cycle.

Independent synthetic evaluation supports only synthetic-task claims. Production promotion additionally requires authorized real-world evaluation, operational error tolerances, measured latency/memory/cost, human escalation, monitoring, rollback and accountable owner approval. Those criteria remain unestablished; no production promotion can occur under this plan's small-set gates.

## Risks and contingencies

| Risk | Detection | Response |
|---|---|---|
| Convention ambiguity is mistaken for model failure | Independent annotation disagreement | Resolve policy before training; version labels and rescore both adapters |
| Repeated development cycles overfit exposed cases | Gains confined to known families | Use new family-level validation; reserve a fresh final collection |
| Better F1 hides a semantic regression | Paired field tables and exact match | Reject promotion when any mandatory gate fails |
| More null predictions mimic better uncertainty | Track true/false/null confusions separately | Require evidence-specific equipment contrasts and preserve explicit exclusions |
| Runtime interruption or corrupted artifacts | Checkpoints, exit status, archive/hash verification | Separate run IDs; preserve current adapter; verify local backup before ending Colab |
| Compute ceiling exceeded | Elapsed time and memory checks | Stop the experiment at the predeclared ceiling; retain partial-run evidence; replan rather than silently changing settings |

## Immediate actions

Assign an independent reviewer, resolve P1–P5, and approve or amend the proposed gates before building the next training revision. No new training has been started by this review. No causal diagnosis, independent annotation sign-off, final-test approval or production readiness is claimed.
