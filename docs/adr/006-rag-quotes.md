# 006-rag-quotes: Lexical retrieval and exact-quote generative gate

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Start with offline lexical retrieval. Local vLLM can select exact cited quotes; reject unsupported IDs/text and abstain on no evidence.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Supports traceability without an external judge. Quote support is only a proxy; relevance/currentness require human review. Embeddings postponed until measured retrieval errors justify them.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
