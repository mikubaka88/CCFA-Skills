---
name: ccf-submission-checker
description: "Check CCF venue rules and submission packages: template, pages, anonymity, PDF build, metadata, and reproducibility. Use for 投稿检查, 会议格式, page limits, and artifact readiness. Verify current official rules for the exact venue/year/track. Manuscript polishing belongs to ccf-paper-writer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Submission Checker

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Core Rule

Treat submission as a build, venue-policy, page-budget, and artifact-readiness gate. Use local venue guides for expected rules, then require official-policy freshness for final decisions. Do not rewrite paper content.

## Modes

- `venue-format`: template, page limit, anonymity, author block, supplementary and camera-ready rules.
- `package-check`: LaTeX/PDF build, metadata, fonts, page count, file structure, and submission checklist.
- `artifact`: code/data/model release plan, environment, seeds, hardware, licenses, artifact README, and reproducibility appendix.
- `full`: venue + package + artifact.

## Workflow

1. Identify venue/year/track, submission mode, project directory, TeX/PDF files, supplementary/artifact files, and deadline pressure.
2. Read `ccfa.yaml` when available. If absent, proceed with supplied files and state that project-state tracking is unavailable.
3. For venue questions, read `../ccf-paper-writer/references/venue-guides/index.md` and the specific venue guide before checking official freshness.
4. For package checks, inspect the actual TeX/PDF/build output, page accounting for the exact venue/year/track, anonymity, fonts, metadata, references, and applicable required forms. For ICLR 2027, apply the matched guide's year-specific template, stage-specific page budget, and AI-use statement/form checks; unconfirmed usage facts remain not verified. Read logs and affected pages; do not infer a successful build from file presence.
5. For artifact checks, build a reproducibility checklist: code, data, models, environment, seeds, hardware, license, access restrictions, and README.
6. Hand off to `ccf-paper-writer` for text/page rewrites: compression when over limit, substantive expansion when actual explanation is missing, and normal polishing when within budget. Hand off to `ccf-experiment-designer` for missing reproducibility experiments, `ccf-visual-composer` for figure/table float order, caption placement, font, clipping, palette, or visual readability fixes, and `ccf-rebuttal-writer` for post-review response packaging.

## Output Contract

```text
Mode:
Venue and rule freshness:
Files checked:
Pass/fail checklist:
Build/package issues:
Anonymity/page/font/metadata issues:
Length budget status:
Artifact/reproducibility issues:
Required fixes:
Next CCFA owner:
```

## Check Scope

Follow `../ccf-common/references/handoff-modes.md` and `../ccf-common/references/task-modes.md`. Run checks relevant to the requested mode and actual artifacts. Distinguish pass, fail, not applicable, and not verified; missing tools do not imply passing or failure. Record the official rule URL and the date checked. Reuse the project build configuration and place generated logs/previews in the established or shared task build directory. Update the canonical readiness report in place and distinguish old PDFs from successful current builds. Recheck only affected build surfaces after a fix. Underfilling a page budget alone is not a venue violation. Do not upload or submit files merely because a readiness check was requested.
