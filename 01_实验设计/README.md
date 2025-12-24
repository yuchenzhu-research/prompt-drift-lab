# 01｜实验设计（v2：对齐现有产物）

> 本 README 只描述**已跑出的实验**与**已存在的评测产物**；不扩展“未来可能做”的设置。

## 1. 本次实验在测什么

研究对象：LLM 在提示词/格式/措辞发生微小变化时，出现的
- 指令遵循率下降（instruction following drop）
- 格式崩坏（format break / schema violation）
- 语义漂移（semantic drift / content deviation）

本次 v2 的具体落点：
- 让模型输出固定**三段式结构**（用于后续检索与深挖），观察其在不同版本/触发方式下是否稳定遵循。

## 2. 评测单元与实验矩阵

本次已完成的评测 bundle：共 **16** 份输出文件。

维度：
- Questions：`Q3`、`Q4`
- Versions：`baseline`、`long`、`weak`、`conflict`
- Trigger types：`implicit`、`explicit`

因此实验矩阵为：`2 questions × 4 versions × 2 triggers = 16`。

文件命名约定：
- `q{question_id} {version} {trigger_type}.pdf`
- 示例：`q3 baseline explicit.pdf`

> 说明：`version` 与 `trigger_type` 的具体含义以本仓库对应提示词文件为准；此处不新增定义，仅按现有产物的命名与汇总字段复述。

## 3. 被要求的输出格式（三段式）

每份输出都应严格按顺序包含以下 3 个小节（标题必须出现）：
1) `[事实快照]`
2) `[ChatGPT 联网搜索指令]`
3) `[Gemini 深度挖掘指令]`

其中 `[事实快照]` 的约束：
- **≤ 50 字**
- **只写事实**，不夹带解释/因果

你可以把三段式理解为：
- 事实快照：给评测与后续分析提供“压缩后的事实入口”
- 联网搜索指令：给 ChatGPT Deep Research/联网检索直接用
- 深度挖掘指令：给 Gemini Deep Research 直接用

## 4. 打分维度（与现有汇总 JSON 字段一致）

评分量表：每维 `0–2` 分，共 5 维，总分 `0–10`。

- **A_structure**：是否按三段式输出（顺序正确、段落清晰）
- **B_snapshot_constraint**：事实快照是否 ≤50 字且无解释/因果
- **C_actionability**：ChatGPT 联网搜索指令是否可直接执行（明确联网、产出形态等）
- **D_completeness**：Gemini 深挖指令是否覆盖机制点 + 结构化产出 + 可操作建议
- **E_drift_failure**：是否出现明显漂移失败（输出退化成分析长文/结构不可辨认）

> 详细口径见：`01_实验设计/实验协议.yaml`（EVAL_PROTOCOL_v2）。

## 5. 本次已观测到的现象（只复述汇总结论）

来自汇总产物 `judge_chatgpt_bundle_gemini_v2.json` 的统计摘要：
- **implicit**：8/8 未按三段式输出（平均总分 0）
- **explicit**：8/8 完成三段式（平均总分 9）
- 主要扣分点集中在：`[事实快照]` **超 50 字**或**夹带因果/解释**

> 这是一轮固定矩阵的对照结果；本 README 不做外推、不做机制推断。

## 6. 产物清单（复现所需的最小证据链）

本次实验的“最小可复现证据链”由两类文件组成：
1) **16 份原始输出（PDF）**：文件名遵循 `q{question_id} {version} {trigger_type}.pdf`
2) **评测汇总 JSON**：`judge_chatgpt_bundle_gemini_v2.json`
   - `bundle_meta`：bundle 元信息
   - `per_file_scores`：逐文件逐维度分数 + evidence + notes
   - `aggregates`：总体均值、implicit vs explicit、按 version 汇总
   - `final_notes`：评测者总结（如有）

> 任何对外展示的结论，至少需要能指回：`per_file_scores[*].evidence` 的可观察片段。

## 7. 如何把本 README 与后续章节对齐

- Step 3（回写到 01）只做两件事：
  1) 让读者在 `01_实验设计/` 看懂“这 16 份文件在测什么、怎么判分”
  2) 保证 `01_实验设计/实验协议.yaml` 与 `04_实验结果/judge_chatgpt_bundle_gemini_v2.json` 字段一致

- Step 4/05 的分析（如“为什么 implicit 全失败”）应放在：
  - `04_实验结果/`（结果描述与对照）
  - `05_总结与展望/`（局限性、未来工作）