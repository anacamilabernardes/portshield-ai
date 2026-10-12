# PortShield V2 pilot evidence

Start with `results/training-v2-20261012T062041Z-d8f05304/REPORT.md` for the English paired comparison, and `REVIEW-AND-PROTOCOL.md` for the data review and experiment rules.

The result package contains the 54 training records, 12 development-validation records, 12 historical diagnostic records, 48 individual responses, field differences, paired corrections/regressions, confusion tables, training metrics, loss-mask checks, source snapshots and hashes. The previous incomplete execution is preserved in `superseded-attempt/`.

## Model storage

Model weights are **not included in this local evidence package**. The new adapter remains in the Colab session at:

`/content/portshield-ai/results/runs/training-v2-20261012T062041Z-d8f05304/adapter`

The ready-to-download ZIP is:

`/content/portshield-v2-adapter-20261012T062041Z-d8f05304.zip`

ZIP SHA256: `bb553378bd81bf112986b56b42787226e7087ce4b33aa8dbe3f390ff5fb603ac`.

Adapter weights SHA256: `caab5d8fa23a442cc0122ddbd702d3fe75650201b344ea621260e97ee50c435f`.

The owner saved the ZIP locally. On 2026-10-12 its SHA256, archive CRC and all nine adapter-file hashes were verified. See `results/training-v2-20261012T062041Z-d8f05304/backup-verification.json`. Weights are archived separately and are not published in this repository. It contains the adapter, tokenizer, base provenance and training records of configuration/metrics; it does not contain the full base model or optimizer checkpoints. Loading requires the same Qwen base revision. Keep the current adapter unchanged.

## Integrity

The original `artifact-hashes.json` includes weights and tokenizer files still in Colab. It also captured `comparison-console.log` before the final summary was printed. Its historical bytes are preserved. The completed console log was checked separately against Colab SHA256 `721a1872ff64b0e4b7f310ff23c21fee5405d2679246ceb622ff0b9a0fcf2df6`.

`local-verification.json` records an independent recount of all 48 responses and 24 paired transitions, plus 36 byte-identical original evidence artifacts. `publication-manifest.json` covers the files included in this local delivery. This directory is the GitHub evidence publication. The original run manifest remains preserved; the publication manifest covers the final files here.
