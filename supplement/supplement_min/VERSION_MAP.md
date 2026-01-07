# VERSION_MAP

This file freezes the canonical evaluation artifact set for **Prompt Drift Lab**.

- **Frozen version:** v2.1
- **Frozen date:** 2026-01-06
- **Policy:** Any *behavioral* change to the evaluation contract MUST bump this version (v2.2, v2.3, …) and regenerate SHA256.

## Canonical artifacts (frozen)

| Artifact ID | Lang | Path | SHA256 |
|---|---|---|---|
| PROMPT_MANIFEST_EN | EN | `02_prompt_variants/PROMPT_MANIFEST.md` | `e5c3045cf9a015a195e71d75871e197bc2d4ca8ef64597d538484bf831a48533` |
| PROMPT_MANIFEST_ZH | ZH | `02_prompt_variants/PROMPT_MANIFEST_ZH.md` | `0e40d346b97e157d3e6b13af93529b611bed644134fa2269ddb0d449d0b390d4` |
| EVAL_PROTOCOL_EN | EN | `03_evaluation_rules/EVAL_PROTOCOL.md` | `8e9b30ddc7e4f14f21a9e523777291b372577bc1dc4a1518599bec245945ae1b` |
| EVAL_PROTOCOL_ZH | ZH | `03_evaluation_rules/EVAL_PROTOCOL_ZH.md` | `174f80cbfb8f814f239ca912bfcfaaf827bb10e6cb7b15e87aae91687106a9b4` |
| JUDGE_PROMPT_EN | EN | `03_evaluation_rules/JUDGE_PROMPT.md` | `6511ae8c32326c1a7f0f209236dbddc7baf2d55ab36ce84888b03f7ad816d3c4` |
| JUDGE_PROMPT_ZH | ZH | `03_evaluation_rules/JUDGE_PROMPT_ZH.md` | `38fa7142a4bb05310ea065d96dcbd44f91413330b6e6c1d0e92dc22493bf59d4` |

## How to verify (one command)

From repo root:

```bash
sha256sum -c VERSION_MAP.sha256
```

Expected: all entries show `OK`.

## How to bump the version

1. Duplicate your intended changes **only** into the canonical artifact files above.
2. Update the `PDL_VERSION` header inside each artifact.
3. Recompute SHA256 and update both `VERSION_MAP.md` and `VERSION_MAP.sha256`.
4. Re-run one end-to-end evaluation and store a new `runs/YYYY-MM-DD_.../summary/` row that references the new version.
