# Prompt Drift Lab
**大语言模型结构化提示词稳定性评测与归因实验（Prompt Drift）**

> 双语仓库约定：
> - **不带** `_ZH` 的文件为**英文版**
> - **带** `_ZH` 的文件为**中文版**
>
> 关于 PDF（重要说明）：
> - `07_deep_research/` 下的 PDF **多数为中文**，英语母语读者可能无法直接阅读。
> - 我保留它们是为了**引用、可追溯与实验记录**（并非“必须阅读材料”）。

- English entry: [`README.md`](README.md)

---

## 0) 30 秒导航

1. **实验设计** → `01_experiment_design/README_ZH.md`
2. **生成侧提示词与变体** → `02_prompt_variants/README_ZH.md`
3. **评测规则（协议 + judge 契约）** → `03_evaluation_rules/README_ZH.md`
4. **结果工件与表格** → `04_results/README_ZH.md`
5. **解释层 + 边界声明（不引入新实验）** → `05_summary_and_outlook/README_ZH.md`

---

## 1) 目录分工（按文件夹）

- `01_experiment_design/`  
  题集（`eval_questions_*.jsonl`）、实验协议（`experiment_protocol*.yaml`）、输出 schema、术语对齐。

- `02_prompt_variants/`  
  **生成侧** prompt 与受控变体（A/B/…）；manifest 用于映射 `prompt_id/prompt_version -> 文件`.

- `03_evaluation_rules/`  
  **评测侧**契约：评测协议、有效性判定、评分维度、输出 schema。
  - 关键入口：`EVAL_PROTOCOL_ZH.md`, `JUDGE_PROMPT_ZH.md`

- `04_results/`  
  原始输出、评测 JSON/CSV、汇总表与分析笔记（“证据层”）。

- `05_summary_and_outlook/`  
  **解释层**：结果总结、方法启示、明确 non-claims、未来工作方向  
  （必须可追溯到 `04_results/` 与 `03_evaluation_rules/`）。

- `06_methodological_addenda_and_controls/`  
  方法补充、对照与 rationale：解释“为什么这样设计”，但不夸大结论。

- `07_deep_research/`  
  文献笔记与 PDF（常为中文），用于**引用/记录**。

---

## 2) 结论边界（务必遵守）

- 本仓库是 **artifact-first**：提示词、协议、输出、打分与表格都显式保存。
- 任何解释性文字都应能**追溯**到：
  - `04_results/` 的结果工件，以及
  - `03_evaluation_rules/` 的评测规则。
- 不应把本仓库当作“可广泛泛化”的 benchmark 来做超出记录设置的主张。

---

## 3) 最小复现方式

- 基于已有评测输出进行重算/汇总：
  - 见 `03_evaluation_rules/compute_scores.py`
- 若要完整复跑（重新生成模型输出），需要外部模型调用权限；本仓库不保证一键跑通整条生成链路。

---

## 4) 命名约定

- `_ZH` 后缀 = 中文对应版本
- 用稳定 id（`question_id/prompt_id/prompt_version`）保证可审计与可对齐
