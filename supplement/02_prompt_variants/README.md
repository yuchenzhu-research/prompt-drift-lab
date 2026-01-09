# 02 Prompt Variants

This folder contains the **generator-side prompts** and their controlled variants used to probe instruction-following stability (prompt drift).

> This folder is **not** for judge prompts. Judge prompts and scoring rules live in: `03_evaluation_rules/` (see `JUDGE_PROMPT.md` and `EVAL_PROTOCOL.md`).

---

## 0) 30-second start

- Want to see the exact prompts used in the experiment?

  - Start from the manifest (recommended):
    - `PROMPT_MANIFEST.md` (EN) / `PROMPT_MANIFEST_ZH.md` (ZH)
  - Or inspect the prompt files directly:
    - `00_baseline_prompt_A*.txt`
    - `01_structured_prompt_B*.txt`
    - `02_conflict_prompt*.txt`

- Want to know how prompts connect to results?

  - Results snapshots (if present) live under:
    - `04_results/**/used_prompt_manifest*.md`

---

## 1) What belongs here (and what does not)

### Belongs in `02_prompt_variants/`

- Generator prompts (prompt text) and **their variants** used as experimental factors
- A prompt manifest that maps `prompt_id / prompt_version -> filename`
- Notes about prompt versioning (not scoring rules)

### Does NOT belong here

- Scoring / judging rules → `03_evaluation_rules/`
- Results / tables / analysis → `04_results/`

---

## 2) Recommended manifest contract

If `PROMPT_MANIFEST.md` exists, treat it as the **single source of truth** for prompt inventory:

- `prompt_id` (stable)
- `prompt_version` (stable label used in runs)
- `language` (EN/ZH)
- `filepath` (relative path in this folder)

This keeps runs auditable and lets results directories snapshot the exact manifest used.

---

## 3) Directory map (typical)

```
02_prompt_variants/
  README.md
  README_ZH.md
  PROMPT_MANIFEST.md
  PROMPT_MANIFEST_ZH.md
  00_baseline_prompt_A.txt
  00_baseline_prompt_A_ZH.txt
  01_structured_prompt_B.txt
  01_structured_prompt_B_ZH.txt
  02_conflict_prompt.txt
  02_conflict_prompt_ZH.txt
```

(If your actual filenames differ, update the manifest and this README accordingly.)

---

## 4) Versioning rules (simple & safe)

- Do not overwrite prompts silently if you want comparability.
- Prefer: add a new file or update the manifest with a new `prompt_version`.
- Keep `prompt_id` stable across versions so analysis can group by id.

---

## 5) How this connects to the rest of the repo

- Experimental inputs (questions, schema) → `01_experiment_design/`
- Scoring rules + judge contract → `03_evaluation_rules/`
- Results + snapshots → `04_results/`