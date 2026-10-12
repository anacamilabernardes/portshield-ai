# QLoRA adapter: opaque-prefix versus no-prefix diagnostic

Recorded on 2026-10-12. **Removing the prefix improved event classification but reduced all-field exact match. Neither input variant is selected for deployment on event F1 alone.** The adapter remains research-only.

## Scope and provenance

This compares opaque-prefix run `20261012T041428Z-f48de04f` with no-prefix run `20261012T044151Z-a123d07e`. Both use the same V1-trained adapter; there was no retraining. The 240 paired records retain their IDs and expected labels. Only the leading `Fictional exercise <opaque reference>: ` was removed. There are six distinct scenario bodies, each repeated 40 times.

The base is Qwen/Qwen2.5-1.5B-Instruct at revision `989aa7980e4cf806f80c7fef2b1adb7bc71aa306`. Adapter weights SHA-256: `32fbfa11cb627c4444df25a1d5087805bc1ba2a67837b62e89ac1568bb56a0b9`. Recorded adapter files, base provenance, inference-code hashes, package versions, GPU and generation overrides match the preceding run. The saved generation configuration is byte-identical. Generation uses `do_sample=false`, `max_new_tokens=256`, and `pad_token_id=151645`, on a Tesla T4.

Opaque-prefix dataset SHA-256: `7c2d7b063ca152302e8e234480da68bfc5c939ec0e002575b8e7cac53cbf0fbe`.
No-prefix dataset SHA-256: `1a257d3b8be3fb1a1c3fb3858a4445a57632f0f742ca141730b304bce85dd9c6`.

## Gains and regressions

| Metric | Opaque prefix | No prefix | Change |
| --- | ---: | ---: | ---: |
| Event macro F1 | 0.8609 | 1.0000 | +0.1391 |
| All-field exact match | 169/240 (70.42%) | 160/240 (66.67%) | -9 records; -3.75 pp |
| JSON parse validity | 240/240 | 240/240 | Unchanged |
| Schema validity | 240/240 | 240/240 | Unchanged |
| Event type accuracy | 211/240 | 240/240 | +29 |
| Affected function accuracy | 200/240 | 200/240 | Unchanged |
| Road access accuracy | 238/240 | 200/240 | -38 |
| Operational status accuracy | 240/240 | 240/240 | Unchanged |
| Equipment failure accuracy | 240/240 | 240/240 | Unchanged |
| Information sufficiency accuracy | 240/240 | 240/240 | Unchanged |
| Human review required accuracy | 240/240 | 240/240 | Unchanged |
| Abstention rate | 40/240 | 40/240 | Unchanged |
| Abstention precision / recall | 1.000 / 1.000 | 1.000 / 1.000 | Unchanged |
| Answerable coverage | 1.000 | 1.000 | Unchanged |
| Inference errors | 0 | 0 | Unchanged |

Full-record paired outcomes: 131 correct in both, 29 corrected, 38 regressed, and 42 incorrect in both. The net change is nine fewer fully correct records. Valid JSON and a valid schema do not establish semantic correctness.

| Test family | Opaque-prefix fully correct | No-prefix fully correct |
| --- | ---: | ---: |
| Weather disruption | 11/40 | 40/40 |
| Land access disruption | 40/40 | 40/40 |
| Equipment failure | 38/40 | 0/40 |
| Navigation restriction | 40/40 | 40/40 |
| Normal operations | 40/40 | 40/40 |
| Unknown / rumor | 0/40 | 0/40 |

## Evidence behind the changes

**Weather gain.** For "Gale conditions partially restricted vessel manoeuvring. Road access remains normal. No equipment failures.", all 40 no-prefix predictions correctly identify `weather_disruption`. Previously 29 were classified as `navigation_restriction`. These 29 records became fully correct.

**Road-access regression.** For "Equipment failure partially restricted cargo handling.", all 40 no-prefix predictions assign `road_access=restricted`; the expected value is `unknown`. The narrative supports restricted cargo handling, but does not state that road access is restricted. This adds 38 errors to the two already present in the opaque-prefix run. The other fields are correct.

**Persistent rumor error.** For "A rumour about cargo operations has no verified status.", all 40 predictions still assign `affected_function=cargo_handling` instead of the expected `unknown`. A mention of cargo operations does not establish a confirmed affected function under the recorded labels. Event type, information sufficiency and the other fields remain correct. Label-policy review should remain separate from these frozen historical targets.

Each no-prefix family has one distinct prediction across its 40 repeated records. This consistency includes the two systematic error patterns; it is not evidence of correctness.

## Interpretation and decision

The observations are consistent with sensitivity to the input prefix, but that sensitivity remains a **hypothesis**, not a proven causal mechanism. This is a historical paired comparison rather than a simultaneous randomized experiment. Matching recorded settings does not isolate execution order, session effects or numerical variation.

No overall improvement or operational readiness is claimed. Event F1 would favor the no-prefix run, while exact match and road-access accuracy favor the opaque-prefix run. Selection must consider all fields, unsupported assertions, abstention, schema validity and the consequence of each error. Neither variant is promoted by this analysis.

These results concern six repeated synthetic bodies, not 240 independent real-world scenarios. The V1 training history and its label-leakage limitations remain unchanged. These inspected examples are now diagnostic cases and must not serve as an independent blind test for subsequent versions.

## Follow-up

1. Review annotations for all fields, especially mention versus confirmed impact and field-specific evidence for road access.
2. Use paired repeated runs and counterbalanced execution order to investigate the prefix hypothesis while preserving all responses and settings.
3. Build diverse, independently reviewed scenarios, including weather versus confirmed equipment failure, negation, and unknown versus explicitly false values.
4. Predefine an evaluation decision using all-field exact match, per-field errors, event confusion, abstention and unsupported assertions. Evaluate subsequent changes on a fresh independent holdout.

## Preserved evidence

The [original no-prefix artifacts](../../results/no-prefix/diagnostic-20261012T044151Z-a123d07e/) include individual input texts, raw responses, expected values, predictions, differences, paired comparisons, confusion matrix, metrics, execution script, metadata and hashes. Files from the supplied archive are preserved without modification in this new directory. The [preceding diagnostic](prefix-v2-diagnostic-analysis.md) and its evidence remain available.

The supplied ZIP and its internal hashes were checked, and paired IDs, labels, prefix-only text transformation and outcome counts were verified. Hashes support artifact integrity, not proof of real-world validity. No inference or training was repeated during publication.
