# Reserved comparison: Qwen base versus current QLoRA adapter
Run: reserved-comparison-20261012T053216Z-3b6e9ac5
Completed in Google Colab on 2026-10-12. No training performed.

## Scope and controls

12 reserved synthetic examples, 24 individual responses. Both models used the same input texts, labels, prompt, generation parameters and base weights. The current adapter was loaded only for the adapter arm. Generation used do_sample=False, max_new_tokens=256, seed 42, float16, and no 4-bit quantization. Dataset and weight hashes were checked before inference. This is an inference comparison of an existing QLoRA-trained adapter, not a new QLoRA training run.
Base: Qwen/Qwen2.5-1.5B-Instruct
Base revision: 989aa7980e4cf806f80c7fef2b1adb7bc71aa306
Dataset source commit: 7bfd2b4f2839522d1d9505e22c10f3a98bfefb18
Dataset SHA256: 57b1bbf66994c827fe7cb61433092e038ce3fdf16b8ba3b6f5306a8ae61839b0
Base weights SHA256: dd924a11b4c220f385b51ffa522daea7c9f3d850e31b162bb5661df483c6d3ee
Adapter weights SHA256: 32fbfa11cb627c4444df25a1d5087805bc1ba2a67837b62e89ac1568bb56a0b9

## Results

| Measure | Base | Current adapter |
|---|---:|---:|
| JSON parseable | 12/12 | 12/12 |
| Schema valid | 2/12 | 10/12 |
| All fields correct | 1/12 | 3/12 |
| Official event macro F1 | 0.222222 | 0.611111 |
| Inference failures | 0 | 0 |

## Raw-field errors (out of 12)

| Field | Base errors | Adapter errors |
|---|---:|---:|
| affected_function | 4 | 2 |
| road_access | 2 | 2 |
| operational_status | 2 | 2 |
| equipment_failure | 4 | 4 |
| information_sufficiency | 8 | 2 |
| event_type | 3 | 5 |
| human_review_required | 0 | 0 |

## Metric interpretation

Raw-field errors compare each parsed JSON value independently with the frozen target, including responses that fail validation in another field. The existing official evaluator gates field scores on whole-response schema validity. Its field error counts are therefore different:
event_type 10 -> 5; affected_function 10 -> 3; operational_status 10 -> 4; road_access 11 -> 4; equipment_failure 11 -> 6; information_sufficiency 10 -> 3; human_review_required 10 -> 2.
The official event F1 gain must not be interpreted as a uniform improvement in event classification: raw event errors increased from 3 to 5.

## Paired findings

SYN-RESERVE-0005 was entirely correct in both arms. 0002 and 0006 became entirely correct with the adapter. Nine remained incorrect in both arms. No previously entirely correct response became incorrect; individual-field regressions did occur.
affected_function: corrections in 0002 and 0007; errors persist in 0008 and 0011.
road_access: 0002 corrected unknown versus normal; 0007 regressed normal to restricted despite explicitly normal roads. Both still infer normal roads in 0009 although road access is not covered.
event_type: regressions in 0004 (land_access_disruption -> navigation_restriction) and 0008 (navigation_restriction -> suspended). In 0008, suspended belongs to operational_status, not event_type.
equipment_failure: four corrections (0002, 0006, 0008, 0009) and four regressions (0001, 0003, 0007, 0010). All four regressions replace unknown/null with false despite no explicit exclusion of a fault.
information_sufficiency: seven corrections and one regression (0011).
Rumor case 0011 remains a failure: both assert cargo_handling and a definite event/status without confirmed impact; the adapter additionally changes insufficient to sufficient.
Case 0012 remains incorrect in both: an unresolved cause is assigned navigation_restriction instead of unknown, while the other raw fields match.
Neither model abstains as required in the two target-unknown event cases.

## Conclusion

The adapter improves structure and affected_function accuracy, but only 3/12 responses match all target fields. Road errors do not decrease, and event classification regresses on two cases. This does not satisfy a criterion requiring simultaneous progress on affected_function, road_access and full-record correctness without meaningful regressions. Retain both arms and all evidence; do not select a model from event F1 alone.

## Limitations and next use

The sample contains only 12 synthetic examples, two per event label, and was publicly available before evaluation. It is not evidence of blind, real-world independent validation. Results are scored against the existing frozen annotations. Having examined these outcomes, use the cases as regression diagnostics if they inform future changes; reserve new independently reviewed cases for the next final evaluation.

## Preserved evidence

This run directory preserves all 24 individual responses, frozen inputs and labels, original metric files, generation configurations, code snapshots, hashes and runtime metadata. All 23 original artifacts were verified byte-for-byte against the Colab artifact-hashes.json. The original artifact manifest is unchanged. The additional raw-event confusion matrices were derived after inference and are covered by publication-validation.json and the repository manifest.

- [Run metadata](run-metadata.json)
- [Base responses](base-predictions.jsonl) and [adapter responses](adapter-predictions.jsonl)
- [Paired comparison](comparison.json)
- [Original artifact hashes](artifact-hashes.json)
- [Validation](publication-validation.json)

The event confusion matrices named *-event-confusion.json use the official schema gate; *-raw-event-confusion.json retain actual event field values, including invalid values such as suspended. The second view makes the classification regressions visible.

No weights, credentials or notebook outputs are included. The runner is the original Colab snapshot and expects its documented /content paths and the frozen input directory. It creates a new run on execution; replaying inference is not necessary to inspect this evidence. Historical files remain intact.
