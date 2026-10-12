# Contrastive examples for annotation review

Status: assistant-authored synthetic development candidates; independent annotation review pending. Created 2026-10-12. Language: English.

15 unique examples: three rumor/confirmation pairs and three road-condition triples. No examples were added to the existing splits, used for training, or treated as an independent test.

## Contract and intended use

- Only the `text` field is model input. IDs and group names are metadata, never prompt prefixes.
- A verified cargo impact can coexist with `event_type=unknown` when its cause/type remains unresolved. Under the existing contract, `information_sufficiency=insufficient` concerns event type, not the completeness of every field.
- An independent verified road statement remains usable even when a cargo allegation is unverified.
- Road triples explicitly identify a primary cargo incident to avoid ambiguity in the current single-event schema. Without a stated primary event, multiple confirmed event types would require separate adjudication.
- False equipment failure labels have explicit inspection evidence. Unverified or unstated condition is null.
- Preserve each contrast group in a single future split to avoid near-duplicate train/test contamination. These disclosed cases are development material, not a blind holdout.
- These deliberately small contrasts do not solve the diversity gap. Independently reviewed paraphrases and new scenarios remain necessary before further training.

## Examples and targets

### SYN-CONTRAST-0001 (contrast-01)

An unverified message claims that cargo handling has stopped. The cause has not been established.

```json
{
  "event_type": "unknown",
  "affected_function": "unknown",
  "operational_status": "unknown",
  "road_access": "unknown",
  "equipment_failure": null,
  "information_sufficiency": "insufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0002 (contrast-01)

The operations supervisor verified that cargo handling has stopped. The cause has not been established.

```json
{
  "event_type": "unknown",
  "affected_function": "cargo_handling",
  "operational_status": "suspended",
  "road_access": "unknown",
  "equipment_failure": null,
  "information_sufficiency": "insufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0003 (contrast-02)

An unverified message claims that strong winds have reduced cargo handling capacity. No operational impact has been verified.

```json
{
  "event_type": "unknown",
  "affected_function": "unknown",
  "operational_status": "unknown",
  "road_access": "unknown",
  "equipment_failure": null,
  "information_sufficiency": "insufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0004 (contrast-02)

The operations supervisor verified that strong winds have reduced cargo handling capacity. Cargo handling continues at reduced capacity.

```json
{
  "event_type": "weather_disruption",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "unknown",
  "equipment_failure": null,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0005 (contrast-03)

An unverified message claims that a conveyor fault has stopped cargo handling. Separately, the access supervisor verified that road access remains normal.

```json
{
  "event_type": "unknown",
  "affected_function": "unknown",
  "operational_status": "unknown",
  "road_access": "normal",
  "equipment_failure": null,
  "information_sufficiency": "insufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0006 (contrast-03)

The maintenance supervisor verified that a conveyor fault has stopped cargo handling. Separately, the access supervisor verified that road access remains normal.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "suspended",
  "road_access": "normal",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0007 (contrast-04)

A confirmed conveyor fault partially restricted cargo handling. This cargo incident is explicitly identified as the primary event. Road access is confirmed normal.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "normal",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0008 (contrast-04)

A confirmed conveyor fault partially restricted cargo handling. This cargo incident is explicitly identified as the primary event. Road access is confirmed restricted.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "restricted",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0009 (contrast-04)

A confirmed conveyor fault partially restricted cargo handling. This cargo incident is explicitly identified as the primary event.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "unknown",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0010 (contrast-05)

Strong winds partially restricted cargo handling. This weather-related cargo incident is explicitly identified as the primary event. An inspection confirmed that no equipment had failed. Road access is confirmed normal.

```json
{
  "event_type": "weather_disruption",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "normal",
  "equipment_failure": false,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0011 (contrast-05)

Strong winds partially restricted cargo handling. This weather-related cargo incident is explicitly identified as the primary event. An inspection confirmed that no equipment had failed. Road access is confirmed restricted.

```json
{
  "event_type": "weather_disruption",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "restricted",
  "equipment_failure": false,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0012 (contrast-05)

Strong winds partially restricted cargo handling. This weather-related cargo incident is explicitly identified as the primary event. An inspection confirmed that no equipment had failed.

```json
{
  "event_type": "weather_disruption",
  "affected_function": "cargo_handling",
  "operational_status": "partial_restriction",
  "road_access": "unknown",
  "equipment_failure": false,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0013 (contrast-06)

A confirmed crane motor fault suspended cargo handling completely. This cargo incident is explicitly identified as the primary event. Road access is confirmed normal.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "suspended",
  "road_access": "normal",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0014 (contrast-06)

A confirmed crane motor fault suspended cargo handling completely. This cargo incident is explicitly identified as the primary event. Road access is confirmed restricted.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "suspended",
  "road_access": "restricted",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

### SYN-CONTRAST-0015 (contrast-06)

A confirmed crane motor fault suspended cargo handling completely. This cargo incident is explicitly identified as the primary event.

```json
{
  "event_type": "equipment_failure",
  "affected_function": "cargo_handling",
  "operational_status": "suspended",
  "road_access": "unknown",
  "equipment_failure": true,
  "information_sufficiency": "sufficient",
  "human_review_required": true
}
```

## Files and validation

- [Model-compatible examples](examples.jsonl)
- [Per-field annotation rationale](annotations.jsonl)
- [Contrast groups and invariant fields](contrast-groups.json)
- [Integrity manifest](manifest.json)

Review every target independently before training. Evaluate all-field exact match and per-field accuracy; separately count unverified impact assertions and road restrictions inferred without evidence. Schema validity and event F1 alone do not establish success.
