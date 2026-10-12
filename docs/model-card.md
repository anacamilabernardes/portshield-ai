# Model card: PortShield research SLM adapter

Status: a research QLoRA adapter was trained and restored in Colab. Weights are not included
in this evidence package; independent validation remains pending. Base model:
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


## V1 experimental evidence update

See [reviewed results](experiments/qlora-v1-reviewed-results.md) for measured outcomes and
[dataset audit](data/dataset-v1-audit-and-v2-plan.md) for label-bearing input identifiers and
six distinct test scenarios repeated across 240 records. The observed 1.000 event macro-F1
and 83.3% exact match are not independent domain-validation results. Three exploratory
scenarios yielded only one schema-valid, checked-field-correct response for each model.
The adapter is research-only; no operational approval is claimed. Training loss near zero,
generalization and semantic consistency remain unresolved. Proposed annotation changes are
documented in [policy V2](data/annotation-policy-v2.md) and are not yet applied to the code.

## Corrected-prefix evaluation follow-up

The existing V1 adapter was evaluated without retraining on the same scenario bodies with
opaque prefixes: event macro-F1 0.8609, all-field exact match 169/240 (70.42%), schema validity
100%, abstention recall 100%. The base model scored 0.2825 macro-F1 and 0% exact match.
The previous three-case diagnostic and its failures remain valid separate evidence.
Only six distinct scenario bodies are represented; training leakage history is unchanged.
See [comparison](experiments/prefix-v2-comparison.md) for provenance, latency, field-level
counts and limits. This follow-up does not change the research-only status.
