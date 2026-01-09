# 02 提示词变体（Prompt Variants）

本目录存放**生成侧（generator-side）提示词**及其受控变体，用于探测 LLM 在提示词微小变化下的稳定性（prompt drift）。

> 本目录**不是** judge 提示词存放处。 judge 提示词与评测规则在：`03_evaluation_rules/`（见 `JUDGE_PROMPT_ZH.md` 与 `EVAL_PROTOCOL_ZH.md`）。

---

## 0) 30 秒导航（从这里开始）

- 想看实验实际用到的 prompts？

  - 建议从清单开始（推荐口径）：
    - `PROMPT_MANIFEST_ZH.md`（中文）/ `PROMPT_MANIFEST.md`（英文）
  - 或直接查看提示词文件：
    - `00_baseline_prompt_A*.txt`
    - `01_structured_prompt_B*.txt`
    - `02_conflict_prompt*.txt`

- 想看 prompts 如何与结果对应？

  - 若结果目录保存了“当次使用的 prompt 清单快照”，通常位于：
    - `04_results/**/used_prompt_manifest*.md`

---

## 1) 分工边界（该放什么/不该放什么）

### 属于 `02_prompt_variants/` 的内容

- 生成侧提示词文本（prompt text）及其**变体**
- 一个 prompt 清单（manifest），用于映射 `prompt_id / prompt_version -> 文件名`
- 版本化与引用口径说明（不包含评分规则）

### 不属于本目录的内容

- 评分/评测规则 → `03_evaluation_rules/`
- 结果表/结果分析 → `04_results/`

---

## 2) 推荐的 manifest 口径

如果存在 `PROMPT_MANIFEST_ZH.md` / `PROMPT_MANIFEST.md`，建议把它当作 prompt 清单的**唯一权威入口**：

- `prompt_id`（稳定）
- `prompt_version`（运行记录里使用的版本标签）
- `language`（EN/ZH）
- `filepath`（本目录相对路径）

这样结果目录可快照 `used_prompt_manifest*`，做到可审计/可复现。

---

## 3) 目录地图（典型结构）

```
02_prompt_variants/
  README.md
  README_ZH.md
  PROMPT_MANIFEST.md
  PROMPT_MANIFEST_ZH.md
  00_baseline_prompt_A.txt
  00_baseline_prompt_A_ZH.txt
  01_structured_prompt_B.txt
  01_structured_prompt_B_ZH.txt
  02_conflict_prompt.txt
  02_conflict_prompt_ZH.txt
```

（若你的实际文件名不同，以实际为准：同步更新 manifest 与本 README。）

---

## 4) 版本化规则（简单且稳）

- 为了可比性，不建议“悄悄覆盖”旧 prompt。
- 推荐：新增文件或在 manifest 中引入新的 `prompt_version`。
- `prompt_id` 保持稳定，方便分析按 id 聚合、按 version 对比。

---

## 5) 与其他目录如何串联

- 实验输入（题集、schema）→ `01_experiment_design/`
- 评测规则 + judge 契约 → `03_evaluation_rules/`
- 结果工件 + 快照 → `04_results/`