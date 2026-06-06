---
name: ccf-artifact-reproducibility
description: "Prepare reproducibility and artifact packages for CCF submissions: artifact checklist, code/data/model release plan, environment files, seeds, hardware notes, licenses, README structure, and reproducibility appendix. Use for artifact evaluation and reproducibility sections. Do not claim reproducibility without evidence."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Artifact Reproducibility

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Convert actual project assets into an honest artifact plan. Distinguish released, internal, restricted, and unavailable materials.

## Inputs

Code/data/model status, experiment scripts, environment, licensing constraints, and target venue artifact policy.

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

Artifact checklist, release plan, README outline, reproducibility notes, and unresolved blockers.

## Handoff

Use `ccf-experiment-designer` for missing protocols and `ccf-submission-checker` for package compliance.

## Forbidden

Do not promise data/code release that the user has not authorized or cannot legally provide.
