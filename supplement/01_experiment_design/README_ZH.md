# 01 实验设计

本目录存放本项目的**实验设计输入与版本化工件**，包括：
- 题集
- 生成输出的期望格式
- 运行配置模板
- 术语对齐与威胁/局限（用于方法说明与复现边界）

> **重要说明**
> - 本目录**不定义评分或评测规则**。
> - 评分与评测规则**唯一且权威**地定义在：`supplement/03_evaluation_rules/`。
> - 评测协议的权威入口为：`supplement/03_evaluation_rules/EVAL_PROTOCOL_ZH.md`。
> - 本目录中的英文文件仅作为**审稿可读性参考**，不构成独立定义或第二套规则。

---

## 0) 30 秒导航

- **修改题集**
  → `eval_questions_ZH.jsonl`（权威）
  → `eval_questions_EN.jsonl`（参考翻译）

- **确认生成输出格式要求**
  → `output_schema_ZH.md`（权威）
  → `output_schema.md`（参考翻译）

- **查看或调整运行配置模板**
  → `experiment_protocol_ZH.yaml`（权威）
  → `experiment_protocol.yaml`（参考翻译）

- **阅读实验设计 rationale（5 步设计说明）**
  → `design_five_step.md`
  
  > 说明：该文件以英文撰写，用于审稿人理解实验设计逻辑；其内容与权威中文设计意图保持一致，不引入额外规则。

- **核对全仓术语一致性**
  → `terminology_alignment_ZH.md`（权威）

- **查看已知威胁与方法局限**
  → `threats_and_limitations_ZH.md`（权威）
  → `threats_and_limitations.md`（参考翻译）

---

## 1) 分工边界

### 属于 `01_experiment_design/` 的内容
- **题集**：题目内容与稳定的 `question_id`
- **输出 schema**：生成侧需遵循的格式契约
- **实验协议模板**：运行配置与元信息的记录规范
- **设计 rationale**：实验设计动机与结构（不包含结果）
- **术语对齐**：全仓统一命名与含义
- **威胁与局限**：方法风险、边界与不可外推点

### 不属于本目录的内容
- **评分 / 评测规则细节** → `supplement/03_evaluation_rules/`
- **Prompt 变体与提示词文本** → `supplement/02_prompt_variants/`
- **结果表、统计或分析** → `supplement/04_results/`

---

## 2) 目录地图

```
01_experiment_design/
  README.md
  README_ZH.md
  eval_questions_ZH.jsonl
  eval_questions_EN.jsonl
  output_schema_ZH.md
  output_schema.md
  experiment_protocol_ZH.yaml
  experiment_protocol.yaml
  design_five_step.md
  terminology_alignment_ZH.md
  threats_and_limitations_ZH.md
  threats_and_limitations.md
```

> 注：本目录不包含评分逻辑或结果文件。

---

## 3) 版本化与修改约定

- 带 `_ZH` 后缀的文件为**权威定义**，决定实验语义与可比性。
- 英文文件为**非权威参考翻译**，不引入新的字段、规则或假设。
- 题集的可比性依赖稳定的 `question_id`。

---

## 4) 与其他目录的关联关系

- **Prompt 变体** → `supplement/02_prompt_variants/`
- **评测规则** → `supplement/03_evaluation_rules/`
- **结果工件** → `supplement/04_results/`

