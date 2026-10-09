# 003-contract-abstention: Strict contract and mandatory human review

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

One strict Pydantic/JSON schema is used for authored targets, inference and API. Unknown evidence remains unknown; invalid generated output abstains at serving and fails evaluation.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

JSON-valid does not equal correct. Model metrics must retain invalid attempts. Every record requires review.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
