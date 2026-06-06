<h1 align="center">CCFA Skills</h1>

<p align="center"><strong>A skill family for shaping the research storyline of CCF-A papers.</strong></p>

<p align="center">
  <a href="README.md">简体中文</a> ·
  <strong>English</strong> ·
  <a href="README.zh-TW.md">繁體中文</a>
</p>

<p align="center">
  <img src="assets/ccfaskills.png" alt="CCFA Skills visual identity" width="100%">
</p>

---

> "The structure of the prose becomes the structure of the scientific argument."
> — George D. Gopen and Judith A. Swan, [*The Science of Scientific Writing*](https://www.cs.tufts.edu/comp/150FP/archive/george-gopen/sci.html)

A strong paper is rarely defined by the final PDF alone. What matters is the research storyline behind it: an unstable idea finds its position through literature, earns credibility through experiments, becomes a legible argument through writing, and is refined again through review and rebuttal. The hard part is not only drafting one introduction paragraph. The hard part is keeping the idea, evidence, experiments, narrative, and response aligned around the same research question.

CCFA Skills starts from that observation. It treats a CCF-A paper project as a research storyline that can be maintained, audited, and advanced over time, rather than as a one-shot text generation task. An idea should be shaped before it is defended. Experiments should serve explicit claims rather than merely fill tables. Writing should preserve evidence boundaries. A rebuttal should not be an improvised answer at the end of the process, but a traceable bridge to revision and resubmission.

The central insight is that paper quality comes from the quality of continuous decisions. Writing, review, integrity audit, submission checking, and rebuttal should not replace one another; they should keep separate responsibilities and hand off through the same project state. The v0.4.5 line therefore organizes the family into 13 stage roles, so each stage has a clear responsibility, each artifact has a home, and the system behaves more like a collaboration framework around the research storyline than a loose prompt collection.

![CCFA skill family logic](assets/ccfa-skills-architecture.svg)

## Workflow

The default paper-project loop is:

```text
project scaffold
  -> workflow orchestration
  -> idea optimization
  -> idea review
  -> literature search
  -> experiment design
  -> venue-aware writing
  -> scientific/writing review
  -> integrity audit
  -> submission package check
  -> rebuttal / revision ledger / resubmission
```

`ccfa.yaml` is the shared project-state file. It records `target_venue`, `stage`, `artifacts`, `claims`, `experiments`, `reviews`, `revision_ledger`, and `submission_checks`, so skills can hand off without overwriting each other's files.

![Workflow](assets/ccfa-skills-workflow.svg)

## Runtime Skills

| Stage | Skill | Starts when | Main output | Do not use for |
| --- | --- | --- | --- | --- |
| Setup | `ccf-project-scaffolder` | Create a paper project, copy templates, initialize `ccfa.yaml`. | Project tree, template files, initial state. | Research content generation. |
| Planning | `ccf-pipeline-orchestrator` | Plan stages, gates, artifact status, next owner. | Workflow plan, gates, handoff. | Writing, review, search, experiments, rebuttal. |
| Idea shaping | `ccf-idea-optimizer` | Concretize a rough idea or vague direction. | Problem-gap-insight-method-evidence brief. | Ranking multiple ideas. |
| Idea gate | `ccf-idea-reviewer` | Score, rank, stress-test, or triage ideas. | Scores, risks, closest-prior-art concerns. | Developing one idea further. |
| Evidence | `ccf-literature-searcher` | Search related work, prior art, datasets, benchmarks. | Literature notes, evidence gaps, related-work structure. | Auditing already cited papers only. |
| Experiments | `ccf-experiment-designer` | Design baselines, metrics, ablations, robustness checks. | Protocols, baseline matrix, result templates, real-result tables. | Inventing results or drawing docs diagrams. |
| Manuscript | `ccf-paper-writer` | Draft, revise, polish, compress, create venue-aware LaTeX, make presentations. | Manuscript text, format-preserving edits, compressed text, slides/poster/talk. | Full review, integrity audit, submission check, rebuttal. |
| Review | `ccf-paper-reviewer` | Run scientific review, writing review, scoring, AC/meta-review. | Review report, risk table, revision priorities. | Rewriting the manuscript directly. |
| Integrity | `ccf-integrity-auditor` | Check claims, numbers, tables/figures, citations, BibTeX. | Claim-support table, numeric consistency report, citation audit. | Broad literature search or full paper review. |
| Submission | `ccf-submission-checker` | Check venue rules, pages, anonymity, PDF metadata, artifacts. | Submission package report, LaTeX/PDF build result, artifact checklist. | Polishing manuscript content. |
| Response | `ccf-rebuttal-writer` | Draft rebuttal, response letter, revision ledger, resubmission plan. | Rebuttal text, reviewer-response table, ledger. | Ordinary manuscript writing. |
| Governance | `ccf-common` | Maintain routing, evidence/privacy policy, source registry, artifact contracts. | Shared policy and validation controls. | Ordinary research tasks. |
| Maintenance | `ccf-skill-forger` | Maintain skills, docs, SVGs, validation, release. | Updated skills, docs, diagrams, release commits. | Research writing, review, experiments. |

![Runtime catalog](assets/ccfa-skills-catalog.svg)

## Routing Boundaries

| User intent | Use | Do not use |
| --- | --- | --- |
| Make a rough idea concrete | `ccf-idea-optimizer` | `ccf-idea-reviewer` |
| Score or rank ideas | `ccf-idea-reviewer` | `ccf-idea-optimizer` |
| Find new papers, datasets, benchmarks | `ccf-literature-searcher` | `ccf-integrity-auditor` |
| Verify already cited papers | `ccf-integrity-auditor` | `ccf-literature-searcher` |
| Design experiments and tables | `ccf-experiment-designer` | `ccf-paper-writer` |
| Draft, polish, compress, preserve source format | `ccf-paper-writer` | `ccf-paper-reviewer` |
| Judge acceptance risk | `ccf-paper-reviewer` | `ccf-paper-writer` |
| Check pages, anonymity, PDF, metadata, artifacts | `ccf-submission-checker` | `ccf-paper-writer` |
| Answer reviewers and maintain revision ledger | `ccf-rebuttal-writer` | `ccf-paper-reviewer` |
| Maintain docs diagrams or skills | `ccf-skill-forger` | `ccf-experiment-designer` |

![Routing boundaries](assets/ccfa-skills-routing.svg)

## Merged Helper Capabilities

Do not install these old names as standalone runtime skills:

```text
ccf-workflow-planner
ccf-paper-compressor
ccf-writing-reviewer
ccf-citation-auditor
ccf-figure-table-builder
ccf-artifact-packager
ccf-venue-format-guide
ccf-resubmission-adapter
ccf-paper-presenter
ccf-doc-diagram-designer
```

| Merged capability | Current owner |
| --- | --- |
| Workflow planning | `ccf-pipeline-orchestrator` |
| Compression, slides, poster, talk, Q&A | `ccf-paper-writer` |
| Writing review | `ccf-paper-reviewer` |
| Citation audit | `ccf-integrity-auditor` |
| Result figures/tables | `ccf-experiment-designer` |
| Artifact package and venue format | `ccf-submission-checker` |
| Resubmission adaptation | `ccf-rebuttal-writer` |
| Documentation SVGs | `ccf-skill-forger` |

## Artifact Contract

![Artifact contract](assets/ccfa-skills-artifacts.svg)

`ccfa.yaml` is a status spine, not the whole paper. Concrete outputs still live in idea briefs, literature notes, experiment plans, manuscripts, review reports, integrity audits, submission checks, and revision ledgers. Review and audit skills diagnose; writing changes go back to `ccf-paper-writer`.

## Output Policy

- Writing, polishing, compression, and presentation tasks should follow the user's requested output format.
- If the user provides LaTeX, preserve LaTeX; if the user provides Markdown, preserve Markdown.
- From-scratch manuscript requests read the target venue guide first; if missing, use the NeurIPS fallback.
- Non-review skills should produce concrete, information-dense artifacts.
- Review, audit, and submission-gate skills may remain more structured because their value is traceable diagnosis.
- No skill may invent results, citations, official rules, or reviewer conclusions.

![Review and audit boundaries](assets/ccfa-skills-review-boundaries.svg)

## Venue Guides

Venue-specific LaTeX/template information is reference material:

```text
ccf-paper-writer/references/venue-guides/index.md
ccf-paper-writer/references/venue-guides/<venue>.md
```

Use `ccf-paper-writer` for venue-aware manuscript writing. Use `ccf-submission-checker` for page limits, anonymity, PDF metadata, camera-ready checks, and artifact readiness.

## Install

Full install:

```bash
git clone https://github.com/mikubaka88/CCFA-Skills.git
mkdir -p "$CODEX_HOME/skills"
cp -R CCFA-Skills/ccf-* "$CODEX_HOME/skills/"
```

Partial install must include `ccf-common`:

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

![Installation sets](assets/ccfa-skills-installation.svg)

## Further Reading

To understand why the family is designed this way, read these in order:

| Document | When to read it |
| --- | --- |
| [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) | Understand the main chain, governance layer, artifact state, and revision loop. |
| [docs/SKILLS_CATALOG.md](docs/SKILLS_CATALOG.md) | Check each skill's startup condition, boundary, and common conflict cases. |
| [docs/INSTALLATION_MATRIX.md](docs/INSTALLATION_MATRIX.md) | Decide which skills are required for partial installation. |
| [docs/NAMING_AND_MERGE_AUDIT.md](docs/NAMING_AND_MERGE_AUDIT.md) | Understand why helper skills were merged and how naming conflicts were reduced. |
| [AGENT_GUIDE.md](AGENT_GUIDE.md) | Operational guide for owner selection, artifact handoff, and overwrite avoidance. |
| [demo/attention-is-all-you-need/](demo/attention-is-all-you-need/) | See a complete ICLR-style closed-loop example. |

## Demo

`demo/attention-is-all-you-need/` is an optional ICLR-style closed-loop demo showing idea extraction, idea review, LaTeX writing, review, integrity audit, submission check, and rebuttal.

![Attention demo](assets/ccfa-skills-demo-attention.svg)

## Validation

```bash
python ccf-common/scripts/check_v04.py
python ccf-common/scripts/check_markdown_links.py
python ccf-common/scripts/check_sources.py
python ccf-common/scripts/check_path_privacy.py .
python tools/build_ccfa_diagrams.py
```
