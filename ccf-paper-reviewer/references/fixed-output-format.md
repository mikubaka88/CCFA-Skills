# Manuscript Review Formats

Use `detailed` by default. Use `brief` only when the user explicitly asks for 简要版, 简短, 快速概览, 只给结论, brief, concise, or a restrictive length/output format. A short prompt, a single manuscript, narrow subject matter, or no-score request does not by itself select brief output. Report detail is independent of review scope and execution depth: a detailed writing review still assesses writing only.

These formats organize review scope, substantive findings, ratings, and revision priorities. Translate headings to the user's language. Preserve an explicit venue form or user schema.

## Detailed Version — Default

For scientific/full manuscript review, use the following numbered sections. Develop the reasoning within each applicable section using concrete manuscript content, evidence locations, and decision consequences. Do not reduce a detailed report to headings, a score table, or one generic sentence per section. Keep stable concern IDs so later sections can discuss implications without repeating the full criticism.

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

Develop each consequential concern under a stable ID. Include the exact location or claim, inspected evidence, why it affects the conclusion, severity, and what would resolve it. Distinguish a demonstrated defect, an unsupported asserted result, and an unanswered question. Verify that the relevant section or supplied appendix does not already answer the objection.

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

Use the applicable venue scale or `calibration-and-rank.md`. Include dimension scores, evidence or concern IDs, deductions, change conditions, one overall score or stance, and confidence. Unassessed or inapplicable criteria are not zero. A verified unsupported central claim can justify a low Evidence score; an intentionally supplied excerpt cannot establish a whole-paper defect.

A detailed no-score request keeps qualitative criterion-by-criterion judgments and their basis. Without a real comparable corpus, omit ranks, percentiles, outperformed counts, and distribution plots.

### 13. 作者关键问题与改判条件 / Questions And Decision Conditions

List questions whose answers could resolve uncertainty or change the stance. Distinguish clarification, additional support for an asserted claim, and a substantive research change. Refer to concern IDs and state the answer or change that would affect the judgment; do not promise acceptance or a guaranteed score increase.

### 14. 修改优先级与复审记录 / Action Priorities And Re-Review

Consolidate next actions in one table, preserving issue identity across revisions:

| ID | Priority / severity | Required change | Why it matters | Status / version |
| --- | --- | --- | --- | --- |

Separate decisive fixes from useful refinements. Add an owner only for a needed handoff. For version comparison, use `version-comparison.md`: retain the frozen contract, relative-progress scorecard with historical/current/delta/weights, a separate absolute-readiness scorecard, issue provenance, traceable decreases, and confidence/comparability. Place the two scorecards in section 12 and the issue changes here; never merge them into one score.

## Scope-Specific Detailed Reports

Detailed output does not expand the authorized review. For writing-only or a narrow excerpt, retain the applicable sections: scope, conclusion, argument reconstruction, strengths, anchored issues, reader perspectives, qualitative/numeric writing criteria, questions, and priorities. Group excluded scientific/venue criteria in the initial scope note; do not fabricate sections about unprovided experiments or scientific acceptance. A brief input limits available findings, not the default output selection.

## Brief Version — Explicit Request

Use five compact blocks, unless an exact user format takes precedence:

1. **结论 / Verdict:** stance and assessed scope.
2. **主要优点 / Strengths:** the most consequential supported merits.
3. **关键问题 / Concerns:** the decisive issues with locations and severity.
4. **评分概览与置信度 / Ratings:** applicable overall/criterion summary, or qualitative judgment when scores are excluded; material coverage limits.
5. **下一步 / Next Actions:** prioritized changes and the condition that would alter the verdict.

Keep the same evidence and fairness standards; brief does not mean ungrounded. Do not perform a shallower requested scientific review merely because its presentation is brief. If a user explicitly asks for a quick scan, preserve that execution scope and disclose the material coverage limit. A brief version comparison must still separate progress from readiness and retain a traceable basis for any score change.

## Persistence

When a report file is requested or in scope, update its canonical Markdown file. Generate one version unless both are requested. Switching detailed/brief updates the existing report; do not create parallel copies, a JSON sidecar, or per-role files by default. Keep real source versions required for comparison under the existing artifact policy.
