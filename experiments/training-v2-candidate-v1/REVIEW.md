# Training revision V2: annotation review

54 assistant-authored synthetic examples. Review status: project owner reported completing review; independent reviewer status unverified. See review-record.json. These are development data, not a final test.

## SYN-V2-0001 — train / r01

A forwarded chat alleges that lightning stopped pallet loading at the east shed. The control room has not verified the message.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0002 — train / r01

The control room verified that lightning stopped pallet loading at the east shed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | The control room verified that lightning stopped pallet loading at the east shed. |
| `affected_function` | `"cargo_handling"` | The control room verified that lightning stopped pallet loading at the east shed. |
| `operational_status` | `"suspended"` | The control room verified that lightning stopped pallet loading at the east shed. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0003 — train / r02

An unsigned note claims a seized gearbox has slowed sack unloading at the bagging station. Neither the fault nor the slowdown has been checked. Independently, the gate officer confirmed unrestricted road access.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"normal"` | The independent gate report establishes normal road access. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0004 — train / r02

A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. Independently, the gate officer confirmed unrestricted road access.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| `affected_function` | `"cargo_handling"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| `operational_status` | `"partial_restriction"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| `road_access` | `"normal"` | The independent gate report establishes normal road access. |
| `equipment_failure` | `true` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0005 — train / r03

A caller alleges that parcel sorting has ceased at the dispatch shed. The call remains uncorroborated and the cause is unresolved.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0006 — train / r03

The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The cause remains unresolved. |
| `affected_function` | `"cargo_handling"` | The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved. |
| `operational_status` | `"suspended"` | The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0007 — train / r04

A social post alleges that smoke from a nearby grass fire has slowed freight packing. The post has not been corroborated; its proposed cause remains unverified.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0008 — train / r04

The packing supervisor confirmed slower freight packing. The proposed cause remains unverified.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The cause remains unresolved. |
| `affected_function` | `"cargo_handling"` | The packing supervisor confirmed slower freight packing. The proposed cause remains unverified. |
| `operational_status` | `"partial_restriction"` | The packing supervisor confirmed slower freight packing. The proposed cause remains unverified. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0013 — train / a01

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `affected_function` | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `operational_status` | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0014 — train / a01

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `affected_function` | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `operational_status` | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0015 — train / a01

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `affected_function` | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `operational_status` | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0016 — train / a02

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `affected_function` | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `operational_status` | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0017 — train / a02

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `affected_function` | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `operational_status` | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0018 — train / a02

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `affected_function` | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `operational_status` | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0019 — train / a03

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `affected_function` | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `operational_status` | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0020 — train / a03

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `affected_function` | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `operational_status` | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0021 — train / a03

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `affected_function` | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `operational_status` | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0022 — train / a04

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `affected_function` | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `operational_status` | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0023 — train / a04

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `affected_function` | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `operational_status` | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0024 — train / a04

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `affected_function` | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `operational_status` | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0031 — train / e01

The duty log confirms every terminal service is operating normally. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The duty log confirms every terminal service is operating normally. |
| `affected_function` | `"none"` | The duty log confirms every terminal service is operating normally. |
| `operational_status` | `"normal"` | The duty log confirms every terminal service is operating normally. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0032 — train / e01

The duty log confirms every terminal service is operating normally. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The duty log confirms every terminal service is operating normally. |
| `affected_function` | `"none"` | The duty log confirms every terminal service is operating normally. |
| `operational_status` | `"normal"` | The duty log confirms every terminal service is operating normally. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0033 — train / e02

Observed dense fog has stopped vessel turning in the maneuvering basin. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `affected_function` | `"vessel_manoeuvring"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `operational_status` | `"suspended"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0034 — train / e02

Observed dense fog has stopped vessel turning in the maneuvering basin. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `affected_function` | `"vessel_manoeuvring"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `operational_status` | `"suspended"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0035 — train / e03

An official closure of the northern approach road has stopped truck access. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | An official closure of the northern approach road has stopped truck access. |
| `affected_function` | `"land_access"` | An official closure of the northern approach road has stopped truck access. |
| `operational_status` | `"suspended"` | An official closure of the northern approach road has stopped truck access. |
| `road_access` | `"restricted"` | An official closure of the northern approach road has stopped truck access. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0036 — train / e03

An official closure of the northern approach road has stopped truck access. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | An official closure of the northern approach road has stopped truck access. |
| `affected_function` | `"land_access"` | An official closure of the northern approach road has stopped truck access. |
| `operational_status` | `"suspended"` | An official closure of the northern approach road has stopped truck access. |
| `road_access` | `"restricted"` | An official closure of the northern approach road has stopped truck access. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0037 — train / e04

The supervisor verifies all terminal services continue at their usual capacity. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `affected_function` | `"none"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `operational_status` | `"normal"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0038 — train / e04

The supervisor verifies all terminal services continue at their usual capacity. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `affected_function` | `"none"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `operational_status` | `"normal"` | The supervisor verifies all terminal services continue at their usual capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0043 — train / s01

Technicians confirmed a failed winch controller at the timber quay. Timber unloading continues at reduced capacity.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Technicians confirmed a failed winch controller at the timber quay. |
| `affected_function` | `"cargo_handling"` | Timber unloading continues at reduced capacity. |
| `operational_status` | `"partial_restriction"` | Timber unloading continues at reduced capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | Technicians confirmed a failed winch controller at the timber quay. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0044 — train / s01

Technicians confirmed a failed winch controller at the timber quay. Timber unloading is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Technicians confirmed a failed winch controller at the timber quay. |
| `affected_function` | `"cargo_handling"` | Timber unloading is fully suspended. |
| `operational_status` | `"suspended"` | Timber unloading is fully suspended. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | Technicians confirmed a failed winch controller at the timber quay. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0045 — train / s02

The authority confirmed a navigation restriction due to loose floating logs in the channel. Vessel passage continues under an escort restriction.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The authority confirmed a navigation restriction due to loose floating logs in the channel. |
| `affected_function` | `"navigation"` | Vessel passage continues under an escort restriction. |
| `operational_status` | `"partial_restriction"` | Vessel passage continues under an escort restriction. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0046 — train / s02

The authority confirmed a navigation restriction due to loose floating logs in the channel. Vessel passage is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The authority confirmed a navigation restriction due to loose floating logs in the channel. |
| `affected_function` | `"navigation"` | Vessel passage is fully suspended. |
| `operational_status` | `"suspended"` | Vessel passage is fully suspended. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0047 — train / s03

The eastern approach-road bridge is under a confirmed emergency traffic restriction. Trucks can still reach the terminal at a reduced rate.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| `affected_function` | `"land_access"` | Trucks can still reach the terminal at a reduced rate. |
| `operational_status` | `"partial_restriction"` | Trucks can still reach the terminal at a reduced rate. |
| `road_access` | `"restricted"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0048 — train / s03

The eastern approach-road bridge is under a confirmed emergency traffic restriction. Truck access to the terminal is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| `affected_function` | `"land_access"` | Truck access to the terminal is fully suspended. |
| `operational_status` | `"suspended"` | Truck access to the terminal is fully suspended. |
| `road_access` | `"restricted"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0049 — train / s04

An inspected power-supply fault affects the cargo palletizer. Pallet handling continues using reduced capacity.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | An inspected power-supply fault affects the cargo palletizer. |
| `affected_function` | `"cargo_handling"` | Pallet handling continues using reduced capacity. |
| `operational_status` | `"partial_restriction"` | Pallet handling continues using reduced capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | An inspected power-supply fault affects the cargo palletizer. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0050 — train / s04

An inspected power-supply fault affects the cargo palletizer. Pallet handling is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | An inspected power-supply fault affects the cargo palletizer. |
| `affected_function` | `"cargo_handling"` | Pallet handling is fully suspended. |
| `operational_status` | `"suspended"` | Pallet handling is fully suspended. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | An inspected power-supply fault affects the cargo palletizer. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0009 — validation / r05

An anonymous radio relay says hail has halted bulk-bag stacking at the inland warehouse. Operations staff cannot verify the claim. Independently, the gate officer confirmed unrestricted road access.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"normal"` | The independent gate report establishes normal road access. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0010 — validation / r05

The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. Independently, the gate officer confirmed unrestricted road access.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| `affected_function` | `"cargo_handling"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| `operational_status` | `"suspended"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| `road_access` | `"normal"` | The independent gate report establishes normal road access. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0011 — validation / r06

A handwritten complaint alleges a snapped drive chain has reduced carton loading at the rail shed. No inspection or operational check has corroborated it.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"unknown"` | The alleged cause has not been verified. |
| `affected_function` | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| `operational_status` | `"unknown"` | No operational impact is verified. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0012 — validation / r06

Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| `affected_function` | `"cargo_handling"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| `operational_status` | `"partial_restriction"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0025 — validation / a05

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `affected_function` | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `operational_status` | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0026 — validation / a05

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `affected_function` | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `operational_status` | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0027 — validation / a05

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `affected_function` | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `operational_status` | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0028 — validation / a06

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `affected_function` | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `operational_status` | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `road_access` | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0029 — validation / a06

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `affected_function` | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `operational_status` | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `road_access` | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0030 — validation / a06

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `affected_function` | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `operational_status` | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0039 — validation / e05

Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `affected_function` | `"vessel_manoeuvring"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `operational_status` | `"partial_restriction"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0040 — validation / e05

Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"weather_disruption"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `affected_function` | `"vessel_manoeuvring"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `operational_status` | `"partial_restriction"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0041 — validation / e06

The audited overnight summary confirms all terminal services are running at normal capacity. Equipment condition has not been assessed.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `affected_function` | `"none"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `operational_status` | `"normal"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | Equipment condition has not been assessed. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0042 — validation / e06

The audited overnight summary confirms all terminal services are running at normal capacity. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"normal_operations"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `affected_function` | `"none"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `operational_status` | `"normal"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0051 — validation / s05

The port authority confirmed a navigation restriction around a damaged breakwater. Vessel transit continues in controlled batches.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The port authority confirmed a navigation restriction around a damaged breakwater. |
| `affected_function` | `"navigation"` | Vessel transit continues in controlled batches. |
| `operational_status` | `"partial_restriction"` | Vessel transit continues in controlled batches. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0052 — validation / s05

The port authority confirmed a navigation restriction around a damaged breakwater. Vessel transit is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"navigation_restriction"` | The port authority confirmed a navigation restriction around a damaged breakwater. |
| `affected_function` | `"navigation"` | Vessel transit is fully suspended. |
| `operational_status` | `"suspended"` | Vessel transit is fully suspended. |
| `road_access` | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0053 — validation / s06

A verified washout has restricted the service road used by inbound trucks. Inbound truck access continues at reduced capacity.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | A verified washout has restricted the service road used by inbound trucks. |
| `affected_function` | `"land_access"` | Inbound truck access continues at reduced capacity. |
| `operational_status` | `"partial_restriction"` | Inbound truck access continues at reduced capacity. |
| `road_access` | `"restricted"` | A verified washout has restricted the service road used by inbound trucks. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0054 — validation / s06

A verified washout has restricted the service road used by inbound trucks. Inbound truck access is fully suspended.

| Field | Target | Rationale |
|---|---|---|
| `event_type` | `"land_access_disruption"` | A verified washout has restricted the service road used by inbound trucks. |
| `affected_function` | `"land_access"` | Inbound truck access is fully suspended. |
| `operational_status` | `"suspended"` | Inbound truck access is fully suspended. |
| `road_access` | `"restricted"` | A verified washout has restricted the service road used by inbound trucks. |
| `equipment_failure` | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| `information_sufficiency` | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| `human_review_required` | `true` | Required by the project policy, including normal operations. |

