# 数据分析图的设计与组合素材库

论文单图优先按实际版面选取，通常从单栏约85–90 mm起稿。在同一坐标系统中组合有意义的位置、颜色、符号、面积和配对连线；需要局部细节时再加小型放大图。多面板只用于确有必要的不同问题或数据域。现有组合案例仍保留，`compose --panel <id>`可单独复用一个面板及其叠加图层，原数据、颜色身份和组合来源不变。

先说清楚图要让读者发现什么，再选图法。一个均值差异、一个长尾问题和一次配对变化，需要的观察单位与布局并不相同。素材库按这些表达目的组织；会议和期刊只用于定位已检查的图例，不作为固定外观预设。

## 已选模板：复用原规格，只换数据

用户选中图库入口、命名模板、JSON或Python后，直接读取该规格和绘制实现。不要重新运行demo、换一个相似原语或凭缩略图重写。画布、字号、配色身份、图层与统计定义沿用所选规格；输入不兼容就解决具体字段，不默默换图。

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py compose --spec selected.json --data supplied.json --out ccfa-workfiles/figures/analysis/build/figure
```

`replace_data(spec, supplied)`返回新规格，不改原文件。原生template/layout传入完整新data对象；普通面板组合传入`{"panels":[{"id":"panel-1","data":{...},"layers":[{"data":{...}}]}]}`，提供所有选中面板及叠加层。`compose --panel <id>`先提取目标面板，再绑定其新数据，不要求未选面板。CSV/TSV仍用已有table bindings修改源路径/列映射；不要混用半份原始JSON替换和旧表格绑定。

展示参数与观测分开：颜色、点形、字号等可以继承，series按稳定method/label身份匹配；缺失的观测、范围或权重不能用旧demo补上。检查`_meta.retained_text_to_check`中的静态标题／说明是否仍符合新数据，按实际任务更新。demo来源元数据不冒充新数据来源。

只有未选定设计的新任务才运行问题／数据路由。同分的可用设计可以随机选择；选定之后的渲染与修改保持该设计，不再抽样换图。

`original:mechanism_overview`保留为“已批准的方法PNG＋数值分析”的混合模板：`data.mechanism.image`必须指向现有PNG，代码只放置原图，不从stage标签重建框和箭头。示例使用已有插图与明确标记的模拟分析；真实任务需换成当前方法图。

## 三层入口

- `resources/figure-library/catalog.json`：43 种原语的表达目的、必需字段、选择理由，以及 16 种组合入口。先通过路由读少量候选，不把整个文件塞进上下文。
- `resources/figure-library/studies.json`：78 张已检查图例的设计卡。每张说明原图布局、为什么这样设计、真实数据需要哪些字段、可以怎样融合及当前实现的适配范围。累计 75 张有直接视觉检查记录，3 张复用早期记录；本轮新增 25 张；复用情况单独标记。
- `resources/python/ccfa_figure_library.py`：小路由、图例演示和组合器。调用已有 `ccfa_analysis_panels.py` 及新增 `ccfa_semantic_panels.py`；原来的九套 `ccfa_analysis_templates.py` 数值模板继续可用；数值 SVG/PDF 仅按明确要求导出。

设计卡使用 `source_id` 连接 Common 的来源登记，不重复收录论文 URL，也不附带原论文图片。这里复现的是**可用于新数据的分析关系与排版结构**，不是原论文的数值结果或逐像素图像。非直接支持的极坐标、三维示意、图像拼贴、生物结构注释等，逐卡在 `adaptation_notes` 说明如何转换或继续编辑。

## 按绘制家族归并，按科学问题选择

一张论文设计卡记录一种使用情境，不必占一个新的模板入口。导航分成**绘制家族 → 结构变体 → 科学情境**：先展示组合与代表图，同一绘制计划的网格、分面数量、其他论文、数据和配色放在家族内部；基础原语保留为编辑零件。原来的 ID、代码、来源和两个用户参考双面板均保留，可直接调用。

家族比较有序绘制计划、统计编码、共享坐标关系、叠加层、轴变换和实际启用的分析元素。同一图法的 2／4／8 面板分面共享家族，网格、跨度、面板数量及比例保留为结构变体；单图与分面仍分开。混合图按其有序图法组织，同一图法连续重复的数量留在变体中。只更改数据、标题、类别名称或配色，则仍是同一个结构变体下的不同情境。普通箱体与 median–P90/P99/P95 汇总、普通密度与带权重走廊标注的密度图保持不同家族；同一数据的图形相似不能省掉统计解释。

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py families
python ccf-visual-composer/resources/python/ccfa_figure_library.py families --member reference:sensitivity-pair
```

`route` 先检查当前文章的问题和数据，再给出每个家族的一个候选；同分时保留现有随机选择，不要求固定种子，也不生成额外图稿。`studies` 和 `examples` 仍能查到所有使用情境。候选中的 `family_id` 对应声明的基础结构；实际输入启用了区间、叠层或注释后，应按最终规格重新归类。

整理已有图库时可直接传实际规格，不读取全部论文或重新模拟数据：

```python
from ccfa_figure_library import families, family_for_spec

# entries 是已有图卡列表；specs 按图卡 ID 提供已读取的组合 JSON。
index = families(entries, specs=specs)
identity = family_for_spec(specs[entries[0]["id"]])
```

`index["families"]` 提供代表图 ID、完整成员 ID、各成员情境、表达目的、`variant_count` 和 `variants`。`family_for_spec` 的 `id` 识别家族，`variant_id` 识别严格结构；`drawing_signature` 继续保留网格、面板数量、跨度与完整共享坐标结构。家族的 `family_signature` 表达可复用计划，各变体的 `signature` 保留实际结构，可用 `families --variant <variant-id>` 查询。合并只发生在导航层，不丢失原始数据，不把一张示意图当作另一篇论文的完整复现。缺少规格的旧 SVG 保持独立入口，不能凭缩略图外形自动判定相同。

维护标准示例时，`examples.json` 可用紧凑的 `drawing_options` 声明默认启用的元素：例如对数轴、带权重走廊、median–P90 汇总、独立采样横坐标、轮廓柱、标注及给定区间。这里的 `true` 只表示元素存在，不是实测值，也不能直接当作绘图数据。标准家族索引据此识别参考图的完整结构，无需导入 NumPy／Matplotlib 或生成样本；真正渲染仍使用实际数据或显式请求的演示数据。参考双面板的签名只读取会绘制的那一半，另一半的调整不制造重复家族。默认演示改变分析元素后，维护测试对照原生演示与声明的签名，避免目录又退回只登记外框。

## 按表达目的找图

| 路由 ID | 先问什么 | 优先考虑 | 下一步怎样组合 |
| --- | --- | --- | --- |
| `comparison` | 整体水平差多少？ | `comparison_intervals`、`grouped_dot` | 接群体分布，检查均值是否由少量样本推动。 |
| `distribution` | 主体、长尾和异常值在哪里？ | `raincloud`、`ecdf`、`ridgeline` | 接阈值比例或同分箱群体组成。 |
| `shift` | 条件改变后，是平移还是形状改变？ | `ecdf`、`mirrored_histogram` | 接同一对象的配对变化，区分群体换了和个体变了。 |
| `paired_change` | 谁受益、谁退化，起点有影响吗？ | `dumbbell`、`mean_delta` | 接差值分布或按起点分层的区间。 |
| `agreement` | 两种测量有一致偏差吗？ | `bland_altman`、`mirror_stem` | 接原值对照和残差，不只展示相关系数。 |
| `uncertainty` | 效应方向和范围是否因群体而异？ | `forest_intervals`、`ranked_intervals` | 接原始样本分布，保留区间的统计含义。 |
| `calibration` | 说有多大把握，实际就有多准吗？ | `calibration` | 接分箱人数和风险–覆盖率，检查稀疏区间与实际使用。 |
| `operating_tradeoff` | 换阈值或允许拒答，要付出什么？ | `precision_recall`、`roc`、`risk_coverage` | 接选定操作点的样本量、成本和错误类型。 |
| `ranking` | 排名会随任务、阶段或扰动改变吗？ | `rank_trajectories`、`ranked_intervals` | 接实际性能差，避免把微小差异放大成名次故事。 |
| `dynamics` | 过程怎样到达终点，何时开始不稳定？ | `line_band`、`ordered_trajectory`、`convergence_envelope`、`quantile_fan` | 时间轴用递增序列；相空间按 checkpoint 顺序连线，允许回折。 |
| `composition` | 总体由什么组成，样本转移到哪里？ | `mosaic_composition`、`transition_matrix`、`ternary` | 接绝对人数和条件分布，明确每个分母。 |
| `association` | 空间、矩阵或表征关系是什么？ | `matrix_heatmap`、`dot_matrix`、`embedding_scatter` | 接群体统计或原空间量，避免只凭投影外形下结论。 |
| `error_structure` | 错误集中在什么位置和条件？ | `residual_diagnostics`、`matrix_heatmap` | 接校准和拒答曲线，说明错误怎样影响使用。 |
| `tradeoff` | 提升质量需要多少时间、资源或其他目标代价？ | `cost_quality_frontier`、`pareto_scatter`、`parallel_coordinates` | 接同预算剖面，声明每个目标是越大越好还是越小越好。 |
| `response` | 哪个控制因素重要，它们是否交互？ | `contour_response`、`matrix_heatmap` | 接同一响应矩阵抽出的行列切片。 |
| `generalization` | 换域、加噪或增加难度后还能保持吗？ | `robustness_profile`、`line_band` | 接具体群体、迁移差值和失败样本，不只留一个总分。 |

`mirror_stem` 适合共同位置上的两组峰、频谱或稀疏响应。`binned_group_composition` 将分数分箱与其中的群体组成连接起来。它们按数据关系选用，不限定生信或计算机视觉领域。

## 一张图是怎样想到的

1. **先写一句科学消息。** 例如“平均改善来自低资源语言，其他语言基本没变”，而不只写“展示实验结果”。
2. **确定观察单位。** 一行是样本、模型、随机种子、语言还是一次运行？有配对 ID 就保留配对，只有均值就不画出不存在的样本云。
3. **找到必须保留的关系。** 是位置对应、同一分箱、同一 checkpoint、共同基线，还是两个结果量之间的取舍？这些关系决定共享什么；颜色相同并不意味着数据可以共用数轴。
4. **选一个主视角，再选补充视角。** 主图回答核心问题，副图解释主图中尚未清楚的部分。例如“分布在哪里”配“这些区间由谁组成”，而不是把相同均值换三种图画一遍。
5. **按信息量分空间。** 长类别名用横向点区间；连续轨道共享横坐标；二维热图可比单行数据条带分配更多高度。允许矩形、跨行、跨列，少面板不需要硬填满网格。
6. **最后确定视觉语言。** 方法与群体颜色跨面板保持一致；保留必要参考线；字体按最终物理尺寸检查。先删重复标题、冗余数值和多余图例，再考虑缩小字体。

`observed_layout` 记录看到了什么，`why` 是维护者对设计作用的分析，`adaptation_notes` 说明现有 Python 实现怎样承接它们。三者分开，后续可以改进设计而不改写原文献事实。

几个可继续创作的例子：

| 设计卡 ID | 为什么这样组织 | 可以继续怎样改 |
| --- | --- | --- |
| `acl25-distribution-conditioned-composition` | 直方图找异常区间，同 bin 的组成图找异常来自哪些任务。 | 换成误差、延迟或生物测量值；保留同一批样本和 bin 边界。 |
| `nmi26-parameter-surface-with-slices` | 全局矩阵定位交互，少数切片解释局部行为。 | 接到超参数、噪声×数据规模、药物剂量×时间等问题。 |
| `nmi26-training-phase-trajectories` | 相同终点可能经由不同路径，状态平面与时间曲线互补。 | 用准确率×代价、误差×置信度、两个目标的 checkpoint 轨迹。 |
| `vision-poca-reward-conflict` | 样本级奖励冲突与最终双目标表现分工明确。 | 接训练曲线，检查冲突何时出现及实际影响；不靠散点推断因果。 |
| `vision-weather-variable-horizon-heatmap` | 不同数据维度需要不同面板高度。 | 用 GridSpec 跨行布局融合二维矩阵和一维轨道，避免填空白。 |
| `nm25-acquisition-budget-threshold-pair` | 评估标准和采集预算回答不同问题。 | 配入图像样本、质量曲线和采集成本，保留各自横轴。 |
| `nature26-aligned-genomic-tracks` | 同位置对齐后才容易找到预测与实测差异发生在哪一段。 | 用时序传感器、层级激活或基因组轨道；每轨道保留自己的单位。 |
| `nmi26-optimal-setting-butterfly` | 两组分布共用设置轴，直接比较峰值和偏移。 | 加累计覆盖率或同设置的质量曲线；镜像只表示分组，不是负计数。 |

## 使用 Python 路由与演示

以下命令在仓库根目录执行。路由与查卡只用标准库；渲染需要已有 NumPy、Matplotlib，不启动模型调用，也不自动下载论文。

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py list
python ccf-visual-composer/resources/python/ccfa_figure_library.py route "校准" --fields confidence accuracy counts --count 3
python ccf-visual-composer/resources/python/ccfa_figure_library.py explain calibration
python ccf-visual-composer/resources/python/ccfa_figure_library.py studies --intent calibration --limit 6
python ccf-visual-composer/resources/python/ccfa_figure_library.py studies --id acl25-distribution-conditioned-composition
```

`--fields` 按已有字段筛选可用原语，渲染器继续检查实际值。字段存在不等于指标定义已经相同；选择时仍要核对配对单位、分母、区间和目标方向。设计卡中的领域字段需要映射到所选原语的参数，不能仅重命名后省略这层含义检查。

需要演示图时，显式使用 `--demo` 生成模拟值。两个例子分别复现一张图例的分析关系和一个组合：

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py reproduce acl25-distribution-conditioned-composition --demo --out ccfa-workfiles/figures/bin-composition/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py demo --fusion response_slices --out ccfa-workfiles/figures/response-slices/figure
```

默认生成 PNG、Python 源和元数据，不自动导出 SVG；PDF/SVG 需显式指定 `--formats`。数值图的可编辑请求需按其真实源码／对象能力交付，不能把 Python 可复现或 PDF 可缩放等同于 PowerPoint 对象可编辑；新方法图放入 PPTX 仍是位图。文件保存在同一具名图稿目录；后续更新同一文件。Python 源含明确的 `SPEC`，可以替换输入、改面板跨度、标题、尺寸和配色后再次导出。共享模块在同一解压目录树或仓库中时，生成源会自行找到它；其他项目可将 `ccf-visual-composer/resources/python` 加入 Python 导入路径。

真实作图不加 `--demo`，传入包含实际数据的组合规范：

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py reproduce acl25-distribution-conditioned-composition --data ccfa-workfiles/figures/bin-composition/source/figure-spec.json --out ccfa-workfiles/figures/bin-composition/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py compose --spec ccfa-workfiles/figures/custom-analysis/source/figure-spec.json --out ccfa-workfiles/figures/custom-analysis/figure
```

`reproduce --data` 保留该卡规定的面板类型与顺序；`compose` 接受自定义组合。每个 panel 给出唯一 `id`、`kind`、`row`、`column`、`data`，可选 `rowspan`、`colspan`；整体给出 `rows`、`columns`、`width_mm`、`height_mm`。需要共享数轴时，声明同一指标与单位的 `x_meaning`/`y_meaning`，再在 `shared_axes` 中列出参与面板。不要将导出元数据外层对象直接当作组合规范。

进一步融合可以发生在同一个坐标轴内：panel 的 `layers` 为每层给出 `kind`、实际 `data` 及与底层相同的 `x_meaning`、`y_meaning`，例如在观察值上叠加独立提供的拟合曲线。线图层可通过 `style` 的 `linestyle`、`marker` 等区分观察、拟合和外推，不通过改数值制造视觉差别。panel 可声明 `xscale`、`yscale` 为 `linear` 或 `log`；非正值不能被对数轴默默隐藏。原语缺少的领域注释仍在导出的 Python 源中明确添加。

叠加层和共享分类轴还会核对实际类别顺序与坐标位置：A、B 和 B、A 不能直接叠在一起，矩阵的行列、排序区间图的显示顺序也要对应；热图单元中心与点矩阵的位置不同，需要先在自定义源中明确对齐。散点旁的实体名称不作为分类轴。底图和 layer 共用实体配色规则；单条曲线可声明 `entity_ids:["Method B"]`、`color_argument:"color"`，多组图使用与实际分组顺序相同的 `entity_ids`。顶层 `entity_order` 确定跨图颜色；省略时按首次出现的分组与显式实体登记。没有实体绑定的显式数据配色保持原样。

## 文章上下文，不增加一次填表

从已提供的文章、结果表和当前对话提取图的消息，不让用户为每张图重新填写资料。简单局部图直接传问题；上下文复杂时，把已有信息放入一份紧凑的 `figure-brief.json`，沿用当前图稿目录：

```json
{
  "version": 1,
  "question": "哪些任务受益，起点会影响改善吗？",
  "claim": "改善集中在原本表现较弱的任务",
  "section": "analysis",
  "intent_ids": ["paired_change"],
  "data": {
    "fields": ["labels", "before", "after"],
    "observation_unit": "同一任务在修改前后的测量",
    "paired": true,
    "sample_count": 12
  },
  "layout": {"width_mm": 183, "long_labels": true}
}
```

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py route --brief path/to/figure-brief.json
```

`intent_ids` 用于确认科学关系；`fields` 用于检查函数输入。`paired=false` 会排除需要匹配观测的图，`intervals_supplied=false` 排除必须给定区间的图；`ordered_x=false`、`checkpoint_order=true` 的状态轨迹保留时间顺序。还有原始样本、完整响应网格、现成嵌入、给定分位数等条件，只填写已经知道的事实。未知条件保留在候选的 `check_before_use` 中；不为了通过路由而把未知写成 true。可用 `preferred_charts` 或 `exclude_charts` 保留文章已选方向和当前用户要求。组合建议的每个面板同样遵守字段、排除项和数据条件；未声明字段时仍可探索，已经声明但不足的字段不会被当作现成可用的组合。

组合建议通过兼容检查后，再按主问题覆盖和成员对文章条件的贴合度排序，明确偏好也参与排序；重复的切片不会重复加分。最多返回三个组合，同分时自然随机选择，显式启用的已采用图法历史只影响同分选择。

## 直接用 CSV、TSV、JSON 里的结果

`compose --spec` 通过 `data_sources` 指定本地表，路径相对规范文件；panel 的 `table` 声明筛选和排序，`data` 再从同一组记录取列。例如一张前后对照图：

```json
{
  "version": 1, "rows": 1, "columns": 1,
  "data_sources": {"results": {"path": "results.csv"}},
  "panels": [{
    "id": "paired", "kind": "dumbbell", "row": 0, "column": 0,
    "table": {"source": "results", "order_by": "sample_id"},
    "data": {
      "labels": {"column": "sample_id", "dtype": "string"},
      "before": {"column": "before"},
      "after": {"column": "after"}
    }
  }]
}
```

表至少含 `sample_id,before,after` 三列。数值必须有限；空值、错误数字和缺列会报错，不变成零。`where` 可以按明确条件筛行，`order_by` 对所有绑定列使用同一个稳定顺序；layers 默认继承父 panel 的选择，也可声明自己的 `table`。

分组原始样本用 `{"groups":{"by":"method","value":"score","order":["A","B"]}}`；二维数值用 `{"matrix":{"row":"dataset","column":"method","value":"score","row_order":["D1","D2"],"column_order":["A","B"]}}`。矩阵要求明确行列顺序，重复格和缺失格均需上游处理，工具不私自求均值或补格。已有内嵌数组与颜色映射继续支持。规范文件和所有声明的表一并受到导出覆盖保护。

长表的配对分组增加 `pair_by`，例如 `{"groups":{"by":"method","value":"score","order":["A","B"],"pair_by":"subject"}}`。每组的样本 ID 必须唯一、集合相同；工具按第一组的样本顺序对齐其他组，行序不同不会连错样本。`labels` 仍须对应 `order`。`paired_distribution` 的 `paired=true`、`paired_effects` 模板及配对叠加层都检查此约定。匿名数据若已经明确按同一观察顺序排列，可改用 `matched_order:true`，并检查组长相同；没有身份或明确顺序的配对分组会报错。普通非配对分组保持原行为，已有按相同样本顺序提供的数组 API 无需增加字段。

组合规范顶层的 `font_size` 以 pt 表示，对普通面板、九套模板和三种联动布局都生效，默认仍为 8.5。主轴标签、刻度与图例沿用同一字号层级；放大文字后应检查最终物理尺寸和留白，避免把较大的图整体缩小回去。

## 三种真正联动的复合布局

43 种单坐标轴图法之外，`ccfa_figure_layouts.py` 提供三种共享真实数据关系的布局：

| 布局 | 需要的数据关系 | 图形怎样联动 |
| --- | --- | --- |
| `joint_marginals` | 同一批 x/y 观测，明确的两轴分箱边界 | 中央关系图与两侧边缘计数来自同一批样本。 |
| `aligned_tracks` | 共同位置 x，各轨数值和各自单位 | 所有轨道位置对齐；同轨的预测/观测共用位置，各轨量纲独立。 |
| `matrix_slices` | 实际 x/y 网格、响应矩阵、选定行列索引 | 热图标出切线，侧边曲线直接取该行/列；不另造剖面。 |

它们是三种完整布局，不把同一批图法重新计数成更多原语。真实规范使用 `{"version":1,"layout":"aligned_tracks","data":{...}}`，也支持顶层 `table` 与数据列绑定。演示需要显式选择：

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py layout matrix_slices --demo --out ccfa-workfiles/figures/response-slices/build/figure
```

## 参考分析图的完整编码

指定参考图不仅是一种外框。使用 `sensitivity_dynamics`、`reference:sensitivity-pair` 或 `reference:dynamics-pair` 时，保留实际提供的分析元素：

| 参考元素 | 保留的含义与输入 |
| --- | --- |
| 对数距离密度与计数色条 | 实际轴变换、log-count归一化、计数范围和单位。 |
| 双阈值走廊 | 两个边界及交集；状态份额用完整人群分母，加权份额只由实际权重计算。 |
| median–P90箱、P99须、P95菱形 | 明确的分位数，不换成普通IQR箱、1.5-IQR须或均值；使用原始样本或完整给定分位数。 |
| 独立采样步的多条曲线 | 各系列保留自身横坐标，不补不存在的起始观测。 |
| 轮廓柱与同单位曲线 | 保留类别身份、百分比定义和色形；范围仅来自给定上下界，稀疏标注不重复全部数值。 |

实现支持 `density.corridor={x_max,y_max,weights?,label?,annotation_xy?}`、密度轴与计数色条参数；敏感度块支持 `summary={median,p90,p95,p99}` 或 `summary_mode="median_p90"` 和实际样本。动态系列保留自身 `x`；类别块支持 `bar_style="outlined"`、`bar_labels`、`label_wrap`、给定区间及选定标注。标签换行只改显示，不改实体顺序。具体参数只读当前所用模板，不加载所有卡。

这两组用户参考示例和原始案例继续保留。使用冻结的模拟输入看版式，真实任务替换完整数据；缺少权重、区间或采样点时不伪造，按所需科学范围解决输入。

## 原示例继续保留

[完整示例表](figure-examples.md)列出原九套模板、指定参考双面板、论文设计卡与融合布局。旧例是后续改进的起点，新增功能不会将它们从表中挤掉：

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py examples --category original
python ccf-visual-composer/resources/python/ccfa_figure_library.py examples --category reference
python ccf-visual-composer/resources/python/ccfa_figure_library.py example original:sensitivity_dynamics --demo --out ccfa-workfiles/figures/reference-full/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:sensitivity-pair --demo --out ccfa-workfiles/figures/reference-sensitivity/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:dynamics-pair --demo --out ccfa-workfiles/figures/reference-dynamics/build/figure
```

## 按当前文章选择，随机探索与稳定修改

选图由当前文章决定。先看论点和段落要解决的问题，再核对观察单位、配对关系、顺序、实际区间与版面；只在同样合适的候选之间自然随机。不需要用户设置种子，不通过全局使用次数决定这篇文章该画什么。保存下来的实际数据与组合规范，就是后续修改和重画的依据。

如果同一项目有多张同类图，需要减少重复选择，可以显式使用项目自有历史。它只影响同等适合的候选，不是必需配置：

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py route "分布与长尾" --count 3 --history ccfa-workfiles/figures/selection-history.json
python ccf-visual-composer/resources/python/ccfa_figure_library.py record --history ccfa-workfiles/figures/selection-history.json raincloud ecdf
```

只在图法已被接受或实际采用后 `record`，不把浏览候选计作使用。接受后固定组合规范，局部修改直接编辑现有 Python 源；不因多轮对话、换一个 agent 或同一图再次渲染而重新随机。新的科学问题、数据结构或明确要求比较另一方案时，再走路由。

演示组合也保留已实现的共享数据关系：配对图使用同一组 before/after，分布与分位数图复用原始观察，共分箱组成使用同一 bin 边界，响应切片从同一响应矩阵抽取。具体共享关系记录在 `_meta.shared_simulation_contracts`；没有该关系的演示面板只用于看图法，不能写成彼此解释的实测分析。

## 融合时保留什么

优先使用 `fusions` 列出的组合关系，再按当前问题取舍面板。融合应增加一层解释，例如从总体到群体、从位置到分布、从响应面到剖面、从质量到成本。

- 同对象比较共享 ID 和顺序；同分箱图共享边界与成员；轨迹保留 checkpoint 顺序。不能分别随机生成各面板的数据后，把它们写成相互解释的实测分析。
- 统一实体颜色和含义，数值尺度只在指标、单位和变换相同时共享。不同单位相邻展示，不相加成一个总分。
- 区分观察、拟合、理论参考和外推；均值、IQR、种子范围与置信区间各自命名。
- 组成图保留分母；可选同时展示样本量。二维表面只有稀疏观测时先用矩阵，不借平滑插值制造确定边界。
- 原图缺少可复现的统计输入时，保留其设计关系并说明字段需求；真实任务等待数据所有者补齐，演示图继续标记模拟值。

## 目录覆盖与图例覆盖

2025、2026 年的官方会议目录和 NMI 出版登记用于发现候选；Nature 主刊与 Nature Methods 的 AI 论文另记精选范围。目录元数据的完整程度在素材库 `resources/figure-library/corpus.json` 中逐集合记录，不能等同于每篇论文的每幅图均已阅读或复现。

当前 78 卡是已检查、去重后可复用的设计起点。先从相关表达目的查少量卡，必要时查其 `source_id` 和原图；不在每次作图时重搜所有会议或全量加载素材库。后续扩展复用相同字段、来源登记和原语，给已有卡增加有用变体，而不为同一种图复制几十份近似 Python 文件。

## 输入数据与图类型分别检索

素材库保留两个独立分类：输入类型包括二维观测、分组/配对样本、有序序列、估计与区间、分位数摘要、分箱计数、类别多指标、矩阵、空间坐标和组成数据；图类型包括曲线、柱形、区间、分布、二维密度、散点、热图、组成和轨迹。同一复合图可以有多个图类型标签。

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py route category_comparison --input-type category_series --chart-type bar --fields labels bars series series.lower series.upper annotate
```

路由返回 `element_plan`，说明已有分析要素和哪些给定字段可增加范围、条件区域、加权份额或关键数值。`describe_plot`按实际内容识别数据类型，避免把汇总分位数当成原始样本。图库默认优先展示多元素分析，基础图法仍可作为拼装部件查看。复杂度标签是浏览提示，不是科研价值评分。
