# 03 评测规则（索引入口）

**You are here：** `03_evaluation_rules/README_ZH.md`  
**Upstream：** `01_experiment_design/` → `02_prompt_variants/`  
**Downstream：** `04_results/`（证据）→ `05_summary_and_outlook/`（结论）  
**Sidecar：** `06_methodological_addenda_and_controls/`（控制实验/方法选择）

## 本目录职责
本目录定义“**如何评测已有产物**”（不重新生成）：
- 什么是 valid / invalid
- 评分维度 A–E 的含义与边界
- 实际使用的 judge 提示词
- 如何从 judge JSON 汇总成 CSV

> 本 README 只做 **索引 + 职责边界**。  
> 结果解释与归因请去：`04_results/03_results_analysis_ZH.md`。

---

## 语言约定（全仓一致）
- **无** `_ZH` 后缀：英文版
- **有** `_ZH` 后缀：中文版
- 注意：很多实验产物/资料为中文，英语母语读者可能无法直接阅读原始内容，这些文件主要用于引用与存档。

---

## 事实来源优先级 & 分工（不要混写）

### 1) 协议（流程 + 硬约束）
- `EVAL_PROTOCOL.md` / `EVAL_PROTOCOL_ZH.md`  
  负责：评测范围、A/B 不感知、可用 meta 字段、可追溯要求。

### 2) Bundle 合同 & 操作规则（脚本真正依赖的结构）
- `00_evaluation_protocol*.md`  
  负责：bundle 单位（如 16 个 PDF）、文件命名预期、invalid 条件清单。

> ⚠️ 命名提醒：当前仓库里可能存在“文件名尾部空格”：
> `00_evaluation_protocol.md `、`01_validity_criteria.md `。建议先用 `git mv` 修复，否则引用容易断链。

### 3) Validity（二值筛选）
- `01_validity_criteria.md` / `01_validity_criteria_ZH.md`  
  负责：Hard Fail / Strict Pass 边界与 invalid flags。

### 4) 评分维度（A–E 含义）
- `02_scoring_dimensions.md` / `02_scoring_dimensions_ZH.md`  
  负责：维度意图、档位解释、常见失败模式、结构优先规则。

### 5) Judge 提示词（评测时使用的固定文本）
- `JUDGE_PROMPT.md` / `JUDGE_PROMPT_ZH.md`  
  负责：judge prompt 原文 + 严格 JSON-only 输出要求。若冲突，以协议为准。

### 6) 汇总脚本（不重新判分）
- `compute_scores.py` / `compute_scores_ZH.py`  
  负责：校验 + 聚合输出 CSV；不负责评分本身。

### 7) schema（可选）
- `schema/`  
  可选的机器校验 schema；当前主汇总主要依赖 `compute_scores.py` 内置校验。

---

## judge JSON / 汇总表实际存放位置（指向 04_results）
本目录只定义规则；产物在：
- valid：
  - `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
  - `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`
- invalid：
  - `04_results/02_cross_model_evaluation/invalid_evaluations/`
- 汇总表：
  - `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/`

---

## 明确不做什么（避免与其它 README 重叠）
- 不解释结果 → 去 `04_results/03_results_analysis_ZH.md`
- 不复述实验设计 → 去 `01_experiment_design/README_ZH.md`
- 不讨论为什么选 Prompt B → 去 `06_methodological_addenda_and_controls/README_ZH.md`
