# 03 评测规则

本目录定义本项目的**评测侧契约**，用于固定评测行为与结果解释方式：

- 判定输出是否有效（valid / invalid）
- 定义评分维度及其使用方式
- 约束 judge 的输入、输出结构与证据要求（严格 JSON）

**权威性声明**

- 带 `_ZH` 后缀的文件构成本项目评测规则的**唯一权威定义**。
- 英文文件仅作为**可读性参考翻译**，不具备规范效力。
- 若任一文件与权威协议存在差异，**以对应的 `_ZH` 文件为准**。

**唯一权威入口（中文）**

- `03_evaluation_rules/EVAL_PROTOCOL_ZH.md`

---

## 0) 快速导航

- **修改或审查评测规则**
  - 仅查看或修改：`EVAL_PROTOCOL_ZH.md`

- **查看 judge 的提示词契约（输入 / 输出 / 约束）**
  - 查看：`JUDGE_PROMPT_ZH.md`

- **理解评分维度（解释性，不改变规则）**
  - 查看：`02_scoring_dimensions_ZH.md`

- **理解合规性与 invalid 判定（解释性，不改变规则）**
  - 查看：`01_validity_criteria_ZH.md`

- **从 judge JSON 生成汇总表**
  - 执行：`compute_scores_ZH.py`

---

## 1) 文件职责划分

### 权威协议

- `EVAL_PROTOCOL_ZH.md` — **评测协议的唯一权威规范**
- `EVAL_PROTOCOL.md` — 权威协议的英文参考版本

### 解释性文档

- `01_validity_criteria_ZH.md` / `01_validity_criteria.md` — 合规与有效性判定解释
- `02_scoring_dimensions_ZH.md` / `02_scoring_dimensions.md` — 评分维度解释

### Judge 契约

- `JUDGE_PROMPT_ZH.md` / `JUDGE_PROMPT.md`
  - A/B 不感知
  - 严格按 Rubric 评分
  - 仅输出协议规定的 JSON 结构

### 聚合脚本

- `compute_scores_ZH.py` / `compute_scores.py`
  - 从 judge 输出 JSON 计算汇总结果

### 说明性文档

- `00_evaluation_protocol_ZH.md` / `00_evaluation_protocol.md`
  - 背景与设计说明
  - 不得与 `EVAL_PROTOCOL_ZH.md` 或 `EVAL_PROTOCOL.md` 冲突

### Schema

- `schema/`
  - JSON schema 及相关结构化规范文件

---

## 2) 结果位置说明

本目录仅定义**评测规则与评分逻辑**。

所有评测结果与中间产物统一存放于：

- `supplement/04_results/`