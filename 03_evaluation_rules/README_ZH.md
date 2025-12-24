# 03 评测规则（Evaluation Rules）

本目录定义本项目的**评测侧契约**：
- 什么输出算有效/无效（valid/invalid）
- 评分维度如何定义与使用
- judge 必须输出什么结构（可脚本聚合的 JSON）

> **唯一权威入口（中文）：** `03_evaluation_rules/EVAL_PROTOCOL_ZH.md`  
> 若任何文件与协议不一致，**以协议为准**。

---

## 0) 30 秒导航（从这里开始）

- 想理解/修改评测规则？  
  → 只看/只改：`EVAL_PROTOCOL_ZH.md`

- 想看 judge 的提示词契约（输入/输出 + 约束）？  
  → 看：`JUDGE_PROMPT_ZH.md`

- 想看维度解释（仅解释，不改规则）？  
  → 看：`02_scoring_dimensions_ZH.md`

- 想看合规/有效性解释？  
  → 看：`01_validity_criteria_ZH.md`

- 想把 judge JSON 聚合成表格？  
  → 跑：`compute_scores_ZH.py`

---

## 1) 文件分工（不要越权）

### 权威协议（改规则只改这里）
- `EVAL_PROTOCOL_ZH.md` — **评测协议权威规范（中文）**
- `EVAL_PROTOCOL.md` — 评测协议权威规范（英文）

### 解释性文档（不得覆盖协议）
- `01_validity_criteria_ZH.md` / `01_validity_criteria.md` — 合规/有效性判定解释
- `02_scoring_dimensions_ZH.md` / `02_scoring_dimensions.md` — 评分维度解释

### Judge 契约（必须服从协议）
- `JUDGE_PROMPT_ZH.md` / `JUDGE_PROMPT.md` — A/B 不感知、只按 Rubric、仅输出 JSON

### 聚合脚本（机械执行，不引入新规则）
- `compute_scores_ZH.py` / `compute_scores.py` — 从 judge 输出 JSON 计算汇总表

### 可选/历史说明
- `00_evaluation_protocol_ZH.md` / `00_evaluation_protocol.md` — 背景说明（若存在）。  
  仅作解释，不得与 `EVAL_PROTOCOL(.md|_ZH).md` 冲突。

### Schema（若使用）
- `schema/` — JSON schema 或相关结构化规范文件。

---

## 2) 结果在哪里
本目录只负责“规则与评分逻辑”。结果工件统一在：
- `04_results/`（原始输出、judge JSON、CSV 汇总表）