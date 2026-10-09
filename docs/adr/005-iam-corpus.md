# 005-iam-corpus: Fail-closed IAM and pre-ranking source access

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Signed RS256 JWT with fixed issuer/audience and role mapping; operator-controlled internal JWKS. Explicit shared-token demo mode for localhost public/synthetic data only. Filter source roles before ranking.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Production requires internal TLS, immutable audit, gateway limits and cache ACL inheritance; demo identity cannot authorize institutional decisions.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
