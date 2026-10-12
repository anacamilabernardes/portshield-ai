"""One contract for labels, LLM responses, API and evaluation."""
from typing import Literal
from pydantic import BaseModel, ConfigDict, Field, model_validator

class EventAnalysis(BaseModel):
    model_config = ConfigDict(extra="forbid", strict=True)
    event_type: Literal["weather_disruption", "land_access_disruption", "equipment_failure", "navigation_restriction", "normal_operations", "unknown"]
    affected_function: Literal["vessel_manoeuvring", "land_access", "cargo_handling", "navigation", "none", "unknown"]
    operational_status: Literal["partial_restriction", "suspended", "normal", "unknown"]
    road_access: Literal["normal", "restricted", "unknown"]
    equipment_failure: bool | None
    information_sufficiency: Literal["sufficient", "insufficient"]
    human_review_required: Literal[True] = True

    @model_validator(mode="after")
    def consistent(self):
        if self.information_sufficiency == "insufficient" and self.event_type != "unknown":
            raise ValueError("Insufficient evidence must abstain on event type")
        if self.event_type == "unknown" and self.information_sufficiency != "insufficient":
            raise ValueError("Unknown type requires insufficient evidence")
        return self

class ReportRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    text: str = Field(min_length=1, max_length=6000)

class QueryRequest(BaseModel):
    model_config = ConfigDict(extra="forbid")
    question: str = Field(min_length=1, max_length=2000)

class EventRecord(BaseModel):
    """Synthetic dataset record; operational identities are never accepted here."""
    model_config = ConfigDict(extra="forbid", strict=True)
    id: str = Field(pattern=r"^SYN-", max_length=160)
    template_family: str = Field(min_length=1, max_length=160)
    facility_id: str = Field(pattern=r"^SYNTH-PORT-\d{4}$")
    data_class: Literal["synthetic"]
    text: str = Field(min_length=1, max_length=6000)
    target: EventAnalysis
