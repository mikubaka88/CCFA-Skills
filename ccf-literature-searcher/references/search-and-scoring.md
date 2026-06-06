# Literature Search And Scoring

Use this file for source selection, source-quality exclusions, paper classification, and quality scoring.

## Source Tiers

Preferred primary sources:

- Official proceedings or publisher pages: ACL Anthology, CVF Open Access, PMLR, ACM Digital Library, IEEE Xplore, USENIX, VLDB, OpenReview, AAAI/OJS, SIAM, Springer/LIPIcs when venue-appropriate.
- Stable paper records: arXiv, DBLP, Semantic Scholar, OpenAlex, Crossref, DOI landing pages, project pages, benchmark leaderboards, and dataset pages.
- Strong journals and transactions when the field is journal-centered: JMLR, TPAMI, TOG, TKDE, TDSC, TOSEM, TSE, TODS, CACM, IEEE/ACM Transactions, Nature/Science family only when relevant.

Discovery sources are allowed for finding candidates, but final claims should point to a stable paper page or proceedings page whenever possible.

## Hard Exclusions

Exclude:

- MDPI domains, journals, proceedings, PDFs, and special issues.
- Predatory or low-signal venues with no clear review standard.
- Untraceable PDFs without title, authors, venue, or stable link.
- Papers whose only accessible evidence is a search snippet.

If an excluded paper appears important because the user specifically named it, report that it is excluded by policy and ask whether they want a separate user-directed note. Do not include it in the scored candidate table.

## Search Strategy

Use several query forms:

```text
"<task>" "<method>" benchmark
"<task>" "<closest baseline>" "dataset"
"<problem phrase>" site:openaccess.thecvf.com OR site:proceedings.mlr.press
"<method phrase>" OpenReview NeurIPS ICLR ICML
"<topic>" DBLP SIGMOD SIGCOMM SOSP CCS CHI PLDI STOC
```

Prefer a mix of:

- recent papers from the last 2-4 years,
- one or two older anchor papers,
- closest baselines,
- benchmark/dataset papers,
- survey or taxonomy papers only when they clarify a field boundary.

## Opportunity Mapping

When the search is for early direction scouting, classify each cluster as one or more of:

- `crowded but open`: many papers exist, but a measurable failure mode, setting, or assumption remains weak.
- `covered central claim`: the same problem, mechanism, and evidence path are already present; the idea needs a new angle.
- `benchmark gap`: the field lacks a dataset, protocol, metric, stress test, workload, or evaluation standard.
- `mechanism gap`: papers report performance but do not explain why the method works or fails.
- `deployment/system gap`: real constraints, cost, latency, robustness, privacy, security, or user workflow are under-tested.
- `theory/analysis gap`: empirical results exist but formal understanding, bounds, or diagnostics are missing.
- `negative-result opportunity`: common assumptions fail, and a careful diagnostic or falsification paper may be valuable.

For every `covered central claim`, still report the best possible rescue route:

```text
What is covered:
Why direct novelty is weak:
Possible rescue route: new problem / new mechanism / new evidence / new venue / stop
Evidence needed to decide:
```

Do not conclude "the direction is dead" merely because the topic is popular. A direction is likely dead only when the user's central problem, mechanism, target setting, and evidence path are all already covered and no credible reframing remains.

## Paper-Type Taxonomy

Classify each included paper:

- `pure benchmark`: primary contribution is dataset, benchmark, workload, protocol, evaluation suite, or leaderboard.
- `pure method`: primary contribution is method, algorithm, model, system design, proof, or analysis.
- `method + benchmark`: introduces a method and a new dataset/benchmark/protocol that both matter.
- `survey`: synthesizes prior work.
- `system/tool`: primary contribution is implementation, infrastructure, deployment, or usable tool.
- `theory/proof`: primary contribution is theorem, bound, proof technique, or formal model.
- `other`: use only with a short explanation.

## Scoring

Use 1-5 anchors unless the user asks for another scale.

Score paper quality separately from idea viability. A high-quality close paper may reduce direct novelty while also revealing a better problem boundary, baseline, benchmark, or unresolved assumption. A low-quality paper should not be used as strong evidence that a direction is solved.

Insight:

- 5: clear, non-obvious insight that changes how the problem is understood.
- 4: strong idea with a specific mechanism or framing.
- 3: useful but incremental insight.
- 2: mostly engineering assembly or standard framing.
- 1: unclear or weak insight.

Completeness:

- 5: method/protocol/proof, evaluation, limitations, reproducibility, and positioning are all well covered.
- 4: strong coverage with minor missing details.
- 3: adequate but with visible gaps.
- 2: partial; important design or evidence details missing.
- 1: incomplete or hard to audit.

Experimental numeric evidence:

- 5: strong, fair, multi-setting numerical evidence with appropriate baselines and analysis.
- 4: solid numerical evidence with minor weaknesses.
- 3: adequate numbers but limited settings, baselines, or statistics.
- 2: weak numbers, narrow protocol, or unclear fairness.
- 1: numerical evidence absent or not meaningful for claims.
- `N/A benchmark`: use for pure benchmark papers; instead write a benchmark-quality note.

Benchmark-quality note for `pure benchmark`:

```text
Benchmark scope:
Task realism:
Metric validity:
Baseline coverage:
Adoption or reproducibility signal:
Known limitation:
```

Overall quality label:

- `A`: high-priority close work.
- `B`: useful supporting or baseline work.
- `C`: background only or weak fit.
- `Risk`: must inspect because it may undercut novelty.

Do not convert scores into acceptance probability.
