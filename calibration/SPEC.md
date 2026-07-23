# 📋 校準資料集規格書（CALIBRATION SPEC）

> 本檔是校準資料集的完整規格：欄位字典、有效性規則、預登記分析協議、
> 重校程序與 artifact 案底。目的：三個月後的維護者或任何外部研究者，
> 不需要任何對話上下文即可正確使用這批數據做 alpha 研究與等級重校。
> 隨每次出口同步到公開庫 `calibration/SPEC.md`。schema_version = 2。

## 0. 主假說與 Alpha 策略（整個資料集為此而存在）

**主假說 H**：假說樹的判定變化走在股價前面——純降級股其後一週跑輸全池
中位、純升級股跑贏；等級愈重、降級愈齊，效應愈強。

**Alpha 策略讀數**：做多純升級組、做空純降級組（組內等權）。此組合的
市場中性回報＝

```
策略回報（strategy return）＝升級籃超額均值 − 降級籃超額均值
    某週缺一邊 ⇒ 該邊以 0 計（缺邊以全池對沖）——單邊週照樣計分：
    僅有降級組時，策略回報＝−降級組超額（做空降級、對沖全池）
組差（spread）＝雙邊週之策略回報（兩邊皆有時兩者相等）
加權版＝同式，但以 |訊號分| 為權
訊號分＝Σ±衝擊等級權重（致命 2.5／重創 1.6／明顯受損 0.9／
        輕微 0.4／邊緣 0.15；升級＋、降級−）
```

大盤升跌與板塊順逆風在策略回報中互相抵銷——**策略回報序列持續 >0 即
策略有 alpha**，單邊命中率只是輔助讀數。超額＝個股一週回報−全池中位
（口徑同 §5.2）。

**持有期**：非固定一週。倉位持有至 (a) 該判定被下一次轉變推翻（state
翻轉即平倉／反手），或 (b) H\* 週上限——H\* 由 H-horizon 之
`excess_h1..h8` 曲線見頂位置決定，樣本累積後成文。每週對答案窗口只是
**最小追蹤單位**（每個名單 cohort 之 h1 讀數），多週延續效應由校準
曲線自動累積（同一 cohort 之 h2、h3……逐週補齊）。

衝擊等級權重是**變數而非常數**：隨校準樣本累積按 §6 以 Bayesian 信度
混合重估，上列為現行值；事實源＝`_lib/tree_quant.py` 之 `IMPACT_GRADES`，
週報訊號分／加權組差／方法腳註皆即時讀取該處，重校後自動跟隨。

**檢驗機制**：每週六名單先公開（Slack ＋ `verdict_watch.jsonl`
append-only 帳本），下週六對答案；逐週 `spread_pp`／`wspread_pp` 落賬；
累積 ≥30 個獨立降級樣本後跑正式 permutation 檢定（§5.4）。mixed 週
（同股同週有升有降）依 H-purity 不入比分；recode 與模型遷移事件於
源頭剔除（§4.1、§7）。實驗規則全文見公開庫
`portfolio/PUBLIC_EXPERIMENT_20260722.md`。

## 1. 資料層級

```
verdict_history（假說 JSON，事實源）
  → events.csv    一行一個判定轉變事件（raw ＋ enrichment）
  → clusters.csv  一行一個 ticker×事件週 cluster（廣度＋cascade）
  → CALIBRATION.md 結果表（全部由 analysis.py 生成，人手不落數字）
```

生成鏈：`tree_quant.py cmd_calib_table`（raw）→ `analysis.py`（enrichment
＋統計）。兩支腳本隨出口發布，外部跑同一份 code 得同一份數。

## 2. events.csv 欄位字典

| 欄 | 定義 | 空值語義 |
|---|---|---|
| `schema_version` | 本表 schema 版本（現為 2） | 不空 |
| `event_id` | `ticker:hypothesis:date`，穩定主鍵 | 不空 |
| `ticker` / `hypothesis` / `branch` | 樹、子假說 ID、所屬分支 ID | branch 空＝無法歸屬 |
| `impact_grade` | 分支衝擊等級（§1.5 封閉枚舉：致命/重創/明顯受損/輕微/邊緣） | 空＝未設 |
| `grade_implied_from_fib` | True＝等級由舊制 Fibonacci 權重遷移映射推得，非人工判定 | — |
| `branch_weight` | 分支 log-odds 合成權重（致命2.5/重創1.6/明顯受損0.9/輕微0.4/邊緣0.15） | — |
| `is_necessity_leaf` | 該假說是否分支之必要葉（證偽即殺支） | — |
| `model` | 判讀模型：entry 有 stamp 用 stamp（2026-07-22 起 apply-patch 寫入）；無則按日期推斷年代（<07-16 grok-4.5／07-16–17 deepseek-v3.2／≥07-18 deepseek-v4-pro） | 不空 |
| `model_transition` | True＝事件屬模型切換首個判讀日（07-16/17/18）的重新評分潮，非市場事件；統計表剔除、原始行保留 | — |
| `trigger` | 觸發源：`weekly`＝週六掃描；`earnings`＝財報後裁定（每日 cron 偵測業績剛公布，`--earnings-mode` 以發布材料重審）。兩層統計性質不同，分析須分層（§5.6 H-trigger） | 空＝2026-07-23 stamp 前 legacy，觸發源不可考 |
| `date` / `from` / `to` | 事件日、轉變前後判定（六值枚舉） | — |
| `score_delta` | 判定分數差（✅+2/🟢+1/⚪0/🟡−1/🟠−2/🔴−3） | 空＝legacy 判定無法映射 |
| `direction` | downgrade / upgrade / lateral（按 score_delta 符號） | — |
| `next_transition_days` | 同一假說下一次非 recode 轉變距本事件日數＝本 state 實際壽命 | 空＝至今未再轉變（右刪失） |
| `days_since_prev_transition` | 距上一次轉變日數（轉變頻密度） | 空＝首次轉變 |
| `gap_days` | 事件日至最近一個不早於它的價格行的日數 | 空＝無價格行 |
| `row_date` / `conviction_at` / `price_at` | 對齊行（僅 `gap_days`≤7 時填）：日期、當時 H0 信念、快照價 | 空＝對齊無效 |
| `conviction_delta_1w` | 事件後一行 H0 信念變化（信念反應速度） | 空＝無下一行 |
| `fwd_h1..fwd_h8` | 對齊行起 +1..+8 行累計原始回報（每行≈1 週） | 空＝歷史不足或 leg 無效 |
| `pool_h1..pool_h8` | 同期全池（全 72 樹）同 leg 回報中位數 | 空＝該期無池數據 |
| `excess_h1..excess_h8` | `fwd_h − pool_h`（超額回報，**分析主口徑**） | 空＝任一輸入空 |
| `cluster_id` / `cluster_size` | `ticker@ISO週`；該 cluster 事件總數 | 不空 |

## 3. clusters.csv 欄位字典

| 欄 | 定義 |
|---|---|
| `cluster_id` / `ticker` / `first_event` / `last_event` | ticker×ISO 事件週；首末事件日 |
| `mix_type` | 訊號純度：down_only（純降級週）／mixed（同週有升有降，訊號互相抵銷）／up_only／lateral_only |
| `n_events` / `n_hypotheses` / `n_branches` | 廣度：事件數、涉及葉數、涉及分支數 |
| `n_down` / `n_up` / `n_lateral` | 方向分解 |
| `sum_score_delta` | 淨分數變化（正=淨升級） |
| `grade_weighted_delta` | Σ score_delta × 等級權重（衝擊加權淨變化） |
| `any_necessity_down` | 該週是否有必要葉降級 |
| `aligned` | 是否有成員事件通過價格對齊 |
| `fut_transitions_28d` / `fut_downgrades_28d` / `fut_upgrades_28d` | cascade：末事件日後 28 日內同 ticker 再現轉變/降級/升級次數 |
| `excess_h1..excess_h8` | cluster 層超額回報（對齊成員事件均值） |

## 4. 有效性規則（引擎層執行，非事後篩選）

1. **recode 剔除**：`recode: true` 之轉變屬方法論重新編碼，非市場事件，源頭不入樣本。
2. **事件對齊**：事件日 7 日內無價格行 ⇒ 無「事件時價格」可言，對齊欄與
   前向回報一律留空（`gap_days` 照記供審計）。
3. **leg 有效性**：leg 起訖兩行 `snapshot_price_date` 相同 ⇒ 期間無重新
   標價，0% 屬 artifact，不出數。池基準 leg 同規則。

## 5. 預登記分析協議（先寫規則，後見數據）

1. **分析單位＝cluster**（ticker×事件週）。同週同股多事件共享同一段回報，
   事件層均值會重覆計數（案例：2026-07-10 ONDS 四葉齊降共享同一段 −10.1%）。
2. **主口徑＝超額回報**（扣同期全池中位）。原始回報只作參考表。
3. **Horizon family 固定 +1..+8 週，永遠呈報全條曲線**，不得只引用單一
   窗口（防事後挑選）。曲線右端隨追蹤歷史自然填滿。
4. **顯著性＝cluster 層單尾 permutation 檢定**（固定種子、20,000 次重抽），
   p 值照報，不因結果不好看而省略。
5. **state 壽命過濾**（嚴格讀法）：h×7 > `next_transition_days` 的格已跨入
   下一個 state，混雜；嚴格分析應剔除。
6. **預登記假說**：
   - **H-grade**：降級後超額回報為負，負向幅度隨衝擊等級遞增。
   - **H-breadth**：同週降級廣度（`n_down`、`grade_weighted_delta`、
     `any_necessity_down`）愈大，未來 28 日 cascade 機率愈高、超額回報愈差。
   - **H-purity**（2026-07-22 增補）：逐隻股票逐週看淨方向——同週有升有降
     （mixed）＝訊號互相抵銷，不應與純降級週（down_only）混計；預期
     純降級週回報差於混合週，且純降級多葉週差於單葉週。**誠實聲明**：
     此假說由維護者檢視首批 19 個對齊事件（ACN 混合週 +4.6% 異常）後
     提出，對該批樣本屬 in-sample 探索——假說由數據啟發，不能用同一批
     數據證明自己；僅對其後累積的新樣本具預登記檢定效力。純度口徑的
     permutation 檢定（down_only vs up_only＋lateral_only，mixed 剔除）
     與原始口徑並列呈報。
   - **H-trigger**（2026-07-23 增補，先寫規則後見數據）：判定轉變按觸發源
     分兩層——`weekly`（週六掃描：判讀模型從一週新聞流中發現的增量資訊）
     與 `earnings`（財報後裁定：業績公布翌日以發布材料重審）。財報後層
     的股價已於公布時即時反應大半，其後一週超額回報測的是**財報後漂移**
     （post-earnings drift）而非純資訊發現；預期：(a) 兩層的降級後超額
     回報同號（漂移文獻支持財報後仍沿意外方向延續），但 (b) 週掃描層
     的幅度更大（財報層的資訊已部分入價）。兩層永遠分開呈報，不合併
     檢定；主組差照計全樣本，觸發源作分層輔助讀數，累積 ≥30 個獨立
     cluster／層後分層 permutation。stamp 前 legacy 事件（`trigger` 空）
     不入分層檢定。**財報層操作規則**（2026-07-23 增補）：(a) 財報後裁定
     產生判定轉變時，事件**當日即時公開**於實驗頻道（逐葉明細＋訊號分＋
     事件日收盤價）——「先公開後對答案」之日內版；(b) 其**計分基準＝事件
     日收盤**（earnings-mode 當日快照價），非週六名單日收盤——事件先行
     兩三日而週六才開錶，會漏計（或倒計）事件後最烈的一段；(c) 事件照隨
     週六名單落賬（`earn_base`／`earn_base_date` 欄），對答案時由基準價
     開錶，池中位仍為週窗口徑——此窗口差異屬財報層固有，兩層分開呈報
     即為此故。
   - **H-horizon**（2026-07-23 增補）：效應的**持續期**本身是研究對象——
     判定轉變的效應並非一週內完結。預期：(a) 降級後累計超額回報於 +1..+4
     週持續走闊（漂移延續），不出現一週內完全均值回歸；(b) 持續期與
     state 壽命（`next_transition_days`）相關——判定未被下一次轉變推翻
     期間，效應持續；state 愈長命，可收割的窗口愈長。讀數＝
     `excess_h1..h8` 全條曲線（§5.3 已強制全曲線呈報，禁止單點引用）；
     嚴格讀法依 §5.5 剔除已跨入下一 state 的格。此假說決定策略的
     **持倉期參數**：若曲線於 h2–h3 見頂，正式實驗的一週對答案窗口
     之外應另設多週追蹤讀數。
   - **H-spread**（2026-07-23 增補，主策略讀數；同日修訂為策略回報口徑）：
     每週「策略回報」（§0：升級籃超額−降級籃超額，缺邊以 0 計——單邊週
     照計分）之時間序列均值 >0；加權版（|訊號分| 為權）同號且幅度不小於
     等權版——若加權版明顯弱於等權版，即「等級愈重效應愈強」不成立，
     IMPACT_GRADES 應依 §6 重校。逐週 `strat_pp`／`wstrat_pp`（及雙邊週
     之 `spread_pp`／`wspread_pp`）存於 `portfolio/verdict_watch.jsonl`
     之 review 欄。
   - cascade 解讀警示：本管道每週重審同批假說，同一單新聞可連續兩週觸發
     轉變，「再有轉變」部分是管道自身持續反應；一律對比無降級週基準行。

## 6. 等級重校程序（IMPACT_GRADES 何時改、如何改）

1. **門檻**：某等級累積 ≥30 個獨立降級 cluster（aligned）方可重估。
2. **估計**：以該等級 cluster 層 `excess_h1..h4` 均值曲線推算實證衝擊，
   與現行常數（致命2.5/重創1.6/明顯受損0.9/輕微0.4/邊緣0.15）比較。
3. **混合**：新常數＝信度加權（§5.6 同式：Z=m/(m+k)，m＝獨立 cluster 數）
   之實證值與專家先驗混合——樣本愈多，數據的決定權愈大。
4. **紀錄**：任何常數修改必須在 RELEASES.md 開新版本、附全套重算數字；
   舊常數原文保留。

## 7. Artifact 案底（datestamped，處理歷史數據時必讀）

| 日期 | 症狀 | 成因 | 修法 |
|---|---|---|---|
| 2026-07-22 | 964 事件中 908 個「前向回報」實為追蹤首週行情 | 判定史始於 5 月、價格史始於 7 月，at_or_after 錯配 | 規則 4.2（7 日對齊），錯配事件前向回報清空 |
| 2026-07-22 | 34 條 leg 回報恆為 0 | 07-22 補行未 sync 價（snapshot_price_date 未變） | 規則 4.3（stale-leg），`cmd_snapshot` 加寫行警示 |
| 2026-07-21 | 首版「首個訊號」表（降級 −1.5%、等級單調）誤讀為訊號 | 上述兩 artifact ＋事件重覆計數 | RELEASES.md 已附正式更正；主口徑改 cluster×超額 |
| 2026-07-22 | 07-18 週轉變量爆升至常態 4–6 倍（32 個 vs 平時 5–8）、方向偏淡（23 降 9 升）、跳≥2 級 12 個 | 判讀模型遷移（07-16 grok-4.5→deepseek-v3.2；07-18→v4-pro）——「換改卷老師」重新評分潮，非市場事件 | `model`／`model_transition` 欄入表；遷移日事件統計表剔除、觀察名單剔除；公開實驗延至 07-31 後首個 mark 開始；覆核計劃：追蹤 07-18 批轉變其後數週的反轉率——低反轉＝一次性口徑重校，高反轉＝模型噪音需整批標記 |
| 2026-07-22（續） | 凍結證據 A/B（12 樹×3 葉×3 reps，`_ab_results/model_ab_20260722_1805`）：deepseek-v4-pro 自我一致性 95%（同一證據可判出橫跨三級的不同答案）、無故改判 5 次中 4 次為降級、API 失敗 4 次；grok-4.3 一致性 100%、零失敗、更平（$0.038 vs $0.042）。deepseek 單次無故改判率 ~4.6% × ~610 葉 ≈ 每週 28 個純噪音轉變——與 07-18 實測 32 個吻合 | deepseek-v4-pro 判讀噪音（偏淡），非市場事件亦非口徑重校 | 艦隊 default 切換至 x-ai/grok-4.3（07-23 起）；07-16..18 全部非 recode 轉變由 `model_audit.py` 以 grok-4.3 零搜尋整體重審，更正以 recode:true 入帳；07-25（grok 首個週六判讀）預防性入 MODEL_TRANSITION_DATES |

| 2026-07-23 | 週報「無池內價格」／calib「價格對齊無效」比例偏高 | ①07-11 週六有 15/72 棵樹因個別 workflow 失敗整週冇快照行（星期五收市價缺失，無補數機制）；②07-09、07-22 兩次全艦隊中週補行未 sync 價（snapshot_price_date 停留上一週六）——stale 行夾在中間令 positional h1 leg 永久失效（受影響事件於 h2 位補見完整週回報）；③cmd_fetch_price 單源 Yahoo、無重試，失敗時 apply-patch 曾以空字串抹走舊 last_price_line | 價格 fetch 加重試 ×3 ＋ Finnhub 後備；apply-patch 禁以空 price 覆寫；新增週六 price-sweep workflow（只補價不觸判定）逐棵補齊過期收市價；歷史 stale 行保留原樣（stale 規則照剔），不回填 |

## 8. 版本紀錄

- **v2.9（2026-07-23）**：H-trigger 財報層操作規則——事件當日即時公開至
  實驗頻道（`_earnings_cron` 自動）、計分基準＝事件日收盤（週報名單記
  `earn_base`，對答案由基準價開錶）、照隨週六名單落賬分層呈報。
- **v2.8（2026-07-23）**：point-in-time 價格回補工具（`price_backfill.py`
  ＋手動 workflow）——以 Yahoo 歷史日線補返 07-11 缺行的 12 棵樹（另 3 棵
  無先前行、無狀態可搬，不補）。界線：只補客觀市場價與 carried state
  （該週無 judging 發生）、目標規則自動發現不容挑選、逐行帶
  `backfilled: true` 標記、pi_*／er_* 以舊 targets＋新價確定性重算。
  回補屬資料修復而非改寫歷史：價格可對照任一公開數據源覆核。
- **v2.7（2026-07-23）**：價格可用性加固（§7 末行）——fetch 重試＋Finnhub
  後備、apply-patch 空價保護、週六 price-sweep 掃底 workflow；目標：任何
  一棵樹不再出現「成週冇星期五收市價」。
- **v2.6（2026-07-23）**：§0 策略讀數由「組差」改為「策略回報」（缺邊
  以 0 計、全池對沖——單邊週照計分；雙邊週即組差）；新增持有期條款
  （持有至 state 翻轉或 H\* 上限，一週僅為最小追蹤單位）；H-spread 改
  策略回報口徑；review 欄新增 `strat_pp`／`wstrat_pp`。維護者裁定：
  「僅降級週無組差可計」屬錯誤框架——沽空降級對沖全池本身就是完整
  倉位，必須計分。
- **v2.5（2026-07-23）**：§5.6 增補 H-horizon（效應持續期：+1..+4 週累計
  超額持續走闊、持續期與 state 壽命相關；決定策略持倉期參數）；公開帳本
  README 主假說成績改三層結構（歷史資料集／先導逐週計分／正式實驗）。
- **v2.4（2026-07-23）**：events.csv 加 `trigger` 欄（weekly／earnings／
  空＝legacy）；判讀 patch 與 apply-patch 全艦隊 stamp 觸發源；§5.6 增補
  H-trigger（財報後裁定＝財報後漂移層，與週掃描分層呈報）；週報明細
  以 📅 標記財報後裁定、分維度摘要加按觸發源一行。
- **v2.3（2026-07-23）**：新增 §0 主假說與 Alpha 策略（組差／加權組差／
  訊號分定義）；§5.6 增補 H-spread（主策略讀數）；週報第二條 message
  改組差頭條＋合併排榜，`verdict_watch.jsonl` review 欄新增
  `spread_pp`／`wspread_pp`。
- **v2.2（2026-07-22）**：events.csv 加 `model`／`model_transition` 欄；
  遷移日事件於統計表與觀察名單剔除（原始行保留）；verdict_history 新
  entry 起帶 `model` stamp；公開實驗開始日定為 07-31 後首個 mark。
- **v2.1（2026-07-22）**：clusters.csv 加 `mix_type`（訊號純度）；新增
  H-purity 假說（附 in-sample 誠實聲明）與純度口徑 permutation 檢定。
- **v2（2026-07-22）**：加 event_id/cluster/pool/excess/necessity/state 壽命
  /conviction_delta 欄；clusters.csv＋廣度 cascade 層；分析腳本隨庫發布；
  預登記協議與重校程序成文。
- **v1（2026-07-21）**：首版 fwd_1w/fwd_4w 事件表（受 artifact 影響，見 §7）。

*研究用途，非投資建議。*
