# 📋 校準資料集規格書（CALIBRATION SPEC）

> 本檔是校準資料集的完整規格：欄位字典、有效性規則、預登記分析協議、
> 重校程序與 artifact 案底。目的：三個月後的維護者或任何外部研究者，
> 不需要任何對話上下文即可正確使用這批數據做 alpha 研究與等級重校。
> 隨每次出口同步到公開庫 `calibration/SPEC.md`。schema_version = 2。

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
   - cascade 解讀警示：本管道每週重審同批假說，同一單新聞可連續兩週觸發
     轉變，「再有轉變」部分是管道自身持續反應；一律對比無降級週基準行。

## 6. 等級重校程序（IMPACT_GRADES 何時改、點樣改）

1. **門檻**：某等級累積 ≥30 個獨立降級 cluster（aligned）方可重估。
2. **估計**：以該等級 cluster 層 `excess_h1..h4` 均值曲線推算實證衝擊，
   與現行常數（致命2.5/重創1.6/明顯受損0.9/輕微0.4/邊緣0.15）比較。
3. **混合**：新常數＝信度加權（§5.6 同式：Z=m/(m+k)，m＝獨立 cluster 數）
   之實證值與專家先驗混合——樣本愈多，數據話事權愈大。
4. **紀錄**：任何常數修改必須在 RELEASES.md 開新版本、附全套重算數字；
   舊常數原文保留。

## 7. Artifact 案底（datestamped，處理歷史數據時必讀）

| 日期 | 症狀 | 成因 | 修法 |
|---|---|---|---|
| 2026-07-22 | 964 事件中 908 個「前向回報」實為追蹤首週行情 | 判定史始於 5 月、價格史始於 7 月，at_or_after 錯配 | 規則 4.2（7 日對齊），錯配事件前向回報清空 |
| 2026-07-22 | 34 條 leg 回報恆為 0 | 07-22 補行未 sync 價（snapshot_price_date 未變） | 規則 4.3（stale-leg），`cmd_snapshot` 加寫行警示 |
| 2026-07-21 | 首版「首個訊號」表（降級 −1.5%、等級單調）誤讀為訊號 | 上述兩 artifact ＋事件重覆計數 | RELEASES.md 已附正式更正；主口徑改 cluster×超額 |

## 8. 版本紀錄

- **v2.1（2026-07-22）**：clusters.csv 加 `mix_type`（訊號純度）；新增
  H-purity 假說（附 in-sample 誠實聲明）與純度口徑 permutation 檢定。
- **v2（2026-07-22）**：加 event_id/cluster/pool/excess/necessity/state 壽命
  /conviction_delta 欄；clusters.csv＋廣度 cascade 層；分析腳本隨庫發布；
  預登記協議與重校程序成文。
- **v1（2026-07-21）**：首版 fwd_1w/fwd_4w 事件表（受 artifact 影響，見 §7）。

*研究用途，非投資建議。*
