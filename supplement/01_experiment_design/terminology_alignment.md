# terminology_alignment.md (Terminology & Naming Conventions)

> Purpose: enforce **one canonical term / one canonical key** across the repository, preventing inconsistent naming across 01/02/03/04.

## 1. Entities & Roles

- **Prompt Drift**: Systematic differences in model outputs caused *only* by small changes in prompt wording, formatting, or structure, manifesting in instruction-following, structural validity, or semantic alignment.
- **Generator (generation model)**: The model under evaluation that produces task outputs (e.g., ChatGPT, Gemini, Claude).
- **Judge (evaluation model)**: The model that scores generated outputs according to a rubric or protocol and provides evidence-based judgments. The judge may be the same or a different model from the generator.

## 2. Factors & Canonical Keys

> All recorded fields **must use snake_case**.

- **question_id**: Unique identifier of the evaluation question. Canonical values: `q1`, `q2`, `q3`, `q4`
- **prompt_version**: Prompt variant identifier. Canonical values: `prompt_a`, `prompt_b`
  - Note: Even if the main experiment uses only `prompt_b`, the `prompt_a` field should be preserved for extensibility.
- **length_variant**: Prompt length condition. Canonical values: `short`, `long`
- **instruction_variant**: Instruction explicitness. Canonical values: `explicit`, `implicit`
- **generator_model**: Identifier of the generation model (free string, but must be consistent; e.g., `chatgpt`, `gemini`, `claude`).
- **judge_model**: Identifier of the evaluation model (same convention as `generator_model`).
- **run_id**: Unique identifier for a single generation run (recommended: timestamp or hash).
- **eval_id**: Unique identifier for a single evaluation record (recommended: timestamp or hash).

## 3. Artifact Naming Conventions

> Existing artifacts do not need to be renamed. The following conventions apply to newly generated artifacts.

### Generation Outputs (PDF)

- **Pattern**:
  ```
  {question_id}__{length_variant}_{instruction_variant}__{prompt_version}__{generator_model}.pdf
  ```
- **Example**:
  ```
  q3__long_implicit__prompt_b__chatgpt.pdf
  ```

### Evaluation Records (JSON)

- **Pattern**:
  ```
  {eval_id}__{judge_model}__on__{generator_model}__{question_id}.json
  ```
- **Example**:
  ```
  2025-12-23T21-10-00__gemini__on__chatgpt__q3.json
  ```

## 4. Metrics: Canonical Keys & Definitions

> Metric keys define **terminology only**. Scoring rules are specified in the rubric.

| metric_key | Definition |
|---|---|
| instruction_following | Whether the model completes the requested task and satisfies the core instruction without deviation. |
| schema_validity | Whether the output strictly conforms to the required format or schema (Markdown, JSON, sectioning, etc.). |
| section_coverage | Whether all required sections or fields are present, without omission. |
| semantic_drift | Whether the output meaning deviates from the intended or baseline semantics. |
| hallucination_risk | Presence of fabricated, unverifiable, or unreliable content. |
| citation_compliance | Whether required citations are provided and whether fabricated citations are avoided. |
| verbosity_control | Whether the response length is appropriate and avoids unnecessary expansion. |
| refusal_safety | Whether refusals or safety-related responses are appropriate and not overly restrictive. |

## 5. Synonym Convergence (Do Not Mix)

- “A/B versions” → `prompt_a` / `prompt_b`
- “explicit / implicit instructions” → `explicit` / `implicit`
- “long / short prompts” → `long` / `short`
- “instruction adherence / compliance / following” → `instruction_following`
- “format break / structural failure / template violation” → `schema_validity` (use `section_coverage` if partial)

