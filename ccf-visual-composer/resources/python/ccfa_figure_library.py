#!/usr/bin/env python3
"""Route scientific questions to editable charts; compose only supplied data.

Routing and catalog lookup need only the standard library. Plotting imports
NumPy/Matplotlib on demand. Example data requires an explicit demo command.
"""
from __future__ import annotations

import argparse
import copy
from functools import lru_cache
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


def route(question=None, *, fields=None, count=3, seed=None, usage=None, exclude=(), context=None):
    """Sample without replacement from equally relevant, data-compatible charts.

    Does not mutate history. Record a selection only after accepting it. A local
    revision reuses the accepted composition, not a new route call.
    """
    brief=_brief(context)
    question=question or brief.get("question") or brief.get("claim")
    if not isinstance(question, str) or not question.strip():
        raise ValueError("Supply a scientific question or intent")
    if isinstance(count, bool) or not isinstance(count, int) or not 1 <= count <= 12:
        raise ValueError("count must be between 1 and 12")
    if seed is not None:_nonnegative_integer(seed, "seed")
    counts = _usage(usage)
    text = " ".join([question,brief.get("claim","")]).casefold()
    named_text=question.casefold()
    named=next((entry for entry in catalog()["charts"] if entry["id"]==named_text),None)
    intents = list(brief.get("intent_ids",[]))
    for key, entry in catalog()["intents"].items():
        if text == key or any(_matches(term,text) for term in entry["terms"]):
            if key not in intents:intents.append(key)
    if not intents:
        if named:intents=list(named["intents"])
        else:raise ValueError("No intent matched; use an intent ID from --list or state the scientific relationship")
    if fields is not None and (isinstance(fields,str) or not all(isinstance(v,str) for v in fields)):
        raise ValueError("fields must be a list of parameter names")
    known_fields=brief.get("data",{}).get("fields")
    if fields is not None and known_fields is not None and set(fields)!=set(known_fields):
        raise ValueError("CLI fields and paper brief fields disagree")
    available = None if fields is None and known_fields is None else set(fields if fields is not None else known_fields)
    exclude=set(exclude)|set(brief.get("exclude_charts",[]))
    unknown = set(exclude) - {c["id"] for c in catalog()["charts"]}
    if unknown:
        raise ValueError(f"Unknown excluded charts: {sorted(unknown)}")
    candidates = [];fit_info={};rejected=[]
    for entry in catalog()["charts"]:
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
            fits.append((score,option))
        selected_fusions=[]
        while fits and len(selected_fusions)<3:
            best=max(score for score,_ in fits)
            tier=[item for item in fits if item[0]==best]
            weights=[1/(1+sum(counts.get(kind,0) for kind in set(option["panels"]))/len(set(option["panels"]))) for _,option in tier]
            chosen=rng.choices(tier,weights=weights,k=1)[0]
            selected_fusions.append(chosen[1]);fits.remove(chosen)
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
        selected.append({"id": entry["id"], "title": entry["title"], "score": score,
                         "why": entry["why"], "required": list(entry["required"]),
                         "paper_fit":fit_info[entry["id"]][0],"check_before_use":fit_info[entry["id"]][1],
                         "previous_selections": counts.get(entry["id"], 0),
                         "design_card": f"explain {entry['id']}"})
        candidates.remove(chosen)
    result.update(selection_policy="paper meaning and declared data conditions, then random choice within the best fit; optional history breaks ties",
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
        fig.set_layout_engine("constrained",w_pad=.045,h_pad=.055,wspace=.12,hspace=.15,
                              rect=(0,.055,1,.96 if spec.get("title") else 1))
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
                    if handles:ax.legend(frameon=False,fontsize=max(6,font_size-1))
                ax.text(0,1.065,f"({chr(97+i)}) {panel.get('title','')}",transform=ax.transAxes,
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
            return fig
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


def export(spec, base, *, formats=("svg","png"), python_source=True, protected_paths=()):
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
    h=sub.add_parser("record");h.add_argument("--history",type=Path,required=True);h.add_argument("kinds",nargs="+")
    studies_parser=sub.add_parser("studies")
    studies_parser.add_argument("--id")
    studies_parser.add_argument("--intent",choices=tuple(catalog()["intents"]))
    studies_parser.add_argument("--offset",type=int,default=0)
    studies_parser.add_argument("--limit",type=int,default=12)
    sub.add_parser("fusions")
    ex=sub.add_parser("examples");ex.add_argument("--category",choices=("original","reference","paper","fusion","layout"));ex.add_argument("--id");ex.add_argument("--offset",type=int,default=0);ex.add_argument("--limit",type=int,default=12)
    use=sub.add_parser("example");use.add_argument("id");use.add_argument("--demo",action="store_true");use.add_argument("--data",type=Path);use.add_argument("--out",type=Path,required=True)
    layout=sub.add_parser("layout");layout.add_argument("kind");layout.add_argument("--demo",action="store_true");layout.add_argument("--data",type=Path);layout.add_argument("--out",type=Path,required=True)
    d=sub.add_parser("demo");d.add_argument("kinds",nargs="*");d.add_argument("--fusion");d.add_argument("--seed",type=int,help=argparse.SUPPRESS);d.add_argument("--columns",type=int);d.add_argument("--out",type=Path,required=True)
    c=sub.add_parser("compose");c.add_argument("--spec",type=Path,required=True);c.add_argument("--out",type=Path,required=True)
    s=sub.add_parser("reproduce");s.add_argument("study");s.add_argument("--demo",action="store_true");s.add_argument("--data",type=Path);s.add_argument("--seed",type=int,help=argparse.SUPPRESS);s.add_argument("--out",type=Path,required=True)
    for output_parser in (d,c,s,use,layout):
        output_parser.add_argument("--formats",nargs="+",choices=("svg","pdf","png"),default=["svg","png"])
    args=parser.parse_args(argv)
    try:
        if args.command=="list":result={"intents":catalog()["intents"],"charts":[{"id":c["id"],"title":c["title"],"intents":c["intents"],"required":c["required"]} for c in catalog()["charts"]]}
        elif args.command=="explain":result=explain(args.kind)
        elif args.command=="route":result=route(args.question,fields=args.fields,count=args.count,seed=args.seed,usage=json.loads(args.history.read_text(encoding="utf-8")) if args.history and args.history.exists() else None,exclude=args.exclude,context=json.loads(args.brief.read_text(encoding="utf-8-sig")) if args.brief else None)
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
            protected=[]
            if args.command=="demo":
                kinds=args.kinds
                if args.fusion:
                    if kinds:raise ValueError("Use kinds or --fusion")
                    spec=demo_fusion(args.fusion,seed=args.seed,columns=args.columns)
                else:spec=demo_spec(kinds,seed=args.seed,columns=args.columns)
            elif args.command=="compose":
                from ccfa_figure_data import load_composition
                spec,protected=load_composition(args.spec)
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
            result={k:str(v) for k,v in export(spec,args.out,formats=tuple(args.formats),protected_paths=protected).items()}
        print(json.dumps(result,ensure_ascii=False,indent=2,allow_nan=False))
    except (OSError,ValueError,TypeError,KeyError) as exc:parser.error(str(exc))


if __name__=="__main__":
    import sys
    for stream in (sys.stdout,sys.stderr):
        if hasattr(stream,"reconfigure"):stream.reconfigure(encoding="utf-8")
    main()
