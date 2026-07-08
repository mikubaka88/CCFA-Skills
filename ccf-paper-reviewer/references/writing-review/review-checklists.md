# Writing Review Checklists

Use this file to prevent omissions during manuscript writing review, paragraph-by-paragraph writing review, LaTeX/format audit, and writing revision planning.

## Intake Checklist

- Target venue, year, track, and paper type are stated, or generic CS conference writing review is explicitly assumed.
- Manuscript scope is stated: abstract only, section, main paper, full paper, appendix, TeX source, reviews, or revised draft.
- Requested mode is selected: quick writing scan, standard writing review, paragraph-by-paragraph review, LaTeX/format audit, consistency audit, or revision planning.
- Missing materials that affect confidence are named.
- Current-year official rules are checked when the user asks for latest policy, page limits, templates, anonymization, or compliance.

## Full Writing Review Checklist

- The paper's intended story is summarized in one sentence.
- Abstract, introduction, contribution list, headings, figures/tables, and conclusion are read before local paragraph comments.
- Contributions are stated as the paper claims them and checked for specificity, overlap, and evidence support.
- High-impact paragraphs receive IDs and local diagnoses.
- Paragraph issues are tied to role, takeaway, logic, evidence, redundancy, and concrete edit action.
- Global motivation and problem-gap-root-challenge chain are checked.
- Claim-evidence alignment is included for major claims.
- Quantitative writing scorecard is produced when enough text is available.
- Writing-review panel roles are run independently before synthesis in standard mode.
- Terminology, notation, datasets, models, and contribution wording are checked across sections.
- Prose quality guardrails are checked: no defensive/incremental framing, label-heavy shorthand, number-only abstracts, formula dumping, third-person manuscript voice, punctuation-driven structure, unsupported hype, or overlong compound sentences.
- Related work is checked for closest-work positioning, not citation-list volume.
- Figures/tables/captions/equations/algorithms are checked when present.
- LaTeX/source/template issues are checked when source or snippets are available.
- Weaknesses are ranked by severity and converted into concrete revision actions.
- Checklist status is reported.

## Paragraph-By-Paragraph Checklist

- Paragraph IDs are assigned by section.
- Each high-impact paragraph has a current role and desired reviewer takeaway.
- A paragraph is flagged when it mixes multiple jobs.
- Unsupported claims are tied to the exact missing citation/result/proof/example/qualification.
- Repeated material is marked as cut, merge, move, or appendix candidate.
- Transitions between paragraphs are checked for causal order.
- Sentence rhythm and syntax are checked so paragraphs do not become mechanically uniform.
- Edit actions are concrete: keep, reorder, split, merge, cut, move, qualify, expand, or rewrite.

## LaTeX / Format Checklist

- Template/class/style and anonymity/camera-ready mode match the stated venue when known.
- Sectioning, abstract, appendix, acknowledgments, bibliography, and supplemental material follow the expected structure.
- Labels, refs, citations, and bibliography commands are checked for missing, duplicate, or stale items.
- Figures and tables have readable sizing, self-contained captions, and text references.
- Equations and notation are introduced before use and remain consistent.
- Algorithms use variables that match the method text.
- Manual spacing hacks, excessive resizing, and style-breaking overrides are flagged.
- Compilation status is stated as compiled / inspected only / not available.

## Quick Writing Scan

Use this compact structure when the user only wants a quick diagnosis:

```text
Scope:
Quick verdict:
Main reviewer confusion:
Top 3 writing risks:
Exact edit actions:
Unresolved materials:
Checklist status:
```

## Revision Planning Checklist

- Every material writing weakness has a revision action.
- Each action has a fix class: writing-fixable, structure-fixable, claim-qualification, citation/positioning, figure/table, LaTeX/format, compression, requires-new-result, accepted-limitation, or venue-mismatch.
- Actions requiring new experiments, proofs, baselines, or studies are separated from writing-only fixes.
- Required edits identify where to revise.
- Claims to weaken, move, support, or remove are listed.
- Risk-reduction condition is tied to reviewer confusion or format compliance.

## Scientific Review Redirect

If the user explicitly asks for paper scoring, simulated reviewers, AC/meta-review, full scientific review, novelty/soundness/evidence review, or acceptance-style risk, stop the writing checklist and route to `ccf-paper-reviewer` under the CCFA handoff mode.

## Minimal Checklist Status

```text
Checklist status:
- Venue/assumptions:
- Reading scope:
- Quantitative scorecard:
- Writing-review panel:
- Paragraph IDs:
- Storyline:
- Prose quality:
- Claim-evidence:
- Consistency:
- LaTeX/format:
- Revision actions:
- Unresolved:
```
