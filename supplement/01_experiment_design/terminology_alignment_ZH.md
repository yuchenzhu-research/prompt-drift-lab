# terminology.md（术语与命名规范）

> 目的：把仓库里反复出现但可能叫法不一致的词统一成“唯一写法”，避免 01/02/03/04 各写各的。

## 1. 实验对象与角色

- **Prompt Drift（提示词漂移）**：仅因提示词/格式/措辞发生微小变化，导致输出在**指令遵循、结构、语义**等方面出现稳定差异。
- **Generator / 生成模型**：被测试的模型，负责产出答案（例如：ChatGPT / Gemini / Claude）。
- **Judge / 评测模型**：负责根据 rubric/protocol 给生成结果打分并给证据（可以是同一批模型互评，也可以自评）。

## 2. 维度（Factors）与唯一写法

> 推荐所有记录字段都用 snake_case（下划线），避免大小写混乱。

- **question_id**：题目编号。唯一写法：`q1` / `q2` / `q3` / `q4`
- **prompt_version**：提示词版本。唯一写法：`prompt_a` / `prompt_b`
  - 备注：如果主实验只用 B，也仍保留 A 的字段值，便于未来扩展。
- **length_variant**：长短版本。唯一写法：`short` / `long`
- **instruction_variant**：显式/隐式。唯一写法：`explicit` / `implicit`
- **generator_model**：生成模型标识（自由字符串，但建议固定表记法，例如：`chatgpt` / `gemini` / `claude`）
- **judge_model**：评测模型标识（同上）
- **run_id**：一次“生成”运行的唯一 ID（建议用时间戳或 hash）
- **eval_id**：一次“评测”记录的唯一 ID（建议用时间戳或 hash）

## 3. 产物（Artifacts）命名建议

> 你当前已有 PDF 产物时，不强制改名；此处是**推荐规范**，用于后续新增数据时保持一致。

- **生成结果（PDF）**：
  - 推荐：`{question_id}__{length_variant}_{instruction_variant}__{prompt_version}__{generator_model}.pdf`
  - 示例：`q3__long_implicit__prompt_b__chatgpt.pdf`

- **评测记录（JSON）**：
  - 推荐：`{eval_id}__{judge_model}__on__{generator_model}__{question_id}.json`
  - 示例：`2025-12-23T21-10-00__gemini__on__chatgpt__q3.json`

## 4. 指标（Metrics）唯一 Key 与含义（建议 8 个）

> 说明：这里的 key 只是“术语对齐”，具体打分规则在 rubric 里。

| metric_key | 中文名 | 你在观察的现象（一句话） |
|---|---|---|
| instruction_following | 指令遵循 | 是否完成了用户要求的任务目标（不跑题） |
| schema_validity | 格式合规 | 是否严格符合要求的 Markdown/JSON/分段结构 |
| section_coverage | 结构覆盖 | 需要的章节/字段是否齐全，有无缺失 |
| semantic_drift | 语义漂移 | 相比基准版本（或预期）是否出现核心含义偏移 |
| hallucination_risk | 幻觉风险 | 是否出现明显不可靠/编造/无法验证的内容倾向 |
| citation_compliance | 引用合规 | 要求引用时是否给出可追溯来源；不该编造引用 |
| verbosity_control | 冗长控制 | 是否在满足要求前提下控制篇幅、避免无关扩写 |
| refusal_safety | 拒答与安全 | 在需要拒答/警示时是否合规、是否过度拒答 |

## 5. 同义词收敛（禁止再混用）

- “A/B 版本” → 统一写：`prompt_a` / `prompt_b`
- “显式/隐式” → 统一写：`explicit` / `implicit`
- “长/短” → 统一写：`long` / `short`
- “遵循率/指令遵循/依从性” → 统一写：`instruction_following`
- “格式崩坏/结构崩坏/模板不合规” → 统一写：`schema_validity`（必要时补 `section_coverage`）
