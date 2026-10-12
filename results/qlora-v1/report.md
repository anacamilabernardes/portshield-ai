# PortShield AI — Post-Training Error Analysis

## Scope

Model: Qwen/Qwen2.5-1.5B-Instruct with a QLoRA adapter.
Data: fictional synthetic maritime reports only.
This document separates the original evaluation metrics from a new inference run used to collect individual predictions.

## Original Evaluation Results

| Metric | Before training | After training |
|---|---:|---:|
| JSON parse validity | 1.0 | 1.0 |
| Schema validity | 0.6666666666666666 | 1.0 |
| Macro-F1: event type | 0.6666666666666666 | 1.0 |
| Exact match | 0.0 | 0.8333333333333334 |
| Abstention precision | 1.0 | 1.0 |
| Abstention recall | 1.0 | 1.0 |
| Mean latency (seconds) | 2.251 | 3.878 |
| P95 latency (seconds) | 2.687 | 4.649 |

## Diagnostic Rerun

- Examples processed: 240
- Schema-valid responses: 240
- Fully correct responses: 200
- Incorrect or failed responses: 40

Rerun results may differ from the original evaluation. The original reports remain unchanged.

## Field Errors in Schema-Valid Responses

- `affected_function`: 40

## Affected Function Confusions

| Expected | Predicted | Count |
|---|---|---:|
| unknown | cargo_handling | 40 |

## Individual Errors

### Example SYN-test-unknown-0028

Template family: unknown-2

```text
Fictional exercise test-unknown-0028: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0019

Template family: unknown-2

```text
Fictional exercise test-unknown-0019: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0013

Template family: unknown-2

```text
Fictional exercise test-unknown-0013: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0023

Template family: unknown-2

```text
Fictional exercise test-unknown-0023: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0021

Template family: unknown-2

```text
Fictional exercise test-unknown-0021: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0027

Template family: unknown-2

```text
Fictional exercise test-unknown-0027: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0032

Template family: unknown-2

```text
Fictional exercise test-unknown-0032: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0035

Template family: unknown-2

```text
Fictional exercise test-unknown-0035: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0020

Template family: unknown-2

```text
Fictional exercise test-unknown-0020: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0000

Template family: unknown-2

```text
Fictional exercise test-unknown-0000: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0034

Template family: unknown-2

```text
Fictional exercise test-unknown-0034: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0024

Template family: unknown-2

```text
Fictional exercise test-unknown-0024: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0030

Template family: unknown-2

```text
Fictional exercise test-unknown-0030: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0014

Template family: unknown-2

```text
Fictional exercise test-unknown-0014: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0009

Template family: unknown-2

```text
Fictional exercise test-unknown-0009: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0038

Template family: unknown-2

```text
Fictional exercise test-unknown-0038: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0036

Template family: unknown-2

```text
Fictional exercise test-unknown-0036: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0037

Template family: unknown-2

```text
Fictional exercise test-unknown-0037: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0018

Template family: unknown-2

```text
Fictional exercise test-unknown-0018: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0031

Template family: unknown-2

```text
Fictional exercise test-unknown-0031: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0010

Template family: unknown-2

```text
Fictional exercise test-unknown-0010: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0004

Template family: unknown-2

```text
Fictional exercise test-unknown-0004: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0015

Template family: unknown-2

```text
Fictional exercise test-unknown-0015: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0007

Template family: unknown-2

```text
Fictional exercise test-unknown-0007: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0025

Template family: unknown-2

```text
Fictional exercise test-unknown-0025: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0001

Template family: unknown-2

```text
Fictional exercise test-unknown-0001: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0008

Template family: unknown-2

```text
Fictional exercise test-unknown-0008: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0003

Template family: unknown-2

```text
Fictional exercise test-unknown-0003: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0029

Template family: unknown-2

```text
Fictional exercise test-unknown-0029: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0017

Template family: unknown-2

```text
Fictional exercise test-unknown-0017: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0016

Template family: unknown-2

```text
Fictional exercise test-unknown-0016: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0002

Template family: unknown-2

```text
Fictional exercise test-unknown-0002: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0026

Template family: unknown-2

```text
Fictional exercise test-unknown-0026: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0005

Template family: unknown-2

```text
Fictional exercise test-unknown-0005: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0022

Template family: unknown-2

```text
Fictional exercise test-unknown-0022: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0006

Template family: unknown-2

```text
Fictional exercise test-unknown-0006: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0011

Template family: unknown-2

```text
Fictional exercise test-unknown-0011: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0039

Template family: unknown-2

```text
Fictional exercise test-unknown-0039: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0012

Template family: unknown-2

```text
Fictional exercise test-unknown-0012: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

### Example SYN-test-unknown-0033

Template family: unknown-2

```text
Fictional exercise test-unknown-0033: A rumour about cargo operations has no verified status.
```

Expected versus predicted differences:

```json
{
  "affected_function": {
    "expected": "unknown",
    "predicted": "cargo_handling"
  }
}
```

## Limitations and Next Steps

- Synthetic template-based results do not establish operational readiness.
- Repeated template variants are not independent real-world scenarios.
- This is post-hoc test-set analysis. If findings inform model or prompt changes, use a new independent test set for final evaluation.
- Review label definitions and annotation consistency before attributing every mismatch to model failure.
- Training-loss values near zero require a separate diagnostic review.
- These reports do not measure TTFT, throughput, GPU memory, or groundedness.
- Human review remains required.
