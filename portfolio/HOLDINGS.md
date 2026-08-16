# 💼 Kelly 持倉與交易日記（Sleeve A）

更新 2026-08-16｜數據源＝[`weekly/*.json`](weekly/)（IBKR 模擬帳戶每週journal，本頁由同一檔案確定性生成，人手零落數）｜規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md)｜研究用途，非投資建議。

倉位由樹的信念（conviction）經 fractional Kelly 決定——樹愈有把握、注碼愈大；判定轉弱，下週自動減倉。

## 目前持倉（IBKR 實倉快照 2026-08-10 15:48 UTC｜Sleeve NLV $42,416｜61 檔）

| 股票 | 股數 | 快照價 | 市值（USD） | 佔比 | 信念 | 牛／熊目標 |
|---|---:|---:|---:|---:|---:|---|
| [XE](../trees/XE/quant_history.jsonl) | 398 | USD 22.65 | 9,015 | 21.3% | 0.67 | 25／8 |
| [CVX](../trees/CVX/quant_history.jsonl) | 40 | USD 186.56 | 7,462 | 17.6% | 0.89 | 192／98 |
| [DDOG](../trees/DDOG/quant_history.jsonl) | 28 | USD 233.93 | 6,550 | 15.4% | 0.75 | 317／159 |
| [IBM](../trees/IBM/quant_history.jsonl) | 14 | USD 237.28 | 3,322 | 7.8% | 0.36 | 381／211 |
| [ADBE](../trees/ADBE/quant_history.jsonl) | 10 | USD 265.21 | 2,652 | 6.3% | 0.76 | 375／200 |
| [V](../trees/V/quant_history.jsonl) | 7 | USD 362.50 | 2,538 | 6.0% | 0.73 | 491／306 |
| [NKE](../trees/NKE/quant_history.jsonl) | 37 | USD 41.70 | 1,543 | 3.6% | 0.58 | 57／34 |
| [MSFT](../trees/MSFT/quant_history.jsonl) | 3 | USD 499.99 | 1,500 | 3.5% | 0.70 | 587／369 |
| [MDT](../trees/MDT/quant_history.jsonl) | 16 | USD 87.16 | 1,395 | 3.3% | 0.43 | 130／75 |
| [MDB](../trees/MDB/quant_history.jsonl) | 3 | USD 398.80 | 1,196 | 2.8% | 0.85 | 501／187 |
| [TEAM](../trees/TEAM/quant_history.jsonl) | 8 | USD 149.07 | 1,193 | 2.8% | 0.82 | 200／51 |
| [POET](../trees/POET/quant_history.jsonl) | 119 | USD 8.91 | 1,060 | 2.5% | 0.51 | 16／5 |
| [HUBS](../trees/HUBS/quant_history.jsonl) | 5 | USD 210.45 | 1,052 | 2.5% | 0.33 | 653／189 |
| [GLW](../trees/GLW/quant_history.jsonl) | 6 | USD 165.68 | 994 | 2.3% | 0.85 | 250／61 |
| [SNOW](../trees/SNOW/quant_history.jsonl) | 3 | USD 330.49 | 991 | 2.3% | 0.78 | 400／168 |
| [VST](../trees/VST/quant_history.jsonl) | 7 | USD 140.59 | 984 | 2.3% | 0.38 | 261／129 |
| [TYL](../trees/TYL/quant_history.jsonl) | 3 | USD 312.45 | 937 | 2.2% | 0.43 | 526／252 |
| [NVDA](../trees/NVDA/quant_history.jsonl) | 4 | USD 223.96 | 896 | 2.1% | 0.43 | 418／154 |
| [MU](../trees/MU/quant_history.jsonl) | 1 | USD 877.57 | 878 | 2.1% | 0.71 | 1,937／367 |
| [CHYM](../trees/CHYM/quant_history.jsonl) | 30 | USD 29.10 | 873 | 2.1% | 0.69 | 39／14 |
| [TSM](../trees/TSM/quant_history.jsonl) | 2 | USD 420.04 | 840 | 2.0% | 0.71 | 611／210 |
| [UUUU](../trees/UUUU/quant_history.jsonl) | 58 | USD 14.14 | 820 | 1.9% | 0.65 | 20／7 |
| [INTC](../trees/INTC/quant_history.jsonl) | 8 | USD 101.65 | 813 | 1.9% | 0.77 | 186／38 |
| [STX](../trees/STX/quant_history.jsonl) | 1 | USD 812.76 | 813 | 1.9% | 0.49 | 447／78 |
| [CEG](../trees/CEG/quant_history.jsonl) | 3 | USD 269.89 | 810 | 1.9% | 0.71 | 406／171 |
| [ADI](../trees/ADI/quant_history.jsonl) | 2 | USD 389.93 | 780 | 1.8% | 0.69 | 624／215 |
| [ISRG](../trees/ISRG/quant_history.jsonl) | 2 | USD 378.81 | 758 | 1.8% | 0.69 | 608／212 |
| [UBER](../trees/UBER/quant_history.jsonl) | 10 | USD 75.02 | 750 | 1.8% | 0.36 | 123／56 |
| [CRDO](../trees/CRDO/quant_history.jsonl) | 3 | USD 249.89 | 750 | 1.8% | 0.52 | 469／94 |
| [GOOGL](../trees/GOOGL/quant_history.jsonl) | 2 | USD 354.30 | 709 | 1.7% | 0.35 | 501／276 |
| [MRVL](../trees/MRVL/quant_history.jsonl) | 3 | USD 218.72 | 656 | 1.5% | 0.69 | 298／88 |
| [BABA](../trees/BABA/quant_history.jsonl) | 5 | USD 128.41 | 642 | 1.5% | 0.72 | 176／61 |
| [AAPL](../trees/AAPL/quant_history.jsonl) | 2 | USD 313.33 | 627 | 1.5% | 0.76 | 391／187 |
| [AMBA](../trees/AMBA/quant_history.jsonl) | 7 | USD 86.78 | 607 | 1.4% | 0.73 | 118／40 |
| [META](../trees/META/quant_history.jsonl) | 1 | USD 592.10 | 592 | 1.4% | 0.68 | 918／286 |
| [CRM](../trees/CRM/quant_history.jsonl) | 3 | USD 192.74 | 578 | 1.4% | 0.53 | 261／131 |
| [HOOD](../trees/HOOD/quant_history.jsonl) | 6 | USD 93.29 | 560 | 1.3% | 0.85 | 125／33 |
| [AMZN](../trees/AMZN/quant_history.jsonl) | 2 | USD 274.48 | 549 | 1.3% | 0.58 | 346／170 |
| [FUTU](../trees/FUTU/quant_history.jsonl) | 5 | USD 109.02 | 545 | 1.3% | 0.53 | 177／67 |
| [AAOI](../trees/AAOI/quant_history.jsonl) | 4 | USD 135.63 | 543 | 1.3% | 0.68 | 185／43 |
| [ACN](../trees/ACN/quant_history.jsonl) | 3 | USD 175.72 | 527 | 1.2% | 0.54 | 258／104 |
| [AMD](../trees/AMD/quant_history.jsonl) | 1 | USD 483.36 | 483 | 1.1% | 0.65 | 960／210 |
| [OKLO](../trees/OKLO/quant_history.jsonl) | 9 | USD 48.42 | 436 | 1.0% | 0.39 | 126／24 |
| [UNH](../trees/UNH/quant_history.jsonl) | 1 | USD 407.08 | 407 | 1.0% | 0.72 | 504／225 |
| [PM](../trees/PM/quant_history.jsonl) | 2 | USD 189.57 | 379 | 0.9% | 0.38 | 262／159 |
| [ONDS](../trees/ONDS/quant_history.jsonl) | 39 | USD 9.11 | 355 | 0.8% | 0.34 | 8／3 |
| [APP](../trees/APP/quant_history.jsonl) | 1 | USD 346.80 | 347 | 0.8% | 0.27 | 922／242 |
| [QCOM](../trees/QCOM/quant_history.jsonl) | 2 | USD 167.86 | 336 | 0.8% | 0.41 | 281／118 |
| [ALAB](../trees/ALAB/quant_history.jsonl) | 1 | USD 334.17 | 334 | 0.8% | 0.64 | 493／123 |
| [NOK](../trees/NOK/quant_history.jsonl) | 33 | USD 9.36 | 309 | 0.7% | 0.39 | 33／4 |
| [PDD](../trees/PDD/quant_history.jsonl) | 3 | USD 91.76 | 275 | 0.6% | 0.32 | 154／64 |
| [TTD](../trees/TTD/quant_history.jsonl) | 19 | USD 13.80 | 262 | 0.6% | 0.21 | 46／13 |
| [ON](../trees/ON/quant_history.jsonl) | 3 | USD 81.17 | 244 | 0.6% | 0.57 | 123／48 |
| [NBIS](../trees/NBIS/quant_history.jsonl) | 1 | USD 187.97 | 188 | 0.4% | 0.33 | 741／52 |
| [PLTR](../trees/PLTR/quant_history.jsonl) | 1 | USD 172.01 | 172 | 0.4% | 0.76 | 176／53 |
| [HPQ](../trees/HPQ/quant_history.jsonl) | 4 | USD 30.05 | 120 | 0.3% | 0.42 | 40／20 |
| [SMR](../trees/SMR/quant_history.jsonl) | 8 | USD 9.82 | 79 | 0.2% | 0.33 | 22／4 |
| [000660.KS](../trees/000660.KS/quant_history.jsonl) | 28 | — | — | — | — | — |
| [ETN](../trees/ETN/quant_history.jsonl) | -8 | USD 448.68 | -3,589 | -8.5% | 0.83 | 496／272 |
| [NOW](../trees/NOW/quant_history.jsonl) | -37 | USD 124.88 | -4,621 | -10.9% | 0.55 | 179／84 |
| [COHR](../trees/COHR/quant_history.jsonl) | -16 | USD 379.13 | -6,066 | -14.3% | 0.65 | 478／124 |

持倉市值合計 ≈ $51,749（另有現金；快照價為名單日收市，未逐日重估）。無快照價者為當週不在名單內的存倉。

## 交易日記（新在前）

旗標說明：λ 折減＝原始 Kelly 注碼按規則折減；上限封頂＝觸及單一持倉上限；低於交易門檻＝目標與現況差距太小，不動。

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
