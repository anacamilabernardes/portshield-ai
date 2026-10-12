# Risk register

Review before each release and monthly in a pilot. L/I use low/medium/high; priority is a judgement,
not a measured probability. Owners are roles to be assigned, not institutional persons.

| ID | Risk | L / I | Mitigation / trigger | Owner | Residual / status |
|---|---|---|---|---|---|
| R01 | Sensitive data published | M / critical | Only public/synthetic; publication inventory; block unapproved corpus | Data Owner | Manual content review still required / open |
| R02 | Hallucination used as action | H / high | Strict schema, citations, abstention, mandatory human review | Applied AI | Exact quote can be misleading / open |
| R03 | Synthetic performance overstates reality | H / high | Family split; error analysis; independent public/domain test set | Evaluator | Only 18 template families / open |
| R04 | Missed ambiguous event | M / high | Abstention metrics, negation and multi-event tests | Domain Owner | Lexical rules incomplete / open |
| R05 | Unauthorized retrieval | M / critical | IAM, pre-ranking ACL, cache ACL inheritance | Security | Future embeddings not reviewed / open |
| R06 | Model/adapter drift | M / high | Frozen suites, registry gates, rollback | Applied AI | No production drift history / open |
| R07 | GPU OOM / poor latency | M / medium | Context/concurrency caps, NF4, measured capacity | Platform | Hardware profile unmeasured / open |
| R08 | Obsolete/vulnerable dependencies | H / high | Pinned research versions, scan, rebuild/patch before promotion | Security | Reference pins are not security approval / open |
| R09 | Ambiguous source reuse rights | M / high | Original summaries; per-source terms reviewed before import | Steward | Upstream licenses not globally inferred / open |
| R10 | Institutional adoption inferred | M / medium | Explicit independent prototype disclaimer | Product Owner | Public readers may misinterpret / monitored |
| R11 | Toy compression mistaken for proprietary method | M / medium | No CompactifAI reproduction claim; measure toy error only | Engineering | No LLM speedup demonstrated / controlled |
| R12 | Metric gaming by abstaining on everything | M / high | Recall plus precision, answerable coverage, invalid denominator | Evaluator | Human utility still needed / open |

Release blockers: any nonpublic content, unauthorized retrieval, broken artifact provenance, unauthenticated
institutional exposure, or claimed performance without measurements. GPU experiment absence blocks a
performance claim; it does not prevent distributing a clearly labelled research pipeline.


## Risks identified in the V1 experiment

All entries below are open; accountable reviewers/owners have not yet been assigned.

| Risk | Evidence / impact | Required mitigation |
|---|---|---|
| Target-label leakage | Class names appear in model-visible exercise IDs; scores can be inflated | Remove label-bearing identifiers; independent V2 evaluation |
| Low semantic diversity | Six test texts repeated 40 times | Author and review diverse scenario groups; group-aware splits |
| Unsupported assertions | Equipment failure inferred without evidence; roads assumed normal | Evidence-based annotation, true/false/null coverage, full-field diagnostics |
| Invalid event enum and consistency | suspended used as event_type; insufficient paired with a specific type | Validate contract; human review; do not silently repair scored outputs |
| Unresolved training-loss behavior | Near-zero displayed training loss despite diagnostic failures | Inspect loss masks, normalization, finite values and gradient accumulation |
| Post-hoc test exposure | Inspected failures may influence subsequent tuning | Preserve V1 and create an independent final holdout |

References: [reviewed evidence](experiments/qlora-v1-reviewed-results.md),
[annotation policy](data/annotation-policy-v2.md), [V2 evaluation](evaluation-v2-protocol.md).
