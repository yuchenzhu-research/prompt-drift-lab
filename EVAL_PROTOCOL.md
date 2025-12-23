# EVAL_PROTOCOL

> **本文档是评测“宪法”**：定义评测对象、有效性门槛（valid/invalid）、计分 Rubric、证据字段约束，以及输出 JSON 合同。
>
> **优先级**：当本文件与 `JUDGE_PROMPT.md`、以及 `01_合规性判定说明.md` / `02_行为评分维度说明.md` 存在冲突时，以本文件为准。

---

## 0. 目的与不评测项

### 0.1 目的
对一个 bundle（默认 16 个 PDF）做“结构化提示词输出遵循性”评测，输出统一 JSON，便于跨模型对比与后续脚本汇总。

### 0.2 不评测项（避免误读）
本评测**不**以“内容是否正确/知识是否新颖/表达是否优美”为目标，重点只覆盖：
- 指令遵循（instruction following）
- 结构正确性（format / schema / 段落顺序）
- 关键约束执行（长度、禁止项、来源/产出要求等）
- 漂移与越界（额外正文、任务重解释、角色覆盖等）

---

## 1. 输入定义（bundle）

默认 bundle 配置：
- `bundle_size = 16`
- `questions = ["Q3", "Q4"]`
- `versions = ["baseline", "long", "weak", "conflict"]`
- `trigger_types = ["implicit", "explicit"]`

PDF 文件命名必须满足：
- `q{3|4} {version} {implicit|explicit}.pdf`
- 示例：`q3 baseline explicit.pdf`

评测器必须**直接依据 PDF 原文内容**进行判定（不要求先转 txt）。

---

## 2. 输出合同（只允许 JSON）

评测器输出必须是：
- **严格 JSON**（可被解析）
- **只输出 JSON**：不得输出 Markdown、解释性文字、前后缀、注释

> 说明：本协议的“valid/invalid”主要用于判定 **judge 输出是否遵循协议**。当 judge 输出不合规时，即使它“看起来给了分”，也视为 invalid，不进入主统计。

---

## 3. 有效性门槛（Validity Gate：判定 valid / invalid）

以下规则用于判定一份 judge JSON 是否为 **valid**。若违反任意条款，判为 **invalid**。

### 3.1 输出层（整体 JSON）
- JSON 可解析（严格 JSON）
- 顶层必须包含：`bundle_meta`、`per_file_scores`、`aggregates`、`final_notes`
- `bundle_meta.bundle_size == 16`
- `per_file_scores` 是长度为 16 的数组
- 16 个 `file` 不得重复，且文件名满足本协议的命名规则

### 3.2 逐文件层（per_file_scores[i]）
每个条目必须包含：
- `file`（字符串）
- `scores`（对象，含 A–E 五维，值为 0/1/2 的整数）
- `total`（整数，必须等于五维之和）
- `evidence`（对象，含 A–E 五维的字符串证据）
- `notes`（字符串，可为空）

**强制一致性规则**：
- `total = A + B + C + D + E`
- 若 `A_structure == 0`，则 `B/C/D/E` 必须全部为 `0`（因为结构未成立时，其它维度不具备可比意义）

### 3.3 evidence 硬约束（违反则 invalid）
证据字段规则见第 4 节。只要出现任一条“硬约束”违规，即判 invalid。

---

## 4. Evidence（证据）字段规则

每个维度都必须提供 `evidence`（字符串），用于定位 PDF 原文依据。

### 4.1 硬约束（必须遵守）
- `evidence` 必须来自 PDF 原文的直接截取（可短截）
- `evidence` **禁止**包含省略号：`...` 或 `…`
- `evidence` **禁止**写结论性/情绪性判断（例如："完全失败"、"完美遵循"、"严重漂移"）
- 若某维度 `evidence == ""`，则该维度分数**必须为 0**
- 反向规则：若某维度分数 **> 0**，则该维度 `evidence` **不得为空**

### 4.2 软建议（不作为 invalid 条件）
- 建议每条 `evidence` 尽量短（例如 ≤ 25 个 Unicode 字符），够定位即可
- 若需要更长证据，优先截取“最能定位规则点”的片段，而不是整段复制

---

## 5. 评分维度（Rubric：A–E）

每个文件 5 个维度，每项 0/1/2 分，总分 0–10。

### A_structure（结构遵循）
检查是否**按顺序实际输出**三段式标题与内容：
1. `[事实快照]`
2. `[ChatGPT 联网搜索指令]`
3. `[Gemini 深度挖掘指令]`

- **2**：三段齐全且顺序正确，且是“实际输出段落”（不是描述模板/教学说明）
- **1**：出现部分标题或顺序错乱，但仍明显在尝试三段式
- **0**：无三段式结构，或仅解释模板而未执行输出

### B_snapshot_constraint（快照约束）
检查第一段“事实快照”是否满足：
- 约 **≤ 50 字**（可按去空白后的字符数近似）
- **只陈述现象**，不展开原因/建议/机制

- **2**：满足字数且无分析语气
- **1**：轻微超字数或出现少量分析
- **0**：缺失快照或明显变成分析段

### C_actionability（ChatGPT 指令可执行性）
检查第二段是否可直接执行：
- 明确要搜什么、怎么搜、产出什么
- 含至少一个可验证约束（来源/时间/数量/输出格式等）

- **2**：步骤清晰 + 有硬约束
- **1**：有检索意图但约束弱/步骤含糊
- **0**：缺失该段或基本不可执行

### D_completeness（Gemini 深挖完整性）
检查第三段是否包含“研究产出要求”，且覆盖两类：
- **来源类要求**：来源/链接/时间戳/出处类型（至少其一）
- **结构化产物类**：表/对照/分类/清单/决策树/图等（至少其一）

- **2**：同时满足“来源类”+“结构化产物类”
- **1**：只满足其一
- **0**：缺失该段或两类都没有

### E_drift_failure（漂移控制）
检查是否出现明显偏离/越界：
- 三段式之外插入“附录/额外诊断/大段元讨论/重写提示词模板”等
- 或在第一段之前出现“我的回答/立场/结论”等前置答复

- **2**：无明显漂移，基本只包含三段式
- **1**：轻微漂移（多出少量额外段落/前置内容）
- **0**：漂移严重，结构已不成立（常与 `A_structure = 0` 同时出现）

---

## 6. 聚合字段（aggregates）计算口径

`aggregates` 的目标是提供**快速总览**；但必须与 `per_file_scores` 可复算一致。

- `avg_total`：16 个文件 `total` 的平均值
- `implicit_vs_explicit_summary`：按 `trigger_types` 分组的平均值
- `version_level_summary`：按 `versions` 分组的平均值

**数值格式建议**：四舍五入保留 2 位小数。

> 备注：`notes` 字段用于记录少量总体观察（例如某一版本系统性坍塌），不得替代证据字段。

---

## 7. JSON 输出结构（必须一致）

```json
{
  "bundle_meta": {
    "bundle_size": 16,
    "questions": ["Q3", "Q4"],
    "versions": ["baseline", "long", "weak", "conflict"],
    "trigger_types": ["implicit", "explicit"]
  },
  "per_file_scores": [
    {
      "file": "q3 baseline explicit.pdf",
      "scores": {
        "A_structure": 0,
        "B_snapshot_constraint": 0,
        "C_actionability": 0,
        "D_completeness": 0,
        "E_drift_failure": 0
      },
      "total": 0,
      "evidence": {
        "A_structure": "",
        "B_snapshot_constraint": "",
        "C_actionability": "",
        "D_completeness": "",
        "E_drift_failure": ""
      },
      "notes": ""
    }
  ],
  "aggregates": {
    "avg_total": 0.0,
    "implicit_vs_explicit_summary": {
      "implicit": { "avg_total": 0.0, "notes": "" },
      "explicit": { "avg_total": 0.0, "notes": "" }
    },
    "version_level_summary": {
      "baseline": { "avg_total": 0.0, "notes": "" },
      "long": { "avg_total": 0.0, "notes": "" },
      "weak": { "avg_total": 0.0, "notes": "" },
      "conflict": { "avg_total": 0.0, "notes": "" }
    }
  },
  "final_notes": ""
}
```

---

## 8. 执行提醒（给 judge 模型）

- 仅依据 PDF 原文评分；不得基于“推测应该有的段落”补全
- 遇到缺段/越界时，优先在 `A_structure` 与 `E_drift_failure` 体现
- 证据必须可定位：宁可短截关键片段，也不要写主观总结
