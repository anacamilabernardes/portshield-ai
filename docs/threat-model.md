# Threat model

Assets: authorized evidence, model snapshots, adapters, tokens, registry, audit metadata and analyst trust.
Boundaries: connected acquisition vs isolated training; gateway/IAM vs API; API vs private vLLM;
source approval vs corpus; evaluator vs registry. Adversaries include malicious documents/users,
compromised dependencies and accidental disclosure. No operational controls are exposed.

| Threat | Entry / failure | Existing measure | Residual / required measure |
|---|---|---|---|
| Identity spoofing | Forged bearer or client role | Signature/issuer/audience/expiry validation, fixed role mapping | Internal HTTPS, token rotation, identity audit |
| Privilege escalation | Retrieval before ACL | Filter by authorized roles before ranking | ACL inheritance in future indexes and caches |
| Prompt injection | Question/report/source instructions | Untrusted data envelopes, schema checks, quote gate, no tools | Adversarial evaluation; malicious exact quotes still need review |
| Data poisoning | Changed source / weights | Source hashes, approval, snapshot manifest | Signed approvals, review sampling, upstream validation |
| Hallucination | Plausible unsupported narrative | Exact citations or abstention; invalid JSON abstains | Quote match is not truth or relevance |
| Leakage | Prompts/weights/logs | Public/synthetic only, no request logging, offline model loading | Sensitive-data review, immutable audit with minimized metadata |
| Denial of service | Long prompts / GPU flood | Field bounds, output bound, timeouts | Gateway quotas, body/rate limits, concurrency budget |
| Supply chain compromise | Models, wheels, images | Remote code disabled, pinned reference versions | Lockfiles, hashes, SBOM, scan, signatures, patched images |
| Stale evidence | Old approved source | Version/hash/retrieved date | Steward refresh SLA and expiry enforcement before promotion |
| Tampered audit | Local writable log | Legacy hash chain detects record edits | Immutable external audit; hash chain alone cannot stop truncation |

Test fixtures target missing auth, forged/expired/wrong-audience tokens, source exclusion,
injection phrases, unsupported citation, malformed JSON and missing evidence. This is an explicit
research threat model, not a penetration test or assurance of institutional compliance.
