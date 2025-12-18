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
