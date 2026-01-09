# 01 实验设计（Experiment Design）

本目录存放本项目的**实验设计输入与版本化工件**：
- 题集（evaluation set / questions）
- 生成输出的期望格式（output schema）
- 运行配置模板（experiment protocol）
- 术语对齐与威胁/局限（writeup 边界）

> 本目录**不定义评分/评测规则**。
> 评测规则在：`03_evaluation_rules/`（权威入口：`EVAL_PROTOCOL_ZH.md`）。
> 结果与分析在：`04_results/`。

---

## 0) 30 秒导航（从这里开始）

- 想修改题集（questions）？
  → `eval_questions_ZH.jsonl`（中文）/ `eval_questions_EN.jsonl`（英文）

- 想确认生成输出格式要求？
  → `output_schema_ZH.md` / `output_schema.md`

- 想看运行配置模板（模型、采样参数等要记录什么）？
  → `experiment_protocol_ZH.yaml` / `experiment_protocol.yaml`

- 想看“5 步实验设计说明”（设计 rationale）？
  → `design_five_step_ZH.md` / `design_five_step.md`

- 想保证全仓术语一致？
  → `terminology_alignment_ZH.md` / `terminology_alignment.md`

- 想写方法局限/威胁模型？
  → `threats_and_limitations_ZH.md` / `threats_and_limitations.md`

---

## 1) 分工边界（该放什么/不该放什么）

### 属于 `01_experiment_design/` 的内容
- **题集**：题目内容 + 稳定 question_id
- **输出 schema**：生成侧应遵循的格式契约
- **实验协议模板**：运行配置需要落盘的字段
- **设计 rationale**：为什么这样设计（高层，不谈结果）
- **术语对齐**：全仓一致写法
- **威胁与局限**：风险、边界、不可外推点

### 不属于本目录的内容
- **评分/评测规则细节** → `03_evaluation_rules/`
- **Prompt 变体与提示词文本** → `02_prompt_variants/`
- **结果表与结果分析** → `04_results/`

---

## 2) 目录地图（实验设计工件）

```
01_experiment_design/
  README.md
  README_ZH.md
  eval_questions_EN.jsonl
  eval_questions_ZH.jsonl
  output_schema.md
  output_schema_ZH.md
  experiment_protocol.yaml
  experiment_protocol_ZH.yaml
  design_five_step.md
  design_five_step_ZH.md
  terminology_alignment.md
  terminology_alignment_ZH.md
  threats_and_limitations.md
  threats_and_limitations_ZH.md
```

---

## 3) 版本化建议（推荐口径）

- 题集的“可比性”依赖稳定的 `question_id`（如 `q1`, `q2`...）。
- 任何会影响可比性的改动（题目内容、schema 关键字段）都应在：
  - `design_five_step(.md|_ZH)` 或 commit message / release notes 中说明。

---

## 4) 与其他目录如何串联

- **Prompt 变体**：`02_prompt_variants/`
- **评测规则**：`03_evaluation_rules/`
- **结果工件**：`04_results/`