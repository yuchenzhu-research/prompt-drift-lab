# 02_prompt_variants（提示词版本）

本目录存放本项目**实际用于实验的提示词本体**（`*.txt`）。
提示词清单、变量层级与主实验统计口径统一由 `PROMPT_MANIFEST.md` 定义，
以保证不同提示词之间的对照关系可复核、可审计。

- `PROMPT_MANIFEST.md`：提示词清单、变量层级（Family / Variant）与主实验统计边界
- `*.txt`：提示词本体（尽量不写解释性注释，保持可读 diff）

---

## 目录内容

- `PROMPT_MANIFEST.md`：提示词清单与统计口径定义
- `00_baseline_prompt_A_ZH.txt`：Prompt A（探索版，pilot）
- `01_structured_prompt_B_ZH.txt`：Prompt B（协议化三段式，主实验基座）
- `02_conflict_prompt_ZH.txt`：B 的扰动版本（conflict）
- `03_long_prompt_ZH.txt`：B 的扰动版本（long）
- `04_weak_prompt_ZH.txt`：B 的扰动版本（weak）

---

## 如何使用（与实验链路对齐）

1. **主实验**：以 Prompt Family B 为基座，在
   `baseline / conflict / long / weak` 之间进行对照。
2. **先导探索（可选）**：Prompt Family A 仅用于补充现象与机制线索；
   若未在同题集、同参数、同次数下形成完整对照，则不进入主实验定量统计。
3. **运行落盘建议**：在 config 或样本 meta 中记录
   `prompt_family / prompt_variant / prompt_file / prompt_hash`，
   以保证结果可复现、可审计。

---

## 与其他目录的关系

- `01_experiment_design/`：实验目标、变量定义与流程
- `02_prompt_variants/`（本目录）：提示词本体与提示词清单
- `03_evaluation_rules/`：有效性判定与评分 Rubric
- `04_results/`：统计汇总与归因分析（主结论以 Prompt Family B 为准）

---

## 维护原则

- 提示词本体（`*.txt`）保持“干净可 diff”，
  所有解释性与分析性内容集中在 `PROMPT_MANIFEST.md`。
- 新增提示词版本时，优先采用“单因素最小差分”，
  避免混杂变量导致归因不可审计。
