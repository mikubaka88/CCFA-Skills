---
name: ccf-figure-table-builder
description: "Build and audit publication figures, LaTeX tables, SVG/PDF assets, captions, result formatting, and visual QA from supplied real experimental results. Use for figure/table generation and result presentation. Do not invent numbers or experimental outcomes."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Figure Table Builder

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Only visualize supplied data. Preserve units, metrics, seeds, uncertainty, and dataset names; mark missing values explicitly.

## Inputs

Result tables, logs, CSV/JSON files, desired venue style, and target figure/table role.

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

Generated table/figure artifacts or source snippets, caption draft, QA checklist, and data-provenance notes.

## Handoff

Use `ccf-experiment-designer` for missing evaluation design and `ccf-integrity-auditor` for result-to-claim audit.

## Forbidden

Do not fabricate values, hide negative results, or overstate statistical meaning.
