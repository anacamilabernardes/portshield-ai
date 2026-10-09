# PIDP principles: public implementation mapping

The user-supplied PIDP proposal was read locally as a reference. Only generic principles are mapped;
the document itself, budgets, internal planning details and personal metadata are not redistributed.
This is alignment of design intent, not an assertion that PortShield has been adopted by MPOR.

| Supplied principle | Reference implementation | Institutional gate |
|---|---|---|
| One reusable platform | Shared contracts, services and data provenance | Approved platform integration |
| Open source by default / reduced lock-in | Python, PEFT, FastAPI, standard JSON, Docker | License/TCO/security review |
| Sovereignty of information and models | Local snapshots, offline inference, private MLflow and RAG | Egress controls, approved infrastructure |
| Bronze–Silver–Gold | Raw source hashes, validated event schema, reports | Shared lakehouse, owners and retention |
| Data Owners / Data Stewards | Explicit public-source approval metadata | Institutionally authenticated approval workflow |
| MLOps and traceability | Snapshot hash, seed, configs, aggregate experiments, model card | Registry promotion and full lineage |
| Docker/Kubernetes | Nonroot container and restricted example manifests | Signed images, quotas, TLS, restore drills |
| IAM and environment segregation | JWT validation, roles, pre-ranking ACLs | Internal Keycloak, least privilege, identity audit |
| Risk-proportional explainability | Structured fields, exact cited quotes, uncertainty | Domain reviewer validates usefulness |
| Human responsibility | Review flag always true; no tool execution | Authenticated auditable review before decisions |

Resiliência climática, hinterlândia, congestionamento, capacidade and risco are domain interfaces:
PortShield could explain validated outputs from such products. It does not claim to replace or implement
the full programme. Models and critical knowledge must remain under their designated owner's governance.
