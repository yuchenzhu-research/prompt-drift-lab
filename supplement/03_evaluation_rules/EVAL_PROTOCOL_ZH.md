# 00_评测协议

## 0. 本目录的作用与优先级

本目录用于**固定** Prompt Drift Lab 的评测规则与执行方式，确保评测结果可复现、可审计、可对照。

**优先级顺序**

1) `EVAL_PROTOCOL.md`：唯一可执行的评测规范（Rubric、JSON 合同、evidence 硬约束）。
2) `JUDGE_PROMPT.md`：评测器使用的固定提示词；与评测规范保持一致，不引入额外规则。
3) `01_validity_criteria.md`、`02_scoring_dimensions.md`：解释性材料，用于说明规则含义，不改变评测口径。

> 本目录内所有文件命名与字段命名均采用英文，并在整个项目中保持一致。

---

## 1. 评测对象与输入

### 1.1 被测对象

- 不同生成模型在同一套提示词条件下生成的三段式结构化输出（以 PDF 形式保存）。

### 1.2 输入 bundle

一个评测 bundle 包含 16 个 PDF，覆盖以下组合：

- `questions`：`Q3`、`Q4`
- `prompt_variant`：`baseline`、`long`、`weak`、`conflict`
- `trigger_type`：`implicit`、`explicit`

**文件命名约定**

- `q{3|4} {prompt_variant} {implicit|explicit}.pdf`
- 示例：`q3 baseline explicit.pdf`

---

## 2. 输出产物

每次评测生成 **1 个严格 JSON 文件**（仅包含协议定义字段），供后续脚本汇总与复算。

### 2.1 交叉评测（cross-model judging）产物命名

- `judge_{judge_model}_bundle_{generator_model}.json`

### 2.2 自评（self-judging）产物命名

- `self_judge_{model}.json`

### 2.3 存放位置

- 合规产物（valid）：`supplement/04_results/02_cross_model_evaluation/valid_evaluations/`
- 不合规产物（invalid）：`supplement/04_results/02_cross_model_evaluation/invalid_evaluations/`

invalid 产物不进入主统计，但保留用于偏差与协议遵循分析。

---

## 3. 评测方法

### 3.1 主方法：交叉评测（Cross-model judging）

- 使用 judge 模型对其他生成模型的 16 个 PDF 逐文件评分。
- 主统计结果基于 **valid 的交叉评测记录**。

若某个 judge 模型的输出不满足协议要求（例如非严格 JSON、字段缺失或 evidence 违规），该产物被标记为 invalid，仅用于单独分析，不纳入主统计。

### 3.2 补充方法：自评（Self-judging）

- 生成模型对自身生成的 16 个 PDF 按同一协议评分。
- 自评结果用于一致性校验与偏差诊断，不作为主结论的唯一依据。

---

## 4. 合规性与 invalid 判定规则

任一 judge 输出满足以下条件之一时，判定为 **invalid**：

- 输出不是严格 JSON（包含 Markdown、解释性文字或前后缀）
- JSON 合同不匹配、字段缺失或条目数量不符合协议
- `total` 不等于五个维度得分之和
- `A_structure == 0` 且 `B/C/D/E` 中存在非 0 分
- evidence 不符合硬约束（非原文截取、包含省略符号、空 evidence 却给非 0 分等）
- `aggregates` 与 `per_file_scores` 无法相互复算

---

## 5. 偏差控制与记录要求

- **盲评**：评测仅依据 PDF 内容与文件名中的元信息字段，不引入提示词角色或对照标签作为先验。
- **统一协议**：所有评测使用同一份 `EVAL_PROTOCOL.md` 与 `JUDGE_PROMPT.md`。
- **元信息记录**：记录模型名称/版本、运行日期、推理模式、`temperature`、`top_p` 等信息，用于复现差异排查。