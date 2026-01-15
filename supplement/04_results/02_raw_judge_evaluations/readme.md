# Raw Judge Evaluations

This directory contains **frozen, unmodified** raw judge outputs.

## Structure
- `diagnostic/`: exploratory judge runs used **only for diagnostic purposes** (not used for final claims).
- `final/`: judge runs used for all reported results.

## Guarantees
- All judge outputs are preserved verbatim as JSON artifacts.
- No post-hoc editing, filtering, or reinterpretation is performed at this stage.
- Downstream processing consumes these files deterministically.

This directory serves solely as an immutable record of judge evaluations.