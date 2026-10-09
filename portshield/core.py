"""Transparent baselines. No model, network service, or operational data required."""

import hashlib
import json
import math
import re
from datetime import datetime, timezone
from pathlib import Path


TAXONOMY = {
    "weather_disruption": ("storm", "weather", "wind"),
    "land_access_disruption": ("road", "rail", "land access"),
    "equipment_failure": ("crane", "equipment", "failure"),
    "navigation_restriction": ("navigation", "channel", "draft"),
}


def classify_event(text):
    tokens = set(re.findall(r"[a-z]+", text.lower()))
    matches = []
    for label, terms in TAXONOMY.items():
        if any(set(term.split()).issubset(tokens) for term in terms):
            matches.append(label)
    return {
        "event_classes": matches or ["unclassified"],
        "method": "keyword_baseline",
        "human_review_required": True,
    }


def retrieve(query, documents, roles, limit=3):
    """Filter before ranking. This baseline implements exact-token matching only."""
    query_terms = set(re.findall(r"[a-z]+", query.lower()))
    ranked = []
    for doc in documents:
        if not set(doc["allowed_roles"]).intersection(roles):
            continue
        terms = set(re.findall(r"[a-z]+", doc["text"].lower()))
        score = len(query_terms & terms)
        if score:
            ranked.append((score, doc["id"], doc))
    ranked.sort(key=lambda item: (-item[0], item[1]))
    return [
        {"source_id": doc["id"], "version": doc["version"],
         "excerpt": doc["text"], "data_class": doc["data_class"],
         "matching_tokens": score}
        for score, _, doc in ranked[:limit]
    ]


def assess_event(event, documents, roles):
    evidence = retrieve(event["description"], documents, roles)
    return {
        "event_id": event["id"], "facility_id": event["facility_id"],
        "data_class": event["data_class"],
        **classify_event(event["description"]),
        "evidence": evidence,
        "status": "evidence_available_for_review" if evidence else "abstained",
        "information_gaps": ["Verified restoration time", "Verified alternative capacity"],
        "limitations": "Keyword matches do not establish cause, severity, or operational impact.",
    }


def forecast(history, horizon=4, window=4):
    """Flat trailing-mean baseline. Spread is descriptive, not a confidence interval."""
    if horizon < 1 or window < 2 or len(history) < window:
        raise ValueError("Need a positive horizon and at least window >= 2 observations")
    if any(not math.isfinite(x) or x < 0 for x in history):
        raise ValueError("Observations must be finite and nonnegative")
    sample = history[-window:]
    mean = sum(sample) / window
    spread = math.sqrt(sum((x - mean) ** 2 for x in sample) / window)
    return {"method": "trailing_mean", "horizon_weeks": horizon,
            "predictions": [round(mean, 2)] * horizon,
            "historical_standard_deviation": round(spread, 2),
            "uncertainty": "Descriptive historical spread; no calibrated prediction interval.",
            "human_review_required": True}


def graph_scenario(edges, origin, destination, removed_nodes=()):
    """Reachability in an undirected fictional graph; does not estimate capacity."""
    removed = set(removed_nodes)
    adjacency = {}
    for a, b in edges:
        adjacency.setdefault(a, set())
        adjacency.setdefault(b, set())
        if a not in removed and b not in removed:
            adjacency[a].add(b)
            adjacency[b].add(a)
    if origin not in adjacency or destination not in adjacency:
        raise ValueError("Origin and destination must be nodes in the graph")
    frontier = [(origin, [origin])] if origin not in removed else []
    visited = set()
    path = None
    while frontier:
        node, route = frontier.pop(0)
        if node in visited:
            continue
        visited.add(node)
        if node == destination:
            path = route
            break
        frontier.extend((n, route + [n]) for n in sorted(adjacency[node]) if n not in visited)
    return {"origin": origin, "destination": destination,
            "removed_nodes": sorted(removed), "reachable": path is not None,
            "illustrative_path": path,
            "limitations": "Connectivity only. No travel time, cargo compatibility, or capacity validation.",
            "human_review_required": True}


def digest(record):
    return hashlib.sha256(json.dumps(record, sort_keys=True, separators=(",", ":")).encode()).hexdigest()


def verify_audit(path):
    previous = "0" * 64
    if not Path(path).exists():
        return True
    for line in Path(path).read_text(encoding="utf-8").splitlines():
        record = json.loads(line)
        stored = record.pop("hash")
        if record["previous_hash"] != previous or digest(record) != stored:
            return False
        previous = stored
    return True


def append_audit(path, action, payload):
    """Single-writer demo log. External immutable storage is required in production."""
    path = Path(path)
    path.parent.mkdir(parents=True, exist_ok=True)
    if not verify_audit(path):
        raise ValueError("Existing audit chain failed verification")
    lines = path.read_text(encoding="utf-8").splitlines() if path.exists() else []
    previous = json.loads(lines[-1])["hash"] if lines else "0" * 64
    record = {"timestamp": datetime.now(timezone.utc).isoformat(), "action": action,
              "payload": payload, "previous_hash": previous}
    record["hash"] = digest(record)
    with path.open("a", encoding="utf-8") as handle:
        handle.write(json.dumps(record, sort_keys=True) + "\n")
    return record


def record_review(report_path, reviewer, decision, reason):
    if decision not in {"acknowledge", "request_more_evidence"}:
        raise ValueError("Unsupported review decision")
    if not reviewer.strip() or not reason.strip():
        raise ValueError("Reviewer and reason are required")
    path = Path(report_path)
    report = json.loads(path.read_text(encoding="utf-8"))
    # Bind the review to the report content; do not mutate the assessed report.
    return append_audit(path.parent / "audit.jsonl", "human_review", {
        "report_hash": digest(report), "reviewer": reviewer, "decision": decision,
        "reason": reason, "identity_assurance": "unauthenticated_demo_input",
        "operational_action_authorized": False,
    })
