---
name: ccf-visual-composer
description: "Render data analyses with Python and create or redraw scientific method, architecture and flow diagrams through a three-stage GPT Image workflow. Use for 数据分析图, quantitative and ablation plots, 绘图美化, 流程图, 架构图, 重绘, 排版 and existing-figure edits. Preserve selected templates, values and topology. Experiment protocols and manuscript prose have separate owners."
metadata:
  ccf_skill_controls:
    handoff_question_mode: partial
    respect_session_denylists: true
    protect_idea_scope_in_writing: true
    private_material_safety: moderate
    shared_controls: ../ccf-common/references/
---

# CCF Visual Composer

## Family File Contract

Reuse canonical paths and one stable task directory, normally `ccfa-workfiles/<purpose>/<artifact-id>/`. Update current artifacts in place, preserve inputs, and check UTF-8/Chinese text. Apply [artifact-contracts.md](../ccf-common/references/artifact-contracts.md) when writing files.

## Collaboration Contract

Apply [ccf-humanization](../ccf-humanization/SKILL.md) first, then [ccf-common](../ccf-common/SKILL.md), once. Reuse their active rules and valid prerequisites. Integrate a needed scientific contribution through [routing.md](../ccf-common/references/routing.md), without duplicate intake or reports.

## Invocation Controls

**CCFA Handoff Mode: PARTIAL (Recommended).** Preserve `metadata.ccf_skill_controls` and Common's [handoff modes](../ccf-common/references/handoff-modes.md).

| User's actual task | Route |
| --- | --- |
| Create or redraw a method, architecture, flow or other conceptual scientific diagram | Complete all three GPT Image stages below. The renderer designs the entire figure; no coordinate skeleton, SVG/PPT shapes, raster tracing or native/vector reconstruction of the diagram. |
| Render numerical analysis, quantitative/ablation experiments or biological data | Python with supplied data. Reuse a selected template's specification and implementation; preserve its layout, style and supported analytical elements. |
| Modify, adjust or polish an existing figure | Use its current image/source and a scoped edit. Raster edits use the host image-editing workflow. Existing code/native sources can be maintained locally; this does not authorize reconstructing a raster into vector objects. A requested complete redraw uses the three-stage route. |
| Combine a method illustration with quantitative results | Keep numerical marks, axes and labels code-rendered and unchanged. Apply the diagram route to the conceptual content; verify numerical fidelity after any image operation. |
| Put an approved diagram into a document or presentation | Place the final PNG when requested. A raster placed in PPTX/PDF remains a raster; do not rebuild its modules or claim native editability. Existing requested source files and explicit numerical exports retain their formats. |

New/redrawn diagrams are raster-first throughout, including repair. If the required image capability is unavailable, retain the useful prompt and explain the missing capability; do not substitute vector construction. Historical numerical SVG exports and local edits to existing SVG/PPTX sources remain distinct from creating a new diagram.

## Understand The Figure Before Expanding The Prompt

First read the relevant method, caption/data and user's requested use. Establish what the reader should learn, the figure's role and scope, the necessary objects and actual relationships, and the target slot/font. Distinguish an explanatory causal relation from an implemented computation; latent/unknown quantities are not observed system inputs. Use reference images for their declared content or visual role. For numerical figures, establish input types, units and statistical meanings before choosing elements; a selected template remains fixed. Use existing answers and ask only about a missing fact that changes the science. Keep this understanding in the current context or source record: no separate report, approval, agent or image call.

## Required Three-Stage Diagram Workflow

1. **Prepare one prompt P.** Expand the established scientific understanding into content, reference roles and visual/delivery instructions. Preserve supported inputs, representations, operations, outputs, labels/equations and important connections; do not invent modules to complete a truncated method. Apply the chosen font, semantic colors and differentiated text hierarchy, with compact groups and clear paths. Let the image model choose detailed placement. Preserve a good supplied prompt and add only missing information; omit duplicated or irrelevant style clauses. No skeleton or separate prompt-writing agent is required.
2. **Generate draft G0.** Call GPT Image with P, the relevant reference images and article material. If a PDF cannot be attached, provide the needed figure/pages as images and/or the relevant scientific content in P. Use minimized authorized material, with reference roles identified in the tool request; do not omit the article's mechanism or send unrelated pages. Generate one complete composition.
3. **Refine to G1.** Inspect G0, then call GPT Image again with the same P and G0 as the edit target. Add one concise refinement request covering the actual related defects; preserve accepted layout, scientific objects, labels, equations and topology. With no identified defect, request restrained visual coordination/readability refinement without inventing a failure or changing the content. Check the affected paths and final appearance. G1 is the delivered PNG.

Stage 1 uses the current assistant; stages 2 and 3 are two actual image-tool calls. The refinement is part of one candidate, not a second optional variant: `figure_variants=off` does not skip it. A prepared prompt is not an executed generation/refinement. Keep one prompt/source record and one current final result; refer to the tool-managed draft rather than copying attempt histories. For the prompt and refinement envelopes, see [architecture-diagram-generation.md](references/architecture-diagram-generation.md).

For an existing-image edit, apply only the requested change with its established context; do not run all three stages unless the user requests a new composition or redraw. Group related corrections into one regional pass. If a scientific defect remains after refinement, repair it through the image workflow and recheck attached connections; when a defect survives repeated repairs, revise the representation or image instructions rather than nudging blindly or constructing a vector substitute.

## Data-Template Fidelity

A named template, selected gallery entry or supplied JSON/Python is the rendering source, not just inspiration. Open and reuse that exact specification/implementation. Replace only the supplied scientific data and requested fields, keeping canvas, font scale, palette identities, subplot/axis structure, layers, legend definitions and statistical meanings. Do not call a fresh demo, reroute to a nearby primitive, reconstruct by eye, or silently change a composition when a required field is missing. Resolve the data mismatch first. Never leave old demonstration values mixed into a real-data figure.

For a new design without a selected template, classify input data and chart type independently with `resources/python/ccfa_figure_library.py route`; inspect only chosen candidates and their `element_plan`. Combine article-supported comparisons, ranges, distributions, conditional summaries or key observations into a coherent analysis unit. Primitives and extracted panels are reusable components. Preserve original examples, the user's reference pairs, actual observation times and sample identities. Extra labels alone do not add analysis. Use the library's automatic choice among equally suitable designs; ask for no seed and impose no usage quota.

## Visual Requirements And Acceptance

- Preserve modules, connections, labels, equations, values, units, uncertainty and statistical definitions. Align paired data by identity or a supplied matching contract; equal lengths do not establish pairing. Verify actual required source-to-target paths, not proximity.
- Fit the actual paper slot with compact meaningful groups, aligned peers, clear short lines and readable text. Keep high information density and supported scientific detail. No default square, compulsory grid, equal-width boxes or decorative additions. Exact gap requests remain targets for raster composition, not a reason to start coordinate construction.
- Use Times New Roman by default or selected Comic Sans MS, subject to user/venue overrides. Bold titles, legends and x/y/colorbar labels and ticks. Keep method headings distinct from subordinate body labels/equations. Maintain coherent semantic colors; bars/boxes use lighter fills and substantial darker same-hue edges, while dense points/matrix cells retain their encoding.
- Inspect the actual final-size image for scientific fidelity and visual quality together. Numerical results must match the supplied data; a selected template must retain its unedited design choices. Check clipping, glyphs, alignment, overlaps and colors. Local changes check their affected dependencies.

## Selective References

The entry above is sufficient for a straightforward task. Load detail for the current decision only.

| Mode | Relevant reference |
| --- | --- |
| `architecture-generation`, `diagram-refinement` | [architecture-diagram-generation.md](references/architecture-diagram-generation.md): three-stage prompt/attachment/refinement details. |
| `figure-design`, `python-plotting` | [figure-design-library.md](references/figure-design-library.md), [python-plot-recipes.md](references/python-plot-recipes.md), or [figure-examples.md](references/figure-examples.md): selected data template, binding or renderer. |
| `visual-contract` | [visual-contract.md](references/visual-contract.md): shared identity, scale, layout or scientific encoding decisions. |
| `existing-source-edit`, `render-qa` | [render-qa.md](references/render-qa.md): scoped source/image maintenance, requested raster placement and final inspection. |
| `table-design`, `layout-integration` | [figure-table-layout.md](references/figure-table-layout.md): manuscript/table placement. Scientific-object and reference use is covered by the diagram workflow. |

Use [adaptive-architecture-style.md](references/adaptive-architecture-style.md) or [palette-and-accessibility.md](references/palette-and-accessibility.md) for an unmet design choice. Deliver the requested visual and necessary source first, with concise provenance and actual checks. Keep process instructions out of the image and avoid a compulsory QA report.
