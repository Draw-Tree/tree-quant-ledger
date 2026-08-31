# 💼 持倉與交易日記（Sleeve A Kelly ＋ Sleeve B 長短倉）

更新 2026-08-31｜數據源＝[`weekly/*.json`](weekly/)（IBKR 模擬帳戶每週journal，本頁由同一檔案確定性生成，人手零落數）｜規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md)｜研究用途，非投資建議。

倉位由樹的信念（conviction）經 fractional Kelly 決定——樹愈有把握、注碼愈大；判定轉弱，下週自動減倉。

自 2026-08-31 起 Sleeve A 為**理論帳**：實驗帳戶已轉為只執行訊號跟隨策略，本 sleeve 每週照舊計算 Kelly 目標書並以週一開市口徑入帳，但不再向券商落單；下表即理論書全部部位。

## 目前持倉（理論帳，截至 2026-08-31｜Sleeve NAV $43,917｜53 檔）

| 股票 | 股數 | 快照價 | 市值（USD） | 佔比 | 信念 | 牛／熊目標 |
|---|---:|---:|---:|---:|---:|---|
| [VST](../trees/VST/quant_history.jsonl) | 35 | USD 137.09 | 4,798 | 10.9% | 0.37 | 261／129 |
| [TTD](../trees/TTD/quant_history.jsonl) | 229 | USD 13.57 | 3,108 | 7.1% | 0.21 | 46／13 |
| [V](../trees/V/quant_history.jsonl) | 7 | USD 381.60 | 2,671 | 6.1% | 0.77 | 491／306 |
| [NKE](../trees/NKE/quant_history.jsonl) | 65 | USD 39.60 | 2,574 | 5.9% | 0.55 | 57／34 |
| [IBM](../trees/IBM/quant_history.jsonl) | 8 | USD 235.59 | 1,885 | 4.3% | 0.35 | 381／211 |
| [ADBE](../trees/ADBE/quant_history.jsonl) | 5 | USD 291.52 | 1,458 | 3.3% | 0.78 | 375／200 |
| [DDOG](../trees/DDOG/quant_history.jsonl) | 5 | USD 236.98 | 1,185 | 2.7% | 0.75 | 317／159 |
| [BRK-B](../trees/BRK-B/quant_history.jsonl) | 2 | USD 505.00 | 1,010 | 2.3% | 0.55 | 631／408 |
| [GLW](../trees/GLW/quant_history.jsonl) | 6 | USD 148.98 | 894 | 2.0% | 0.82 | 250／61 |
| [CEG](../trees/CEG/quant_history.jsonl) | 3 | USD 276.75 | 830 | 1.9% | 0.69 | 406／171 |
| [MDT](../trees/MDT/quant_history.jsonl) | 9 | USD 91.23 | 821 | 1.9% | 0.46 | 130／75 |
| [ETN](../trees/ETN/quant_history.jsonl) | 2 | USD 402.78 | 806 | 1.8% | 0.76 | 496／272 |
| [INTC](../trees/INTC/quant_history.jsonl) | 9 | USD 89.47 | 805 | 1.8% | 0.75 | 186／38 |
| [HUBS](../trees/HUBS/quant_history.jsonl) | 3 | USD 260.68 | 782 | 1.8% | 0.34 | 653／189 |
| [TXN](../trees/TXN/quant_history.jsonl) | 3 | USD 258.64 | 776 | 1.8% | 0.61 | 360／187 |
| [ISRG](../trees/ISRG/quant_history.jsonl) | 2 | USD 372.60 | 745 | 1.7% | 0.69 | 608／212 |
| [ADI](../trees/ADI/quant_history.jsonl) | 2 | USD 361.78 | 724 | 1.6% | 0.67 | 624／215 |
| [AMBA](../trees/AMBA/quant_history.jsonl) | 10 | USD 70.63 | 706 | 1.6% | 0.67 | 118／40 |
| [NVDA](../trees/NVDA/quant_history.jsonl) | 3 | USD 217.55 | 653 | 1.5% | 0.38 | 418／154 |
| [AAPL](../trees/AAPL/quant_history.jsonl) | 2 | USD 319.70 | 639 | 1.5% | 0.77 | 391／187 |
| [BABA](../trees/BABA/quant_history.jsonl) | 5 | USD 118.90 | 594 | 1.4% | 0.70 | 176／61 |
| [POET](../trees/POET/quant_history.jsonl) | 79 | USD 7.50 | 592 | 1.3% | 0.46 | 16／5 |
| [META](../trees/META/quant_history.jsonl) | 1 | USD 578.02 | 578 | 1.3% | 0.67 | 918／286 |
| [PM](../trees/PM/quant_history.jsonl) | 3 | USD 191.89 | 576 | 1.3% | 0.39 | 262／159 |
| [AMKR](../trees/AMKR/quant_history.jsonl) | 12 | USD 47.88 | 575 | 1.3% | 0.30 | 106／38 |
| [HOOD](../trees/HOOD/quant_history.jsonl) | 5 | USD 104.26 | 521 | 1.2% | 0.89 | 125／33 |
| [MSFT](../trees/MSFT/quant_history.jsonl) | 1 | USD 513.53 | 514 | 1.2% | 0.72 | 587／369 |
| [ON](../trees/ON/quant_history.jsonl) | 7 | USD 72.61 | 508 | 1.2% | 0.50 | 123／48 |
| [OKLO](../trees/OKLO/quant_history.jsonl) | 12 | USD 40.14 | 482 | 1.1% | 0.38 | 126／24 |
| [AMD](../trees/AMD/quant_history.jsonl) | 1 | USD 465.58 | 466 | 1.1% | 0.66 | 960／210 |
| [MDB](../trees/MDB/quant_history.jsonl) | 1 | USD 446.62 | 447 | 1.0% | 0.90 | 501／187 |
| [NOW](../trees/NOW/quant_history.jsonl) | 3 | USD 144.71 | 434 | 1.0% | 0.68 | 179／84 |
| [TSM](../trees/TSM/quant_history.jsonl) | 1 | USD 417.52 | 418 | 1.0% | 0.71 | 611／210 |
| [UNH](../trees/UNH/quant_history.jsonl) | 1 | USD 392.95 | 393 | 0.9% | 0.69 | 504／225 |
| [TEAM](../trees/TEAM/quant_history.jsonl) | 2 | USD 190.41 | 381 | 0.9% | 0.92 | 200／51 |
| [TYL](../trees/TYL/quant_history.jsonl) | 1 | USD 377.94 | 378 | 0.9% | 0.52 | 526／252 |
| [NOK](../trees/NOK/quant_history.jsonl) | 34 | USD 10.21 | 347 | 0.8% | 0.40 | 33／4 |
| [QCOM](../trees/QCOM/quant_history.jsonl) | 2 | USD 164.19 | 328 | 0.7% | 0.37 | 281／118 |
| [SNOW](../trees/SNOW/quant_history.jsonl) | 1 | USD 328.00 | 328 | 0.7% | 0.77 | 400／168 |
| [APP](../trees/APP/quant_history.jsonl) | 1 | USD 317.76 | 318 | 0.7% | 0.24 | 922／242 |
| [ALAB](../trees/ALAB/quant_history.jsonl) | 1 | USD 289.47 | 289 | 0.7% | 0.59 | 493／123 |
| [COHR](../trees/COHR/quant_history.jsonl) | 1 | USD 279.20 | 279 | 0.6% | 0.57 | 478／124 |
| [FUTU](../trees/FUTU/quant_history.jsonl) | 2 | USD 124.26 | 249 | 0.6% | 0.61 | 177／67 |
| [CRDO](../trees/CRDO/quant_history.jsonl) | 1 | USD 232.75 | 233 | 0.5% | 0.50 | 469／94 |
| [MRVL](../trees/MRVL/quant_history.jsonl) | 1 | USD 216.62 | 217 | 0.5% | 0.70 | 298／88 |
| [NBIS](../trees/NBIS/quant_history.jsonl) | 1 | USD 209.18 | 209 | 0.5% | 0.37 | 741／52 |
| [SKHY](../trees/SKHY/quant_history.jsonl) | 1 | USD 161.04 | 161 | 0.4% | 0.72 | 259／22 |
| [UBER](../trees/UBER/quant_history.jsonl) | 2 | USD 78.82 | 158 | 0.4% | 0.37 | 123／56 |
| [UUUU](../trees/UUUU/quant_history.jsonl) | 10 | USD 14.67 | 147 | 0.3% | 0.66 | 20／7 |
| [AAOI](../trees/AAOI/quant_history.jsonl) | 1 | USD 106.23 | 106 | 0.2% | 0.61 | 185／43 |
| [PDD](../trees/PDD/quant_history.jsonl) | 1 | USD 85.69 | 86 | 0.2% | 0.28 | 154／64 |
| [PENG](../trees/PENG/quant_history.jsonl) | 1 | USD 49.51 | 50 | 0.1% | 0.28 | 85／37 |
| [XE](../trees/XE/quant_history.jsonl) | 2 | USD 17.22 | 34 | 0.1% | 0.56 | 25／8 |

持倉市值合計 ≈ $39,263（另有現金；快照價為名單日收市，未逐日重估）。無快照價者為當週不在名單內的存倉。

## Sleeve B 長短倉

全數腿於 2026-08-28 隨帳戶重置平倉（maintainer_account_reset）；Sleeve B 結案，往後不再開倉。

## 交易日記（新在前）

旗標說明：λ 折減＝原始 Kelly 注碼按規則折減；上限封頂＝觸及單一持倉上限；低於交易門檻＝目標與現況差距太小，不動。

### 2026-08-31（NLV $43,917｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🔴 賣出 | VST | 5 | 137.09 | 717 | 10.8% | 0.37 | λ 折減 | 理論入帳 |
| 🟢 買入 | TTD | 229 | 13.57 | 3,113 | 7.1% | 0.21 | λ 折減 | 理論入帳 |
| 🟢 買入 | NKE | 12 | 39.60 | 513 | 5.9% | 0.55 | λ 折減 | 理論入帳 |
| 🔴 賣出 | ADBE | 2 | 291.52 | 593 | 3.3% | 0.78 | λ 折減 | 理論入帳 |
| 🔴 賣出 | MSFT | 1 | 513.53 | 523 | 1.1% | 0.72 | λ 折減 | 理論入帳 |
| 🟢 買入 | MRVL | 1 | 216.62 | 0 | 0.7% | 0.70 | — | 理論入帳 |
| 🟢 買入 | PENG | 1 | 49.51 | 0 | 0.2% | 0.28 | — | 理論入帳 |
| 🟢 買入 | XE | 2 | 17.22 | 0 | 0.1% | 0.56 | — | 理論入帳 |

### 2026-08-24（NLV $43,722｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | VST | 26 | 0.00 | 3,658 | 12.7% | 0.36 | λ 折減 | PreSubmitted |
| 🔴 賣出 | ADBE | 2 | 0.00 | 825 | 4.4% | 0.78 | λ 折減 | PreSubmitted |
| 🟢 買入 | BRK-B | 2 | 0.00 | 1,134 | 2.6% | 0.53 | λ 折減 | Cancelled |
| 🔴 賣出 | MDT | 6 | 0.00 | 592 | 2.1% | 0.48 | λ 折減 | PreSubmitted |
| 🟢 買入 | ETN | 2 | 0.00 | 871 | 2.0% | 0.78 | λ 折減 | PreSubmitted |
| 🔴 賣出 | TYL | 1 | 0.00 | 486 | 1.3% | 0.48 | λ 折減 | PreSubmitted |
| 🔴 賣出 | OKLO | 57 | 0.00 | 2,441 | 1.2% | 0.38 | λ 折減 | PreSubmitted |
| 🟢 買入 | UNH | 1 | 0.00 | 451 | 1.0% | 0.69 | λ 折減 | PreSubmitted |
| 🔴 賣出 | MRVL | 2 | 0.00 | 666 | 0.1% | 0.72 | λ 折減 | PreSubmitted |
| 🟢 買入 | NOW | 3 | 0.00 | 0 | 1.0% | 0.56 | — | PreSubmitted |
| 🟢 買入 | COHR | 1 | 0.00 | 0 | 0.7% | 0.58 | — | PreSubmitted |
| 🟢 買入 | SKHY | 1 | 0.00 | 0 | 0.7% | 0.73 | — | PreSubmitted |
| 🟢 買入 | UBER | 2 | 0.00 | 0 | 0.4% | 0.37 | — | PreSubmitted |

### 2026-08-17（NLV $44,749｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | V | 2 | 0.00 | 893 | 7.7% | 0.74 | λ 折減 | PreSubmitted |
| 🟢 買入 | TTD | 216 | 0.00 | 3,062 | 7.4% | 0.20 | λ 折減 | PreSubmitted |
| 🟢 買入 | NKE | 20 | 0.00 | 824 | 5.2% | 0.57 | λ 折減 | PreSubmitted |
| 🔴 賣出 | IBM | 4 | 0.00 | 1,064 | 5.0% | 0.35 | λ 折減 | PreSubmitted |
| 🟢 買入 | VST | 7 | 0.00 | 1,114 | 4.8% | 0.40 | λ 折減 | PreSubmitted |
| 🔴 賣出 | DDOG | 23 | 0.00 | 6,049 | 2.5% | 0.79 | λ 折減 | PreSubmitted |
| 🟢 買入 | BRK-B | 2 | 0.00 | 1,029 | 2.3% | 0.55 | λ 折減 | Cancelled |
| 🔴 賣出 | MSFT | 1 | 0.00 | 533 | 2.1% | 0.70 | λ 折減 | PreSubmitted |
| 🟢 買入 | TXN | 2 | 0.00 | 736 | 1.6% | 0.66 | λ 折減 | PreSubmitted |
| 🟢 買入 | NOW | 4 | 0.00 | 605 | 1.4% | 0.55 | λ 折減 | PreSubmitted |
| 🔴 賣出 | MDB | 1 | 0.00 | 802 | 1.3% | 0.92 | λ 折減 | PreSubmitted |
| 🔴 賣出 | TEAM | 4 | 0.00 | 751 | 1.2% | 0.85 | λ 折減 | PreSubmitted |
| 🔴 賣出 | SNOW | 1 | 0.00 | 506 | 1.1% | 0.77 | λ 折減 | PreSubmitted |
| 🔴 賣出 | UNH | 15 | 0.00 | 6,379 | 1.0% | 0.72 | λ 折減 | PreSubmitted |
| 🔴 賣出 | POET | 73 | 0.00 | 707 | 1.0% | 0.53 | λ 折減 | PreSubmitted |
| 🔴 賣出 | UBER | 5 | 0.00 | 449 | 0.7% | 0.35 | λ 折減 | PreSubmitted |
| 🔴 賣出 | CRDO | 2 | 0.00 | 555 | 0.5% | 0.53 | λ 折減 | PreSubmitted |
| 🔴 賣出 | GOOGL | 1 | 0.00 | 506 | 0.4% | 0.34 | λ 折減 | PreSubmitted |
| 🔴 賣出 | UUUU | 46 | 0.00 | 705 | 0.4% | 0.67 | λ 折減 | PreSubmitted |
| 🔴 賣出 | CHYM | 26 | 0.00 | 864 | 0.2% | 0.73 | λ 折減 | PreSubmitted |
| 🟢 買入 | SKHY | 1 | 0.00 | 0 | 0.7% | 0.73 | — | PreSubmitted |
| 🟢 買入 | AMKR | 4 | 0.00 | 0 | 0.6% | 0.37 | — | PreSubmitted |

### 2026-08-10（NLV $42,416｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | VST | 15 | 0.00 | 2,209 | 7.5% | 0.38 | λ 折減 | PreSubmitted |
| 🟢 買入 | V | 1 | 0.00 | 585 | 7.4% | 0.73 | λ 折減 | PreSubmitted |
| 🟢 買入 | TTD | 198 | 0.00 | 2,735 | 7.1% | 0.21 | λ 折減 | PreSubmitted |
| 🟢 買入 | HUBS | 6 | 0.00 | 1,321 | 5.6% | 0.33 | λ 折減 | PreSubmitted |
| 🔴 賣出 | ADBE | 2 | 0.00 | 643 | 4.7% | 0.76 | λ 折減 | PreSubmitted |
| 🔴 賣出 | IBM | 6 | 0.00 | 1,598 | 4.1% | 0.36 | λ 折減 | PreSubmitted |
| 🔴 賣出 | DDOG | 22 | 0.00 | 5,276 | 3.0% | 0.75 | λ 折減 | PreSubmitted |
| 🔴 賣出 | MSFT | 1 | 0.00 | 742 | 1.8% | 0.70 | λ 折減 | PreSubmitted |
| 🟢 買入 | BRK-B | 1 | 0.00 | 593 | 1.4% | 0.59 | λ 折減 | Cancelled |
| 🔴 賣出 | TEAM | 4 | 0.00 | 613 | 1.4% | 0.82 | λ 折減 | PreSubmitted |
| 🟢 買入 | NOW | 4 | 0.00 | 510 | 1.2% | 0.55 | λ 折減 | PreSubmitted |
| 🔴 賣出 | POET | 63 | 0.00 | 570 | 1.2% | 0.51 | λ 折減 | PreSubmitted |
| 🔴 賣出 | SNOW | 1 | 0.00 | 583 | 1.0% | 0.78 | λ 折減 | PreSubmitted |
| 🔴 賣出 | CHYM | 18 | 0.00 | 544 | 0.8% | 0.69 | λ 折減 | PreSubmitted |
| 🔴 賣出 | UUUU | 36 | 0.00 | 511 | 0.7% | 0.65 | λ 折減 | PreSubmitted |
| 🔴 賣出 | CRDO | 2 | 0.00 | 526 | 0.5% | 0.52 | λ 折減 | PreSubmitted |
| 🔴 賣出 | MRVL | 1 | 0.00 | 434 | 0.5% | 0.69 | λ 折減 | PreSubmitted |
| 🔴 賣出 | AAOI | 3 | 0.00 | 456 | 0.2% | 0.68 | λ 折減 | PreSubmitted |
| 🔴 賣出 | GOOGL | 1 | 0.00 | 670 | 0.1% | 0.35 | λ 折減 | PreSubmitted |
| 🟢 買入 | SKHY | 2 | 0.00 | 0 | 0.9% | 0.69 | — | PreSubmitted |
| 🟢 買入 | AMKR | 6 | 0.00 | 0 | 0.8% | 0.35 | — | PreSubmitted |

### 2026-08-03（NLV $42,371｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | NKE | 12 | 42.84 | 533 | 3.8% | 0.59 | λ 折減 | Filled |
| 🟢 買入 | VST | 7 | 153.22 | 1,113 | 2.6% | 0.34 | λ 折減 | Filled |
| 🔴 賣出 | MSFT | 12 | 481.94 | 6,285 | 2.4% | 0.68 | λ 折減 | Filled |
| 🟢 買入 | AAPL | 1 | 308.74 | 509 | 1.9% | 0.74 | λ 折減 | Filled |
| 🔴 賣出 | NOW | 10 | 114.82 | 1,168 | 1.9% | 0.52 | λ 折減 | Filled |
| 🔴 賣出 | AMBA | 5 | 83.26 | 466 | 1.3% | 0.72 | λ 折減 | Filled |
| 🟢 買入 | QCOM | 2 | 149.88 | 427 | 1.0% | 0.28 | λ 折減 | Filled |
| 🟢 買入 | SKHY | 2 | 140.49 | 0 | 0.9% | 0.69 | — | Filled |

### 2026-07-27（NLV $41,232｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🔴 賣出 | MSFT | 1 | 386.84 | 429 | 14.1% | 0.60 | λ 折減 | Filled |
| 🟢 買入 | IBM | 9 | 220.18 | 2,039 | 7.6% | 0.32 | λ 折減 | Filled |
| 🔴 賣出 | ADBE | 8 | 235.75 | 2,000 | 5.5% | 0.71 | λ 折減 | Filled |
| 🔴 賣出 | V | 4 | 359.24 | 1,741 | 5.5% | 0.73 | λ 折減 | Filled |
| 🔴 賣出 | NOW | 43 | 101.69 | 4,437 | 4.2% | 0.63 | λ 折減 | Filled |
| 🔴 賣出 | MDT | 54 | 84.21 | 4,662 | 3.1% | 0.41 | λ 折減 | Filled |
| 🔴 賣出 | ETN | 4 | 385.64 | 1,704 | 2.5% | 0.78 | λ 折減 | Filled |
| 🔴 賣出 | HUBS | 16 | 218.93 | 3,666 | 2.4% | 0.30 | λ 折減 | Filled |
| 🔴 賣出 | MDB | 2 | 307.23 | 709 | 2.0% | 0.75 | λ 折減 | Filled |
| 🔴 賣出 | POET | 130 | 6.77 | 889 | 2.0% | 0.44 | λ 折減 | Filled |
| 🔴 賣出 | CEG | 8 | 268.02 | 2,179 | 1.9% | 0.71 | λ 折減 | Filled |
| 🔴 賣出 | TYL | 4 | 314.65 | 1,493 | 1.8% | 0.44 | λ 折減 | Filled |
| 🔴 賣出 | TEAM | 11 | 93.36 | 1,074 | 1.7% | 0.70 | λ 折減 | Filled |
| 🔴 賣出 | AMBA | 193 | 62.77 | 12,290 | 1.7% | 0.62 | λ 折減 | Submitted |
| 🔴 賣出 | SNOW | 3 | 264.69 | 908 | 1.7% | 0.68 | λ 折減 | Submitted |
| 🔴 賣出 | ADI | 4 | 359.34 | 1,485 | 1.7% | 0.67 | λ 折減 | Filled |
| 🔴 賣出 | GLW | 4 | 135.63 | 678 | 1.7% | 0.79 | λ 折減 | Filled |
| 🔴 賣出 | ISRG | 7 | 352.39 | 2,517 | 1.7% | 0.67 | λ 折減 | Filled |
| 🔴 賣出 | UBER | 14 | 65.83 | 934 | 1.6% | 0.30 | λ 折減 | Filled |
| 🔴 賣出 | NVDA | 6 | 196.80 | 1,332 | 1.6% | 0.38 | λ 折減 | Filled |
| 🔴 賣出 | CHYM | 63 | 21.06 | 1,354 | 1.5% | 0.58 | λ 折減 | Filled |
| 🔴 賣出 | INTC | 21 | 86.51 | 1,918 | 1.5% | 0.74 | λ 折減 | Filled |
| 🔴 賣出 | MU | 1 | 846.91 | 1,134 | 1.4% | 0.71 | λ 折減 | Filled |
| 🔴 賣出 | TSM | 2 | 385.51 | 1,014 | 1.3% | 0.69 | λ 折減 | Filled |
| 🔴 賣出 | BABA | 9 | 111.83 | 1,070 | 1.2% | 0.68 | λ 折減 | Filled |
| 🔴 賣出 | HOOD | 8 | 92.68 | 811 | 1.2% | 0.85 | λ 折減 | Filled |
| 🔴 賣出 | FUTU | 16 | 101.48 | 1,675 | 1.2% | 0.51 | λ 折減 | Filled |
| 🔴 賣出 | AMD | 1 | 474.45 | 510 | 1.1% | 0.65 | λ 折減 | Filled |
| 🔴 賣出 | AMZN | 2 | 231.75 | 489 | 1.1% | 0.51 | λ 折減 | Filled |
| 🔴 賣出 | CRM | 9 | 171.30 | 1,655 | 1.0% | 0.45 | λ 折減 | Filled |
| 🔴 賣出 | COHR | 2 | 254.93 | 624 | 1.0% | 0.60 | λ 折減 | Filled |
| 🔴 賣出 | ACN | 17 | 152.82 | 2,684 | 1.0% | 0.48 | λ 折減 | Filled |
| 🔴 賣出 | OKLO | 14 | 40.06 | 574 | 0.9% | 0.37 | λ 折減 | Filled |
| 🔴 賣出 | GOOGL | 4 | 322.30 | 1,602 | 0.9% | 0.29 | λ 折減 | Filled |
| 🔴 賣出 | TTD | 64 | 17.69 | 1,148 | 0.8% | 0.26 | λ 折減 | Filled |
| 🔴 賣出 | NOK | 446 | 8.84 | 3,991 | 0.7% | 0.38 | λ 折減 | Filled |
| 🔴 賣出 | AAPL | 2 | 334.31 | 747 | 0.7% | 0.79 | λ 折減 | Filled |
| 🔴 賣出 | ON | 14 | 84.25 | 1,192 | 0.6% | 0.60 | λ 折減 | Filled |
| 🔴 賣出 | PM | 6 | 194.19 | 1,330 | 0.6% | 0.41 | λ 折減 | Filled |
| 🔴 賣出 | XE | 43 | 13.75 | 603 | 0.5% | 0.44 | λ 折減 | Filled |
| 🔴 賣出 | PDD | 16 | 83.50 | 1,431 | 0.4% | 0.28 | λ 折減 | Filled |
| 🔴 賣出 | APP | 1 | 399.04 | 638 | 0.4% | 0.33 | λ 折減 | Submitted |
| 🔴 賣出 | NBIS | 2 | 183.30 | 418 | 0.3% | 0.33 | λ 折減 | Filled |
| 🔴 賣出 | PLTR | 6 | 125.79 | 796 | 0.2% | 0.64 | λ 折減 | Filled |
| 🔴 賣出 | HPQ | 35 | 25.79 | 932 | 0.2% | 0.33 | λ 折減 | Filled |
| 🔴 賣出 | SMR | 74 | 8.08 | 604 | 0.2% | 0.30 | λ 折減 | Filled |
| 🟢 買入 | SKHY | 1 | 142.17 | 0 | 0.6% | 0.69 | — | Filled |

### 2026-07-20（NLV $123,923｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | SKHY | 8 | 159.31 | 1,365 | 1.1% | 0.66 | λ 折減 | Filled |
| 🟢 買入 | UNH | 1 | 423.69 | 0 | 0.3% | 0.75 | — | Filled |

### 2026-07-14（NLV $125,651｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | AMBA | 17 | 72.72 | 1,278 | 4.7% | 0.70 | λ 折減 | PreSubmitted |
| 🟢 買入 | COHR | 4 | 310.46 | 1,311 | 1.0% | 0.79 | λ 折減 | PreSubmitted |
| 🟢 買入 | AMD | 2 | 539.73 | 1,302 | 1.0% | 0.77 | λ 折減 | PreSubmitted |
| 🟢 買入 | AMZN | 4 | 249.78 | 0 | 0.9% | 0.59 | — | PreSubmitted |
| 🟢 買入 | DDOG | 4 | 262.84 | 0 | 0.9% | 0.81 | — | PreSubmitted |
| 🟢 買入 | AAPL | 3 | 320.48 | 0 | 0.9% | 0.79 | — | PreSubmitted |
| 🟢 買入 | NKE | 25 | 44.20 | 0 | 0.9% | 0.77 | — | PreSubmitted |
| 🟢 買入 | STX | 1 | 869.27 | 0 | 0.9% | 0.91 | — | PreSubmitted |
| 🟢 買入 | CVX | 5 | 184.02 | 0 | 0.9% | 0.84 | — | PreSubmitted |
| 🟢 買入 | OKLO | 23 | 46.27 | 0 | 0.8% | 0.60 | — | PreSubmitted |
| 🟢 買入 | META | 1 | 663.30 | 0 | 0.8% | 0.82 | — | PreSubmitted |
| 🟢 買入 | PLTR | 7 | 131.34 | 0 | 0.8% | 0.78 | — | PreSubmitted |
| 🟢 買入 | XE | 59 | 15.58 | 0 | 0.7% | 0.67 | — | PreSubmitted |
| 🟢 買入 | NBIS | 3 | 212.62 | 0 | 0.7% | 0.59 | — | PreSubmitted |
| 🟢 買入 | CRDO | 3 | 239.25 | 0 | 0.7% | 0.68 | — | PreSubmitted |
| 🟢 買入 | MRVL | 3 | 219.71 | 0 | 0.6% | 0.68 | — | PreSubmitted |
| 🟢 買入 | AAOI | 7 | 113.00 | 0 | 0.6% | 0.65 | — | PreSubmitted |
| 🟢 買入 | UUUU | 58 | 13.18 | 0 | 0.6% | 0.66 | — | PreSubmitted |
| 🟢 買入 | SMR | 82 | 8.43 | 0 | 0.5% | 0.55 | — | PreSubmitted |
| 🟢 買入 | ALAB | 1 | 365.67 | 0 | 0.4% | 0.73 | — | PreSubmitted |
| 🟢 買入 | ENPH | 6 | 43.49 | 0 | 0.2% | 0.65 | — | PreSubmitted |
| 🟢 買入 | ONDS | 39 | 7.03 | 0 | 0.2% | 0.57 | — | PreSubmitted |

### 2026-07-13（NLV $127,368｜Kelly 分數 0.5｜單倉上限 0.33）

| 動作 | 股票 | 股數 | 限價 | 金額（USD） | 目標權重 | 信念 | 旗標 | 狀態 |
|---|---|---:|---:|---:|---:|---:|---|---|
| 🟢 買入 | SMSN | 37 | 4,494.50 | 7,204 | 5.7% | 0.57 | λ 折減 | Cancelled |
| 🟢 買入 | SKHY | 1 | 155.42 | 1,657 | 1.3% | 0.75 | λ 折減 | Filled |
| 🟢 買入 | APP | 2 | 449.15 | 1,288 | 1.0% | 0.62 | λ 折減 | Filled |

---

驗證：本頁任何數字皆可對照 [`weekly/*.json`](weekly/) 原始 journal 逐筆重算；成交與帳戶實況另有 reconcile／exec_audit 稽核（見 [`RELEASES.md`](RELEASES.md)）。
