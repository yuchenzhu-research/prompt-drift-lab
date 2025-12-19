"""
用途：
- 对模型输出进行硬性结构合规判定（v2）
- 对应评测规则：03_评测规则/01_硬性合规判定规则.md

说明：
- 本脚本不评内容质量或事实正确性
- 仅用于结构/指令遵循的自动化判定
"""
def score_output(output):
    score = 0
    if "## 1." in output and "## 2." in output and "## 3." in output:
        score += 1
    if len(output.split("## 1.")[1].split("## 2.")[0]) < 120:
        score += 1
    if "联网" in output:
        score += 1
    if "Gemini" in output:
        score += 1
    return score