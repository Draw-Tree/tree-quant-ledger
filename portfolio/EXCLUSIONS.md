# 🚫 剔除紀錄

`更新 2026-07-30`

列入名單、但不入建倉籃的個案。名單帳本 [`verdict_watch.jsonl`](verdict_watch.jsonl) 一經寫入永不改動，計分板亦仍按原名單計分——剔除影響的只是實際建倉。

| 名單日 | 股票 | 裁定 | 原因 |
|---|---|---|---|
| `2026-07-26` | **NET** | 2026-07-27・maintainer | [判定與自身條件紀錄矛盾，且證據重複計算](#net-20260726) |
| `2026-07-26` | **IFNNY** | 2026-07-27・maintainer | [改判所引來源在帳本中不存在，而帳本唯一對題的證據反駁該假說](#ifnny-20260726) |
| `2026-07-26` | **CEG** | 2026-07-27・maintainer | [支撐改判的唯一證據不可查證，且該葉自身的條件評估否定其說法](#ceg-20260726) |

<a id="net-20260726"></a>

## NET　_判定與自身條件紀錄矛盾，且證據重複計算_

名單日 `2026-07-26`　2026-07-27 由maintainer裁定

1. NET 本週訊號完全來自單一片葉 A3（致命級，訊號 -2.5）。
2. 該葉 07-25 由『接近證偽』改判『已證偽』，理由為『Google 已於 2026 年 4 月推出 Gemini Enterprise Agent Platform 及其 Agent Gateway，直接滿足證偽條件 A3-F1』。
3. 但同一件事實已於 06-06 用作『已確認→接近證偽』的理由。同一單證據推動了兩次連續降級，中間並無新資料入帳（lag_days=53）。
4. 更關鍵：該葉自身的結構化欄位與判定互相矛盾——conditions[A3-F1].status='open'、condition_assessments[A3-F1]='approaching'，而判定理由卻聲稱該條件『直接滿足』並落至 Falsified。
5. 全庫同類矛盾共 14 片葉（判定落證偽區、但無任何一條證偽條件評為 met）。本次僅處置 NET；ISRG B1 有同一矛盾但 lag_days=9（證據新鮮，屬條件欄位未同步而非重複計算），TSLA B2 亦有但該檔本週為 mixed，本就不入籃。

<a id="ifnny-20260726"></a>

## IFNNY　_改判所引來源在帳本中不存在，而帳本唯一對題的證據反駁該假說_

名單日 `2026-07-26`　2026-07-27 由maintainer裁定

1. IFNNY 本週訊號完全來自單一片葉 C3（重創級，訊號 +1.6）。該葉命題為「外部產業證據」——外部研究機構是否已將 Infineon 歸類為 AI 電源基礎設施公司，而非傳統功率半導體供應商。
2. 07-25 由「強化中」改判「已確認」，理由為「Gartner 2026 年 6 月報告將 Infineon 列為 AI Data Center Power Semiconductors『the company to beat』」。
3. 該 Gartner 報告在帳本中完全不存在：全檔提及 Gartner 僅兩處，皆在 conclusion 與 verdict_history 的理由文字內，evidence_ledger 與 recent_evidence 皆無任何對應證據行。改判引用了一個從未入帳的來源。
4. 帳本唯一對題的證據行 E003 反駁該假說：「外部產業報告仍主要將 Infineon 歸類為『全球功率半導體絕對領導者』（IGBT/MOSFET/SiC 全線），而非專門歸類為 AI 電源基礎設施公司」。該行卻被標為 impact=supports。
5. E003 的內容正好滿足該葉自己的證偽條件 C3-F2：「外部研究機構持續將 Infineon 歸類為傳統車用/工業半導體供應商而非 AI 基礎設施公司」。條件 status 仍為 open，且 condition_assessments 整個為空——兩條證偽條件一條都未評估。
6. 三條證據行皆無 URL，來源署名為「Industry research」「Market research」「Industry report」，無一具名可查；recent_evidence 為空，即本週搜索對該葉一無所獲。
7. 與 CEG 的分別：CEG 的問題是一條被捏造出來支持判定的證據行；IFNNY 的問題是判定引用了一個根本不在帳本的來源，而帳本內唯一對題的證據指向相反方向並已滿足證偽條件。後者更嚴重。
8. Rule 1b（本日新增）會攔下此類改判——該葉 3 條證據 0 條可查證。E2 擴至 met 之後，若 C3-F2 被如實評為 met，亦會觸發「證偽條件成立而判定仍為正面」之錯誤。

<a id="ceg-20260726"></a>

## CEG　_支撐改判的唯一證據不可查證，且該葉自身的條件評估否定其說法_

名單日 `2026-07-26`　2026-07-27 由maintainer裁定

1. CEG 本週訊號完全來自單一片葉 C2（致命級，訊號 +2.5）。
2. 該葉 07-25 由『減弱中』改判『已確認』，理由為『CEG 於 2026-06-25 簽署第三筆 1.2 GW 超大型科技公司核電 PPA』，所引證據為 E004。
3. E004 不可查證：url 為空，source_name 為『AWARE / industry press』——既非公司、亦非具名刊物，無從覆核。同批遷移新增的 19 條無 URL 證據中，其餘 18 條皆指向可查證來源（Accenture Q3 FY26 earnings、TSMC Q1 2026 Results、Tesla Q1 2026 Update 等具名財報，以及 5 條 deadline_clock 機器合成行）；E004 是唯一一條無法覆核者。
4. E004 並非由每週新聞管道寫入，而是 2026-07-11 commit 6884d88b（§8 fleet migration）由本專案自己派出的遷移 agent 寫入。該 commit 訊息自述『fulfilled deadlines marked met with positive retained (ONDS A1, PLTR C2, CEG C2)』——即 agent 為了把 C2-F1 標為 met，同時寫入一條支持該標記的證據。責任在本專案，不在資料來源。
5. 該葉自身的條件評估否定了改判理由：condition_assessments[C2-F1] 寫『截至 2026 年 7 月 18 日（Q3 前），CEG 未宣布新 PPA』，與改判理由所稱『2026-06-25 已簽署第三筆』直接矛盾，而兩者出自同一次判讀。
6. 維護者以領域知識獨立提出同一質疑：市場上並無第三家 hyperscaler 與 CEG 簽署核電 PPA 的公開宣布。
7. §8 E2 閘未能攔截：E2 只檢查 status ∈ {breached, expired_unfulfilled}，而 C2-F1 的 status 為 met。對一條描述失敗情境的條件而言，met 與 breached 同屬壞消息，E2 的集合定義有缺口。
