/* CCFA local preferences. No external requests, dependencies, or browser-storage claims. */
"use strict";

const KEYS = ["independent_review", "extended_search", "enhanced_document_parsing", "figure_variants", "detailed_reports", "alternative_routes", "maintenance_evolution"];
const MODES = ["off", "auto", "on"];
const LANGUAGES = ["zh-CN", "zh-TW", "en"];
const THEMES = ["system", "light", "dark"];
const DEFAULTS = { version: 1, preferences: { independent_review: "off", extended_search: "auto", enhanced_document_parsing: "auto", figure_variants: "off", detailed_reports: "off", alternative_routes: "off", maintenance_evolution: "off" }, ui: { language: "zh-CN", theme: "system" } };
const PRESETS = { lean: ["off", "off", "off", "off", "off", "off", "off"], balanced: ["off", "auto", "auto", "off", "off", "off", "off"], deep: ["on", "on", "auto", "on", "on", "auto", "auto"] };

const COPY = {
  "zh-CN": {
    title: "CCFA-Skills · 研究偏好", skip: "跳至偏好设置", brandSub: "研究偏好", local: "本地配置", language: "界面语言", theme: "界面主题", themeSystem: "◐ 跟随系统", themeLight: "☀ 日光", themeDark: "☾ 夜航",
    eyebrow: "为你的研究，调好节奏", heroLine1: "把算力，", heroLine2: "用在值得的地方。", heroDesc: "保持日常轻盈，让关键问题得到更多关注。你决定额外投入，CCFA-Skills 记住你的选择。", heroFoot: "同一套研究标准，不同的投入节奏。", artCaption: "深度，由你掌握", sectionKicker: "YOUR RESEARCH, YOUR RHYTHM", workspaceTitle: "设定你的研究节奏",
    scopeLabel: "配置范围", scopeUser: "个人默认", scopeProject: "当前项目", scopeUserDesc: "个人默认供后续任务复用；项目中的显式设置可以覆盖它。只在点击保存后写入配置文件。", scopeProjectDesc: "仅对启动配置器时选定的项目生效。未显式设置的选项继承个人默认。", scopeProjectStatic: "项目配置草稿：未设置的选项将在应用时继承个人默认。静态预览无法读取你的个人配置，当前按内置值展示。", scopeUnavailable: "启动时指定项目目录后，才可编辑项目设置。",
    presetTitle: "从一种节奏开始", presetLean: "轻盈", presetBalanced: "均衡", presetDeep: "深入", recommended: "推荐", presetNote: "仅更新草稿", presetsLabel: "预设方案", presetApplied: "已将「{name}」应用到草稿，保存后生效。", enhancementTitle: "可选增强", legend: "☾ 关闭 · ☀ 开启 · 按需触发", modeOff: "关闭", modeAuto: "按需", modeOn: "开启", inherit: "恢复继承", inherited: "继承中", sourceDefault: "内置默认", sourceUser: "个人默认", sourceProject: "项目设置", explicit: "此处设置", inheritedFrom: "继承：{source}", switchLabel: "{name}：额外增强开关，当前{mode}", autoLabel: "{name}：按需触发", trigger: "触发条件", whenUsed: "触发后",
    baselineTitle: "研究底线，始终在线", baselineDesc: "humanization → common 前置、必要核验、证据约束和交付检查始终执行。这些开关只控制额外投入。",
    advancedTitle: "配置文件与继承", inheritDesc: "仅保存你明确设置的字段。恢复继承后，项目跟随个人默认，个人默认跟随内置设置。", inheritUi: "语言与主题恢复继承", inheritAll: "全部恢复继承", import: "导入 JSON", export: "导出 JSON", reload: "重新读取磁盘", previewLabel: "待保存的配置 JSON", inheritedToast: "已在草稿中恢复继承，保存后生效。", importToast: "配置已导入草稿，尚未应用到 skills。", exportToast: "已导出 JSON；导出不等于应用到 skills。", reloadConfirm: "此范围还有未保存的修改。重新读取磁盘会丢弃这些草稿修改，是否继续？", reloaded: "已重新读取磁盘配置。",
    summaryKicker: "投入概览", summaryTitle: "让每次深入\n都有理由。", onCountLabel: "项增强已开启", autoCount: "另有 {count} 项按需触发", summaryQuiet: "额外增强均已关闭。必要的研究步骤与质量检查仍然执行。", summaryAuto: "优先复用现有材料。按需项在确有价值时触发，产生额外调用与等待。", summaryOn: "已开启的增强在相关任务中执行，增加模型或工具投入；按需项由实际缺口决定。", tokenTitle: "Token", tokenDesc: "更多检索内容、独立检查或图稿生成，会增加模型与工具投入。", timeTitle: "时间", timeDesc: "额外调用与解析需要等待；实际变化取决于材料、任务和可用工具。", estimateNote: "这里显示投入方向，不估算 token 数量或固定耗时。", priorityNote: "当前明确指令优先，其次是项目设置、个人默认和内置设置。", footer: "把精力留给好问题。", footerLocal: "配置保存在本地 · 无外部请求",
    onlineNotice: "本地连接已建立。保存写入所选范围的真实配置；切换范围会保留各自草稿。", staticNotice: "静态预览模式：可编辑、导入和导出，但尚未应用到 skills。请用本地配置服务保存，或将 JSON 放入约定的配置路径。", loading: "正在读取本地配置…", clean: "与已读取配置一致", dirty: "有未保存的修改", saved: "偏好已保存", saving: "正在保存…", staticState: "静态草稿 · 尚未应用", exported: "已导出 · 尚未应用", savedDetail: "后续任务读取所选范围的配置；当前明确指令仍优先。", cleanDetail: "仅明确设置的字段会保存，继承关系保持不变。", dirtyDetail: "草稿不会自动保存。切换范围保留修改；关闭页面会丢失。", staticDetail: "浏览器内的草稿不会改变 skills 的实际配置。", save: "保存偏好", saveStatic: "导出配置", saveToast: "偏好已写入本地配置文件。", savingDetail: "正在写入所选范围，请稍候。", dismiss: "关闭提示", connectionError: "无法连接本地配置服务。请确认服务仍在运行，再重新读取。", errorGeneric: "操作未完成。请检查本地服务或配置文件后重试。", errorAuth: "本地访问凭据无效或已过期。请使用服务新提供的完整地址重新打开。", errorConflict: "配置已被其他操作修改。草稿已保留；请先导出备份，再重新读取磁盘并合并修改。", errorInvalid: "配置不符合约定格式，未保存。请检查版本号、字段和值。", errorStored: "磁盘上的配置无法读取或格式无效。为避免覆盖，未保存；请先修复该文件。", errorScope: "此配置范围不可用。项目设置需要启动时指定项目目录。", errorWrite: "无法写入配置文件。请检查目录权限与磁盘状态。", errorFile: "无法读取这个文件，请选择 UTF-8 编码的 JSON 文件。", errorSize: "文件过大。配置文件不能超过 64 KiB。", errorJson: "JSON 格式无效，请检查引号、逗号和括号。", errorRoot: "配置必须是一个 JSON 对象，且 version 必须为 1。", errorField: "不支持的配置字段：{field}", errorValue: "配置值无效：{field}", errorObject: "{field} 必须是 JSON 对象。", errorServer: "本地服务返回了无法识别的数据。请重启同一版本的配置服务。", fileHelpOnline: "导入先更新草稿，点击保存才生效。导出只包含可移植设置，不包含本地路径或访问凭据。", fileHelpStatic: "个人配置：$CODEX_HOME/ccfa/preferences.json（未设 CODEX_HOME 时为 ~/.codex/ccfa/preferences.json）；项目配置：<项目目录>/.ccfa/preferences.json。静态预览中的项目继承值仅为内置默认。",
    errorDuplicate: "JSON 中存在重复字段：{field}。请删除重复项后再导入。", loadFailed: "尚未读取本地配置", retryDetail: "草稿不会覆盖磁盘。请检查服务或文件，再点击「重新读取磁盘」。", missingState: "使用内置或继承设置 · 尚未保存", missingDetail: "点击保存即可记录当前选择，不会固化继承值。", importing: "正在读取导入文件…", importDetail: "导入只更新当前范围的草稿，请稍候。", conflictState: "磁盘配置已变化 · 草稿已保留", conflictDetail: "请先导出草稿，再重新读取并合并修改。",
    exportNameNote: "手动应用导出文件时，请将它重命名为 preferences.json，再放到所选范围对应的配置目录。",
    errorStorage: "配置存储操作未完成。文件可能正被另一进程锁定，或目录、磁盘不可用。草稿已保留；请等待其他写入完成并检查权限后重试。",
    features: {
      independent_review: { title: "独立第二轮复核", desc: "在主流程审核后，增加一次独立检查，寻找遗漏或不成立的判断。", trigger: "相关审核任务；按需时仅在关键结论存在争议或影响较大时启用。", token: "Token 明显增加", time: "时间明显增加" },
      extended_search: { title: "额外广泛检索", desc: "围绕明确的证据缺口扩展文献与来源范围，复用已核验材料。", trigger: "相关检索任务；按需时在现有证据不足以支持判断时扩展。", token: "Token 随检索范围增加", time: "时间随检索范围增加" },
      enhanced_document_parsing: { title: "复杂文档增强解析", desc: "对难以可靠读取的表格、公式或页面，使用可用的视觉或结构化解析。", trigger: "相关文档任务；按需时仅处理解析存疑且影响结论的页面。", token: "Token 随页数与工具变化", time: "增加解析等待" },
      figure_variants: { title: "额外图稿候选", desc: "为同一图提供额外布局或视觉方案，便于比较并确定方向。", trigger: "相关绘图任务；按需时仅在设计选择会显著影响表达时生成。", token: "增加图像或模型用量", time: "明显增加生成时间" },
      detailed_reports: { title: "附加过程报告", desc: "保留便于追溯的决策、依据与检查记录，整合到既有工作目录。", trigger: "相关交付任务；按需时在需要复现或交接追踪时补充。", token: "增加输出 token", time: "增加整理与核对时间" },
      alternative_routes: { title: "备选路线对照", desc: "在已选路线之外，最多追加一条可选路线对照，优先复用证据。你明确要求的发散和必要纠错照常完成。", trigger: "适用于会影响结果的额外路线比较。关闭不限制你要求的多个方向；额外实验或服务仍按已有授权执行。", token: "增加一次路线分析与证据核对", time: "增加对照时间，取决于证据缺口" },
      maintenance_evolution: { title: "维护期规则迭代", desc: "在 skill 维护中，最多增加一版候选规则和一次固定用例比较。评价口径保持不变，未通过就保留稳定版。", trigger: "仅适用于明确请求的 skill 维护；按需时须有尚未解决的规则问题。自主科研由具体任务及其预算启动，不由此开关启动。", token: "增加候选修正与用例比较投入", time: "增加一次维护评估时间" }
    }
  },
  "zh-TW": {
    title: "CCFA-Skills · 研究偏好", skip: "跳至偏好設定", brandSub: "研究偏好", local: "本機設定", language: "介面語言", theme: "介面主題", themeSystem: "◐ 跟隨系統", themeLight: "☀ 日光", themeDark: "☾ 夜航",
    eyebrow: "為你的研究，調好節奏", heroLine1: "把算力，", heroLine2: "用在值得的地方。", heroDesc: "保持日常輕盈，讓關鍵問題得到更多關注。你決定額外投入，CCFA-Skills 記住你的選擇。", heroFoot: "同一套研究標準，不同的投入節奏。", artCaption: "深度，由你掌握", sectionKicker: "YOUR RESEARCH, YOUR RHYTHM", workspaceTitle: "設定你的研究節奏",
    scopeLabel: "設定範圍", scopeUser: "個人預設", scopeProject: "目前專案", scopeUserDesc: "個人預設供後續任務沿用；專案中的明確設定可以覆寫它。只在點擊儲存後寫入設定檔。", scopeProjectDesc: "僅對啟動設定工具時選定的專案生效。未明確設定的選項繼承個人預設。", scopeProjectStatic: "專案設定草稿：未設定的選項將在套用時繼承個人預設。靜態預覽無法讀取你的個人設定，目前按內建值顯示。", scopeUnavailable: "啟動時指定專案目錄後，才可編輯專案設定。",
    presetTitle: "從一種節奏開始", presetLean: "輕盈", presetBalanced: "均衡", presetDeep: "深入", recommended: "推薦", presetNote: "僅更新草稿", presetsLabel: "預設方案", presetApplied: "已將「{name}」套用至草稿，儲存後生效。", enhancementTitle: "可選增強", legend: "☾ 關閉 · ☀ 開啟 · 按需觸發", modeOff: "關閉", modeAuto: "按需", modeOn: "開啟", inherit: "恢復繼承", inherited: "繼承中", sourceDefault: "內建預設", sourceUser: "個人預設", sourceProject: "專案設定", explicit: "此處設定", inheritedFrom: "繼承：{source}", switchLabel: "{name}：額外增強開關，目前{mode}", autoLabel: "{name}：按需觸發", trigger: "觸發條件", whenUsed: "觸發後",
    baselineTitle: "研究底線，始終在線", baselineDesc: "humanization → common 前置、必要核驗、證據約束和交付檢查始終執行。這些開關只控制額外投入。",
    advancedTitle: "設定檔與繼承", inheritDesc: "僅儲存你明確設定的欄位。恢復繼承後，專案跟隨個人預設，個人預設跟隨內建設定。", inheritUi: "語言與主題恢復繼承", inheritAll: "全部恢復繼承", import: "匯入 JSON", export: "匯出 JSON", reload: "重新讀取磁碟", previewLabel: "待儲存的設定 JSON", inheritedToast: "已在草稿中恢復繼承，儲存後生效。", importToast: "設定已匯入草稿，尚未套用至 skills。", exportToast: "已匯出 JSON；匯出不等於套用至 skills。", reloadConfirm: "此範圍還有未儲存的修改。重新讀取磁碟會捨棄這些草稿修改，是否繼續？", reloaded: "已重新讀取磁碟設定。",
    summaryKicker: "投入概覽", summaryTitle: "讓每次深入\n都有理由。", onCountLabel: "項增強已開啟", autoCount: "另有 {count} 項按需觸發", summaryQuiet: "額外增強均已關閉。必要的研究步驟與品質檢查仍然執行。", summaryAuto: "優先沿用現有材料。按需項在確有價值時觸發，產生額外呼叫與等待。", summaryOn: "已開啟的增強在相關任務中執行，增加模型或工具投入；按需項由實際缺口決定。", tokenTitle: "Token", tokenDesc: "更多檢索內容、獨立檢查或圖稿生成，會增加模型與工具投入。", timeTitle: "時間", timeDesc: "額外呼叫與解析需要等待；實際變化取決於材料、任務和可用工具。", estimateNote: "這裡顯示投入方向，不估算 token 數量或固定耗時。", priorityNote: "目前明確指令優先，其次是專案設定、個人預設和內建設定。", footer: "把精力留給好問題。", footerLocal: "設定儲存在本機 · 無外部請求",
    onlineNotice: "本機連線已建立。儲存會寫入所選範圍的實際設定；切換範圍會保留各自草稿。", staticNotice: "靜態預覽模式：可編輯、匯入和匯出，但尚未套用至 skills。請用本機設定服務儲存，或將 JSON 放入約定的設定路徑。", loading: "正在讀取本機設定…", clean: "與已讀取設定一致", dirty: "有未儲存的修改", saved: "偏好已儲存", saving: "正在儲存…", staticState: "靜態草稿 · 尚未套用", exported: "已匯出 · 尚未套用", savedDetail: "後續任務讀取所選範圍的設定；目前明確指令仍優先。", cleanDetail: "僅明確設定的欄位會儲存，繼承關係保持不變。", dirtyDetail: "草稿不會自動儲存。切換範圍保留修改；關閉頁面會遺失。", staticDetail: "瀏覽器內的草稿不會改變 skills 的實際設定。", save: "儲存偏好", saveStatic: "匯出設定", saveToast: "偏好已寫入本機設定檔。", savingDetail: "正在寫入所選範圍，請稍候。", dismiss: "關閉提示", connectionError: "無法連線至本機設定服務。請確認服務仍在執行，再重新讀取。", errorGeneric: "操作未完成。請檢查本機服務或設定檔後重試。", errorAuth: "本機存取憑證無效或已過期。請使用服務新提供的完整位址重新開啟。", errorConflict: "設定已被其他操作修改。草稿已保留；請先匯出備份，再重新讀取磁碟並合併修改。", errorInvalid: "設定不符合約定格式，未儲存。請檢查版本號、欄位和值。", errorStored: "磁碟上的設定無法讀取或格式無效。為避免覆寫，未儲存；請先修復該檔案。", errorScope: "此設定範圍不可用。專案設定需要啟動時指定專案目錄。", errorWrite: "無法寫入設定檔。請檢查目錄權限與磁碟狀態。", errorFile: "無法讀取這個檔案，請選擇 UTF-8 編碼的 JSON 檔案。", errorSize: "檔案過大。設定檔不能超過 64 KiB。", errorJson: "JSON 格式無效，請檢查引號、逗號和括號。", errorRoot: "設定必須是一個 JSON 物件，且 version 必須為 1。", errorField: "不支援的設定欄位：{field}", errorValue: "設定值無效：{field}", errorObject: "{field} 必須是 JSON 物件。", errorServer: "本機服務傳回了無法辨識的資料。請重新啟動同一版本的設定服務。", fileHelpOnline: "匯入先更新草稿，點擊儲存才生效。匯出只包含可攜設定，不包含本機路徑或存取憑證。", fileHelpStatic: "個人設定：$CODEX_HOME/ccfa/preferences.json（未設 CODEX_HOME 時為 ~/.codex/ccfa/preferences.json）；專案設定：<專案目錄>/.ccfa/preferences.json。靜態預覽中的專案繼承值僅為內建預設。",
    errorDuplicate: "JSON 中存在重複欄位：{field}。請刪除重複項後再匯入。", loadFailed: "尚未讀取本機設定", retryDetail: "草稿不會覆寫磁碟。請檢查服務或檔案，再點擊「重新讀取磁碟」。", missingState: "使用內建或繼承設定 · 尚未儲存", missingDetail: "點擊儲存即可記錄目前選擇，不會固定繼承值。", importing: "正在讀取匯入檔案…", importDetail: "匯入只更新目前範圍的草稿，請稍候。", conflictState: "磁碟設定已變更 · 草稿已保留", conflictDetail: "請先匯出草稿，再重新讀取並合併修改。",
    exportNameNote: "手動套用匯出檔案時，請將它重新命名為 preferences.json，再放到所選範圍對應的設定目錄。",
    errorStorage: "設定儲存操作未完成。檔案可能正被另一個程序鎖定，或目錄、磁碟無法使用。草稿已保留；請等待其他寫入完成並檢查權限後重試。",
    features: {
      independent_review: { title: "獨立第二輪複核", desc: "在主流程審核後，增加一次獨立檢查，尋找遺漏或不成立的判斷。", trigger: "相關審核任務；按需時僅在關鍵結論存在爭議或影響較大時啟用。", token: "Token 明顯增加", time: "時間明顯增加" },
      extended_search: { title: "額外廣泛檢索", desc: "圍繞明確的證據缺口擴展文獻與來源範圍，沿用已核驗材料。", trigger: "相關檢索任務；按需時在現有證據不足以支持判斷時擴展。", token: "Token 隨檢索範圍增加", time: "時間隨檢索範圍增加" },
      enhanced_document_parsing: { title: "複雜文件增強解析", desc: "對難以可靠讀取的表格、公式或頁面，使用可用的視覺或結構化解析。", trigger: "相關文件任務；按需時僅處理解析存疑且影響結論的頁面。", token: "Token 隨頁數與工具變化", time: "增加解析等待" },
      figure_variants: { title: "額外圖稿候選", desc: "為同一張圖提供額外版面或視覺方案，便於比較並確定方向。", trigger: "相關繪圖任務；按需時僅在設計選擇會顯著影響表達時生成。", token: "增加圖像或模型用量", time: "明顯增加生成時間" },
      detailed_reports: { title: "附加過程報告", desc: "保留便於追溯的決策、依據與檢查紀錄，整合到既有工作目錄。", trigger: "相關交付任務；按需時在需要重現或交接追蹤時補充。", token: "增加輸出 token", time: "增加整理與核對時間" },
      alternative_routes: { title: "備選路線對照", desc: "在已選路線之外，最多追加一條可選路線對照，優先沿用證據。你明確要求的發散與必要糾錯照常完成。", trigger: "適用於會影響結果的額外路線比較。關閉不限制你要求的多個方向；額外實驗或服務仍按既有授權執行。", token: "增加一次路線分析與證據核對", time: "增加對照時間，取決於證據缺口" },
      maintenance_evolution: { title: "維護期規則迭代", desc: "在 skill 維護中，最多增加一版候選規則和一次固定用例比較。評價口徑保持不變，未通過就保留穩定版。", trigger: "僅適用於明確請求的 skill 維護；按需時須有尚未解決的規則問題。自主科研由具體任務及其預算啟動，不由此開關啟動。", token: "增加候選修正與用例比較投入", time: "增加一次維護評估時間" }
    }
  },
  en: {
    title: "CCFA-Skills · Research preferences", skip: "Skip to preferences", brandSub: "RESEARCH PREFERENCES", local: "LOCAL", language: "Interface language", theme: "Interface theme", themeSystem: "◐ System", themeLight: "☀ Daylight", themeDark: "☾ Nightfall",
    eyebrow: "FIND YOUR RESEARCH RHYTHM", heroLine1: "Spend your compute", heroLine2: "where it matters.", heroDesc: "Keep everyday work light. Give consequential questions more attention. You choose the extra effort; CCFA-Skills remembers your preferences.", heroFoot: "The same research standards. A rhythm of your own.", artCaption: "DEPTH, ON YOUR TERMS", sectionKicker: "YOUR RESEARCH, YOUR RHYTHM", workspaceTitle: "Set your research rhythm",
    scopeLabel: "Configuration scope", scopeUser: "Personal defaults", scopeProject: "This project", scopeUserDesc: "Personal defaults carry into future tasks. Explicit project settings can override them. Changes reach the configuration file only when you save.", scopeProjectDesc: "Applies only to the project selected when starting this configurator. Unset options inherit your personal defaults.", scopeProjectStatic: "Project draft: unset options will inherit personal defaults when applied. This static preview cannot read your personal configuration, so it displays built-in values.", scopeUnavailable: "Start the configurator with a project directory to edit project settings.",
    presetTitle: "Start with a rhythm", presetLean: "Light", presetBalanced: "Balanced", presetDeep: "Deep", recommended: "Suggested", presetNote: "Updates draft only", presetsLabel: "Preference presets", presetApplied: "Applied “{name}” to your draft. Save to activate it.", enhancementTitle: "OPTIONAL ENHANCEMENTS", legend: "☾ Off · ☀ On · Auto when needed", modeOff: "Off", modeAuto: "Auto", modeOn: "On", inherit: "Restore inheritance", inherited: "Inherited", sourceDefault: "built-in defaults", sourceUser: "personal defaults", sourceProject: "project settings", explicit: "Set here", inheritedFrom: "Inherited from {source}", switchLabel: "{name}: extra enhancement, currently {mode}", autoLabel: "{name}: enable when needed", trigger: "When", whenUsed: "When triggered",
    baselineTitle: "Research standards stay on", baselineDesc: "The humanization → common preflight, necessary verification, evidence rules, and delivery checks always apply. These switches control additional effort only.",
    advancedTitle: "Configuration file & inheritance", inheritDesc: "Only explicitly set fields are saved. Restoring inheritance makes projects follow personal defaults, and personal defaults follow built-in settings.", inheritUi: "Inherit language & theme", inheritAll: "Restore all inheritance", import: "Import JSON", export: "Export JSON", reload: "Reload from disk", previewLabel: "Configuration JSON to save", inheritedToast: "Inheritance restored in the draft. Save to apply it.", importToast: "Configuration imported into your draft. It has not been applied to skills.", exportToast: "JSON exported. Exporting does not apply it to skills.", reloadConfirm: "This scope has unsaved changes. Reloading from disk will discard this draft. Continue?", reloaded: "Configuration reloaded from disk.",
    summaryKicker: "EFFORT AT A GLANCE", summaryTitle: "Make every deep dive\nintentional.", onCountLabel: "enhancements on", autoCount: "{count} more set to auto", summaryQuiet: "All optional enhancements are off. Necessary research steps and quality checks still run.", summaryAuto: "Reuse existing material first. Auto options add calls and waiting only when the task benefits from them.", summaryOn: "Enabled enhancements run in relevant tasks and add model or tool usage. Auto options depend on the actual evidence gaps.", tokenTitle: "Tokens", tokenDesc: "More retrieved material, independent checks, or figure generation adds model and tool usage.", timeTitle: "Time", timeDesc: "Extra calls and parsing add waiting. The actual change depends on your material, task, and available tools.", estimateNote: "These are qualitative directions, not token estimates or fixed completion times.", priorityNote: "Your current explicit instruction comes first, then project settings, personal defaults, and built-in defaults.", footer: "Save your energy for good questions.", footerLocal: "Stored locally · No external requests",
    onlineNotice: "Connected locally. Saving writes the selected configuration file. Switching scope keeps each draft intact.", staticNotice: "Static preview: edit, import, and export only. Nothing has been applied to skills. Save through the local configuration service, or place the JSON at the documented configuration path.", loading: "Reading local configuration…", clean: "Matches the loaded configuration", dirty: "Unsaved changes", saved: "Preferences saved", saving: "Saving…", staticState: "Static draft · Not applied", exported: "Exported · Not applied", savedDetail: "Future tasks read this scope's configuration. Explicit task instructions still take precedence.", cleanDetail: "Only explicit fields are saved. Inheritance stays intact.", dirtyDetail: "Drafts do not autosave. Scope changes keep them; closing the page loses them.", staticDetail: "An in-browser draft does not change the actual skills configuration.", save: "Save preferences", saveStatic: "Export configuration", saveToast: "Preferences written to your local configuration file.", savingDetail: "Writing the selected scope. Please wait.", dismiss: "Dismiss message", connectionError: "Cannot reach the local configuration service. Check that it is running, then reload.", errorGeneric: "The operation did not complete. Check the local service or configuration file and try again.", errorAuth: "The local access credential is invalid or expired. Reopen the complete URL provided by the running service.", errorConflict: "Another operation changed the configuration. Your draft is intact. Export a backup, then reload from disk and merge your changes.", errorInvalid: "The configuration does not match the expected format and was not saved. Check its version, fields, and values.", errorStored: "The on-disk configuration is unreadable or invalid. It has not been overwritten. Repair the file before saving.", errorScope: "This scope is unavailable. Start the service with a project directory to edit project settings.", errorWrite: "The configuration file could not be written. Check directory permissions and disk availability.", errorFile: "Could not read this file. Select a UTF-8 JSON file.", errorSize: "This file is too large. Configuration files must not exceed 64 KiB.", errorJson: "Invalid JSON. Check quotation marks, commas, and brackets.", errorDuplicate: "Duplicate JSON field: {field}. Remove the duplicate before importing.", errorRoot: "Configuration must be a JSON object with version set to 1.", errorField: "Unsupported configuration field: {field}", errorValue: "Invalid configuration value: {field}", errorObject: "{field} must be a JSON object.", errorServer: "The local service returned unexpected data. Restart the matching version of the configuration service.", fileHelpOnline: "Import updates the draft; save to apply it. Export includes portable settings only, with no local paths or access credentials.", fileHelpStatic: "Personal: $CODEX_HOME/ccfa/preferences.json (or ~/.codex/ccfa/preferences.json if CODEX_HOME is unset). Project: <project>/.ccfa/preferences.json. Project inheritance in this static preview shows built-in defaults only.",
    loadFailed: "Local configuration not loaded", retryDetail: "Your draft will not overwrite the disk. Check the service or file, then choose Reload from disk.", missingState: "Using defaults or inherited settings · Not saved", missingDetail: "Save to record this choice without making inherited values explicit.", importing: "Reading the import file…", importDetail: "Import updates the current scope's draft only. Please wait.", conflictState: "Disk configuration changed · Draft preserved", conflictDetail: "Export your draft, then reload and merge your changes.",
    exportNameNote: "To apply an export manually, rename it to preferences.json and place it in the configuration directory for the selected scope.",
    errorStorage: "The configuration storage operation did not complete. Another process may hold the file lock, or the directory or disk may be unavailable. Your draft is intact. Wait for other writes to finish, check permissions, then retry.",
    features: {
      independent_review: { title: "Independent second review", desc: "Add a separate check after the main review to catch omissions and unsupported judgments.", trigger: "Relevant review tasks. Auto activates for disputed or consequential conclusions.", token: "Noticeably more tokens", time: "Noticeably more time" },
      extended_search: { title: "Broader supplementary search", desc: "Expand literature and source coverage around an identified evidence gap; reuse verified material.", trigger: "Relevant search tasks. Auto expands only when existing evidence cannot support the judgment.", token: "Tokens grow with search scope", time: "Time grows with search scope" },
      enhanced_document_parsing: { title: "Enhanced document parsing", desc: "Use available visual or structured parsing for tables, equations, and pages that are hard to read reliably.", trigger: "Relevant document tasks. Auto handles uncertain pages only when they affect a conclusion.", token: "Tokens vary by pages & tools", time: "Additional parsing time" },
      figure_variants: { title: "Additional figure candidates", desc: "Create extra layout or visual options for a figure so you can compare and choose a direction.", trigger: "Relevant figure tasks. Auto generates alternatives when the design choice materially affects communication.", token: "More image or model usage", time: "Noticeably more generation time" },
      detailed_reports: { title: "Additional process reports", desc: "Keep traceable decisions, evidence, and checks together in the existing working directory.", trigger: "Relevant deliverables. Auto adds records when reproducibility or handoff tracking calls for them.", token: "More output tokens", time: "More organization & checking" },
      alternative_routes: { title: "Alternative route comparison", desc: "Add at most one optional comparison to a selected route, reusing evidence first. Requested brainstorming and necessary corrections remain part of the task.", trigger: "Use for consequential extra comparisons. Off does not limit multiple directions you explicitly request. Experiments or extra services still require applicable authorization.", token: "One route analysis & evidence check", time: "Comparison time varies with evidence gaps" },
      maintenance_evolution: { title: "Maintenance rule iteration", desc: "Add at most one candidate rule revision and one fixed-case comparison during skill maintenance. Keep acceptance criteria fixed; retain the stable version if it fails.", trigger: "Explicit skill maintenance only; Auto needs an unresolved rule defect. Autonomous research starts from a specific request and its budget, not this switch.", token: "More candidate revision & comparison work", time: "One additional maintenance evaluation" }
    }
  }
};

const $ = (selector) => document.querySelector(selector);
const clone = (value) => JSON.parse(JSON.stringify(value));
const own = (object, key) => Object.prototype.hasOwnProperty.call(object, key);
const isObject = (value) => value !== null && typeof value === "object" && !Array.isArray(value);
const token = new URLSearchParams(location.hash.slice(1)).get("token") || "";
const localHost = ["127.0.0.1", "localhost", "[::1]"].includes(location.hostname);
const connected = location.protocol === "http:" && localHost && Boolean(token);
const states = new Map();
const systemTheme = window.matchMedia("(prefers-color-scheme: dark)");
let scope = "user";
let availableScopes = connected ? ["user"] : ["user", "project"];
let language = "zh-CN";
let busy = false;
let importing = false;
let loading = connected;
let toastTimer;
let currentError = null;
let operation = 0;

function t(key, parameters = {}) {
  let result = COPY[language][key] ?? COPY.en[key] ?? key;
  for (const [name, value] of Object.entries(parameters)) result = result.replaceAll(`{${name}}`, String(value));
  return result;
}

function blankState() {
  return { stored: { version: 1 }, draft: { version: 1 }, inherited: clone(DEFAULTS), defaults: clone(DEFAULTS), origins: {}, revision: "missing", saved: false, exported: false, loaded: !connected, conflict: false };
}

function current() { return states.get(scope); }
function effective(state = current()) {
  return { version: 1, preferences: { ...state.inherited.preferences, ...state.draft.preferences }, ui: { ...state.inherited.ui, ...state.draft.ui } };
}

function canonical(config) {
  const result = { version: 1 };
  const preferences = {};
  for (const key of KEYS) if (own(config.preferences || {}, key)) preferences[key] = config.preferences[key];
  if (Object.keys(preferences).length) result.preferences = preferences;
  const ui = {};
  for (const key of ["language", "theme"]) if (own(config.ui || {}, key)) ui[key] = config.ui[key];
  if (Object.keys(ui).length) result.ui = ui;
  return result;
}

function dirty(state = current()) { return JSON.stringify(canonical(state.draft)) !== JSON.stringify(canonical(state.stored)); }
function anyDirty() { return [...states.values()].some((state) => dirty(state)); }
function modeText(mode) { return t({ off: "modeOff", auto: "modeAuto", on: "modeOn" }[mode]); }

class ConfigurationError extends Error {
  constructor(key, parameters = {}) { super(key); this.key = key; this.parameters = parameters; }
}

// Called only after JSON.parse has confirmed valid syntax. Decode key escapes so
// "theme" and "th\u0065me" cannot silently override each other during import.
function rejectDuplicateKeys(source) {
  let cursor = 0;
  const whitespace = () => { while (/\s/.test(source[cursor] || "") && cursor < source.length) cursor++; };
  const string = () => {
    const start = cursor++;
    while (cursor < source.length) {
      if (source[cursor] === "\\") cursor += 2;
      else if (source[cursor++] === '"') return JSON.parse(source.slice(start, cursor));
    }
    throw new ConfigurationError("errorJson");
  };
  const value = (path, depth) => {
    if (depth > 64) throw new ConfigurationError("errorJson");
    whitespace();
    if (source[cursor] === "{") {
      cursor++; whitespace(); const keys = new Set();
      if (source[cursor] === "}") { cursor++; return; }
      while (cursor < source.length) {
        whitespace(); const key = string(); const field = path ? `${path}.${key}` : key;
        if (keys.has(key)) throw new ConfigurationError("errorDuplicate", { field });
        keys.add(key); whitespace(); cursor++; value(field, depth + 1); whitespace();
        if (source[cursor++] === "}") return;
      }
    } else if (source[cursor] === "[") {
      cursor++; whitespace();
      if (source[cursor] === "]") { cursor++; return; }
      while (cursor < source.length) { value(path, depth + 1); whitespace(); if (source[cursor++] === "]") return; }
    } else if (source[cursor] === '"') string();
    else while (cursor < source.length && !/[\s,\]}]/.test(source[cursor])) cursor++;
  };
  value("", 0);
}

function validate(config) {
  if (!isObject(config) || config.version !== 1) throw new ConfigurationError("errorRoot");
  for (const field of Object.keys(config)) if (!["version", "preferences", "ui"].includes(field)) throw new ConfigurationError("errorField", { field });
  for (const section of ["preferences", "ui"]) {
    if (!own(config, section)) continue;
    if (!isObject(config[section])) throw new ConfigurationError("errorObject", { field: section });
    const allowed = section === "preferences" ? KEYS : ["language", "theme"];
    for (const [key, value] of Object.entries(config[section])) {
      const field = `${section}.${key}`;
      if (!allowed.includes(key)) throw new ConfigurationError("errorField", { field });
      const values = section === "preferences" ? MODES : key === "language" ? LANGUAGES : THEMES;
      if (!values.includes(value)) throw new ConfigurationError("errorValue", { field });
    }
  }
  return canonical(config);
}

function showError(error) {
  currentError = error instanceof ConfigurationError ? error : new ConfigurationError("errorGeneric");
  $("#error-text").textContent = t(currentError.key, currentError.parameters);
  $("#error").hidden = false;
}

function dismissError() { currentError = null; $("#error").hidden = true; }
function toast(key, params) {
  clearTimeout(toastTimer);
  $("#toast").textContent = t(key, params);
  $("#toast").hidden = false;
  toastTimer = setTimeout(() => { $("#toast").hidden = true; }, 4800);
}

function translatedNode(tag, className, text) {
  const node = document.createElement(tag);
  if (className) node.className = className;
  if (text !== undefined) node.textContent = text;
  return node;
}

function costIcon(time) {
  const svg = document.createElementNS("http://www.w3.org/2000/svg", "svg");
  svg.setAttribute("viewBox", "0 0 16 16"); svg.setAttribute("fill", "none"); svg.setAttribute("aria-hidden", "true");
  const path = document.createElementNS("http://www.w3.org/2000/svg", "path");
  path.setAttribute("d", time ? "M14 8A6 6 0 1 1 2 8a6 6 0 0 1 12 0ZM8 4v4l3 2" : "M3 12 12 3M5 3h7v7");
  path.setAttribute("stroke-width", "1.2"); svg.append(path); return svg;
}

function createFeatures() {
  const fragment = document.createDocumentFragment();
  KEYS.forEach((key, index) => {
    const feature = translatedNode("article", "feature"); feature.dataset.key = key;
    feature.append(translatedNode("div", "feature-index", String(index + 1).padStart(2, "0")));
    const content = translatedNode("div", "feature-content");
    const heading = translatedNode("div", "feature-heading");
    const title = translatedNode("h3"); title.id = `title-${key}`;
    heading.append(title, translatedNode("span", "mode-label"));
    content.append(heading, translatedNode("p", "feature-description"), translatedNode("p", "trigger-description"));
    const tags = translatedNode("div", "cost-tags");
    for (const time of [false, true]) { const item = translatedNode("span"); item.append(costIcon(time), translatedNode("span", time ? "cost-time" : "cost-token")); tags.append(item); }
    content.append(tags); feature.append(content);
    const controls = translatedNode("div", "feature-control");
    const buttons = translatedNode("div", "mode-buttons");
    const toggle = translatedNode("button", "celestial-toggle"); toggle.type = "button"; toggle.setAttribute("role", "switch"); toggle.dataset.toggle = key;
    const orb = translatedNode("span", "toggle-orb"); orb.setAttribute("aria-hidden", "true");
    const stars = translatedNode("span", "toggle-stars"); stars.setAttribute("aria-hidden", "true"); toggle.append(orb, stars);
    toggle.addEventListener("click", () => setField("preferences", key, effective().preferences[key] === "on" ? "off" : "on"));
    const auto = translatedNode("button", "auto-button"); auto.type = "button"; auto.addEventListener("click", () => setField("preferences", key, "auto"));
    buttons.append(toggle, auto);
    const inherit = translatedNode("button", "inherit-button"); inherit.type = "button"; inherit.addEventListener("click", () => setField("preferences", key, undefined));
    controls.append(buttons, inherit); feature.append(controls); fragment.append(feature);
  });
  $("#feature-list").replaceChildren(fragment);
  $(".art-index").textContent = `01 — ${String(KEYS.length).padStart(2, "0")}`;
  $(".summary-meter").replaceChildren(...KEYS.map(() => translatedNode("span")));
}

function setField(section, key, value) {
  if (busy || loading) return;
  const state = current();
  if (value === undefined) { if (state.draft[section]) delete state.draft[section][key]; }
  else { state.draft[section] ||= {}; state.draft[section][key] = value; }
  state.draft = canonical(state.draft); state.saved = false; state.exported = false;
  dismissError(); render();
}

function renderText() {
  document.documentElement.lang = language;
  document.title = t("title");
  document.querySelectorAll("[data-i18n]").forEach((node) => {
    const lines = t(node.dataset.i18n).split("\n");
    node.replaceChildren();
    lines.forEach((line, index) => { if (index) node.append(document.createElement("br")); node.append(document.createTextNode(line)); });
  });
  for (const [id, key] of [["language", "language"], ["theme", "theme"], ["scope-control", "scopeLabel"], ["presets", "presetsLabel"], ["json-preview", "previewLabel"], ["dismiss-error", "dismiss"]]) $(`#${id}`).setAttribute("aria-label", t(key));
}

function applyTheme(theme) { document.documentElement.dataset.theme = theme === "system" ? systemTheme.matches ? "dark" : "light" : theme; }

function render() {
  const state = current(); const config = effective(state);
  language = config.ui.language;
  renderText(); applyTheme(config.ui.theme);
  $("#language").value = language; $("#theme").value = config.ui.theme;
  $("#scope-description").textContent = t(scope === "user" ? "scopeUserDesc" : connected ? "scopeProjectDesc" : "scopeProjectStatic");
  $("#mode-notice").textContent = t(loading ? "loading" : connected ? state.loaded ? "onlineNotice" : "loadFailed" : "staticNotice");
  $("#mode-notice").classList.toggle("static-notice", !connected);
  $("#file-help").textContent = `${t(connected ? "fileHelpOnline" : "fileHelpStatic")} ${t("exportNameNote")}`;
  document.querySelectorAll("[data-scope]").forEach((button) => {
    button.setAttribute("aria-pressed", String(button.dataset.scope === scope));
    button.disabled = busy || loading || !availableScopes.includes(button.dataset.scope);
    button.title = availableScopes.includes(button.dataset.scope) ? "" : t("scopeUnavailable");
  });
  document.querySelectorAll("[data-preset]").forEach((button) => {
    const selected = PRESETS[button.dataset.preset].every((mode, index) => config.preferences[KEYS[index]] === mode);
    button.classList.toggle("active", selected); button.setAttribute("aria-pressed", String(selected)); button.disabled = busy || loading;
  });
  document.querySelectorAll(".feature").forEach((feature) => {
    const key = feature.dataset.key; const info = COPY[language].features[key]; const mode = config.preferences[key];
    feature.dataset.mode = mode;
    feature.querySelector("h3").textContent = info.title;
    feature.querySelector(".mode-label").textContent = modeText(mode);
    feature.querySelector(".feature-description").textContent = info.desc;
    const trigger = feature.querySelector(".trigger-description"); trigger.replaceChildren(translatedNode("strong", "", `${t("trigger")} · `), document.createTextNode(info.trigger));
    feature.querySelector(".cost-token").textContent = info.token; feature.querySelector(".cost-time").textContent = info.time;
    feature.querySelector(".cost-tags").setAttribute("aria-label", t("whenUsed"));
    const toggle = feature.querySelector(".celestial-toggle"); toggle.setAttribute("aria-checked", String(mode === "on")); toggle.setAttribute("aria-label", t("switchLabel", { name: info.title, mode: modeText(mode) })); toggle.disabled = busy || loading;
    const auto = feature.querySelector(".auto-button"); auto.textContent = t("modeAuto"); auto.setAttribute("aria-pressed", String(mode === "auto")); auto.setAttribute("aria-label", t("autoLabel", { name: info.title })); auto.disabled = busy || loading;
    const hasOverride = own(state.draft.preferences || {}, key); const inherit = feature.querySelector(".inherit-button");
    inherit.textContent = t(hasOverride ? "inherit" : "inherited"); inherit.disabled = !hasOverride || busy || loading;
    const source = scope === "project" ? "sourceUser" : "sourceDefault";
    inherit.title = hasOverride ? t("explicit") : t("inheritedFrom", { source: t(source) });
  });
  const on = KEYS.filter((key) => config.preferences[key] === "on").length;
  const auto = KEYS.filter((key) => config.preferences[key] === "auto").length;
  $("#on-count").textContent = String(on); $("#auto-count").textContent = t("autoCount", { count: auto });
  $("#summary-copy").textContent = t(on ? "summaryOn" : auto ? "summaryAuto" : "summaryQuiet");
  document.querySelectorAll(".summary-meter span").forEach((node, index) => { node.className = index < on ? "is-on" : index < on + auto ? "is-auto" : ""; });
  $("#json-preview").textContent = JSON.stringify(canonical(state.draft), null, 2);
  $("#reload").hidden = !connected;
  for (const id of ["language", "theme", "inherit-ui", "reset", "import", "reload"]) $(`#${id}`).disabled = busy || loading;
  $("#export").disabled = busy || loading;
  $("#save").disabled = busy || loading || (connected && (!state.loaded || state.conflict || (!dirty(state) && state.revision !== "missing")));
  $("#save span:first-child").textContent = t(connected ? "save" : "saveStatic");
  let status = "clean", detail = "cleanDetail";
  if (loading) { status = "loading"; detail = "cleanDetail"; }
  else if (busy) { status = importing ? "importing" : "saving"; detail = importing ? "importDetail" : "savingDetail"; }
  else if (!connected) { status = state.exported ? "exported" : "staticState"; detail = "staticDetail"; }
  else if (!state.loaded) { status = "loadFailed"; detail = "retryDetail"; }
  else if (state.conflict) { status = "conflictState"; detail = "conflictDetail"; }
  else if (dirty(state)) { status = "dirty"; detail = "dirtyDetail"; }
  else if (state.saved) { status = "saved"; detail = "savedDetail"; }
  else if (state.revision === "missing") { status = "missingState"; detail = "missingDetail"; }
  $("#save-status").textContent = t(status); $("#save-detail").textContent = t(detail);
  $("#state-dot").classList.toggle("dirty", dirty(state) || !connected);
  if (currentError) $("#error-text").textContent = t(currentError.key, currentError.parameters);
}

function serverError(code, status) {
  // Stable codes distinguish a locked file from a stale revision, even when
  // both use HTTP 409. HTTP status is only a fallback for unknown codes.
  if (["unauthorized", "invalid_token", "forbidden", "invalid_origin", "invalid_host", "bad_host", "bad_origin"].includes(code)) return "errorAuth";
  if (["revision_conflict", "conflict", "stale_revision"].includes(code)) return "errorConflict";
  if (["malformed_stored_config", "invalid_stored_config", "config_read_error", "read_error"].includes(code)) return "errorStored";
  if (["scope_unavailable", "invalid_scope", "project_not_configured"].includes(code)) return "errorScope";
  if (code === "storage_error") return "errorStorage";
  if (["write_error", "config_write_error", "io_error"].includes(code)) return "errorWrite";
  if (["bad_content_type", "request_too_large", "invalid_json", "invalid_config"].includes(code)) return "errorInvalid";
  if (status === 401 || status === 403) return "errorAuth";
  if (status === 409) return "errorConflict";
  if (status === 400 || status === 413 || status === 422) return "errorInvalid";
  return "errorGeneric";
}

async function api(method, requestedScope, config, revision) {
  let response;
  try {
    const headers = { "X-CCFA-Token": token };
    const options = { method, headers, credentials: "omit", cache: "no-store", redirect: "error" };
    let path = `/api/preferences?scope=${encodeURIComponent(requestedScope)}`;
    if (method === "POST") { headers["Content-Type"] = "application/json"; options.body = JSON.stringify({ scope: requestedScope, revision, config }); path = "/api/preferences"; }
    response = await fetch(path, options);
  } catch { throw new ConfigurationError("connectionError"); }
  let data;
  try { data = await response.json(); } catch { throw new ConfigurationError("errorServer"); }
  if (!response.ok) throw new ConfigurationError(serverError(data.code, response.status));
  try {
    if (!isObject(data) || data.version !== 1 || data.scope !== requestedScope || !Array.isArray(data.availableScopes) || !data.availableScopes.every((value) => ["user", "project"].includes(value)) || typeof data.revision !== "string") throw new Error();
    validate(data.defaults); validate(data.inherited); validate(data.effective); if (data.stored !== null) validate(data.stored);
    for (const configValue of [data.defaults, data.inherited, data.effective]) {
      if (!KEYS.every((key) => own(configValue.preferences || {}, key)) || !own(configValue.ui || {}, "language") || !own(configValue.ui || {}, "theme")) throw new Error();
    }
  } catch { throw new ConfigurationError("errorServer"); }
  return data;
}

function acceptSnapshot(requestedScope, data, preserveDraft = false) {
  const previous = states.get(requestedScope);
  const stored = canonical(data.stored || { version: 1 });
  if (preserveDraft && previous) {
    // A new disk revision must never authorize overwriting it with an old draft.
    // Refresh inherited values, but retain the draft's original revision/base.
    states.set(requestedScope, { ...previous, inherited: data.inherited, defaults: data.defaults, origins: data.origins || {}, conflict: data.revision !== previous.revision });
  } else {
    states.set(requestedScope, { stored, draft: clone(stored), inherited: data.inherited, defaults: data.defaults, origins: data.origins || {}, revision: data.revision, loaded: true, saved: false, exported: false, conflict: false });
  }
  availableScopes = data.availableScopes;
}

async function loadScope(requestedScope, preserveDraft = true) {
  if (busy) return;
  if (!connected) { scope = requestedScope; if (!states.has(scope)) states.set(scope, blankState()); render(); return; }
  const previousScope = scope; scope = requestedScope;
  if (!states.has(scope)) states.set(scope, blankState());
  const requestId = ++operation; loading = true; dismissError(); render();
  try {
    const data = await api("GET", requestedScope);
    if (requestId !== operation) return;
    const keep = preserveDraft && states.get(requestedScope).loaded && dirty(states.get(requestedScope));
    acceptSnapshot(requestedScope, data, keep);
    if (current().conflict) { showError(new ConfigurationError("errorConflict")); $(".advanced-panel").open = true; }
  } catch (error) {
    if (requestId !== operation) return;
    if (previousScope !== requestedScope && states.get(previousScope)?.loaded) scope = previousScope;
    showError(error);
  } finally { if (requestId === operation) { loading = false; render(); } }
}

async function save() {
  if (!connected) { exportConfig(); return; }
  if (busy || loading || !current().loaded || current().conflict || (!dirty() && current().revision !== "missing")) return;
  const requestedScope = scope; const state = current(); busy = true; dismissError(); render();
  try {
    const data = await api("POST", requestedScope, canonical(state.draft), state.revision);
    acceptSnapshot(requestedScope, data); current().saved = true; toast("saveToast");
  } catch (error) { showError(error); }
  finally { busy = false; render(); }
}

function exportConfig() {
  const text = `${JSON.stringify(canonical(current().draft), null, 2)}\n`;
  const url = URL.createObjectURL(new Blob([text], { type: "application/json;charset=utf-8" }));
  const anchor = document.createElement("a"); anchor.href = url; anchor.download = `ccfa-preferences-${scope}.json`;
  document.body.append(anchor); anchor.click(); anchor.remove(); setTimeout(() => URL.revokeObjectURL(url), 1000);
  current().exported = true; render(); toast("exportToast");
}

async function importConfig(file) {
  if (!file || busy || loading) return;
  const requestedScope = scope;
  busy = true; importing = true; dismissError(); render();
  try {
    if (file.size > 65536) throw new ConfigurationError("errorSize");
    let content;
    try { content = new TextDecoder("utf-8", { fatal: true }).decode(await file.arrayBuffer()); } catch { throw new ConfigurationError("errorFile"); }
    let parsed;
    try { parsed = JSON.parse(content); } catch { throw new ConfigurationError("errorJson"); }
    rejectDuplicateKeys(content);
    const config = validate(parsed);
    const state = states.get(requestedScope);
    state.draft = config; state.saved = false; state.exported = false; render(); toast("importToast");
  } catch (error) { showError(error); }
  finally { busy = false; importing = false; $("#import-file").value = ""; render(); }
}

function init() {
  states.set(scope, blankState()); createFeatures();
  $("#language").addEventListener("change", (event) => setField("ui", "language", event.target.value));
  $("#theme").addEventListener("change", (event) => setField("ui", "theme", event.target.value));
  document.querySelectorAll("[data-scope]").forEach((button) => button.addEventListener("click", () => { if (button.dataset.scope !== scope) return loadScope(button.dataset.scope); }));
  document.querySelectorAll("[data-preset]").forEach((button) => button.addEventListener("click", () => {
    current().draft.preferences = Object.fromEntries(KEYS.map((key, index) => [key, PRESETS[button.dataset.preset][index]])); current().saved = false; current().exported = false;
    dismissError(); render(); toast("presetApplied", { name: t({ lean: "presetLean", balanced: "presetBalanced", deep: "presetDeep" }[button.dataset.preset]) });
  }));
  $("#inherit-ui").addEventListener("click", () => { delete current().draft.ui; current().saved = false; current().exported = false; render(); toast("inheritedToast"); });
  $("#reset").addEventListener("click", () => { current().draft = { version: 1 }; current().saved = false; current().exported = false; render(); toast("inheritedToast"); });
  $("#save").addEventListener("click", save);
  $("#export").addEventListener("click", exportConfig);
  $("#import").addEventListener("click", () => $("#import-file").click());
  $("#import-file").addEventListener("change", (event) => importConfig(event.target.files[0]));
  $("#reload").addEventListener("click", async () => { if (!dirty() || window.confirm(t("reloadConfirm"))) { await loadScope(scope, false); if (!currentError) toast("reloaded"); } });
  $("#dismiss-error").addEventListener("click", dismissError);
  $(".brand").addEventListener("click", (event) => { event.preventDefault(); window.scrollTo({ top: 0, behavior: "smooth" }); });
  $(".skip-link").addEventListener("click", (event) => { event.preventDefault(); const target = $("#preferences"); target.tabIndex = -1; target.focus(); target.scrollIntoView(); });
  systemTheme.addEventListener("change", () => applyTheme(effective().ui.theme));
  window.addEventListener("beforeunload", (event) => { if (anyDirty() || busy) { event.preventDefault(); event.returnValue = ""; } });
  render(); if (connected) loadScope("user", false);
}

init();
