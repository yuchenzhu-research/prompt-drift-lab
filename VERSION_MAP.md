# VERSION_MAP (v3)

This file freezes the **canonical evaluation contract artifacts** for *Prompt Drift Lab*.

## Bundle metadata

- **Bundle tag:** v3
- **Frozen date:** 2026-01-07
- **Scope:** the hash-locked files below are the minimum set needed to (a) interpret prompts, (b) apply the evaluation contract, and (c) verify integrity of those contracts used by the released results.
- **Versioning policy:**
  - **Behavioral** changes to the evaluation contract (rules / scoring / required schemas) ⇒ bump **major or minor** and regenerate SHA256.
  - **Editorial / packaging** changes (README, folder notes, wording that does not change evaluation behavior) ⇒ stay within the same major bundle (v3.x if tagged).

## Canonical artifacts (hash-locked)

| Artifact ID | Lang | Path | SHA256 |
|---|---|---|---|
| PROMPT_MANIFEST_EN | EN | `02_prompt_variants/PROMPT_MANIFEST.md` | `b41263003a003871ec58cc67ed75137cfc061d5630de51a5c87910010f9cd6ab` |
| PROMPT_MANIFEST_ZH | ZH | `02_prompt_variants/PROMPT_MANIFEST_ZH.md` | `75e3f253ddcd60187763b35fae8fbefd75fa03933257e8f3dcddb4ac98d67b2f` |
| EVAL_PROTOCOL_EN | EN | `03_evaluation_rules/EVAL_PROTOCOL.md` | `a11da0d75ffa334ad6fecc966418b7ddf48e0d362d7e7a204360f9ecd79a4227` |
| EVAL_PROTOCOL_ZH | ZH | `03_evaluation_rules/EVAL_PROTOCOL_ZH.md` | `ba82d6f870246ba2afc315ae68cf2d0754486540b84f9be499dc8c4f282572bc` |
| JUDGE_PROMPT_EN | EN | `03_evaluation_rules/JUDGE_PROMPT.md` | `09a46b67af647a974f392f48fb826fd3c5e5860a79338679b2cf9aeef198d148` |
| JUDGE_PROMPT_ZH | ZH | `03_evaluation_rules/JUDGE_PROMPT_ZH.md` | `c95f4c06f8f28646cec7c4063950df43693a949d403660032575349998b94e93` |

## How to verify (one command)

From `supplement/supplement_min/`:

```bash
sha256sum -c VERSION_MAP.sha256
```

Expected: every line shows `OK`.

## Notes on non-canonical folders (01/05/06/07)

Folders `01_experiment_design/`, `05_summary_and_outlook/`, `06_methodological_addenda_and_controls/`, and `07_deep_research/` are **supporting materials**.  
They are included for reviewer convenience and audit trail, but are **not** part of the hash-locked evaluation contract above.
