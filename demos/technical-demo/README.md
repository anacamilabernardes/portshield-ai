# Technical demonstration — recorded inference and error analysis

**A response can have a valid format and incorrect content.** This demonstration uses preserved model responses to show that distinction and how to investigate it.

## Scope and decision

- **Scope:** an experimental prototype using synthetic maritime reports. Production readiness has not been demonstrated.
- **Example selection:** `SYN-V2R-0006` is the only fully correct V2 response among the 12 development-validation examples. It is shown alongside `SYN-V2R-0001`, a known schema-valid failure, not as a representative success rate.
- **Aggregate result:** gains in some fields came with regressions in others. The selected examples do not replace the full comparison.
- **Decision:** do not replace the existing adapter with V2. Keeping the existing adapter does not establish its operational readiness.

## What the demonstration actually runs

This is a replay of completed Colab inference, with locally rerunnable verification. It does not call a model, load weights, or demonstrate a live production endpoint. Running `demo.py` verifies the evidence hashes, reruns the original Pydantic schema, and recomputes strict field comparisons for all 24 validation responses (12 paired cases). It then generates `DEMO.html`.

The input text and raw responses are preserved unchanged. Expected values are synthetic reference annotations available to this evaluation; they would require annotation in real use. Successful verification reproduces the saved results, including failures; it does not certify model quality.

## Results across all 12 validation examples

| Measure | Existing adapter | V2 adapter |
|---|---:|---:|
| Affected-function errors | 8 | 8 |
| Road-access errors | 5 | 3 |
| Operational-status errors | 5 | 7 |
| Completely correct records | 0 | 1 |
| Schema-invalid responses | 7 | 2 |

### The known failure: SYN-V2R-0001

An updated report withdraws the initial tug-fault explanation and confirms lightning as the reason docking is stopped. The V2 response passes the schema but has three incorrect fields:

| Field | Expected | V2 output |
|---|---|---|
| `affected_function` | `vessel_manoeuvring` | `none` |
| `operational_status` | `suspended` | `partial_restriction` |
| `equipment_failure` | `false` | `null` |

The existing adapter already got status and equipment right in this case. V2 corrected the event type but regressed on those two fields. All the V2 values are allowed by the contract; the schema cannot establish whether the narrative supports them.

## Follow the evidence

The record ID connects the input, raw response, expected values, validation results and field differences in the [existing-adapter responses](evidence/current-validation-predictions.jsonl) and [V2 responses](evidence/v2-validation-predictions.jsonl). The [schema snapshot](schema_snapshot.py), [training configuration](evidence/training-config.json), generation configurations and [SHA256 manifest](evidence-manifest.json) identify the conditions and exact local evidence. Hashes establish byte identity, not correctness of annotations or independence of evaluation cases.

The [full report and original experiment evidence](../../results/qlora-v2/training-v2-20261012T062041Z-d8f05304/results/training-v2-20261012T062041Z-d8f05304/REPORT.md) preserve the larger comparison, including a separate historical diagnostic collection. These exposed synthetic cases are development material, not an independent final test. The mismatches motivate investigation of temporal updates, field scope and explicit negation; they do not prove a causal explanation of model behavior.

## View or reproduce

Download the repository and open `demos/technical-demo/DEMO.html` in a browser for the English presentation. GitHub displays HTML source rather than running it. See [START-HERE.txt](START-HERE.txt) for the 4–5 minute presentation script.

To rerun verification, use Python 3.11 or 3.12 and run from this directory:

```bash
python -m venv .venv
# Windows:
.venv\Scripts\python -m pip install -r requirements.txt
.venv\Scripts\python demo.py
# Linux/macOS: use .venv/bin/python instead.
```

No GPU is required. The dependency is pinned to the Pydantic version recorded for the experiment. The HTML can be opened without installing Python.

AI assistance helped prepare the demonstration and verification code. No response was rewritten to make the demonstration appear more successful. Event F1 alone does not determine model adoption.
