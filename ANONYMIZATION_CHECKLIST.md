# Anonymization Checklist (Optional)

> Optional internal checklist for double-blind packaging. Reviewers may ignore this file.

## Must-pass checks
- [ ] No author names, affiliations, emails, or personal links in `paper/paper.pdf`.
- [ ] No author names, affiliations, emails, or personal links in supplemental files.
- [ ] No identity strings in filenames (e.g., usernames, real names).
- [ ] No OS-specific junk (`__MACOSX/`, `.DS_Store`, `._*`).
- [ ] No API keys or access tokens in any script, config, or log file.

## Suggested verification (local)
- [ ] Run a repo-wide grep for common identity strings and local paths.
- [ ] List archive contents to ensure no macOS metadata folders are included.