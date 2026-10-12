# PortShield AI — Executive Summary

**An experimental case study in structured event analysis and evidence-based model selection**  
**Ana Camila Bernardes | October 2026**

### Problem and objective

Maritime incident reports may mix confirmed disruption, rumors, incomplete information and unrelated operational conditions. Converting these reports into structured records requires preserving those distinctions: an unverified allegation does not establish cargo impact, and a cargo restriction does not establish restricted road access.

PortShield AI explores whether a small open-weight language model can support this task. Its output covers seven fields: event type, affected function, operational status, road access, equipment failure, information sufficiency and required human review. The project is a research prototype using synthetic data; it has not demonstrated production readiness.

### Solution and experimental approach

The prototype uses Qwen2.5-1.5B-Instruct with a QLoRA-trained adapter, structured-output validation and field-level evaluation. Model responses, expected labels, differences, configurations and artifact hashes are retained for audit.

Early evaluation exposed two weaknesses in the original dataset: input identifiers revealed expected event classes, and many records repeated a small set of scenarios. Those findings limited the interpretation of initially strong scores. Subsequent work removed revealing prefixes, examined individual errors and revised annotation guidance.

A new training candidate introduced contrasts addressing unverified impact, independent road conditions, unknown versus explicitly excluded equipment failure, and event type versus operational status. The revised split contained **54 training examples across nine narrative families** and **12 development-validation examples across six separate families**. A fresh adapter completed three training epochs and was compared with the existing adapter using the same base model, prompts and generation settings.

### Results and decision

**Development validation — 12 examples**

| Measure | Existing adapter | New V2 adapter |
|---|---:|---:|
| Affected-function errors | 8 | 8 |
| Road-access errors | 5 | 3 |
| Operational-status errors | 5 | 7 |
| Completely correct records | 0 | 1 |
| Schema-invalid responses | 7 | 2 |

On a separate set of **12 previously examined diagnostic cases**, completely correct records increased from **3 to 7**, although individual regressions remained. The comparison preserved **48 individual responses across 24 paired cases**.

**Decision: do not promote the new adapter to replace the existing one.** Better road-access accuracy, schema validity and event classification did not resolve affected-function errors or offset the operational-status regression. Keeping the existing adapter is an experimental continuity decision, not an endorsement of operational deployment.

Both evaluation collections are small, synthetic and exposed during development. Neither constitutes an independent final test. The experiment also does not isolate the causal contribution of any single annotation change.

### My contribution and use of AI assistance

I directed the project’s objectives and iteration priorities, reviewed proposed revisions, coordinated the Colab workflow and artifact preservation, and required that model selection consider complete-record correctness and regressions across all fields.

I used an AI coding assistant extensively to help draft and revise code, develop synthetic examples and annotation guidance, inspect results, prepare documentation and publish authorized repository updates. These contributions are disclosed rather than presented as entirely unaided implementation. Assistant-supported review does not substitute for independent human annotation or external validation.

### Next step

Investigate the remaining affected-function errors and operational-status regressions, obtain independent annotation review, and define acceptance criteria before further training. Any later claim of generalization should use newly reserved evaluation families and appropriately governed real-world data.

[Full technical report and supporting evidence](../results/qlora-v2/training-v2-20261012T062041Z-d8f05304/results/training-v2-20261012T062041Z-d8f05304/REPORT.md).
