# 图例与保留示例表

先按当前论文要说明的关系选例，再查看对应设计卡。所有示例都接同一个绘图入口；修改已有图稿继续编辑保存的Python与数据，不重新抽样。旧示例保留在此表，新增图例不会替换它们。

## 原有九套模板与用户参考图

| 示例ID | 内容 | 设计目的 |
| --- | --- | --- |
| `original:mechanism_overview` | 方法总览与支持分析 | 方法图与关键结果分工，读者从整体进入具体分析。 |
| `original:benchmark_atlas` | 基准、分布与资源图谱 | 总体比较之外保留样本差异和实际成本。 |
| `original:ablation_interactions` | 消融与模块交互 | 将单因素贡献与组合交互分开，避免用一个排名解释机制。 |
| `original:scaling_robustness` | 规模、预算与鲁棒性 | 同一方法跨规模与扰动条件保持身份。 |
| `original:representation_diagnostics` | 表征诊断 | 嵌入、矩阵和分布互补解释表征结构。 |
| `original:biological_atlas` | 生物数据分析图谱 | 群体、表达和效应分别呈现，同时保留群体颜色。 |
| `original:paired_effects` | 配对变化与群体效应 | 相同观察单位连接前后变化，再看群体差异。 |
| `original:calibration_errors` | 校准与错误结构 | 概率解释、分类错误和分布分工明确。 |
| `original:sensitivity_dynamics` | 密度、扰动与状态演化组合 | 保留用户参考图中的四个分析关系：密度、扰动、状态曲线、类别占比。 |
| `reference:sensitivity-pair` | 用户参考图：密度与径向扰动双面板 | 六边形密度展示状态分布，分箱箱线和上分位数解释敏感性差异。 |
| `reference:dynamics-pair` | 用户参考图：状态演化与类别占比双面板 | 整体状态随迭代变化与类别内部变化相邻展示，保留同一类别顺序和占比分母。 |

用户上传的组合参考图仍有三个入口：`original:sensitivity_dynamics`保留四面板全图；`reference:sensitivity-pair`和`reference:dynamics-pair`分别保留两组双面板。它们使用模拟数据展示相同分析关系，不声称恢复了截图背后的真实数值。

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py examples --category reference
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:sensitivity-pair --demo --out ccfa-workfiles/figures/sensitivity/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py example reference:dynamics-pair --demo --out ccfa-workfiles/figures/dynamics/build/figure
```

## 已有方法图与展示示例

下列既有成图继续保留在原位置；它们是图像或展示材料，不冒称数据分析Python复建。新增数据图库与它们并行使用。

| 保留示例 | 原有文件 | 用途 |
| --- | --- | --- |
| DynTrace论文方法架构图 | [现有PNG](../../assets/visual-showcase/dyntrace-paper-mechanism-llava4d-reference.png) | 分层呈现输入、几何表示、分支、融合和输出。 |
| LLaVA-4D参考图 | [现有参考图](../../assets/visual-showcase/references/llava-4d-figure-2-iclr-2026.png) | 保留出处和构图观察，供需要的方法图任务查看。 |

## 早期 SVG 与展示图（保留原文件）

这些示例仍可从原有 SVG 实现和素材目录继续编辑；它们不被新图库取代。

| 示例 | 原有文件 |
| --- | --- |
| 01 claim strength lollipop | [查看SVG](../../assets/visual-showcase/showcase-01-claim-strength-lollipop.svg) |
| 02 revision lift slopegraph | [查看SVG](../../assets/visual-showcase/showcase-02-revision-lift-slopegraph.svg) |
| 03 evidence coverage heatmap | [查看SVG](../../assets/visual-showcase/showcase-03-evidence-coverage-heatmap.svg) |
| 04 run stability ridgeline | [查看SVG](../../assets/visual-showcase/showcase-04-run-stability-ridgeline.svg) |
| 05 analysis small multiples | [查看SVG](../../assets/visual-showcase/showcase-05-analysis-small-multiples.svg) |
| 06 readiness radial scorecard | [查看SVG](../../assets/visual-showcase/showcase-06-readiness-radial-scorecard.svg) |
| 07 opportunity bubble map | [查看SVG](../../assets/visual-showcase/showcase-07-opportunity-bubble-map.svg) |
| 08 evidence dashboard table | [查看SVG](../../assets/visual-showcase/showcase-08-evidence-dashboard-table.svg) |
| 09 evidence composition donut | [查看SVG](../../assets/visual-showcase/showcase-09-evidence-composition-donut.svg) |
| 10 grouped benchmark bars | [查看SVG](../../assets/visual-showcase/showcase-10-grouped-benchmark-bars.svg) |
| 11 volcano candidate screen | [查看SVG](../../assets/visual-showcase/showcase-11-volcano-candidate-screen.svg) |
| 12 correlation analysis heatmap | [查看SVG](../../assets/visual-showcase/showcase-12-correlation-analysis-heatmap.svg) |
| 13 composite analysis dashboard | [查看SVG](../../assets/visual-showcase/showcase-13-composite-analysis-dashboard.svg) |
| GPT Image概念探索 | [查看PNG](../../assets/visual-showcase/dyntrace-method-architecture-gpt-image-2.png) |
| PPT/Poster参考驱动示例 | [查看PNG](../../assets/visual-showcase/dyntrace-ppt-poster-reference-driven.png) |

## 原生联动布局

| 示例ID | 内容 | 设计目的 |
| --- | --- | --- |
| `layout:joint_marginals` | 联合关系与两个边缘分布 | 二维关系与边缘计数来自同一批观测，在完全对应的坐标上读取。 |
| `layout:aligned_tracks` | 共同位置的多轨观测与预测 | 所有轨道共享位置范围与图形宽度，各自保留单位，定位误差发生在哪里。 |
| `layout:matrix_slices` | 响应矩阵与同源行列切片 | 主矩阵定位交互，选定行列标记与切片使用同一矩阵，不另造趋势。 |

## 论文图例

共78张设计卡，来自43篇论文。每条保留原图观察、设计理由、数据需求和当前适配范围；来源与原图号单独登记。

| 示例ID | 会议/期刊与年份 | 图号 | 关系 |
| --- | --- | --- | --- |
| `paper:vision-calimatch-reliability` | ICCV 2025 | Figure 2 | 跨数据集的置信度校准 |
| `paper:vision-calimatch-threshold` | ICCV 2025 | Figure 3 | 阈值提高时牺牲了什么 |
| `paper:vision-diversity-paired-intervals` | CVPR 2025 | Figure 1 | 类别差异与目标区间 |
| `paper:vision-diversity-saturation` | CVPR 2025 | Figure 4 | 样本增多后的覆盖上限 |
| `paper:vision-scaling-optimum-grid` | CVPR 2025 | Figure 4 | 预测最优点附近的实测地形 |
| `paper:vision-scaling-isoflop` | CVPR 2025 | Figure 6 | 固定计算量下的容量最优点 |
| `paper:vision-landscape-alignment` | CVPR 2025 | Figure 2 | 不同域的损失盆地是否对齐 |
| `paper:vision-pruning-paired-embeddings` | CVPR 2026 | Figure 3 | 表征修改前后的对应关系 |
| `paper:vision-poca-reward-conflict` | CVPR 2026 | Figure 2 | 样本奖励冲突与最终取舍 |
| `paper:vision-poca-preference-composition` | CVPR 2026 | Figure 8 | 人类偏好的组成 |
| `paper:vision-ecoalign-policy-profile` | CVPR 2026 | Figure 3 | 策略在不同任务上的轮廓 |
| `paper:vision-scendi-controlled-surface` | ICCV 2025 | Figure 3 | 分开两种多样性来源 |
| `paper:vision-scendi-context-conditioned-metrics` | ICCV 2025 | Figure 4 | 指标究竟响应哪种变化 |
| `paper:vision-qats-baseline-gain` | ECCV 2026 | Figure 2 | 改进发生在什么起点 |
| `paper:vision-weather-variable-horizon-heatmap` | ECCV 2026 | Fig. 2 | 误差改善发生在哪一层 |
| `paper:vision-weather-scaling-facets` | ECCV 2026 | Fig. 4 | 缩放关系在何种时效成立 |
| `paper:acl25-class-conditional-confidence-cdf` | ACL 2025 | Fig. 1 | 正确与错误回答的置信分布 |
| `paper:acl25-reliability-method-facets` | ACL 2025 | Fig. 3 | 校准改善集中在哪些置信区间 |
| `paper:acl26-turn-paired-reliability` | ACL 2026 | Fig. 2a | 被质疑前后的可靠性 |
| `paper:acl26-answer-state-transitions` | ACL 2026 | Fig. 2b | 信心变化背后的回答转移 |
| `paper:acl26-multi-turn-retention-facets` | ACL 2026 | Fig. 5 | 多轮对话中的准确率保持 |
| `paper:acl25-cross-domain-identity-scatter` | ACL 2025 | Fig. 1 | 跨语言迁移是否丢失能力 |
| `paper:acl25-ranked-agreement-intervals` | ACL 2025 | Fig. 2 | 跨语言一致性的排序与波动 |
| `paper:acl25-distribution-conditioned-composition` | ACL 2025 | Fig. 3 | 分数区间由哪些任务组成 |
| `paper:acl25-multifactor-cohort-comparison` | ACL 2025 | Fig. 5 | 资源、语系与文字的群体差异 |
| `paper:nmi26-parameter-surface-with-slices` | Nature Machine Intelligence 2026 | Fig. 1d | 参数交互与代表性切片 |
| `paper:nmi26-input-space-and-marginals` | Nature Machine Intelligence 2026 | Fig. 3b,e–j | 空间结构与置信分布 |
| `paper:nmi26-training-phase-trajectories` | Nature Machine Intelligence 2026 | Fig. 4a,d–f | 训练如何走到同一结果 |
| `paper:nmi26-ood-distribution-and-roc` | Nature Machine Intelligence 2026 | Fig. 5b,d | 未知输入的置信度与判别 |
| `paper:nmi25-hierarchical-region-ablation` | Nature Machine Intelligence 2025 | Fig. 3 | 信息删减在不同区域的影响 |
| `paper:nmi25-data-scale-versus-alignment` | Nature Machine Intelligence 2025 | Fig. 4e | 数据规模与表征对齐 |
| `paper:nmi25-group-diversity-forest-atlas` | Nature Machine Intelligence 2025 | Fig. 4 | 群体多样性与人类参考 |
| `paper:nmi25-hyperparameter-cohort-ladder` | Nature Machine Intelligence 2025 | Fig. 5 | 参数改变能否接近群体目标 |
| `paper:nmi26-capability-coordination-crossings` | Nature Machine Intelligence 2026 | Fig. 1 | 协作收益随模型能力变化 |
| `paper:nmi26-task-specific-distribution-atlas` | Nature Machine Intelligence 2026 | Fig. 2 | 平均收益背后的任务差异 |
| `paper:nmi26-agent-count-baseline-sweeps` | Nature Machine Intelligence 2026 | Fig. 3 | 增加智能体何时开始失效 |
| `paper:nmi26-optimal-setting-butterfly` | Nature Machine Intelligence 2026 | Fig. 3a | 两组最优设置的分布偏移 |
| `paper:nmi26-mirrored-spectrum-comparison` | Nature Machine Intelligence 2026 | Fig. 3b | 共同位置上的两组峰 |
| `paper:nm25-per-image-restoration-gains` | Nature Methods 2025 | Fig. 1d,f | 图像恢复究竟帮助了谁 |
| `paper:nm25-acquisition-budget-threshold-pair` | Nature Methods 2025 | Fig. 2c,e | 质量阈值与采集成本 |
| `paper:nature26-aligned-genomic-tracks` | Nature 2026 | Fig. 3b,c | 同一位置的预测与实测 |
| `paper:nature26-output-capability-matrix` | Nature 2026 | Fig. 3a,f | 输出覆盖与可比性能 |
| `paper:ml25-moe-isoflop-slices` | ICML 2025 | Figure 2 | 等计算预算下的最优剖面 |
| `paper:ml25-moe-budget-design` | ICML 2025 | Figures 3 and 4 | 计算预算与模型设计 |
| `paper:ml25-calibration-win-matrices` | ICML 2025 | Figure 3 | 校准与泛化的双胜率矩阵 |
| `paper:ml25-distillation-fixed-budget` | ICML 2025 | Figure 2 | 教师条件下的学生预算剖面 |
| `paper:ml25-pareto-preference-frontiers` | ICML 2025 | Figures 4 and 5 | 偏好变化与双任务前沿 |
| `paper:iclr25-calibration-generalization` | ICLR 2025 | Figure 2 | 可靠性之外的泛化解释 |
| `paper:iclr26-scaling-fit-observation` | ICLR 2026 | Figure 2 | 观测、拟合与外推分层 |
| `paper:iclr26-scaling-controlled-ablations` | ICLR 2026 | Figure 4 | 固定度量下的算法消融 |
| `paper:neurips25-overall-to-category` | NeurIPS 2025 | Figure 7 | 整体分布连接类别细分 |
| `paper:neurips25-category-distributions` | NeurIPS 2025 | Figure 8 | 类别分布与原始观测 |
| `paper:icml26-quality-walltime` | ICML 2026 | Figure 9 | 质量与实际等待时间 |
| `paper:iclr25-adak-activation-knee` | ICLR 2025 | Figure 2 | 节省计算的拐点在哪里 |
| `paper:iclr25-ado-extrapolation-domain` | ICLR 2025 | Figure 2 | 拟合范围如何改变外推 |
| `paper:iclr25-ado-learning-meta-loss` | ICLR 2025 | Figure 3 | 内层学习与外层优化是否都前进 |
| `paper:iclr25-ensemble-composition-tradeoffs` | ICLR 2025 | Figure 3 | 选了哪些模型、牺牲了哪些能力 |
| `paper:iclr26-atlas-language-scaling` | ICLR 2026 | Figure 1 | 不同语言的最优扩展路径 |
| `paper:iclr26-atlas-transfer-matrix` | ICLR 2026 | Figure 2 | 迁移收益是否有方向 |
| `paper:iclr26-atlas-reciprocity-groups` | ICLR 2026 | Figure 3 | 双向迁移是否对称 |
| `paper:iclr26-autoqd-best-policy-robustness` | ICLR 2026 | Figure 3 | 最优策略能承受多大环境变化 |
| `paper:iclr26-autoqd-adaptation-population` | ICLR 2026 | Figure 4 | 有多少策略仍然可用 |
| `paper:iclr26-agile-feature-task-dependence` | ICLR 2026 | Figure 3a | 同一表征指标在不同任务上作用相反 |
| `paper:icml25-routing-estimator-noise-surface` | ICML 2025 | Figure 2 | 何种估计误差下路由才有益 |
| `paper:icml25-bestroute-sampling-returns` | ICML 2025 | Figure 2 | 多采样的边际回报 |
| `paper:icml25-bestroute-cost-quality-envelope` | ICML 2025 | Figures 3 and 4 | 成本质量曲线与采样机制 |
| `paper:icml25-semantic-calibration-gap` | ICML 2025 | Figure 3 | 哪一段置信度被校准 |
| `paper:icml25-calibration-training-distribution` | ICML 2025 | Figure 5 | 训练过程与置信尖峰 |
| `paper:icml26-superposition-profile-agreement` | ICML 2026 | Figure 3d | 理论特征关系何时能预测输入攻击 |
| `paper:icml26-agentic-calibration-base-model` | ICML 2026 | Figure 2 | 校准器是否只适合一个基座模型 |
| `paper:icml26-agentic-transfer-geometry-reliability` | ICML 2026 | Figures 5 and 6 | 分布外位置与概率解释 |
| `paper:icml26-alpharouter-efficiency-facets` | ICML 2026 | Figure 3 | 同等激活预算的多任务收益 |
| `paper:icml26-merging-subsets-mean-variance` | ICML 2026 | Figure 3 | 平均收益背后的组合波动 |
| `paper:icml26-merging-order-stability` | ICML 2026 | Figure 8 | 顺序敏感性如何随规模收缩 |
| `paper:neurips26-calarena-binary-multiclass` | NeurIPS 2026 | Figure 1 | 二分类与多分类的校准排名 |
| `paper:neurips26-calarena-class-count-boundary` | NeurIPS 2026 | Figure 2 | 平均胜率取决于评测集有多少类别 |
| `paper:neurips25-research-validation-test-trajectories` | NeurIPS 2025 | Figure 4 | 搜索继续进步还是只在代理指标上进步 |
| `paper:neurips25-research-selection-gap` | NeurIPS 2025 | Figure 6 | 搜索误差与最终选择误差分别占多少 |

## 组合示例

| 示例ID | 设计目的 | 组合思路 |
| --- | --- | --- |
| `fusion:distribution_tails` | 整体分布、阈值与尾部 | 先看分布形状，再读阈值比例，最后比较上尾。 |
| `fusion:paired_benefit` | 改变了谁、改变多少 | 从个体前后值，推进到基线依赖，再检查差值偏差。 |
| `fusion:calibration_decision` | 可靠性与实际决策 | 把置信度是否可靠与拒答、检索的实际代价联系起来。 |
| `fusion:rank_robustness` | 名次与真实性能变化 | 分数、名次和扰动曲线相互补充，防止只按排名夸大差异。 |
| `fusion:scaling_optimum` | 响应面与资源最优 | 先定位二维地形，再检查切片，最后落到实际资源取舍。 |
| `fusion:multiobjective_conflict` | 双目标冲突与多维能力 | 参考线划分改变方向，前沿呈现取舍，多维轴检查被平均掩盖的能力。 |
| `fusion:composition_flow` | 组分、去向与平衡 | 群体组成、状态去向和三部分混合分别回答规模、变化与平衡。 |
| `fusion:representation_atlas` | 表征与特征覆盖 | 用空间结构定位群体，再看局部关系，最后核对特征强度和覆盖。 |
| `fusion:effect_screening` | 筛选与原始差异 | 从全量候选筛选到效应区间，再返回实际样本分布。 |
| `fusion:training_stability` | 训练稳定、范围与泛化 | 训练运行轨迹、条件分位数和扰动结果组成不同层面的稳定性分析。 |
| `fusion:response_slices` | 二维响应与行列切片 | 中心响应面给全局结构，两条切片解释具体控制变量的影响。 |
| `fusion:common_bins` | 共分箱分布与群体组成 | 总体计数、区间内组成与累积比例表达分布差异来自哪里。 |
| `fusion:heterogeneity` | 平均值背后的群体差异 | 区间、样本和多个指标检查结果是否只由少数组别推动。 |
| `fusion:mechanism_change` | 机制交互与变化方向 | 从控制变量作用到目标冲突，再追踪基线依赖的改变。 |
| `fusion:error_diagnosis` | 错误结构与可用范围 | 先定位误差结构，再检查概率解释，最后衡量拒答后的保留风险。 |
| `fusion:spectral_comparison` | 峰位与整体分布 | 用共同位置的峰比较局部结构，再检查幅值分布和累计比例。 |

## 查找、复建与真实数据

```bash
python ccf-visual-composer/resources/python/ccfa_figure_library.py examples --category paper --limit 5
python ccf-visual-composer/resources/python/ccfa_figure_library.py studies --id nmi26-input-space-and-marginals
python ccf-visual-composer/resources/python/ccfa_figure_library.py example layout:matrix_slices --demo --out ccfa-workfiles/figures/response/build/figure
python ccf-visual-composer/resources/python/ccfa_figure_library.py compose --spec path/to/figure-spec.json --out ccfa-workfiles/figures/analysis/build/figure
```

`--demo`才生成明确标记的模拟数据。真实表格的列绑定、配对和网格规则见[设计与融合指南](figure-design-library.md)，数值图输出保留可编辑Python、SVG和预览图。当前论文正文、已有数据与最终版面决定图的选择；随机仅用于同样合适的候选，不需要设置种子。
