"""Invalid predictions stay in the denominator. No automatic JSON repair."""
import json
import time
from pathlib import Path
from .schema import EventAnalysis
from .data import read_rows

LABELS = ["weather_disruption", "land_access_disruption", "equipment_failure", "navigation_restriction", "normal_operations", "unknown"]

def macro_f1(truth, pred):
    scores = []
    for label in LABELS:
        tp = sum(a == label and b == label for a, b in zip(truth, pred))
        fp = sum(a != label and b == label for a, b in zip(truth, pred))
        fn = sum(a == label and b != label for a, b in zip(truth, pred))
        scores.append(2*tp/(2*tp+fp+fn) if 2*tp+fp+fn else 0)
    return sum(scores)/len(scores)

def score(rows, raw):
    if not rows or len(rows) != len(raw):
        raise ValueError("Need a nonempty, aligned prediction set")
    parsed = []
    json_ok = 0
    for value in raw:
        try:
            obj = json.loads(value); json_ok += 1
            parsed.append(EventAnalysis.model_validate(obj))
        except (ValueError, TypeError):
            parsed.append(None)
    truth = [r["target"]["event_type"] for r in rows]
    pred = [p.event_type if p else "INVALID" for p in parsed]
    abstained = [p is not None and p.information_sufficiency == "insufficient" for p in parsed]
    needs = [r["target"]["information_sufficiency"] == "insufficient" for r in rows]
    tp = sum(a and b for a,b in zip(needs, abstained))
    metrics = {"n": len(rows), "json_parse_validity": json_ok/len(rows), "schema_validity": sum(p is not None for p in parsed)/len(rows),
        "macro_f1_event_type": macro_f1(truth, pred), "exact_match": sum(p is not None and p.model_dump() == r["target"] for p,r in zip(parsed,rows))/len(rows),
        "abstention_rate": sum(abstained)/len(rows), "abstention_precision": tp/sum(abstained) if any(abstained) else None,
        "abstention_recall": tp/sum(needs) if any(needs) else None,
        "answerable_coverage": sum(p is not None and not a and not n for p,a,n in zip(parsed,abstained,needs))/sum(not n for n in needs) if any(not n for n in needs) else None}
    metrics["field_accuracy"] = {field: sum(p is not None and getattr(p,field) == r["target"][field] for p,r in zip(parsed,rows))/len(rows) for field in EventAnalysis.model_fields}
    return metrics

def evaluate(dataset, predictor, output, tracking=False):
    rows = read_rows(dataset); raw = []; duration = []
    for row in rows:
        start = time.perf_counter()
        try:
            raw.append(predictor(row["text"]))
        except Exception as exc:
            # Error class only: do not persist prompts, tokens, credentials or response bodies.
            raw.append(json.dumps({"inference_error": type(exc).__name__}))
        duration.append(time.perf_counter()-start)
    report = score(rows, raw)
    report["client_latency_seconds"] = {"mean": sum(duration)/len(duration), "p95": sorted(duration)[min(len(duration)-1, int(.95*len(duration)))]}
    report["dataset"] = str(dataset)
    report["limitations"] = "Synthetic template-held-out evaluation only; latency includes client processing. No TTFT or GPU memory measurement here."
    Path(output).parent.mkdir(parents=True, exist_ok=True)
    Path(output).write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    if tracking:
        import mlflow
        with mlflow.start_run():
            mlflow.log_params({"dataset": str(dataset), "data_class": "synthetic"})
            mlflow.log_metrics({k:v for k,v in report.items() if isinstance(v,(float,int))})
            mlflow.log_artifact(output)
    return report
