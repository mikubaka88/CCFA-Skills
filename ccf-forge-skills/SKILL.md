---
name: ccf-forge-skills
description: "Design, create, update, and validate Codex skills in local .codex/skills folders. Use when the user wants to create a new skill, improve an existing SKILL.md, turn repeated workflows/domain knowledge/tool usage into reusable skills, decide whether to add scripts/references/assets, avoid name conflicts, write Chinese or bilingual skill instructions, scaffold and verify a skill end to end, or maintain CCFA技能, 更新skill, 添加中文触发词, 优化联动, quick/standard模式."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Forge Skills

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Follow `metadata.ccf_skill_controls.handoff_question_mode` and `../ccf-common/references/handoff-modes.md` when maintaining the CCFA skill family.

When maintaining the CCFA skill family, preserve `metadata.ccf_skill_controls` in each `SKILL.md`. Do not add sibling-skill transitions without checking `../ccf-common/references/routing.md`, `../ccf-common/references/task-modes.md`, `../ccf-common/references/handoff-modes.md`, and the denylist-respecting fallback.

If the user disables a skill or asks for writing-only behavior, encode that boundary directly in the edited skill instructions. Do not weaken idea-scope protection in writing skills unless the user explicitly requests that policy change.

When adding sources, update `../ccf-common/references/source-registry.yaml` instead of duplicating URL lists in sibling skills. When adding browsing or evidence rules, keep them aligned with `../ccf-common/references/privacy-and-evidence.md`.

Never commit machine-specific absolute paths, usernames, expanded home directories, or private local directory names into skills, README files, source registries, diagrams, examples, scripts, or command snippets. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or placeholders that do not identify the user or machine.

## Core Rule

Build skills as compact operational guidance for another Codex session. Keep `SKILL.md` focused on trigger-relevant workflow, decisions, and resource navigation. Put detailed examples, checklists, schemas, policy text, or long instructions in `references/` and load them only when needed.

## Workflow

1. Clarify the goal with concrete examples. If the user's intent is clear, proceed with reasonable assumptions. Ask only for missing information that changes the skill's scope, location, or required assets.
2. Choose a skill name and destination. Use lowercase letters, digits, and hyphens only; keep names under 64 characters; check for conflicts in the target skills directory. Default to `$CODEX_HOME/skills`; if unset, use `~/.codex/skills`.
3. Decide the resource shape:
   - Use only `SKILL.md` for short, stable procedural guidance.
   - Add `references/` for detailed documentation that Codex should read selectively.
   - Add `scripts/` only for repeatable deterministic operations or fragile command sequences.
   - Add `assets/` only for templates, images, boilerplate, or other files used in final outputs.
4. Initialize the skill when creating from scratch. Prefer the local `skill-creator` initializer if available:

```powershell
python '<skill-creator-dir>/scripts/init_skill.py' <skill-name> --path '<skills-dir>' --resources references,scripts
```

5. Write `SKILL.md` before filling optional resources. Put all "when to use" trigger wording in the YAML `description`; the body is loaded only after trigger selection. Use imperative instructions and avoid user-facing tutorial prose.
6. Add resources that directly support the skill. Remove placeholder files and unused directories. Test any script by running it on a small representative example.
7. Validate and iterate. Run the available validator, then inspect manually for trigger quality, resource links, naming, and excessive context. Use realistic future prompts to decide whether the skill actually helps.
8. Run `ccf-common/scripts/check_path_privacy.py` before finishing CCFA-family maintenance. Replace any committed local absolute path or username with `$CODEX_HOME`, `$HOME`, a repo-relative path, or a non-identifying placeholder.

## Reference Files

Load these files only when the task calls for them:

- `references/design-checklist.md`: Use when planning a new skill, reviewing structure, or deciding whether content belongs in `SKILL.md`, `references/`, `scripts/`, or `assets/`.
- `references/patterns.md`: Use when drafting a concrete `SKILL.md` shape, frontmatter description, or example-driven workflow.
- `references/local-commands.md`: Use when scaffolding or validating skills on this machine, especially in PowerShell or Windows paths.

## Output Style

When creating a skill, give the user a concise scheme before editing, then create the files. After creation, report the skill name, location, key files, and validation result. If validation cannot run because a local dependency is missing, say exactly what failed and perform the manual checks from `references/design-checklist.md`.
