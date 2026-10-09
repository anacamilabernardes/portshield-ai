# Proposed delivery roadmap

The phases below are planning assumptions, not funded commitments or evidence of institutional approval.

| Phase | Outputs and admission gate |
| --- | --- |
| 0–3 months: design | Business scope, taxonomy, licensed public/synthetic corpus, hardware baseline, security design, analyst acceptance criteria |
| 3–6 months: prototype | Baseline comparison, local SLM experiments, behavior fine-tuning, private RAG, forecast and graph evaluations; only public/synthetic data |
| 6–12 months: controlled pilot | Formal authorization, institutional IAM and classification, selected approved data, analyst workflow, monitored deployment, rollback exercise |
| 12–24 months: expansion | Additional approved use cases, measured capacity planning, drift monitoring, source lifecycle management and governance review |

## Immediate engineering backlog

1. Add versioned schemas and curated multilingual synthetic extraction/abstention datasets.
2. Benchmark candidate local SLMs and confirm redistribution and adaptation licenses.
3. Implement a model adapter and local retrieval interface with permission-aware integration tests.
4. Establish temporal forecast benchmarks and capacity-aware graph validation.
5. Replace demo identity and local logging with institutionally approved services.
6. Gate releases on evaluation, threat tests, provenance, and analyst acceptance.

Hardware needs, costs, service targets, and rollout dates remain to be measured and approved.
