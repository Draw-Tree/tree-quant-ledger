# 💼 Kelly 持倉與交易日記（Sleeve A）

更新 2026-08-04｜數據源＝[`weekly/*.json`](weekly/)（IBKR 模擬帳戶每週journal，本頁由同一檔案確定性生成，人手零落數）｜規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md)｜研究用途，非投資建議。

倉位由樹的信念（conviction）經 fractional Kelly 決定——樹愈有把握、注碼愈大；判定轉弱，下週自動減倉。

## 目前持倉（IBKR 實倉快照 2026-08-03 16:17 UTC｜Sleeve NLV $42,371｜61 檔）

| 股票 | 股數 | 快照價 | 市值（USD） | 佔比 | 信念 | 牛／熊目標 |
|---|---:|---:|---:|---:|---:|---|
| [IBM](../trees/IBM/quant_history.jsonl) | 14 | USD 225.51 | 3,157 | 7.5% | 0.32 | 381／211 |
| [V](../trees/V/quant_history.jsonl) | 7 | USD 368.29 | 2,578 | 6.1% | 0.74 | 491／306 |
| [ADBE](../trees/ADBE/quant_history.jsonl) | 10 | USD 253.67 | 2,537 | 6.0% | 0.74 | 375／200 |
| [NKE](../trees/NKE/quant_history.jsonl) | 37 | USD 42.42 | 1,570 | 3.7% | 0.59 | 57／34 |
| [MSFT](../trees/MSFT/quant_history.jsonl) | 3 | USD 486.81 | 1,460 | 3.4% | 0.68 | 587／369 |
| [MDT](../trees/MDT/quant_history.jsonl) | 16 | USD 86.21 | 1,379 | 3.3% | 0.42 | 130／75 |
| [ETN](../trees/ETN/quant_history.jsonl) | 3 | USD 432.09 | 1,296 | 3.1% | 0.84 | 496／272 |
| [HUBS](../trees/HUBS/quant_history.jsonl) | 5 | USD 245.03 | 1,225 | 2.9% | 0.33 | 653／189 |
| [DDOG](../trees/DDOG/quant_history.jsonl) | 4 | USD 274.13 | 1,097 | 2.6% | 0.83 | 317／159 |
| [VST](../trees/VST/quant_history.jsonl) | 7 | USD 151.70 | 1,062 | 2.5% | 0.34 | 261／129 |
| [MDB](../trees/MDB/quant_history.jsonl) | 3 | USD 349.98 | 1,050 | 2.5% | 0.79 | 501／187 |
| [CVX](../trees/CVX/quant_history.jsonl) | 5 | USD 194.33 | 972 | 2.3% | 0.49 | 192／98 |
| [SNOW](../trees/SNOW/quant_history.jsonl) | 3 | USD 311.26 | 934 | 2.2% | 0.75 | 400／168 |
| [TYL](../trees/TYL/quant_history.jsonl) | 3 | USD 311.03 | 933 | 2.2% | 0.43 | 526／252 |
| [GLW](../trees/GLW/quant_history.jsonl) | 6 | USD 143.75 | 862 | 2.0% | 0.81 | 250／61 |
| [POET](../trees/POET/quant_history.jsonl) | 119 | USD 7.20 | 856 | 2.0% | 0.45 | 16／5 |
| [TEAM](../trees/TEAM/quant_history.jsonl) | 8 | USD 103.84 | 831 | 2.0% | 0.72 | 200／51 |
| [NVDA](../trees/NVDA/quant_history.jsonl) | 4 | USD 206.11 | 824 | 1.9% | 0.40 | 418／154 |
| [STX](../trees/STX/quant_history.jsonl) | 1 | USD 820.29 | 820 | 1.9% | 0.49 | 447／78 |
| [MU](../trees/MU/quant_history.jsonl) | 1 | USD 816.51 | 817 | 1.9% | 0.70 | 1,937／367 |
| [NOW](../trees/NOW/quant_history.jsonl) | 7 | USD 115.98 | 812 | 1.9% | 0.52 | 179／84 |
| [CEG](../trees/CEG/quant_history.jsonl) | 3 | USD 270.13 | 810 | 1.9% | 0.71 | 406／171 |
| [TSM](../trees/TSM/quant_history.jsonl) | 2 | USD 404.08 | 808 | 1.9% | 0.70 | 611／210 |
| [ISRG](../trees/ISRG/quant_history.jsonl) | 2 | USD 371.34 | 743 | 1.8% | 0.68 | 608／212 |
| [GOOGL](../trees/GOOGL/quant_history.jsonl) | 2 | USD 368.09 | 736 | 1.7% | 0.37 | 501／276 |
| [ADI](../trees/ADI/quant_history.jsonl) | 2 | USD 362.10 | 724 | 1.7% | 0.67 | 624／215 |
| [INTC](../trees/INTC/quant_history.jsonl) | 8 | USD 89.96 | 720 | 1.7% | 0.75 | 186／38 |
| [CHYM](../trees/CHYM/quant_history.jsonl) | 30 | USD 23.86 | 716 | 1.7% | 0.62 | 39／14 |
| [UBER](../trees/UBER/quant_history.jsonl) | 10 | USD 71.37 | 714 | 1.7% | 0.33 | 123／56 |
| [UUUU](../trees/UUUU/quant_history.jsonl) | 58 | USD 11.88 | 689 | 1.6% | 0.59 | 20／7 |
| [BABA](../trees/BABA/quant_history.jsonl) | 5 | USD 128.01 | 640 | 1.5% | 0.72 | 176／61 |
| [CRDO](../trees/CRDO/quant_history.jsonl) | 3 | USD 207.55 | 623 | 1.5% | 0.46 | 469／94 |
| [AAPL](../trees/AAPL/quant_history.jsonl) | 2 | USD 305.68 | 611 | 1.4% | 0.74 | 391／187 |
| [AMBA](../trees/AMBA/quant_history.jsonl) | 7 | USD 84.11 | 589 | 1.4% | 0.72 | 118／40 |
| [META](../trees/META/quant_history.jsonl) | 1 | USD 585.50 | 586 | 1.4% | 0.68 | 918／286 |
| [AMZN](../trees/AMZN/quant_history.jsonl) | 2 | USD 285.26 | 571 | 1.3% | 0.60 | 346／170 |
| [COHR](../trees/COHR/quant_history.jsonl) | 2 | USD 284.88 | 570 | 1.3% | 0.57 | 478／124 |
| [CRM](../trees/CRM/quant_history.jsonl) | 3 | USD 189.01 | 567 | 1.3% | 0.51 | 261／131 |
| [MRVL](../trees/MRVL/quant_history.jsonl) | 3 | USD 188.67 | 566 | 1.3% | 0.63 | 298／88 |
| [HOOD](../trees/HOOD/quant_history.jsonl) | 6 | USD 90.70 | 544 | 1.3% | 0.84 | 125／33 |
| [FUTU](../trees/FUTU/quant_history.jsonl) | 5 | USD 105.19 | 526 | 1.2% | 0.52 | 177／67 |
| [ACN](../trees/ACN/quant_history.jsonl) | 3 | USD 167.03 | 501 | 1.2% | 0.52 | 258／104 |
| [AMD](../trees/AMD/quant_history.jsonl) | 1 | USD 479.53 | 480 | 1.1% | 0.65 | 960／210 |
| [AAOI](../trees/AAOI/quant_history.jsonl) | 4 | USD 104.98 | 420 | 1.0% | 0.61 | 185／43 |
| [UNH](../trees/UNH/quant_history.jsonl) | 1 | USD 416.20 | 416 | 1.0% | 0.73 | 504／225 |
| [APP](../trees/APP/quant_history.jsonl) | 1 | USD 405.50 | 406 | 1.0% | 0.33 | 922／242 |
| [PM](../trees/PM/quant_history.jsonl) | 2 | USD 189.89 | 380 | 0.9% | 0.38 | 262／159 |
| [OKLO](../trees/OKLO/quant_history.jsonl) | 9 | USD 41.13 | 370 | 0.9% | 0.37 | 126／24 |
| [TTD](../trees/TTD/quant_history.jsonl) | 19 | USD 18.45 | 351 | 0.8% | 0.27 | 46／13 |
| [ONDS](../trees/ONDS/quant_history.jsonl) | 39 | USD 8.12 | 317 | 0.7% | 0.70 | 8／3 |
| [ALAB](../trees/ALAB/quant_history.jsonl) | 1 | USD 310.26 | 310 | 0.7% | 0.63 | 493／123 |
| [NOK](../trees/NOK/quant_history.jsonl) | 33 | USD 9.20 | 304 | 0.7% | 0.38 | 33／4 |
| [QCOM](../trees/QCOM/quant_history.jsonl) | 2 | USD 148.40 | 297 | 0.7% | 0.28 | 281／118 |
| [XE](../trees/XE/quant_history.jsonl) | 16 | USD 17.82 | 285 | 0.7% | 0.57 | 25／8 |
| [PDD](../trees/PDD/quant_history.jsonl) | 3 | USD 89.57 | 269 | 0.6% | 0.31 | 154／64 |
| [ON](../trees/ON/quant_history.jsonl) | 3 | USD 82.22 | 247 | 0.6% | 0.57 | 123／48 |
| [NBIS](../trees/NBIS/quant_history.jsonl) | 1 | USD 208.56 | 209 | 0.5% | 0.35 | 741／52 |
| [PLTR](../trees/PLTR/quant_history.jsonl) | 1 | USD 125.29 | 125 | 0.3% | 0.63 | 176／53 |
| [HPQ](../trees/HPQ/quant_history.jsonl) | 4 | USD 27.21 | 109 | 0.3% | 0.35 | 40／20 |
| [SMR](../trees/SMR/quant_history.jsonl) | 8 | USD 8.95 | 72 | 0.2% | 0.31 | 22／4 |
| [000660.KS](../trees/000660.KS/quant_history.jsonl) | 28 | — | — | — | — | — |

持倉市值合計 ≈ $45,989（另有現金；快照價為名單日收市，未逐日重估）。無快照價者為當週不在名單內的存倉。

## 交易日記（新在前）

旗標說明：λ 折減＝原始 Kelly 注碼按規則折減；上限封頂＝觸及單一持倉上限；低於交易門檻＝目標與現況差距太小，不動。

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
