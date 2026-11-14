"""Linked scientific layouts, using one supplied dataset and one figure.

``render_layout(kind, data)`` returns a Matplotlib Figure. It inherits paper_style
and exposes ``fig.ccfa_layout`` with its named axes and descriptive computations.
No layout calls demo_data, fits a model, estimates significance, or changes data.
NumPy and Matplotlib are the only dependencies beyond existing CCFA modules.
"""
from __future__ import annotations

from collections.abc import Mapping
import math

import matplotlib as mpl
import matplotlib.colors as mcolors
from matplotlib.lines import Line2D
from matplotlib.ticker import MaxNLocator
import numpy as np

import ccfa_analysis_panels as p
from ccfa_plot_recipes import PALETTES




def _vector(values, name):
    return p._vector(values, name)


def _increasing(values, name, *, minimum=2):
    values = _vector(values, name)
    if len(values) < minimum or np.any(np.diff(values) <= 0):
        raise ValueError(f"{name} needs at least {minimum} strictly increasing finite coordinates")
    return values


def _text(value, name):
    if not isinstance(value, str) or not value.strip():
        raise ValueError(f"{name} must be nonempty text")
    return value


def _title(data):
    title = data.get("title", "")
    if not isinstance(title, str): raise ValueError("title must be text")
    return title


def _palette(palette):
    if palette not in PALETTES: raise ValueError(f"Unknown palette {palette!r}")
    return PALETTES[palette]


def _index(value, length, name):
    if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, np.integer)):
        raise ValueError(f"{name} must be an integer index")
    if not 0 <= value < length: raise ValueError(f"{name} is outside the supplied grid")
    return int(value)


def _range(value, observed, name):
    bound = _vector(value, name)
    if len(bound) != 2 or bound[1] <= bound[0]:
        raise ValueError(f"{name} must contain increasing lower and upper bounds")
    if np.min(observed) < bound[0] or np.max(observed) > bound[1]:
        raise ValueError(f"{name} must enclose all supplied observations")
    return bound


def _meta(fig, kind, axes, computed):
    fig.ccfa_layout = {"kind": kind, "axes": axes, "computed": computed}
    return p.finish_paper_style(fig)


def _bin_counts(values, edges, name):
    edges = _increasing(edges, name)
    if np.any(values < edges[0]) or np.any(values > edges[-1]):
        raise ValueError(f"Every observation must fall inside {name}")
    return edges, np.histogram(values, bins=edges)[0]


def plot_joint_marginals(fig, data, *, palette="npg"):
    """Joint observations with top/right counts from those same observations.

    Required: x, y, bin_edges_x, bin_edges_y. Optional mode is scatter or hexbin.
    Scatter color_values require a stated color_range and matching observations;
    they do not replace either coordinate. All histograms display raw counts.
    """
    x = _vector(data["x"], "x"); y = _vector(data["y"], "y")
    p._same_length(x, y)
    edges_x, counts_x = _bin_counts(x, data["bin_edges_x"], "bin_edges_x")
    edges_y, counts_y = _bin_counts(y, data["bin_edges_y"], "bin_edges_y")
    mode = data.get("mode", "scatter")
    if mode not in ("scatter", "hexbin"): raise ValueError("mode must be scatter or hexbin")
    xlabel = _text(data.get("xlabel", "Observed X"), "xlabel")
    ylabel = _text(data.get("ylabel", "Observed Y"), "ylabel")
    color = _palette(palette)[0]
    color_values = None
    if data.get("color_values") is not None:
        if mode != "scatter": raise ValueError("color_values apply to supplied scatter observations, not hexbin counts")
        color_values = _vector(data["color_values"], "color_values")
        p._same_length(x, color_values)
        if "color_range" not in data: raise ValueError("color_values need an explicit color_range")
        color_range = _range(data["color_range"], color_values, "color_range")
        color_label = _text(data.get("color_label", "Supplied value"), "color_label")
    elif "color_range" in data:
        raise ValueError("color_range requires color_values")
    gridsize = data.get("gridsize", 28)
    if isinstance(gridsize, (bool, np.bool_)) or not isinstance(gridsize, (int, np.integer)) or gridsize < 2:
        raise ValueError("gridsize must be an integer of at least two")
    cmap = data.get("cmap", "viridis")
    # Construct all linked axes inside one GridSpec; comparable plot edges align.
    grid = fig.add_gridspec(2, 2, width_ratios=[4, 1.1], height_ratios=[1.05, 4])
    main = fig.add_subplot(grid[1, 0], gid="joint-main")
    top = fig.add_subplot(grid[0, 0], sharex=main, gid="joint-x-counts")
    right = fig.add_subplot(grid[1, 1], sharey=main, gid="joint-y-counts")
    if mode == "scatter":
        if color_values is None:
            joint = main.scatter(x, y, color=color, s=12, alpha=.55, linewidths=0)
        else:
            joint = main.scatter(x, y, c=color_values, s=12, alpha=.7, linewidths=0,
                                  cmap=cmap, vmin=color_range[0], vmax=color_range[1])
    else:
        joint = main.hexbin(x, y, gridsize=int(gridsize), mincnt=1, cmap=cmap,
                             extent=(edges_x[0], edges_x[-1], edges_y[0], edges_y[-1]),
                             linewidths=0, rasterized=False)
    top_bars = top.bar(edges_x[:-1], counts_x, width=np.diff(edges_x), align="edge",
                       color=color, alpha=.55, edgecolor="white", linewidth=.4)
    right_bars = right.barh(edges_y[:-1], counts_y, height=np.diff(edges_y), align="edge",
                            color=color, alpha=.55, edgecolor="white", linewidth=.4)
    main.set(xlabel=xlabel, ylabel=ylabel, xlim=(edges_x[0], edges_x[-1]),
              ylim=(edges_y[0], edges_y[-1]))
    top.set_ylabel("Count"); right.set_xlabel("Count")
    top.tick_params(axis="x", labelbottom=False)
    right.tick_params(axis="y", labelleft=False)
    top.yaxis.set_major_locator(MaxNLocator(nbins=2, integer=True))
    right.xaxis.set_major_locator(MaxNLocator(nbins=2, integer=True))
    p.clean_axes(main, "both"); p.clean_axes(top, "y"); p.clean_axes(right, "x")
    axes = {"main": main, "x_counts": top, "y_counts": right}
    # A quantitative color scale occupies the otherwise unused corner.
    if color_values is not None or mode == "hexbin":
        corner = grid[0, 1].subgridspec(3, 1, height_ratios=[1, .22, 1])
        color_ax = fig.add_subplot(corner[1, 0], gid="joint-color-scale")
        fig.colorbar(joint, cax=color_ax, orientation="horizontal",
                      label=color_label if color_values is not None else "Bin count")
        color_ax.xaxis.set_major_locator(MaxNLocator(nbins=2))
        axes["colorbar"] = color_ax
    return _meta(fig, "joint_marginals", axes,
                  {"counts_x": counts_x, "counts_y": counts_y,
                   "bin_edges_x": edges_x.copy(), "bin_edges_y": edges_y.copy(),
                   "joint_artist": joint, "x_bars": top_bars, "y_bars": right_bars,
                   "observation_count": len(x), "marginal_meaning": "raw counts of the same paired observations"})


def aligned_tracks(fig, data, *, palette="npg"):
    """One nonuniform numeric x coordinate shared by every continuous track.

    A track has label, unit and either y or series=[{label,y,...}]. Multiple
    series within a track share its declared unit; different tracks keep separate
    y axes. Optional markers=[{x,label}] identify supplied common positions.
    This layout does not infer genomic features, splice arcs or event locations.
    """
    x = _increasing(data["x"], "x")
    tracks = data["tracks"]
    if not isinstance(tracks, list) or not tracks: raise ValueError("tracks must be a nonempty list")
    if not all(isinstance(track, Mapping) for track in tracks):
        raise ValueError("Every track must be a mapping")
    xlabel = _text(data.get("xlabel", "Shared position"), "xlabel")
    p._labels([track.get("label", "") for track in tracks], name="track labels")
    parsed = []; identities = []
    show_legend = False
    for track in tracks:
        unit = _text(track.get("unit"), "track unit")
        if ("y" in track) == ("series" in track):
            raise ValueError("Each track needs either y or series, but not both")
        series = track.get("series") if "series" in track else [{"label": track["label"], "y": track["y"]}]
        if not isinstance(series, list) or not series: raise ValueError("series must be a nonempty list")
        if not all(isinstance(row, Mapping) and "y" in row for row in series):
            raise ValueError("Every series needs a mapping with supplied y values")
        names = p._labels([row.get("label", "") for row in series], name="series labels")
        show_legend = show_legend or len(series) > 1
        rows = []
        for name, row in zip(names, series):
            y = _vector(row["y"], "track y"); p._same_length(x, y)
            linestyle = row.get("linestyle", "-")
            if linestyle not in ("-", "--", "-.", ":"):
                raise ValueError("series linestyle must be -, --, -., or :")
            if name not in identities: identities.append(name)
            rows.append({"label": name, "y": y, "linestyle": linestyle})
        ratio = p._positive(track.get("height_ratio", 1), "height_ratio")
        parsed.append({"label": track["label"], "unit": unit, "series": rows, "ratio": ratio})
    colors = p.entity_encoding(identities, palette=palette, colors=data.get("entity_colors"))
    markers = data.get("markers", [])
    if not isinstance(markers, list): raise ValueError("markers must be a list of supplied positions")
    parsed_markers = []
    for marker in markers:
        if not isinstance(marker, Mapping) or "x" not in marker:
            raise ValueError("Each marker must declare a supplied x position")
        location = float(marker["x"])
        if not math.isfinite(location) or not x[0] <= location <= x[-1]:
            raise ValueError("marker x must be finite and inside the shared coordinate range")
        text = marker.get("label", "")
        if not isinstance(text, str): raise ValueError("marker label must be text")
        parsed_markers.append((location, text))
    ratios = ([.25] if show_legend else []) + [track["ratio"] for track in parsed]
    grid = fig.add_gridspec(len(ratios), 1, height_ratios=ratios)
    axes = []; lines = []; shared = None
    for i, track in enumerate(parsed):
        ax = fig.add_subplot(grid[i + int(show_legend), 0], sharex=shared,
                              gid=f"aligned-track-{i}")
        if shared is None: shared = ax
        track_lines = []
        for row in track["series"]:
            line, = ax.plot(x, row["y"], label=row["label"], color=colors[row["label"]]["color"],
                             linestyle=row["linestyle"], lw=1.2)
            track_lines.append(line)
        for location, text in parsed_markers:
            ax.axvline(location, color=p.INK, lw=.65, ls=":", alpha=.8)
            if i == 0 and text:
                ax.annotate(text, (location, 1), xycoords=("data", "axes fraction"),
                              xytext=(2, 3), textcoords="offset points", fontsize=mpl.rcParams["font.size"]-1,
                              ha="left", va="bottom", annotation_clip=False)
        ax.set_ylabel(f"{track['label']}\n({track['unit']})")
        ax.yaxis.set_major_locator(MaxNLocator(nbins=3))
        ax.set_xlim(x[0], x[-1]); p.clean_axes(ax)
        if i < len(parsed)-1: ax.tick_params(axis="x", labelbottom=False)
        else: ax.set_xlabel(xlabel)
        axes.append(ax); lines.append(track_lines)
    result_axes = {"tracks": axes}
    if show_legend:
        legend_ax = fig.add_subplot(grid[0, 0], gid="aligned-track-legend")
        legend_ax.axis("off")
        handles = [Line2D([], [], color=colors[name]["color"], lw=1.3, label=name)
                   for name in identities]
        legend_ax.legend(handles=handles, loc="center", ncol=min(len(handles), 5),
                           frameon=False, handlelength=1.5, columnspacing=1.1)
        result_axes["legend"] = legend_ax
    return _meta(fig, "aligned_tracks", result_axes,
                  {"x": x.copy(), "lines": lines, "markers": parsed_markers,
                   "units": [track["unit"] for track in parsed], "entity_encoding": colors})


def matrix_slices(fig, data, *, palette="npg"):
    """Heatmap and two linked profiles extracted from one supplied response grid.

    x/y are numeric cell centers and can be nonuniform. The mesh uses nearest
    cell boundaries; the curves show samples at their actual coordinates.
    row_index/column_index select actual rows/columns, not inferred optima.
    """
    x = _increasing(data["x"], "x"); y = _increasing(data["y"], "y")
    try: response = np.asarray(data["response"], dtype=float)
    except (ValueError, TypeError) as exc: raise ValueError("response must be numeric") from exc
    if response.shape != (len(y), len(x)) or not np.isfinite(response).all():
        raise ValueError("response must be finite y rows × x columns on the supplied grid")
    row = _index(data["row_index"], len(y), "row_index")
    column = _index(data["column_index"], len(x), "column_index")
    xlabel = _text(data.get("xlabel", "Control X"), "xlabel")
    ylabel = _text(data.get("ylabel", "Control Y"), "ylabel")
    response_label = _text(data.get("response_label", "Response"), "response_label")
    if data.get("response_range") is not None:
        limits = _range(data["response_range"], response, "response_range")
        norm = mcolors.Normalize(*limits)
    else: norm = p._normalization(response, None, None)
    colors = _palette(palette)
    row_color, column_color = colors[0], colors[1 % len(colors)]
    grid = fig.add_gridspec(2, 2, width_ratios=[4, 1.3], height_ratios=[1.25, 4])
    main = fig.add_subplot(grid[1, 0], gid="matrix-main")
    row_ax = fig.add_subplot(grid[0, 0], sharex=main, gid="matrix-row-slice")
    column_ax = fig.add_subplot(grid[1, 1], sharey=main, gid="matrix-column-slice")
    mesh = main.pcolormesh(x, y, response, shading="nearest", cmap=data.get("cmap", "viridis"),
                            norm=norm, linewidths=0, rasterized=False)
    main.axhline(y[row], color=row_color, lw=1, ls="--")
    main.axvline(x[column], color=column_color, lw=1, ls="--")
    main.scatter([x[column]], [y[row]], marker="s", s=30, facecolors="none",
                   edgecolors="white", linewidths=1, zorder=4)
    row_line, = row_ax.plot(x, response[row, :], color=row_color, marker="o", ms=2.8,
                             lw=1.2, label=f"{ylabel} = {y[row]:g}")
    column_line, = column_ax.plot(response[:, column], y, color=column_color, marker="o",
                                   ms=2.8, lw=1.2, label=f"{xlabel} = {x[column]:g}")
    main.set(xlabel=xlabel, ylabel=ylabel)
    row_ax.set_ylabel(response_label); column_ax.set_xlabel(response_label)
    row_ax.tick_params(axis="x", labelbottom=False)
    column_ax.tick_params(axis="y", labelleft=False)
    row_ax.set_title(f"{ylabel} = {y[row]:g}", loc="left", fontsize=mpl.rcParams["font.size"]-.5, pad=3)
    column_ax.set_title(f"{xlabel} = {x[column]:g}", loc="left", fontsize=mpl.rcParams["font.size"]-.5, pad=3)
    row_ax.yaxis.set_major_locator(MaxNLocator(nbins=3))
    column_ax.xaxis.set_major_locator(MaxNLocator(nbins=3))
    p.clean_axes(main, None); p.clean_axes(row_ax); p.clean_axes(column_ax, "x")
    corner = grid[0, 1].subgridspec(3, 1, height_ratios=[1, .22, 1])
    color_ax = fig.add_subplot(corner[1, 0], gid="matrix-color-scale")
    fig.colorbar(mesh, cax=color_ax, orientation="horizontal", label=response_label)
    color_ax.xaxis.set_major_locator(MaxNLocator(nbins=2))
    # Share cell boundaries as well as axes, including the full edge cells.
    coordinates = mesh.get_coordinates()
    main.set_xlim(float(coordinates[0, 0, 0]), float(coordinates[0, -1, 0]))
    main.set_ylim(float(coordinates[0, 0, 1]), float(coordinates[-1, 0, 1]))
    return _meta(fig, "matrix_slices",
                  {"main": main, "row_slice": row_ax, "column_slice": column_ax, "colorbar": color_ax},
                  {"row_index": row, "column_index": column,
                   "row_values": response[row, :].copy(), "column_values": response[:, column].copy(),
                   "row_coordinate": float(y[row]), "column_coordinate": float(x[column]),
                   "row_line": row_line, "column_line": column_line, "mesh": mesh,
                   "x": x.copy(), "y": y.copy()})


LAYOUTS = {
    "joint_marginals": {
        "function": plot_joint_marginals,
        "required": ["x", "y", "bin_edges_x", "bin_edges_y"],
        "why": "Keep a relationship and both one-variable distributions attached to identical observations and physical axes.",
        "cautions": "Marginals are raw counts with supplied bins, not inferred probability densities. Continuous scatter colors require a declared common range.",
        "study_candidates": ["nmi26-input-space-and-marginals"],
    },
    "aligned_tracks": {
        "function": aligned_tracks,
        "required": ["x", "tracks"],
        "why": "Read measurements and predictions at the same coordinate without losing position through independent panel widths or resampling.",
        "cautions": "Every track declares its own unit; overlaid series share that unit. Genomic feature annotations and splice arcs remain explicit authoring work.",
        "study_candidates": ["nature26-aligned-genomic-tracks"],
    },
    "matrix_slices": {
        "function": matrix_slices,
        "required": ["x", "y", "response", "row_index", "column_index"],
        "why": "Link a two-control response surface to actual row and column profiles, with selected positions marked on the original matrix.",
        "cautions": "Profiles come from the same supplied grid; calibration curves, fitted optima and extrapolations cannot be recovered from a scalar response matrix.",
        "study_candidates": ["nmi26-parameter-surface-with-slices", "vision-scaling-optimum-grid"],
    },
}


def render_layout(kind, data, *, width_mm=183, height_mm=None, font="serif", palette="npg", font_size=8.5):
    """Render one linked layout; the returned Figure owns all component axes.

    The caller exports with ccfa_analysis_panels.save_figure or fig.savefig.
    fig.ccfa_layout provides named axes and computed descriptive quantities.
    No randomness runs here; demo data must be requested separately.
    """
    if kind not in LAYOUTS: raise ValueError(f"Unknown linked layout {kind!r}")
    font_size = p._positive(font_size, "font_size")
    if not isinstance(data, Mapping): raise ValueError("data must be a mapping of supplied observations")
    missing = [name for name in LAYOUTS[kind]["required"] if name not in data]
    if missing: raise ValueError(f"Missing layout fields: {', '.join(missing)}")
    title = _title(data); _palette(palette)
    if height_mm is None:
        height_mm = 32 + 23*len(data["tracks"]) if kind == "aligned_tracks" and isinstance(data.get("tracks"), list) else 126
    for value, name in ((width_mm, "width_mm"), (height_mm, "height_mm")):
        if isinstance(value, (bool, np.bool_)) or not isinstance(value, (int, float, np.integer, np.floating)) or not math.isfinite(value):
            raise ValueError(f"{name} must be a finite physical dimension")
    minimum_height = 30 + 16*len(data["tracks"]) if kind == "aligned_tracks" and isinstance(data.get("tracks"), list) else 70
    if not 70 <= width_mm <= 1000 or not minimum_height <= height_mm <= 1000:
        raise ValueError("The physical canvas is too small for readable linked axes or exceeds 1000 mm")
    fig = None
    with p.paper_style(font=font, font_size=font_size):
        try:
            fig = p.new_figure(width_mm=width_mm, height_mm=height_mm)
            synthetic = isinstance(data.get("_meta"), Mapping) and data["_meta"].get("synthetic")
            bottom = .055 if synthetic else 0
            top = .94 if title else 1
            fig.set_layout_engine("constrained", w_pad=.035, h_pad=.025, wspace=.025, hspace=.025,
                                  rect=(0, bottom, 1, top-bottom))
            LAYOUTS[kind]["function"](fig, data, palette=palette)
            if title: fig.suptitle(title, fontsize=font_size+1.5, weight="bold")
            if synthetic:
                fig.text(.995, .006, "Simulated data · layout demonstration", ha="right", va="bottom",
                           fontsize=max(6,font_size-1.5), color="#6C747A")
        except Exception:
            if fig is not None:
                import matplotlib.pyplot as plt
                plt.close(fig)
            raise
    return p.finish_paper_style(fig)


def demo_data(kind, seed=None):
    """Explicit synthetic data; a fresh local generator is used by default.

    ``seed`` exists for internal regression reproducibility. It is not a chart
    design control and is not used by render_layout or saved as a user setting.
    """
    if kind not in LAYOUTS: raise ValueError(f"Unknown linked layout {kind!r}")
    rng = np.random.default_rng(seed)
    meta = {"synthetic": True, "purpose": "linked-layout demonstration; not paper results"}
    if kind == "joint_marginals":
        x = rng.beta(2.2, 3.5, 180)
        y = .15 + .65*x + rng.normal(0, .09, len(x))
        return {"x": x, "y": y, "bin_edges_x": np.array([0,.1,.2,.35,.5,.7,1]),
                "bin_edges_y": np.linspace(-.2, 1, 12), "xlabel": "Supplied score A",
                "ylabel": "Supplied score B", "_meta": meta}
    if kind == "aligned_tracks":
        x = np.cumsum(rng.integers(2, 11, 70)).astype(float)
        reference = 4 + 28*np.exp(-((x-120)/25)**2) + 21*np.exp(-((x-240)/32)**2)
        observed = np.maximum(reference+rng.normal(0, 2.5, len(x)), 0)
        return {"x": x, "xlabel": "Shared position (bp)",
                "markers": [{"x": float(x[len(x)//2]), "label": "Supplied variant"}],
                "tracks": [{"label": "RNA signal", "unit": "counts", "series": [
                    {"label": "Observed", "y": observed}, {"label": "Predicted", "y": reference, "linestyle": "--"}]},
                    {"label": "Accessibility", "unit": "a.u.", "y": .2+.7*np.exp(-((x-160)/45)**2)},
                    {"label": "Variant effect", "unit": "score", "y": .3*np.sin(x/45)+rng.normal(0,.025,len(x))}],
                "_meta": meta}
    x = np.array([.02, .05, .1, .2, .4, .8, 1.4])
    y = np.array([1, 2, 4, 7, 12.])
    xx, yy = np.meshgrid(x, y)
    response = .18 + .6*np.exp(-((xx-.4)/.5)**2)*np.exp(-((yy-5)/5)**2) + rng.normal(0,.015,xx.shape)
    return {"x": x, "y": y, "response": response, "row_index": 2, "column_index": 4,
            "xlabel": "Control X", "ylabel": "Control Y", "response_label": "Measured response", "_meta": meta}
