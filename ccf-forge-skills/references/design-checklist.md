# Design Checklist

## Intake

Collect only the details that affect the skill:

- Goal: What task should future Codex sessions become better at?
- Triggers: What would the user naturally say that should activate this skill?
- Examples: What are 2-3 realistic requests the skill should handle?
- Inputs: Which files, APIs, tools, credentials, or domain facts are involved?
- Output: What should the completed work look like?
- Risk: What mistakes would be costly, destructive, or hard to notice?

If examples are missing, invent likely examples and proceed unless the domain is high-stakes or the wrong scope would create unwanted files, network calls, credentials, or destructive actions.

## Naming And Location

- Normalize names to lowercase hyphen-case, such as `pdf-redline` or `gh-pr-review`.
- Prefer short verb-led names when natural, such as `draft-contracts`, `query-metrics`, or `build-plugins`.
- Check the target directory before creating the skill.
- Avoid names that collide with system skills or are too broad, such as `helper`, `coding`, or `skill-creator`.
- Place personal skills in `$CODEX_HOME/skills` when set, otherwise `~/.codex/skills`.
- Do not write expanded home directories, usernames, drive-specific local paths, or machine-specific skill roots into committed files. Use `$CODEX_HOME`, `$HOME`, repo-relative paths, or non-identifying placeholders.

## Resource Decision

Choose the smallest structure that solves repeated work:

| Need | Put It In | Reason |
| --- | --- | --- |
| Short workflow or decision rules | `SKILL.md` | Loaded after trigger and cheap to read |
| Long docs, schemas, policies, examples | `references/` | Loaded selectively when needed |
| Repeatable or fragile operations | `scripts/` | Executable and deterministic |
| Templates, fonts, images, boilerplate | `assets/` | Used as files, not context |

Avoid `README.md`, changelogs, installation guides, or broad explanatory documents unless the runtime explicitly requires them. A skill is for agent execution, not general documentation.

## Frontmatter

For Codex skills, keep YAML frontmatter to:

```yaml
---
name: skill-name
description: "What the skill does and exactly when to use it."
---
```

For CCFA family skills, also preserve this metadata block unless the user explicitly requests a family-policy change:

```yaml
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
```

Make the `description` do all trigger work:

- Include task verbs and user phrases.
- Mention important file types, tools, platforms, or domains.
- Include update/review/validate triggers if the skill supports them.
- Do not rely on a "When to use" body section, because the body loads only after the skill is selected.

## Body

Keep the body actionable:

- Start with the operating principle or quick workflow.
- Use imperative instructions.
- Reference bundled resources with relative paths.
- Keep the main file under 500 lines.
- Move variant-specific details into one-level-deep files under `references/`.
- Include command snippets only when they are reusable and safe.

## Validation

Check these before finishing:

- Folder name equals frontmatter `name`.
- `name` uses only lowercase letters, digits, and hyphens.
- `description` is non-empty, specific, and trigger-rich.
- `SKILL.md` has no unfinished placeholders.
- Referenced files exist.
- CCFA family skills preserve the shared `ccf_skill_controls` keys and use `ccf-common` for routing, handoff, privacy, and source-registry policy.
- No committed file contains personal absolute paths, usernames, expanded local skill roots, or machine-specific command examples.
- `ccf-common/scripts/check_path_privacy.py` passes when run at the repository root.
- Optional directories contain only useful files.
- Scripts, if any, were executed on a representative example.
- `agents/openai.yaml`, if present, matches the skill and uses a correct `$skill-name` default prompt.
