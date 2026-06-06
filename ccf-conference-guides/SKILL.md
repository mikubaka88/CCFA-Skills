---
name: ccf-conference-guides
description: "Conference venue LaTeX, page-limit, anonymity, template, camera-ready, and format requirement lookup for CCF paper submissions. Use when the user asks about CVPR/NeurIPS/ICML/ICLR/AAAI/ACL/SIGMOD/KDD/SIGCOMM/CCS/CHI or similar venue formatting, official template paths, page limits, double-blind rules, author blocks, supplementary material, rebuttal templates, or camera-ready checklists. Do not use for writing, polishing, full review, or rebuttal content; route those to the owning CCFA skill."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Conference Guides

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/skill-trigger-registry.yaml`.

Treat private manuscripts, reviews, drafts, results, code, and project state as private user material. Do not browse with private text unless the user authorizes it or the shared privacy/evidence policy allows a safe transformed query.

## Core Rule

Answer venue-format questions through the v0.4 venue guide branch. Load `../ccf-writing-skills/references/venue-guides/index.md` first, then the specific venue file. Before final submission advice, require a current official-policy check because migrated guides are not a substitute for official rules.

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

Route content writing to `ccf-writing-skills`, writing/format critique to `ccf-conference-writing-reviewer`, package checks to `ccf-submission-checker`, and rebuttal content to `ccf-conference-paper-rebuttal`.

## Forbidden

Do not rewrite manuscript text, invent current policy, or treat migrated guide content as final official policy.
