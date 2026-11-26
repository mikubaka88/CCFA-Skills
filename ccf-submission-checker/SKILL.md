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

## Shared Files And Preflight

Reuse one established task directory, default `ccfa-workfiles/<purpose>/<artifact-id>/`; preserve inputs, update in place, and check UTF-8/Chinese text. Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md) before every task. Reuse applicable active rules; refresh changed or lost ones. Common's artifact and **PARTIAL** handoff contracts govern naming, cleanup and necessary contributions under one owner. Preserve the metadata controls; do not duplicate intake or reports.

## Core Rule

Treat submission as a build, venue-policy, page-budget, and artifact-readiness gate. Use local venue guides for expected rules, then require official-policy freshness for final decisions. Do not rewrite paper content.

## Modes

- `venue-format`: template, page limit, anonymity, author block, supplementary and camera-ready rules.
- `package-check`: LaTeX/PDF build, metadata, fonts, page count, file structure, and submission checklist.
- `artifact`: code/data/model release plan, environment, seeds, hardware, licenses, artifact README, and reproducibility appendix.
- `full`: venue + package + artifact.

## Workflow

1. Identify venue/year/track, submission mode, project directory, TeX/PDF files, supplementary/artifact files, and deadline pressure.
2. Read `ccfa.yaml` when available. If absent, proceed with supplied files; report only missing information that affects a requested check.
3. For venue questions, read `../ccf-paper-writer/references/venue-guides/index.md` and the specific guide as navigation. Apply format, page and anonymity rules only from a verified official source matching the venue/year/track/stage; reuse a current verified result. Legacy guide examples cannot override a supplied verified template. Resolve a real mismatch against the target official requirements before changing the manuscript.
   - For ICML 2027, use [the venue guide](../ccf-paper-writer/references/venue-guides/icml.md) and `scripts/check_icml2027.py`. Check the primary contribution type and the Impact and AI Disclosure Statements.
4. For package checks, inspect the actual TeX/PDF/build output, page accounting for the exact venue/year/track, anonymity, fonts, metadata, references, and applicable required forms. For CVPR 2027, use the complete `CVPR/2027` bundle and the matched guide's eight-page main-text budget, required LLM Usage Statement placement, anonymity and enrollment/quota checks. Use `scripts/check_cvpr2027.py` for local TeX/PDF checks; it cannot establish author enrollment, disclosure truth or official-review AI authorization. For ICLR 2027, retain its distinct template, stage budget and AI-use statement/form rules. Unconfirmed facts remain not verified. Read logs and affected pages; do not infer a successful build from file presence.
   - For ACL 2027, use [the venue guide](../ccf-paper-writer/references/venue-guides/acl.md) and `scripts/check_acl2027.py`. Check the chosen ARR long/short track and separate ARR review from ACL commitment.
5. For artifact checks, build a reproducibility checklist: code, data, models, environment, seeds, hardware, license, access restrictions, and README.
6. Route actual findings or authorized fixes through their owners: paper writer for needed text/page revisions, visual composer for figure/table layout defects, and rebuttal writer for post-review response packaging. A paper within the page budget does not automatically need polishing. For a reproducibility gap, distinguish missing documentation, configuration, code, and scientific evidence: research engineer handles implementation or reproduction work, and experiment designer resolves a comparison or protocol question. A missing checklist item alone does not require a new experiment.

For edition profiles linked in a venue guide, run its documented local preflight and inspect the manual checks.

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
