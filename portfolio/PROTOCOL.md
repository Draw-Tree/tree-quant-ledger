# 📐 Paper Portfolio 實驗協議（預先登記）

> 版本：**v1.1**（2026-07-10 修訂，於首次實際調倉（2026-07-13）之前生效；v1.0 全文見 git 歷史）。
> 本文件為本實驗之證偽預先登記——**開倉後不得修改判準**；任何修訂須另立版本，
> 並於 journal 中註明生效日期。v1.1 相對 v1.0 之修訂僅限 §3.1（熊市目標破位處理）
> 與 §3.2（下行下限），均屬開倉前修訂；§6 證偽判準一字未改。
> ⚠️ 本實驗全程使用 IBKR 模擬帳戶（paper trading），不涉及任何真實資金。
> 全部內容僅為方法論研究用途，絕不構成投資建議。

## 1. 核心假說（H0）

> 由假說樹推導之證據指數（conviction）與三情境賠率（bull/bear 目標價對現價），
> 經「half-Kelly → 相關性 haircut → normalize → cap」管道每週配置，
> 可以產生**優於同一 universe 等權組合**之風險調整後回報。

本實驗檢驗的是 **sizing 是否增加價值**（選股是樹的功勞，等權 benchmark 已含選股）。
證據指數目前未經校準（見 `_lib/VALUATION_STANDARD.md` §2.4）——本實驗正是
其樣本外考場。

## 2. 參數（開倉前定案）

| 參數 | 值 | 備註 |
|---|---|---|
| Kelly fraction | **0.5（half-Kelly）** | 使用者決定 2026-07-10 |
| Position cap | 0.33 | 依 dashboard 預設 |
| Haircut λ | 0.9 | 依 dashboard 預設 |
| No-trade threshold | 1% | 依 dashboard 預設 |
| Paper NLV 起點 | USD 1,000,000 | |
| Rebalance 頻率 | 每週一（美股開盤後）| 使用星期六 cron 之最新 verdicts |
| Sizing engine | `POST https://drawtree.capital/api/portfolio/size-and-rebalance` | 不得於本地重寫；request/response 全文存檔 |

## 3. Universe 規則

- 全部 stock-trees 標的（無地域限制），**除**：
  - `TSLA-OPTIMUS`（與 TSLA 為同一證券之主題樹——避免重複下注，以 TSLA 為準）
- 必須具備有效 v2.1 估值（`tree_quant --check` 通過）方可入圍。
- Edge ≤ 0（樹的情境結構顯示現價不具正期望）之標的由 engine 自動剔除——
  整棵樹表示「此價不值得下注」，不下注屬設計之一部分。
- 非美元標的：以當日匯率將 bull/bear/current 換算為美元後傳入 engine
  （股數方能正確），匯率記入 journal。
- IBKR 不支援之市場（如韓國 KRX）：照常計算 weight，執行失敗如實記錄為
  cash drift，不得事後修改 universe 掩飾。

### 3.1 熊市目標破位（bear breach）——v1.1 新增

現價 ≤ 熊市目標價，與 edge ≤ 0 是**性質不同的兩件事**，不得混同剔除。
現價跌破證偽情境目標，只有兩種可能：

1. **估值資料錯誤**（例：2026-07-10 ONDS 審計發現股數錯誤，使全部目標價高估約一倍）；
2. **市場開價低於最壞情境**——若樹是對的，這是全組合賠率最佳的機會。

兩者無法由機器區分，因此規則為「**隔離＋強制審查；審查通過即為最大注碼候選**」：

- **隔離**：破位標的當週不入 sizing，於 journal 記錄
  `bear_breach_review_required`，並在週報中公開列示（不得靜默剔除）。
- **強制審查**：依 `_lib/VALUATION_STANDARD.md` §4.4 執行——外部市值對數、
  事件掃描、相關 verdict 重審；結論二擇一：
  - 樹錯了 → 依 §4.3 重新錨定估值（破位自然消失）；
  - 樹是對的 → 於 `valuation.yaml` 寫入
    `bear_breach_review: {date, verdict: affirmed, note}`。
- **重新入場**：持有效期內（28 日）affirmed 審查之破位標的重新入圍，
  其下行以 §3.2 之 5% 下限計算——Kelly 值極大，實際倉位由 position cap
  與 normalize 約束。審查逾期須重新審查。

### 3.2 下行下限（downside floor）——v1.1 新增

所有入圍標的傳入 engine 之熊市價格以
`min(熊市目標, 現價 × (1 − 5%))` 計算，即 **sizing 使用之下行風險最少為 5%**。
理由：下行趨近於零時 Kelly 公式發散，倉位大小完全由單一輸入（熊市目標）之
微小誤差主導——ONDS 事件中「下行 4% → raw Kelly 531%」即為此病理。
原始熊市目標與下限是否觸發均記入 journal；原始下行介乎 0–10% 之標的
於週報標示為待覆核。

## 4. 每週流程（全自動）

```
六（HKT）  樹 cron 更新 verdicts + snapshots（既有）
日 04:00 UTC  fleet-audit：全部樹 --check + 外部市值 sanity gate
一 13:45 UTC  GitHub Actions：
   1. 拉取 main 最新樹數據 → 建構 ideas（§3 規則，含破位隔離）
   2. POST engine（§2 參數）→ target weights + IBKR 訂單
   3. IB Gateway（paper）：讀取 NLV/持倉 → 提交 marketable-limit 訂單
   4. Journal：ideas / engine request+response / 訂單 / fills / NAV → append-only commit
   5. Slack：模擬組合週報（附研究免責聲明）
```

## 5. 紀錄（append-only，與 quant_history 同一紀律）

- `_paper/weekly/YYYY-MM-DD.json` — 該週全部原始數據（ideas、engine 往返、
  訂單、fills、匯率、破位隔離名單、下行下限觸發記錄）
- `_paper/nav.jsonl` — 每週一行：paper NLV、等權 benchmark 指數、SPY、turnover
- 歷史行**永不修改**。

## 6. 證偽判準（預先登記，不得事後移動門檻；v1.1 未作任何修改）

1. **期限**：52 週。
2. **主判準**：第 52 週，組合對同 universe 等權 benchmark 之資訊比率（IR）< 0
   → **H0 證偽**，實驗結束並公開覆盤。
3. **中期檢查**：第 26 週，conviction 對標的其後 4 週回報之 realized IC ≤ 0
   → 「證據指數具訊號」子假說接近證偽 → 組合縮至半倉繼續（樣本不足，不停止）。
4. **風控熔斷**：任何時點相對等權 benchmark 落後 ≥ 15 個百分點
   → 暫停加倉、啟動公開檢討（red flag，非證偽）。

## 7. Benchmarks

- **主尺**：同一 universe 等權組合（每週使用相同入圍名單、等權、同步 rebalance；
  以隔離 sizing 效果）
- **副尺**：SPY（供讀者參照）

## 8. 對外呈現

每週 Slack 貼文以「📐 模擬組合週報 · 🔬 校準中實驗」格式，展示 target weights
前十位、現金、NAV 對 benchmarks、破位隔離名單；每貼附註
「IBKR 模擬帳戶・非真實資金・非投資建議」。
