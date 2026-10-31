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

    def test_edited_source_is_exported_without_overwriting_inputs(self):
        with tempfile.TemporaryDirectory() as folder:
            base=Path(folder)/"图例"
            spec=f.demo_spec(["ecdf","mean_delta"],seed=9)
            outputs=f.export(spec,base)
            self.assertTrue(outputs["python"].exists())
            source=outputs["python"].read_text(encoding="utf-8")
            compile(source,str(outputs["python"]),"exec")
            self.assertIn("Simulated",outputs["svg"].read_text(encoding="utf-8"))
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
