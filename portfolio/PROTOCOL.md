# 📐 Paper Portfolio 實驗協議（預登記）

> Status: ACTIVE（2026-07-10 起）。本文件為實驗嘅證偽預登記——**開倉後不得修改判準**；
> 任何修訂須另立版本並喺 journal 註明生效日期。
> ⚠️ 本實驗全程使用 IBKR 模擬帳戶（paper trading），不涉及任何真實資金。
> 全部內容為方法論研究用途，絕不構成投資建議。

## 1. 核心假說（H0）

> 由假說樹推導嘅證據指數（conviction）＋三情境賠率（bull/bear 目標價 vs 現價），
> 經「half-Kelly → 相關性 haircut → normalize → cap」管道每週配置，
> 可以產生**優於同一 universe 等權組合**嘅風險調整後回報。

呢個實驗測試嘅係 **sizing 有冇加值**（選股係樹嘅功勞，等權 benchmark 已含選股）。
證據指數目前未經校準（見 `_lib/VALUATION_STANDARD.md` §2.4）——本實驗正正係
佢嘅 out-of-sample 考場。

## 2. 參數（開倉前定案）

| 參數 | 值 | 備註 |
|---|---|---|
| Kelly fraction | **0.5（half-Kelly）** | 用戶決定 2026-07-10 |
| Position cap | 0.33 | 跟 dashboard 預設 |
| Haircut λ | 0.9 | 跟 dashboard 預設 |
| No-trade threshold | 1% | 跟 dashboard 預設 |
| Paper NLV 起點 | USD 1,000,000 | |
| Rebalance 頻率 | 每週一（美股開市後）| 用星期六 cron 嘅最新 verdicts |
| Sizing engine | `POST https://drawtree.capital/api/portfolio/size-and-rebalance` | 不得本地重寫；request/response 全文存檔 |

## 3. Universe 規則

- 全部 stock-trees 標的（無地域限制），**除**：
  - `TSLA-OPTIMUS`（與 TSLA 同一證券嘅主題樹——避免雙重落注，以 TSLA 為準）
- 必須有效 v2.1 估值（`tree_quant --check` 通過）先入圍。
- Engine 對 downside 非正（現價 ≤ 熊市目標）或 edge ≤ 0 嘅名自動剔除——
  賠率結構壞咗嘅名唔落注，屬設計一部分。
- 非美元標的：以當日 FX 將 bull/bear/current 換算成 USD 傳入 engine（股數先會正確），
  FX 記入 journal。
- IBKR 不支援嘅市場（如韓國 KRX）：照計 weight，執行失敗如實記錄為 cash drift，
  不得事後改 universe 遮醜。

## 4. 每週流程（全自動）

```
六（HKT）  樹 cron 更新 verdicts + snapshots（既有）
一 13:45 UTC  GitHub Actions：
   1. 拉 main 最新樹數據 → 砌 ideas（§3 規則）
   2. POST engine（§2 參數）→ target weights + IBKR 訂單
   3. IB Gateway（paper）：讀 NLV/持倉 → 提交 marketable-limit 訂單
   4. Journal：ideas / engine request+response / 訂單 / fills / NAV → append-only commit
   5. Slack：模擬組合週報（掛研究免責）
```

## 5. 紀錄（append-only，與 quant_history 同一紀律）

- `_paper/weekly/YYYY-MM-DD.json` — 該週全部原始數據（ideas、engine 往返、訂單、fills、FX）
- `_paper/nav.jsonl` — 每週一行：paper NLV、等權 benchmark 指數、SPY、turnover
- 歷史行**永不修改**。

## 6. 證偽判準（預登記，唔准事後搬龍門）

1. **期限**：52 週。
2. **主判準**：第 52 週，組合對同 universe 等權 benchmark 嘅資訊比率（IR）< 0
   → **H0 證偽**，實驗結束並公開覆盤。
3. **中期檢查**：第 26 週，conviction 對標的其後 4 週回報嘅 realized IC ≤ 0
   → 「證據指數有訊號」子假說接近證偽 → 組合縮至半倉繼續（樣本未夠，唔停）。
4. **風控熔斷**：任何時點相對等權 benchmark 落後 ≥ 15 個百分點
   → 暫停加倉、觸發公開檢討（red flag，非證偽）。

## 7. Benchmarks

- **主尺**：同一 universe 等權組合（每週用相同入圍名單、等權、同步 rebalance；隔離 sizing 效果）
- **副尺**：SPY（俾讀者 context）

## 8. 對外呈現

每週 Slack 貼文以「📐 模擬組合 · 🔬 校準中實驗」格式，只展示 target weights 頭十位、
cash、NAV vs benchmarks；每貼附「IBKR 模擬帳戶・非真實資金・非投資建議」。
