"""Small source-grounded regression suite; human relevance is deliberately unmeasured."""
import json
from pathlib import Path
from .rag import answer, groundedness, load_corpus

def evaluate_rag(cases_path, corpus_path, output, client=None):
    cases = json.loads(Path(cases_path).read_text(encoding="utf-8"))
    if not cases:
        raise ValueError("Need nonempty RAG cases")
    docs = load_corpus(corpus_path)
    records = []
    for case in cases:
        result = answer(case["question"], docs, case["roles"], client)
        records.append({"id": case["id"], "expected_abstain": case["expected_abstain"],
            "abstained": result["abstained"], "quote_support_proxy": groundedness(result, docs),
            "source_ids": [c["source_id"] for c in result["claims"]]})
    tp = sum(r["expected_abstain"] and r["abstained"] for r in records)
    predicted = sum(r["abstained"] for r in records)
    expected = sum(r["expected_abstain"] for r in records)
    supports = [r["quote_support_proxy"] for r in records if r["quote_support_proxy"] is not None]
    report = {"n": len(records), "method": "local_generative_quotes" if client else "extractive_retrieval_baseline",
        "abstention_precision": tp/predicted if predicted else None,
        "abstention_recall": tp/expected if expected else None,
        "answerable_coverage": sum(not r["expected_abstain"] and not r["abstained"] for r in records)/(len(records)-expected) if len(records)>expected else None,
        "quote_support_proxy": sum(supports)/len(supports) if supports else None,
        "human_relevance": None, "limitations": "Tiny regression suite; quote support is not entailment, relevance, completeness or factual truth.",
        "cases": records}
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report, indent=2)+"\n", encoding="utf-8")
    return report
