# 001-finetuning-vs-rag: Fine-tuning behavior, retrieving knowledge

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Stable taxonomy/JSON/abstention behavior belongs in LoRA/QLoRA. Changing authorized evidence stays in a private reviewed corpus. Do not put institutional documents into public weights.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Two independently versioned artifacts; evaluate both retrieval and model behavior. RAG evidence does not guarantee truth.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
