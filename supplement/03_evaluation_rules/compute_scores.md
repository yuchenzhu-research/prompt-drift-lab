# compute scores — deterministic JSON-to-summary mapping (archival)

## 0. scope (hard)

This file specifies the **mechanical behavior** of `compute_scores.py` only.

- It SHALL describe only actions that `compute_scores.py` actually performs.
- It MUST NOT introduce evaluation rules, scoring rules, validity rules, or any analysis narrative.
- It MUST NOT parse PDFs or read any natural-language sections from model outputs.

---

## 1. stable inputs (CLI only)

`compute_scores.py` MUST consume only the following stable inputs:

- `--run_dir`: path to one run directory (string path)
- `--rubric`: path to one rubric markdown file (string path)
- `--output`: path to one output JSON file (string path)

The script MUST NOT:
- read or parse any PDF files
- read any model output text content
- use directory names, file names, or model names as semantic signals
- use any `bundle_meta`-like metadata to make decisions

---

## 2. deterministic procedure (same input → same output)

Given the same CLI arguments and filesystem existence state, the script MUST behave deterministically.

The procedure is:

1) Check `run_dir` exists and is a directory.
2) Check `rubric` file exists.
3) Create parent directory for `output` if needed.
4) Write exactly one JSON object to `output` with the fields defined in Section 3.

The procedure MUST NOT depend on:
- filesystem traversal order
- OS-specific directory listing order
- path name semantics

No randomness SHALL be used.

---

## 3. output JSON (exact fields)

The script MUST write a single JSON object to `--output` with exactly these keys:

- `run_dir`: string (the CLI `--run_dir` value serialized)
- `rubric`: string (the CLI `--rubric` value serialized)
- `status`: string, fixed value `"ok"`
- `note`: string, fixed value `"Utility script executed for internal analysis only."`

The output MUST be valid strict JSON.

---

## 4. prohibited content (hard)

This file (and the script behavior it describes) MUST NOT include:

- any aggregation of `per_file_scores`
- any computation over judge records
- any explanation of what averages/variance mean
- any statement of “why this mapping is used”
- any phase language (`v0`, `v1`, `v2`)
- any result or trend language (drift, stability, mitigation)

---

## 5. correspondence to code (one-to-one)

Each section above corresponds to `compute_scores.py`:

- Section 1: `argparse` definitions for `--run_dir`, `--rubric`, `--output`
- Section 2 (Steps 1–3): filesystem existence checks and `output.parent.mkdir(...)`
- Section 3: the `summary = {...}` object and `json.dump(...)`

No other behavior is specified in this document.