# PortShield review closure and next experiment plan

Start with [annotation and error review](REVIEW.md), then [work plan and proposed approval criteria](WORK-PLAN.md).

The assistant-assisted review covers 78 records and 546 target fields. No historical labels were changed. All 48 recorded responses were rechecked, with 24 paired transitions and 84 incorrect-field instances preserved. Independent human adjudication remains pending. Numerical gates are proposals to freeze before a new experiment; no new training or promotion has occurred.

- annotation-review.jsonl: each source text, retained targets, rationale and per-field rules.
- annotation-change-log.json: review status and zero-change decision.
- field-errors.jsonl: wrong fields with observed versus expected values; descriptive categories are not causal diagnoses.
- paired-transitions.json: per-case corrections and regressions.
- metrics-recount.json and verification.json: independently recomputed results and checks.
- evidence/: unchanged source inputs, model responses, schema and original aggregate comparison.
- source-hashes.json: SHA256 values of evidence files.

To recheck evidence with Python 3.11/3.12, install pydantic==2.11.3 in a virtual environment and run `python verify.py` from this directory. Verification checks byte identity, schema and metric consistency; it does not establish semantic label correctness or human approval.

AI assistance was used for the review, analysis and documents. Published as an evidence review and proposed work plan. Publication does not constitute independent annotation sign-off or acceptance of the numerical gates.
