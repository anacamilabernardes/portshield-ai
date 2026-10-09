# Model card: proposed PortShield SLM adapter

Status: training pipeline implemented; no PortShield trained model or adapter distributed. Base option:
Qwen/Qwen2.5-1.5B-Instruct, Apache-2.0 per upstream model card. Resolve/review the exact revision via
`scripts/acquire_model.py`; record model checksums, license, dataset manifest, config and dependency freeze.

Intended use: classify/extract English synthetic maritime events and emit the EventAnalysis contract.
Required human review; abstain on insufficient/ambiguous evidence. Out of scope: real operational
decisions, incident forecasting by language generation, regulatory interpretation, personal profiling.

Training data: six categories × three authored paraphrase families, one family per category per split;
40 variants per family by default. Fictional identifiers and order differ; semantic diversity remains small.
No real facility, nonpublic document or personal data. Language: English. Portuguese is unvalidated.
LoRA/QLoRA defaults: rank16, alpha32, dropout .05, 3 epochs, lr2e-4, seed42, assistant-only loss,
one-GPU FP16 compute, NF4 base weights for QLoRA, held-out validation, test excluded.

Metrics: event macro F1 (six fixed classes), field accuracy, exact match, JSON parse/schema validity,
abstention precision/recall and answerable coverage. Compare base, adapter, merged FP16, NF4 and private
vLLM on the identical test set. Record errors, distributions and human relevance assessment.
Latencies and memory are measured independently of model quality. No superiority or efficiency claim yet.

Limitations: repeated templates, lexical shortcuts, false confidence, negation/compound incidents,
base-model biases, drift and source poisoning. Safety measures do not remove these risks. Deployment
requires independent domain data, reviewed artifact lineage, access control, resource/SLO testing and rollback.
After a run, append exact snapshot/adapter hashes, hardware, metrics, known failures and approval decision;
do not replace unmeasured fields with expectations. Code MIT; weights retain upstream terms.
