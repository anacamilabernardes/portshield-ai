# 002-open-weight-offline: Small open-weight model with offline loading

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Use Qwen2.5-1.5B-Instruct as the reference, resolve immutable revision, review Apache-2.0 terms, disable remote code and load local snapshots only.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Model acquisition needs a connected reviewed staging area; larger baselines are optional and separately licensed. No GPU capability demonstrated yet.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
