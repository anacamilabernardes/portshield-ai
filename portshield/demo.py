"""Entirely fictional fixtures generated for this demonstration."""

import json
from pathlib import Path
from .core import append_audit, assess_event, digest, forecast, graph_scenario


DOCUMENTS = [
    {"id": "SYNTH-DOC-001", "version": "1", "allowed_roles": ["demo_analyst"],
     "data_class": "synthetic", "text": "Storm and wind reports require analyst verification of weather duration and local restrictions."},
    {"id": "SYNTH-DOC-002", "version": "1", "allowed_roles": ["demo_analyst"],
     "data_class": "synthetic", "text": "Rail and road interruptions require verification of alternative corridor capacity and restoration time."},
    {"id": "SYNTH-DOC-003", "version": "1", "allowed_roles": ["demo_supervisor"],
     "data_class": "synthetic", "text": "Synthetic supervisor-only exercise: crane failure requires equipment inspection."},
]

EVENTS = [
    {"id": "SYNTH-EVENT-001", "facility_id": "PORT_SYNTH_A", "data_class": "synthetic",
     "description": "Storm and wind may reduce local navigation availability."},
    {"id": "SYNTH-EVENT-002", "facility_id": "PORT_SYNTH_B", "data_class": "synthetic",
     "description": "Rail access interruption reported in a fictional corridor."},
    {"id": "SYNTH-EVENT-003", "facility_id": "PORT_SYNTH_C", "data_class": "synthetic",
     "description": "Crane failure reported; supporting evidence is unavailable to this role."},
]


def run(output):
    output = Path(output)
    output.mkdir(parents=True, exist_ok=True)
    edges = [("INLAND_SYNTH", "RAIL_SYNTH"), ("RAIL_SYNTH", "PORT_SYNTH_A"),
             ("INLAND_SYNTH", "ROAD_SYNTH"), ("ROAD_SYNTH", "PORT_SYNTH_B")]
    report = {
        "project": "PortShield AI", "version": "0.1.0", "data_class": "synthetic",
        "deployment": "local_reference_prototype", "human_review_required": True,
        "events": [assess_event(event, DOCUMENTS, {"demo_analyst"}) for event in EVENTS],
        "forecast": forecast([90, 95, 92, 100, 105, 102, 98, 110]),
        "forecast_unit": "fictional throughput units per week",
        "network_scenarios": [
            graph_scenario(edges, "INLAND_SYNTH", "PORT_SYNTH_A"),
            graph_scenario(edges, "INLAND_SYNTH", "PORT_SYNTH_A", ["RAIL_SYNTH"]),
            graph_scenario(edges, "INLAND_SYNTH", "PORT_SYNTH_B", ["RAIL_SYNTH"]),
        ],
        "notice": "Fictional exercise. No operational action or real infrastructure risk inference.",
    }
    path = output / "report.json"
    append_audit(output / "audit.jsonl", "assessment_generated", {
        "report_hash": digest(report), "data_class": "synthetic", "software_version": "0.1.0"})
    path.write_text(json.dumps(report, indent=2) + "\n", encoding="utf-8")
    return path
