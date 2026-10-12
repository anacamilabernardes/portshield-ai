# Corrected-prefix evaluation evidence

Source: user-supplied `portshield-prefix-v2-evaluation.zip`, reviewed on 2026-10-12.
The two JSON reports and JSONL dataset are preserved as UTF-8 content from that archive.

- `qwen-base-prefix-v2.json`: Qwen base model evaluation, 240 attempts.
- `qwen-adapter-prefix-v2.json`: existing V1 QLoRA adapter evaluation, 240 attempts.
- `test-prefix-v2.jsonl`: actual dataset supplied with the reports; SHA-256
  `7c2d7b063ca152302e8e234480da68bfc5c939ec0e002575b8e7cac53cbf0fbe`.

The dataset equals the published corrected V2 test bytes, but contains six scenario bodies
repeated 40 times each. It is a prefix correction, not the completed diverse V2 dataset plan.
No model weights, credentials, real operational records or per-example predictions are included.

Execution used the existing project evaluator with `--backend hf`, `--model models/base`,
`--data data/synthetic/test-prefix-v2.jsonl`; the adapter run added
`--adapter models/adapter`. No retraining was requested or performed in this comparison.

See [reviewed comparison](../../docs/experiments/prefix-v2-comparison.md).
Historical evidence remains under `results/qlora-v1/`. Hashes are listed in the repository
manifest. Run timestamps and adapter hashes are absent from the supplied aggregate reports;
do not infer them from this documentation's recording date.
