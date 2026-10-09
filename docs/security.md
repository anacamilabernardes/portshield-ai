# Security, provenance and information sovereignty

## Prototype boundary

The prototype contains only generated fictional data. The access-filtering demonstration is not institutional IAM. Hash-linked records can detect changes relative to a known record but do not prevent rewriting the whole chain, deleting its tail, or concurrent-write corruption. A trusted external anchor and immutable storage are needed for stronger audit guarantees. Do not process sensitive information with this reference implementation.

## Requirements before a controlled institutional pilot

| Area | Required control |
| --- | --- |
| Identity | Institutional authentication, least privilege, role and source permissions, separation of duties |
| Data | Classification, provenance, license review, minimization, retention and deletion policy |
| Retrieval | Authorization before ranking, versioned citations, entitlement-aware caching, permission rechecks |
| Models | Approved licenses and provenance; no restricted knowledge in adapters; signed release records |
| Host | Segmented local infrastructure, encryption, secret management, backups and monitored access |
| Audit | Authenticated identity, model and data versions, evidence IDs, decision trace, immutable retention |
| Deployment | Approved change process, dependency review, reproducible evaluation and rollback |

## Threat scenarios to test

- A retrieved document tries to override the analyst request or extract another source. Treat retrieved text as untrusted data; enforce tools and access outside the model and test adversarial corpora.
- A user changes role claims or requests supervisor-only evidence. Resolve entitlements from trusted IAM, not request text.
- A model returns a confident answer without evidence. Require schema validation, citations, evidence sufficiency checks and tested abstention.
- A prompt or log exposes sensitive context. Apply minimization and classification controls throughout prompts, caches, telemetry, exports, and backups.
- A model, dependency, or dataset is replaced. Track approved hashes, ownership, provenance, evaluation evidence, and release history.

These are design requirements and future test cases; the current prototype does not claim to implement or pass institutional adversarial testing.

## Adding public data

Potential public source families include transport statistics, public meteorological observations, and published geospatial datasets. For each actual dataset, record publisher, exact source URL, license, retrieval date, version/hash, update cadence, permitted purpose, and known quality limitations. No external dataset is bundled, downloaded, or represented as licensed by this repository.
