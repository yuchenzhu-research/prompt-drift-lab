# Prompt Drift Lab  
**大语言模型结构化提示词稳定性评测与归因实验**  
*Prompt Drift Lab: A Reproducible Evaluation Framework for Instruction-Following Stability in LLMs*

> 中文为主；模型/框架/关键术语保留英文，以便对齐学界与工业界阅读习惯。  
> 本仓库面向两类读者：**科研评审/导师**（可复现与归因严谨）与**工业 Mentor/用人方**（可落地的评测与迭代闭环）。

---

## 1. 研究动机（Why this exists）

在真实应用中，LLM 的输出常会因**提示词格式、措辞、长度、冲突约束**等细微变化而出现：
- 指令遵循率下降（instruction following drop）
- 结构/格式崩坏（format break）
- 语义漂移或答非所问（semantic drift / off-topic）
- “看似听话但关键约束漏掉”的隐性失败（silent constraint violation）

我们把这类“对提示词微扰高度敏感，导致行为退化”的现象统称为 **Prompt Drift**，并将其工程化为：  
> **可复现的 Prompt 设计 → 评测 → 归因 → 迭代**闭环。

这一思路与学界/工业界关于“系统化评测（evals）与可复现基准”的方向一致：  
- OpenAI 强调用 evals 在模型升级/对比中持续验证行为与风格约束。 
- Stanford HELM 强调“透明、可复现”的综合评测框架。 
- IFEval 以“可验证指令（verifiable instructions）”为核心，强调简单、易复现的指令遵循评测。  
- lm-evaluation-harness 提供统一框架在多任务上评测生成式模型。 
---

## 2. 核心贡献（Contributions）

### 学术侧（可写入 workshop/实验报告）
1) **Prompt Drift 的可操作定义与测试协议**：将“微小提示词变化→行为退化”转化为可观测指标与判据。  
2) **多维度 Rubric**：将失败拆为“硬性合规/结构化输出/语义一致性/约束满足”等维度，避免只做主观打分。  
3) **跨模型对照**：在不同模型上复用同一题集与评测协议，观察鲁棒性差异并归因（而非单模型结论）。

### 工业侧（可直接对齐 Prompt Engineering 岗位）
1) **提示词版本管理（Prompt Manifest）**：沉淀“优质案例/失败案例/改进策略”，可扩展为团队 Prompt 知识库。  
2) **评测与迭代闭环**：对比不同 Prompt 方案，记录失败类型并驱动迭代。  
3) **可复用评测资产**：题集、协议、评审提示词、打分脚本与汇总表，便于在业务场景中做 regression。

---

## 3. 研究问题（Research Questions）

- **RQ1：Prompt Drift 的主要表现形态是什么？**（合规失败、结构崩坏、语义漂移、隐性漏约束等）
- **RQ2：哪些提示词微扰最容易触发退化？**（长度、冲突指令、弱化约束、格式要求等）
- **RQ3：不同模型对同一提示词微扰的敏感性是否一致？**（cross-model robustness）
- **RQ4：失败能否被系统归因到“可修复的提示词设计缺陷”？**（可执行的改进建议）

---

## 4. 方法概览（Method Overview）

本项目遵循“实验协议化”的评测思路（protocol-driven eval）：

1) **提示词版本（Prompt Variants）**  
   - baseline / structured / conflict / long / weak 等版本，用于构造“微扰空间”（prompt perturbation space）。  
2) **固定题集（Eval Set）**  
   - 使用固定题集确保可对照；题集可扩展为多领域、多难度分层。  
3) **模型生成（Model Outputs）**  
   - 对每个（prompt × question × model）生成输出，保留原始产物。  
4) **评审与打分（Judging & Scoring）**  
   - 主方法：跨模型互评（model A judge model B）  
   - 辅助方法：模型自评（sanity check / 上界参考）  
   - Rubric：硬性合规判定 + 行为维度评分 + 失败类型标注  
5) **汇总与归因（Aggregation & Attribution）**  
   - 通过脚本生成统计表；从失败案例抽样做“可证据链”的归因分析。

> 说明：本项目借鉴“可验证指令/结构化约束”的评测思想：对能自动或半自动验证的约束优先结构化。

---

## 5. 仓库结构（Repository Structure）

> 本仓库采用“**科研论文 → 工程化目录**”的组织方式，
> 将论文中的 *方法 / 实验设计 / 评测 / 结果 / 讨论* 映射为清晰、可复现的目录结构。

```text
├── 01_实验设计/
│   ├── README.md
│   ├── 实验设计_五步法.md
│   ├── 实验协议_v2.yaml
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
│   └── PROMPT_MANIFEST_v2.md
│
├── 03_评测规则/
│   ├── 00_评测协议.md
│   ├── 01_硬性合规判定规则.md
│   ├── 02_行为表现评分维度.md
│   ├── EVAL_PROTOCOL_v2.md
│   ├── JUDGE_PROMPT_v2.md
│   └── compute_scores_v2.py
│
├── 04_实验结果/
│   ├── 01_模型原始输出/
│   │   ├── anthropic_claude-*
│   │   ├── google_gemini-*
│   │   └── openai_gpt-*
│   │
│   ├── 02_跨模型评测结果/
│   │   ├── 有效评测/
│   │   │   ├── 主方法_跨模型互评/
│   │   │   ├── 辅助方法_模型自评/
│   │   │   └── 统计汇总表/
│   │   │
│   │   └── 无效评测/
│   │       ├── 主方法_跨模型互评/
│   │       └── 辅助方法_模型自评/
│   │
│   └── 03_实验结果分析.md
│
├── 05_总结与展望/
│   └── README.md
│
└── README.md
```
## 6. 快速开始（Reproducibility Quickstart）

### 6.1 最小复现路径（建议第一次只走这条）
1) 阅读 `01_实验设计/README.md`，理解题集与协议。  
2) 查看 `02_提示词版本/PROMPT_MANIFEST_v2.md`，明确本次比较的 Prompt 版本。  
3) 打开 `03_评测规则/EVAL_PROTOCOL_v2.md` 与 `JUDGE_PROMPT_v2.md`，确认评审标准与输出格式。  
4) 直接从 `04_实验结果/01_模型原始输出/` 抽取样本，手工对照 Rubric，理解失败模式。  
5) 使用 `03_评测规则/compute_scores_v2.py` 生成统计汇总表（见脚本说明）。

> 由于不同人本地路径/环境不同，脚本的具体入参以 `python compute_scores_v2.py -h` 的帮助信息为准（保证可复现而不“写死命令”）。

### 6.2 推荐实验纪律（对齐顶会/工业评测规范）
- 固定：题集版本、Prompt 版本、模型版本、采样参数（temperature/seed/次数）  
- 记录：运行日志（run log）、原始输出、评审输出、汇总表  
- 任何“修改提示词/协议”的变更都应记录到 manifest 或 git tag

这种“把评测当作持续工程能力”的思路与工业界的 evals 实践一致。 

---

## 7. 评测指标与判据（Rubric Overview）

本项目将“好不好”拆成可复现的维度（示例，详见 `03_评测规则/`）：

### 7.1 硬性合规（Hard Compliance）
- 是否遵循指定输出结构（Markdown/JSON/章节/字段齐全）
- 是否出现禁止内容（额外闲聊、越界输出、缺失关键字段）
- 是否满足可验证约束（长度、关键词、列表结构等）

> 设计理念与 IFEval 的“可验证指令”相近：优先把指令写成可判定的约束。

### 7.2 行为表现（Behavioral Scores）
- 相关性（Relevance）
- 完整性（Completeness）
- 逻辑性（Coherence）
- 结构稳定性（Structure Integrity）
- 约束满足度（Constraint Satisfaction）

### 7.3 失败类型（Failure Taxonomy）
- 格式崩坏 / 字段缺失
- 语义漂移 / 只答一部分
- 冲突指令处理失败（优先级错误）
- “表面合规但关键约束漏掉”（silent failures）

---

## 8. 结果与解读（Results & Analysis）

- 原始输出：`04_实验结果/01_模型原始输出/`
- 跨模型评测：`04_实验结果/02_跨模型评测结果/有效评测/`
- 失败与无效评测：`04_实验结果/02_跨模型评测结果/无效评测/`
- 论文式分析：`04_实验结果/03_实验结果分析.md`

> 本仓库强调：**失败产物不是“丢弃”，而是作为证据链用于归因与改进**（这点对科研与工业都更有价值）。

---

## 9. 与相关工作的位置关系（Positioning / Related Work）

你可以将本项目理解为：  
- 借鉴 HELM 对“可复现、透明评测”的理念，但聚焦在**提示词微扰导致的稳定性问题**。 
- 借鉴 OpenAI Evals 的“把评测当作持续工程”的实践方式，将 Rubric/协议/数据资产化。  
- 与 IFEval 的“可验证指令”思想一致，但更强调**结构化输出 + 失败归因 + 提示词版本对照**。 
- 与 lm-evaluation-harness 的“统一评测框架”目标一致，但本项目更偏**提示词工程场景的行为评测与鲁棒性实验**。 
- （可选扩展）近期也有面向行为评测的 agentic 框架发布趋势，可作为未来扩展方向之一。

---

## 10. 工业场景能力映射（For Prompt Engineering Roles）

如果你来自业务/产品/算法团队，可把本项目直接映射到以下任务：

- **Prompt 设计与迭代**：`02_提示词版本/`（可复用模板 + 版本化对照）
- **效果评估与优化**：`03_评测规则/` + `compute_scores_v2.py`（指标/协议/统计）
- **提示词知识库**：`PROMPT_MANIFEST_v2.md`（优质/失败/改进策略沉淀）
- **数据与标注规则**：题集与 Rubric 可扩展为标注规范（human-in-the-loop）
- **跨团队协作**：同一协议可迁移到不同模型/不同业务任务，形成统一沟通语言

---

## 11. 局限性（Limitations）

- 题集规模有限：目前用于验证“提示词微扰→行为退化”的可观测性；后续需扩展到更多任务类型与难度分层。  
- 模型与采样的覆盖有限：不同模型版本/解码参数可能改变结论，需要更系统的控制变量与重复试验。  
- 自动化判定的边界：部分“语义正确但形式不合规 / 形式合规但语义偏离”的情况仍需人工审阅或更强的 verifier。

---

## 12. 如何引用（Citation）

若你将本项目用于报告/复现/二次开发，建议引用：
- 本仓库（Git commit hash / tag）
- 评测协议版本：`EVAL_PROTOCOL_v2.md`
- 提示词版本清单：`PROMPT_MANIFEST_v2.md`
- （如写论文）并在 Related Work 中对 HELM / OpenAI Evals / IFEval 等做位置说明。 




