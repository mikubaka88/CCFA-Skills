---
name: ccf-submission-checker
description: "Check CCF conference submission readiness: venue LaTeX/template/page/anonymity/camera-ready rules, LaTeX/PDF build, metadata, fonts, supplementary files, artifact/reproducibility package, code/data/model release plan, licenses, seeds, and policy freshness. Use for submission check, venue format, NeurIPS/CVPR/ICML template/page limit, artifact package, 投稿检查, 会议格式. Do not polish manuscript content."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Submission Checker

## Core Rule

Treat submission as a build, venue-policy, and artifact-readiness gate. Use local venue guides for expected rules, then require official-policy freshness for final decisions. Do not rewrite paper content.

## Modes

- `venue-format`: template, page limit, anonymity, author block, supplementary and camera-ready rules.
- `package-check`: LaTeX/PDF build, metadata, fonts, page count, file structure, and submission checklist.
- `artifact`: code/data/model release plan, environment, seeds, hardware, licenses, artifact README, and reproducibility appendix.
- `full`: venue + package + artifact.

## Workflow

1. Identify venue/year/track, submission mode, project directory, TeX/PDF files, supplementary/artifact files, and deadline pressure.
2. Read `ccfa.yaml` when available. If absent, proceed with supplied files and state that project-state tracking is unavailable.
3. For venue questions, read `../ccf-paper-writer/references/venue-guides/index.md` and the specific venue guide before checking official freshness.
4. For package checks, inspect compile status, page count, anonymity, fonts, PDF metadata, template path, references, supplementary files, and required forms.
5. For artifact checks, build a reproducibility checklist: code, data, models, environment, seeds, hardware, license, access restrictions, and README.
6. Hand off to `ccf-paper-writer` for text/page rewrites, `ccf-experiment-designer` for missing reproducibility experiments, and `ccf-rebuttal-writer` for post-review response packaging.

## Output Contract

```text
Mode:
Venue and rule freshness:
Files checked:
Pass/fail checklist:
Build/package issues:
Anonymity/page/font/metadata issues:
Artifact/reproducibility issues:
Required fixes:
Next CCFA owner:
```
