# Reserved synthetic evaluation candidate V1

Status: reserved for evaluation, not evaluated; review completion reported by the project owner on 2026-10-12. See `review-record.json`.

This package contains 12 newly authored English scenarios: two per event class. It is a small synthetic evaluation pilot, not real-world validation. The 12 narrative bodies are distinct and not exact copies of the 720 historical rows or the 15 disclosed contrastive examples after prefix removal. This check does not prove semantic independence or absence from model pretraining. The same assistant authored these cases after examining earlier failures; the user has reported completing review. Reviewer independence and detailed adjudication have not been verified.

## Separation

- `inputs.jsonl`: IDs and narratives only. Pass only `text` to the model.
- `expected-labels.jsonl`: reserved scoring labels; keep out of prompts, training, retrieval and model selection.
- `records.jsonl`: schema-compatible combined records for the existing evaluator; scoring must keep targets outside model inputs.
- `diagnostic-registry.json`: already examined sets, excluded from future independent evaluation claims.
- `manifest.json`: frozen hashes and role restrictions.

The files are separated by convention, not encrypted or access-controlled. A reviewer can inspect the labels; the person tuning the model should not use these cases to change prompts or weights. This package is published on GitHub at the owner's request. It is an exposed evaluation set, not a secret or blind holdout. Repository publication does not authorize using it for training or retrieval.

## Evaluation protocol

1. Preserve the user-reported review record. Record any later field-level adjudication and reviewer independence explicitly. Any label revision creates a new version and manifest; retain the original snapshot.
2. Freeze the model/adapter revision, prompt, generation settings and the comparison decision before inference. This package must never enter training or retrieval. Develop only against the historical diagnostics and separately versioned training candidates.
3. Run each predeclared model configuration on identical inputs; record raw responses, parsed predictions, errors, timing and artifact hashes in a new output directory. Do not overwrite prior outputs.
4. Report all-field exact match, seven per-field accuracies, JSON/schema validity, event confusion and macro F1, and abstention precision/recall. Audit unsupported affected-function claims and unsupported road restrictions explicitly. Report counts alongside rates because this pilot is small. Do not choose a version solely on event F1 or silently invent a weighted score after seeing results.
5. If outcomes inform any prompt, model or annotation change, retire this version to diagnostic status and reserve a fresh set for the next independent comparison. Do not repeatedly tune against this reserve.

No model inference, training or performance claim has been made for this package. The original datasets, their labels and historical results remain unchanged. The set is published to GitHub as evaluation-only material. Publication and owner review do not establish independent real-world validation.
