# README.md

# 02_提示词版本

本目录存放本项目实际使用的提示词（`*.txt`），并通过 `PROMPT_MANIFEST.md` 统一定义它们之间的对照关系与统计口径。

- `PROMPT_MANIFEST.md`：提示词清单、变量层级（Family/Variant）与主实验统计边界
- `*.txt`：提示词本体（尽量不写解释性注释，保持可读 diff）

---

## 目录内容

- `00_baseline_prompt_A.txt`：Prompt A（探索版，pilot）
- `01_structured_prompt_B.txt`：Prompt B（协议化三段式，主实验基座）
- `02_conflict_prompt.txt`：B-variant（conflict）
- `03_long_prompt.txt`：B-variant（long）
- `04_weak_prompt.txt`：B-variant（weak）

---

## 如何使用（与实验链路对齐）

1. **主实验建议**：选择 Prompt B，并在 `baseline / conflict / long / weak` 间做对照。
2. **先导探索可选**：Prompt A 仅用于补充现象与机制线索；若未形成完整对照口径，不进入主实验定量统计。
3. **运行落盘建议**：在 config 或样本 meta 中记录 `prompt_family / prompt_variant / prompt_hash`，保证复现与审计。

---

## 与其他目录的关系

- `01_实验设计/`：实验目标、变量定义与流程
- `02_提示词版本/`（本目录）：提示词本体与变量清单
- `03_评测规则/`：有效性判定与评分 Rubric
- `04_实验结果/`：统计汇总与归因分析（主结论以 Prompt B 为准）

---

## 维护原则

- 提示词本体（`*.txt`）保持“干净可 diff”，解释性内容集中在 `PROMPT_MANIFEST.md`。
- 新增提示词版本时优先采用“单因素最小差分”，避免混杂变量导致归因不可审计。

