<div align="center">

# CCFA Skills

### A governed `ccf-*` skill family for CCF/ICLR/NeurIPS-style paper projects.

<p>
  <strong>English</strong> ·
  <a href="README.zh-CN.md">简体中文</a> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<img src="assets/ccfaskills.png" alt="CCFA Skills visual identity" width="100%">

</div>

---

CCFA Skills is a local Codex skill family for research-paper projects. The v0.4.5 line keeps the runtime surface small: 13 owner skills cover the full paper lifecycle, while former helper skills are now modes inside the correct owner. The goal is not to make every request trigger a different skill; the goal is to keep idea, evidence, writing, review, submission, rebuttal, and governance connected without conflicts.

![Skill family logic](assets/ccfa-skills-architecture.svg)

## Family Logic

The normal closed loop is:

```text
project scaffold
  -> workflow orchestration
  -> idea optimization and idea review
  -> literature and experiment evidence
  -> venue-aware manuscript writing
  -> scientific/writing review and integrity audit
  -> submission package check
  -> rebuttal, revision ledger, and possible resubmission
```

`ccfa.yaml` is the shared project state. It records the target venue, stage, artifacts, claims, experiments, reviews, submission checks, and revision ledger so skills can hand off without overwriting each other.

![Workflow](assets/ccfa-skills-workflow.svg)

## Runtime Skills

| Stage | Skill | Owns | Usually hands off to |
| --- | --- | --- | --- |
| Setup | `ccf-project-scaffolder` | Project folders, LaTeX template, initial `ccfa.yaml`. | `ccf-pipeline-orchestrator`, `ccf-paper-writer` |
| Planning | `ccf-pipeline-orchestrator` | Stage plan, gates, artifact status, next owner. | Any stage owner |
| Idea | `ccf-idea-optimizer` | Problem-gap-insight-method-evidence shaping. | `ccf-idea-reviewer`, `ccf-literature-searcher` |
| Idea gate | `ccf-idea-reviewer` | Strict idea scoring, ranking, reject-risk triage. | `ccf-idea-optimizer`, `ccf-experiment-designer` |
| Evidence | `ccf-literature-searcher` | Prior art, related work, datasets, benchmarks. | `ccf-experiment-designer`, `ccf-paper-writer` |
| Evidence | `ccf-experiment-designer` | Baselines, metrics, ablations, real result tables/figures. | `ccf-paper-writer`, `ccf-integrity-auditor` |
| Manuscript | `ccf-paper-writer` | Drafting, revision, polishing, compression, presentations, venue-aware LaTeX. | `ccf-paper-reviewer`, `ccf-submission-checker` |
| Review | `ccf-paper-reviewer` | Scientific review, writing review, score/risk report, AC/meta-review. | `ccf-paper-writer`, `ccf-integrity-auditor` |
| Audit | `ccf-integrity-auditor` | Claim support, numeric consistency, citation/BibTeX/context audit. | `ccf-paper-writer`, `ccf-literature-searcher` |
| Submission | `ccf-submission-checker` | Venue rules, PDF/LaTeX build, anonymity, metadata, artifacts. | `ccf-paper-writer`, `ccf-rebuttal-writer` |
| Response | `ccf-rebuttal-writer` | Rebuttal, response letter, revision ledger, conservative resubmission. | `ccf-paper-writer`, `ccf-submission-checker` |
| Governance | `ccf-common` | Routing, privacy/evidence policy, source registry, artifact contracts. | All CCFA skills |
| Maintenance | `ccf-skill-forger` | Skill edits, docs, generated SVGs, validation, release work. | `ccf-common` |

![Catalog](assets/ccfa-skills-catalog.svg)

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

![Installation](assets/ccfa-skills-installation.svg)

## Merged Helper Modes

Do not install these names as standalone runtime skills: `ccf-workflow-planner`, `ccf-paper-compressor`, `ccf-writing-reviewer`, `ccf-citation-auditor`, `ccf-figure-table-builder`, `ccf-artifact-packager`, `ccf-venue-format-guide`, `ccf-resubmission-adapter`, `ccf-paper-presenter`, `ccf-doc-diagram-designer`.

Their capabilities still exist:

| Old helper capability | Current owner |
| --- | --- |
| Compression, paper talks, poster/slides/Q&A | `ccf-paper-writer` |
| Writing review | `ccf-paper-reviewer` |
| Citation audit | `ccf-integrity-auditor` |
| Result figures/tables | `ccf-experiment-designer` |
| Artifact package and venue format check | `ccf-submission-checker` |
| Resubmission adaptation | `ccf-rebuttal-writer` |
| Documentation SVG maintenance | `ccf-skill-forger` |

![Routing](assets/ccfa-skills-routing.svg)

## Venue Guides

Venue-specific LaTeX/template notes are reference material, not standalone runtime skills:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-paper-writer` for venue-aware manuscript text. Use `ccf-submission-checker` for venue compliance, page limits, anonymity, PDF metadata, camera-ready details, and artifact readiness. If a from-scratch writing request names a target venue, the writer reads the venue guide first; if the venue is absent or unspecified, it falls back to the NeurIPS template.

## Demo

`demo/attention-is-all-you-need/` is a complete ICLR-style closed-loop demo. It reads the original Transformer paper, extracts the idea, reviews the idea, writes a compiling LaTeX manuscript, runs writing/scientific review, audits integrity, checks ICLR submission readiness, drafts rebuttal text, and records remaining CCFA family issues.

![Attention Demo](assets/ccfa-skills-demo-attention.svg)

## Diagrams And Docs

![Artifacts](assets/ccfa-skills-artifacts.svg)

![Review Boundaries](assets/ccfa-skills-review-boundaries.svg)

Detailed docs: [SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md), [ARCHITECTURE.md](docs/ARCHITECTURE.md), [INSTALLATION_MATRIX.md](docs/INSTALLATION_MATRIX.md), [NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md).
