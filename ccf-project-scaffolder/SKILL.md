---
name: ccf-project-scaffolder
description: "Initialize CCF project folders, LaTeX templates, artifact directories, and ccfa.yaml. Use for 项目初始化, 目录搭建, template setup, and reproducible workspace scaffolding. Preserve existing files. Workflow planning belongs to ccf-pipeline-orchestrator; research content belongs to its specialist owner."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Project Scaffolder

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode`, `../ccf-common/references/handoff-modes.md`, and `../ccf-common/references/task-modes.md`. A scaffold request authorizes the necessary local structure; a dry-run or no-new-files request limits changes accordingly.

## Core Rule

Create the requested project structure, template, and state without inventing research content. Preserve existing user files and complete compatible missing pieces instead of replacing an established project.

## Workflow

1. Resolve the project location, venue, requested folders, and existing artifacts from the conversation and filesystem. Infer routine directory names; ask only about a consequential unresolved location or overwrite choice.
2. Select the matching template through `../ccf-paper-writer/references/venue-guides/index.md`. Verify that the template and its supporting style/assets are available. Use supplied templates when requested; identify unavailable dependencies precisely instead of copying an incomplete template.
3. Resolve final artifacts and the working root through `../ccf-common/references/artifact-contracts.md`. Create only needed directories and templates, with source/assets/cache/build subdirectories on demand. Preserve existing layout; do not migrate user files or overwrite a manuscript, bibliography, or configuration to refresh a scaffold.
4. If `ccfa.yaml` is absent and initialization is requested, copy `assets/ccfa.yaml`, preserve the required fields in `../ccf-common/references/ccfa-yaml-contract.md`, and fill only supplied project metadata. Existing state is read and updated only within the requested scope; unknown research fields remain explicit placeholders.
5. Check the created paths, template references, and YAML. A build is useful when a runnable template was requested and an engine is available; do not run research experiments or final submission checks for directory setup.
6. Report the actual created/updated paths and any concrete missing dependency. For a dry run, return the proposed tree and actions without writing files.

## Boundaries

Use `../ccf-common/references/artifact-contracts.md` for file ownership. Project workflow planning belongs to `ccf-pipeline-orchestrator`, manuscript prose to `ccf-paper-writer`, and final package checks to `ccf-submission-checker`. Do not invent a title, abstract, claim, experiment, or citation.
