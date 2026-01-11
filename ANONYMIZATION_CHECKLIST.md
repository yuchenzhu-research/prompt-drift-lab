# ANONYMIZATION_CHECKLIST

This package is intended for double-blind review.

## Must-pass checks
- [ ] No author names, affiliations, emails, or personal links in `paper/paper.pdf`.
- [ ] No author names, affiliations, emails, or personal links in supplemental files.
- [ ] No identity strings in filenames (e.g., usernames, real names).
- [ ] No OS-specific junk (`__MACOSX/`, `.DS_Store`).
- [ ] No API keys / tokens in any script or log.

## Quick grep (run locally)
```bash
# Adjust keywords as needed
grep -RIn --exclude-dir=.git -E "YOUR_NAME|YOUR_EMAIL|YOUR_UNIVERSITY|/Users/|github\.com|openreview\.net" .
```
