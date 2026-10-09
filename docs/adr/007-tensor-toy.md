# 007-tensor-toy: SVD and Tensor Train / MPO toy only

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Tensorize a 16x16 synthetic matrix into four interleaved row/column sites and apply TT-SVD with bounded bond dimension.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Parameter ratio and Frobenius error are educational. Dense reconstruction is not a speedup, does not compress an LLM, and does not reproduce CompactifAI.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
