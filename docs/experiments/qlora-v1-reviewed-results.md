# QLoRA V1 — reviewed results and limitations

## Status and scope

Completed research experiment supplied by the user: Qwen/Qwen2.5-1.5B-Instruct with a QLoRA
adapter, three epochs, followed by adapter restoration and diagnostic inference. GPU shown
in the run: Tesla T4; PyTorch 2.6.0+cu124 and isolated Python 3.12.15. Base revision shown:
989aa7980e4cf806f80c7fef2b1adb7bc71aa306. These environment details come from run outputs;
the evidence package does not contain adapter weights or a full environment freeze.

## Original aggregate evaluation

| Metric | Base | Adapter |
|---|---:|---:|
| Records | 240 | 240 |
| JSON parse validity | 1.000 | 1.000 |
| Schema validity | 0.667 | 1.000 |
| Event-type macro-F1 | 0.667 | 1.000 |
| Exact match | 0.000 | 0.833 |
| Abstention precision / recall | 1.000 / 1.000 | 1.000 / 1.000 |
| Answerable coverage | 0.600 | 1.000 |
| Mean client latency, seconds | 2.251 | 3.878 |
| P95 client latency, seconds | 2.687 | 4.649 |

The adapter rerun produced 200 fully correct records and 40 affected_function mismatches.
All 40 correspond to the same unknown-2 text with different identifiers: an unverified rumour
about cargo operations. Expected affected_function=unknown; predicted cargo_handling.
All other fields matched, with no inference failures in the 240-row diagnostic rerun.

These are six distinct test scenario texts, not 240 independent situations. Moreover, the
input identifiers expose target class labels. V1 scores therefore cannot establish generalization.
The observed latency increase is about 72%; no repeated controlled benchmark establishes its
cause. TTFT, throughput, GPU memory and groundedness were not measured by these reports.

## Three-case exploratory comparison

| Case | Base | QLoRA |
|---|---|---|
| Wind interrupts cranes | navigation_restriction; insufficient; schema invalid | equipment_failure; failure=false; insufficient; schema invalid |
| Confirmed motor fault | Correct checked fields; unsupported road_access=normal | Correct checked fields; road_access=unknown |
| Cause unknown | navigation_restriction with insufficient; schema invalid | event_type=suspended (invalid enum), unsupported failure=true |

Each model passed the two checked fields plus schema validation in 1/3 cases. This is not
all-field accuracy: the base model's confirmed-fault response incorrectly asserted normal roads.
All six responses were parseable JSON, but only one response per model passed the schema.
The QLoRA fault response matches the reviewed full-field diagnostic target.

A prior restoration prompt about wind and cranes also yielded equipment_failure=true with
the adapter. Its wording differs from the weather case above, which yielded false. Do not
merge these as the same observation. Neither output supports reliable causal classification.

## Interpretation and decision

Adapter loading and inference worked. Aggregate improvements were not reproduced as an overall
advantage in the three-case diagnostic. The comparison is too small to establish overall
superiority or infer the mechanism of failure. Lexical shortcuts and label leakage require
dataset correction before further training or promotion.

Generation warnings did not prevent execution. Sampling parameters were ignored under greedy
decoding. The sliding-window/SDPA warning and near-zero training loss remain separate technical
investigations; neither is established as the cause of the observed classification errors.

Decision: retain V1 as a reproducible, limited research record; no operational deployment or
validated sovereignty/efficiency claim. A Colab experiment is cloud execution, not evidence
of on-premise sovereignty. Use public/synthetic data and human review throughout.

See ../data/annotation-policy-v2.md, ../data/dataset-v1-audit-and-v2-plan.md and
../evaluation-v2-protocol.md for the proposed next experiment.
