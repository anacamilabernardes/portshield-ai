# Data revision record

## training-v2-candidate-v1 — 2026-10-12

- Authored 54 new English narratives in 24 minimal-contrast groups.
- Assigned 16 complete groups to training (36 rows) and eight to development validation (18 rows).
- Covered all six event classes in both splits, without forcing artificial class balance through repeated rows.
- Added seven-field rationales and explicit group-level invariants.
- Preserved unknown equipment condition as null, independently evidenced roads, and confirmed impact with unresolved event cause.
- Kept suspended exclusively in operational_status; event identity stays fixed in state contrasts.
- Kept all historical data and labels unchanged. No historical rows, prior contrastive rows or examined reserve rows were added to either new split.
- No inference or training performed. Independent human review is not claimed.

This is a targeted small candidate dataset. The V2 designation describes the data revision, not a newly trained or validated model. Future annotation corrections must identify affected IDs, old/new values and rationale in a new version; validation data must not be recycled as an independent final test.

## Publication review record

The project owner reported completing review and authorized GitHub publication. No label corrections were supplied; narratives and targets are unchanged. Independent reviewer status has not been verified. Per-example assistant review entries preserve their original authorship-stage status; review-record.json records the subsequent owner review.
