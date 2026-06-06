---
name: ccf-submission-checker
description: "Check CCF conference submission packages for LaTeX compilation, PDF metadata, page limits, anonymity, fonts, template compliance, supplementary files, and policy freshness. Use for submission readiness. Do not polish manuscript content."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Submission Checker

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Treat submission as a build-and-policy gate. Load venue guides for expected format, then require current official-policy verification for final decisions.

## Inputs

Project directory, TeX/PDF files, target venue/year, venue guide, and submission mode.

## Workflow

1. Identify quick or standard mode from the request, available artifacts, and deadline pressure.
2. Check `../ccf-common/references/skill-trigger-registry.yaml` for ownership boundaries before absorbing adjacent work.
3. Read `ccfa.yaml` when it exists. If absent, continue with supplied artifacts and report that project-state tracking is unavailable.
4. Execute only this skill's owned task. Mark missing evidence, stale venue rules, missing files, or authorization gaps explicitly.
5. Produce the output contract below and name the next owning skill when handoff is needed.

## Quick And Standard Modes

- Quick mode: answer the narrow request with the minimum relevant checklist and a compact risk note.
- Standard mode: produce the full table/checklist, artifact-state notes, boundary checks, and handoff recommendations.

## Output Contract

Pass/fail checklist, commands run, page/anonymity/font/template issues, official-policy freshness, and required fixes.

## Handoff

Use `ccf-venue-format-guide` for requirement lookup, `ccf-paper-compressor` for page overflow, and `ccf-paper-writer` only for content edits.

## Forbidden

Do not rewrite text, change claims, or silently relax official venue policy.
