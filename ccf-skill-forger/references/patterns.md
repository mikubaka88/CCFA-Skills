# Skill Patterns

## Minimal Workflow Skill

Use this when the skill mainly guides a repeated process.

```markdown
---
name: review-contracts
description: "Review contract drafts for risk, missing terms, inconsistent definitions, and negotiation notes. Use when the user asks Codex to inspect, summarize, revise, or compare contract text or contract files."
---

# Review Contracts

## Workflow

1. Identify contract type, parties, governing law, and user objective.
2. Read the full document before suggesting edits.
3. Separate legal-risk findings from style or clarity suggestions.
4. Cite exact clauses or section names when possible.
5. Ask for jurisdiction-specific confirmation before giving high-stakes advice.
```

## Reference-Backed Skill

Use this when domain details are too long for `SKILL.md`.

```text
skill-name/
  SKILL.md
  references/
    schema.md
    metrics.md
    examples.md
```

In `SKILL.md`, state when to read each file:

```markdown
## References

- `references/schema.md`: Read before writing SQL or interpreting table relationships.
- `references/metrics.md`: Read when the user asks for revenue, retention, or activation metrics.
- `references/examples.md`: Read when writing a query similar to prior reports.
```

## Script-Backed Skill

Use this when repeated code would otherwise be rewritten.

```text
skill-name/
  SKILL.md
  scripts/
    transform_input.py
```

In `SKILL.md`, include:

- What the script does.
- Required inputs and outputs.
- A small command example.
- A requirement to run the script on a representative sample after editing it.

Avoid scripts for simple one-off shell commands. Prefer scripts for fragile parsing, file format manipulation, validation, or repeatable conversions.

## Asset-Backed Skill

Use this when the skill should copy or modify reusable files.

```text
skill-name/
  SKILL.md
  assets/
    template.pptx
    frontend-starter/
```

In `SKILL.md`, explain which assets to use and how to adapt them. Do not paste the asset contents into `SKILL.md`.

## Description Formula

Use this shape for strong trigger descriptions:

```text
<Primary capability>. Use when the user asks to <verbs>, <verbs>, or <verbs> for <domain/files/tools>, including <specific scenarios>.
```

Examples:

- `Create and maintain project release notes. Use when the user asks to draft, update, summarize, or standardize changelogs from git history, PR descriptions, issue lists, or milestone notes.`
- `Build reusable Codex skills. Use when the user asks to create, update, validate, or refactor a SKILL.md package with scripts, references, assets, or trigger descriptions.`

## Common Anti-Patterns

- Hiding trigger conditions in the body instead of the `description`.
- Writing a tutorial for humans rather than operational instructions for Codex.
- Adding all optional directories by default.
- Duplicating the same information in `SKILL.md` and `references/`.
- Creating long nested reference chains that require multiple hops to discover.
- Including broad advice that any strong model already knows.
