import json
import tempfile
import unittest
from pathlib import Path
from portshield.core import (assess_event, forecast, graph_scenario, retrieve,
                            record_review, verify_audit)
from portshield.demo import DOCUMENTS, EVENTS, run


class WorkflowTests(unittest.TestCase):
    def test_access_filter_prevents_supervisor_evidence_leak(self):
        self.assertEqual(retrieve("crane failure", DOCUMENTS, {"demo_analyst"}), [])
        result = retrieve("crane failure", DOCUMENTS, {"demo_supervisor"})
        self.assertEqual([item["source_id"] for item in result], ["SYNTH-DOC-003"])
        self.assertEqual(retrieve("storm", DOCUMENTS, set()), [])

    def test_absent_evidence_requires_abstention(self):
        event = assess_event(EVENTS[2], DOCUMENTS, {"demo_analyst"})
        self.assertEqual(event["status"], "abstained")
        self.assertTrue(event["human_review_required"])

    def test_forecast_uses_trailing_observations(self):
        self.assertEqual(forecast([999, 10, 20, 30, 40])["predictions"], [25.0] * 4)
        for values in ([1], [1, 2, 3, float("nan")], [1, 2, 3, -1]):
            with self.assertRaises(ValueError):
                forecast(values)

    def test_graph_disruption_and_alternative(self):
        edges = [("a", "b"), ("b", "c"), ("a", "d")]
        self.assertTrue(graph_scenario(edges, "a", "c")["reachable"])
        self.assertFalse(graph_scenario(edges, "a", "c", ["b"])["reachable"])
        self.assertTrue(graph_scenario(edges, "a", "d", ["b"])["reachable"])
        self.assertFalse(graph_scenario(edges, "a", "d", ["a"])["reachable"])

    def test_review_binds_report_without_mutating_it(self):
        with tempfile.TemporaryDirectory() as directory:
            path = run(directory)
            original = path.read_bytes()
            review = record_review(path, "demo-analyst", "acknowledge", "Reviewed fictional exercise")
            self.assertFalse(review["payload"]["operational_action_authorized"])
            self.assertEqual(path.read_bytes(), original)
            self.assertTrue(verify_audit(Path(directory) / "audit.jsonl"))

    def test_audit_detects_modified_record(self):
        with tempfile.TemporaryDirectory() as directory:
            run(directory)
            path = Path(directory) / "audit.jsonl"
            record = json.loads(path.read_text())
            record["payload"]["data_class"] = "modified"
            path.write_text(json.dumps(record) + "\n")
            self.assertFalse(verify_audit(path))


if __name__ == "__main__":
    unittest.main()
