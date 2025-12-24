# 00_评测协议

## 0. 本目录的作用与优先级

本目录用于冻结 Prompt Drift Lab 的评测规则与评测执行方式，确保结果**可复现、可审计、可对照**。

**优先级（非常重要）**

1) `EVAL_PROTOCOL.md`：唯一可执行的评测规范（Rubric + JSON 合同 + evidence 硬约束）。
2) `JUDGE_PROMPT.md`：评测器（judge）使用的固定提示词；若与协议冲突，以协议为准。
3) `01_合规性判定说明.md`、`02_行为评分维度说明.md`：解释与辅助阅读；不得改变协议口径。

**术语对齐（Step 4 要点）**
- 本目录内出现的任何 “baseline / versions / 提示词版本 / prompt(相关字段)” 等措辞，若与 `01_实验设计` / `02_提示词版本` 的官方命名不一致，**以 01/02 为准**并在本目录内统一口径。
- 评测侧**不感知 A/B**：A/B 仅是提示词编写侧的对照标记；评测仅依据样本 **meta**（如文件名中的版本标签或 `prompt_version` 等字段）进行记录与分组，不作为评分先验。

> 备注：仓库中部分历史产物文件名可能带有 `_v2` 后缀，这是早期命名遗留，**不代表当前规则存在“版本分裂”**。
> 评测口径以本目录内的 `EVAL_PROTOCOL.md` / `JUDGE_PROMPT.md` 为准。

---

## 1. 评测对象与输入

### 1.1 被测对象（generator）

- 不同模型在同一套提示词条件下生成的“三段式结构化输出”（以 PDF 形式保存）。

### 1.2 输入 bundle（每次评测的最小单元）

一个 bundle = 16 个 PDF，覆盖：

- questions：`Q3`, `Q4`
- versions：`baseline`, `long`, `weak`, `conflict`
- trigger_types：`implicit`, `explicit`

补充说明（术语对齐）：
- 此处的 `versions` 表示“提示词版本标签”（如 02 中已统一为 `prompt_version` / `prompt_id` 等字段名，则将 `versions` 视为同义旧称，最终以 02 的官方叫法为准）。
- 评测阶段对 `versions` 仅做记录/分组，不将其解释为“A/B”或强弱先验。

**文件命名约定**：

- `q{3|4} {version} {implicit|explicit}.pdf`
- 示例：`q3 baseline explicit.pdf`

---

## 2. 输出产物（Artifacts）

每次评测输出 **1 个 JSON**（严格 JSON，仅包含协议要求字段），用于后续脚本汇总。

### 2.1 交叉评测（cross-model judging）产物命名

推荐命名：

- `judge_{judge_model}_bundle_{generator_model}.json`

> 若你当前仓库里使用了 `..._v2.json` 的文件名，可继续沿用以保证历史路径与脚本不受影响；只要内容遵循本协议即可。

### 2.2 自评（self-judging）产物命名

推荐命名：

- `self_judge_{model}.json`

### 2.3 存放位置（与统计脚本一致）

- 通过合规检查（valid）：放入 `.../valid_results/...`
- 未通过合规检查（invalid）：放入 `.../invalid_results/...`

invalid 的产物不进入主统计，但保留用于分析“评测器偏移/协议不遵循”。

---

## 3. 两种评测方法（Methods）

### 3.1 主方法：交叉评测（Cross-model judging）

- 使用 judge 模型对其他 generator 模型的 16 个 PDF 逐文件打分。
- 主结论以 **valid 的交叉评测结果**为统计口径。

说明：若某个 judge 模型输出经常不满足协议（例如输出非严格 JSON、缺字段、evidence 违规等），其结果会进入 invalid，用于单独分析，不纳入主统计。

### 3.2 补充方法：自评（Self-judging）

- generator 对自己的 16 个 PDF 按同一协议打分。
- 用途：一致性校验、偏差诊断、对照参考；不作为主结论的唯一依据。

---

## 4. 合规性与 invalid 规则（Validity）

judge 输出出现以下任一情况，判为 **invalid**：

- 非严格 JSON（含 Markdown、解释性文字、前后缀）
- JSON 合同不匹配 / 缺字段 / 条目数量不对
- `total` 不等于五维之和
- `A_structure == 0` 但仍给 `B/C/D/E` 非 0 分
- evidence 违反协议硬约束（例如包含 `.../…`、不是原文截取、空 evidence 却给非 0 分等）
- `aggregates` 与 `per_file_scores` 不可复算一致

---

## 5. 偏差控制（Bias control）

- **盲评**：评测器不应被提示词角色标签影响（只依据文件名与 PDF 内容判定）。
- **A/B 不感知**：评测器不将样本标记解释为“A/B 对照”，不进行跨样本比较；仅按样本 meta（如 `versions`/`prompt_version`）记录与分组，评分只基于内容与 Rubric。
- **统一协议**：所有评测必须使用同一份 `EVAL_PROTOCOL.md` 与 `JUDGE_PROMPT.md`。
- **记录元信息（若可得）**：模型名/版本、日期、推理模式、temperature/top_p 等，用于排查复现差异。
