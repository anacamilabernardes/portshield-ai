# Product requirements and accountable delivery

## Decision and user

An analyst reviewing a fictional disruption needs a consistent event record and traceable evidence to
decide whether further investigation is required. The product improves analysis consistency and time
to review; it does not decide ship manoeuvres, allocate assets or exercise administrative authority.

Input: English public/synthetic report. Output: strict event contract, explicit unknowns, review flag.
Evidence question: authorized public corpus. Output: cited exact quotes or abstention.
Non-goals: live ports, internal feeds, safety-critical control, legal advice, autonomous remediation.

## Acceptance and value

V1: generated disjoint splits; invalid output counted as failure; assistant-only training; identical
test corpus across model variants; measured client/server performance and hashes of artifacts.
V2: unauthorized content absent from retrieval; missing evidence abstains; citations resolve; relevance
and completeness judged by humans. V3/V4 gates live in the roadmap. Provisional evaluation targets
are research hypotheses, not contractual SLOs or achieved numbers.
Measure analyst time, correction rate and evidence usefulness in a consented synthetic exercise;
pair these with F1, abstention coverage, latency and memory. Fluent text is not the value metric.

## Responsibility matrix

| Activity | Accountable | Responsible / consulted |
|---|---|---|
| Scope, release and ADR | Engineering Lead | Applied AI, domain, platform |
| Source classification and reuse | Data Owner | Data Steward, security, legal |
| Model promotion | Applied AI Lead | evaluator, domain reviewer, security |
| Infrastructure and rollback | Platform Owner | SRE and security |
| Human review policy | Product / domain owner | IAM, audit and governance |

Suggested first increment: generator/contracts → CPU tests → SLM baseline → QLoRA → unchanged
held-out evaluation → quantization benchmark → review of cost/quality tradeoff. Stop expansion if
measured usefulness or provenance is insufficient. Delivery artifacts are reviewed before deployment.
