"""Reproducible fictional reports. Template families never cross splits."""
import hashlib
import json
import random
from pathlib import Path
from .schema import EventAnalysis, EventRecord

# Independent paraphrase families; labels are authored, not produced by the baseline.
FAMILIES = {
 "weather_disruption": ["Strong winds temporarily restricted vessel manoeuvres.", "A storm caused partial restriction of vessel manoeuvring.", "Gale conditions partially restricted vessel manoeuvring."],
 "land_access_disruption": ["Road access is blocked; land access operations suspended.", "Road restricted with land access partially restricted.", "Rail closure: land access operations suspended; road access restricted."],
 "equipment_failure": ["Crane failed and cargo handling suspended.", "Equipment fault: cargo handling halted.", "Equipment failure partially restricted cargo handling."],
 "navigation_restriction": ["Channel restriction partially restricted navigation.", "Navigation restriction: navigation suspended.", "Restricted draft partially restricted navigation."],
 "normal_operations": ["Normal operations. Road access normal. No equipment failure.", "All operations normal. Road access remains normal. No crane failures.", "Operations remain normal. Road access is normal. No equipment failures."],
 "unknown": ["An unconfirmed report mentions a possible disruption.", "Contradictory reports: normal operations and crane failed.", "A rumour about cargo operations has no verified status."]}
FUNCTION = dict(weather_disruption="vessel_manoeuvring", land_access_disruption="land_access", equipment_failure="cargo_handling", navigation_restriction="navigation", normal_operations="none", unknown="unknown")

def generate(out, per_class=40, seed=42):
    if per_class < 1:
        raise ValueError("per_class must be positive")
    out = Path(out); out.mkdir(parents=True, exist_ok=True)
    rng = random.Random(seed)
    manifest = {"generator_version": "2", "seed": seed, "data_class": "synthetic", "license": "MIT", "split_unit": "template_family", "files": {}}
    for i, split in enumerate(("train", "validation", "test")):
        rows = []
        for label, templates in FAMILIES.items():
            for j in range(per_class):
                text = templates[i]
                suffix = " Road access remains normal. No equipment failures." if label in ("weather_disruption", "navigation_restriction") else ""
                unknown = label == "unknown"
                target = EventAnalysis(event_type=label, affected_function=FUNCTION[label],
                    operational_status="unknown" if unknown else ("normal" if label == "normal_operations" else ("suspended" if any(w in text.lower() for w in ("suspended", "halted", "blocked", "closure")) else "partial_restriction")),
                    road_access="unknown" if unknown or label == "equipment_failure" else ("restricted" if label == "land_access_disruption" else "normal"),
                    equipment_failure=None if unknown or label == "land_access_disruption" else label == "equipment_failure",
                    information_sufficiency="insufficient" if unknown else "sufficient")
                record_id = f"SYN-{split}-{label}-{j:04d}"
                # Opaque reference: the model input must never contain the split or label.
                ref = hashlib.sha256(f"{seed}:{record_id}".encode()).hexdigest()[:10]
                rows.append({"id": record_id, "template_family": f"{label}-{i}",
                    "facility_id": f"SYNTH-PORT-{rng.randrange(10000):04d}", "data_class": "synthetic",
                    "text": f"Fictional exercise {ref}: " + text + suffix,
                    "target": target.model_dump()})
        rng.shuffle(rows)
        for row in rows:
            EventRecord.model_validate(row)
        content = "".join(json.dumps(row, sort_keys=True) + "\n" for row in rows)
        # Write exact UTF-8/LF bytes: text mode translates LF to CRLF on Windows.
        dataset_path = out / f"{split}.jsonl"
        dataset_path.write_bytes(content.encode("utf-8"))
        manifest["files"][split] = {"rows": len(rows), "sha256": hashlib.sha256(dataset_path.read_bytes()).hexdigest()}
    (out / "manifest.json").write_bytes((json.dumps(manifest, indent=2) + "\n").encode("utf-8"))
    return manifest

def read_rows(path):
    return [json.loads(line) for line in Path(path).read_text(encoding="utf-8").splitlines() if line.strip()]
