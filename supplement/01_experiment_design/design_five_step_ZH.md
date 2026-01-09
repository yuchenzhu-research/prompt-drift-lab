# 实验设计五步法（Workflow）

本文件回答一个问题：**Prompt Drift Lab 的实验到底怎么做，才能可复现、可迭代、可统计？**

- 我研究的是：提示词/措辞/约束强弱发生微小变化时，LLM 输出是否出现 **遵循率下降、结构崩坏、语义漂移**。
- 我评测的是：**是否按要求做事**（instruction following & structured output stability），而不是内容对错。

> 本文件是“方法论导读”，不承载硬参数与真值源。  
> 具体参数与实验条件以 `实验协议_protocol.yaml` 为准。

---

## Step 0：先看清楚 5 个核心产物（你最终要交付什么）

完成一次“可复现实验批次（Eval Bundle）”，你至少会得到：

1) **原始输出**（PDF）：模型真实输出的证据  
2) **Eval Bundle JSON**：每个文件的 rubric 分数 + invalid 归档  
3) **汇总表**（可选）：按维度统计均值/分布/失败模式  
4) **漂移归因笔记**（可选）：为什么会崩、崩在哪里  
5) **协议记录**：当时用的模型/参数/版本（写进 protocol.yaml）

这些产物分别对应目录里的文件：
- 输出结构定义：`标准输出结构.md`
- 问题集：`问题集.jsonl`
- 实验协议真值源：`实验协议_protocol.yaml`
- 风险与边界：`威胁与局限.md`

---

## Step 1：定义“被测任务”与“输出结构”（Task Spec）

目标：让评测对象是**稳定的**，否则你根本不知道漂移来自哪里。

需要固定两件事：

### 1.1 题目（Question / Task）
- 从 `问题集.jsonl` 选择 Q1 到 Q4
- 每个 Q 代表一种结构化输出任务类型（例如三段式、严格模板、冲突约束等）

### 1.2 标准输出结构（Output Schema）
- 以 `标准输出结构.md` 为准
- 这一步要确保：你评的不是“答得好不好”，而是“结构是否遵循”

**本步检查点（通过才进入 Step 2）：**
- 题目文本稳定（不要一边跑一边改题）
- 输出结构稳定（模板字段/段落定义不变）

---

## Step 2：定义“最小扰动”的提示词版本（Prompt Variants）

目标：把“变化”控制在可解释范围内。

常用版本（示例）：
- baseline：正常版本（对照）
- long：更长、更解释、更重复约束（检验“越长越听话？”）
- weak：弱化硬约束（检验结构是否靠强指令维持）
- conflict：引入冲突或歧义（检验模型如何选择/崩坏）

同时定义触发强度：
- implicit：暗示/推荐结构
- explicit：必须/严格遵守结构（strict compliance）

**本步检查点：**
- 版本差异是“刻意且可描述”的（你能用一句话说清差在哪里）
- 不要同时改 3 个东西（否则归因会崩）

---

## Step 3：生成输出并固化证据（Run → Archive）

目标：保证“每个样本”都是可追溯证据。

### 3.1 建议命名规范
推荐统一为：
`q{QID}_{version}_{trigger}_{model}_r{rep}.pdf`

示例：
- `q3_baseline_explicit_chatgpt_r1.pdf`
- `q4_conflict_implicit_gemini_r2.pdf`

### 3.2 运行时记录（强建议）
每份输出最好能追溯到：
- generator model（具体型号/界面显示名）
- 时间（大致即可）
- 参数（temperature/top_p 等）
- prompt 版本 + trigger 类型 + QID + replicate

> 你可以把这些写进 PDF 顶部，或写进独立 run log。  
> “证据能对上协议”是 workshop 级项目的底线。

**本步检查点：**
- 输出保存为“原始证据”（不要手工改写）
- 文件名可解析（后续聚合不痛苦）

---

## Step 4：按 Rubric 评分并处理 invalid（Score → Validate）

目标：把“看起来像结果”变成“可统计数据”。

### 4.1 Rubric 评分
你会对每个 PDF 给出一个维度分数（0/1/2 或你定义的刻度），例如：
- A_structure：结构是否保持
- B_snapshot_constraint：事实快照是否“只陈述不分析”
- C_actionability：搜索指令/动作是否可执行
- D_completeness：覆盖是否完整
- E_drift_failure：是否发生明显漂移/越界/改任务

> Rubric 的细则写在 `03_评测规则/`，这里不重复。

### 4.2 invalid 的规则（必须统一）
invalid 只用于“不可评分样本”，例如：
- 拒答 / 变闲聊 / 完全改任务
- 严重截断到无法判断结构
- 输出不包含任何可评分内容

**注意：**
- “做得很差” ≠ invalid  
- 只要能评分，就打低分

**本步检查点：**
- 每个文件要么进入 `per_file_scores`，要么进入 `invalid_files`
- invalid 必须写明 reason

---

## Step 5：汇总与漂移归因（Aggregate → Diagnose → Iterate）

目标：把分数变成结论，把结论变成下一轮实验。

### 5.1 最小统计（建议）
至少做三类聚合：
- 按 prompt version（baseline/long/weak/conflict）聚合
- 按 trigger type（implicit/explicit）聚合
- 按 generator model（chatgpt/gemini/claude）聚合

输出可以是：
- `results/summary.csv`（或你现有的总表）
- 以及一段简短的 observations（写进 notes）

### 5.2 漂移归因（建议用 failure modes）
把“崩坏”归类成可复用的 failure modes，例如：
- format_drift（结构丢失）
- role_confusion（角色混乱、开始聊天）
- constraint_violation（违反禁止项）
- task_rewrite（改写任务目标）
- verbosity_overflow（解释过多导致模板破坏）

### 5.3 迭代规则（避免越改越乱）
- 一次只改一个变量（版本 or 触发 or 问题）
- 新版本必须写清楚“它在检验什么假设”
- 任何修改要回写到 `实验协议_protocol.yaml`（保持真值源一致）

**本步检查点：**
- 你能回答：这轮实验的“主结论”是什么？
- 你能回答：下一轮实验要验证哪个“因果假设”？
