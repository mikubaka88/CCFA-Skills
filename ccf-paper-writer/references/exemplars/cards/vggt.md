# VGGT

Venue/year: CVPR 2025.
Venue family: CVPR.
Custom status: user-custom writing-format exemplar. This card participates in the default custom writing format when the user does not specify a target venue. VGGT is also recorded separately as the CVPR 2025 Best Paper in `cards/cvpr-2025-vggt-best-paper.md`, but this card remains the user-custom writing source.
Source: `paper_ref/VGGT_ Visual Geometry Grounded Transformer.pdf`; CVF `https://openaccess.thecvf.com/content/CVPR2025/html/Wang_VGGT_Visual_Geometry_Grounded_Transformer_CVPR_2025_paper.html`.
Use when: writing feed-forward vision, 3D reconstruction, multi-task prediction, model simplicity, or replacement of iterative pipelines.

## Story Pattern

The paper begins from a classic pipeline with strong priors and heavy optimization, then asks whether modern neural networks can directly solve the same family of tasks. The contribution is framed as a simpler feed-forward model that predicts many related 3D attributes together and competes with specialized or optimization-based systems.

## Abstract Moves

- Define the model by outputs first: cameras, point maps, depth, and tracks.
- Make scale flexibility explicit: one view, few views, or hundreds of views.
- Contrast simplicity and speed against post-processing-heavy alternatives.
- Close by extending the value beyond the main tasks: pretrained features help downstream tasks.

## Introduction Moves

- Start from the historical baseline and why it still dominates.
- Pose a sharp capability question rather than only listing limitations.
- Position related work as partial progress, then identify what still requires post-processing.
- Argue that standard transformers plus enough 3D-annotated data may be sufficient.
- Summarize contributions around model, direct usability, post-processing compatibility, and benchmark breadth.

## Method Moves

- State problem inputs and outputs before architecture details.
- Use over-complete prediction as a training/evidence idea: related outputs can improve each other even if some are mathematically connected.
- Explain architectural restraint as a virtue, then isolate the few necessary design choices.

## Evidence Moves

- Benchmark across several tasks to prove generality.
- Compare both direct outputs and outputs with optional refinement.
- Include in-the-wild qualitative figures that reveal where optimization methods are brittle.

## Reusable Techniques

- Use "direct prediction of a family of outputs" as a unifying paper story.
- Make simplicity reviewer-facing: fewer special components can be a claim if evidence is broad.
- Let one overview figure show input/output breadth and runtime contrast.

## User Notes

This is one of the user's recognized exemplars. Use it for papers that want to claim a simple model can replace a complicated classical pipeline.

## Do-Not-Copy Boundary

Do not borrow the exact visual-geometry task list, transformer framing, or speed comparison unless the user's method and experiments support them.
