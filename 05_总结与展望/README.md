# 05 总结与展望（Conclusion & Outlook）

> 本节总结 Prompt Drift Lab v2 的核心发现与方法学贡献，并结合 2025 年“AI 审稿链路被隐藏提示注入操控”的现实事件与最新安全讨论，提出 Prompt Drift Lab v3 的研究升级方向：从“良性漂移观测”走向“对抗性漂移评测与防御”。

---

## 5.1 本项目的核心贡献（v2）

### 贡献 1：将“提示词微扰 → 行为失稳”工程化为可复现实验流程
Prompt Drift Lab 以结构化输出任务为载体，将“提示词措辞/格式的微小变化”显式化为可控扰动变量，并通过固定题集、版本化提示词、统一评分 rubric 与批量运行产物（PDF + JSON + CSV）将现象转化为可复验数据。

### 贡献 2：跨模型互评（cross-model evaluation）作为主评测范式
v2 使用“模型 A 生成 → 模型 B/C 做评委”的互评机制作为主方法，并以自评作为辅助方法对照，从方法论上缓解单一评委偏差与自我强化偏差，为后续更大规模评测提供可扩展框架。

### 贡献 3：把“格式崩坏/语义漂移”拆成可操作的五维评分面
rubric 将失败模式分解为：结构合规、快照约束、可行动性、完整性、漂移/失败模式等维度，使得“漂移”不再只是主观印象，而能以维度化方式统计对比，并支持后续归因。

---

## 5.2 关键发现（v2）

### 发现 1：Prompt Drift 更接近“门控式失效”，而非线性退化
在隐式触发条件下，系统性出现“结构维度先失败、其余维度随之坍塌”的链式现象，提示漂移呈现出明显的阈值/门控特征：一旦模型对任务的“结构约束”识别失败，后续内容质量很难通过“更努力生成”补救。

### 发现 2：提示词版本的关键风险不是“更长”，而是“约束弱化与语义冲突”
对比 baseline/long 与 weak/conflict 的结果趋势显示：长度本身并非主要风险源；相反，约束表达变弱、指令之间存在张力/冲突时，更容易诱发结构性失效与语义漂移。

### 发现 3：自评与互评存在系统偏差，自评会“低估漂移、忽略违规”
辅助方法揭示：模型在自评时更可能忽略格式偏离与隐性违规，导致对自身鲁棒性的估计偏乐观。这说明仅依赖 self-evaluation 难以刻画真实“遵循鲁棒性边界”。

---

## 5.3 局限与威胁（v2 的边界）

1) **任务覆盖面有限**：当前题集规模小、任务类型集中在结构化输出，尚不足以代表更广泛的现实工作流（RAG/Agent/审稿辅助等）。  
2) **输入通道较单一**：v2 主要在“提示词文本扰动”层面建模，尚未系统纳入“文件解析差异、渲染差异、检索注入”等现实链路。  
3) **评分仍依赖模型评委**：虽然互评缓解了单点评委，但仍需引入更强的确定性验证器（结构校验、关键词约束、引用一致性、仲裁机制）来提高可解释性与可审计性。

---

## 5.4 展望：Prompt Drift Lab v3 路线图（可执行升级）

v3 的目标：建立一个“**漂移—注入统一框架**”下的基准与防御评测套件，使本项目从“现象观测”升级为“可测量、可对抗、可防御”的研究平台。

### 方向 1：加入 The Sanitizer —— 面向文档输入的“解析-渲染差分净化”
新增一条实验链路：同一 PDF 同时做两种提取
- Stream 提取（常规 PDF-to-text）
- Vision/OCR 提取（基于最终渲染图像）
对两路文本做差分，检测“仅机器可见”的高风险片段；必要时强制使用 OCR 结果作为 LLM 输入，从源头削弱间接注入。

### 方向 2：指标体系升级——从“总分”走向“遵循分解 + 注入敏感度”
建议引入两类指标：
- **遵循分解类**：将结构/字段/约束拆成可验证条件，计算分解需求遵循率（DRFR）  
- **注入鲁棒类**：定义指令辨识率（Instruction Discrimination Rate, IDR）、攻击成功率（ASR/Flip Rate）、仲裁触发率等  
这样可以把“漂移”与“注入”都映射到统一、可量化的空间里。

### 方向 3：任务集扩展——把“AI 审稿链路”纳入 benchmark
新增任务族（建议至少 6 类）：
1) 结构化输出（延续 v2，作为 drift 基准）
2) 文档摘要/评审草稿生成（模拟审稿辅助）
3) RAG 检索摘要（引入外部文本通道）
4) PDF 隐形注入对抗（white text / tiny font / overlay / unicode trick）
5) 角色/优先级冲突（system vs user vs document instructions）
6) 防御评测（净化前后对比、拒绝注入、输出一致性）

### 方向 4：评测协议升级——引入“确定性验证 + 仲裁”
- 输出先过 deterministic validator（JSON schema/字段完整性/结构匹配）
- 再做跨模型互评（多评委）
- 若评委分歧集中在结构失效边界样本，触发仲裁（第三评委或规则裁决）
最终形成可审计、可复核的评测流水线。

---

## 5.5 你接下来最小可落地动作（建议按顺序）

- [ ] 将 v2 的结果目录固定为“可发布版本”（锁定输入、脚本、输出 CSV 的哈希或 tag）
- [ ] 在 `tools/` 下建立 `sanitizer/`，实现 PDF 差分提取（stream vs OCR）原型
- [ ] 在 `benchmarks/` 下新增 `aprb/`（Adversarial Peer Review Benchmark）最小子集（先 20 篇/20 个样例）
- [ ] 在 `metrics/` 中加入 DRFR/IDR/ASR 的计算脚本与说明
- [ ] 将评测协议升级为“validator → multi-judge → arbitration”的流水线，并产出 `protocol_v3.md`
- [ ] 形成一页式“现实风险动机”材料：用 2025 隐形提示事件解释为什么 Prompt Drift 研究不止是工程技巧
- [ ] 写成 workshop-ready 的 2–3 条“最小可发表贡献点”（方法学 + 基准 + 防御）

---

## 参考链接
- Hidden Prompts in Manuscripts Exploit AI-Assisted Peer Review (arXiv:2507.06185): https://arxiv.org/abs/2507.06185
- OWASP GenAI Security Project — LLM01 Prompt Injection: https://genai.owasp.org/llmrisk/llm01-prompt-injection/
- UK NCSC — Prompt injection is not SQL injection (Dec 2025): https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection
- ICML 2025 Peer Review FAQ — Generative AI policy: https://icml.cc/Conferences/2025/PeerReviewFAQ
- ICML 2025 Reviewer Instructions — 禁止评审用 LLM: https://icml.cc/Conferences/2025/ReviewerInstructions
- InFoBench (arXiv:2401.03601) — DRFR 指标: https://arxiv.org/abs/2401.03601
- BIPIA (Microsoft) — indirect prompt injection benchmark: https://github.com/microsoft/BIPIA
