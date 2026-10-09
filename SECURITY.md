# Security policy

Supported research version: 0.1.x. Do not deploy this prototype directly on an operational network.
Report vulnerabilities through GitHub private vulnerability reporting once enabled by the repository owner.
If unavailable, contact the owner privately without posting exploit details, credentials or sensitive data
in public issues. The owner should acknowledge within 5 working days and agree remediation timing by severity.

Authentication defaults to fail-closed JWT verification (RS256, issuer, audience, expiry, subject and role).
Use an internal Keycloak realm with role `portshield-analyst`. Demo token mode is explicit and localhost only;
it is a shared identity for public/synthetic exercises. Roles are never read from client request fields.
JWKS configuration is operator-controlled; use internal HTTPS. No public JWKS endpoint is required.

Request text is untrusted. Structured extraction validates schema and abstains on invalid output.
RAG applies source access rules before ranking and rejects generated quotes not present in cited sources.
Neither safeguard proves factual truth or complete prompt-injection resistance. No tools can execute actions.
Request size/rate limits and TLS are required at the gateway; model generation and client timeouts are bounded.
The prototype does not implement a production audit store or comprehensive sensitive-data detector.

Do not log prompts, model replies, bearer tokens or user questions. Prometheus labels contain task/status
only. Disable vLLM request logs. Keep MLflow private and log only aggregate metrics and synthetic experiments.
Storage encryption, retention, per-user quotas, immutable audit export, image digests and signing,
dependency vulnerability review, egress restrictions and disaster recovery are production gate requirements.

If disclosure occurs: restrict access; revoke affected secrets; preserve sanitized audit evidence;
notify the designated security owner; remove exposed Git history with coordinated owner approval;
rebuild corpora, adapters and caches from verified sources; reevaluate before restoring service.
