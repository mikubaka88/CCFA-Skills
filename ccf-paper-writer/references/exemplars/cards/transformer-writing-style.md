# Transformer Writing Style

Source: Vaswani et al., *Attention Is All You Need*, NeurIPS 2017.
Inspected version: arXiv:1706.03762v7, 2 August 2023, as identified on the stored PDF.
Local PDF: `references/exemplars/papers/1706.03762.pdf`.
Local text: `references/exemplars/papers/1706.03762.md`.
Use when: explaining a computational dependency, structural bottleneck, or change of modeling primitive.

The source observations below describe selected passages. Reusable Techniques gives adaptation advice; neither prescribes the new paper's section lengths or paragraph count.

## Story Pattern

**Source observation, Sections 1–2:** the paper introduces established recurrent sequence models, explains their sequential computation, and positions attention as a way to relate distant positions. The Transformer proposal changes the modeling primitive. Background discusses convolutional alternatives and path length before the architecture is developed.

The inspected Introduction has four paragraphs on PDF page 2. It ends with the proposed architecture and a training/result preview; it has no numbered contribution list. Related work appears in the Introduction and Background rather than a separate Related Work section. These facts correct the former generic outline; they are not recommendations to copy that organization.

## Abstract Moves

**Source observation, Abstract, PDF page 1:** the opening describes the dominant architectures and the role attention already plays. The proposal then names the changed architecture. Subsequent sentences report translation quality, training cost, and a parsing application. The abstract does not follow a five-sentence problem/gap/insight/components/results template.

**Adaptation advice:** make the relationship to the prior computational approach legible before describing performance. Report only the new work's supplied results; do not borrow the source's claims or numerical emphasis.

## Introduction Moves

**Source observation, Section 1, paragraph 2:** a sentence explains the recurrence between hidden states. The next links that dependence to sequential computation and the resulting restriction on parallelization. Later sentences distinguish improvements in efficiency from the remaining sequential constraint.

**Sentence-level technique:** the same scientific object carries the explanation from computation to constraint to consequence. The bottleneck is established through the operation, rather than announced with an abstract ability label.

**Adaptation advice:** use this progression when the supplied method actually has an explanatory dependency. A different task may need an observation, counterexample, or definition instead. Do not invent an impossibility claim to imitate the source.

## Method Moves

**Source observation, Section 3.2.1:** the text defines queries, keys, and values, states the dot-product, scaling, and softmax operations, and then gives the matrix expression. The later discussion explains the scaling choice through a proposed gradient-related account, with an explicit probabilistic assumption in the footnote.

**Source observation, Section 3.5:** positional encoding is introduced because the architecture needs sequence-order information. The passage separates the design rationale, the reported comparison with learned embeddings, and a possible extrapolation benefit. The possibility is not presented as a proven result.

**Adaptation advice:** place definitions and computations where they answer the reader's next question. Preserve the distinction between an explanation, a hypothesis, and an observed comparison. Parameters can appear in relevant prose; the source does not place all hyperparameters in a single table.

## Evidence Moves

**Source observation, Section 4 and Table 1:** the analytical comparison names per-layer complexity, sequential operations, and path length as distinct quantities. It then explains the conditions under which the comparisons apply.

**Source observation, Sections 5–6:** training settings, translation results, architecture variations, and parsing are described in their respective contexts.

**Adaptation advice:** choose the quantities that distinguish the new method's actual operation and explain their meaning. An analytical comparison and an empirical study answer different questions; neither is a mandatory companion to every contribution.

## Reusable Techniques

- Explain a computational dependence before deriving its consequence.
- Define the operation in prose before using a compact equation.
- Give a design choice its specific rationale without turning that rationale into an observed benefit.
- Introduce a comparison quantity together with the scientific question it answers.
- Keep standard technical terms and justified uncertainty, including when the original uses negation or hedging.

For an original hypothetical adaptation of the dependency-to-consequence technique, see `references/exemplar-style-analysis.md`.

## Do-Not-Copy Boundary

The architecture, task, equations, comparisons, and findings belong to the source. Transfer the explanatory relationship only when the new material supports it. Do not copy source sentences with substituted nouns or present adaptation advice as a fact about the paper.
