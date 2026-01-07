# ANONYMIZATION_CHECKLIST

This package is intended for double-blind review.

## Must-pass checks
- [ ] No author names, affiliations, emails, or personal links in `paper/paper_main.pdf`.
- [ ] No author names, affiliations, emails, or personal links in supplemental files.
- [ ] No identity strings in filenames (e.g., usernames, real names).
- [ ] No OS-specific junk (`__MACOSX/`, `.DS_Store`).
- [ ] No API keys / tokens in any script or log.

## Quick grep (run locally)
```bash
# Adjust keywords as needed
grep -RIn --exclude-dir=.git -E "Yuchen|Zhu|Shanghai University|yuchenzhu|上海|朱宇晨" .
```
