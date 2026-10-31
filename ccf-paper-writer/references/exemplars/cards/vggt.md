# VGGT

Venue/year: CVPR 2025.
Venue family: CVPR.
Custom status: user-recognized exemplar available for a matching writing question. Selecting its relevant original passage does not activate the whole custom format; that format still follows the user's request or established preference.
Source: `paper_ref/VGGT_ Visual Geometry Grounded Transformer.pdf`; CVF `https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html`.
Inspected local source: `references/exemplars/papers/cvpr-2025-vggt.pdf`, CVF open-access accepted version; corresponding extraction `references/exemplars/papers/cvpr-2025-vggt.md`.
Award context remains in `cards/cvpr-2025-vggt-best-paper.md`.
Use when: explaining feed-forward geometry, related prediction outputs, or the relationship between direct prediction and iterative refinement.

The observations below describe selected source passages. Reusable Techniques gives adaptation advice.

## Story Pattern

**Source observation, Section 1:** the paper describes the continued role of visual geometry and iterative optimization, asks whether a neural network can solve the tasks directly, and relates the proposal to recent pairwise reconstruction methods. The argument connects the proposed input/output behavior to the remaining role of post-processing.

## Abstract Moves

**Source observation, Abstract, PDF page 1:** the opening names the model, states the prediction operation, lists concrete output quantities, and specifies the range of input views. Subsequent sentences discuss performance across tasks and downstream use.

**Sentence-level technique:** the definition is carried by the model's operation and its objects. The output list gives substance to the broader claim about 3D attributes.

**Adaptation advice:** define a new method through the outputs and input conditions relevant to the user's work. Do not borrow this paper's task list, input range, speed, or performance claim.

## Introduction Moves

**Source observation, Section 1, from the opening through the contribution paragraph:** the text moves from classical reconstruction and hybrid learned systems to the remaining computational role of geometry. The capability question then introduces direct prediction. Later paragraphs distinguish joint prediction during training from how predicted quantities can be used during inference.

**Adaptation advice:** establish the actual computation that motivates a new formulation. A direct-prediction story is useful only when the supplied method changes that computation; model simplicity alone does not establish a new capability.

## Method Moves

**Source observation, Sections 3.1–3.3:** the method defines inputs and predicted quantities before introducing the backbone and heads. Section 3.1 distinguishes tracking features from tracks produced by the tracking module. It also discusses the relationship among geometrically connected outputs.

**Adaptation advice:** define what the representation contains and what each subsequent computation derives from it. Do not collapse intermediate features and final outputs into one attractive capability claim.

## Evidence Moves

**Source observation, Sections 4.1–4.5:** the paper reports task-specific comparisons and ablations. Its camera-pose comparison distinguishes feed-forward predictions from predictions followed by bundle adjustment; Section 4.5 examines architectural and prediction choices.

**Adaptation advice:** preserve comparison configurations and explain which question each result answers. Results on multiple tasks support the evaluated task coverage; they do not prove unrestricted generality.

## Reusable Techniques

- Name concrete inputs and outputs when defining a broad model.
- Explain how a computational dependency motivates the proposed formulation.
- Distinguish training targets, intermediate features, direct outputs, and optional inference refinement.
- Tie a simplicity claim to the actual operations removed or retained.
- Organize results by the scientific differences among comparisons, without importing a fixed experiment package.

## User Notes

This is one of the user's recognized exemplars. Select its relevant passage when the current writing question concerns related output quantities, direct prediction, or refinement.

## Do-Not-Copy Boundary

The visual-geometry task list, transformer design, input range, runtime, and measured advantages belong to VGGT. The new manuscript must use its own design and results. The source's award is context, not a reason to strengthen a claim.
