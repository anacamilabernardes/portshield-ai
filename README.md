# PortShield AI

**Sovereign Intelligence Platform for Port Infrastructure and Logistics Resilience**

PortShield AI is an independent reference prototype for analyst-led assessment of port and logistics continuity. It demonstrates a local workflow that combines structured events, access-filtered evidence retrieval, transparent forecasting, network dependency analysis, and recorded human review.

The proposed institutional architecture runs within the Ministry of Ports and Airports (MPOR) data center. This repository is a research and engineering prototype, with no claim of Ministry sponsorship, approval, production deployment, or access to institutional systems.

## Run the demonstration

Python 3.11 or newer is required. The demonstration uses the Python standard library and requires no API key, external service, GPU, or downloaded model.

```sh
python -m portshield demo --output artifacts
python -m unittest discover -s tests -v
```

Open `artifacts/report.json` to inspect the assessment. It includes synthetic event classifications, a four-week baseline forecast, graph connectivity scenarios, cited evidence, uncertainty notices, and mandatory human review. `artifacts/audit.jsonl` records a local hash-linked audit trail. Generated artifacts are excluded from Git.

To record a demonstration review:

```sh
python -m portshield review --report artifacts/report.json --reviewer demo-analyst --decision acknowledge --reason "Synthetic exercise reviewed; no operational action authorized."
```

The reviewer name is a demonstration input, not an authenticated identity. Real deployment must replace this input with institutionally authenticated identity and authorization.

## Implemented and planned capabilities

| Capability | Repository status |
| --- | --- |
| Synthetic data and structured event taxonomy | Implemented |
| Local evidence retrieval with source access filtering | Implemented: deterministic lexical baseline |
| Forecasting and graph scenarios | Implemented: transparent, uncalibrated baselines |
| Human review and hash-linked audit records | Implemented: local demonstration workflow |
| SLM inference and LoRA/QLoRA fine-tuning | Planned; no trained model or measured model scores provided |
| Private RAG with embeddings and a local model | Planned; the lexical baseline is not a generative RAG system |
| Institutional IAM, encrypted storage, monitoring and hardened serving | Planned; required before institutional use |

No operational instruction is executed. The system supports evidence review and scenario discussion; it does not operate ports, allocate resources, or issue alerts to external parties.

## Sovereign AI design

An approved small language model would extract and classify events, route tasks, explain quantitative outputs, cite retrieved evidence, and abstain when evidence is inadequate. Fine-tuning would teach task behavior and terminology. Current or restricted knowledge would remain in a permission-controlled private retrieval corpus rather than model weights.

Forecasts and network calculations belong to dedicated quantitative components. The language model must not invent numbers or substitute fluent text for measured results. Training, inference, embeddings, adapters, corpora, and operational logs are intended to remain on premises. No external LLM API is used by this demonstration.

See [architecture](docs/architecture.md), [security and data governance](docs/security.md), [evaluation](docs/evaluation.md), and [roadmap](docs/roadmap.md).

## Data and limitations

All included ports, corridors, documents, and events are fictional and marked `synthetic`. No real facility vulnerability, privileged document, personal data, credential, or operational feed is included. Future public datasets require provenance and license review before ingestion. The baseline results are illustrative, not estimates of actual infrastructure risk. The project has no measured fine-tuning or RAG benchmark results.

## Repository layout

```text
portshield/         Dependency-free demonstration and CLI
tests/              Behavioral checks for access filtering, abstention and analysis
docs/               Architecture, evaluation, security and phased delivery
.github/workflows/  Automated test checks
```

The repository currently has no open-source license grant. Publication is intended for a private repository; select and add a license before distributing it under open-source terms.
