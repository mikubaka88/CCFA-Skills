# Reference-Driven Layout Blueprint

Inspect supplied references and use their actual images when authorized. For an ordinary new diagram, a few observed composition properties are enough; this reference is for an ambiguous role, a detailed reconstruction, or a defect that needs measured repair.

## Reference Selection

Prefer the user's references, then already inspected relevant paper figures. Search only for an unresolved design decision. Identify each included image by order and role: scientific content, composition, object appearance, palette or existing draft. A reference for appearance does not supply this method's scientific topology. Include only needed images within the existing privacy boundary.

Record source/credits in the current source record when persistence is useful. Preserve explicit template geometry, otherwise describe a few useful properties—aligned input strips, a shared trunk, compact output branches, a restrained palette or clear text hierarchy. Do not create a separate measurement sheet, read the entire asset library or upload a full manuscript to explain a figure. An adequate reference does not need exhaustive verbal reconstruction.

## Layout-First Workflow

1. Keep the supported scientific objects, connections and exact labels; adapt the reference to the current method rather than copying its science.
2. For a new diagram, generate a complete composition from that content and the actual references. Leave module sizes, positions, grouping and local illustration to the image model unless the user fixed them. Straight lines and alignment do not require a pre-rendered skeleton.
3. Inspect compactness, explanatory hierarchy, peer alignment, legibility and clear paths at the final paper size, together with the scientific content. Boxes are optional; proximity, open lanes, light groups and supported asymmetry may communicate better.
4. Repair actual defects locally. For an explicit measured reconstruction, existing native source, or requested editability, use coordinates/shared baselines/ports and the visual contract's optional measurements. A skeleton is an optional tool for a specific unresolved geometry problem, not a mandatory stage before image generation.

An overview/detail pair preserves object identity, coordinate frame and crop correspondence. Data views keep their actual scales and entity mappings. Changing a style does not change observations, statistical definitions, topology or text meaning.

## Numerical Reference Reconstruction

For a supplied analytical figure, inventory encodings before choosing a nearby template. A density map plus boxes is incomplete when the reference also encodes a threshold region, a mass-weighted statistic, explicitly named quantiles, or different observation times. Preserve these elements when the corresponding data are supplied:

| Reference element | Preserve in the editable reconstruction |
| --- | --- |
| Density with logarithmic distance and count colorbar | The actual x/y transforms, log count normalization, count scale and units. Do not replace log counts with a linear intensity legend. |
| Corridor defined by two thresholds | Both boundaries, the highlighted intersection and a concise leader annotation. Compute state share from the full stated population; compute mass share only from supplied weights. Missing mass data do not become an assumed percentage. |
| Median–P90 boxes, P99 whiskers and P95 diamonds | These exact quantile meanings. The ordinary median/IQR default is a different statistic and remains available for other tasks. Supplied summaries and raw samples are alternative inputs, not interchangeable hidden fallbacks. |
| Series observed at different steps | Keep each series' actual x coordinates. A curve beginning at step 4 does not acquire synthetic observations at steps 0 and 2 merely to share an axis. |
| Outlined bars with two line criteria | Retain their shared percentage axis, method colors and marker differences. Draw bands only when lower/upper values are supplied. Annotate a small useful subset of line values; bar labels remain optional. |

The `sensitivity_dynamics` template supports these details without changing legacy calls. Use `density.corridor={x_max,y_max,weights?,label?,annotation_xy?}` with optional axis limits and log-count colorbar settings. A sensitivity block can use `summary={median,p90,p95,p99}` without `samples`, or `summary_mode="median_p90"` with actual samples; `annotate` and `quantile_label` govern labels. Dynamic series may supply their own `x`, marker and line style. Category blocks support `bar_style="outlined"`, `bar_labels`, `label_wrap`, `tick_font_size`, provided bands, and selected annotation indices. Wrapping labels changes display only, not group identity or order.

The maintained demonstration and both reference-pair examples exercise the complete encodings above with marked synthetic inputs. In the four-panel form, the colorbar occupies a dedicated GridSpec column so upper and lower data rectangles align, including the density/time-series right edge. Demo typography inherits the requested final-size font setting; it does not pin small ticks or legends when a caller selects larger type.

Keep visual hierarchy tied to the message: small aligned panel labels, restrained grids, a common baseline, enough headroom for legends, and one warm annotation color against quieter data colors. Do not add density, uncertainty, a corridor or extra panels only to make a sparse dataset look more elaborate. Explain statistical definitions in the caption or supplied metadata rather than crowding the canvas; transfer a reference caption's scientific facts only when they apply to the current data.

## Reference Boundaries

Use requested alignment, proportions, spacing, typography, and palette relationships; preserve supplied editable template geometry when requested. Do not transplant unrelated science, captions, logos, or artwork into the new method. Do not use a screenshot as the final background of an allegedly editable figure. Keep source links and credits in the existing specification; method names and output titles describe their function. Deliver a wireframe only when requested; otherwise plan internally. Search additional references only for an unresolved layout decision.

Research basis is registered in `../../ccf-common/references/source-registry.yaml` under `livefigure-editable-scientific-illustration`, `autofigure-edit-editable-svg`, `scifig-editable-figure-generation`, and `astradraw-visual-workflow`; grid and connector guidance also draws on `d2-grid-layout` and `elk-layered-layout`. Reference assets remain in the task cache unless their reuse and publication are authorized.
