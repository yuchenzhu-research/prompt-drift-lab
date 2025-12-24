# 04 实验结果（索引入口）

**You are here：** `04_results/README_ZH.md`  
**Upstream：** `01_experiment_design/` → `02_prompt_variants/` → `03_evaluation_rules/`  
**Downstream：** `05_summary_and_outlook/`  
**Sidecar：** `06_methodological_addenda_and_controls/`（控制实验/方法选择）

## 本目录职责
本目录存放所有**可复核的证据产物**：
- 汇总表（CSV）
- 评测 bundle（JSON）
- 原始模型输出（PDF）
- valid / invalid 分桶（便于审计）

> 本 README 只做**索引**（文件在哪里）。  
> 结果解释、失败模式与归因逻辑请看：`04_results/03_results_analysis_ZH.md`。

---

## 30 秒入口：数字在哪里

### 1) 主汇总表（从这里开始）
- **全局汇总表：**  
  `04_results/02_cross_model_evaluation/valid_evaluations/summary_tables/summary.csv`

### 2) 切片表（按模型/题目/版本拆分）
- `.../summary_tables/main_method_by_*.csv`
- `.../summary_tables/supporting_method_by_*.csv`
- `.../summary_tables/main_method_inter_judge_agreement.csv`

---

## 证据文件分别放在哪

### A) 原始模型输出（生成产物）
- `04_results/01_raw_model_outputs/`  
  （按 generator 模型分组的 PDF）

### B) 有效评测（进入统计汇总）
- **主方法（跨模型互评）：**  
  `04_results/02_cross_model_evaluation/valid_evaluations/main_method_cross_model/`
- **辅助方法（自评；仅 sanity-check）：**  
  `04_results/02_cross_model_evaluation/valid_evaluations/supporting_method_self_eval/`

### C) 无效评测（不进统计；用于诊断）
- `04_results/02_cross_model_evaluation/invalid_evaluations/`
  - `invalid_evaluations/README.md`（invalid 判定与 flags 说明）
  - `invalid_evaluations/used_evaluation_protocol_ZH.md`（协议快照）
  - `invalid_evaluations/used_prompt_manifest_ZH.md`（提示词快照）
  - `invalid_evaluations/main_method_cross_model/`
  - `invalid_evaluations/supporting_method_self_eval/`

---

## 如何复核任何结论（3 步）
1) 在 `summary_tables/summary.csv`（或 `*_by_*.csv`）定位对应行  
2) 打开 `valid_evaluations/.../` 下对应的 bundle JSON（评分与理由）  
3) 如需追溯生成输出，到 `01_raw_model_outputs/` 找对应 PDF

---

## 接下来读什么
- 解释与失败模式：`04_results/03_results_analysis_ZH.md`  
- 最终结论与边界：`05_summary_and_outlook/README_ZH.md`  
- 为什么主实验用 Prompt B：`06_methodological_addenda_and_controls/README_ZH.md`
