# snapshot contracts

This file defines the Snapshot constraint used in this repo.
Snapshot-related scoring uses the contract_id listed here.

---

## contract ids

### SC_50_NOEXT
- word_limit: 50
- allow_extension: false
- allow_analysis: false
- allow_recommendation: false
- intent: Short factual snapshot. No analysis. No advice.

### SC_150_EXT
- word_limit: 150
- allow_extension: true
- allow_analysis: true
- allow_recommendation: false
- intent: Short snapshot with limited analysis allowed. Still no advice.

---

## formatting

- Snapshot is the first section.
- Snapshot is one paragraph (no lists, no sub-headings).
- Exceeding the word limit counts as a Snapshot constraint violation.

---

## bindings

### prompt variants
- supplement/02_prompt_variants/00_baseline_prompt_A.txt   -> SC_50_NOEXT
- supplement/02_prompt_variants/01_structured_prompt_B.txt -> SC_50_NOEXT
- supplement/02_prompt_variants/02_conflict_prompt.txt     -> SC_50_NOEXT
- supplement/02_prompt_variants/03_long_prompt.txt         -> SC_50_NOEXT
- supplement/02_prompt_variants/04_weak_prompt.txt         -> SC_50_NOEXT

### raw judge runs
- supplement/04_results/02_raw_judge_evaluations/v0_baseline_judge/      -> SC_50_NOEXT
- supplement/04_results/02_raw_judge_evaluations/v1_paraphrase_judge/    -> SC_150_EXT
- supplement/04_results/02_raw_judge_evaluations/v2_schema_strict_judge/ -> SC_150_EXT

### ablation prompts (extension enabled)
- promptv0 -> SC_150_EXT
- promptv1 -> SC_150_EXT
- promptv2 -> SC_150_EXT

---

## run metadata

Each run records:
- snapshot_contract_id
- snapshot_word_limit
- snapshot_allow_extension

Example:
snapshot_contract_id: SC_50_NOEXT
snapshot_word_limit: 50
snapshot_allow_extension: false