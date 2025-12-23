# Prompt Drift Lab
**大语言模型结构化提示词稳定性评测与归因实验**  
*Prompt Drift Lab: A Reproducible Evaluation Framework for Instruction-Following Stability in LLMs*

> 中文为主；模型/框架/关键术语保留英文，便于对齐学界与工业界阅读习惯。  
> 本仓库面向两类读者：  
> - **科研评审/导师**：关心可复现、证据链、归因逻辑  
> - **工业 Mentor/用人方**：关心可落地的 eval 闭环、提示词版本管理、失败模式沉淀

---

## 1. 研究动机（Why this exists）

在真实应用中，LLM 的输出会因**提示词格式、措辞、长度、冲突约束**等微小变化而出现：
- 指令遵循率下降（instruction following drop）
- 结构/格式崩坏（format break）
- 语义漂移或答非所问（semantic drift / off-topic）
- “表面合规但关键约束漏掉”的隐性失败（silent constraint violation）

我们把这类“对提示词微扰高度敏感，导致行为退化”的现象称为 **Prompt Drift**。  
本项目做的事情很简单：把它工程化为一个可复现闭环：

> **Prompt 设计 → 批量运行 → 统一评分 → 汇总对比 → 失败归因 → 迭代沉淀**

---

## 2. 你会在这个仓库里得到什么（What you get）

- 一套固定题集：`01_实验设计/问题集.jsonl`
- 一组可对照的提示词版本：`02_提示词版本/*.txt` + `PROMPT_MANIFEST.md`
- 一套评测协议与评委提示词：`03_评测规则/EVAL_PROTOCOL.md` + `JUDGE_PROMPT.md`
- 一组原始产物与评测产物：PDF（模型输出）、JSON（评审记录）、CSV（统计汇总）
- 一份“结果索引/解读入口”：`04_实验结果/`（从表格与样例证据开始读）

---

## 3. 研究问题（Research Questions）

- **RQ1：Prompt Drift 的主要表现形态是什么？**（合规失败、结构崩坏、语义漂移、漏约束等）
- **RQ2：哪些提示词微扰最容易触发退化？**（长度、冲突指令、弱化约束、格式要求等）
- **RQ3：不同模型对同一微扰的敏感性是否一致？**（cross-model robustness）
- **RQ4：失败能否被系统归因到“可修复的提示词设计缺陷”？**（可执行的改进建议）

---

## 4. 快速开始（Reproducibility Quickstart）

### 4.1 第一次阅读建议走这条路径
1) 打开 `01_实验设计/README.md`：先理解题集、协议、输出结构  
2) 打开 `02_提示词版本/PROMPT_MANIFEST.md`：明确本次对照的 Prompt 版本与差分意图  
3) 打开 `03_评测规则/EVAL_PROTOCOL.md` 与 `JUDGE_PROMPT.md`：确认评审标准与输出格式  
4) 在 `04_实验结果/` 里：
   - 先看 `summary.csv`（总体现象）
   - 再看 `main_method_*` 与 `supporting_method_*`（主方法/辅助方法对照）
   - 最后抽样回看对应 PDF 与 judge JSON（建立证据链）

> 本仓库强调：失败产物不是“丢弃”，而是作为证据链用于归因与改进。

### 4.2 实验纪律（强烈建议遵守）
- 固定：题集版本、Prompt 版本、模型版本、采样参数（temperature/seed/次数）
- 记录：运行日志（run log）、原始输出、评审输出、汇总表
- 协议或提示词每次修改，都应同步更新 manifest 与说明文档

---

## 5. 仓库结构（Repository Structure）

```text
├── 01_实验设计/
│   ├── README.md
│   ├── 实验设计_五步法.md
│   ├── 实验协议.yaml
│   ├── 标准输出结构.md
│   ├── 问题集.jsonl
│   └── 威胁与局限.md
│
├── 02_提示词版本/
│   ├── 00_baseline_prompt_A.txt
│   ├── 01_structured_prompt_B.txt
│   ├── 02_conflict_prompt.txt
│   ├── 03_long_prompt.txt
│   ├── 04_weak_prompt.txt
│   └── PROMPT_MANIFEST.md
│
├── 03_评测规则/
│   ├── 00_评测协议.md
│   ├── 01_合规性判定说明.md
│   ├── 02_行为评分维度说明.md
│   ├── EVAL_PROTOCOL.md
│   ├── JUDGE_PROMPT.md
│   └── compute_scores.py
│
├── 04_实验结果/
│   ├── （模型原始输出 PDF）
│   ├── （互评/自评 judge JSON）
│   ├── （统计汇总 CSV：summary/main_method/supporting_method 等）
│   └── （结果解读与分析文档）
│
├── 05_总结与展望/
│   └── README.md
│
└── README.md
```
## 6. 方法概览（Method Overview）

本项目采用 **protocol-driven evaluation** 的工程化思路，将“提示词微小变化导致的行为退化”转化为一个可复现、可对照、可归因的评测流程。

### 6.1 提示词版本（Prompt Variants）

使用多种具有**最小差分**的提示词版本，用于构造 *prompt perturbation space*：

- **baseline**：最小可用提示词，作为对照基线
- **structured**：显式结构化约束（标题/字段/顺序）
- **long**：增加上下文与冗余说明，用于测试“长度是否提升遵循率”
- **weak**：弱化约束强度，测试模型是否会回退为自然对话模式
- **conflict**：引入潜在冲突或张力指令，测试优先级处理与对齐策略

每个版本的设计动机与差分说明详见：`02_提示词版本/PROMPT_MANIFEST.md`。

---

### 6.2 固定题集（Eval Set）

采用固定题集（`01_实验设计/问题集.jsonl`）以确保不同提示词版本、不同模型之间的**可对照性**。

当前题集主要用于验证：
- 指令遵循失败是否可被稳定触发
- 不同问题类型是否会放大或抑制 Prompt Drift

题集规模与领域范围在本阶段刻意保持克制，后续可扩展为多领域/多难度分层。

---

### 6.3 模型生成（Model Outputs）

对每一个组合：

```
(prompt × question × model)
```

生成模型输出，并**完整保留原始产物（PDF）**，作为后续评测、复核与归因的一级证据。

本项目明确区分：
- **模型输出失败**（实验现象，应被计入分析）
- **评测产物无效**（数据质量问题，应被剔除以保证统计可复现）

---

### 6.4 评审与打分（Judging & Scoring）

评测阶段采用多层次判定机制：

- **主方法：跨模型互评**  
  由模型 A 对模型 B 的输出进行评分，用于降低单一模型偏置。

- **辅助方法：模型自评**  
  作为 sanity check 与上界参考，不作为最终结论来源。

评测依据统一的协议与 rubric：
- `03_评测规则/EVAL_PROTOCOL.md`
- `03_评测规则/JUDGE_PROMPT.md`

---

### 6.5 汇总与归因（Aggregation & Attribution）

所有评测结果通过脚本自动汇总为 CSV 表格，包括：

- 总体表现（`summary.csv`）
- 主方法统计（`main_method_*.csv`）
- 辅助方法统计（`supporting_method_*.csv`）
- 评委一致性分析（`*_inter_judge_agreement.csv`）

分析遵循从**汇总现象 → 分组对比 → 样例回溯**的路径，所有结论均可追溯至具体 PDF 与 judge JSON。

---

## 7. 指标与判据（Rubric Overview）

### 7.1 硬性合规（Hard Compliance）

用于判定输出是否满足**最低可评测条件**：

- 是否严格遵循指定输出结构（章节/字段齐全）
- 是否出现禁止内容（额外引言、闲聊、越界输出）
- 是否满足可验证约束（长度、关键词、列表结构等）

未通过硬性合规的评测产物将被标记为 **invalid**，不进入统计汇总。

---

### 7.2 行为维度评分（Behavioral Scores）

在通过硬性合规的前提下，对模型行为进行多维评分，包括：

- 相关性（Relevance）
- 完整性（Completeness）
- 结构稳定性（Structure Integrity）
- 约束满足度（Constraint Satisfaction）
- 漂移控制情况（Drift / Failure Indicators）

具体维度定义与打分标准详见：
`03_评测规则/02_行为评分维度说明.md`。

---

### 7.3 失败类型（Failure Taxonomy）

在评分之外，额外标注失败类型，用于归因与设计改进：

- 格式崩坏 / 字段缺失
- 语义漂移 / 答非所问
- 冲突指令处理失败（优先级错误）
- 表面合规但关键约束漏掉（silent failures）

---

## 8. 如何阅读实验结果（How to Read the Results）

建议按以下顺序浏览 `04_实验结果/` 目录：

1. **总体现象**：`summary.csv`
2. **方法级对比**：`main_method_*.csv` / `supporting_method_*.csv`
3. **一致性检查**：`*_inter_judge_agreement.csv`
4. **证据回溯**：对应 PDF 原始输出与 judge JSON

该顺序可帮助读者从宏观趋势逐步定位到具体失败样例。

---

## 9. 相关工作与研究位置（Positioning & Related Work）

本项目关注的不是单次跑分，而是**提示词工程场景下的稳定性评测**，与以下方向形成互补关系：

- 学术界：可复现评测、可验证指令、结构化输出稳定性
- 工业界：LLM Eval 工程化、Prompt Injection / Prompt Drift 风险治理

外部研究仅用于帮助定位本项目的研究位置，不替代本仓库中的实验数据与结论。

---

## 10. 局限性（Limitations）

- 题集规模有限：当前用于验证 Prompt Drift 的可观测性，而非穷尽所有任务类型
- 模型与采样覆盖有限：不同模型版本与解码参数可能改变现象边界
- 自动评测的边界：部分语义层面的细微差异仍需人工复核

---

## 11. 如何引用（Citation）

如在报告、复现或二次研究中使用本项目，建议同时引用：

- 本仓库（Git commit hash 或 release tag）
- 评测协议：`03_评测规则/EVAL_PROTOCOL.md`
- 评委提示词：`03_评测规则/JUDGE_PROMPT.md`
- 提示词清单：`02_提示词版本/PROMPT_MANIFEST.md`
