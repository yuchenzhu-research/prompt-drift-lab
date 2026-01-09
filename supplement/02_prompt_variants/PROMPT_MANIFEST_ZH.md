# PROMPT_MANIFEST.md

# 提示词清单与变量定义

本文件用于定义本项目的提示词资产、变量层级与统计口径，确保不同提示词之间的对照关系可复核、可审计。

---

## 0. 范围与统计口径

- **主实验（定量统计）**：以 **Prompt B（协议化三段式）** 为基座，仅比较 **B 的扰动版本（baseline / conflict / long / weak）**。
- **先导探索（定性留档）**：`00_baseline_prompt_A.txt` 为 **Prompt A（探索版）**，用于动机与失败样本收集；若未在同题集、同参数、同次数下形成完整对照，则**不进入主实验统计汇总**。

一句话：**统计口径以 B 为准；A 仅用于补充现象与机制线索。**

---

## 1. 文件清单

| 文件 | Prompt Family | Prompt Variant | 用途定位 |
|---|---|---|---|
| `00_baseline_prompt_A.txt` | A | baseline | 先导探索（pilot） |
| `01_structured_prompt_B.txt` | B | baseline | 主实验基座（protocol prompt） |
| `02_conflict_prompt.txt` | B | conflict | 引入指令张力，测试优先级失效 |
| `03_long_prompt.txt` | B | long | 拉长与冗余，测试注意力稀释 |
| `04_weak_prompt.txt` | B | weak | 弱化约束，测试回退到自然对话 |

---

## 2. 变量层级（Family 与 Variant）

为避免“提示词版本/变体”混用，本项目将变量拆成两层：

- **Prompt Family**：A vs B（两套三段式模板）
- **Prompt Variant**：在选定某个 Family 后，对措辞与约束做单因素扰动（baseline / conflict / long / weak …）

建议在所有运行产物（raw outputs / judged scores / summary）中显式记录：

- `prompt_family`: `A` 或 `B`
- `prompt_variant`: `baseline` / `conflict` / `long` / `weak`

---

## 3. Prompt Family A：探索版（Pilot Baseline）

**定位**：早期跑通链路与暴露失败模式。

**常见可观察现象**（用于定性记录）：
- 结构漂移：段落合并、标题改写、字段缺失
- 指令偏离：忽略约束、擅自扩展内容任务
- 语义漂移：答非所问、立场先行、泛化总结
- 静默漏约束：看似相关但缺关键动作/关键字段

**统计边界**：除非 A 在与 B 完全一致的题集覆盖与运行口径下形成对照，否则不与 B 的定量结果混合。

---

## 4. Prompt Family B：协议化三段式（主实验基座）

**目标**：把输出要求写成更可执行、可核验的“协议”，使 drift 更容易被 rubric 识别、统计与回溯。

**设计要点**（以提示词本体为准）：
- 结构锚定：三段式边界更明确，便于对齐与判分
- 约束可核验：减少“表面合规、关键约束缺失”的灰区
- 机制导向：鼓励提出可证伪假说与最小验证步骤

---

## 5. B 的扰动空间（Prompt Variants）

下列版本均以 B 为基座，原则上一次只改变一个主要维度，用于形成可对照的最小差分。

### 5.1 `baseline`（`01_structured_prompt_B.txt`）

- **用途**：主实验对照基线。
- **期望**：结构稳定、字段齐全、便于判分。

### 5.2 `conflict`（`02_conflict_prompt.txt`）

- **扰动维度**：引入潜在冲突/张力指令，测试优先级分配。
- **典型失败**：绕开结构协议、优先级不稳定、对齐覆盖。

### 5.3 `long`（`03_long_prompt.txt`）

- **扰动维度**：提示更长、更冗余，测试注意力稀释与局部遗忘。
- **典型失败**：只遵循部分要求、关键约束被淹没、目标被模型重写。

### 5.4 `weak`（`04_weak_prompt.txt`）

- **扰动维度**：把硬约束弱化为建议性表述，测试回退到自然对话分布。
- **典型失败**：结构崩坏、字段缺失、静默漏约束比例上升。

---

## 6. 复现记录（最低字段建议）

为保证结果可复核，建议每次运行与评测落盘时记录以下字段（可放在 config 或样本 meta 中）：

- `question_id`：题目 ID（如 Q1–Q4）
- `model`：被测模型
- `prompt_family` / `prompt_variant`
- `prompt_file`：提示词文件名
- `prompt_hash`：提示词内容哈希（建议 SHA256）
- `temperature` / `top_p` / `seed` / `n_runs`
- `run_date`：运行日期（平台更新可能影响结果）

---

## 7. 新增或修改提示词的约束（minimal diffs）

新增 variant 时建议遵守：

1. **单因素**：一次只测试一个假设（长度、冲突、约束强度、示例位置等）
2. **可指认**：变化点能被清晰指出（diff 可读）
3. **可回溯**：结果能在统计与归因中按同一维度对照

---

## 8. 与评测规则的对应关系

- 提示词负责构造输入扰动（prompt space）
- 评测规则负责判定输出行为（rubric & validity）

相关文件位于：
- `03_评测规则/`（协议、判分标准、维度说明）