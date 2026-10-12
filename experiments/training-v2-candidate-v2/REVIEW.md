# Full field and family review

Assistant review; new split and 12 new labels have not been reviewed by the user.

## SYN-V2-0001 — train / weather_claim_verification

A forwarded chat alleges that lightning stopped pallet loading at the east shed. The control room has not verified the message.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0002 — train / weather_claim_verification

The control room verified that lightning stopped pallet loading at the east shed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | The control room verified that lightning stopped pallet loading at the east shed. |
| affected_function | `"cargo_handling"` | The control room verified that lightning stopped pallet loading at the east shed. |
| operational_status | `"suspended"` | The control room verified that lightning stopped pallet loading at the east shed. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0003 — train / mechanical_claim_verification

An unsigned note claims a seized gearbox has slowed sack unloading at the bagging station. Neither the fault nor the slowdown has been checked. Independently, the gate officer confirmed unrestricted road access.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"normal"` | The independent gate report establishes normal road access. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0004 — train / mechanical_claim_verification

A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. Independently, the gate officer confirmed unrestricted road access.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| affected_function | `"cargo_handling"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| operational_status | `"partial_restriction"` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| road_access | `"normal"` | The independent gate report establishes normal road access. |
| equipment_failure | `true` | A maintenance inspection confirmed a seized gearbox and the shift lead verified slower sack unloading at the bagging station. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0005 — train / unresolved_cargo_claim

A caller alleges that parcel sorting has ceased at the dispatch shed. The call remains uncorroborated and the cause is unresolved.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0006 — train / unresolved_cargo_claim

The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The cause remains unresolved. |
| affected_function | `"cargo_handling"` | The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved. |
| operational_status | `"suspended"` | The dispatch supervisor directly verified that parcel sorting has ceased at the dispatch shed. The cause is unresolved. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0007 — train / unresolved_cargo_claim

A social post alleges that smoke from a nearby grass fire has slowed freight packing. The post has not been corroborated; its proposed cause remains unverified.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0008 — train / unresolved_cargo_claim

The packing supervisor confirmed slower freight packing. The proposed cause remains unverified.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The cause remains unresolved. |
| affected_function | `"cargo_handling"` | The packing supervisor confirmed slower freight packing. The proposed cause remains unverified. |
| operational_status | `"partial_restriction"` | The packing supervisor confirmed slower freight packing. The proposed cause remains unverified. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0009 — train / weather_claim_verification

An anonymous radio relay says hail has halted bulk-bag stacking at the inland warehouse. Operations staff cannot verify the claim. Independently, the gate officer confirmed unrestricted road access.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"normal"` | The independent gate report establishes normal road access. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0010 — train / weather_claim_verification

The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. Independently, the gate officer confirmed unrestricted road access.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| affected_function | `"cargo_handling"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| operational_status | `"suspended"` | The warehouse manager witnessed hail halt bulk-bag stacking at the inland warehouse. |
| road_access | `"normal"` | The independent gate report establishes normal road access. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0011 — train / mechanical_claim_verification

A handwritten complaint alleges a snapped drive chain has reduced carton loading at the rail shed. No inspection or operational check has corroborated it.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The alleged cause has not been verified. |
| affected_function | `"unknown"` | Cargo activity occurs only inside the unverified claim. |
| operational_status | `"unknown"` | No operational impact is verified. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"insufficient"` | Event type is unresolved; other independently verified fields remain usable. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0012 — train / mechanical_claim_verification

Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| affected_function | `"cargo_handling"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| operational_status | `"partial_restriction"` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | Technicians verified a snapped drive chain, and the rail-shed foreman confirmed reduced carton loading as a result. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0013 — train / confirmed_cargo_fault

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| affected_function | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| operational_status | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0014 — train / confirmed_cargo_fault

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| affected_function | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| operational_status | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0015 — train / confirmed_cargo_fault

A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| affected_function | `"cargo_handling"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| operational_status | `"partial_restriction"` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | A fractured hopper valve has been inspected and confirmed to limit grain loading to one line. The report identifies this cargo fault as the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0016 — train / weather_cargo_road_scope

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| affected_function | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| operational_status | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0017 — train / weather_cargo_road_scope

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| affected_function | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| operational_status | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0018 — train / weather_cargo_road_scope

A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| affected_function | `"cargo_handling"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| operational_status | `"partial_restriction"` | A verified dust storm has reduced outdoor steel-coil transfers to intermittent lifts. The report identifies the weather-related cargo disruption as the primary incident. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0019 — train / navigation_restriction_scope

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| affected_function | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| operational_status | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0020 — train / navigation_restriction_scope

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| affected_function | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| operational_status | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0021 — train / navigation_restriction_scope

A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| affected_function | `"navigation"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| operational_status | `"partial_restriction"` | A harbor order limits passage beside a newly marked wreck to one vessel at a time. The primary incident is this confirmed navigation restriction; passage continues. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0022 — train / navigation_restriction_scope

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| affected_function | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| operational_status | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0023 — train / navigation_restriction_scope

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| affected_function | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| operational_status | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0024 — train / navigation_restriction_scope

A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| affected_function | `"navigation"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| operational_status | `"partial_restriction"` | A verified exclusion area around survey divers narrows the shipping route, while vessels continue on the remaining route. This navigation restriction is the primary event. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0025 — train / confirmed_cargo_fault

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| affected_function | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| operational_status | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0026 — train / confirmed_cargo_fault

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| affected_function | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| operational_status | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0027 — train / confirmed_cargo_fault

Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| affected_function | `"cargo_handling"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| operational_status | `"partial_restriction"` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | Inspectors confirmed a split discharge hose that reduces liquid-cargo transfer capacity. This cargo-system fault is explicitly the primary incident. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0028 — train / navigation_restriction_scope

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. Separately, the access desk confirms all approach roads are open without restrictions.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| affected_function | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| operational_status | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| road_access | `"normal"` | Separately, the access desk confirms all approach roads are open without restrictions. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0029 — train / navigation_restriction_scope

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. Separately, the access desk confirms approach-road traffic is restricted by a checkpoint.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| affected_function | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| operational_status | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| road_access | `"restricted"` | Separately, the access desk confirms approach-road traffic is restricted by a checkpoint. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0030 — train / navigation_restriction_scope

The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| affected_function | `"navigation"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| operational_status | `"partial_restriction"` | The pilot station confirmed that a temporary salvage corridor limits shipping to scheduled windows. Navigation continues at reduced capacity, and this is the primary incident. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0031 — train / global_normal_operation

The duty log confirms every terminal service is operating normally. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The duty log confirms every terminal service is operating normally. |
| affected_function | `"none"` | The duty log confirms every terminal service is operating normally. |
| operational_status | `"normal"` | The duty log confirms every terminal service is operating normally. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0032 — train / global_normal_operation

The duty log confirms every terminal service is operating normally. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The duty log confirms every terminal service is operating normally. |
| affected_function | `"none"` | The duty log confirms every terminal service is operating normally. |
| operational_status | `"normal"` | The duty log confirms every terminal service is operating normally. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0033 — train / weather_manoeuvre_equipment_scope

Observed dense fog has stopped vessel turning in the maneuvering basin. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| affected_function | `"vessel_manoeuvring"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| operational_status | `"suspended"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0034 — train / weather_manoeuvre_equipment_scope

Observed dense fog has stopped vessel turning in the maneuvering basin. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| affected_function | `"vessel_manoeuvring"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| operational_status | `"suspended"` | Observed dense fog has stopped vessel turning in the maneuvering basin. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0035 — train / road_access_disruption

An official closure of the northern approach road has stopped truck access. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | An official closure of the northern approach road has stopped truck access. |
| affected_function | `"land_access"` | An official closure of the northern approach road has stopped truck access. |
| operational_status | `"suspended"` | An official closure of the northern approach road has stopped truck access. |
| road_access | `"restricted"` | An official closure of the northern approach road has stopped truck access. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0036 — train / road_access_disruption

An official closure of the northern approach road has stopped truck access. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | An official closure of the northern approach road has stopped truck access. |
| affected_function | `"land_access"` | An official closure of the northern approach road has stopped truck access. |
| operational_status | `"suspended"` | An official closure of the northern approach road has stopped truck access. |
| road_access | `"restricted"` | An official closure of the northern approach road has stopped truck access. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0037 — train / global_normal_operation

The supervisor verifies all terminal services continue at their usual capacity. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The supervisor verifies all terminal services continue at their usual capacity. |
| affected_function | `"none"` | The supervisor verifies all terminal services continue at their usual capacity. |
| operational_status | `"normal"` | The supervisor verifies all terminal services continue at their usual capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0038 — train / global_normal_operation

The supervisor verifies all terminal services continue at their usual capacity. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The supervisor verifies all terminal services continue at their usual capacity. |
| affected_function | `"none"` | The supervisor verifies all terminal services continue at their usual capacity. |
| operational_status | `"normal"` | The supervisor verifies all terminal services continue at their usual capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0039 — train / weather_manoeuvre_equipment_scope

Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| affected_function | `"vessel_manoeuvring"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| operational_status | `"partial_restriction"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0040 — train / weather_manoeuvre_equipment_scope

Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| affected_function | `"vessel_manoeuvring"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| operational_status | `"partial_restriction"` | Measured icing on exposed surfaces has reduced vessel berthing maneuvers to daylight operations. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0041 — train / global_normal_operation

The audited overnight summary confirms all terminal services are running at normal capacity. Equipment condition has not been assessed.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| affected_function | `"none"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| operational_status | `"normal"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | Equipment condition has not been assessed. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0042 — train / global_normal_operation

The audited overnight summary confirms all terminal services are running at normal capacity. A completed technical inspection explicitly ruled out equipment failures relevant to this report.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| affected_function | `"none"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| operational_status | `"normal"` | The audited overnight summary confirms all terminal services are running at normal capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `false` | A completed technical inspection explicitly ruled out equipment failures relevant to this report. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0043 — train / confirmed_cargo_fault

Technicians confirmed a failed winch controller at the timber quay. Timber unloading continues at reduced capacity.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Technicians confirmed a failed winch controller at the timber quay. |
| affected_function | `"cargo_handling"` | Timber unloading continues at reduced capacity. |
| operational_status | `"partial_restriction"` | Timber unloading continues at reduced capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | Technicians confirmed a failed winch controller at the timber quay. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0044 — train / confirmed_cargo_fault

Technicians confirmed a failed winch controller at the timber quay. Timber unloading is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Technicians confirmed a failed winch controller at the timber quay. |
| affected_function | `"cargo_handling"` | Timber unloading is fully suspended. |
| operational_status | `"suspended"` | Timber unloading is fully suspended. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | Technicians confirmed a failed winch controller at the timber quay. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0045 — train / navigation_restriction_scope

The authority confirmed a navigation restriction due to loose floating logs in the channel. Vessel passage continues under an escort restriction.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The authority confirmed a navigation restriction due to loose floating logs in the channel. |
| affected_function | `"navigation"` | Vessel passage continues under an escort restriction. |
| operational_status | `"partial_restriction"` | Vessel passage continues under an escort restriction. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0046 — train / navigation_restriction_scope

The authority confirmed a navigation restriction due to loose floating logs in the channel. Vessel passage is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The authority confirmed a navigation restriction due to loose floating logs in the channel. |
| affected_function | `"navigation"` | Vessel passage is fully suspended. |
| operational_status | `"suspended"` | Vessel passage is fully suspended. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0047 — train / road_access_disruption

The eastern approach-road bridge is under a confirmed emergency traffic restriction. Trucks can still reach the terminal at a reduced rate.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| affected_function | `"land_access"` | Trucks can still reach the terminal at a reduced rate. |
| operational_status | `"partial_restriction"` | Trucks can still reach the terminal at a reduced rate. |
| road_access | `"restricted"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0048 — train / road_access_disruption

The eastern approach-road bridge is under a confirmed emergency traffic restriction. Truck access to the terminal is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| affected_function | `"land_access"` | Truck access to the terminal is fully suspended. |
| operational_status | `"suspended"` | Truck access to the terminal is fully suspended. |
| road_access | `"restricted"` | The eastern approach-road bridge is under a confirmed emergency traffic restriction. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0049 — train / confirmed_cargo_fault

An inspected power-supply fault affects the cargo palletizer. Pallet handling continues using reduced capacity.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | An inspected power-supply fault affects the cargo palletizer. |
| affected_function | `"cargo_handling"` | Pallet handling continues using reduced capacity. |
| operational_status | `"partial_restriction"` | Pallet handling continues using reduced capacity. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | An inspected power-supply fault affects the cargo palletizer. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0050 — train / confirmed_cargo_fault

An inspected power-supply fault affects the cargo palletizer. Pallet handling is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | An inspected power-supply fault affects the cargo palletizer. |
| affected_function | `"cargo_handling"` | Pallet handling is fully suspended. |
| operational_status | `"suspended"` | Pallet handling is fully suspended. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `true` | An inspected power-supply fault affects the cargo palletizer. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0051 — train / navigation_restriction_scope

The port authority confirmed a navigation restriction around a damaged breakwater. Vessel transit continues in controlled batches.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The port authority confirmed a navigation restriction around a damaged breakwater. |
| affected_function | `"navigation"` | Vessel transit continues in controlled batches. |
| operational_status | `"partial_restriction"` | Vessel transit continues in controlled batches. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0052 — train / navigation_restriction_scope

The port authority confirmed a navigation restriction around a damaged breakwater. Vessel transit is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The port authority confirmed a navigation restriction around a damaged breakwater. |
| affected_function | `"navigation"` | Vessel transit is fully suspended. |
| operational_status | `"suspended"` | Vessel transit is fully suspended. |
| road_access | `"unknown"` | No road or gate-access evidence; unknown is retained. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0053 — train / road_access_disruption

A verified washout has restricted the service road used by inbound trucks. Inbound truck access continues at reduced capacity.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | A verified washout has restricted the service road used by inbound trucks. |
| affected_function | `"land_access"` | Inbound truck access continues at reduced capacity. |
| operational_status | `"partial_restriction"` | Inbound truck access continues at reduced capacity. |
| road_access | `"restricted"` | A verified washout has restricted the service road used by inbound trucks. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2-0054 — train / road_access_disruption

A verified washout has restricted the service road used by inbound trucks. Inbound truck access is fully suspended.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | A verified washout has restricted the service road used by inbound trucks. |
| affected_function | `"land_access"` | Inbound truck access is fully suspended. |
| operational_status | `"suspended"` | Inbound truck access is fully suspended. |
| road_access | `"restricted"` | A verified washout has restricted the service road used by inbound trucks. |
| equipment_failure | `null` | No verified equipment assessment; absence of a fault report does not exclude a fault. |
| information_sufficiency | `"sufficient"` | The primary event type is supported; this does not imply every field is known. |
| human_review_required | `true` | Required by the project policy, including normal operations. |

## SYN-V2R-0001 — validation / weather_current_bulletin

The 06:00 bulletin attributed a halt in vessel docking to a tug fault. At 07:00 the duty officer withdrew that attribution: inspection found the tug sound, and instrument readings confirmed a lightning exclusion remains the sole reason docking is stopped. Classify the situation at 07:00. Road access is not covered.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence. |
| affected_function | `"vessel_manoeuvring"` | Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence. |
| operational_status | `"suspended"` | Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence. |
| road_access | `"unknown"` | Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence. |
| equipment_failure | `false` | Use the corrected 07:00 bulletin: lightning causes the current docking stop; the earlier equipment attribution is explicitly withdrawn. Inspection excludes a tug fault. No road evidence. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0002 — validation / weather_current_bulletin

The 06:00 bulletin attributed a halt in vessel docking to a tug fault. At 07:00 the duty officer withdrew that attribution: inspection found the tug sound, and instrument readings confirmed a lightning exclusion remains the sole reason docking is stopped. Classify the situation at 07:00. A separate 07:00 access check reports the approach roads open without limits.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"weather_disruption"` | The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded. |
| affected_function | `"vessel_manoeuvring"` | The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded. |
| operational_status | `"suspended"` | The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded. |
| road_access | `"normal"` | The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded. |
| equipment_failure | `false` | The updated bulletin supports weather and suspended docking. The separate current access check supports normal roads; equipment failure is explicitly excluded. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0003 — validation / rail_only_land_disruption

The terminal receives freight by rail and road. A rail operator has confirmed a track occupation by a stalled external train, stopping all terminal rail arrivals; no terminal equipment defect has been assessed. This rail-access incident is the primary event. The dispatcher confirms road vehicles still enter without limits.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault. |
| affected_function | `"land_access"` | The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault. |
| operational_status | `"suspended"` | The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault. |
| road_access | `"normal"` | The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault. |
| equipment_failure | `null` | The primary incident suspends the affected rail-access service, not all transport modes. Road access independently remains normal. A stalled external train does not establish a terminal equipment fault. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0004 — validation / rail_only_land_disruption

The terminal receives freight by rail and road. A rail operator has confirmed a track occupation by a stalled external train, stopping all terminal rail arrivals; no terminal equipment defect has been assessed. This rail-access incident is the primary event. The dispatcher provides no current road-access information.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"land_access_disruption"` | The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred. |
| affected_function | `"land_access"` | The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred. |
| operational_status | `"suspended"` | The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred. |
| road_access | `"unknown"` | The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred. |
| equipment_failure | `null` | The confirmed rail blockage is land-access disruption. Status describes the stopped rail service. Neither the road state nor a terminal equipment fault can be inferred. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0005 — validation / tug_fault_primary_vs_cargo

The assessment concerns vessel manoeuvring, not the terminal cargo line. A tug engineer verified a steering-actuator failure, and the pilot confirms all assisted vessel turns are stopped. Cargo unloading continues normally. No road-access assessment is available.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed. |
| affected_function | `"vessel_manoeuvring"` | Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed. |
| operational_status | `"suspended"` | Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed. |
| road_access | `"unknown"` | Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed. |
| equipment_failure | `true` | Verified tug steering failure affects manoeuvring; normal cargo unloading does not move the impact into cargo_handling. Assisted turns are stopped. Roads are unassessed. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0006 — validation / tug_fault_primary_vs_cargo

The assessment concerns vessel manoeuvring, not the terminal cargo line. A tug engineer verified a steering-actuator failure, and the pilot confirms assisted vessel turns continue at reduced capacity using a spare tug. Cargo unloading continues normally. No road-access assessment is available.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"equipment_failure"` | The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate. |
| affected_function | `"vessel_manoeuvring"` | The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate. |
| operational_status | `"partial_restriction"` | The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate. |
| road_access | `"unknown"` | The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate. |
| equipment_failure | `true` | The same confirmed equipment incident affects manoeuvring, but the spare tug preserves reduced service. Normal cargo operations and unstated roads remain separate. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0007 — validation / navigation_lifted_order

An earlier notice stopped all ships at the river crossing. The current signed order lifts the total stop and permits only vessels below the published air-draft limit to pass under the fixed bridge. Passage has resumed for eligible vessels. The bridge has no reported malfunction, but no equipment inspection was performed. Road conditions are not supplied.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false. |
| affected_function | `"navigation"` | The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false. |
| operational_status | `"partial_restriction"` | The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false. |
| road_access | `"unknown"` | The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false. |
| equipment_failure | `null` | The current order supersedes the old stop. Air-draft limits restrict navigation while eligible vessels move. No reported malfunction without an inspection is unknown, not false. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0008 — validation / navigation_lifted_order

An earlier notice stopped all ships at the river crossing. The current signed order lifts the total stop and permits only vessels below the published air-draft limit to pass under the fixed bridge. Passage has resumed for eligible vessels. A technical inspection explicitly ruled out equipment failures relevant to this event. Road conditions are not supplied.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"navigation_restriction"` | Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown. |
| affected_function | `"navigation"` | Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown. |
| operational_status | `"partial_restriction"` | Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown. |
| road_access | `"unknown"` | Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown. |
| equipment_failure | `false` | Current passage is restricted, not stopped. Unlike the sibling example, an explicit inspection excludes relevant equipment failures. Roads remain unknown. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0009 — validation / normal_after_recovery

Yesterday a sorter breakdown halted cargo processing. The current shift report confirms the repair is complete, all terminal services have returned to normal, and a post-repair inspection found no remaining equipment failures. Classify current conditions, not the historical outage. Road access is not described.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | Current recovery supersedes yesterday's failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported. |
| affected_function | `"none"` | Current recovery supersedes yesterday's failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported. |
| operational_status | `"normal"` | Current recovery supersedes yesterday's failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported. |
| road_access | `"unknown"` | Current recovery supersedes yesterday's failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported. |
| equipment_failure | `false` | Current recovery supersedes yesterday's failure. All services are normal, so no function is currently affected. Post-repair inspection excludes an active fault. Roads remain unreported. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0010 — validation / normal_after_recovery

Yesterday a sorter breakdown halted cargo processing. The current shift report confirms all terminal services have returned to normal using a replacement processing line. The condition of the original sorter has not been checked. Classify current conditions, not the historical outage. Road access is not described.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"normal_operations"` | Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown. |
| affected_function | `"none"` | Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown. |
| operational_status | `"normal"` | Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown. |
| road_access | `"unknown"` | Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown. |
| equipment_failure | `null` | Restored service supports normal operations and no currently affected service, but replacement capacity does not establish the current condition of the old sorter. Equipment condition and roads remain unknown. |
| information_sufficiency | `"sufficient"` | Event type is supported; missing secondary fields do not negate this. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0011 — validation / conflicting_current_sources

Two equally current authorized reports disagree: the dispatch log says cargo weighing is stopped, while the weighing supervisor says it is running at full capacity. No reconciliation or cause assessment is available. A separate access inspector confirms normal roads.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available. |
| affected_function | `"unknown"` | Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available. |
| operational_status | `"unknown"` | Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available. |
| road_access | `"normal"` | Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available. |
| equipment_failure | `null` | Equally current unresolved contradictory impact reports establish neither a cargo impact nor its status/type. Independent road confirmation remains usable. No equipment assessment is available. |
| information_sufficiency | `"insufficient"` | Event type remains unresolved; other independent fields can still be used. |
| human_review_required | `true` | Human review is mandatory under project policy. |

## SYN-V2R-0012 — validation / conflicting_current_sources

Two equally current authorized reports disagree: the dispatch log says cargo weighing is stopped, while the weighing supervisor says it is running at full capacity. No reconciliation or cause assessment is available. A separate access inspector confirms restricted road access. Classify the disputed cargo report as the primary subject; the road check is a separate field observation.

| Field | Reviewed value | Rationale |
|---|---|---|
| event_type | `"unknown"` | The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case. |
| affected_function | `"unknown"` | The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case. |
| operational_status | `"unknown"` | The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case. |
| road_access | `"restricted"` | The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case. |
| equipment_failure | `null` | The disputed primary cargo event remains unresolved; the explicit scope prevents replacing it with the independently known road restriction. Only road_access changes from the sibling case. |
| information_sufficiency | `"insufficient"` | Event type remains unresolved; other independent fields can still be used. |
| human_review_required | `true` | Human review is mandatory under project policy. |

