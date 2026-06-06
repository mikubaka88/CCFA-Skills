---
name: ccf-venue-format-guide
description: "Look up and summarize CCF conference LaTeX templates, page limits, anonymity rules, author blocks, supplementary rules, rebuttal templates, and camera-ready format requirements. Use for venue format questions such as CVPR page limit or NeurIPS template. Do not write, polish, review, or rebut paper content."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Venue Format Guide

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Answer venue-format questions through the v0.4 venue guide branch. Load `../ccf-paper-writer/references/venue-guides/index.md` first, then the specific venue file. Before final submission advice, require a current official-policy check because migrated guides are not a substitute for official rules.

## Inputs

Target venue/year, question type, draft/template path if available.

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

Venue requirement summary, template path, risk notes, official-policy freshness status, and handoff target if the request is actually writing/review/rebuttal.

## Handoff

Route content writing to `ccf-paper-writer`, writing/format critique to `ccf-writing-reviewer`, package checks to `ccf-submission-checker`, and rebuttal content to `ccf-rebuttal-writer`.

## Forbidden

Do not rewrite manuscript text, invent current policy, or treat migrated guide content as final official policy.
