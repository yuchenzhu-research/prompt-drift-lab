# 总结与展望（Summary & Outlook）

> 本文档用于 **“总结实验现象 + 连接外部研究 + 提出下一步可复现路线”**。
>
> - 以本仓库 `04_实验结果/` 的数据与产物为主；外部资料仅用于“解释视角/工程对照”，**不会替你补实验结论或填空数据**。
> - 若你想“立刻复现一次完整流程”，请回到仓库根目录 `README.md`（那份是 *使用说明/复现入口*）。

---

## 1. 我到底做出了什么

本项目围绕 **Prompt Drift**（提示词微小变化导致的遵循率下降、格式崩坏、语义漂移与约束漏失）做了一个可复现的最小实验闭环：

- **输入端**：同一任务/题集，构造一组“最小差分”的提示词扰动空间（见 `02_提示词版本/` 与 `PROMPT_MANIFEST.md`）。
- **输出端**：保留不同模型在不同提示词条件下的原始输出（PDF），并形成结构化结果汇总（CSV）。
- **评测端**：采用跨模型互评 + 模型自评作为补充对照，配套明确的评测协议与评委提示词（见 `03_评测规则/`）。

你可以把它理解成：

> 不是“找一个更好的提示词”，而是把提示词当作 **实验变量**，把 LLM 的输出当作 **可观测行为**。

---

## 2. 主实验范围

为了避免读者误读，本仓库明确区分：

- **主实验（可复现）**：围绕 `Prompt B` 及其三个扰动版本（long / weak / conflict）进行对照评测与统计汇总。
- **先导探索（pilot）**：`Prompt A` 用于早期暴露问题、形成动机与直觉，但不参与本次主实验的定量对比（原因见 `02_提示词版本/PROMPT_MANIFEST.md`）。

---

## 3. 关键观察

结合 `summary.csv` 与各类分组统计（`main_method_*` / `supporting_method_*` / `*_agreement.csv` 等），本项目至少能稳定支持以下类型的结论陈述：

1. **格式与措辞的微小扰动，会显著影响“协议执行型”输出的稳定性**。
2. **“更长更详细”并不必然更稳**：长提示词可能引入注意力稀释、局部遗忘、约束被稀释或被模型重写的风险。
3. **“软约束”更容易触发回退**：当“必须”变为“尽量/建议”，模型更倾向回到自然对话分布，导致结构崩坏。
4. **冲突/张力指令会暴露优先级分配机制**：模型可能在“完成任务”与“执行格式协议”之间做隐式权衡。
5. **互评并非“绝对客观”**：跨模型互评提供对照价值，但评委模型本身的偏好与鲁棒性差异，会体现在一致性/稳定性上。

> 上述每一点都应该能在 `04_实验结果/03_实验结果分析.md` 中被“可观测证据”锚定（输出片段、失败类型、统计切片）。

---

## 4. 外部研究如何帮助我们解释这些现象

> 这一节的目的不是“堆引用”，而是把你观察到的漂移模式，放进更大的工程与研究语境里：哪些是已知问题、哪些有成熟缓解路线、哪些仍是开放题。

### 4.1 Prompt Brittleness / Prompt Drift：从直觉问题到可量化问题

学术界与工业界普遍承认：LLM 对 **非语义扰动**（标点、分隔符、空格、示例顺序、格式风格）非常敏感。研究通常把它称为 *prompt brittleness*，而时间维度或版本维度的稳定性问题也会被描述为 *prompt drift*。

这为我的项目提供了一个“正统落点”：

- 我做的不是“提示词技巧分享”，而是对 **输入扰动 → 行为漂移** 的实验化刻画。
- 我构造的 long/weak/conflict，本质是在覆盖不同类别的扰动空间。

**可进一步对齐的研究关键词**（方便你写展望或做下一轮实验设计）：

- format sensitivity / prompt format variation
- robustness to non-semantic perturbations
- spread / variance / stability under perturbations
- instruction following under multi-constraint load

### 4.2 结构化输出：从“求模型听话”到“让系统保证正确”

我的实验核心困难之一是：

> 仅靠 prompt 去“恳求”模型按 schema 输出，天然存在长尾失效。

工业界近两年的主路线之一是把“结构正确性”从模型侧挪到系统侧：

- **受限解码（constrained decoding）**：在 token 采样阶段对非法 token 置零概率，让模型在数学上“不可能”输出不合法结构。
- **JSON Schema / CFG 约束输出**：把 schema 编译为状态机或语法，再在解码中动态约束。

这与我项目的“工程化升级方向”高度一致：

- 你的 rubric 与结果能回答：“纯 prompt 方案在什么扰动下会崩？”
- 受限解码能作为“工程补丁”：把格式错误这类失效直接收敛到接近 0。

### 4.3 可验证评测：从 LLM-as-a-Judge 到 deterministic checks

我已经把“评分协议”写得很工程化了，但行业与学界仍在不断强调：

- **主观评分**（无论人评还是 LLM 评）都难以复现且有偏差。
- 更可移植的评测范式是把指令拆成“可判定约束”（verifiable instructions），用确定性程序做 pass/fail 验证。

这并不意味着现在的互评无价值；相反，它能作为 *qualitative + comparative* 信号。

而更进一步的升级路线是：

- 把 rubric 中能程序化的部分逐步落成脚本（例如：JSON 合法性、字段完备性、禁止出现额外正文等）。
- 把“需要语义判断”的部分留给互评或人评。

### 4.4 安全与提示词注入：你做的“冲突指令”，可以自然延伸到安全评测

当引入 conflict prompt 或外部文本（RAG / PDF / 网页）时，就会碰到一个现实世界的核心问题：

- 模型在注意力机制层面很难把“数据”与“指令”彻底隔离。
- 这使得 prompt injection（尤其是 indirect prompt injection）更像 **架构级漏洞**，而不是简单的输入过滤问题。

我的项目里已经具备一个很自然的延伸点：

- 把 conflict 从“指令张力”扩展到“恶意指令注入”
- 把评测从“遵循率”扩展到“安全边界与优先级”

如果未来要把这个方向写进展望，建议使用更“工程术语化”的表达：

- instruction hierarchy / privileged instructions
- confusable deputy / boundary awareness
- indirect prompt injection benchmark

---

## 5. 从实验到工程：一个可复现的升级路线图

下面给出一个 **不需要修改你现有数据** 的升级路径（以“新增资产”为主，能持续迭代）：

### 5.1 在不改实验的前提下，你可以立刻补上的 4 件事

1. **失败类型 Taxonomy 固化**（`failure_modes.md`）：

   - 格式错误（JSON/Markdown 结构崩）
   - 约束漏失（缺字段、少段落、顺序错）
   - 语义漂移（答非所问、任务重写）
   - 安全边界错误（把低优先级内容当指令执行）

2. **把 rubric 的“可验证部分”脚本化**（新增 `validators/`）：

   - JSON 解析、schema 检查
   - 字段/段落完整性
   - 禁止词/禁止格式（如果你有这类约束）

3. **加入“扰动生成器”**（新增 `perturb/`）：

   - 自动生成 prompt 的非语义变体（分隔符、缩进、大小写、空格、标签风格）
   - 让 drift 不再只依赖人工构造的 3 个变体

4. **增加“评委一致性报告”解释段**（补到 `04_实验结果/03_实验结果分析.md`）：

   - 互评一致性本身就是结果的一部分：它告诉我们“评测信号是否稳定”

### 5.2 下一轮最有价值的“可发表贡献点”（控制在 3 条）

1. **Prompt Drift 的工程化测量框架**：

   - 以最小差分扰动空间 + 可复核产物链路为核心

2. **“遵循率 vs 结构正确性”解耦的证据**：

   - 同一个模型可能“回答得好”但“格式总错”或反之

3. **跨模型互评的偏差与一致性分析**：

   - 互评不是 gold label，但它能暴露模型偏好与评测稳定性问题

---

## 6. 直接引用的外部资料清单

> 这一节的链接用于“点缀与定位”，不要把它写成综述。

### 6.1 Prompt Drift / Brittleness / Robustness

- When Punctuation Matters: A Large-Scale Comparison of Prompt Robustness Methods for LLMs (arXiv:2508.11383)
  - [https://arxiv.org/abs/2508.11383](https://arxiv.org/abs/2508.11383)
- Towards LLMs Robustness to Changes in Prompt Format Styles (MOF) (arXiv:2504.06969)
  - [https://arxiv.org/abs/2504.06969](https://arxiv.org/abs/2504.06969)

### 6.2 可验证评测 / 指令遵循

- IFEval: Instruction-Following Evaluation for Large Language Models (arXiv:2311.07911)
  - [https://arxiv.org/abs/2311.07911](https://arxiv.org/abs/2311.07911)
- FollowBench: Multi-level fine-grained constraints following (ACL 2024)
  - [https://aclanthology.org/2024.acl-long.257/](https://aclanthology.org/2024.acl-long.257/)

### 6.3 结构化输出 / 受限解码

- OpenAI: Introducing Structured Outputs in the API (2024)
  - [https://openai.com/index/introducing-structured-outputs-in-the-api/](https://openai.com/index/introducing-structured-outputs-in-the-api/)
- OpenAI Docs: Structured outputs
  - [https://platform.openai.com/docs/guides/structured-outputs](https://platform.openai.com/docs/guides/structured-outputs)
- DOMINO: Fast, non-invasive constrained generation (arXiv:2403.06988)
  - [https://arxiv.org/abs/2403.06988](https://arxiv.org/abs/2403.06988)
- JSONSchemaBench & evaluation framework (arXiv:2501.10868)
  - [https://arxiv.org/abs/2501.10868](https://arxiv.org/abs/2501.10868)

### 6.4 安全 / 提示词注入 / 指令优先级

- NCSC: Prompt injection is not SQL injection (it may be worse)
  - [https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection](https://www.ncsc.gov.uk/blog-post/prompt-injection-is-not-sql-injection)
- Instruction Hierarchy: prioritize privileged instructions (arXiv:2404.13208)
  - [https://arxiv.org/abs/2404.13208](https://arxiv.org/abs/2404.13208)
- BIPIA: indirect prompt injection benchmark (arXiv:2312.14197)
  - [https://arxiv.org/abs/2312.14197](https://arxiv.org/abs/2312.14197)
- Hidden prompts in manuscripts & AI-assisted peer review (arXiv:2507.06185)
  - [https://arxiv.org/abs/2507.06185](https://arxiv.org/abs/2507.06185)
- OWASP Top 10 for LLM Applications (v2025 PDF)
  - [https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf](https://owasp.org/www-project-top-10-for-large-language-model-applications/assets/PDF/OWASP-Top-10-for-LLMs-v2025.pdf)

---

## 7. 如何引用本项目

如果你要在笔记/报告/分享中引用本仓库，推荐用以下两种方式之一：

### 7.1 文本引用

> Zhu, Yuchen. *Prompt Drift Lab: protocol-driven evaluation of instruction-following drift under minimal prompt perturbations*. GitHub repository, 2025.

### 7.2 BibTeX（可选）

```bibtex
@misc{prompt_drift_lab,
  title        = {Prompt Drift Lab: protocol-driven evaluation of instruction-following drift under minimal prompt perturbations},
  author       = {Zhu, Yuchen},
  year         = {2025},
  howpublished = {GitHub repository}
}
```
