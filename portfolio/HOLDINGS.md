# 💼 Kelly 持倉與交易日記（Sleeve A）

更新 2026-08-02｜數據源＝[`weekly/*.json`](weekly/)（IBKR 模擬帳戶每週journal，本頁由同一檔案確定性生成，人手零落數）｜規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md)｜研究用途，非投資建議。

倉位由樹的信念（conviction）經 fractional Kelly 決定——樹愈有把握、注碼愈大；判定轉弱，下週自動減倉。

## 目前持倉（IBKR 實倉快照 2026-07-30 09:03 UTC｜Sleeve NLV $41,232｜59 檔）

| 股票 | 股數 | 快照價 | 市值（USD） | 佔比 | 信念 | 牛／熊目標 |
|---|---:|---:|---:|---:|---:|---|
| [MSFT](../trees/MSFT/quant_history.jsonl) | 15 | USD 390.75 | 5,861 | 14.2% | 0.60 | 587／369 |
| [IBM](../trees/IBM/quant_history.jsonl) | 14 | USD 218.00 | 3,052 | 7.4% | 0.32 | 381／207 |
| [V](../trees/V/quant_history.jsonl) | 7 | USD 362.87 | 2,540 | 6.2% | 0.73 | 491／306 |
| [ADBE](../trees/ADBE/quant_history.jsonl) | 10 | USD 238.13 | 2,381 | 5.8% | 0.71 | 375／200 |
| [NOW](../trees/NOW/quant_history.jsonl) | 17 | USD 102.72 | 1,746 | 4.2% | 0.63 | 179／84 |
| [MDT](../trees/MDT/quant_history.jsonl) | 16 | USD 85.06 | 1,361 | 3.3% | 0.41 | 130／75 |
| [ETN](../trees/ETN/quant_history.jsonl) | 3 | USD 389.54 | 1,169 | 2.8% | 0.78 | 496／272 |
| [HUBS](../trees/HUBS/quant_history.jsonl) | 5 | USD 221.14 | 1,106 | 2.7% | 0.30 | 653／189 |
| [NKE](../trees/NKE/quant_history.jsonl) | 25 | USD 42.07 | 1,052 | 2.6% | 0.59 | 57／34 |
| [DDOG](../trees/DDOG/quant_history.jsonl) | 4 | USD 250.58 | 1,002 | 2.4% | 0.77 | 317／159 |
| [CVX](../trees/CVX/quant_history.jsonl) | 5 | USD 192.02 | 960 | 2.3% | 0.47 | 192／98 |
| [TYL](../trees/TYL/quant_history.jsonl) | 3 | USD 317.83 | 953 | 2.3% | 0.44 | 526／252 |
| [MDB](../trees/MDB/quant_history.jsonl) | 3 | USD 310.33 | 931 | 2.3% | 0.75 | 501／187 |
| [MU](../trees/MU/quant_history.jsonl) | 1 | USD 855.46 | 855 | 2.1% | 0.71 | 1,937／367 |
| [GLW](../trees/GLW/quant_history.jsonl) | 6 | USD 137.00 | 822 | 2.0% | 0.79 | 250／61 |
| [POET](../trees/POET/quant_history.jsonl) | 119 | USD 6.83 | 813 | 2.0% | 0.44 | 16／5 |
| [CEG](../trees/CEG/quant_history.jsonl) | 3 | USD 270.73 | 812 | 2.0% | 0.71 | 406／171 |
| [SNOW](../trees/SNOW/quant_history.jsonl) | 3 | USD 267.36 | 802 | 1.9% | 0.68 | 400／168 |
| [NVDA](../trees/NVDA/quant_history.jsonl) | 4 | USD 198.79 | 795 | 1.9% | 0.38 | 418／154 |
| [STX](../trees/STX/quant_history.jsonl) | 1 | USD 781.17 | 781 | 1.9% | 0.49 | 447／78 |
| [TSM](../trees/TSM/quant_history.jsonl) | 2 | USD 389.40 | 779 | 1.9% | 0.69 | 611／210 |
| [AMBA](../trees/AMBA/quant_history.jsonl) | 12 | USD 63.40 | 761 | 1.8% | 0.62 | 118／40 |
| [TEAM](../trees/TEAM/quant_history.jsonl) | 8 | USD 94.31 | 754 | 1.8% | 0.70 | 200／51 |
| [ADI](../trees/ADI/quant_history.jsonl) | 2 | USD 362.97 | 726 | 1.8% | 0.67 | 624／215 |
| [ISRG](../trees/ISRG/quant_history.jsonl) | 2 | USD 355.95 | 712 | 1.7% | 0.67 | 608／212 |
| [INTC](../trees/INTC/quant_history.jsonl) | 8 | USD 87.38 | 699 | 1.7% | 0.74 | 186／38 |
| [UBER](../trees/UBER/quant_history.jsonl) | 10 | USD 66.49 | 665 | 1.6% | 0.30 | 123／56 |
| [UUUU](../trees/UUUU/quant_history.jsonl) | 58 | USD 11.38 | 660 | 1.6% | 0.57 | 20／7 |
| [GOOGL](../trees/GOOGL/quant_history.jsonl) | 2 | USD 325.56 | 651 | 1.6% | 0.29 | 501／276 |
| [CHYM](../trees/CHYM/quant_history.jsonl) | 30 | USD 21.27 | 638 | 1.5% | 0.58 | 39／14 |
| [META](../trees/META/quant_history.jsonl) | 1 | USD 602.25 | 602 | 1.5% | 0.69 | 918／286 |
| [CRDO](../trees/CRDO/quant_history.jsonl) | 3 | USD 197.84 | 594 | 1.4% | 0.45 | 469／94 |
| [BABA](../trees/BABA/quant_history.jsonl) | 5 | USD 112.96 | 565 | 1.4% | 0.68 | 176／61 |
| [HOOD](../trees/HOOD/quant_history.jsonl) | 6 | USD 93.62 | 562 | 1.4% | 0.85 | 125／33 |
| [MRVL](../trees/MRVL/quant_history.jsonl) | 3 | USD 183.29 | 550 | 1.3% | 0.62 | 298／88 |
| [CRM](../trees/CRM/quant_history.jsonl) | 3 | USD 173.03 | 519 | 1.3% | 0.45 | 261／131 |
| [COHR](../trees/COHR/quant_history.jsonl) | 2 | USD 257.51 | 515 | 1.2% | 0.60 | 478／124 |
| [FUTU](../trees/FUTU/quant_history.jsonl) | 5 | USD 102.51 | 513 | 1.2% | 0.51 | 177／67 |
| [AMD](../trees/AMD/quant_history.jsonl) | 1 | USD 479.24 | 479 | 1.2% | 0.65 | 960／210 |
| [AMZN](../trees/AMZN/quant_history.jsonl) | 2 | USD 234.09 | 468 | 1.1% | 0.51 | 346／170 |
| [ACN](../trees/ACN/quant_history.jsonl) | 3 | USD 154.36 | 463 | 1.1% | 0.48 | 258／104 |
| [UNH](../trees/UNH/quant_history.jsonl) | 1 | USD 417.47 | 417 | 1.0% | 0.73 | 504／225 |
| [APP](../trees/APP/quant_history.jsonl) | 1 | USD 403.07 | 403 | 1.0% | 0.33 | 922／242 |
| [PM](../trees/PM/quant_history.jsonl) | 2 | USD 196.16 | 392 | 1.0% | 0.41 | 262／159 |
| [AAOI](../trees/AAOI/quant_history.jsonl) | 4 | USD 92.61 | 370 | 0.9% | 0.58 | 185／43 |
| [OKLO](../trees/OKLO/quant_history.jsonl) | 9 | USD 40.46 | 364 | 0.9% | 0.37 | 126／24 |
| [TTD](../trees/TTD/quant_history.jsonl) | 19 | USD 17.87 | 340 | 0.8% | 0.26 | 46／13 |
| [AAPL](../trees/AAPL/quant_history.jsonl) | 1 | USD 337.69 | 338 | 0.8% | 0.79 | 391／187 |
| [ONDS](../trees/ONDS/quant_history.jsonl) | 39 | USD 7.81 | 305 | 0.7% | 0.68 | 8／3 |
| [NOK](../trees/NOK/quant_history.jsonl) | 33 | USD 8.93 | 295 | 0.7% | 0.38 | 33／4 |
| [ALAB](../trees/ALAB/quant_history.jsonl) | 1 | USD 270.02 | 270 | 0.7% | 0.59 | 493／123 |
| [ON](../trees/ON/quant_history.jsonl) | 3 | USD 85.11 | 255 | 0.6% | 0.60 | 123／48 |
| [PDD](../trees/PDD/quant_history.jsonl) | 3 | USD 84.34 | 253 | 0.6% | 0.28 | 154／64 |
| [XE](../trees/XE/quant_history.jsonl) | 16 | USD 13.88 | 222 | 0.5% | 0.44 | 25／8 |
| [NBIS](../trees/NBIS/quant_history.jsonl) | 1 | USD 185.16 | 185 | 0.4% | 0.33 | 741／52 |
| [PLTR](../trees/PLTR/quant_history.jsonl) | 1 | USD 127.06 | 127 | 0.3% | 0.64 | 176／53 |
| [HPQ](../trees/HPQ/quant_history.jsonl) | 4 | USD 26.05 | 104 | 0.3% | 0.33 | 40／20 |
| [SMR](../trees/SMR/quant_history.jsonl) | 8 | USD 8.16 | 65 | 0.2% | 0.30 | 22／4 |
| [000660.KS](../trees/000660.KS/quant_history.jsonl) | 26 | — | — | — | — | — |

持倉市值合計 ≈ $47,377（另有現金；快照價為名單日收市，未逐日重估）。無快照價者為當週不在名單內的存倉。

## 交易日記（新在前）

旗標說明：λ 折減＝原始 Kelly 注碼按規則折減；上限封頂＝觸及單一持倉上限；低於交易門檻＝目標與現況差距太小，不動。

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
