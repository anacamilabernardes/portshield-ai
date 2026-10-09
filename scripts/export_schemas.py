"""Generate versioned JSON schemas from the runtime contract."""
import json
from pathlib import Path
from portshield_ai.schema import EventAnalysis, EventRecord

out = Path("data/schemas")
out.mkdir(parents=True, exist_ok=True)
for name, model in (("event-analysis", EventAnalysis), ("event-record", EventRecord)):
    (out / f"{name}.schema.json").write_text(
        json.dumps(model.model_json_schema(), indent=2) + "\n", encoding="utf-8"
    )
