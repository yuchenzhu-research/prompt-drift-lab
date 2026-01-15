# snapshot contracts

This file defines **Snapshot** constraints only. It MUST NOT define scoring rules, validity rules, or any cross-file precedence.

---

## 1. snapshot block (hard format)

A Snapshot block is the **first block** of the judge output.

### 1.1 required order and count
The judge output MUST start with exactly **one** Snapshot block.

The Snapshot block MUST contain exactly:
1) **one header line**
2) **one body paragraph**

No additional lines, headings, lists, appendices, or trailing text are allowed inside the Snapshot block.

### 1.2 required header (verifiable)
The Snapshot header line MUST be exactly **one** of the following:
- `1. [事实快照]`
- `1. [Snapshot]`

Anything else MUST be treated as a Snapshot-format violation.

### 1.3 required body shape (verifiable)
The Snapshot body MUST be:
- exactly **one paragraph**
- **plain text only** (no bullet lists, no numbered lists, no sub-headings)

The body MUST NOT contain:
- extra section markers (e.g., `2.` / `##` / `Appendix`)
- additional blocks separated by blank lines

---

## 2. content type constraints (by contract_id)

The Snapshot body MUST follow the content-type constraints of the active `contract_id`.

Content types are judged by surface intent, not by correctness:
- **facts / phenomena**: descriptions of observed outputs, structure, or visible properties
- **analysis**: explanations, causes, interpretations, or reasoning
- **recommendations**: advice, next steps, instructions, or suggested actions

### 2.1 SC_50_NOEXT
- `word_limit`: 50 words (Section 3)
- Allowed content types: **facts / phenomena** only
- MUST NOT include: **analysis**, **recommendations**

### 2.2 SC_150_EXT
- `word_limit`: 150 words (Section 3)
- Allowed content types: **facts / phenomena**, **analysis**
- MUST NOT include: **recommendations**

---

## 3. verifiable constraints

### 3.1 word limit
The Snapshot body MUST NOT exceed the contract `word_limit`.

- Words MUST be counted by splitting on whitespace.
- Any count above the limit MUST be treated as a Snapshot constraint violation.

### 3.2 prohibited formatting tokens (quick checks)
The Snapshot block MUST NOT contain any of the following patterns:
- list markers: `- `, `* `, `1)`, `2)`
- markdown headings: `#`, `##`, `###`
- section starters after the Snapshot header: a new line starting with `2.`

If any pattern appears, it MUST be treated as a Snapshot-format violation.

---

## 4. bindings (which contract_id applies)

### 4.1 prompt variants
- `supplement/02_prompt_variants/00_baseline_prompt_A.txt`   -> `SC_50_NOEXT`
- `supplement/02_prompt_variants/01_structured_prompt_B.txt` -> `SC_50_NOEXT`
- `supplement/02_prompt_variants/02_conflict_prompt.txt`     -> `SC_50_NOEXT`
- `supplement/02_prompt_variants/03_long_prompt.txt`         -> `SC_50_NOEXT`
- `supplement/02_prompt_variants/04_weak_prompt.txt`         -> `SC_50_NOEXT`

### 4.2 ablation prompts
- `promptv0` -> `SC_150_EXT`
- `promptv1` -> `SC_150_EXT`
- `promptv2` -> `SC_150_EXT`

---

## 5. run metadata fields (required)

Each run MUST record:
- `snapshot_contract_id`
- `snapshot_word_limit`
- `snapshot_allow_extension`

Example:
- `snapshot_contract_id: SC_50_NOEXT`
- `snapshot_word_limit: 50`
- `snapshot_allow_extension: false`