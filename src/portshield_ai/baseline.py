"""Conservative English lexical baseline, not a trained SLM."""
import re
from .schema import EventAnalysis

def abstain():
    return EventAnalysis(event_type="unknown", affected_function="unknown", operational_status="unknown",
        road_access="unknown", equipment_failure=None, information_sufficiency="insufficient")

def classify(text):
    t = text.lower()
    if any(x in t for x in ("ignore previous", "system prompt", "unconfirmed", "contradictory", "rumour", "rumor")):
        return abstain()
    road = "normal" if re.search(r"road access (?:remains |is )?normal", t) else "unknown"
    if re.search(r"road (?:access )?(?:is )?(?:blocked|restricted|closed)", t):
        road = "restricted"
    no_failure = bool(re.search(r"no (?:equipment |crane )?failures?", t))
    failure = bool(re.search(r"(?:crane|equipment) (?:has )?(?:failed|failure|fault)", t)) and not no_failure
    candidates = []
    if re.search(r"(?:strong winds|storm|high winds|weather disruption|gale)", t):
        candidates.append(("weather_disruption", "vessel_manoeuvring"))
    if road == "restricted" or "rail closure" in t:
        candidates.append(("land_access_disruption", "land_access"))
    if failure:
        candidates.append(("equipment_failure", "cargo_handling"))
    if re.search(r"(?:channel restriction|navigation restriction|restricted draft)", t):
        candidates.append(("navigation_restriction", "navigation"))
    if not candidates and re.search(r"(?:normal operations|all operations normal|operations remain normal)", t):
        candidates.append(("normal_operations", "none"))
    if len(candidates) != 1:
        return abstain()
    label, function = candidates[0]
    status = "normal" if label == "normal_operations" else (
        "suspended" if re.search(r"suspended|halted|closed|blocked|closure", t) else "partial_restriction")
    return EventAnalysis(event_type=label, affected_function=function, operational_status=status,
        road_access=road, equipment_failure=False if no_failure else (True if failure else None),
        information_sufficiency="sufficient")
