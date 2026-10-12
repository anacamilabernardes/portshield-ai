# Existing-label review: rumor versus impact and field-specific evidence

Review date: 2026-10-12. Source commit: `390bd592974875342d699828c4986077610e6ddf`.

## Outcome

Reviewed 720 records across train, validation and test (240 each), covering all 18 distinct scenario bodies. **0 records require label changes under this review.** All seven stored target fields were compared with narrative-based decisions. The two priority fields are `affected_function` and `road_access`.

The expected labels already distinguish rumor from confirmed impact and do not transfer cargo restrictions to roads. The observed diagnostic failures are prediction-versus-target errors; these findings do not justify relabeling the targets to match model outputs.

## Rules applied

- A function mentioned only in rumor or unresolved contradictory reports is not a confirmed affected function: use `unknown`.
- Assign a specific affected function only when the text establishes actual impact; explicitly normal operations support `none`.
- Road access requires its own evidence. Cargo or navigation restrictions alone leave road access `unknown`.
- Preserve other independently supported fields. A missing road condition does not erase confirmed cargo impact.
- Equipment failure is `false` only with explicit exclusion, and `null` when unreported or unresolved. Human review remains required by policy.

## Review of all narrative families

| Split / family | Rows | Affected function retained | Road access retained | Rationale |
| --- | ---: | --- | --- | --- |
| test / equipment_failure-2 | 40 | cargo_handling | unknown | Restriction applies explicitly to cargo handling. It cannot be transferred to road access. |
| test / land_access_disruption-2 | 40 | land_access | restricted | Road restriction has an explicit clause; it is not inferred from rail closure. Equipment condition is unstated. |
| test / navigation_restriction-2 | 40 | navigation | normal | Draft restriction affects navigation. Normal road access and no equipment failures are explicitly stated. |
| test / normal_operations-2 | 40 | none | normal | Operations, roads and equipment condition each have explicit evidence. |
| test / unknown-2 | 40 | unknown | unknown | Cargo is mentioned only within an unverified rumor. No confirmed affected function or road condition is established. |
| test / weather_disruption-2 | 40 | vessel_manoeuvring | normal | Gale conditions affect manoeuvring. Explicit independent clauses support normal roads and no equipment failures. |
| train / equipment_failure-0 | 40 | cargo_handling | unknown | Cargo handling is explicitly suspended after crane failure. No road evidence is supplied. |
| train / land_access_disruption-0 | 40 | land_access | restricted | Blocked roads and suspended land access are explicit. Equipment condition is not stated. |
| train / navigation_restriction-0 | 40 | navigation | normal | Navigation restriction is explicit. Separate road and equipment statements justify their labels. |
| train / normal_operations-0 | 40 | none | normal | Normal operations, normal roads and absence of equipment failure are explicit. |
| train / unknown-0 | 40 | unknown | unknown | An unconfirmed possible disruption establishes neither a function nor road conditions. |
| train / weather_disruption-0 | 40 | vessel_manoeuvring | normal | Wind restricts vessel manoeuvres; separate clauses explicitly establish normal roads and no equipment failures. |
| validation / equipment_failure-1 | 40 | cargo_handling | unknown | Cargo handling is explicitly halted with an equipment fault. No road evidence is supplied. |
| validation / land_access_disruption-1 | 40 | land_access | restricted | Both road and land-access restrictions are explicitly stated. Equipment condition is not stated. |
| validation / navigation_restriction-1 | 40 | navigation | normal | Navigation is explicitly suspended. Roads remain normal and equipment failure is explicitly excluded. |
| validation / normal_operations-1 | 40 | none | normal | All operations and roads are explicitly normal; no crane failures supplies the relevant equipment exclusion in this synthetic scope. |
| validation / unknown-1 | 40 | unknown | unknown | The narrative explicitly presents contradictory reports; neither impact nor equipment condition is resolved. Roads are unmentioned. |
| validation / weather_disruption-1 | 40 | vessel_manoeuvring | normal | The storm and manoeuvring impact are explicit; roads and absence of equipment failures have their own evidence. |

## Priority cases and coverage gaps

- Test rumor: "A rumour about cargo operations has no verified status." All 40 labels already use `affected_function=unknown`, `operational_status=unknown`, `road_access=unknown`, and `equipment_failure=null`.
- Test cargo restriction: "Equipment failure partially restricted cargo handling." All 40 labels already use `affected_function=cargo_handling`, `operational_status=partial_restriction`, and `road_access=unknown`.
- The three equipment-failure families all leave roads unknown: 120 records total. Road restrictions occur only where roads are explicitly restricted or blocked.
- The rumor explicitly mentioning cargo appears only in test. Training uses a generic unconfirmed report and has no matched rumor/confirmed-impact contrast for the same activity.
- The equipment family always has unknown roads; the current set lacks matched cargo-impact cases with independently normal or restricted roads. Repeating labels is not equivalent to teaching these distinctions across varied evidence.

## Change log and preservation

No label changes were applied. No dataset regeneration, training, model-selection change or historical-result rewrite was performed. Source hashes match the published dataset manifest. Prefix-bearing and no-prefix diagnostic targets remain frozen.

See [record-level review](label-review-records.jsonl) for every input, original and reviewed target, explicit change map and rationale. See [summary and source hashes](label-review-summary.json). The [source snapshot](source-snapshot.json) also preserves the fetched policy and generator at the reviewed commit.

## Limits and next work

This is an assistant review against the stated policy, not independent domain-expert adjudication. There are 18 authored bodies, not 720 independent situations. In particular, the validation contradiction is explicitly designated contradictory and remains unresolved; future examples should identify evidence provenance more precisely. The validation normal-operations family excludes crane failures; broader equipment taxonomy should be clarified in a future dataset rather than silently changing historical targets.

Before further training, add separately versioned contrastive training examples and obtain independent annotation review. Keep the already inspected test cases as diagnostics. Reserve newly authored independent cases for final evaluation, and assess all-field exact match, per-field errors, unsupported assertions and abstention alongside event F1.
