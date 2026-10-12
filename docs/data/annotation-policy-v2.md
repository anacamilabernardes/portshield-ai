# Annotation policy V2 — synthetic maritime event analysis

Status: proposed policy, prepared for review before further training. Language: English.
This document does not modify the existing generator, schema, evaluator or trained adapter.
Only public or independently authored synthetic material is permitted. No internal MPOR
documents, operational identities, personal information or confidential events are included.

## Core rule

Label explicit evidence, not associations between words. Mentioning a crane does not establish
equipment failure. Weather can interrupt cargo handling, navigation, land access or vessel
manoeuvring. Unknown cause does not erase a directly confirmed operational impact.
Record short supporting evidence spans and an annotation rationale in a separate annotation
sidecar; these are not additional fields in the current EventAnalysis response.

## Field contract

| Field | Rule |
|---|---|
| event_type | Use weather_disruption for an explicitly weather-caused interruption; equipment_failure for a confirmed fault causing the event; land_access_disruption for disrupted land access; navigation_restriction for explicitly restricted navigation. Use normal_operations only with affirmative normality evidence. Use unknown when type cannot be resolved. |
| affected_function | Use vessel_manoeuvring, land_access, cargo_handling or navigation only when impact is confirmed. Use none for explicitly unaffected/normal operations and unknown when the affected function is not established. A rumour mentioning cargo does not confirm affected cargo handling. |
| operational_status | suspended means stopped; partial_restriction means reduced/restricted but not stopped; normal requires explicit normality; unknown means unestablished/conflicting status. suspended is never an event_type. |
| road_access | normal or restricted requires explicit road evidence. Weather being normal does not establish road access. Rail disruption alone does not establish road restriction. Otherwise use unknown. |
| equipment_failure | true: confirmed equipment fault; false: explicitly ruled out failure or explicitly verified relevant equipment functioning normally; null: unmentioned, unverified or conflicting evidence. An alternative cause does not by itself justify false. |
| information_sufficiency | In the current contract this indicates whether event_type is resolvable, not whether every field is known. Use sufficient with a supported non-unknown type; insufficient with unknown. Other fields may remain known independently. |
| human_review_required | Always true. This is a research decision-support output. |

For one report describing multiple independently confirmed event types without a stated primary
event, use event_type=unknown and information_sufficiency=insufficient under the current
single-event contract. Retain other directly supported, nonconflicting fields. Route to human
review; do not silently invent a priority order. A future multi-event schema is a separate change.

## Required distinctions

| Evidence | Event type | Equipment failure | Status |
|---|---|---|---|
| Wind suspended cranes; equipment condition unreported | weather_disruption | null | suspended |
| Crane motor failure confirmed; cargo handling stopped | equipment_failure | true | suspended |
| Crane operations stopped; cause and equipment condition unverified | unknown | null | suspended |
| Wind suspended cranes; inspection explicitly found no equipment fault | weather_disruption | false | suspended |

All four can have affected_function=cargo_handling when actual crane/cargo operations are
confirmed affected. The unverified-rumour example in V1 instead has affected_function=unknown.

## Annotation and review procedure

1. Author a fictional scenario independently of class-to-function lookup tables.
2. Identify evidence for each of the seven fields and explicitly mark missing evidence.
3. Assign all seven labels; validate syntax, enum membership and cross-field consistency.
4. Obtain independent label review and adjudicate disagreements before freezing a test set.
5. Keep scenario lineage, evidence spans, reviewer status and policy version in a sidecar.
6. Freeze labels before model comparison. Record policy amendments; do not relabel a test
   merely to agree with a model response.

Proposed semantic checks include rejecting equipment_failure events without confirmed failure
and checking the event_type/information_sufficiency relationship. Some evidence-based checks
require human review; schema validity alone cannot establish factual support.
