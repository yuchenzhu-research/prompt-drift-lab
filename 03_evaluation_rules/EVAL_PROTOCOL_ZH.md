# EVAL_PROTOCOL

> 目标：让评测侧的任何“baseline / 版本 / 提示词”等措辞，与以下目录的官方写法完全一致：
> - `01_experiment_design/`
> - `02_prompt_variants/`
>
> 核心约束：**评测不感知 A/B，只按样本 meta + 输出判定**。

---

## 0. 适用范围
本协议用于对实验运行产物进行评分与汇总，覆盖：
- 指令遵循率下降（instruction following drop）
- 格式崩坏（format break / schema violation）
- 语义漂移（semantic drift / content deviation）
-（可选）引用/检索行为漂移（citation/search drift）

不在本协议范围内：
- 重新运行模型（本协议只评测已有产物）
- 对提示词文本做主观分析或推断（评测侧只看 **meta 与输出**）
- 额外引入新指标或新维度（维度与档位以既有定义为准）

---

## 1. 术语与命名
### 1.1 单一事实来源
- **提示词变体/版本/baseline 的官方写法以 `02_prompt_variants/` 为准。**
- **题集/数据集版本的官方写法以 `01_experiment_design/` 为准。**
- 本协议不新增“项目级名词”；如必须新增，只能新增“评测流程内部术语”，且不得与 01/02 同名冲突。

### 1.2 术语对齐表（必须与 01/02 一字一致）
> 将下表中的“官方写法”直接从 01/02 复制粘贴，确保全项目同一概念只有一种称呼。

| 概念 | 官方写法（从 01/02 复制） | 说明 | 禁用/历史别名（如有） |
|---|---|---|---|
| Prompt Variant / Version（提示词变体/版本） | （填入） | 例如 prompt_a/prompt_b 或 vA/vB，以 02 为准 | （填入） |
| Prompt Set（提示词集合） | （填入） | 若 02 使用 promptset/prompt_pack 等，按 02 | （填入） |
| Baseline | （填入） | baseline 含义必须明确：提示词 baseline 或模型 baseline | （填入） |
| Eval Set（题集版本） | （填入） | 例如 eval_set_v*.jsonl，按 01 | （填入） |
| Run（单次运行） | （填入） | 例如 runs/YYYY-MM-DD_<model>_<promptset>/，按 01 | （填入） |

### 1.3 A/B 不感知原则
- 评测侧 **不读取** 提示词文本本体（prompt content）。
- 评测侧 **不使用** “A/B”作为评分先验。
- 分组与统计仅依据样本 meta 字段，例如：
  - `prompt_version` / `prompt_id` / `promptset`
  - `eval_set_version`
  - `model`
  - `run_id`
- 若缺少关键 meta：按“meta 不完整”处理，不得靠推断补齐。

---

## 2. 输入与评测单位
### 2.1 评测输入
评测输入为一次或多次运行目录下的产物集合。每次 run 至少包含：
1) config（模型/温度/采样/种子/提示词版本/题集版本）
2) raw outputs（原始输出，未经清洗）
3) judged scores（逐题逐维度评分 + 理由片段）
4) summary（汇总表一行）

文件存在性与命名约定以 `01_experiment_design/` 的定义为准。

### 2.2 评测单位
- 评测单位为“一个样本输出”（通常：某模型 + 某提示词版本 + 某题目的一次生成）。
- 每个样本输出必须可追溯到其 meta（run_id、model、prompt_version、eval_set_version、question_id 等）。

---

## 3. 维度绑定（Rubric = 维度 + Validity + Judge Prompt）
### 3.1 事实来源
本仓库中 “Rubric（评分口径）” 由以下**具体文件**共同定义：
- **评分维度与档位：** `03_evaluation_rules/02_scoring_dimensions.md`
- **Validity（valid/invalid 判定）：** `03_evaluation_rules/01_validity_criteria.md`
- **Judge 提示词（评测时使用的固定文本）：** `03_evaluation_rules/JUDGE_PROMPT.md`

本协议只定义“如何应用这些定义”，不扩展维度或档位。

### 3.2 Failure taxonomy 映射（用于归因，不新增打分维度）
在评分理由中允许使用以下标签做归因（可多选）：
- A. Schema/格式错误
- B. 指令偏离
- C. 语义漂移
- D. 稳健性问题（方差）
- E. 评测投机

这些标签用于解释，不改变维度定义与档位含义。

---

## 4. 评测流程
### 4.1 预检查
对每个 run：
1. 检查 config 是否齐全，并能解析：`model`、`sampling`、`seed`、`prompt_version`、`eval_set_version`。
2. 检查 raw outputs 是否为“原始输出”，未被二次加工。
3. 若缺失：记录为 `input_incomplete`，但仍可对存在样本继续评测。

### 4.2 样本级评分
对每个样本输出：
1. 读取问题（question）与参考信息（若题集包含）。
2. 仅依据输出文本 + 维度定义进行评分。
3. 记录：
   - 各维度分数
   - 关键证据片段（输出中的短片段）
   - 归因标签（A–E）
4. **不得**：
   - 因为 meta 显示 prompt_version 就预设更高/更低分
   - 以“应该比较 A/B”为由改变评分标准

### 4.3 汇总与统计
- 汇总表必须能按 meta 字段复现每一个数字。
- 允许的分组字段仅来自 meta（例如 prompt_version、model、eval_set_version）。
- 若要做 A/B 对比：只在汇总阶段按 `prompt_version` 分组做差异统计，评测过程中仍保持不感知。

---

## 5. 输出与落盘要求
### 5.1 judged_scores（逐题逐维度评分）
每个样本输出都必须生成一条记录，至少包含：
- `run_id`
- `model`
- `prompt_version`
- `eval_set_version`
- `question_id`
- `scores`（按维度组织）
- `evidence`（短片段）
- `failure_tags`（A–E 可多选）

字段名以 01/02 中既有实现为准；本协议不强行更改历史字段名。

### 5.2 summary（汇总表一行）
每个 run 生成一行 summary，至少包含：
- run 标识（与目录一致）
- 样本数量
- 各维度均值/占比
- 关键失败类型比例（A–E）

---

## 6. 一致性与审计
### 6.1 可复现验收
满足以下条件视为通过：
- 能从 runs/ 目录复现 summary 表中的每个数字
- 任意一条 judged_scores 都能定位到对应 raw output 与 config

### 6.2 术语一致性检查
对本文件、`JUDGE_PROMPT`、`00_evaluation_protocol` 三者做全文检索，确保：
- “baseline / 版本 / 提示词 / prompt_version / promptset / eval_set_version”等关键术语写法一致
- 不出现同一概念多种叫法

---

## 7. 变更记录
- Step（对齐引用）：将 `02_提示词版本` 的引用统一为 `02_prompt_variants/`；将 Rubric 引用绑定到具体文件（`02_scoring_dimensions`、`01_validity_criteria`、`JUDGE_PROMPT`）。
