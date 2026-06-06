<div align="center">

# CCFA Skills

### A governed `ccf-*` skill family for CCF/NeurIPS-style paper projects.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

</div>

---

CCFA Skills is a local Codex skill family for research-paper projects. The current v0.4 line intentionally reduces the runtime surface from many helper skills to 13 clear owners. Helper capabilities such as compression, writing review, citation audit, result figures, artifact packaging, venue format lookup, resubmission, paper talks, and docs SVG generation now live as modes or references inside their owning skills.

![Architecture](assets/ccfa-skills-architecture.svg)

## Install

Full install:

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

Partial install is supported, but always include `ccf-common`:

```bash
skills=(ccf-common ccf-paper-writer ccf-paper-reviewer ccf-submission-checker)
mkdir -p "$CODEX_HOME/skills"
for s in "${skills[@]}"; do cp -R "$s" "$CODEX_HOME/skills/"; done
```

PowerShell:

```powershell
$skills = @("ccf-common", "ccf-paper-writer", "ccf-paper-reviewer", "ccf-submission-checker")
New-Item -ItemType Directory -Force "$env:CODEX_HOME\skills" | Out-Null
foreach ($s in $skills) { Copy-Item -Recurse -Force $s "$env:CODEX_HOME\skills\" }
```

See [INSTALLATION_MATRIX.md](docs/INSTALLATION_MATRIX.md) before installing a subset.

## Runtime Skills

- `ccf-project-scaffolder`: creates the project directory, selects/copies templates, and initializes `ccfa.yaml`.
- `ccf-pipeline-orchestrator`: plans the workflow, decomposes tasks, coordinates gates, and chooses the next owner.
- `ccf-idea-optimizer`: turns a rough direction into a concrete problem-gap-insight-method-evidence plan.
- `ccf-idea-reviewer`: scores, compares, ranks, and triages early ideas.
- `ccf-literature-searcher`: searches related work, prior art, datasets, benchmarks, and citation evidence.
- `ccf-experiment-designer`: designs experiments and builds real-result tables/figures without inventing numbers.
- `ccf-paper-writer`: drafts, revises, polishes, compresses, preserves source format during edits, creates venue-aware LaTeX drafts from ideas, and presentation-adapts manuscript text.
- `ccf-paper-reviewer`: reviews scientific quality, writing quality, format-facing risks, reviewer scores, and AC/meta-review.
- `ccf-integrity-auditor`: audits claims, numbers, figures/tables, citations, BibTeX, and citation-context support.
- `ccf-submission-checker`: checks venue rules, templates, page/anonymity, LaTeX/PDF package, metadata, and artifacts.
- `ccf-rebuttal-writer`: writes rebuttals, response letters, revision ledgers, and conservative resubmission plans.
- `ccf-common`: shared routing, privacy/evidence policy, source registry, and artifact contracts.
- `ccf-skill-forger`: maintains skills, routing, docs, generated SVG diagrams, validation, and releases.

## Family Flow

```text
ccf-project-scaffolder
  -> ccf-pipeline-orchestrator
  -> ccf-idea-optimizer -> ccf-idea-reviewer
  -> ccf-literature-searcher -> ccf-experiment-designer
  -> ccf-paper-writer
  -> ccf-paper-reviewer -> ccf-integrity-auditor
  -> ccf-submission-checker
  -> ccf-rebuttal-writer

Governance: ccf-common / ccf-skill-forger
```

![Workflow](assets/ccfa-skills-workflow.svg)

## Merged Helpers

Do not install these as standalone runtime skills: `ccf-workflow-planner`, `ccf-paper-compressor`, `ccf-writing-reviewer`, `ccf-citation-auditor`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-venue-format-guide`, `ccf-resubmission-adapter`, `ccf-paper-presenter`, `ccf-doc-diagram-designer`.

Their capabilities are still present:

- compression and talks -> `ccf-paper-writer`
- writing review -> `ccf-paper-reviewer`
- citation audit -> `ccf-integrity-auditor`
- result figures/tables -> `ccf-experiment-designer`
- venue format and artifacts -> `ccf-submission-checker`
- resubmission -> `ccf-rebuttal-writer`
- docs SVGs -> `ccf-skill-forger`

## Venue Guides

Venue-specific LaTeX/template notes are reference material:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-paper-writer` for venue-aware manuscript text and `ccf-submission-checker` for venue compliance and package checks. For from-scratch manuscript writing, `ccf-paper-writer` reads the target venue guide first; if the guide is missing or no venue is provided, it drafts with the NeurIPS LaTeX fallback.

## Demo

`demo/attention-is-all-you-need/` is a complete ICLR-style closed-loop run. It reads the original Transformer paper, extracts the idea, reviews it, writes a full compiling LaTeX manuscript, runs writing/scientific review, audits integrity, checks submission readiness, drafts rebuttal text, and records remaining CCFA family issues.

![Attention Demo](assets/ccfa-skills-demo-attention.svg)

## Diagrams

![Catalog](assets/ccfa-skills-catalog.svg)

![Routing](assets/ccfa-skills-routing.svg)

![Artifacts](assets/ccfa-skills-artifacts.svg)

![Installation](assets/ccfa-skills-installation.svg)

![Review Boundaries](assets/ccfa-skills-review-boundaries.svg)

Detailed docs: [SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md), [ARCHITECTURE.md](docs/ARCHITECTURE.md), [INSTALLATION_MATRIX.md](docs/INSTALLATION_MATRIX.md), [NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md).
