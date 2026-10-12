# Evidence provenance

- qwen-before-training.json and qwen-after-training.json: original user-provided aggregate reports.
- predictions.jsonl, errors.json and report.md: user-provided post-training diagnostic rerun.
- three-scenario-diagnostic.json: original JSON downloaded from Colab and supplied by the user,
  preserved byte-for-byte. It replaces the earlier console reconstruction. All six records
  match the reconstruction except Markdown link formatting in validation-error messages;
  predictions, validation outcomes and conclusions are unchanged.
- three-scenario-console.txt: supplied console text retained as provenance. It includes local
  Colab paths and public library warnings; no credentials or private MPOR records were observed.

The original report.md is retained as historical output; the reviewed interpretation is in
../../docs/experiments/qlora-v1-reviewed-results.md. In particular, the dataset audit identifies
label-bearing input IDs and only six distinct V1 test scenario texts.

None of the files contains adapter or base-model weights. Full-field diagnostic target labels
are separately proposed in ../../data/diagnostics/three-scenario-reviewed-labels.json.
