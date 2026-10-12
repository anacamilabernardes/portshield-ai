# Dataset V1 audit and V2 design

## Findings from the existing generator and prediction files

The default V1 generator produces 240 rows per split and 720 rows total. Each split contains
only six distinct scenario texts after removing exercise identifiers, repeated 40 times each.
There are 18 authored scenario templates across the three splits. Different IDs, facility IDs
and shuffle order do not create independent semantic examples.

Splits are separate by authored template family but retain strong lexical and label shortcuts:

- Weather always maps to vessel_manoeuvring; equipment faults always map to cargo_handling.
- Weather and navigation reports always append normal roads and no equipment failures.
- Unknown cases always have unknown affected function and unknown operational status.
- Normal cases always report normal roads and no equipment failure.
- Exercise identifiers embedded in the model input contain the target event-type label.
  This is direct label leakage and substantially compromises interpretation of V1 scores.
- Status labels are partly assigned by keyword matching rather than independent annotation.

These patterns make the dataset useful for pipeline checks, not an independent capability
benchmark. The original template-held-out split does not remove label leakage or semantic
correlations. Preserve V1 results but do not claim that its 1.000 event macro-F1 establishes
domain generalization. The exact contribution of each shortcut has not been measured.

## V2 requirements before training

- Remove class names and label-bearing metadata from model-visible report prefixes.
- Keep IDs and lineage outside the report text supplied to the model.
- Annotate all fields from evidence using annotation-policy-v2.md.
- Cross causes with affected functions: weather can stop cranes or restrict vessel movement;
  equipment faults must not be inferred from the mere mention of equipment.
- Cross cause certainty with impact certainty, and distinguish false from null explicitly.
- Include negation, rumours, conflicting claims, unaffected equipment, partial restrictions,
  mixed events, normal operations and missing road-access evidence.
- Use substantive differences in causal structure and evidence, not identifier substitution.
- Group related paraphrases, minimal pairs and scenario derivations in the same split.
- Check exact duplicates and normalized/semantic near-duplicates across splits.
- Record unique scenario counts and group counts separately from row counts.

Suggested initial design target: at least 30 independently authored scenario groups per event
class, with 20 groups for training, 5 for validation and 5 for test per class. This is a planning
target, not a completed dataset or evidence that coverage is adequate. Hold out some causal and
function combinations and assess coverage explicitly. Freeze the new test after independent
review; keep it out of prompt, hyperparameter and example selection.

## Diagnostic contamination boundary

The original six test templates, the wind/crane restoration example and the three newly
inspected cases are development diagnostics now. They may become regression checks, with
provenance, but cannot count as a new independent holdout. Further tuning must use training
and validation data, followed by a separately authored and reviewed final test.

## Training-loss investigation

Near-zero displayed training loss is unresolved. Duplication and label shortcuts are plausible
contributors, not a demonstrated sole cause. Before another run, inspect assistant-token masks,
supervised token counts, nonfinite losses, gradient scaling and loss reduction/normalization
with gradient accumulation. Compare a fixed batch's explicit assistant-token cross-entropy
with the Trainer-reported loss. Preserve dependency versions and logs; do not declare perfect
learning from rounded loss values. No further training was performed for this review.
