# 📐 tree-quant-ledger

Stock Trees 研究系統的**公開操作帳本**。

我們在私有研究庫維護 70+ 棵「假說樹」——每個投資論點寫成可證偽的結構，每週
自動對照新證據逐葉判定，合成信念，再由 Kelly 引擎定出模擬組合的注碼。本庫
每週自動同步其中的**操作層**：數字信號、判定枚舉、分支重要度、模擬組合的
每一筆動作——以及對私有內容的 SHA-256 承諾。研究原文（假說、結論、估值邏輯）
不在此庫，但**每一個對外的賭注與判定都預先公開、事後可驗、錯誤不可塗改**。

## 📈 最新表現（對比基準）

截至 **2026-07-20**（三指數自 2026-07-14 起 base 100，指數對指數、貨幣中性）：

| 指數 | 水平 | 累計 |
|---|---|---|
| **組合**（Kelly 定倉） | 97.43 | −2.57% |
| 等權同池（真正的對手） | 96.12 | −3.88% |
| SPY（大市參照） | 99.10 | −0.90% |

**相對等權（sizing 淨貢獻）：+1.31 點**｜相對 SPY：−1.67 點

本實驗檢驗的是 Kelly 定倉能否勝過同池等權——單週為 noise，須看累積。完整逐週表：[`portfolio/PERFORMANCE.md`](portfolio/PERFORMANCE.md)

## 🧭 導讀（按你想做的事）

| 你想…… | 讀這裡 |
|---|---|
| 看表現 | 上表＋[`portfolio/PERFORMANCE.md`](portfolio/PERFORMANCE.md)（逐週對基準） |
| 明白系統怎樣運作 | [`portfolio/RELEASES.md`](portfolio/RELEASES.md) 的「設計全貌」——五步把論點變成注碼，另見 [`portfolio/PROTOCOL.md`](portfolio/PROTOCOL.md)（預登記協議） |
| 看判定變化有無預測力 | [`calibration/CALIBRATION.md`](calibration/CALIBRATION.md)——每週重算的降級×等級前向回報表；自行重算見「如何驗證」第 3 條 |
| 驗證我們沒有改寫歷史 | 「如何驗證」第 1、2 條（git 歷史＋`commitments/`） |
| 挑戰我們的方法 | [`portfolio/OPEN_QUESTIONS.md`](portfolio/OPEN_QUESTIONS.md)（公開掛帳的方法論爭議） |

## 📂 結構

**組合實驗（`portfolio/`）**
- `PERFORMANCE.md` — 每週淨值對比基準：組合／等權同池／SPY 皆 base 100，
  逐週回報＋累計、相對等權（sizing 淨貢獻）與相對 SPY 領先點數
- `PROTOCOL.md` — 〈一個投資組合，究竟是如何形成的？〉＋預登記實驗協議
- `RELEASES.md` — 方法論版本變更（公開理由、公式、實測影響），含系統設計全貌
- `OPEN_QUESTIONS.md` — 尚未解決的方法論爭議，歡迎挑戰
- `weekly/*.json` · `nav.jsonl` — IBKR 模擬組合每週 journal（ideas、sizing
  引擎往返、訂單、成交）與 NAV 序列

**研究樹信號（`trees/{TICKER}/`）**
- `quant_history.jsonl` — 每週一行：價格、三情境目標價、證據指數
  （conviction）、雙軌傾向數值、各分支 weight/impact_grade/score/verdict
- `structure.json` — 分支重要度地圖：每支分支的權重、衝擊等級（§1.5）、
  必要葉 ID、葉成員 ID 與葉權重。等級為封閉枚舉（致命 2.5／重創 1.6／
  明顯受損 0.9／輕微 0.4／邊緣 0.15，數值＝log-odds 合成權重），語義為
  「此分支證偽時對整體論點的承諾後果」
- `verdicts_current.json` · `verdict_transitions.jsonl` — 每條子假說
  （僅 ID）的當前判定與全部歷史轉變（date / from / to）；`recode: true`
  標記方法論重新編碼（非市場事件），計算預測力時應剔除

**校準（`calibration/`）——alpha 研究資料集**
- `CALIBRATION.md` — 結果表：超額回報曲線（1–8 週）、降級×等級、
  轉變廣度×cascade、permutation 檢定；每次出口自動重算
- `events.csv`（schema v2）— 一行一個判定轉變事件：等級、必要葉旗、
  state 壽命、1–8 週原始＋超額回報、cluster 標記——去重、算超額、切
  feature 一表搞掂
- `clusters.csv` — 一行一個 ticker×事件週：廣度特徵（幾多葉/幾多支/
  等級加權淨變化）＋未來 28 日 cascade 結果＋cluster 層超額回報
- `SPEC.md` — 欄位字典、有效性規則、預登記分析協議、等級重校程序、
  artifact 案底（研究者由此讀起）
- `analysis.py` — 生成本頁全部數字的腳本本體（固定種子，跑同一份
  code 得同一份數）

**承諾（`commitments/{date}.json`）**
- 私有內容檔案的 SHA-256 雜湊＋私有庫 commit hash

## ✅ 如何驗證

1. **操作不可竄改**：本庫由排程自動 commit；fork/watch 本庫即可偵測任何歷史改寫。
2. **內容承諾**：若我們日後發布任何一棵樹的原文，任何人可對發布檔案計算
   SHA-256，與當日 `commitments/` 中的紀錄比對——證明內容未曾事後修改。
3. **判定變化的預測力（外部可覆核）**：我們每週在
   [`calibration/CALIBRATION.md`](calibration/CALIBRATION.md) 重算一份分組
   結果（方向×衝擊等級的前向回報），原始事件表在 `calibration/events.csv`。
   要獨立重算：以 `verdict_transitions.jsonl` 取全部轉變事件（剔除
   `recode: true`），按判定分數（✅+2／🟢+1／⚪0／🟡−1／🟠−2／🔴−3）分為升級
   與降級；以 `structure.json` 將每片葉映射到所屬分支的衝擊等級；再以任一
   公開價格來源計算事件後 1 週／4 週前瞻回報。可檢驗的預登記主張
   （RELEASES.md「首個訊號」）：降級事件的前瞻回報為負，且負向幅度隨衝擊
   等級遞增（重創支 < 明顯受損支 < 輕微支）。樣本仍少，歡迎推翻。

## ⚠️ 免責聲明

本庫全部內容僅為方法論之研究用途（含未經實證校準之數據），絕不構成任何投資建議、
要約或招攬。模擬組合使用 IBKR 模擬帳戶，不涉及真實資金。投資涉及風險，讀者應自行
判斷並承擔全部決策責任。
