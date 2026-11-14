#!/usr/bin/env python3
"""Route scientific questions to PNG charts; compose only supplied data.

Routing and catalog lookup need only the standard library. Plotting imports
NumPy/Matplotlib on demand. Example data requires an explicit demo command.
"""
from __future__ import annotations

import argparse
import copy
from functools import lru_cache
import hashlib
import inspect
import json
import math
import os
from pathlib import Path
import random
import re
import secrets
import tempfile

LIBRARY = Path(__file__).resolve().parents[2] / "resources/figure-library"


def _plain(value):
    if isinstance(value, dict):
        return {key: _plain(item) for key, item in value.items()}
    if isinstance(value, (list, tuple)):
        return [_plain(item) for item in value]
    if hasattr(value, "tolist"):
        return _plain(value.tolist())
    return value


@lru_cache(maxsize=1)
def catalog():
    return json.loads((LIBRARY / "catalog.json").read_text(encoding="utf-8"))


def explain(kind):
    for item in catalog()["charts"]:
        if item["id"] == kind:
            return copy.deepcopy(item)
    raise ValueError(f"Unknown chart: {kind}")


# Equivalent drawing machinery shares navigation, while each member retains its
# scientific field contract. Optional features below keep material variants apart.
_DRAWING_GRAMMAR = {
    "comparison_intervals": "point_intervals", "forest_intervals": "point_intervals",
    "ranked_intervals": "point_intervals", "matrix_heatmap": "cell_matrix",
    "transition_matrix": "cell_matrix", "dot_matrix": "bubble_matrix",
    "matrix_bubbles": "bubble_matrix", "pareto_scatter": "pareto_frontier",
    "cost_quality_frontier": "pareto_frontier",
}
_STRUCTURAL_KEYS = {"xscale", "yscale", "scale", "normalization", "paired",
                    "orientation", "quantile", "whisker_quantile", "box_quantiles",
                    "summary_kind", "summary_mode", "panel_pair", "order", "mode", "statistic",
                    "bar_style", "linestyle", "marker"}
_FEATURE_FIELDS = {
    "interval": ("lower", "upper"), "given_quantiles": ("quantiles",),
    "raw_runs": ("runs",), "censored": ("censored",),
    "corridor": ("corridor",), "threshold": ("threshold",),
    "weights": ("weights",), "value_labels": ("value_labels",),
    "annotations": ("annotations",), "color_values": ("color_values",),
    "filled_series": ("fill_method",), "sample_labels": ("annotate_labels",),
    "given_summary": ("summary",), "point_labels": ("annotate",),
    "bar_labels": ("bar_labels",), "explicit_colorbar_ticks": ("colorbar_ticks",),
    "log_count_range": ("count_range",),
}


def _drawing_options(data):
    """Retain encoded relationships, never an observation or its label text."""
    if not isinstance(data, dict):
        return {}
    result = {}
    for key in sorted(_STRUCTURAL_KEYS & data.keys()):
        value = data[key]
        # These are protocol/encoding selectors, not arbitrary nested records.
        if key in {"xscale", "yscale", "scale"} and value == "linear":
            continue
        if key == "panel_pair" and value == "all":
            continue
        if key == "order" and value == "input":
            continue
        if isinstance(value, (str, bool)) or value is None:
            result[key] = value
        elif key in {"quantile", "whisker_quantile", "box_quantiles"}:
            result[key] = _plain(value)
    def present(value):
        return value is not None and value is not False and not (isinstance(value, (list, tuple, dict, str)) and len(value) == 0)
    for name, fields in _FEATURE_FIELDS.items():
        if all(key in data and present(data[key]) for key in fields):
            result[name] = True
    if "corridor" in result:
        corridor = data.get("corridor")
        if isinstance(corridor, dict):
            result["corridor_fields"] = sorted(key for key in corridor
                if key not in {"label", "text", "color", "alpha", "annotation_xy"})
    if isinstance(data.get("summary"), dict):
        result["summary_fields"] = sorted(data["summary"])
    if "quantiles" in data and isinstance(data.get("probabilities"), list):
        result["quantile_levels"] = _plain(data["probabilities"])
    # Templates keep nested blocks separate. Numeric data, category names,
    # palette choices and exact thresholds cannot create duplicate families.
    blocks = {key: _drawing_options(value) for key, value in data.items()
              if isinstance(value, dict) and not key.startswith("_")}
    blocks = {key: value for key, value in blocks.items() if value}
    if blocks:
        result["blocks"] = blocks
    if isinstance(data.get("series"), list):
        options = []
        for row in data["series"]:
            if not isinstance(row, dict):
                continue
            option = _drawing_options(row)
            if row.get("x") is not None:
                option["independent_x"] = True
            options.append(option)
        if any(options):
            unique = {json.dumps(row, sort_keys=True): row for row in options}
            result["series_options"] = [unique[key] for key in sorted(unique)]
    return result


def drawing_signature(spec):
    """Return the drawing structure used to merge equivalent gallery entries.

    No plotting dependency, data generation, source inspection or network call
    occurs. Equal signatures mean equivalent declared drawing structure, not
    equal scientific questions or interchangeable datasets.
    """
    if not isinstance(spec, dict) or spec.get("version", 1) != 1 or isinstance(spec.get("version"), bool):
        raise ValueError("A drawing signature needs a version-1 specification")
    if "template" in spec or "layout" in spec:
        kind = "template" if "template" in spec else "layout"
        if not isinstance(spec[kind], str) or not spec[kind]:
            raise ValueError("Specify an actual template or layout name")
        data = spec.get("data", {})
        if kind == "template" and spec[kind] == "sensitivity_dynamics":
            pair = data.get("panel_pair", "all")
            relevant = {"density", "sensitivity"} if pair == "sensitivity" else {"dynamics", "categories"} if pair == "dynamics" else None
            if relevant is not None:
                data = {key: value for key, value in data.items() if key in relevant | {"panel_pair"}}
        return {"renderer": kind, "kind": spec[kind],
                "options": _drawing_options(data)}
    panels = spec.get("panels")
    if not isinstance(panels, list) or not panels:
        raise ValueError("A drawing signature needs panels, a template, or a layout")
    ids = {panel.get("id"): i for i, panel in enumerate(panels)}
    def node(panel):
        if not isinstance(panel, dict) or not isinstance(panel.get("kind"), str):
            raise ValueError("Each drawing node needs its renderer kind")
        result = {"kind": _DRAWING_GRAMMAR.get(panel["kind"], panel["kind"]),
                  "options": _drawing_options(panel.get("data", {}))}
        data = panel.get("data", {})
        if panel["kind"] in {"forest_intervals", "ranked_intervals"} and data.get("reference", 0) is not None:
            result["options"]["reference_line"] = True
        if panel["kind"] == "pareto_scatter" and data.get("annotate", True):
            result["options"]["point_labels"] = True
        if panel["kind"] in {"dot_matrix", "matrix_bubbles"}:
            result["options"]["size_binding"] = "independent_measurement" if panel["kind"] == "dot_matrix" else "absolute_value"
        for axis in ("xscale", "yscale"):
            if panel.get(axis, "linear") != "linear":
                result[axis] = panel[axis]
        if panel.get("layers"):
            result["layers"] = [node(layer) for layer in panel["layers"]]
        if panel.get("style"):
            style = _drawing_options(panel["style"])
            if style:
                result["style"] = style
        if panel.get("colorbar") is False:
            result["colorbar"] = False
        return result
    drawings = []
    for i, panel in enumerate(panels):
        item = node(panel)
        item["position"] = [panel.get("row", 0), panel.get("column", i),
                            panel.get("rowspan", 1), panel.get("colspan", 1)]
        drawings.append(item)
    shared = []
    for group in spec.get("shared_axes", []):
        members = group.get("panels", [])
        shared.append({"axis": group.get("axis"),
                       "panels": sorted(ids.get(value, value) for value in members)})
    result = {"renderer": "panels", "rows": spec.get("rows", 1),
            "columns": spec.get("columns", len(panels)), "panels": drawings,
            "shared_axes": sorted(shared, key=lambda row: json.dumps(row, sort_keys=True))}
    for key in ("width_ratios", "height_ratios"):
        if spec.get(key) is not None:
            result[key] = _plain(spec[key])
    return result


def _family_plan(signature):
    """Reusable drawing machinery; multiplicity and placement remain variants."""
    if signature["renderer"] != "panels":
        return copy.deepcopy(signature)
    nodes = [{key: value for key, value in row.items() if key != "position"}
             for row in signature["panels"]]
    def runs(rows):
        result = []
        for row in rows:
            if not result or row != result[-1]:
                result.append(copy.deepcopy(row))
        return result
    plans = runs(nodes)
    mode = "single" if len(nodes) == 1 else "faceted" if len(plans) == 1 else "composition"
    relations = []
    for axis in ("x", "y"):
        groups = [row for row in signature["shared_axes"] if row["axis"] == axis]
        if not groups:
            continue
        covered = {index for row in groups for index in row["panels"]}
        all_indices = set(range(len(nodes)))
        relation = ("all" if any(set(row["panels"]) == all_indices for row in groups)
                    else "partitioned" if covered == all_indices else "partial")
        shared_plans = []
        for row in groups:
            group_plan = runs([nodes[index] for index in row["panels"]])
            if group_plan not in shared_plans:
                shared_plans.append(group_plan)
        relations.append({"axis": axis, "relationship": relation, "plans": shared_plans})
    return {"renderer": "panels", "mode": mode, "plans": plans, "shared_relations": relations}


def family_for_spec(spec):
    """Identify a reusable family and a strict structural variant within it.

    Facet counts, grid positions, spans and panel ratios identify variants;
    scientific encodings, transformations, layers and shared relationships
    identify families. The original specification remains the rendering source.
    """
    signature = drawing_signature(spec)
    raw = json.dumps(signature, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    plan = _family_plan(signature)
    family_raw = json.dumps(plan, ensure_ascii=False, sort_keys=True, separators=(",", ":"), allow_nan=False)
    grammar = ([row["kind"] for row in signature["panels"]] if signature["renderer"] == "panels"
               else [signature["renderer"] + ":" + signature["kind"]])
    panel_count = len(grammar)
    if signature["renderer"] == "template":
        panel_count = {"mechanism_overview": 5, "benchmark_atlas": 5, "ablation_interactions": 5,
                       "scaling_robustness": 6, "representation_diagnostics": 5,
                       "biological_atlas": 4, "paired_effects": 4, "calibration_errors": 6,
                       "sensitivity_dynamics": 4}.get(signature["kind"], 1)
        if signature["kind"] == "sensitivity_dynamics" and spec.get("data", {}).get("panel_pair") in {"sensitivity", "dynamics"}:
            panel_count = 2
    elif signature["renderer"] == "layout":
        panel_count = (len(spec.get("data", {}).get("tracks", [])) or 1) if signature["kind"] == "aligned_tracks" else 3
    return {"id": "figure-family-" + hashlib.sha256(family_raw.encode("utf-8")).hexdigest()[:16],
            "variant_id": "figure-variant-" + hashlib.sha256(raw.encode("utf-8")).hexdigest()[:16],
            "signature": signature, "family_signature": plan, "grammar": grammar,
            "panel_count": panel_count,
            "features": sorted(set(re.findall(r'"([a-z_]+)":true', raw)))}


def _panel_structure(kinds, columns=None, positions=None, overrides=None):
    columns = columns or (2 if len(kinds) == 4 else min(3, len(kinds)))
    panels = []
    for i, kind in enumerate(kinds):
        data = {field: [None] for field in explain(kind)["required"]}
        data.update((overrides or {}).get(str(i), {}))
        panels.append({"id": "p" + str(i), "kind": kind, "row": i // columns,
                       "column": i % columns, "data": data})
        if positions:
            panels[-1].update(positions[i])
    rows = max(panel["row"] + panel.get("rowspan", 1) for panel in panels)
    return {"version": 1, "rows": rows, "columns": columns, "panels": panels}


def _fusion_structure(row):
    layout = row.get("layout", {})
    return _panel_structure(row["panels"], layout.get("columns"), layout.get("positions"))


def _chart_family(kind, available=None):
    spec = _panel_structure([kind])
    if available:
        for key in set(available) & {key for fields in _FEATURE_FIELDS.values() for key in fields}:
            spec["panels"][0]["data"].setdefault(key, [None])
    return family_for_spec(spec)


def _standard_family_inputs():
    entries, specs = [], {}
    for chart in catalog()["charts"]:
        key = "primitive:" + chart["id"]
        entries.append({"id": key, "title": chart["title"], "type": "primitive",
                        "intent_ids": chart["intents"], "why": chart["why"]})
        specs[key] = _panel_structure([chart["id"]])
    for row in catalog()["fusions"]:
        key = "fusion:" + row["id"]
        entries.append({"id": key, "title": row["title"], "type": "fusion",
                        "intent_ids": row.get("primary_intents", []), "why": row["why"]})
        specs[key] = _fusion_structure(row)
    for row in json.loads((LIBRARY / "examples.json").read_text(encoding="utf-8")):
        entries.append({**row, "type": row["category"], "intent_ids": row.get("intents", [])})
        declarations = row.get("drawing_options", {})
        if not isinstance(declarations, dict):
            raise ValueError("Example drawing_options must be an object")
        declared_data = copy.deepcopy(declarations)
        if row.get("layout"):
            specs[row["id"]] = {"version": 1, "layout": row["layout"], "data": declared_data}
        else:
            declared_data["panel_pair"] = row.get("panel_pair", "all")
            specs[row["id"]] = {"version": 1, "template": row["template"],
                                "data": declared_data}
    for row in json.loads((LIBRARY / "studies.json").read_text(encoding="utf-8")):
        key = "paper:" + row["id"]
        entries.append({"id": key, "title": row["short_title"], "type": "study",
                        "intent_ids": row.get("intents", []), "why": row["why"],
                        "source_id": row["source_id"]})
        specs[key] = ({"version": 1, "layout": row["native_layout"], "data": {}}
                      if row.get("native_layout") else _panel_structure(row["panel_plan"], row.get("columns"), overrides=row.get("panel_overrides")))
    return entries, specs


def families(entries=None, *, specs=None):
    """Group catalog or supplied gallery entries without deleting contextual aliases.

    For a rendered gallery, pass its actual specs keyed by entry ID. Entries
    without a specification (legacy assets/atlas) remain distinct. No supplied
    path is opened or source file executed by this function.
    """
    if entries is None:
        entries, specs = _standard_family_inputs()
    if not isinstance(entries, list) or not isinstance(specs, dict):
        raise ValueError("Supply entries and their specifications keyed by ID")
    groups, seen = {}, set()
    priority = {"featured": -1, "reference": 0, "composition": 1, "template": 1, "original": 1, "fusion": 2, "linked": 3, "layout": 3, "study": 4, "paper": 4, "primitive": 5}
    for row in entries:
        key = row.get("id")
        if not isinstance(key, str) or not key or key in seen:
            raise ValueError("Family members need unique nonempty IDs")
        seen.add(key)
        asset_hash = hashlib.sha256(key.encode("utf-8")).hexdigest()[:16]
        identity = (family_for_spec(specs[key]) if key in specs else
                    {"id": "asset-family-" + asset_hash, "variant_id": "asset-variant-" + asset_hash,
                     "signature": {"asset": key}, "family_signature": {"asset": key},
                     "grammar": [], "panel_count": 0, "features": []})
        family = groups.setdefault(identity["id"], {"members": [], "identities": {}})
        family["identities"][key] = identity
        family["members"].append({name: row[name] for name in ("id", "title", "type", "category", "why", "intent_ids", "source_id") if name in row})
    result = []
    for family in groups.values():
        members = family["members"]
        representative = min(members, key=lambda row: (priority.get(row.get("type", row.get("category")), 9), row["id"]))
        identity = family["identities"][representative["id"]]
        variants = {}
        for member in members:
            member_identity = family["identities"][member["id"]]
            variant = variants.setdefault(member_identity["variant_id"], {
                "id": member_identity["variant_id"], "signature": member_identity["signature"],
                "panel_count": member_identity["panel_count"], "members": []})
            variant["members"].append(member)
        variant_rows = []
        for variant in variants.values():
            preferred = min(variant["members"], key=lambda row: (priority.get(row.get("type", row.get("category")), 9), row["id"]))
            variant_rows.append({"id": variant["id"], "signature": variant["signature"],
                                 "panel_count": variant["panel_count"], "title": preferred.get("title", preferred["id"]),
                                 "representative_id": preferred["id"], "member_ids": [row["id"] for row in variant["members"]]})
        result.append({**identity, "members": members,
                       "title": representative.get("title", representative["id"]),
                       "representative_id": representative["id"], "member_ids": [row["id"] for row in members],
                       "why": representative.get("why", "Same declared drawing structure; inspect each member's scientific conditions."),
                       "intent_ids": sorted({value for row in members for value in row.get("intent_ids", [])}),
                       "variant_count": len(variant_rows), "variants": variant_rows,
                       "level": "composition" if identity["signature"].get("renderer") in {"template", "layout"} or identity["panel_count"] > 1 else "primitive"})
    result.sort(key=lambda row: row["level"] != "primitive")
    return {"version": 1, "total_examples": len(entries), "total_families": len(result),
            "total_variants": sum(row["variant_count"] for row in result), "families": result}


def _nonnegative_integer(value, name):
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _usage(state):
    if state is None:
        return {}
    if not isinstance(state, dict) or state.get("version") != 1 or not isinstance(state.get("counts"), dict):
        raise ValueError("Usage state must contain version=1 and counts")
    for key, value in state["counts"].items():
        explain(key)
        _nonnegative_integer(value, "Usage count")
    return state["counts"]


def _matches(term, text):
    term=term.casefold()
    if term.isascii():
        return re.search(r"(?<![a-z0-9_])"+re.escape(term)+r"(?![a-z0-9_])",text) is not None
    return term in text


def _brief(context):
    if context is None:return {}
    if not isinstance(context,dict) or context.get("version",1)!=1 or isinstance(context.get("version"),bool):
        raise ValueError("Figure brief must be an object with version=1")
    allowed={"version","question","claim","section","domain","intent_ids","data","layout","preferred_charts","exclude_charts"}
    if set(context)-allowed:raise ValueError(f"Unknown brief fields: {sorted(set(context)-allowed)}")
    result=copy.deepcopy(context)
    for name in ("question","claim","section","domain"):
        if name in result and not isinstance(result[name],str):raise ValueError(f"Brief {name} must be text")
    for name in ("intent_ids","preferred_charts","exclude_charts"):
        if name in result and (not isinstance(result[name],list) or not all(isinstance(v,str) for v in result[name])):
            raise ValueError(f"Brief {name} must be a list of IDs")
    if set(result.get("intent_ids",[]))-set(catalog()["intents"]):raise ValueError("Unknown brief analytical intent")
    known={row["id"] for row in catalog()["charts"]}
    if (set(result.get("preferred_charts",[]))|set(result.get("exclude_charts",[])))-known:
        raise ValueError("Unknown chart in figure brief")
    data=result.setdefault("data",{});layout=result.setdefault("layout",{})
    if not isinstance(data,dict) or not isinstance(layout,dict):raise ValueError("Brief data and layout must be objects")
    flags={"paired","ordered_x","checkpoint_order","raw_samples","intervals_supplied","quantiles_supplied","complete_grid","embedding_supplied","composition","survival_estimate","counts_supplied"}
    amounts={"sample_count","category_count","component_count"}
    if set(data)-(flags|amounts|{"fields","observation_unit"}):raise ValueError("Unknown brief data property")
    for key in flags:
        if key in data and not isinstance(data[key],bool):raise ValueError(f"Brief data.{key} must be true or false")
    for key in amounts:
        if key in data:_nonnegative_integer(data[key],key)
    if "fields" in data and (not isinstance(data["fields"],list) or not all(isinstance(v,str) for v in data["fields"])):
        raise ValueError("Brief data.fields must list parameter names")
    if "observation_unit" in data and not isinstance(data["observation_unit"],str):raise ValueError("Observation unit must be text")
    if set(layout)-{"width_mm","height_mm","max_panels","long_labels"}:raise ValueError("Unknown brief layout property")
    for key in ("width_mm","height_mm"):
        if key in layout and (isinstance(layout[key],bool) or not isinstance(layout[key],(int,float)) or not math.isfinite(layout[key]) or layout[key]<=0):
            raise ValueError(f"Brief {key} must be finite and positive")
    if "long_labels" in layout and not isinstance(layout["long_labels"],bool):raise ValueError("long_labels must be boolean")
    if "max_panels" in layout and (isinstance(layout["max_panels"],bool) or not isinstance(layout["max_panels"],int) or not 1<=layout["max_panels"]<=12):raise ValueError("max_panels must be between 1 and 12")
    return result


def _paper_fit(entry,brief):
    data=brief.get("data",{});layout=brief.get("layout",{});reasons=[];checks=[];score=0
    for name,required in entry.get("data_requirements",{}).items():
        if name in data:
            if data[name]!=required:return None,[],[f"Requires {name}={required}; the paper brief states {data[name]}"]
            reasons.append(f"Matches declared {name}={required}")
        else:checks.append(f"Confirm {name}={required} before using this chart")
    kind=entry["id"]
    if kind=="ternary" and "component_count" in data and data["component_count"]!=3:
        return None,[],["A ternary chart needs exactly three composition parts"]
    if data.get("paired") and kind in ("dumbbell","mean_delta","bland_altman","paired_distribution"):
        score+=3;reasons.append("Preserves the paper's matched observation units")
    if data.get("ordered_x") is False and data.get("checkpoint_order") and kind=="ordered_trajectory":
        score+=5;reasons.append("Retains checkpoint order even when the state axis folds back")
    if layout.get("long_labels") and entry.get("horizontal_labels"):
        score+=3;reasons.append("Horizontal labels fit the declared long category names")
    if data.get("sample_count",0)>300 and kind=="density_map":
        score+=2;reasons.append("Local counts reveal overlap in many observations")
    if 0<data.get("sample_count",0)<20 and kind in ("density_map","ridgeline"):
        score-=4;reasons.append("Few observations favor showing individual values")
    if layout.get("width_mm",183)<100 and kind=="parallel_coordinates" and data.get("category_count",0)>6:
        score-=5;reasons.append("Many profiles are difficult to separate at this paper width")
    if kind in brief.get("preferred_charts",[]):
        score+=20;reasons.append("Matches an explicit article design preference")
    return score,reasons,checks


def _input_compatible(entry, available, excluded):
    return entry["id"] not in excluded and (available is None or set(entry["required"]).issubset(available))


def element_plan(kind, fields=None):
    """A small evidence-gated plan; keys/labels alone are not analytical layers."""
    entry=next((row for row in catalog()["charts"] if row["id"]==kind),None)
    if entry is None:raise ValueError("Unknown chart grammar")
    available=set(fields or [])
    roles=list(entry.get("analysis_elements",[]))
    additions=[]
    if {"lower","upper"}<=available or {"series.lower","series.upper"}<=available:
        additions.append("supplied_range")
    if "corridor" in available:
        additions.extend(["conditional_region","threshold_boundaries","conditional_state_share"])
        weights="weights" in available or "corridor.weights" in available
        weight_kind="weight_kind" in available or "corridor.weight_kind" in available
        if weights and ("counts" not in available or weight_kind):additions.append("weighted_share")
    if "reference_value" in available:additions.append("supplied_reference")
    if "threshold" in available and "conditional_region" not in additions:additions.append("supplied_threshold")
    if "annotations" in available or "annotate" in available:additions.append("selected_value_labels")
    analytical=[r for r in roles+additions if r!="selected_value_labels"]
    return {"base":roles,"add_from_supplied_data":additions,
            "needs_enrichment":len(set(analytical))<2,
            "rule":"Select supported relationships from the article; legends and labels do not replace analysis."}


def describe_plot(kind, data=None):
    entry=next((row for row in catalog()["charts"] if row["id"]==kind),None)
    if entry is None:raise ValueError("Unknown chart grammar")
    data=data or {}
    def supplied(value):
        return value is not None and value is not False and not (isinstance(value,(list,dict,str,tuple)) and len(value)==0)
    fields={key for key,value in data.items() if supplied(value)}
    for name in ("series","corridor","summary"):
        value=data.get(name)
        blocks=value if isinstance(value,list) else [value]
        for block in blocks:
            if isinstance(block,dict):fields.update(name+"."+key for key,value in block.items() if supplied(value))
    inputs=list(entry.get("input_types",[]))
    if kind=="binned_summary":inputs=["quantile_summaries"] if data.get("summary") is not None else ["grouped_samples"]
    if kind=="density_map":inputs=["binned_counts"] if data.get("counts") is not None else ["raw_xy"]
    plan=element_plan(kind,fields)
    return {"input_types":inputs,"chart_types":entry.get("chart_types",[]),"element_plan":plan}


def route(question=None, *, fields=None, count=3, seed=None, usage=None, exclude=(), context=None, input_type=None, chart_type=None):
    """Sample without replacement from equally relevant, data-compatible charts.

    Does not mutate history. Record a selection only after accepting it. A local
    revision reuses the accepted composition, not a new route call.
    """
    brief=_brief(context)
    if input_type is not None and input_type not in catalog().get("input_types",{}):raise ValueError("Unknown input data type")
    if chart_type is not None and chart_type not in catalog().get("chart_types",{}):raise ValueError("Unknown chart type")
    question=question or brief.get("question") or brief.get("claim")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Supply a scientific question or intent")
    if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 12:
        raise ValueError("count must be between 1 and 12")
    if seed is not None:_nonnegative_integer(seed, "seed")
    counts = _usage(usage)
    text = " ".join([question,brief.get("claim","")]).casefold()
    if fields is not None and (isinstance(fields,str) or not all(isinstance(v,str) for v in fields)):
        raise ValueError("fields must be a list of parameter names")
    known_fields=brief.get("data",{}).get("fields")
    if fields is not None and known_fields is not None and set(fields)!=set(known_fields):
        raise ValueError("CLI fields and paper brief fields disagree")
    available = None if fields is None and known_fields is None else set(fields if fields is not None else known_fields)
    named_text=question.casefold()
    named=next((entry for entry in catalog()["charts"] if entry["id"]==named_text),None)
    # A chosen exemplar is a rendering contract, not another semantic search.
    selection_name=named_text
    for prefix,target in (("template--","original:"),("reference--","reference:"),("linked--","layout:"),
                          ("fusion--","fusion:"),("study--","paper:")):
        if selection_name.startswith(prefix):selection_name=target+selection_name[len(prefix):];break
    pinned=next((entry for entry in examples() if entry["id"].casefold()==selection_name
                 or (entry.get("category")=="original" and entry.get("template")==named_text)),None)
    if pinned:
        return {"question":question,"selection_policy":"selected_example","selected_example":copy.deepcopy(pinned),
                "candidates":[],"fields_checked":False,
                "reuse_command":"compose --spec <selected-example.json> --data <supplied-data.json> --out <prefix>",
                "instruction":"Reuse the selected JSON/Python. Replace its complete data with replace_data; retain layout, style and layers. Do not reroute or regenerate demo data."}
    intents = list(brief.get("intent_ids",[]))
    for key, entry in catalog()["intents"].items():
        if text == key or any(_matches(term,text) for term in entry["terms"]):
            if key not in intents:intents.append(key)
    if not intents:
        if named:intents=list(named["intents"])
        else:raise ValueError("No intent matched; use an intent ID from --list or state the scientific relationship")
    exclude=set(exclude)|set(brief.get("exclude_charts",[]))
    unknown = set(exclude) - {c["id"] for c in catalog()["charts"]}
    if unknown:
        raise ValueError(f"Unknown excluded charts: {sorted(unknown)}")
    candidates = [];fit_info={};rejected=[]
    for entry in catalog()["charts"]:
        if input_type is not None and input_type not in entry.get("input_types",[]):continue
        if chart_type is not None and chart_type not in entry.get("chart_types",[]):continue
        if named and entry["id"]!=named["id"]:continue
        if not _input_compatible(entry,available,exclude) or not set(entry["intents"]) & set(intents):
            continue
        fit,reasons,checks=_paper_fit(entry,brief)
        if fit is None:
            rejected.append({"id":entry["id"],"reason":checks[0]});continue
        score = 10 * len(set(entry["intents"]) & set(intents))
        score += sum(1 for term in entry.get("terms", []) if _matches(term,text))
        score+=fit;fit_info[entry["id"]]=(reasons,checks)
        candidates.append((score, entry))
    result={"question":question,"intents":intents,"randomness":"automatic" if seed is None else "explicit legacy diagnostic seed",
            "fields_checked":available is not None,"candidates":[]}
    rng = random.SystemRandom() if seed is None else random.Random(seed)
    if seed is not None:result["seed"]=seed
    if brief:
        result["paper_context"]={key:brief[key] for key in ("claim","section","domain") if key in brief}
        result["paper_conditions_checked"]=bool(brief.get("data"))
        layout=brief.get("layout",{})
        fits=[]
        for fusion in catalog()["fusions"]:
            if not set(fusion.get("primary_intents",[])).intersection(intents):continue
            members=[explain(kind) for kind in fusion["panels"]]
            if input_type is not None and not all(input_type in row.get("input_types",[]) for row in members):continue
            if chart_type is not None and not any(chart_type in row.get("chart_types",[]) for row in members):continue
            if not all(_input_compatible(entry,available,exclude) for entry in members):continue
            if len(fusion["panels"])>layout.get("max_panels",12):continue
            meanings=set().union(*(set(explain(kind)["intents"]) for kind in fusion["panels"]))
            if not meanings.intersection(intents):continue
            # A narrow final-size column needs a vertical/custom arrangement.
            columns=fusion.get("layout",{}).get("columns",min(3,len(fusion["panels"])))
            if layout.get("width_mm",183)/columns<38:continue
            rows=fusion.get("layout",{}).get("rows",math.ceil(len(fusion["panels"])/columns))
            if "height_mm" in layout and layout["height_mm"]/rows<32:continue
            member_fits=[_paper_fit(entry,brief) for entry in {row["id"]:row for row in members}.values()]
            if any(fit is None for fit,_,_ in member_fits):continue
            # Prefer the article's main relationships and declared design before
            # considering variety. Repeated slice panels do not earn extra fit.
            primary=set(fusion.get("primary_intents",[])).intersection(intents)
            score=10*len(primary)+3*len(meanings.intersection(intents)-primary)+sum(fit for fit,_,_ in member_fits)
            option={"id":fusion["id"],"title":fusion["title"],"why":fusion["why"],
                         "alignment_contract":fusion["alignment_contract"],"panels":list(fusion["panels"]),
                         "data_bindings_required":True,"score":score,
                         "paper_fit":list(dict.fromkeys(reason for _,reasons,_ in member_fits for reason in reasons))}
            family = family_for_spec(_fusion_structure(fusion))
            option["family_id"] = family["id"]
            option["variant_id"] = family["variant_id"]
            fits.append((score,option))
        selected_fusions=[]
        while fits and len(selected_fusions)<3:
            best=max(score for score,_ in fits)
            tier=[item for item in fits if item[0]==best]
            weights=[1/(1+sum(counts.get(kind,0) for kind in set(option["panels"]))/len(set(option["panels"]))) for _,option in tier]
            chosen=rng.choices(tier,weights=weights,k=1)[0]
            selected_fusions.append(chosen[1])
            fits=[item for item in fits if item[1]["family_id"] != chosen[1]["family_id"]]
        result["fusion_options"]=selected_fusions
    if rejected:result["incompatible_charts"]=rejected
    if not candidates:
        result["reason"]="No compatible chart; resolve the stated data conditions or retain the existing figure"
        return result
    selected = []
    while candidates and len(selected) < count:
        # Never trade semantic fit for variety. Balance only the current best tier.
        best = max(score for score, _ in candidates)
        tier = [(score, entry) for score, entry in candidates if score == best]
        weights = [1 / (1 + counts.get(entry["id"], 0)) for _, entry in tier]
        chosen = rng.choices(tier, weights=weights, k=1)[0]
        score, entry = chosen
        family = _chart_family(entry["id"])
        family_id = family["id"]
        selected.append({"id": entry["id"], "title": entry["title"], "score": score,
                         "input_types":entry.get("input_types",[]),"chart_types":entry.get("chart_types",[]),
                         "element_plan":element_plan(entry["id"],available),
                         "why": entry["why"], "required": list(entry["required"]),
                         "paper_fit":fit_info[entry["id"]][0],"check_before_use":fit_info[entry["id"]][1],
                         "previous_selections": counts.get(entry["id"], 0),
                         "family_id": family_id,
                         "variant_id": family["variant_id"],
                         "design_card": f"explain {entry['id']}"})
        candidates = [item for item in candidates if _chart_family(item[1]["id"])["id"] != family_id]
    result.update(selection_policy="paper meaning and declared data conditions, one candidate per declared drawing family, then random choice within the best fit; optional history breaks ties",
                  candidates=selected)
    return result


def record_selection(state_path, kinds):
    """Update one task-owned history only for accepted/used charts."""
    path = Path(state_path)
    state = json.loads(path.read_text(encoding="utf-8")) if path.exists() else {"version": 1, "counts": {}}
    _usage(state)
    if not kinds:
        raise ValueError("Supply at least one accepted chart")
    for kind in kinds:
        explain(kind)
    result = copy.deepcopy(state)
    for kind in kinds:
        result["counts"][kind] = result["counts"].get(kind, 0) + 1
    _write_json(path, result)
    return result


def _write_json(path, value):
    path = Path(path)
    content = json.dumps(value, ensure_ascii=False, indent=2, allow_nan=False) + "\n"
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, temp = tempfile.mkstemp(prefix=".ccfa-chart-", suffix=".json", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8", newline="\n") as stream:
            stream.write(content)
        os.replace(temp, path)
    finally:
        if Path(temp).exists():
            Path(temp).unlink()


def _renderer(kind):
    entry = explain(kind)
    if entry["module"] == "ccfa_analysis_panels":
        import ccfa_analysis_panels as module
        return getattr(module, kind)
    if entry["module"] == "ccfa_semantic_panels":
        import ccfa_semantic_panels as module
        return module.REGISTRY[kind]["function"]
    raise ValueError("Unsupported chart implementation")


def _palette_data(kind,data,palette):
    """Color visual channels, never remap a quantitative colormap by accident."""
    from ccfa_plot_recipes import PALETTES
    result=copy.deepcopy(data);colors=PALETTES[palette]
    group_fields={"comparison_intervals":"labels","pareto_scatter":"labels",
        "paired_distribution":"labels","forest_intervals":"labels","raincloud":"labels",
        "ridgeline":"labels","ranked_intervals":"labels","rank_trajectories":"labels",
        "parallel_coordinates":"labels","mosaic_composition":"component_labels",
        "grouped_dot":"series_labels","robustness_profile":"labels","cost_quality_frontier":"labels",
        "quadrant_scatter":"labels","mean_delta":"labels",
        "binned_group_composition":"group_order"}
    if kind in group_fields and result.get("colors") is None:
        result["colors"]=[colors[i%len(colors)] for i in range(len(result[group_fields[kind]]))]
    elif kind=="embedding_scatter" and result.get("colors") is None:
        groups=result.get("order") or list(dict.fromkeys(result["groups"]))
        result["colors"]={key:colors[i%len(colors)] for i,key in enumerate(groups)}
    elif kind in ("dumbbell","signed_effects","mirrored_histogram","mirror_stem") and result.get("colors") is None:
        result["colors"]=list(colors[:2])
    elif kind in ("volcano","matrix_bubbles") and result.get("colors") is None:
        result["colors"]=[colors[0],"#F4F4F4",colors[1]]
    elif kind=="transition_matrix" and result.get("colors") is None:
        result["colors"]=["#F4F4F4",colors[0]]
    if "color" in inspect.signature(_renderer(kind)).parameters and result.get("color") is None:
        result["color"]=colors[0]
    if kind=="binned_summary" and "line_color" not in result:result["line_color"]=colors[1]
    if kind=="category_comparison":
        if "bar_color" not in result:result["bar_color"]=colors[0]
        for i,series in enumerate(result["series"]):
            if "color" not in series:series["color"]=colors[(i+1)%len(colors)]
    return result


def _entity_sequence(kind,data):
    field={"comparison_intervals":"labels","pareto_scatter":"labels","paired_distribution":"labels",
           "forest_intervals":"labels","raincloud":"labels","ridgeline":"labels","ranked_intervals":"labels",
           "rank_trajectories":"labels","parallel_coordinates":"labels","grouped_dot":"series_labels",
           "robustness_profile":"labels","cost_quality_frontier":"labels","quadrant_scatter":"labels",
           "mean_delta":"labels","mosaic_composition":"component_labels","binned_group_composition":"group_order"}.get(kind)
    if field:return list(data[field])
    if kind=="embedding_scatter":return list(data.get("order") or dict.fromkeys(data["groups"]))
    return None


def _categorical_axes(kind,data):
    """Describe category identities at actual slots, not scatter annotations."""
    horizontal={"comparison_intervals","forest_intervals","raincloud","ridgeline",
                "dumbbell","signed_effects","grouped_dot","ranked_intervals"}
    vertical={"binned_summary","category_comparison","paired_distribution"}
    if kind in horizontal|vertical:
        labels=list(data["labels"])
        if kind=="ranked_intervals" and data.get("order","input")!="input":
            indices=sorted(range(len(labels)),key=lambda i:data["values"][i])
            if data["order"]=="descending":indices.reverse()
            labels=[labels[i] for i in indices]
        return {"y" if kind in horizontal else "x":(labels,list(range(len(labels))))}
    if kind in ("matrix_heatmap","dot_matrix","matrix_bubbles","transition_matrix"):
        offset=.5 if kind in ("matrix_heatmap","transition_matrix") else 0
        rows=list(data["labels"] if kind=="transition_matrix" else data["row_labels"])
        cols=list(data["labels"] if kind=="transition_matrix" else data["col_labels"])
        return {"x":(cols,[i+offset for i in range(len(cols))]),
                "y":(rows,[i+offset for i in range(len(rows))])}
    if kind=="rank_trajectories":
        labels=list(data["stages"])
        return {"x":(labels,list(range(len(labels))))}
    if kind=="parallel_coordinates":
        labels=[(name,tuple(bounds)) for name,bounds in zip(data["dimensions"],data["ranges"])]
        return {"x":(labels,list(range(len(labels))))}
    if kind=="mosaic_composition":
        totals=[sum(row) for row in data["counts"]];total=sum(totals)
        if total<=0 or any(value<=0 for value in totals):
            raise ValueError("Mosaic groups need positive supplied denominators")
        centers=[];left=0
        for value in totals:
            width=value/total;centers.append(left+width/2);left+=width
        return {"x":(list(data["group_labels"]),centers)}
    return {}


def _check_categorical_axis(existing,current):
    labels,slots=existing;other_labels,other_slots=current
    if labels!=other_labels or len(slots)!=len(other_slots) or any(
            not math.isclose(a,b,rel_tol=1e-10,abs_tol=1e-10) for a,b in zip(slots,other_slots)):
        raise ValueError("Categorical axes require identical ordered categories and coordinate slots; align supplied data explicitly")


def _entity_payload(node,palette,enc):
    """Apply the same explicit and inferred entity policy to panels and layers."""
    kind,data=node["kind"],node["data"]
    payload=_palette_data(kind,data,palette)
    actual=_entity_sequence(kind,data)
    if actual and data.get("colors") is None:
        if any(key not in enc for key in actual):
            raise ValueError("Declare plotted group labels in entity_order")
        payload["colors"]={key:enc[key]["color"] for key in actual} if kind=="embedding_scatter" else [enc[key]["color"] for key in actual]
    if "entity_ids" in node:
        entity_ids=node["entity_ids"]
        if (not isinstance(entity_ids,list) or not entity_ids or
                not all(isinstance(key,str) and key in enc for key in entity_ids) or
                len(set(entity_ids))!=len(entity_ids)):
            raise ValueError("Declare unique panel or layer entity IDs in entity_order")
        argument=node.get("color_argument","colors")
        if argument not in ("colors","color") or argument not in inspect.signature(_renderer(kind)).parameters:
            raise ValueError("Renderer does not support this entity color argument")
        if argument=="color" and len(entity_ids)!=1:
            raise ValueError("A single color requires a single entity ID")
        if argument=="colors" and actual!=entity_ids:
            raise ValueError("Entity IDs must match the actual plotted group labels and order")
        payload[argument]=[enc[key]["color"] for key in entity_ids] if argument=="colors" else enc[entity_ids[0]]["color"]
        if kind=="embedding_scatter":payload[argument]={key:enc[key]["color"] for key in entity_ids}
    return payload


def demo_data(kind, seed=None):
    """Explicit simulation entrypoint, never used by the real-data renderer."""
    entry = explain(kind)
    if entry["module"] == "ccfa_semantic_panels":
        import ccfa_semantic_panels as module
        return _plain(module.demo_data(kind, seed=seed))
    import numpy as np
    rng = np.random.default_rng(seed)
    labels = ["Base", "Variant", "Proposed"]
    samples = [rng.normal(m, .065, 45).tolist() for m in [.58, .68, .77]]
    x = np.arange(1, 9)
    options = {
        "comparison_intervals": dict(labels=labels, values=[.58, .68, .77], lower=[.55, .65, .73], upper=[.61, .71, .81], runs=samples, xlabel="Score"),
        "line_band": dict(x=x.tolist(), y=(.5+.3*(1-np.exp(-x/3))).tolist(), lower=(.46+.3*(1-np.exp(-x/3))).tolist(), upper=(.54+.3*(1-np.exp(-x/3))).tolist(), xlabel="Budget", ylabel="Score"),
        "density_map": dict(x=(z := rng.normal(size=450)).tolist(), y=(.65*z+rng.normal(0,.55,len(z))).tolist(), xlabel="Observed A", ylabel="Observed B"),
        "binned_summary": dict(samples=samples, labels=labels, ylabel="Observed value"),
        "category_comparison": dict(labels=["A", "B", "C", "D"], bars=[.15,.3,.35,.2], series=[{"label":"After", "values":[.2,.25,.3,.25]}]),
        "matrix_heatmap": dict(values=rng.uniform(.4,.9,(4,4)).tolist(), row_labels=["A","B","C","D"], col_labels=["W","X","Y","Z"]),
        "dot_matrix": dict(values=rng.normal(size=(4,3)).tolist(), sizes=rng.uniform(0,100,(4,3)).tolist(), row_labels=["A","B","C","D"], col_labels=labels),
        "pareto_scatter": dict(x=[1,2,3,4,6], y=[.53,.66,.63,.75,.78], labels=["A","B","C","D","E"]),
        "paired_distribution": dict(values=samples, labels=labels, paired=True),
        "embedding_scatter": dict(coordinates=np.concatenate([rng.normal([i, i%2],.3,(35,2)) for i in range(3)]).tolist(), groups=sum(([label]*35 for label in labels),[])),
        "forest_intervals": dict(labels=labels, estimates=[-.1,.08,.2], lower=[-.16,.01,.13], upper=[-.04,.15,.27]),
        "volcano": dict(effects=rng.normal(0,1.1,120).tolist(), probabilities=rng.uniform(.0002,1,120).tolist(), statistic="q"),
        "calibration": dict(confidence=[.1,.3,.5,.7,.9], accuracy=[.14,.28,.46,.65,.85], counts=[30,55,80,70,40]),
    }
    return options[kind]


def demo_spec(kinds, *, seed=None, columns=None, width_mm=183, title=""):
    if not kinds or len(kinds) > 12:
        raise ValueError("Use between one and twelve panels; split a larger figure into named groups")
    for kind in kinds:
        explain(kind)
    explicit_seed=seed
    if seed is None:seed=secrets.randbits(64)
    _nonnegative_integer(seed,"seed")
    columns = (2 if len(kinds)==4 else min(3,len(kinds))) if columns is None else columns
    if not isinstance(columns, int) or isinstance(columns, bool) or not 1 <= columns <= len(kinds):
        raise ValueError("columns must be a positive integer no larger than the panel count")
    rows = math.ceil(len(kinds) / columns)
    spec={"version": 1, "width_mm": width_mm, "height_mm": rows * (67 if columns <= 2 else 63) + 12,
            "columns": columns, "rows": rows, "title": title, "palette": "npg", "font": "serif",
            "panels": [{"id": f"panel-{i+1}", "kind": kind, "title": explain(kind)["title"],
                        "row": i // columns, "column": i % columns,
                        "data": demo_data(kind, seed=seed+i)} for i, kind in enumerate(kinds)],
            "_meta": {"synthetic": True, "randomness":"automatic" if explicit_seed is None else "explicit diagnostic seed",
                      "purpose": "chart-design demonstration; not original paper results"}}
    if explicit_seed is not None:spec["_meta"]["seed"]=explicit_seed
    _coherent_demo(spec,seed)
    if len(kinds)%columns:
        spec["panels"][-1]["colspan"]=columns-spec["panels"][-1]["column"]
    return spec


def demo_fusion(fusion_id, *, seed=None, columns=None):
    fusion=next((row for row in catalog()["fusions"] if row["id"]==fusion_id),None)
    if fusion is None:raise ValueError("Unknown fusion")
    spec=demo_spec(fusion["panels"],seed=seed,columns=columns,title=fusion["title"])
    layout=fusion.get("layout")
    if layout and columns is None:
        spec.update(rows=layout["rows"],columns=layout["columns"],height_mm=layout["height_mm"])
        for panel,position in zip(spec["panels"],layout["positions"]):
            panel.pop("colspan",None);panel.update(position)
    spec["_meta"].update(fusion=fusion_id,alignment_contract=fusion["alignment_contract"])
    return spec


def _coherent_demo(spec,seed):
    """Share actual simulated observations where panels claim a common origin."""
    import numpy as np
    rng=np.random.default_rng(seed)
    by_kind={kind:[panel for panel in spec["panels"] if panel["kind"]==kind]
             for kind in {panel["kind"] for panel in spec["panels"]}}
    linked=[]
    if "dumbbell" in by_kind or "mean_delta" in by_kind:
        key="dumbbell" if "dumbbell" in by_kind else "mean_delta"
        pair=by_kind[key][0]["data"]
        before,after=pair["before"],pair["after"]
        for kind in ("dumbbell","mean_delta"):
            for panel in by_kind.get(kind,[]):panel["data"].update(before=copy.deepcopy(before),after=copy.deepcopy(after),labels=copy.deepcopy(pair["labels"]))
        for panel in by_kind.get("bland_altman",[]):panel["data"].update(first=copy.deepcopy(before),second=copy.deepcopy(after))
        linked.append("Matched before/after values shared across paired-change panels")
    if "raincloud" in by_kind:
        base=by_kind["raincloud"][0]["data"]
        for panel in by_kind.get("binned_summary",[]):panel["data"].update(samples=copy.deepcopy(base["samples"]),labels=copy.deepcopy(base["labels"]))
        for panel in by_kind.get("ecdf",[]):panel["data"]["samples"]=[value for group in base["samples"] for value in group]
        linked.append("Group observations reused for distributions and pooled ECDF")
    if "mirrored_histogram" in by_kind:
        base=by_kind["mirrored_histogram"][0]["data"]
        first,second=base["first"],base["second"]
        values=list(first)+list(second)
        for panel in by_kind.get("binned_group_composition",[]):
            panel["data"]={"values":values,"groups":["First"]*len(first)+["Second"]*len(second),
                           "bin_edges":list(base["bin_edges"]),"group_order":["First","Second"]}
        xlabel=base.get("xlabel","Observed value")
        for panel in by_kind.get("binned_group_composition",[]):panel["data"]["xlabel"]=xlabel
        for panel in by_kind.get("ecdf",[]):panel["data"].update(samples=values,xlabel=xlabel)
        linked.append("Mirrored counts, within-bin fractions and ECDF use the same observations and bin edges")
    if "convergence_envelope" in by_kind and "quantile_fan" in by_kind:
        base=by_kind["convergence_envelope"][0]["data"]
        for panel in by_kind["quantile_fan"]:
            panel["data"]={"x":base["steps"],"quantiles":np.quantile(base["runs"],[.1,.25,.5,.75,.9],axis=0).tolist(),
                           "probabilities":[.1,.25,.5,.75,.9],"xlabel":"Training step","ylabel":"Objective"}
        linked.append("Training quantiles computed from the displayed simulated runs")
    if "contour_response" in by_kind and "line_band" in by_kind:
        base=by_kind["contour_response"][0]["data"];surface=np.asarray(base["response"])
        for i,panel in enumerate(by_kind["line_band"]):
            if i%2==0:
                index=len(base["y"])//2;xx=base["x"];yy=surface[index,:];fixed=f"Control B={base['y'][index]:.2g}"
            else:
                index=len(base["x"])//2;xx=base["y"];yy=surface[:,index];fixed=f"Control A={base['x'][index]:.2g}"
            panel["data"]={"x":list(xx),"y":yy.tolist(),"xlabel":"Control A" if i%2==0 else "Control B","ylabel":"Response"}
            panel["title"]=fixed
        linked.append("Slices are extracted from the displayed response grid at named fixed conditions")
    if all(kind in by_kind for kind in ("calibration","risk_coverage","precision_recall")):
        confidence=rng.uniform(.03,.99,320);correct=rng.random(len(confidence))<(.08+.82*confidence)
        edges=np.linspace(0,1,9);bins=np.clip(np.searchsorted(edges,confidence,side="right")-1,0,len(edges)-2)
        counts=np.bincount(bins,minlength=8);means=np.array([confidence[bins==i].mean() for i in range(8)])
        accuracy=np.array([correct[bins==i].mean() for i in range(8)])
        order=np.argsort(-confidence);hits=np.cumsum(correct[order]);kept=np.arange(1,len(confidence)+1)
        for panel in by_kind["calibration"]:panel["data"]={"confidence":means.tolist(),"accuracy":accuracy.tolist(),"counts":counts.tolist(),"edges":edges.tolist()}
        for panel in by_kind["risk_coverage"]:panel["data"]={"coverage":(kept/len(confidence)).tolist(),"risk":(1-hits/kept).tolist()}
        for panel in by_kind["precision_recall"]:panel["data"]={"recall":(hits/correct.sum()).tolist(),"precision":(hits/kept).tolist(),"prevalence":float(correct.mean())}
        linked.append("Confidence/correctness observations share calibration bins and selective-prediction decisions")
    if linked:spec["_meta"]["shared_simulation_contracts"]=linked


def single_panel_spec(spec, panel_id, *, width_mm=88, height_mm=68):
    """Reuse one supplied panel and its layers without copying or resampling data.

    Resolve external tables before calling this helper. Keep the original
    figure's entity order so extraction cannot change category colors.
    Linked layouts and templates are atomic; they need their own explicit data
    specification rather than cropping a rendered image.
    """
    panels = spec.get("panels") if isinstance(spec, dict) else None
    if not isinstance(panels, list):
        raise ValueError("Select a panel from an explicit panels specification; linked layouts stay atomic")
    matches = [node for node in panels if node.get("id") == panel_id]
    if len(matches) != 1:
        raise ValueError("Select one existing, unique panel ID")
    if any(not math.isfinite(float(v)) or not 30 <= float(v) <= 1000 for v in (width_mm, height_mm)):
        raise ValueError("Use finite physical dimensions from 30 to 1000 mm")
    result = copy.deepcopy(spec)
    identities = copy.deepcopy(spec.get("entity_order", []))
    if not identities:
        for panel in panels:
            for node in [panel, *panel.get("layers", [])]:
                for name in (_entity_sequence(node["kind"], node["data"]) or []) + node.get("entity_ids", []):
                    if name not in identities:
                        identities.append(name)
    if identities:
        result["entity_order"] = identities
    node = copy.deepcopy(matches[0])
    node.update(row=0, column=0, rowspan=1, colspan=1)
    for key in ("shared_axes", "width_ratios", "height_ratios", "title"):
        result.pop(key, None)
    result.update(rows=1, columns=1, panels=[node], width_mm=float(width_mm), height_mm=float(height_mm), panel_letters=False)
    result.setdefault("_meta", {}).update(selected_panel=panel_id)
    return result




def _replacement_presentation(previous, supplied, *, kind=None, palette="npg"):
    """Carry visual controls, never missing observations or interval endpoints."""
    result=copy.deepcopy(supplied)
    visual={"color","bar_color","line_color","box_color","cmap","missing_color","alpha","band_alpha",
            "marker","markersize","linewidth","linestyle","font_size","tick_font_size","label_wrap",
            "bar_style","bar_labels","value_format","xscale","yscale","summary_mode","quantile","gridsize"}
    legend_visual={"loc","ncol","ncols","fontsize","title_fontsize","frameon","framealpha","edgecolor",
                   "facecolor","borderaxespad","handlelength","handletextpad","columnspacing","labelspacing",
                   "mode","bbox_to_anchor","markerfirst","alignment"}
    old_id=next((previous[k] for k in ("method","label") if isinstance(previous.get(k),str)),None)
    new_id=next((result[k] for k in ("method","label") if isinstance(result.get(k),str)),None)
    renamed=old_id is not None and new_id is not None and old_id!=new_id
    for key in visual:
        if key not in result and key in previous and not (renamed and key in {"color","marker","linestyle"}):
            result[key]=copy.deepcopy(previous[key])
    if "annotate" not in result and isinstance(previous.get("annotate"),bool):result["annotate"]=previous["annotate"]
    for key in ("legend","legend_options"):
        if key not in result and isinstance(previous.get(key),bool):result[key]=previous[key]
        if isinstance(previous.get(key),dict):
            retained={k:copy.deepcopy(v) for k,v in previous[key].items() if k in legend_visual}
            if key not in result and retained:result[key]=retained
            elif isinstance(result[key],dict):result[key]={**retained,**result[key]}
    for key,value in list(result.items()):
        old=previous.get(key)
        if key in ("legend","legend_options","_meta"):continue
        if isinstance(value,dict) and isinstance(old,dict):
            result[key]=_replacement_presentation(old,value,palette=palette)
        elif key=="series" and isinstance(value,list) and isinstance(old,list):
            def identity(row):
                return next(((k,row[k]) for k in ("method","label") if isinstance(row,dict) and isinstance(row.get(k),str)),None)
            indexed={identity(row):row for row in old if identity(row) is not None}
            # Duplicate or absent IDs do not justify positional style transfer.
            if len(indexed)==len(old):
                result[key]=[_replacement_presentation(indexed[identity(row)],row,palette=palette)
                             if identity(row) in indexed else copy.deepcopy(row) for row in value]
    from ccfa_plot_recipes import PALETTES
    for key in ("colors","entity_colors"):
        if key in result or key not in previous:continue
        old_ids=previous.get("methods") if key=="entity_colors" else (_entity_sequence(kind,previous) if kind else None)
        new_ids=result.get("methods") if key=="entity_colors" else (_entity_sequence(kind,result) if kind else None)
        colors=previous[key]
        if colors is None:continue
        if old_ids is None and new_ids is None and kind is not None:
            result[key]=copy.deepcopy(colors)  # Fixed channel roles, e.g. before/after or negative/neutral/positive.
        elif isinstance(old_ids,list) and isinstance(new_ids,list):
            mapped=colors if isinstance(colors,dict) else dict(zip(old_ids,colors)) if len(colors)==len(old_ids) else {}
            if any(key in mapped for key in new_ids):
                fallback=PALETTES[palette]
                result[key]=[mapped.get(name,fallback[i%len(fallback)]) for i,name in enumerate(new_ids)]
    return result


def replace_data(spec, supplied):
    """Replace complete data while keeping a selected figure's rendering plan.

    Templates/layouts accept their raw data object. Panel compositions accept
    {"panels":[{"id":...,"data":...,"layers":[{"data":...}, ...]}, ...]}.
    Every selected panel/layer must be supplied; otherwise old demonstration
    values could silently survive. Pure presentation controls are retained,
    with series styles matched by stable method/label identity, never index. Use normal table bindings in the source
    composition for CSV/TSV rather than mixing bindings with this raw-data API.
    """
    if not isinstance(spec,dict) or spec.get("version")!=1:
        raise ValueError("Data replacement requires an existing version=1 composition")
    if not isinstance(supplied,dict):raise ValueError("Replacement data must be an object")
    if "data_sources" in spec or "table" in spec:
        raise ValueError("Resolve table bindings before replacing data")
    result=copy.deepcopy(spec)
    if "template" in result or "layout" in result:
        if set(supplied)&{"version","template","layout","panels","data_sources","table"}:
            raise ValueError("Supply the template/layout data only; use compose --spec for a full composition")
        result["data"]=_replacement_presentation(result.get("data",{}),supplied,palette=result.get("palette","ccfa"))
        if "title" in supplied:result["title"]=supplied["title"]
        incoming_meta=supplied.get("_meta",{})
    else:
        if set(supplied)-{"panels","_meta"} or not isinstance(supplied.get("panels"),list):
            raise ValueError("Panel replacement needs a panels list with IDs and complete data/layers")
        panels=result.get("panels",[]);incoming=supplied["panels"]
        ids=[row.get("id") for row in incoming if isinstance(row,dict)]
        if len(ids)!=len(incoming) or len(ids)!=len(set(ids)) or set(ids)!={p["id"] for p in panels}:
            raise ValueError("Replacement must supply every panel ID exactly once")
        by_id={row["id"]:row for row in incoming}
        for panel in panels:
            node=by_id[panel["id"]]
            if set(node)-{"id","data","layers"} or not isinstance(node.get("data"),dict):
                raise ValueError("Panel replacement changes data only, not the selected drawing plan")
            layers=node.get("layers",[])
            if not isinstance(layers,list) or len(layers)!=len(panel.get("layers",[])):
                raise ValueError("Replacement must supply every selected overlay layer")
            for old,new in zip(panel.get("layers",[]),layers):
                if not isinstance(new,dict) or set(new)!={"data"} or not isinstance(new["data"],dict):
                    raise ValueError("Each replacement layer needs only its complete data object")
                old["data"]=_replacement_presentation(old["data"],new["data"],kind=old["kind"],palette=result.get("palette","npg"))
            panel["data"]=_replacement_presentation(panel["data"],node["data"],kind=panel["kind"],palette=result.get("palette","npg"))
        incoming_meta=supplied.get("_meta",{})
        identities=[]
        for panel in panels:
            for node in [panel,*panel.get("layers",[])]:
                for key in (_entity_sequence(node["kind"],node["data"]) or [])+node.get("entity_ids",[]):
                    if key not in identities:identities.append(key)
        previous=result.get("entity_order",[])
        if identities and not set(identities)<=set(previous):
            result["entity_order"]=(previous+[key for key in identities if key not in previous]
                                    if set(identities)&set(previous) else identities)
    if not isinstance(incoming_meta,dict):raise ValueError("Replacement _meta must be an object")
    meta=result.setdefault("_meta",{})
    provenance={key:meta.pop(key) for key in ("study_id","source_id","source_figure","fidelity") if key in meta}
    if provenance:meta["design_reference"]=provenance
    for key in ("synthetic","seed","randomness","shared_simulation_contracts","data_file"):
        meta.pop(key,None)
    if meta.get("purpose") and spec.get("_meta",{}).get("synthetic"):
        meta.pop("purpose",None)
    retained=[]
    if result.get("title"):retained.append({"scope":"figure","text":result["title"]})
    retained.extend({"scope":panel["id"],"text":panel["title"]} for panel in result.get("panels",[]) if panel.get("title"))
    meta.update(copy.deepcopy(incoming_meta));meta.update(data_replaced=True,data_status="supplied")
    if retained:meta["retained_text_to_check"]=retained
    return result


def compose(spec):
    """Compose an explicit panel plan without filling any missing data."""
    import matplotlib.pyplot as plt
    import ccfa_analysis_panels as p
    if not isinstance(spec, dict) or spec.get("version") != 1 or isinstance(spec.get("version"),bool):
        raise ValueError("Composition requires version=1")
    font_size = float(spec.get("font_size",8.5))
    if not math.isfinite(font_size) or not 6 <= font_size <= 24:
        raise ValueError("font_size must be between 6 and 24 pt")
    if "data_sources" in spec or "table" in spec or any("table" in panel for panel in spec.get("panels",[])):
        raise ValueError("Resolve declared data tables with load_composition before rendering")
    if "layout" in spec:
        if "panels" in spec or "template" in spec:raise ValueError("Use a linked layout, template, or panel composition")
        import ccfa_figure_layouts as linked
        data=copy.deepcopy(spec.get("data",{}))
        if spec.get("title"):data["title"]=spec["title"]
        if spec.get("_meta"):data["_meta"]=copy.deepcopy(spec["_meta"])
        return linked.render_layout(spec["layout"],data,width_mm=spec.get("width_mm",183),
            height_mm=spec.get("height_mm"),font=spec.get("font","serif"),palette=spec.get("palette","npg"),font_size=font_size)
    if "template" in spec:
        if "panels" in spec:raise ValueError("Use a template or panel composition")
        import ccfa_analysis_templates as templates
        data=copy.deepcopy(spec.get("data",{}))
        if spec.get("_meta"):data["_meta"]=copy.deepcopy(spec["_meta"])
        if spec.get("title"):data["title"]=spec["title"]
        return templates.render_template(spec["template"],data,palette=spec.get("palette","ccfa"),
            font=spec.get("font","serif"),font_size=font_size,width_mm=spec.get("width_mm",183),height_mm=spec.get("height_mm"))
    panels = spec.get("panels")
    if not isinstance(panels, list) or not 1 <= len(panels) <= 12:
        raise ValueError("Composition needs one to twelve supplied panels")
    rows, cols = spec.get("rows"), spec.get("columns")
    for value in (rows, cols):
        if isinstance(value, bool) or not isinstance(value, int) or not 1 <= value <= 12:
            raise ValueError("rows and columns must be integers between one and twelve")
    occupied, ids, plans = set(), set(), []
    category_domains={}
    for panel in panels:
        key = panel.get("id")
        if not isinstance(key, str) or not key or key in ids:
            raise ValueError("Panel IDs must be nonempty and unique")
        ids.add(key)
        function = _renderer(panel.get("kind"))
        data = panel.get("data")
        if not isinstance(data, dict):
            raise ValueError(f"Panel {key} requires supplied data")
        inspect.signature(function).bind(None, **data)
        domains=_categorical_axes(panel["kind"],data)
        layers=panel.get("layers",[])
        if not isinstance(layers,list) or len(layers)>8:
            raise ValueError("Use at most eight explicit layers per panel")
        for layer in layers:
            if not isinstance(layer,dict) or not isinstance(layer.get("data"),dict):
                raise ValueError("Each overlay needs its own supplied data")
            for axis in ("x","y"):
                if not panel.get(axis+"_meaning") or panel.get(axis+"_meaning")!=layer.get(axis+"_meaning"):
                    raise ValueError("Overlays require matching declared axis meanings and units")
            inspect.signature(_renderer(layer.get("kind"))).bind(None,**layer["data"])
            for axis,domain in _categorical_axes(layer["kind"],layer["data"]).items():
                if axis in domains:_check_categorical_axis(domains[axis],domain)
                else:domains[axis]=domain
            if set(layer.get("style",{})) - {"linestyle","marker","linewidth","alpha","markersize"}:
                raise ValueError("Only line appearance properties are supported in overlay style")
        r, c, rh, cw = panel.get("row"), panel.get("column"), panel.get("rowspan", 1), panel.get("colspan", 1)
        for value in (r, c, rh, cw):
            _nonnegative_integer(value, "Grid position/span")
        if not rh or not cw or r+rh > rows or c+cw > cols:
            raise ValueError("Panel span exceeds the declared layout")
        cells = {(i,j) for i in range(r,r+rh) for j in range(c,c+cw)}
        if cells & occupied:
            raise ValueError("Panel regions overlap")
        occupied.update(cells)
        category_domains[key]=domains
        plans.append((panel, function, data, r,c,rh,cw))
    width, height = float(spec.get("width_mm",183)), float(spec.get("height_mm",120))
    if not all(math.isfinite(v) and 30 <= v <= 1000 for v in (width,height)):
        raise ValueError("Use finite physical dimensions from 30 to 1000 mm")
    # Refuse geometries that can fit only by making final-size text unreadable.
    if width/cols < 38 or height/rows < 32:
        raise ValueError("Panels are too small; increase physical size or split the figure")
    palette = spec.get("palette","npg")
    from ccfa_plot_recipes import PALETTES
    if palette not in PALETTES:
        raise ValueError("Unknown palette")
    identities = spec.get("entity_order", [])
    if not identities:
        identities=[]
        for panel in panels:
            for node in [panel,*panel.get("layers",[])]:
                explicit=node.get("entity_ids",[])
                if not isinstance(explicit,list) or not all(isinstance(name,str) for name in explicit):
                    raise ValueError("entity_ids must be a list of entity names")
                for name in (_entity_sequence(node["kind"],node["data"]) or [])+explicit:
                    if name not in identities:identities.append(name)
    enc = p.entity_encoding(identities, palette=palette) if identities else {}
    with p.paper_style(spec.get("font","serif"),font_size):
        fig = p.new_figure(width_mm=width,height_mm=height)
        fig.set_layout_engine("constrained",w_pad=.025,h_pad=.03,wspace=.035,hspace=.045,
                              rect=(0,.055,1,.90 if spec.get("title") else .945))
        grid = fig.add_gridspec(rows,cols,width_ratios=spec.get("width_ratios"),height_ratios=spec.get("height_ratios"))
        axes = {}
        try:
            for i,(panel,function,data,r,c,rh,cw) in enumerate(plans):
                ax=fig.add_subplot(grid[r:r+rh,c:c+cw]); axes[panel["id"]]=ax
                payload=_entity_payload(panel,palette,enc)
                artist=function(ax,**payload)
                numeric_color_kinds={"matrix_heatmap","dot_matrix","matrix_bubbles","density_map","contour_response","transition_matrix"}
                if panel["kind"] in numeric_color_kinds and panel.get("colorbar",True) is not False:
                    mappable=artist
                    if isinstance(artist,dict):
                        mappable=next((artist[key] for key in ("mesh","contours","scatter") if key in artist),None)
                    label=panel.get("colorbar_label")
                    if not label:
                        label="Count" if panel["kind"]=="density_map" else ("Transition count" if payload.get("normalization")=="counts" else "Transition fraction") if panel["kind"]=="transition_matrix" else "Value"
                    fig.colorbar(mappable,ax=ax,label=label,fraction=.045,pad=.035)
                for layer in panel.get("layers",[]):
                    previous_limits={axis:getattr(ax,"get_"+axis+"lim")() for axis in ("x","y")}
                    layer_data=_entity_payload(layer,palette,enc)
                    layer_artist=_renderer(layer["kind"])(ax,**layer_data)
                    for axis,old_limits in previous_limits.items():
                        new_limits=getattr(ax,"get_"+axis+"lim")()
                        if (old_limits[0]>old_limits[1])!=(new_limits[0]>new_limits[1]):
                            raise ValueError("Overlays cannot reverse an existing axis direction")
                        low=min(*old_limits,*new_limits);high=max(*old_limits,*new_limits)
                        getattr(ax,"set_"+axis+"lim")((high,low) if old_limits[0]>old_limits[1] else (low,high))
                    if layer.get("style"):
                        from matplotlib.lines import Line2D
                        if not isinstance(layer_artist,Line2D):
                            raise ValueError("Line style requires a line renderer")
                        layer_artist.set(**layer["style"])
                for axis in ("x","y"):
                    scale=panel.get(axis+"scale")
                    if scale is not None:
                        if scale not in ("linear","log"):raise ValueError("Use linear or log axis scales")
                        interval=getattr(ax.dataLim,"interval"+axis)
                        if scale=="log" and min(interval)<=0:
                            raise ValueError("Log display cannot hide nonpositive supplied values or reference marks")
                        getattr(ax,"set_"+axis+"scale")(scale)
                if panel.get("legend"):
                    handles,labels=ax.get_legend_handles_labels()
                    if handles:p.compact_legend(ax,handles=handles,labels=labels,fontsize=max(7,font_size-1))
                heading = panel.get('title','')
                if spec.get("panel_letters", len(panels) > 1):
                    heading = f"({chr(97+i)}) {heading}"
                if heading:
                    ax.text(0,1.04,heading,transform=ax.transAxes,
                            ha="left",va="bottom",weight="bold",fontsize=font_size,clip_on=False)
            by_id={panel["id"]:panel for panel in panels}
            for group in spec.get("shared_axes",[]):
                axis=group.get("axis");members=group.get("panels",[])
                if axis not in ("x","y") or len(members)<2 or len(set(members))!=len(members) or any(key not in axes for key in members):
                    raise ValueError("Shared axis groups need x/y and distinct existing panels")
                contracts=[by_id[key].get(axis+"_meaning") for key in members]
                if not contracts[0] or len(set(contracts))!=1:
                    raise ValueError("Shared scales require identical declared metric and unit meaning")
                domains=[category_domains[key].get(axis) for key in members]
                if any(domain is not None for domain in domains):
                    if any(domain is None for domain in domains):
                        raise ValueError("Shared categorical axes require an explicit category domain in every panel")
                    for domain in domains[1:]:_check_categorical_axis(domains[0],domain)
                scales=[getattr(axes[key],'get_'+axis+'scale')() for key in members]
                if len(set(scales))!=1:
                    raise ValueError("Cannot share different axis transformations")
                limits=[getattr(axes[key],'get_'+axis+'lim')() for key in members]
                if any(b<a for a,b in limits):
                    raise ValueError("Share reversed/categorical axes explicitly in the custom source")
                low=min(a for a,b in limits);high=max(b for a,b in limits)
                for key in members:getattr(axes[key],'set_'+axis+'lim')(low,high)
            if spec.get("title"):fig.suptitle(spec["title"],fontsize=font_size+1.5,weight="bold")
            if spec.get("_meta",{}).get("synthetic"):
                fig.text(.99,.009,"Simulated data · design reconstruction",ha="right",va="bottom",fontsize=7,color="#66717A")
            return p.finish_paper_style(fig)
        except Exception:
            plt.close(fig)
            raise


def study_spec(study_id, *, demo=False, data=None, seed=None):
    studies=json.loads((LIBRARY/"studies.json").read_text(encoding="utf-8"))
    study=next((row for row in studies if row["id"]==study_id),None)
    if study is None:raise ValueError("Unknown study; use studies command")
    plan=study["panel_plan"]
    if demo:
        if study.get("native_layout"):
            spec=layout_spec(study["native_layout"],demo=True,seed=seed,title=study["short_title"])
        else:
            spec=demo_spec(plan,seed=seed,columns=study.get("columns"),title=study["short_title"])
            for index,overrides in study.get("panel_overrides",{}).items():
                spec["panels"][int(index)]["data"].update(copy.deepcopy(overrides))
            for panel,title in zip(spec["panels"],study.get("panel_titles",[])):
                panel["title"]=title
    else:
        if data is None:raise ValueError("Supply a composition with real data, or request --demo")
        spec=copy.deepcopy(data)
        native=study.get("native_layout")
        if native and spec.get("layout")==native:pass
        elif [p["kind"] for p in spec.get("panels",[])]!=plan:
            raise ValueError("Real study data must match the declared panel plan; use compose for a custom fusion")
    spec.setdefault("_meta",{}).update(study_id=study_id,source_id=study["source_id"],
        source_figure=study["figure"],fidelity=study["reproduction_level"])
    return spec


def layout_spec(kind, *, demo=False, data=None, seed=None, title=""):
    import ccfa_figure_layouts as linked
    if kind not in linked.LAYOUTS:raise ValueError("Unknown linked layout")
    if demo:
        data=_plain(linked.demo_data(kind,seed=seed))
    elif data is None:raise ValueError("Supply linked-layout data, or explicitly request demo")
    spec={"version":1,"layout":kind,"width_mm":183,"font":"serif","palette":"npg","data":copy.deepcopy(data)}
    if title:spec["title"]=title
    if demo:spec["_meta"]={"synthetic":True,"purpose":"linked analytical layout demonstration"}
    return spec


def examples():
    """One compact index retains the initial templates and user-reference pairs."""
    rows=json.loads((LIBRARY/"examples.json").read_text(encoding="utf-8"))
    rows+= [{"id":"paper:"+row["id"],"title":row["short_title"],"category":"paper",
             "study_id":row["id"],"why":row["why"],"source_id":row["source_id"]}
            for row in json.loads((LIBRARY/"studies.json").read_text(encoding="utf-8"))]
    rows+= [{"id":"fusion:"+row["id"],"title":row["title"],"category":"fusion",
             "fusion_id":row["id"],"why":row["why"]} for row in catalog()["fusions"]]
    return rows


def example_spec(example_id, *, demo=False, data=None, seed=None):
    entry=next((row for row in examples() if row["id"]==example_id),None)
    if entry is None:raise ValueError("Unknown example ID; use examples")
    if not demo:
        if data is None:raise ValueError("Supply an example composition, or explicitly request demo")
        if entry["category"]=="paper":return study_spec(entry["study_id"],data=data)
        spec=copy.deepcopy(data)
    elif entry["category"]=="paper":spec=study_spec(entry["study_id"],demo=True,seed=seed)
    elif entry["category"]=="fusion":spec=demo_fusion(entry["fusion_id"],seed=seed)
    elif entry["category"]=="layout":spec=layout_spec(entry["layout"],demo=True,seed=seed,title=entry["title"])
    else:
        import ccfa_analysis_templates as templates
        generated=_plain(templates.demo_data(secrets.randbits(64) if seed is None else seed)[entry["template"]])
        if entry.get("panel_pair"):generated["panel_pair"]=entry["panel_pair"]
        spec={"version":1,"template":entry["template"],"data":generated,
              "_meta":{"synthetic":True,"purpose":"preserved original example demonstration"}}
    spec.setdefault("_meta",{})["example_id"]=example_id
    if entry["category"] in ("original","reference"):
        if spec.get("template")!=entry["template"]:raise ValueError("Example data declares another template")
        if entry.get("panel_pair") and spec.get("data",{}).get("panel_pair")!=entry["panel_pair"]:
            raise ValueError("Reference example data must retain its declared panel pair")
    elif entry["category"]=="layout" and spec.get("layout")!=entry["layout"]:
        raise ValueError("Example data declares another linked layout")
    return spec


def export(spec, base, *, formats=("png",), python_source=True, protected_paths=()):
    import matplotlib.pyplot as plt
    import ccfa_analysis_panels as p
    spec=_plain(spec)
    base=Path(base)
    if base.suffix.lower() in (".svg",".pdf",".png"):base=base.with_suffix("")
    source=base.parent/(base.name+".py")
    protected={Path(path).resolve() for path in protected_paths}
    if python_source and source.resolve() in protected:
        raise ValueError("Export would overwrite a protected Python source")
    # Validate serialization before any figure file can be replaced.
    json.dumps(spec,ensure_ascii=False,allow_nan=False)
    fig=compose(spec)
    try:
        outputs=p.save_figure(fig,base,formats=formats,metadata={"composition":spec},protected_paths=protected_paths)
    finally:plt.close(fig)
    if python_source:
        code=('"""Editable chart source. Synthetic inputs, if present, stay explicitly marked.\n'
              'Run inside the supplied library tree, or add its resources/python to PYTHONPATH.\n"""\n'
              'from pathlib import Path\nimport json\nimport sys\n\n'
              'for parent in Path(__file__).resolve().parents:\n'
              '    library = parent / "ccf-visual-composer/resources/python"\n'
              '    if (library / "ccfa_figure_library.py").is_file():\n'
              '        sys.path.insert(0, str(library))\n        break\n'
              'from ccfa_figure_library import export\n\n'
              'SPEC = json.loads('+repr(json.dumps(spec,ensure_ascii=False,allow_nan=False))+')\n\n'
              'if __name__ == "__main__":\n    export(SPEC, Path(__file__).with_suffix(""), formats='+repr(tuple(formats))+', python_source=False)\n')
        source.write_text(code,encoding="utf-8",newline="\n");outputs["python"]=source
    return outputs


def main(argv=None):
    parser=argparse.ArgumentParser(description=__doc__)
    sub=parser.add_subparsers(dest="command",required=True)
    sub.add_parser("list")
    e=sub.add_parser("explain");e.add_argument("kind")
    r=sub.add_parser("route");r.add_argument("question",nargs="?");r.add_argument("--brief",type=Path);r.add_argument("--fields",nargs="*");r.add_argument("--count",type=int,default=3);r.add_argument("--seed",type=int,help=argparse.SUPPRESS);r.add_argument("--history",type=Path);r.add_argument("--exclude",nargs="*",default=[])
    r.add_argument("--input-type",choices=tuple(catalog().get("input_types",{})))
    r.add_argument("--chart-type",choices=tuple(catalog().get("chart_types",{})))
    h=sub.add_parser("record");h.add_argument("--history",type=Path,required=True);h.add_argument("kinds",nargs="+")
    studies_parser=sub.add_parser("studies")
    studies_parser.add_argument("--id")
    studies_parser.add_argument("--intent",choices=tuple(catalog()["intents"]))
    studies_parser.add_argument("--offset",type=int,default=0)
    studies_parser.add_argument("--limit",type=int,default=12)
    sub.add_parser("fusions")
    family_parser=sub.add_parser("families", help="Canonical drawing structures with preserved contextual members")
    family_parser.add_argument("--id")
    family_parser.add_argument("--member", help="Existing ID such as paper:<study>, primitive:<chart>, or reference:sensitivity-pair")
    family_parser.add_argument("--variant", help="Inspect the family containing a strict structural variant")
    family_parser.add_argument("--offset",type=int,default=0)
    family_parser.add_argument("--limit",type=int,default=12)
    ex=sub.add_parser("examples");ex.add_argument("--category",choices=("original","reference","paper","fusion","layout"));ex.add_argument("--id");ex.add_argument("--offset",type=int,default=0);ex.add_argument("--limit",type=int,default=12)
    use=sub.add_parser("example");use.add_argument("id");use.add_argument("--demo",action="store_true");use.add_argument("--data",type=Path);use.add_argument("--out",type=Path,required=True)
    layout=sub.add_parser("layout");layout.add_argument("kind");layout.add_argument("--demo",action="store_true");layout.add_argument("--data",type=Path);layout.add_argument("--out",type=Path,required=True)
    d=sub.add_parser("demo");d.add_argument("kinds",nargs="*");d.add_argument("--fusion");d.add_argument("--seed",type=int,help=argparse.SUPPRESS);d.add_argument("--columns",type=int);d.add_argument("--out",type=Path,required=True)
    c=sub.add_parser("compose");c.add_argument("--spec",type=Path,required=True);c.add_argument("--out",type=Path,required=True)
    c.add_argument("--data",type=Path,help="Replace all selected data while retaining the source JSON layout/style; no demo fallback")
    s=sub.add_parser("reproduce");s.add_argument("study");s.add_argument("--demo",action="store_true");s.add_argument("--data",type=Path);s.add_argument("--seed",type=int,help=argparse.SUPPRESS);s.add_argument("--out",type=Path,required=True)
    for output_parser in (d,c,s,use,layout):
        output_parser.add_argument("--formats",nargs="+",choices=("svg","pdf","png"),default=["png"],help="PNG by default; request SVG/PDF explicitly")
        output_parser.add_argument("--panel", help="Render one named supplied panel, retaining its layers and data")
    args=parser.parse_args(argv)
    try:
        if args.command=="list":result={"intents":catalog()["intents"],"input_types":catalog().get("input_types",{}),"chart_types":catalog().get("chart_types",{}),"charts":[{key:c[key] for key in ("id","title","intents","required","input_types","chart_types")} for c in catalog()["charts"]]}
        elif args.command=="explain":result=explain(args.kind)
        elif args.command=="route":result=route(args.question,fields=args.fields,count=args.count,seed=args.seed,usage=json.loads(args.history.read_text(encoding="utf-8")) if args.history and args.history.exists() else None,exclude=args.exclude,context=json.loads(args.brief.read_text(encoding="utf-8-sig")) if args.brief else None,input_type=args.input_type,chart_type=args.chart_type)
        elif args.command=="record":result=record_selection(args.history,args.kinds)
        elif args.command=="studies":
            rows=json.loads((LIBRARY/"studies.json").read_text(encoding="utf-8"))
            if args.id:
                result=next((row for row in rows if row["id"]==args.id),None)
                if result is None:raise ValueError("Unknown study ID")
            else:
                if args.intent:
                    kinds={row["id"] for row in catalog()["charts"] if args.intent in row["intents"]}
                    rows=[row for row in rows if kinds.intersection(row["panel_plan"])]
                if args.offset<0 or not 1<=args.limit<=50:raise ValueError("Use a nonnegative offset and limit between 1 and 50")
                result={"total":len(rows),"offset":args.offset,"studies":[{key:row[key] for key in ("id","short_title","venue","year","figure","panel_plan")} for row in rows[args.offset:args.offset+args.limit]]}
        elif args.command=="fusions":result=catalog()["fusions"]
        elif args.command=="families":
            index=families()
            rows=index["families"]
            if args.id or args.member or args.variant:
                rows=[row for row in rows if (not args.id or row["id"]==args.id)
                      and (not args.member or args.member in row["member_ids"])
                      and (not args.variant or args.variant in {variant["id"] for variant in row["variants"]})]
                if len(rows)!=1:raise ValueError("Unknown or inconsistent family/member ID")
                result=rows[0]
            else:
                if args.offset<0 or not 1<=args.limit<=50:raise ValueError("Use a nonnegative offset and limit from 1 to 50")
                result={"version":1,"total_examples":index["total_examples"],"total_families":index["total_families"],
                        "total_variants":index["total_variants"],
                        "offset":args.offset,"families":[{key:row[key] for key in ("id","title","representative_id","member_ids","why","intent_ids","level","panel_count","variant_count")} for row in rows[args.offset:args.offset+args.limit]]}
        elif args.command=="examples":
            rows=examples()
            if args.id:
                result=next((row for row in rows if row["id"]==args.id),None)
                if result is None:raise ValueError("Unknown example ID")
            else:
                if args.category:rows=[row for row in rows if row["category"]==args.category]
                if args.offset<0 or not 1<=args.limit<=50:raise ValueError("Use a nonnegative offset and limit from 1 to 50")
                result={"total":len(rows),"offset":args.offset,"examples":rows[args.offset:args.offset+args.limit]}
        else:
            protected=[];panel_selected=False
            if args.command=="demo":
                kinds=args.kinds
                if args.fusion:
                    if kinds:raise ValueError("Use kinds or --fusion")
                    spec=demo_fusion(args.fusion,seed=args.seed,columns=args.columns)
                else:spec=demo_spec(kinds,seed=args.seed,columns=args.columns)
            elif args.command=="compose":
                from ccfa_figure_data import load_composition
                spec,protected=load_composition(args.spec)
                if args.panel:
                    spec=single_panel_spec(spec,args.panel);panel_selected=True
                if args.data:
                    spec=replace_data(spec,json.loads(args.data.read_text(encoding="utf-8-sig")))
                    protected.append(args.data.resolve())
            elif args.command in ("example","layout"):
                if args.demo and args.data:raise ValueError("Use --demo or --data")
                data=None
                if args.data:
                    from ccfa_figure_data import load_composition
                    data,protected=load_composition(args.data)
                if args.command=="example":spec=example_spec(args.id,demo=args.demo,data=data)
                elif data is not None:
                    if data.get("layout")!=args.kind:raise ValueError("Layout data must declare the requested layout")
                    spec=data
                else:spec=layout_spec(args.kind,demo=args.demo)
            else:
                if args.demo and args.data:raise ValueError("Use --demo or --data")
                data=None
                if args.data:
                    from ccfa_figure_data import load_composition
                    data,protected=load_composition(args.data)
                spec=study_spec(args.study,demo=args.demo,data=data,seed=args.seed)
            if args.panel and not panel_selected:
                spec=single_panel_spec(spec,args.panel)
            result={k:str(v) for k,v in export(spec,args.out,formats=tuple(args.formats),protected_paths=protected).items()}
        print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False))
    except (OSError,ValueError,TypeError,KeyError) as exc:parser.error(str(exc))


if __name__=="__main__":
    import sys
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,"reconfigure"):stream.reconfigure(encoding="utf-8")
    main()
