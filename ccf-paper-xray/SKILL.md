---
name: ccf-paper-xray
description: "Read one supplied paper closely enough to reconstruct how its authors actually got there. Use for 精读论文, 讲透这篇论文, 把这篇读懂, 作者为什么这么设计, 这个公式怎么推出来的, paper-xray, and deep single-paper comprehension before building on, reviewing, or presenting that paper. Recovers the real starting point and the bet the authors placed, separates load-bearing design from decoration, grounds each key formula in a worked micro-example, and checks the evidence boundary skeptically. Distilling writing patterns belongs to ccf-paper-to-exemplar; manuscript assessment and scores belong to ccf-paper-reviewer; finding literature belongs to ccf-literature-searcher; rendering figures belongs to ccf-visual-composer."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# Paper X-Ray

## Family File Contract

Before writing, resolve the canonical output and one stable working directory per task/artifact. Reuse explicit or established task paths; otherwise use project-root `ccfa-workfiles/<purpose>/<artifact-id>/`, with `source/`, `assets/`, `cache/`, and `build/` only as needed. Update current files in place; do not scatter intermediates or create iteration copies. Preserve inputs and required evidence; clean only verified disposable files created by this task. Use UTF-8 text I/O and check Chinese text after saving or rendering. For file work, apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) and reuse the same paths across skill transitions.

## Collaboration Contract

Before specialist execution, read and apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md). At every handoff, reuse their applicable active rules or refresh missing/changed ones. Both preflights are required even without prose; detailed editing, experiment, and maintenance modes run only when relevant.

Keep one integrating owner and actively use other skills to resolve missing prerequisites or check material findings. Reuse applicable evidence; do not skip necessary groundwork to save tokens. Before finalizing, integrate contributions and verify affected results. Follow the conditional [cooperation routes](../ccf-common/references/routing.md); avoid unrelated stages and duplicate reports.

## Scope And Shared Controls

Own the comprehension of one supplied paper. Produce the understanding the downstream skill needs, not the downstream artifact.

This skill owns: the reconstructed research path, the load-bearing/decoration judgement, worked micro-examples for the key formulas, and the evidence-boundary read. It does not own manuscript prose (`ccf-paper-writer`), review verdicts and scores (`ccf-paper-reviewer`), claim/number/citation audit against verified evidence (`ccf-integrity-auditor`), literature discovery (`ccf-literature-searcher`), writing-pattern extraction (`ccf-paper-to-exemplar`), experiment design (`ccf-experiment-designer`), or figures (`ccf-visual-composer`).

Reading sets no verdict. Forming an assessment of a manuscript is `ccf-paper-reviewer` even when a full PDF is supplied; this skill reports what the paper does and how far its evidence reaches, and never labels a paper accepted, rejected, or scored.

Follow `../ccf-common/references/handoff-modes.md`, `../ccf-common/references/task-modes.md`, and `../ccf-common/references/artifact-contracts.md`. Preserve a no-new-files request by returning the reading in context. Do not treat the paper's own abstract, introduction narrative, or contribution list as the record of what the authors did; those are post-hoc framing.

## Workflow

1. Identify the source, its version, the requested depth, and the authorized destination. Reuse a completed reading when the same source version and scope already match; a new version invalidates only the affected sections.
2. Read the whole paper, including appendix, footnotes, figure and table captions, and supplementary material. The appendix is where unfavorable ablations, real hyperparameter search ranges, and reviewer-response material usually live. When only a PDF is supplied, inspect actual pages for equations, figures, and reading order instead of relying on extracted text alone.
3. Reconstruct the research path. Name the concrete failure the work reacts to, and the bet the authors placed on their strongest evidence. If the paper does not state a motive, say the paper does not state it rather than supplying one. Record any place where the body and the appendix disagree.
4. Separate load-bearing design from decoration. For each distinctive component, state whether removing it collapses the result or merely accompanies it, and cite the ablation, appendix, or comparison that settles it. With no such evidence, write that the paper does not run that control.
5. Ground the mathematics. Give every symbol its shape and meaning, and follow each key formula with a worked micro-example with concrete numbers carried to the end. Load [deep-reading-protocol.md](references/deep-reading-protocol.md) for the full reading checklist, the worked-example standard, and the evidence-boundary review list.
6. Check the evidence boundary: agreement between body numbers and figures/tables; whether baselines share data, steps, and tuning budget; whether hyperparameters were selected on the test set; preprocessing leakage; cost, latency, and the conditions under which the conclusion stops holding. Preserve the source's hedging strength and write "the paper does not report this" instead of a plausible substitute.
7. Return the reading in the destination the request authorized, with the reconstructed path, the load-bearing judgement, the worked examples, and the evidence boundary. Name open gaps explicitly. Report the reading's scope (which sections, appendix, supplementary) rather than implying full coverage when coverage was partial.
8. Keep the output separate from the paper's own text. Do not reproduce the source at length; quote only what an anchor requires.

## Handoff

Pass the source identity and version, the reconstructed path, the elements judged load-bearing, the worked micro-examples, and the evidence gaps.

- To `ccf-paper-writer`: the mechanism and the evidence boundary to preserve when writing related work or positioning.
- To `ccf-idea-optimizer`: the gap the paper leaves open, as a starting point, not as an assessed idea.
- To `ccf-paper-reviewer`: the reading as input; the review verdict, scores, and report remain with the reviewer.
- To `ccf-literature-searcher`: named open questions to search against, not a substitute for retrieval.

Do not present the reading as a review, a score, or a novelty verdict, and do not extend it into manuscript edits without the owning skill.
