# Transformer Writing Style

Source: Vaswani et al., "Attention Is All You Need," NeurIPS2017.
Paper PDF: `references/exemplars/papers/1706.03762.pdf`

Use when: writing architecture papers, backbone-replacement papers, or papers whose main contribution is changing the fundamental modeling primitive rather than adding a module to an existing pipeline.

## Actual Section Lengths (from the published paper)

| Section | Approx. Pages | Characterization |
| --- | --- | --- |
| Abstract |0.2 | Concise: problem, gap, method, evidence. |
| Introduction |1.2 | Broad hook, specific gap, insight, architecture summary, contributions, paper roadmap. |
| Background |0.7 | Formal problem statement, notation, why path length matters. |
| Model Architecture |3.0 | The largest section. Every component motivated individually: attention, multi-head, FFN, embeddings, positional encoding. Each subsection has: motivation, equation, explanation, why it works. |
| Why Self-Attention |0.5 | Analytical justification: complexity comparison table, path-length analysis. |
| Training |0.3 | Dataset, hardware, schedule — just enough to justify claims. |
| Results |1.5 | Main BLEU table, comparison table, ablations table, training curves. |
| Related Work |1.0 | Organized by paradigm, not by chronology. Each subsection contrasts directly with the gap the paper fills. |
| Conclusion |0.3 | Restates insight and evidence, no new claims. |

Total: ~8.7 pages main text,2.3 pages references + appendix.

## Story Pattern

The paper starts from a widely understood problem (sequence transduction), identifies a structural bottleneck in existing solutions (sequential computation), introduces a clean conceptual shift (attention as backbone), supports it with both theoretical analysis (path length) and empirical evidence (WMT BLEU), and concludes with bounded claims.

## Section-by-Section Writing Moves

### Abstract
- Sentence1: Problem and importance.
- Sentence2: Gap in existing methods.
- Sentence3: Core insight and method name.
- Sentence4: Architecture components.
- Sentence5: Headline evidence (numbers).

### Introduction
- Paragraph1: Task importance and broad motivation.
- Paragraph2: Existing methods and their limitations (structural, not just empirical).
- Paragraph3: Root cause of the limitation — why existing methods cannot address it.
- Paragraph4: Insight and proposed method (named here).
- Paragraph5: Architecture summary (one sentence per component).
- Paragraph6: Evidence preview.
- Paragraph7: Contributions list (numbered).
- Paragraph8 (optional): Paper structure.

### Method
- Each subsection: motivation first, then equations, then explanation.
- Motivation answers: "Why is this component needed, given the gap described in the Introduction?"
- Equations are clean and self-contained.
- Hyperparameters are in a table, not scattered in text.

### Experiments
- Setup: dataset sizes, preprocessing, hardware.
- Main results: a clean table with bold best results.
- Complexity analysis: a theoretical table that supports the architectural claim.
- Ablations: each row tests one design choice against a specific claim.
- Training efficiency: wall-clock time to support the parallelism claim.

### Related Work
- Organized by paradigm: recurrent, convolutional, attention-based, efficient methods.
- Each paragraph: paradigm name, key papers, limitation relative to this work, how this work differs.
- Ends with the closest gap.

## Reusable Techniques

- Make the structural bottleneck explicit (not just "others do worse").
- Name the method early in the Introduction.
- Every method component has a clear "why" before the "how".
- Pair analytical evidence (complexity table) with empirical evidence (BLEU table).
- Keep ablation rows directly tied to design choices listed in Method.
- Use bold for best results — one convention throughout.

## Do-Not-Copy Boundary

Do not reuse the specific architecture, equations, motivation framing, or reported numbers unless the user's paper genuinely supports them. This card provides writing moves and structural patterns, not content to copy.