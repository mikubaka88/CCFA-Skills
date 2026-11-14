#!/usr/bin/env python3
"""Scientific routing, composition, source lookup, and editable export checks."""
from __future__ import annotations

import copy
import json
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

ROOT=Path(__file__).resolve().parents[2]
MODULES=ROOT/"ccf-visual-composer/resources/python"
sys.path.insert(0,str(MODULES))
import ccfa_figure_library as f


class FigureLibraryTests(unittest.TestCase):
    def tearDown(self):
        plt.close("all")

    def test_selected_template_is_pinned_instead_of_rerouted(self):
        for name,expected in [("reference:sensitivity-pair","reference:sensitivity-pair"),
                              ("reference--sensitivity-pair","reference:sensitivity-pair"),
                              ("template--benchmark_atlas","original:benchmark_atlas"),
                              ("benchmark_atlas","original:benchmark_atlas")]:
            result=f.route(name)
            self.assertEqual(result["selection_policy"],"selected_example")
            self.assertEqual(result["selected_example"]["id"],expected)
            self.assertFalse(result["fields_checked"])
            self.assertNotIn("randomness",result)
        with self.assertRaisesRegex(ValueError,"fields"):
            f.route("reference:sensitivity-pair",fields="x")

    def test_replacement_preserves_native_plan_and_all_style_settings(self):
        original=f.example_spec("reference:sensitivity-pair",demo=True)
        original.update(width_mm=132,height_mm=84,font_size=11,palette="npg",title="Selected analytical question")
        before=copy.deepcopy(original);values=copy.deepcopy(original["data"])
        values.pop("_meta",None);values["sensitivity"]["xlabel"]="Updated grouping"
        with patch.object(f,"demo_data",side_effect=AssertionError("No new simulation")):
            actual=f.replace_data(original,values)
        self.assertEqual(original,before)
        self.assertEqual(actual["data"],values)
        for key in ["template","width_mm","height_mm","font_size","palette","title"]:
            self.assertEqual(actual[key],original[key])
        self.assertNotIn("synthetic",actual["_meta"])
        self.assertTrue(actual["_meta"]["data_replaced"])
        self.assertEqual(actual["_meta"]["data_status"],"supplied")
        self.assertEqual(actual["_meta"]["retained_text_to_check"][0]["text"],original["title"])
        self.assertNotIn("shared_simulation_contracts",actual["_meta"])
        fig=f.compose(actual)
        self.assertEqual(fig._suptitle.get_text(),original["title"])
        self.assertEqual(fig._suptitle.get_fontweight(),"bold")
        self.assertAlmostEqual(fig.get_figwidth()*25.4,132)
        self.assertAlmostEqual(fig.get_figheight()*25.4,84)

    def test_replacement_requires_all_panels_and_layers_without_changing_drawing_plan(self):
        original=f.demo_spec(["line_band","line_band"])
        original.update(width_mm=150,height_mm=81,font_size=10)
        node=original["panels"][0]
        node.update(x_meaning="Step",y_meaning="Error")
        node["layers"]=[{"kind":"line_band","data":{"x":[1,2],"y":[3,4]},
                         "x_meaning":"Step","y_meaning":"Error","style":{"linestyle":"--"}}]
        values={"panels":[{"id":p["id"],"data":{"x":[1,2],"y":[5,6]}} for p in original["panels"]]}
        with self.assertRaisesRegex(ValueError,"every selected overlay"):
            f.replace_data(original,values)
        values["panels"][0]["layers"]=[{"data":{"x":[1,2],"y":[7,8]}}]
        actual=f.replace_data(original,values)
        self.assertEqual(actual["panels"][0]["layers"][0]["style"],{"linestyle":"--"})
        self.assertEqual(actual["panels"][0]["layers"][0]["data"]["y"],[7,8])
        self.assertEqual(actual["font_size"],10)
        with self.assertRaisesRegex(ValueError,"every panel ID"):
            f.replace_data(original,{"panels":values["panels"][:1]})
        values["panels"][0]["title"]="Unrequested layout rewrite"
        with self.assertRaisesRegex(ValueError,"drawing plan"):
            f.replace_data(original,values)

    def test_numeric_replacement_keeps_presentation_but_never_old_intervals(self):
        spec={"version":1,"rows":1,"columns":1,"width_mm":132,"height_mm":84,"font_size":10,
              "panels":[{"id":"p","kind":"category_comparison","row":0,"column":0,
                         "data":{"labels":["A","B"],"bars":[1,2],"bar_style":"outlined","bar_labels":True,
                                 "bar_color":"#123456","tick_font_size":9,
                                 "legend_options":{"loc":"lower right","fontsize":10},
                                 "series":[{"label":"Mass","values":[3,4],"lower":[2,3],"upper":[4,5],
                                            "color":"#B84D2A","marker":"D","band_alpha":.12}]}}]}
        supplied={"panels":[{"id":"p","data":{"labels":["A","B"],"bars":[6,7],
                    "series":[{"label":"Mass","values":[8,9]}]}}]}
        actual=f.replace_data(spec,supplied);data=actual["panels"][0]["data"]
        self.assertEqual(data["bar_style"],"outlined");self.assertTrue(data["bar_labels"])
        self.assertEqual(data["bar_color"],"#123456");self.assertEqual(data["tick_font_size"],9)
        self.assertEqual(data["legend_options"],{"loc":"lower right","fontsize":10})
        self.assertEqual(data["series"][0]["color"],"#B84D2A")
        self.assertEqual(data["series"][0]["marker"],"D")
        self.assertNotIn("lower",data["series"][0]);self.assertNotIn("upper",data["series"][0])
        fig=f.compose(actual);self.assertEqual(len(fig.axes[0].collections),0)
        self.assertEqual(fig.axes[0].lines[0].get_marker(),"D")
        supplied["panels"][0]["data"]["series"][0]["label"]="Different criterion"
        new=f.replace_data(spec,supplied)["panels"][0]["data"]["series"][0]
        self.assertNotIn("color",new);self.assertNotIn("marker",new)

    def test_template_series_style_matches_identity_when_supplied_order_changes(self):
        spec={"version":1,"template":"scaling_robustness","data":{"methods":["A","B"],
              "entity_colors":["#123456","#FEDCBA"],"curve":{"series":[
                  {"method":"A","y":[1,2],"color":"#123456","marker":"s","lower":[0,1],"upper":[2,3]},
                  {"method":"B","y":[3,4],"color":"#FEDCBA","marker":"D"}]}}}
        data={"methods":["B","A"],"curve":{"series":[{"method":"B","y":[7,8]},{"method":"A","y":[9,10]}]}}
        actual=f.replace_data(spec,data)["data"]
        self.assertEqual(actual["entity_colors"],["#FEDCBA","#123456"])
        self.assertEqual([r["marker"] for r in actual["curve"]["series"]],["D","s"])
        self.assertNotIn("lower",actual["curve"]["series"][1])
        data["methods"]=["Unknown"]
        data["curve"]["series"]=[{"method":"Unknown","y":[4,5]}]
        actual=f.replace_data(spec,data)["data"]
        self.assertNotIn("entity_colors",actual)
        self.assertNotIn("marker",actual["curve"]["series"][0])

    def test_data_replacement_keeps_shared_entity_colors_and_handles_new_labels(self):
        spec={"version":1,"rows":1,"columns":1,"entity_order":["Unused","Base"],"palette":"npg",
              "panels":[{"id":"p","kind":"comparison_intervals","row":0,"column":0,
                         "data":{"labels":["Base"],"values":[1]}}]}
        unchanged=f.replace_data(spec,{"panels":[{"id":"p","data":{"labels":["Base"],"values":[2]}}]})
        self.assertEqual(unchanged["entity_order"],["Unused","Base"])
        renamed=f.replace_data(spec,{"panels":[{"id":"p","data":{"labels":["New A","New B"],"values":[2,3]}}]})
        self.assertEqual(renamed["entity_order"],["New A","New B"])
        f.compose(renamed)

    def test_compose_cli_replaces_complete_template_data_and_protects_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder);source=base/"selected.json";data_path=base/"measurements.json"
            spec=f.example_spec("reference:sensitivity-pair",demo=True)
            spec.update(width_mm=132,height_mm=84,font_size=10,palette="aaas")
            source.write_text(json.dumps(spec),encoding="utf-8")
            data=copy.deepcopy(spec["data"]);data.pop("_meta",None)
            data_path.write_text(json.dumps(data),encoding="utf-8")
            snapshot={p:p.read_bytes() for p in [source,data_path]}
            result=subprocess.run([sys.executable,"-B","-X","utf8",str(MODULES/"ccfa_figure_library.py"),
                "compose","--spec",str(source),"--data",str(data_path),"--out",str(base/"actual")],
                capture_output=True,text=True,encoding="utf-8")
            self.assertEqual(result.returncode,0,result.stderr)
            metadata=json.loads((base/"actual.metadata.json").read_text(encoding="utf-8"))["composition"]
            self.assertEqual(metadata["width_mm"],132);self.assertEqual(metadata["font_size"],10)
            self.assertEqual(metadata["data"],data)
            self.assertTrue((base/"actual.png").is_file());self.assertFalse((base/"actual.svg").exists())
            for path,raw in snapshot.items():self.assertEqual(path.read_bytes(),raw)

    def test_two_taxonomies_cover_every_grammar_and_filter_independently(self):
        catalog=f.catalog()
        for entry in catalog["charts"]:
            self.assertTrue(entry["input_types"] and entry["chart_types"] and entry["analysis_elements"])
            self.assertTrue(set(entry["input_types"])<=set(catalog["input_types"]))
            self.assertTrue(set(entry["chart_types"])<=set(catalog["chart_types"]))
        result=f.route("category_comparison",fields=["labels","bars","series"],input_type="category_series",chart_type="bar")
        self.assertEqual([row["id"] for row in result["candidates"]],["category_comparison"])
        self.assertEqual(f.route("category_comparison",input_type="paired_samples")["candidates"],[])
        with self.assertRaisesRegex(ValueError,"Unknown input"):
            f.route("comparison",input_type="invented")

    def test_element_plan_only_adds_layers_supported_by_supplied_fields(self):
        plain=f.element_plan("line_band",["x","y"])
        self.assertTrue(plain["needs_enrichment"])
        rich=f.element_plan("line_band",["x","y","lower","upper"])
        self.assertIn("supplied_range",rich["add_from_supplied_data"])
        self.assertFalse(rich["needs_enrichment"])
        density=f.element_plan("density_map",["x","y","corridor"])
        self.assertNotIn("weighted_share",density["add_from_supplied_data"])
        self.assertIn("weighted_share",f.element_plan("density_map",["x","y","corridor","weights"])["add_from_supplied_data"])
        self.assertNotIn("weighted_share",f.element_plan("density_map",["x","y","counts","corridor","weights"])["add_from_supplied_data"])
        self.assertIn("weighted_share",f.element_plan("density_map",["x","y","counts","corridor","weights","weight_kind"])["add_from_supplied_data"])

    def test_actual_data_format_separates_raw_samples_and_summaries(self):
        self.assertEqual(f.describe_plot("binned_summary",{"summary":{"median":[1]}})["input_types"],["quantile_summaries"])
        self.assertEqual(f.describe_plot("binned_summary",{"samples":[[1,2,3]]})["input_types"],["grouped_samples"])
        self.assertEqual(f.describe_plot("density_map",{"counts":[2,3]})["input_types"],["binned_counts"])
        empty=f.describe_plot("line_band",{"x":[1,2],"y":[3,4],"lower":None,"upper":None,"annotate":False})
        self.assertEqual(empty["element_plan"]["add_from_supplied_data"],[])

    def test_single_panel_keeps_data_layers_identity_and_original(self):
        original=f.demo_spec(["line_band","line_band"])
        original["panels"][0].update(entity_ids=["Earlier"],color_argument="color")
        node=original["panels"][1]
        node.update(entity_ids=["Selected"],color_argument="color",x_meaning="Step",y_meaning="Rate")
        layer=copy.deepcopy(node);layer.pop("layers",None)
        node["layers"]=[layer]
        before=copy.deepcopy(original)
        selected=f.single_panel_spec(original,node["id"])
        self.assertEqual(original,before)
        self.assertEqual(selected["panels"][0]["data"],node["data"])
        self.assertEqual(selected["panels"][0]["layers"],node["layers"])
        self.assertEqual(selected["entity_order"],["Earlier","Selected"])
        self.assertEqual((selected["rows"],selected["columns"]),(1,1))
        fig=f.compose(selected)
        self.assertEqual(len(fig.axes),1)
        self.assertFalse(any(t.get_text().startswith("(a)") for t in fig.axes[0].texts))
        from ccfa_analysis_panels import audit_figure
        self.assertEqual(audit_figure(fig)["text_outside_canvas"],[])

    def test_single_panel_rejects_missing_and_atomic_layouts(self):
        with self.assertRaisesRegex(ValueError,"unique panel"):
            f.single_panel_spec(f.demo_spec(["line_band"]),"missing")
        with self.assertRaisesRegex(ValueError,"atomic"):
            f.single_panel_spec({"version":1,"layout":"joint_marginals"},"main")

    def test_compose_panel_replacement_needs_only_the_selected_panel(self):
        with tempfile.TemporaryDirectory() as directory:
            base=Path(directory);source=base/"selected.json";data_path=base/"values.json"
            spec=f.demo_spec(["line_band","line_band"]);target=spec["panels"][1]["id"]
            source.write_text(json.dumps(spec),encoding="utf-8")
            data_path.write_text(json.dumps({"panels":[{"id":target,"data":{"x":[1,2],"y":[7,8]}}]}),encoding="utf-8")
            run=subprocess.run([sys.executable,"-B","-X","utf8",str(MODULES/"ccfa_figure_library.py"),"compose",
                "--spec",str(source),"--panel",target,"--data",str(data_path),"--out",str(base/"actual")],
                capture_output=True,text=True,encoding="utf-8")
            self.assertEqual(run.returncode,0,run.stderr)
            actual=json.loads((base/"actual.metadata.json").read_text(encoding="utf-8"))["composition"]
            self.assertEqual([p["id"] for p in actual["panels"]],[target])
            self.assertEqual(actual["panels"][0]["data"]["y"],[7,8])
            self.assertEqual((actual["rows"],actual["columns"]),(1,1))
            self.assertEqual(json.loads(source.read_text(encoding="utf-8")),spec)

    def test_compose_cli_selects_one_panel_without_new_svg(self):
        with tempfile.TemporaryDirectory() as directory:
            root=Path(directory)
            source=root/"original.json"
            spec=f.demo_spec(["line_band","line_band"])
            source.write_text(json.dumps(spec),encoding="utf-8")
            result=subprocess.run([sys.executable,"-B",str(MODULES/"ccfa_figure_library.py"),
                "compose","--spec",str(source),"--panel",spec["panels"][1]["id"],"--out",str(root/"single")],
                capture_output=True,text=True,encoding="utf-8")
            self.assertEqual(result.returncode,0,result.stderr)
            self.assertTrue((root/"single.png").is_file())
            self.assertFalse((root/"single.svg").exists())
            self.assertEqual(json.loads(source.read_text()),spec)

    def test_structural_families_ignore_values_titles_palette_and_panel_names(self):
        before={"version":1,"rows":1,"columns":2,"panels":[
            {"id":"a","kind":"line_band","row":0,"column":0,"data":{"x":[1,2],"y":[.2,.5]}},
            {"id":"b","kind":"line_band","row":0,"column":1,"data":{"x":[1,2],"y":[.3,.7]}}],
            "shared_axes":[{"axis":"x","panels":["a","b"]}]}
        after=copy.deepcopy(before);after.update(title="Another scientific context",palette="ccfa")
        for i,panel in enumerate(after["panels"]):
            panel["id"]="new-"+str(i);panel["title"]="Different text"
            panel["data"]["y"]=[.8,.9]
        after["shared_axes"][0]["panels"]=["new-0","new-1"]
        self.assertEqual(f.family_for_spec(before)["id"],f.family_for_spec(after)["id"])
        after["panels"][0]["colspan"]=2
        self.assertEqual(f.family_for_spec(before)["id"],f.family_for_spec(after)["id"])
        self.assertNotEqual(f.family_for_spec(before)["variant_id"],f.family_for_spec(after)["variant_id"])

    def test_family_identity_preserves_scientific_visual_elements_and_layers(self):
        base={"version":1,"panels":[{"id":"p","kind":"density_map","data":{"x":[1,2],"y":[.1,.2]}}]}
        family=f.family_for_spec(base)["id"]
        for addition in ({"yscale":"log"},{"corridor":{"x_max":20,"y_max":.1}},
                         {"count_range":[1,1000]},{"annotate":[0]}):
            modified=copy.deepcopy(base);modified["panels"][0]["data"].update(addition)
            self.assertNotEqual(f.family_for_spec(modified)["id"],family)
        modified=copy.deepcopy(base)
        modified["panels"][0]["layers"]=[{"kind":"line_band","data":{"x":[1,2],"y":[.1,.2]}}]
        self.assertNotEqual(f.family_for_spec(modified)["id"],family)
        corridor=copy.deepcopy(base);corridor["panels"][0]["data"]["corridor"]={"x_max":20,"y_max":.1}
        weighted=copy.deepcopy(corridor);weighted["panels"][0]["data"]["corridor"]["weights"]=[1,2]
        self.assertNotEqual(f.family_for_spec(corridor)["id"],f.family_for_spec(weighted)["id"])

    def test_template_pairs_quantile_summary_and_repeated_facets_stay_distinct(self):
        spec={"version":1,"template":"sensitivity_dynamics","data":{"panel_pair":"sensitivity"}}
        first=f.family_for_spec(spec)
        self.assertEqual(first["panel_count"],2)
        spec["data"]["sensitivity"]={"summary_mode":"median_p90","summary":{"median":[.1],"p90":[.2],"p95":[.3],"p99":[.4]}}
        enhanced=f.family_for_spec(spec)
        self.assertNotEqual(first["id"],enhanced["id"])
        spec["data"]["panel_pair"]="dynamics"
        self.assertNotEqual(enhanced["id"],f.family_for_spec(spec)["id"])
        one=f._panel_structure(["calibration"])
        eight=f._panel_structure(["calibration"]*8,columns=4)
        self.assertNotEqual(f.family_for_spec(one)["id"],f.family_for_spec(eight)["id"])

    def test_pair_signature_ignores_the_inactive_half_but_retains_its_own_elements(self):
        spec={"version":1,"template":"sensitivity_dynamics","data":{
            "panel_pair":"sensitivity","density":{"yscale":"log"},
            "dynamics":{"series":[{"marker":"s","x":[4,8],"y":[30,80]}]}}}
        before=f.family_for_spec(spec)
        spec["data"]["dynamics"]["series"][0]["lower"]=[20,60]
        spec["data"]["dynamics"]["series"][0]["upper"]=[40,90]
        self.assertEqual(f.family_for_spec(spec)["id"],before["id"])
        self.assertEqual(f.family_for_spec(spec)["variant_id"],before["variant_id"])
        spec["data"]["density"]["corridor"]={"x_max":20,"y_max":.1,"weights":[1,2]}
        self.assertNotEqual(f.family_for_spec(spec)["id"],before["id"])

    def test_standard_reference_family_declarations_match_the_native_demo_encodings(self):
        _,specs=f._standard_family_inputs()
        for key in ("original:sensitivity_dynamics","reference:sensitivity-pair","reference:dynamics-pair"):
            with self.subTest(example=key):
                native=f.family_for_spec(f.example_spec(key,demo=True))
                declared=f.family_for_spec(specs[key])
                self.assertEqual(native["family_signature"],declared["family_signature"])
                self.assertEqual(native["features"],declared["features"])
                self.assertEqual(native["panel_count"],declared["panel_count"])

    def test_actual_gallery_groups_equivalent_variants_without_losing_context(self):
        spec=f._panel_structure(["line_band"])
        rows=[{"id":"primitive--curve","type":"primitive","title":"Curve","intent_ids":["dynamics"]},
              {"id":"study--curve","type":"study","title":"Learning in another domain","intent_ids":["generalization"],"source_id":"paper-identity"},
              {"id":"legacy--asset","type":"legacy","title":"Preserved original"}]
        index=f.families(rows,specs={rows[0]["id"]:spec,rows[1]["id"]:copy.deepcopy(spec)})
        self.assertEqual((index["total_examples"],index["total_families"]),(3,2))
        family=next(row for row in index["families"] if len(row["member_ids"])==2)
        self.assertEqual(family["representative_id"],"study--curve")
        self.assertEqual(family["variant_count"],1)
        self.assertEqual(family["intent_ids"],["dynamics","generalization"])
        self.assertEqual(next(row for row in family["members"] if row["id"]=="study--curve")["source_id"],"paper-identity")
        with self.assertRaisesRegex(ValueError,"unique"):
            f.families(rows+rows[:1],specs={})

    def test_repeated_facets_share_a_family_with_discoverable_structural_variants(self):
        rows=[];specs={}
        for count in (1,2,4,8):
            key="curve-"+str(count)
            rows.append({"id":key,"type":"reference" if count==2 else "study", "title":str(count)+" distinct datasets"})
            specs[key]=f._panel_structure(["line_band"]*count,columns=min(count,4))
        index=f.families(rows,specs=specs)
        self.assertEqual((index["total_families"],index["total_variants"]),(2,4))
        family=next(row for row in index["families"] if len(row["member_ids"])==3)
        self.assertEqual(family["variant_count"],3)
        self.assertEqual(set(family["member_ids"]),{"curve-2","curve-4","curve-8"})
        self.assertEqual({row["panel_count"] for row in family["variants"]},{2,4,8})
        self.assertEqual(family["representative_id"],"curve-2")
        self.assertEqual(family["panel_count"],2)
        self.assertEqual({key for variant in family["variants"] for key in variant["member_ids"]},set(family["member_ids"]))

    def test_grid_layout_changes_are_variants_but_shared_relationships_stay_distinct(self):
        horizontal=f._panel_structure(["line_band"]*4,columns=4)
        grid=f._panel_structure(["line_band"]*4,columns=2)
        self.assertEqual(f.family_for_spec(horizontal)["id"],f.family_for_spec(grid)["id"])
        self.assertNotEqual(f.family_for_spec(horizontal)["variant_id"],f.family_for_spec(grid)["variant_id"])
        shared=copy.deepcopy(grid)
        shared["shared_axes"]=[{"axis":"x","panels":[row["id"] for row in shared["panels"]]}]
        self.assertNotEqual(f.family_for_spec(grid)["id"],f.family_for_spec(shared)["id"])
        two=f._panel_structure(["line_band"]*2,columns=2)
        two["shared_axes"]=[{"axis":"x","panels":[row["id"] for row in two["panels"]]}]
        self.assertEqual(f.family_for_spec(shared)["id"],f.family_for_spec(two)["id"])

    def test_mixed_ordered_drawing_plan_merges_layouts_not_analysis_order(self):
        first=f._panel_structure(["matrix_heatmap","line_band"],columns=2)
        repeated=f._panel_structure(["matrix_heatmap","matrix_heatmap","line_band"],columns=1)
        reversed_spec=f._panel_structure(["line_band","matrix_heatmap"],columns=2)
        self.assertEqual(f.family_for_spec(first)["id"],f.family_for_spec(repeated)["id"])
        self.assertNotEqual(f.family_for_spec(first)["variant_id"],f.family_for_spec(repeated)["variant_id"])
        self.assertNotEqual(f.family_for_spec(first)["id"],f.family_for_spec(reversed_spec)["id"])

    def test_catalog_families_preserve_every_existing_example_without_plotting_imports(self):
        index=f.families()
        self.assertEqual(index["total_examples"],151)
        member_ids=[key for row in index["families"] for key in row["member_ids"]]
        self.assertEqual(len(member_ids),len(set(member_ids)))
        self.assertTrue({row["id"] for row in f.examples()}<=set(member_ids))
        self.assertLess(index["total_families"],index["total_examples"])
        code="import sys;sys.path.insert(0,sys.argv[1]);import ccfa_figure_library as f;f.families();assert 'numpy' not in sys.modules;assert 'matplotlib' not in sys.modules"
        subprocess.run([sys.executable,"-c",code,str(MODULES)],check=True,capture_output=True)

    def test_route_has_one_candidate_per_drawing_family_and_keeps_field_checks(self):
        result=f.route("uncertainty",count=12,seed=0)
        ids=[row["family_id"] for row in result["candidates"]]
        self.assertEqual(len(ids),len(set(ids)))
        for row in result["candidates"]:
            self.assertEqual(row["required"],f.explain(row["id"])["required"])

    def test_routing_needs_no_plotting_dependencies_or_network(self):
        code="import sys;sys.path.insert(0,sys.argv[1]);import ccfa_figure_library as f;f.route('分布',seed=2);assert 'numpy' not in sys.modules;assert 'matplotlib' not in sys.modules;assert 'requests' not in sys.modules"
        subprocess.run([sys.executable,"-c",code,str(MODULES)],check=True,capture_output=True)

    def test_semantic_compatibility_precedes_randomness(self):
        for seed in range(25):
            result=f.route("agreement",fields=["first","second"],seed=seed)
            self.assertEqual([c["id"] for c in result["candidates"]],["bland_altman"])

    def test_unknown_question_is_not_routed_arbitrarily(self):
        with self.assertRaisesRegex(ValueError,"No intent"):
            f.route("unmatched-concept-zzzz",seed=0)

    def test_default_route_uses_automatic_randomness_without_a_user_seed(self):
        with patch.object(f.random,"SystemRandom",wraps=f.random.SystemRandom) as system:
            result=f.route("distribution")
        self.assertTrue(system.called)
        self.assertEqual(result["randomness"],"automatic")
        self.assertNotIn("seed",result)

    def test_article_data_conditions_exclude_false_pairing(self):
        brief={"claim":"两组群体不是相同样本","intent_ids":["paired_change"],
               "data":{"fields":["labels","before","after"],"paired":False}}
        result=f.route(context=brief)
        self.assertFalse(result["candidates"])
        self.assertEqual({r["id"] for r in result["incompatible_charts"]},{"dumbbell","mean_delta"})

    def test_article_checkpoint_order_preserves_a_folding_state_axis(self):
        brief={"question":"模型训练过程","intent_ids":["dynamics"],
               "data":{"fields":["x","y","steps"],"ordered_x":False,"checkpoint_order":True}}
        result=f.route(context=brief)
        self.assertEqual(result["candidates"][0]["id"],"ordered_trajectory")
        self.assertIn("line_band",{r["id"] for r in result["incompatible_charts"]})

    def test_article_long_names_change_the_fit_before_random_choice(self):
        brief={"question":"比较整体表现","intent_ids":["comparison"],"data":{},"layout":{"long_labels":True}}
        for _ in range(5):
            result=f.route(context=brief,count=1)
            self.assertTrue(f.explain(result["candidates"][0]["id"])["horizontal_labels"])

    def test_article_panel_limit_and_final_size_filter_fusion_options(self):
        brief={"question":"配对变化","data":{"paired":True},"layout":{"max_panels":1}}
        self.assertEqual(f.route(context=brief)["fusion_options"],[])
        brief["layout"]={"width_mm":70,"height_mm":28}
        self.assertEqual(f.route(context=brief)["fusion_options"],[])

    def test_unknown_paper_conditions_remain_questions_not_facts(self):
        result=f.route("dumbbell")
        self.assertIn("Confirm paired=True before using this chart",result["candidates"][0]["check_before_use"])

    def test_fusion_cannot_recommend_a_missing_data_analysis(self):
        brief={"question":"calibration","data":{"fields":["confidence","accuracy","counts"]}}
        result=f.route(context=brief)
        self.assertEqual([c["id"] for c in result["candidates"]],["calibration"])
        self.assertEqual(result["fusion_options"],[])
        brief["data"]["fields"] += ["coverage","risk","precision","recall"]
        self.assertIn("calibration_decision",{x["id"] for x in f.route(context=brief)["fusion_options"]})

    def test_fusion_respects_each_explicit_member_exclusion(self):
        brief={"question":"calibration","data":{"fields":["confidence","accuracy","counts","coverage","risk","precision","recall"]}}
        for kind in ("calibration","risk_coverage","precision_recall"):
            with self.subTest(kind=kind):
                self.assertNotIn("calibration_decision",{x["id"] for x in f.route(context=brief,exclude=[kind])["fusion_options"]})
                requested=copy.deepcopy(brief);requested["exclude_charts"]=[kind]
                self.assertNotIn("calibration_decision",{x["id"] for x in f.route(context=requested)["fusion_options"]})

    def test_fusion_members_keep_the_same_declared_condition_filter(self):
        fields=sorted(set().union(*(set(f.explain(k)["required"]) for k in ("dumbbell","mean_delta","bland_altman"))))
        brief={"question":"paired change","intent_ids":["paired_change"],"data":{"fields":fields,"paired":False}}
        self.assertEqual(f.route(context=brief)["fusion_options"],[])

    def test_fusion_ranking_uses_article_preference_before_catalog_order(self):
        brief={"question":"distribution composition association",
               "preferred_charts":["binned_group_composition"]}
        for _ in range(5):
            result=f.route(context=brief)
            self.assertEqual(result["fusion_options"][0]["id"],"common_bins")
            scores=[row["score"] for row in result["fusion_options"]]
            self.assertEqual(scores,sorted(scores,reverse=True))
            self.assertIn("Matches an explicit article design preference",result["fusion_options"][0]["paper_fit"])
        changed=copy.deepcopy(f.catalog());changed["fusions"].reverse()
        with patch.object(f,"catalog",return_value=changed):
            self.assertEqual(f.route(context=brief)["fusion_options"][0]["id"],"common_bins")

    def test_fusion_ties_use_random_choice_and_optional_accepted_history(self):
        brief={"question":"distribution association"}
        seen=[]
        class Chooser:
            def choices(self,tier,weights,k):
                if len(tier)>1:seen.append(([item[1]["id"] for item in tier],weights))
                return [tier[-1]]
        usage={"version":1,"counts":{"raincloud":50,"ecdf":50,"binned_summary":50}}
        with patch.object(f.random,"SystemRandom",return_value=Chooser()):
            result=f.route(context=brief,usage=usage)
        self.assertEqual(result["fusion_options"][0]["id"],"spectral_comparison")
        tier,weights=next((tier,weights) for tier,weights in seen if "distribution_tails" in tier)
        self.assertLess(weights[tier.index("distribution_tails")],weights[tier.index("common_bins")])

    def test_font_size_reaches_templates_layouts_ticks_and_legends(self):
        specs=[f.example_spec("original:paired_effects",demo=True),
               f.example_spec("original:sensitivity_dynamics",demo=True)]
        specs += [f.layout_spec(kind,demo=True) for kind in ("joint_marginals","aligned_tracks","matrix_slices")]
        for spec in specs:
            with self.subTest(container=spec.get("template",spec.get("layout"))):
                spec["font_size"]=14
                fig=f.compose(spec)
                labeled=[ax for ax in fig.axes if ax.get_xlabel() or ax.get_ylabel()]
                self.assertTrue(labeled)
                for ax in labeled:
                    if ax.get_xlabel():self.assertEqual(ax.xaxis.label.get_fontsize(),14)
                    if ax.get_ylabel():self.assertEqual(ax.yaxis.label.get_fontsize(),14)
                    for tick in ax.get_xticklabels()+ax.get_yticklabels():
                        self.assertEqual(tick.get_fontsize(),13.5)
                legends=[ax.get_legend() for ax in fig.axes if ax.get_legend()]
                for legend in legends:
                    self.assertTrue(all(t.get_fontsize()>=13 for t in legend.get_texts()))
                if spec.get("template"):self.assertTrue(legends)
                plt.close(fig)

    def test_all_composition_containers_reject_an_invalid_font_size(self):
        for container in ({"template":"paired_effects","data":{}},{"layout":"joint_marginals","data":{}},{"panels":[]}):
            for size in (0,5,25,float("nan"),float("inf")):
                with self.subTest(container=container,size=size),self.assertRaisesRegex(ValueError,"font_size"):
                    f.compose({"version":1,"font_size":size,**container})

    def test_fourteen_point_chinese_layout_reaches_an_actual_editable_export(self):
        from xml.etree import ElementTree as ET
        import ccfa_analysis_panels as panels
        spec={"version":1,"layout":"aligned_tracks","font_size":14,"height_mm":130,
            "data":{"x":[1,2,3],"xlabel":"共享位置","tracks":[
                {"label":"觀測信號","unit":"counts","series":[
                    {"label":"观测","y":[1,2,3]},{"label":"預測","y":[1.2,1.9,3.1]}]}]}}
        fig=f.compose(spec)
        self.assertEqual(panels.audit_figure(fig)["missing_glyphs"],[])
        self.assertEqual(panels.audit_figure(fig)["text_outside_canvas"],[])
        with tempfile.TemporaryDirectory() as folder:
            output=f.export(spec,Path(folder)/"中文字号",formats=("svg",),python_source=False)
            svg=ET.fromstring(output["svg"].read_text(encoding="utf-8"))
            texts=svg.findall(".//{http://www.w3.org/2000/svg}text")
            label=next(t for t in texts if "".join(t.itertext())=="共享位置")
            self.assertIn("14px",label.attrib["style"])
            self.assertIn("觀測信號","".join(svg.itertext()))

    def test_conflicting_fields_or_unknown_context_properties_are_errors(self):
        with self.assertRaisesRegex(ValueError,"disagree"):
            f.route("comparison",fields=["x"],context={"data":{"fields":["y"]}})
        with self.assertRaises(ValueError):f.route("comparison",context={"claim":"text","data":{"paierd":True}})

    def test_demo_is_random_by_default_and_saved_values_stay_stable(self):
        one=f.demo_spec(["ecdf"]);two=f.demo_spec(["ecdf"])
        self.assertNotEqual(one["panels"][0]["data"],two["panels"][0]["data"])
        self.assertNotIn("seed",one["_meta"])
        before=copy.deepcopy(one);f.compose(one);self.assertEqual(one,before)

    def test_original_templates_and_both_user_reference_pairs_remain_indexed(self):
        rows=f.examples();ids={row["id"] for row in rows}
        self.assertEqual(len([r for r in rows if r["category"]=="original"]),9)
        self.assertTrue({"original:sensitivity_dynamics","reference:sensitivity-pair","reference:dynamics-pair"}.issubset(ids))
        for example_id,pair in [("reference:sensitivity-pair","sensitivity"),("reference:dynamics-pair","dynamics")]:
            spec=f.example_spec(example_id,demo=True)
            self.assertEqual(spec["data"]["panel_pair"],pair)
            fig=f.compose(spec);self.assertGreaterEqual(len(fig.axes),2)

    def test_linked_layout_example_does_not_fill_missing_real_data(self):
        spec=f.example_spec("layout:aligned_tracks",demo=True)
        self.assertEqual(spec["layout"],"aligned_tracks")
        fig=f.compose(spec);self.assertTrue(hasattr(fig,"ccfa_layout"))
        with self.assertRaisesRegex(ValueError,"Supply"):
            f.example_spec("layout:aligned_tracks")

    def test_unavailable_data_yields_no_fabricated_chart(self):
        self.assertEqual(f.route("composition",fields=["labels"],seed=0)["candidates"],[])

    def test_equal_fit_sampling_is_replayable_and_diverse(self):
        a=f.route("distribution",count=3,seed=71)
        self.assertEqual(a,f.route("distribution",count=3,seed=71))
        self.assertEqual(len({c["id"] for c in a["candidates"]}),3)
        first={f.route("distribution",count=1,seed=s)["candidates"][0]["id"] for s in range(70)}
        self.assertGreater(len(first),4)

    def test_usage_balances_only_appropriate_candidates(self):
        kinds=[c["id"] for c in f.catalog()["charts"] if "distribution" in c["intents"]]
        frequent=kinds[0]
        usage={"version":1,"counts":{frequent:10000}}
        before=copy.deepcopy(usage)
        selections=[f.route("distribution",count=1,seed=s,usage=usage)["candidates"][0]["id"] for s in range(60)]
        self.assertEqual(usage,before)
        self.assertNotIn(frequent,selections)
        self.assertTrue(set(selections).issubset(kinds))

    def test_routing_does_not_record_suggestions_and_record_is_explicit(self):
        with tempfile.TemporaryDirectory() as folder:
            path=Path(folder)/"usage.json"
            f.route("distribution",seed=0)
            self.assertFalse(path.exists())
            result=f.record_selection(path,["ecdf","ecdf","raincloud"])
            self.assertEqual(result["counts"],{"ecdf":2,"raincloud":1})
            self.assertEqual(json.loads(path.read_text(encoding="utf-8")),result)

    def test_bad_history_and_unknown_exclusions_are_reported(self):
        for state in ({"version":1,"counts":{"ecdf":-1}},{"version":1,"counts":{"ecdf":True}},{"version":2,"counts":{}}):
            with self.assertRaises(ValueError):f.route("distribution",usage=state)
        with self.assertRaises(ValueError):f.route("distribution",exclude=["fake"])

    def test_every_chart_has_design_reason_and_data_contract(self):
        for chart in f.catalog()["charts"]:
            self.assertTrue(chart["why"])
            self.assertTrue(chart["avoid_when"])
            self.assertTrue(chart["fusion_role"])
            self.assertTrue(chart["required"])
            self.assertTrue(set(chart["intents"]).issubset(f.catalog()["intents"]))

    def test_every_chart_composes_serializable_simulation_without_input_changes(self):
        for chart in f.catalog()["charts"]:
            with self.subTest(chart=chart["id"]):
                spec=f.demo_spec([chart["id"]],seed=5)
                original=json.dumps(spec,sort_keys=True,allow_nan=False)
                fig=f.compose(spec)
                self.assertEqual(original,json.dumps(spec,sort_keys=True,allow_nan=False))
                self.assertTrue(any("Simulated" in t.get_text() for t in fig.texts))
                plt.close(fig)

    def test_real_composition_never_calls_demo_or_fills_missing_values(self):
        spec=f.demo_spec(["ecdf"],seed=0);spec.pop("_meta")
        with patch.object(f,"demo_data",side_effect=AssertionError("no simulation")):
            fig=f.compose(spec)
            self.assertFalse(any("Simulated" in t.get_text() for t in fig.texts))
            spec["panels"][0]["data"]={}
            with self.assertRaises(TypeError):f.compose(spec)

    def test_each_fusion_renders_all_requested_panels(self):
        for fusion in f.catalog()["fusions"]:
            with self.subTest(fusion=fusion["id"]):
                fig=f.compose(f.demo_fusion(fusion["id"],seed=2))
                self.assertGreaterEqual(len(fig.axes),len(fusion["panels"]))
                plt.close(fig)

    def test_overlapping_or_out_of_bounds_layouts_are_rejected(self):
        spec=f.demo_spec(["ecdf","raincloud"])
        spec["panels"][1]["column"]=0
        with self.assertRaisesRegex(ValueError,"overlap"):f.compose(spec)
        spec["panels"][1]["column"]=10
        with self.assertRaisesRegex(ValueError,"exceeds"):f.compose(spec)

    def test_final_size_and_unknown_fields_are_not_silently_repaired(self):
        spec=f.demo_spec(["ecdf","raincloud","line_band"]);spec["width_mm"]=90
        with self.assertRaisesRegex(ValueError,"too small"):f.compose(spec)
        spec=f.demo_spec(["ecdf"]);spec["panels"][0]["data"]["made_up"]=1
        with self.assertRaises(TypeError):f.compose(spec)

    def test_shared_axes_require_matching_semantics_and_transform(self):
        spec=f.demo_spec(["line_band","line_band"])
        ids=[p["id"] for p in spec["panels"]]
        spec["shared_axes"]=[{"axis":"y","panels":ids}]
        with self.assertRaisesRegex(ValueError,"meaning"):f.compose(spec)
        for panel in spec["panels"]:panel["y_meaning"]="Accuracy, fraction"
        spec["panels"][1]["data"]["y"]=[x+.5 for x in spec["panels"][1]["data"]["y"]]
        spec["panels"][1]["data"].pop("lower");spec["panels"][1]["data"].pop("upper")
        fig=f.compose(spec)
        self.assertEqual(fig.axes[0].get_ylim(),fig.axes[1].get_ylim())

    def test_entity_colors_are_stable_under_different_local_orders(self):
        spec=f.demo_spec(["comparison_intervals","comparison_intervals"])
        spec["entity_order"]=["Base","Variant","Proposed"]
        for panel in spec["panels"]:panel["entity_ids"]=panel["data"]["labels"]
        spec["panels"][1]["entity_ids"]=list(reversed(spec["entity_order"]))
        for key in ("labels","values","lower","upper","runs"):
            spec["panels"][1]["data"][key]=list(reversed(spec["panels"][1]["data"][key]))
        fig=f.compose(spec)
        a=fig.axes[0].collections[-1].get_facecolors()[0]
        b=fig.axes[1].collections[0].get_facecolors()[0]
        self.assertTrue((a[:3]==b[:3]).all())

    def test_entity_ids_cannot_relabel_groups_by_only_reordering_colors(self):
        spec=f.demo_spec(["comparison_intervals"])
        spec["entity_order"]=["Base","Variant","Proposed"]
        spec["panels"][0]["entity_ids"]=list(reversed(spec["entity_order"]))
        with self.assertRaisesRegex(ValueError,"actual plotted group"):
            f.compose(spec)

    def test_later_layer_cannot_crop_earlier_rank_observations(self):
        spec=f.demo_spec(["rank_trajectories"])
        panel=spec["panels"][0]
        panel["data"]={"stages":["A","B","C"],"ranks":[[1,3,5],[5,2,1]],"labels":["One","Two"]}
        panel.update(x_meaning="Stage",y_meaning="Rank")
        panel["layers"]=[{"kind":"rank_trajectories","x_meaning":"Stage","y_meaning":"Rank",
                          "data":{"stages":["A","B","C"],"ranks":[[1,2,3],[3,2,1]],"labels":["Other","Extra"]}}]
        fig=f.compose(spec);low,high=sorted(fig.axes[0].get_ylim())
        self.assertLess(low,1);self.assertGreater(high,5)

    def test_overlay_rejects_reordered_category_labels_on_either_axis(self):
        for kind in ("comparison_intervals","paired_distribution"):
            with self.subTest(kind=kind):
                spec=f.demo_spec([kind]);panel=spec["panels"][0]
                panel.update(x_meaning="Shared X",y_meaning="Shared Y")
                data=copy.deepcopy(panel["data"]);data["labels"].reverse()
                panel["layers"]=[{"kind":kind,"data":data,"x_meaning":"Shared X","y_meaning":"Shared Y"}]
                with self.assertRaisesRegex(ValueError,"ordered categories"):
                    f.compose(spec)

    def test_matrix_overlay_checks_both_domains_and_actual_cell_centers(self):
        for field in ("row_labels","col_labels"):
            spec=f.demo_spec(["matrix_heatmap"]);panel=spec["panels"][0]
            panel.update(x_meaning="Feature",y_meaning="Group")
            data=copy.deepcopy(panel["data"]);data[field].reverse()
            panel["layers"]=[{"kind":"matrix_heatmap","data":data,"x_meaning":"Feature","y_meaning":"Group"}]
            with self.subTest(field=field),self.assertRaisesRegex(ValueError,"ordered categories"):
                f.compose(spec)
        panel["layers"][0]["kind"]="dot_matrix"
        panel["layers"][0]["data"]=copy.deepcopy(panel["data"])
        panel["layers"][0]["data"]["sizes"]=[[20]*4 for _ in range(4)]
        with self.assertRaisesRegex(ValueError,"coordinate slots"):
            f.compose(spec)

    def test_ranked_overlay_compares_displayed_sort_order(self):
        spec=f.demo_spec(["ranked_intervals"]);panel=spec["panels"][0]
        panel.update(x_meaning="Value",y_meaning="Method")
        data=copy.deepcopy(panel["data"]);data.update(order="descending")
        panel["layers"]=[{"kind":"ranked_intervals","data":data,"x_meaning":"Value","y_meaning":"Method"}]
        with self.assertRaisesRegex(ValueError,"ordered categories"):
            f.compose(spec)

    def test_scatter_entity_labels_are_not_categorical_axis_slots(self):
        spec=f.demo_spec(["pareto_scatter"]);panel=spec["panels"][0]
        panel.update(x_meaning="Cost",y_meaning="Quality")
        data=copy.deepcopy(panel["data"])
        for key in ("labels","x","y"):data[key].reverse()
        panel["layers"]=[{"kind":"pareto_scatter","data":data,"x_meaning":"Cost","y_meaning":"Quality"}]
        fig=f.compose(spec)
        self.assertEqual(len(fig.axes),1)

    def test_shared_categorical_axis_requires_the_same_order(self):
        spec=f.demo_spec(["paired_distribution","paired_distribution"])
        for panel in spec["panels"]:panel["x_meaning"]="Method"
        spec["panels"][1]["data"]["labels"].reverse()
        spec["shared_axes"]=[{"axis":"x","panels":[p["id"] for p in spec["panels"]]}]
        with self.assertRaisesRegex(ValueError,"ordered categories"):
            f.compose(spec)

    def test_single_entity_layer_uses_the_same_binding_as_other_panels(self):
        from ccfa_plot_recipes import PALETTES
        spec=f.demo_spec(["line_band","line_band"])
        spec["entity_order"]=["A","B"]
        first,second=spec["panels"]
        first.update(entity_ids=["A"],color_argument="color",x_meaning="Steps",y_meaning="Score")
        second.update(entity_ids=["B"],color_argument="color")
        layer={"kind":"line_band","data":copy.deepcopy(second["data"]),
               "entity_ids":["B"],"color_argument":"color","x_meaning":"Steps","y_meaning":"Score"}
        first["layers"]=[layer]
        fig=f.compose(spec)
        self.assertEqual(fig.axes[0].lines[1].get_color(),fig.axes[1].lines[0].get_color())
        self.assertEqual(fig.axes[0].lines[1].get_color(),PALETTES["npg"][1])
        self.assertNotEqual(fig.axes[0].lines[0].get_color(),fig.axes[0].lines[1].get_color())
        # Explicit IDs also provide an identity order when the spec omits it.
        spec.pop("entity_order");fig=f.compose(spec)
        self.assertEqual(fig.axes[0].lines[1].get_color(),fig.axes[1].lines[0].get_color())
        layer["entity_ids"]=["A","B"]
        with self.assertRaisesRegex(ValueError,"single entity"):
            f.compose(spec)

    def test_quantitative_color_has_a_readable_scale_by_default(self):
        spec=f.demo_spec(["matrix_heatmap"])
        spec["panels"][0]["colorbar_label"]="Transfer gain"
        fig=f.compose(spec)
        self.assertEqual(len(fig.axes),2)
        self.assertEqual(fig.axes[1].get_ylabel(),"Transfer gain")

    def test_ascii_words_do_not_match_inside_other_words(self):
        with self.assertRaisesRegex(ValueError,"No intent"):f.route("process",seed=0)
        self.assertIn("operating_tradeoff",f.route("ROC",seed=0)["intents"])

    def test_simplified_traditional_and_english_questions_share_the_correct_route(self):
        for question in ("置信度校准","置信度校準","calibration"):
            result=f.route(question,fields=["confidence","accuracy","counts"],seed=3)
            self.assertEqual(result["candidates"][0]["id"],"calibration")
        result=f.route("訓練相空間軌跡",fields=["x","y","steps"],seed=9)
        self.assertEqual(result["candidates"][0]["id"],"ordered_trajectory")

    def test_returned_candidate_cannot_poison_later_routing(self):
        result=f.route("distribution",seed=3)
        original=copy.deepcopy(result)
        result["candidates"][0]["required"].append("polluted")
        self.assertEqual(f.route("distribution",seed=3),original)

    def test_palette_changes_group_colors_and_keeps_explicit_colors(self):
        from matplotlib.colors import to_rgba
        from ccfa_plot_recipes import PALETTES
        spec=f.demo_spec(["comparison_intervals"])
        spec["panels"][0]["data"].pop("runs")
        spec["palette"]="lancet"
        fig=f.compose(spec)
        self.assertEqual(tuple(fig.axes[0].collections[0].get_facecolors()[0]),to_rgba(PALETTES["lancet"][0]))
        spec["panels"][0]["data"]["colors"]=["black"]*3
        fig=f.compose(spec)
        self.assertEqual(tuple(fig.axes[0].collections[0].get_facecolors()[0]),to_rgba("black"))

    def test_paired_fusion_reuses_actual_observations(self):
        spec=f.demo_spec(["dumbbell","mean_delta","bland_altman"],seed=8)
        a,b,c=[panel["data"] for panel in spec["panels"]]
        self.assertEqual(a["before"],b["before"])
        self.assertEqual(a["after"],c["second"])
        self.assertEqual(b["before"],c["first"])

    def test_common_bins_fusion_preserves_observation_identity_and_edges(self):
        spec=f.demo_spec(["mirrored_histogram","binned_group_composition","ecdf"],seed=9)
        a,b,c=[panel["data"] for panel in spec["panels"]]
        self.assertEqual(a["bin_edges"],b["bin_edges"])
        self.assertEqual(a["first"]+a["second"],b["values"])
        self.assertEqual(b["values"],c["samples"])
        self.assertEqual(len(b["groups"]),len(b["values"]))

    def test_response_slices_are_taken_from_the_displayed_grid(self):
        spec=f.demo_spec(["contour_response","line_band","line_band"])
        a,b,c=[panel["data"] for panel in spec["panels"]]
        self.assertEqual(b["y"],a["response"][len(a["y"])//2])
        self.assertEqual(c["y"],[row[len(a["x"])//2] for row in a["response"]])

    def test_overlay_requires_shared_meaning_and_preserves_own_values(self):
        spec=f.demo_spec(["line_band"])
        panel=spec["panels"][0]
        overlay={"kind":"line_band","data":{"x":[1,2,3],"y":[.2,.5,.8]}}
        panel["layers"]=[overlay]
        with self.assertRaisesRegex(ValueError,"meaning"):f.compose(spec)
        for target in (panel,overlay):target.update(x_meaning="Budget, steps",y_meaning="Accuracy, fraction")
        overlay["style"]={"linestyle":"--","marker":"x"}
        fig=f.compose(spec)
        self.assertEqual(list(fig.axes[0].lines[-1].get_ydata()),[.2,.5,.8])
        self.assertEqual(fig.axes[0].lines[-1].get_linestyle(),"--")

    def test_log_scale_cannot_silently_hide_nonpositive_data(self):
        spec=f.demo_spec(["line_band"])
        spec["panels"][0]["yscale"]="log"
        spec["panels"][0]["data"]={"x":[1,2,3],"y":[-.1,.2,.5]}
        with self.assertRaisesRegex(ValueError,"nonpositive"):f.compose(spec)

    def test_export_normalizes_base_and_generated_python_keeps_formats(self):
        import runpy
        with tempfile.TemporaryDirectory() as folder:
            outputs=f.export(f.demo_spec(["ecdf"]),Path(folder)/"figure.svg",formats=("svg",))
            self.assertEqual(outputs["python"].name,"figure.py")
            with patch.object(f,"export",return_value={}) as writer:
                runpy.run_path(str(outputs["python"]),run_name="__main__")
            self.assertEqual(writer.call_args.kwargs["formats"],("svg",))

    def test_default_cli_and_generated_source_never_add_svg_or_pdf(self):
        import runpy
        with tempfile.TemporaryDirectory() as folder:
            base = Path(folder) / "ordinary"
            cli = subprocess.run([sys.executable, "-B", "-X", "utf8", str(MODULES / "ccfa_figure_library.py"),
                "demo", "line_band", "--out", str(base)], capture_output=True, text=True, encoding="utf-8")
            self.assertEqual(cli.returncode, 0, cli.stderr)
            result = json.loads(cli.stdout)
            self.assertTrue(base.with_suffix(".png").is_file())
            self.assertNotIn("svg", result)
            self.assertNotIn("pdf", result)
            with patch.object(f, "export", return_value={}) as writer:
                runpy.run_path(str(base.with_suffix(".py")), run_name="__main__")
            self.assertEqual(writer.call_args.kwargs["formats"], ("png",))
            self.assertFalse(base.with_suffix(".svg").exists())
            self.assertFalse(base.with_suffix(".pdf").exists())

    def test_edited_source_is_exported_without_overwriting_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder)/"图例"
            spec=f.demo_spec(["ecdf","mean_delta"],seed=9)
            outputs=f.export(spec,base)
            self.assertTrue(outputs["python"].exists())
            source=outputs["python"].read_text(encoding="utf-8")
            compile(source,str(outputs["python"]),"exec")
            self.assertEqual(set(outputs), {"png", "metadata", "python"})
            self.assertFalse(base.with_suffix(".svg").exists())
            self.assertTrue(json.loads(outputs["metadata"].read_text(encoding="utf-8"))["composition"]["_meta"]["synthetic"])
            namespace={"__name__":"library_test","__file__":str(outputs["python"])}
            exec(compile(source,str(outputs["python"]),"exec"),namespace)
            self.assertEqual(namespace["SPEC"],spec)
            with self.assertRaisesRegex(ValueError,"protected"):
                f.export(spec,base,protected_paths=[outputs["python"]])

    def test_source_studies_are_resolved_and_require_explicit_demo(self):
        studies=json.loads((f.LIBRARY/"studies.json").read_text(encoding="utf-8"))
        self.assertGreater(len(studies),20)
        for study in studies:
            self.assertTrue(study["source_id"])
            self.assertTrue(study["why"])
            self.assertTrue(all(explainable in {c["id"] for c in f.catalog()["charts"]} for explainable in study["panel_plan"]))
        with self.assertRaisesRegex(ValueError,"Supply"):
            f.study_spec(studies[0]["id"])


if __name__=="__main__":unittest.main()
