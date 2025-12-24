# Prompt Drift Lab
**大语言模型结构化提示词稳定性评测与归因实验**  
*Prompt Drift Lab: A Reproducible Evaluation Framework for Instruction-Following Stability in LLMs*

> 中文为主；模型/框架/关键术语保留英文，便于对齐学界与工业界阅读习惯。  
> 面向读者：
> - **科研评审/导师**：关注可复现、证据链、归因逻辑
> - **工业 Mentor/用人方**：关注可落地的 eval 闭环、提示词版本管理、失败模式沉淀

---

## 1. 研究动机（Why this exists）

真实应用中，LLM 的输出会因**提示词格式、措辞、长度、冲突约束**等微小变化而出现：
- 指令遵循率下降（instruction following drop）
- 结构/格式崩坏（format break / schema violation）
- 语义漂移或答非所问（semantic drift / off-topic）
- “表面合规但关键约束漏掉”的隐性失败（silent constraint violation）

本项目将这类“对提示词微扰高度敏感、导致行为退化”的现象抽象为 **Prompt Drift**，并将其工程化为可复现闭环：

> **Prompt 设计 → 批量运行 → 统一评分 → 汇总对比 → 失败归因 → 迭代沉淀**

---

## 2. 仓库包含内容（What’s inside）

- 固定题集：`01_实验设计/问题集.jsonl`
- 实验协议与输出约束：`01_实验设计/实验协议.yaml` + `01_实验设计/标准输出结构.md`
- 提示词版本与差分意图：`02_提示词版本/*.txt` + `02_提示词版本/PROMPT_MANIFEST.md`
- 评测协议与评委提示词：`03_评测规则/EVAL_PROTOCOL.md` + `03_评测规则/JUDGE_PROMPT.md`
- 结果产物与证据链入口：`04_实验结果/README.md` +（PDF 原始输出、judge JSON、汇总 CSV）
- 方法论补充与 A/B 对照依据：`06_方法论补充与对照依据/`
- Deep Research 搜索汇总与参考资料：`07_DeepResearch_资料汇总/`

---

## 3. 研究问题（Research Questions）

- **RQ1：Prompt Drift 的主要表现形态是什么？**（合规失败、结构崩坏、语义漂移、漏约束等）
- **RQ2：哪些提示词微扰最容易触发退化？**（长度、冲突指令、弱化约束、格式要求等）
- **RQ3：不同模型对同一微扰的敏感性是否一致？**（cross-model robustness）
- **RQ4：失败能否被系统归因到“可修复的提示词设计缺陷”？**（actionable prompt fixes）

---

## 4. 推荐阅读路径（30 秒定位入口）

### 4.1 读者从哪里开始

建议按以下顺序阅读，以最快建立“协议 → 版本 → 评分 → 结果 → 证据链”的闭环认知：

1) `01_实验设计/README.md`：题集范围、实验假设、协议与字段约束（含 `实验协议.yaml`）  
2) `02_提示词版本/PROMPT_MANIFEST.md`：Prompt A/B 与变体的最小差分意图  
3) `03_评测规则/EVAL_PROTOCOL.md` + `JUDGE_PROMPT.md`：评分维度、合规判定与输出 schema  
4) `04_实验结果/README.md`：结果索引（summary / main_method / supporting_method / valid&invalid）  
5) `04_实验结果/03_实验结果分析.md`：对照结论与失败归因（可回溯到 PDF 与 judge JSON）  
6) `06_方法论补充与对照依据/README.md`：为何采用当前主方法（含 A/B 对照证据链）  
7) `05_总结与展望/README.md`：局限、外推边界与下一步扩展路线

> 核心原则：任何结论都可回溯到 `04_实验结果/01_模型原始输出/` 的原始输出与 `02_跨模型评测结果/` 的逐样本判定记录。

### 4.2 实验纪律（Reproducibility Contract）

- 固定：题集版本、Prompt 版本、模型版本、采样参数（temperature/seed/次数）
- 落盘：config / raw outputs / judged scores / summary（均可在 `04_实验结果/` 追溯）
- 任何协议或提示词修改：同步更新 `PROMPT_MANIFEST.md` 与对应 README（保持术语一致）

---

## 5. 仓库结构（Repository Structure）

```text
├── 01_实验设计/
│   ├── README.md
│   ├── eval_record.json
│   ├── 问题集.jsonl
│   ├── 实验协议.yaml
│   ├── 标准输出结构.md
│   ├── 实验设计_五步法.md
│   ├── 术语对齐.md
│   └── 威胁与局限.md
│
├── 02_提示词版本/
│   ├── 00_baseline_prompt_A.txt
│   ├── 01_structured_prompt_B.txt
│   ├── 02_conflict_prompt.txt
│   ├── 03_long_prompt.txt
│   ├── 04_weak_prompt.txt
│   ├── PROMPT_MANIFEST.md
│   └── README.md
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
│   ├── 01_模型原始输出/          # 原始输出（一级证据）
│   ├── 02_跨模型评测结果/        # judge 记录与统计产物
│   ├── 03_实验结果分析.md
│   └── README.md                 # 结果索引入口（从这里开始看数据）
│
├── 05_总结与展望/
│   └── README.md
│
├── 06_方法论补充与对照依据/
│   ├── A_B_对照依据.md
│   ├── Prompt A_B 三段式转译器对照评测报告.pdf
│   └── README.md
│
├── 07_DeepResearch_资料汇总/
│   ├── *.pdf
│   └── README.md
│
└── README.md
```

---

## 6. 方法概览（Method Overview）

本项目采用 **protocol-driven evaluation**：将“提示词微小变化导致的行为退化”转化为可对照、可复现、可归因的评测流程。

### 6.1 提示词版本（Prompt Variants）

以“最小差分（minimal diffs）”构造对照组：
- **baseline / A**：最小可用提示词（对照基线）
- **structured / B**：显式结构化约束（字段/顺序/禁止额外文本）
- **long**：增加上下文与冗余说明（测试长度对遵循率的影响）
- **weak**：弱化约束（测试是否回退到自然对话）
- **conflict**：引入张力/潜在冲突指令（测试优先级处理与对齐策略）

差分动机与版本说明见：`02_提示词版本/PROMPT_MANIFEST.md`。

### 6.2 固定题集（Eval Set）

固定题集用于确保不同 Prompt / 不同模型之间可对照：`01_实验设计/问题集.jsonl`。  
题集规模在当前阶段刻意保持克制，以优先验证 Prompt Drift 的可观测性与可归因性（而非穷尽任务空间）。

### 6.3 生成与留存（Outputs as Evidence）

对每个组合 `(prompt × question × model)`：
- 保留原始输出（PDF）作为一级证据：`04_实验结果/01_模型原始输出/`
- 区分“模型输出失败（实验现象）”与“评测产物无效（数据质量）”，以保证统计可复现

### 6.4 评审与打分（Judging & Scoring）

采用统一协议与 rubric：
- `03_评测规则/EVAL_PROTOCOL.md`
- `03_评测规则/JUDGE_PROMPT.md`

主方法与辅助方法的定义、统计口径及一致性检查均在 `04_实验结果/README.md` 给出索引与解释。

### 6.5 汇总与归因（Aggregation & Attribution）

通过脚本将逐样本评分汇总为表格（summary / main_method / supporting_method / valid&invalid 等），并遵循：

> 汇总现象 → 分组对比 → 样例回溯（PDF + judge JSON）  
> 确保每条结论具备可复核证据链。

---

## 7. 指标与失败类型（Rubric & Failure Taxonomy）

- **硬性合规（Hard Compliance）**：字段齐全、结构正确、禁止额外文本等；不合规样本标记为 invalid  
- **行为维度评分（Behavioral Scores）**：相关性、完整性、结构稳定性、约束满足度等  
- **失败类型（Failure Taxonomy）**：schema/格式错误、指令偏离、语义漂移、隐性漏约束等

维度定义与评分档位见：`03_评测规则/02_行为评分维度说明.md`。

---

## 8. A/B 选择的对照依据（Why B over A）

关于 Prompt A/B 的差异、三段式转译器对照评测与“选择 B 的方法论依据”，统一收口于：
- `06_方法论补充与对照依据/A_B_对照依据.md`
- `06_方法论补充与对照依据/Prompt A_B 三段式转译器对照评测报告.pdf`

该部分用于回答“为何采用 B 作为主实验提示词版本”的证据链问题，并与 `04_实验结果` 的统计口径对齐。

---

## 9. 局限性（Limitations）

- 题集规模有限：用于验证 Prompt Drift 的可观测性与归因路径，外推需谨慎  
- 覆盖面有限：模型版本、解码参数、评委模型选择均可能改变现象边界  
- 自动评测边界：细粒度语义差异仍需抽样人工复核（以 PDF 与 judge JSON 为证据）

---

## 10. 如何引用（Citation）

复现、报告或二次研究中，建议同时引用：
- 本仓库（Git commit hash 或 release tag）
- 评测协议：`03_评测规则/EVAL_PROTOCOL.md`
- 评委提示词：`03_评测规则/JUDGE_PROMPT.md`
- 提示词清单：`02_提示词版本/PROMPT_MANIFEST.md`
- A/B 对照依据：`06_方法论补充与对照依据/A_B_对照依据.md`

