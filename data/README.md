# Public and synthetic data contract

No MPOR PDF, internal document, topology, incident, credential, personal record or operational feed belongs here.
The reference PIDP was read outside this repository solely to derive general architectural principles.

`synthetic/`: independently authored fictional English reports, six classes, three disjoint paraphrase families
per class. The fixed seed controls fictional facility IDs and row order. Event taxonomy labels are authored
independently of the classifier. Manifests record SHA-256, generator version, seed and split unit.
Changing fictional IDs does not create new independent examples: this small dataset has only 18 report
families and is a pipeline smoke test, not evidence of real-world generalization. No real port coordinates exist.

`public/corpus.json`: three original short summaries of public ANTAQ/PEFT/vLLM pages with URLs,
hashes, approval and license metadata. These are enough to run a tiny retrieval demonstration;
they are not a comprehensive maritime regulatory corpus. The summaries are original MIT-licensed text,
not copies of third-party publications. Dates and terms of original documents must be rechecked before use.

Public text import requires a Data Steward to verify provenance, currentness, redistribution rights,
absence of sensitive/personal content, and an explicit approval record. Metadata example defaults to
`approved=false`. Use `portshield-ai ingest --text approved.txt --metadata reviewed.json`.
Approval metadata is a process record, not a cryptographic proof. No crawling or PDF extraction is automatic.
Unauthorized content is never retrieved before ranking. Indexes/caches inherit source classifications.

Dataset and schemas: MIT. Upstream model weights: their own Apache-2.0 license, not re-licensed here.
Bronze: raw approved source + checksum; Silver: validated event contract; Gold: reports and evaluation
artifacts. The filesystem implementation is a small local analogue; it is not an Iceberg lakehouse.
