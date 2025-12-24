# Prompt Drift Lab
**大语言模型结构化提示词稳定性评测与归因实验**  
*Prompt Drift Lab: A Reproducible Evaluation Framework for Instruction-Following Stability in LLMs*

> 以中文为主，关键模型名、框架名与技术术语保留英文写法，以对齐学界与工业界通行表达。  
> 目标读者包括：  
> - **科研评审 / 导师**：关注可复现性、证据链完整性与归因逻辑；  
> - **工业 Mentor / 用人方**：关注可落地的 eval 闭环、提示词版本管理与失败模式沉淀。

---

## 1. 研究动机（Why this exists）

在真实应用中，大语言模型（LLMs）的输出往往会因**提示词格式、措辞、长度或约束表达的细微变化**而出现显著行为差异，例如：

- 指令遵循率下降（instruction following drop）
- 结构或格式崩坏（format break / schema violation）
- 语义漂移或答非所问（semantic drift / off-topic）
- 表面合规但关键约束被忽略的隐性失败（silent constraint violation）

本项目将上述“因提示词微扰而触发的稳定性退化现象”统一抽象为 **Prompt Drift**，并将其工程化为一个**可复现、可对照、可归因**的实验闭环：

> **Prompt 设计 → 批量运行 → 统一评分 → 汇总对比 → 失败归因 → 迭代沉淀**

---

## 2. 仓库包含内容（What’s inside）

本仓库围绕 Prompt Drift 的完整评测流程，包含以下核心组成：

- 固定题集与实验设定：`01_experiment_design/`
- 提示词版本与差分意图说明：`02_prompt_variants/`
- 评测协议与 judge 提示词：`03_evaluation/`
- 结果产物与证据链入口：`04_results/`
- 总结、局限与外推边界：`05_summary_and_outlook/`
- 方法论补充与 A/B 对照依据：`06_methodological_addenda_and_controls/`
- Deep Research 搜索记录与参考资料：`07_deep_research/`

---

## 3. 研究问题（Research Questions）

本项目围绕以下问题展开：

- **RQ1：Prompt Drift 的主要表现形态是什么？**  
  （指令失效、结构崩坏、语义漂移、隐性漏约束等）

- **RQ2：哪些提示词微扰最容易触发行为退化？**  
  （长度变化、冲突指令、弱化约束、结构要求等）

- **RQ3：不同模型对同一微扰的敏感性是否一致？**  
  （cross-model robustness）

- **RQ4：失败能否被系统性归因到“可修复的提示词设计缺陷”？**  
  （actionable prompt fixes）

---

## 4. 推荐阅读路径（30 秒定位入口）

### 4.1 从哪里开始阅读

建议按以下顺序阅读，以最快建立“协议 → 版本 → 评分 → 结果 → 证据链”的整体认知：

1. `01_experiment_design/README.md`：题集范围、实验假设、协议与字段约束
2. `02_prompt_variants/PROMPT_MANIFEST.md`：Prompt A/B 及其变体的最小差分设计
3. `03_evaluation/EVAL_PROTOCOL.md` 与 `JUDGE_PROMPT.md`：评分维度、合规判定与输出结构
4. `04_results/README.md`：结果索引（summary / main_method / supporting_method / valid & invalid）
5. `04_results/03_results_analysis_ZH.md`：对照结论与失败模式归因（可回溯到 PDF 与 judge JSON）
6. `06_methodological_addenda_and_controls/README_ZH.md`：方法论选择与 A/B 对照依据
7. `05_summary_and_outlook/README_ZH.md`：局限、外推边界与后续扩展路线

> 核心原则：任何结论都应能够回溯到 `04_results/` 中的原始模型输出与逐样本评测记录。

### 4.2 实验纪律（Reproducibility Contract）

- 固定：题集版本、Prompt 版本、模型版本与采样参数
- 落盘：config / raw outputs / judged scores / summary
- 任何协议或提示词变更，均需同步更新对应的 manifest 与 README

---

## 5. 方法概览（Method Overview）

本项目采用 **protocol-driven evaluation**，将“提示词微小变化导致的行为退化”转化为可对照、可复现、可归因的评测流程。

### 5.1 提示词版本（Prompt Variants）

基于“最小差分（minimal diffs）”构造对照组：

- **Prompt A (baseline)**：最小可用、弱结构约束的自然语言提示词
- **Prompt B (structured)**：显式结构化约束（字段、顺序、禁止项）
- **long**：增加上下文与冗余说明
- **weak**：系统性弱化约束表达
- **conflict**：引入潜在冲突或指令张力

差分动机与版本说明见：`02_prompt_variants/PROMPT_MANIFEST.md`。

### 5.2 固定题集（Eval Set）

固定题集用于确保不同 Prompt 与不同模型之间的可对照性：`01_experiment_design/questions.jsonl`。  
题集规模在当前阶段刻意保持克制，以优先验证 Prompt Drift 的**可观测性与可归因性**。

### 5.3 生成与留存（Outputs as Evidence）

对每个 `(prompt × question × model)` 组合：

- 保留原始输出（PDF）作为一级证据
- 明确区分“模型输出失败（实验现象）”与“评测产物无效（数据质量）”

### 5.4 评审与打分（Judging & Scoring）

评测统一遵循：

- `03_evaluation/EVAL_PROTOCOL.md`
- `03_evaluation/JUDGE_PROMPT.md`

主方法与辅助方法的定义及统计口径见 `04_results/README.md`。

### 5.5 汇总与归因（Aggregation & Attribution）

通过汇总表与分组统计，将逐样本评分映射为可对照结果，并通过：

> 汇总现象 → 分组对比 → 样例回溯（PDF + judge JSON）

确保每条结论具备可复核的证据链。

---

## 6. 指标与失败类型（Rubric & Failure Taxonomy）

- **硬性合规（Hard Compliance）**：结构、字段与禁止项要求
- **行为维度评分（Behavioral Scores）**：相关性、完整性、结构稳定性、约束满足度
- **失败类型（Failure Taxonomy）**：格式错误、指令偏离、语义漂移、隐性漏约束等

维度定义与评分标准见：`03_evaluation/`。

---

## 7. A/B 选择的对照依据（Why B over A）

关于 Prompt A/B 的差异、三段式模板对照评测，以及选择 B 作为主实验 anchor 的方法论依据，统一收口于：

- `06_methodological_addenda_and_controls/A_B_comparative_rationale_ZH.md`
- `06_methodological_addenda_and_controls/Prompt_A_B_three_step_template_comparative_evaluation.pdf`

该部分用于回答“为何采用 B 作为主实验提示词版本”的证据链问题，并与 `04_results/` 的统计口径保持一致。

---

## 8. 局限性（Limitations）

- 题集规模有限，外推需谨慎；
- 模型版本、解码参数与 judge 选择可能改变现象边界；
- 细粒度语义差异仍需抽样人工复核（以 PDF 与 judge JSON 为证据）。

---

## 9. 如何引用（Citation）

在复现、报告或二次研究中，建议同时引用：

- 本仓库（Git commit hash 或 release tag）
- 评测协议：`03_evaluation/EVAL_PROTOCOL.md`
- judge 提示词：`03_evaluation/JUDGE_PROMPT.md`
- 提示词清单：`02_prompt_variants/PROMPT_MANIFEST.md`
- A/B 对照依据：`06_methodological_addenda_and_controls/A_B_comparative_rationale_ZH.md`

