# Manuscript Review Formats

Use `detailed` by default. Use `brief` only when the user explicitly asks for 简要版, 简短, 快速概览, 只给结论, brief, concise, or a restrictive length/output format. A short prompt, a single manuscript, narrow subject matter, or no-score request does not by itself select brief output. Report detail is independent of review scope and execution depth: a detailed writing review still assesses writing only.

These formats organize review scope, substantive findings, ratings, and revision priorities. Use the exact numbered headings below in Chinese, English, or the displayed bilingual form; do not rename, reorder, merge, or invent peer sections. Render report sections as `## 1. ...`, with lower-level headings for findings and tables. Preserve an explicit venue form or user schema; state that override instead of claiming the default format was validated.

Record `Template: ccfa-review-1`, mode, detail level, rubric (`generic-7`, writing, inherited comparison, or named venue form), source version, and contribution type in the initial scope block. This identifies the report contract without changing the skill release version. Unknown metadata is not a reason to stop. One report uses one profile; its depth does not change the selected scientific, writing, or concept-only scope.

## Detailed Version — Default

For scientific/full and detailed version-comparison review, retain all fourteen sections below. Inapplicable or unassessed sections keep their heading and a short reason referring to the initial scope note. Develop applicable sections with concrete manuscript content, evidence locations, and decision consequences; do not fill missing scope with invented checks or reduce substantive sections to generic sentences. Keep stable concern IDs so later sections refer to findings without repeating them.

### 1. 评审信息与范围 / Review Information

Identify title, venue/year/track if known, review mode, source version, materials inspected, and source coverage. State the actual assessed scope and group unavailable materials here. Unknown metadata is not an intake blocker.

### 2. 总体结论与关键理由 / Expected Review Outcome

Lead with the evidence-supported stance and the reasons that decide it. Separate positive contribution value from unresolved blockers and give a confidence summary. Derive the verdict after examining the findings; do not assign a target score and manufacture reasons.

### 3. 预审与投稿适配 / Desk Rejection Assessment

Assess applicable venue fit, reviewability, and verified submission requirements. Use pass, concern, or not assessed. A desk-reject concern requires a relevant rule and evidence; unknown page count, anonymity, or appendix information is not failure. Continue substantive review where possible.

### 4. 论文摘要与贡献拆解 / Summary And Contributions

Explain the problem, proposed mechanism, contribution type, and claimed findings without mixing in criticism. Distinguish the main contribution from supporting components and identify the paper's central claims.

### 5. 主要优势 / Strengths

Give separately numbered strengths with specific manuscript anchors and explain their scientific importance. Include every consequential merit found; do not manufacture praise or impose a quota. When none can be substantiated, explain the scope of that judgment briefly.

### 6. 主要问题与严重程度 / Major Concerns

Use the fixed finding record below for each consequential concern. Before retaining a major or critical concern, inspect the cited passage and relevant supplied appendix, then look for the strongest evidence that would invalidate the criticism. Record what was checked and whether the concern survived, narrowed, or was withdrawn. A missing input is a scope limit, not a confirmed defect.

### 7. 次要问题与写作表达 / Minor And Presentation Concerns

Identify local clarity, terminology, organization, notation, and figure/table narration issues with locations and concrete edit directions. Explain how they affect understanding. Do not recast the same scientific defect as several additional writing deductions or rewrite manuscript prose.

### 8. 新颖性与相关工作 / Novelty And Positioning

Compare decisive closest work, stating verified overlap and the remaining difference. Identify searched, supplied, or unverified sources and distinguish unavailable retrieval from demonstrated low novelty.

| Work / source | What it already establishes | Overlap and remaining difference | Consequence / concern ID |
| --- | --- | --- | --- |

If browsing is forbidden and no sources were supplied, state the resulting coverage limit once; do not invent comparison rows.

### 9. 方法正确性与主张支撑 / Soundness And Claim Support

Examine assumptions, method logic, derivations, causal arguments, or system guarantees. Map the central claims to their actual support and explain gaps or contradictions.

| Claim / location | Inspected support | Judgment | Consequence / concern ID |
| --- | --- | --- | --- |

Check the strongest support as well as the strongest counterexample. Missing source material is not automatically missing evidence in the full paper.

### 10. 实验、证明与可复核性 / Evaluation And Reproducibility

Use evidence expectations appropriate to the paper type: experiments, proofs, workloads, or user studies. Explain the adequacy of decisive comparisons and protocols, statistical treatment where relevant, and material reproducibility details. Theory papers do not inherit compulsory empirical checklists. Separate primary evidence gaps from optional extensions; connect each requested change to a central claim.

### 11. 多视角评审与综合意见 / Reviewer Perspectives And Synthesis

Use `reviewer-panel.md` to present distinct observations and the best-supported, strongest favorable, and strongest substantiated critical interpretations. Show what each view actually inspected, its basis, and where views agree or differ. Finish with the decisive synthesis. They may agree; do not claim independent reviewers unless separate calls actually occurred.

### 12. 维度评分与置信度 / Critical Reviewer Ratings

Use the canonical seven-dimension table and order in `calibration-and-rank.md`, or a verified venue scale explicitly named in scope. Include evidence or concern IDs, deductions, change conditions, one overall score or stance, and confidence. Unassessed or inapplicable criteria are not zero. A verified unsupported central claim can justify a low Evidence score; an intentionally supplied excerpt cannot establish a whole-paper defect.

A detailed no-score request keeps qualitative criterion-by-criterion judgments and their basis. Without a real comparable corpus, omit ranks, percentiles, outperformed counts, and distribution plots.

### 13. 作者关键问题与改判条件 / Questions And Decision Conditions

List questions whose answers could resolve uncertainty or change the stance. Distinguish clarification, additional support for an asserted claim, and a substantive research change. Refer to concern IDs and state the answer or change that would affect the judgment; do not promise acceptance or a guaranteed score increase.

### 14. 修改优先级与复审记录 / Action Priorities And Re-Review

Consolidate next actions in one table, preserving issue identity across revisions:

| ID | Priority / severity | Required change | Why it matters | Status / version |
| --- | --- | --- | --- | --- |

Separate decisive fixes from useful refinements. Add an owner only for a needed handoff. For version comparison, use `version-comparison.md`: retain the frozen contract, relative-progress scorecard with historical/current/delta/weights, a separate absolute-readiness scorecard, issue provenance, traceable decreases, and confidence/comparability. In section 12 use the subheadings `### Relative Progress / 相对进步`, `### Absolute Readiness / 绝对成熟度`, and `### Confidence And Comparability / 置信度与可比性`, in that order. Put issue changes here; never merge the two scores or replace inherited comparison dimensions with the new generic rubric.

## Writing Detailed Profile

Writing-only review uses these nine sections in this order. Scientific review of an excerpt still uses the fourteen-section profile, marking unassessed parts; an excerpt alone does not turn scientific judgment into writing review. A brief input limits findings, not the default detail level.

### 1. 评审信息与范围 / Review Information

State the text and presentation material inspected, writing-only scope, source version, and applicable formatting rules. Group excluded scientific criteria here.

### 2. 写作结论与关键理由 / Writing Outcome

Give the writing judgment and the main reader-facing reasons. Do not give a scientific acceptance recommendation.

### 3. 论证与结构重建 / Argument And Structure

Reconstruct the intended story, section roles, and claim-evidence presentation without rewriting prose or evaluating unrequested research quality.

### 4. 主要优势 / Strengths

Identify supported writing strengths with locations; do not manufacture praise.

### 5. 写作问题与严重程度 / Writing Concerns

Use the finding record for located problems in logic, organization, terminology, captions, or source formatting. Place requested paragraph/LaTeX audit tables inside this section.

### 6. 读者视角与综合意见 / Reader Perspectives And Synthesis

Consolidate reader perspectives using the same concern IDs, accurately labeling simulated and independent work.

### 7. 写作评分与置信度 / Writing Ratings

Use `writing-review/writing-review-rubric.md`, including its assessed-weight denominator. Honor no-score requests. A writing composite is not an acceptance score.

### 8. 作者关键问题与改判条件 / Questions And Decision Conditions

Ask only questions that can resolve the identified writing uncertainties, referring to concern IDs.

### 9. 修改优先级与复审记录 / Action Priorities And Re-Review

Give located edit actions, priorities, and status. Keep research changes outside writing-only scope unless separately requested.

## Brief Version — Explicit Request

Use these five numbered sections for an explicitly requested brief scientific, full, writing, or comparison review. The chosen mode still controls what may be assessed:

### 1. 结论 / Verdict

Stance, assessed scope, and compact report metadata.

### 2. 主要优点 / Strengths

The most consequential supported merits.

### 3. 关键问题 / Concerns

Decisive issues using compact finding records; omit repeated prose, not the evidence basis.

### 4. 评分概览与置信度 / Ratings

Applicable overall/criterion summary, or qualitative judgment when scores are excluded; material coverage limits. A brief comparison keeps the three comparison subheadings and separate scorecards, but may abbreviate their explanations.

### 5. 下一步 / Next Actions

Prioritized changes and the condition that would alter the verdict.

Keep the same evidence and fairness standards; brief does not mean ungrounded. Do not perform a shallower requested scientific review merely because its presentation is brief. If a user explicitly asks for a quick scan, preserve that execution scope and disclose the material coverage limit. A brief version comparison must still separate progress from readiness and retain a traceable basis for any score change.

## Finding Record

Define each concern once in the concerns section with a heading such as `### C001: Missing assumption in the claim`. Use `C001`, `C002`, etc. for new IDs; keep inherited IDs such as `R1` unchanged. Refer to definitions elsewhere with `[C001]`, including scorecards and action rows. Preserve a resolved issue's identity and compact record on re-review instead of renumbering or silently deleting it. Do not impose a finding, search, annotation, or reviewer-count quota.

Each record contains these fields on separate lines; labels may be English, Chinese, or bilingual. A short finding needs only short values. Minor concerns may use `not needed` for Countercheck with a reason; major/critical concerns state the actual countercheck or its coverage limit.

```text
Type / 类型: confirmed_flaw | unsupported_claim | clarification
Severity / 严重程度: critical | major | minor
Location / 位置: exact page/section/paragraph/line/figure/table anchor
Evidence / 证据: inspected basis, including source version when needed
Countercheck / 反证复核: strongest answer/counterevidence checked and the result
Judgment / 判断: consequence for the claim or reader; no inferred defect from missing input
Criterion / 维度: affected criterion or writing dimension
Resolution / 解决或改判条件: feasible answer/change that would resolve or alter the finding
Status / 状态: unresolved | partially_resolved | resolved | not_applicable
```

`confirmed_flaw` requires an observed error or contradiction; `unsupported_claim` concerns support for an actual asserted claim; `clarification` is an unresolved question. Types are not interchangeable with severity, confidence, or revision provenance. Keep provenance fields from `version-comparison.md` when comparing versions. For major findings, try to disprove the objection before deciding the score; remove or narrow it if the manuscript already answers it. Reuse inspected passages and references rather than performing a fixed number of searches or full rereads.

## Deterministic Report Check

For a saved default-format report, run the existing script directly on Markdown; it writes no files:

```text
python ccf-paper-reviewer/scripts/validate_version_comparison.py report.md --report --mode scientific
python ccf-paper-reviewer/scripts/validate_version_comparison.py report.md --report --mode writing --detail brief --no-scores
```

The check covers section names/order, finding fields and ID references, and generic scorecard structure/ranges/statuses. It does not verify scientific correctness, source truth, severity, or review completeness. For a CCFA-shaped report with verified venue-specific ratings, add `--rubric external`; rating semantics then require inspection against that venue form. An exact external/user layout is outside this default-template checker and must be checked against its own schema, never forced into these headings. The old JSON comparison API/CLI remains available without `--report`; no JSON sidecar is required.

## Persistence

When a report file is requested or in scope, update its canonical Markdown file. Generate one version unless both are requested. Switching detailed/brief updates the existing report; do not create parallel copies, a JSON sidecar, or per-role files by default. Keep real source versions required for comparison under the existing artifact policy.
