# 02 Prompt Variants

This directory contains the **generator-side prompt definitions** and their
controlled variants used to probe instruction-following stability (prompt drift).

This directory does **not** contain judge prompts or scoring logic. All evaluation
rules and judge-side prompts are defined under
`supplement/03_evaluation_rules/`.

---

## 0) Quick orientation

- **Prompt inventory and scope**
  - See `PROMPT_MANIFEST.md` (authoritative)

- **Prompt content**
  - Individual prompt files are stored as `.txt` and referenced by the manifest

- **Result linkage**
  - When present, result snapshots record the exact manifest used for execution
    under `supplement/04_results/**/used_prompt_manifest*.md`

---

## 1) Scope definition

### Included

- Generator-side prompt texts used as experimental input factors
- Explicit prompt variants defined and tracked via `PROMPT_MANIFEST.md`
- Documentation describing prompt variant structure and variable hierarchy

### Excluded

- Judge prompts and scoring rules
- Evaluation rubrics or validity criteria
- Result tables, plots, or analyses

---

## 2) Manifest authority and auditability

- `PROMPT_MANIFEST.md` is the **single source of truth** for the prompt inventory
  used in experiments.
- Prompt files listed in the manifest are treated as **preserved execution
  assets** and must not be modified in place.
- Result directories may snapshot the exact manifest used for a run to support
  auditability and traceability.

---

## 3) Directory structure

```
02_prompt_variants/
  README.md
  PROMPT_MANIFEST.md
  *.txt
```

Only files that physically exist in the directory are listed here. The
authoritative inventory of prompt files and variants is maintained in
`PROMPT_MANIFEST.md`.

---

## 4) Versioning and modification rules

- Do not silently overwrite existing prompt files if comparability is required.
- To introduce a new variant:
  1. Add a new `.txt` file.
  2. Register the variant in `PROMPT_MANIFEST.md` with a new `prompt_variant`.
- Keep `prompt_family` and `prompt_id` stable across variants to support
  aggregation and comparison.

---

## 5) Relation to other components

- Experimental inputs (questions, schemas): `supplement/01_experiment_design/`
- Evaluation rules and judge contracts: `supplement/03_evaluation_rules/`
- Results and execution snapshots: `supplement/04_results/`