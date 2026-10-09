# 004-quantization-serving: Separate training and serving environments

Status: accepted for research reference. Date: 2026-10-09.

## Context

Deliver reproducible public/synthetic AI engineering under sovereignty, traceability and review constraints.

## Decision

Train with NF4 QLoRA or FP16 LoRA, merge into fresh FP16 base, quantize with bitsandbytes, serve privately through vLLM.

## Alternatives

Hosted APIs, opaque end-to-end prompting and a single all-purpose deployment were considered. They do not provide the required local control or independently measurable boundaries for this experiment.

## Consequences

Separate torch/CUDA dependency stacks prevent version conflicts. Benchmark all variants with identical task corpus; weight compression does not measure total VRAM.

## Review trigger

Revisit after independent domain evaluation, measured resource bottlenecks or governance changes.
