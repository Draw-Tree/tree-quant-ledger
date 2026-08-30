# 💼 持倉與交易日記（Sleeve A Kelly ＋ Sleeve B 長短倉）

更新 2026-08-30｜數據源＝[`weekly/*.json`](weekly/)（IBKR 模擬帳戶每週journal，本頁由同一檔案確定性生成，人手零落數）｜規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md)｜研究用途，非投資建議。

倉位由樹的信念（conviction）經 fractional Kelly 決定——樹愈有把握、注碼愈大；判定轉弱，下週自動減倉。

## 目前持倉（IBKR 實倉快照 2026-08-24 15:45 UTC｜Sleeve NLV $43,722｜63 檔）

| 股票 | 股數 | 快照價 | 市值（USD） | 佔比 | 信念 | 牛／熊目標 |
|---|---:|---:|---:|---:|---:|---|
| [CVX](../trees/CVX/quant_history.jsonl) | 40 | USD 205.27 | 8,211 | 18.8% | 0.49 | 192／98 |
| [XE](../trees/XE/quant_history.jsonl) | 398 | USD 18.67 | 7,431 | 17.0% | 0.59 | 25／8 |
| [HUBS](../trees/HUBS/quant_history.jsonl) | 24 | USD 240.01 | 5,760 | 13.2% | 0.32 | 653／189 |
| [VST](../trees/VST/quant_history.jsonl) | 40 | USD 136.21 | 5,448 | 12.5% | 0.36 | 261／129 |
| [V](../trees/V/quant_history.jsonl) | 9 | USD 371.04 | 3,339 | 7.6% | 0.75 | 491／306 |
| [IBM](../trees/IBM/quant_history.jsonl) | 10 | USD 235.68 | 2,357 | 5.4% | 0.35 | 381／211 |
| [NKE](../trees/NKE/quant_history.jsonl) | 57 | USD 40.76 | 2,323 | 5.3% | 0.57 | 57／34 |
| [ADBE](../trees/ADBE/quant_history.jsonl) | 8 | USD 275.30 | 2,202 | 5.0% | 0.78 | 375／200 |
| [DDOG](../trees/DDOG/quant_history.jsonl) | 5 | USD 235.62 | 1,178 | 2.7% | 0.75 | 317／159 |
| [TYL](../trees/TYL/quant_history.jsonl) | 3 | USD 350.73 | 1,052 | 2.4% | 0.48 | 526／252 |
| [MU](../trees/MU/quant_history.jsonl) | 1 | USD 966.78 | 967 | 2.2% | 0.75 | 1,937／367 |
| [MSFT](../trees/MSFT/quant_history.jsonl) | 2 | USD 483.24 | 966 | 2.2% | 0.68 | 587／369 |
| [MDT](../trees/MDT/quant_history.jsonl) | 10 | USD 93.35 | 934 | 2.1% | 0.48 | 130／75 |
| [GLW](../trees/GLW/quant_history.jsonl) | 6 | USD 149.84 | 899 | 2.1% | 0.82 | 250／61 |
| [MDB](../trees/MDB/quant_history.jsonl) | 2 | USD 430.83 | 862 | 2.0% | 0.89 | 501／187 |
| [NVDA](../trees/NVDA/quant_history.jsonl) | 4 | USD 214.72 | 859 | 2.0% | 0.41 | 418／154 |
| [STX](../trees/STX/quant_history.jsonl) | 1 | USD 850.00 | 850 | 1.9% | 0.49 | 447／78 |
| [TSM](../trees/TSM/quant_history.jsonl) | 2 | USD 418.95 | 838 | 1.9% | 0.71 | 611／210 |
| [CEG](../trees/CEG/quant_history.jsonl) | 3 | USD 272.88 | 819 | 1.9% | 0.69 | 406／171 |
| [ISRG](../trees/ISRG/quant_history.jsonl) | 2 | USD 378.81 | 758 | 1.7% | 0.69 | 608／212 |
| [ADI](../trees/ADI/quant_history.jsonl) | 2 | USD 373.09 | 746 | 1.7% | 0.68 | 624／215 |
| [INTC](../trees/INTC/quant_history.jsonl) | 8 | USD 90.07 | 721 | 1.6% | 0.75 | 186／38 |
| [TEAM](../trees/TEAM/quant_history.jsonl) | 4 | USD 171.81 | 687 | 1.6% | 0.87 | 200／51 |
| [SNOW](../trees/SNOW/quant_history.jsonl) | 2 | USD 332.78 | 666 | 1.5% | 0.78 | 400／168 |
| [HOOD](../trees/HOOD/quant_history.jsonl) | 6 | USD 108.13 | 649 | 1.5% | 0.90 | 125／33 |
| [CRM](../trees/CRM/quant_history.jsonl) | 3 | USD 209.17 | 628 | 1.4% | 0.59 | 261／131 |
| [AAPL](../trees/AAPL/quant_history.jsonl) | 2 | USD 309.35 | 619 | 1.4% | 0.75 | 391／187 |
| [FUTU](../trees/FUTU/quant_history.jsonl) | 5 | USD 123.64 | 618 | 1.4% | 0.60 | 177／67 |
| [BABA](../trees/BABA/quant_history.jsonl) | 5 | USD 119.34 | 597 | 1.4% | 0.70 | 176／61 |
| [ACN](../trees/ACN/quant_history.jsonl) | 3 | USD 185.28 | 556 | 1.3% | 0.57 | 258／104 |
| [UBER](../trees/UBER/quant_history.jsonl) | 7 | USD 78.80 | 552 | 1.3% | 0.37 | 123／56 |
| [META](../trees/META/quant_history.jsonl) | 1 | USD 549.90 | 550 | 1.3% | 0.66 | 918／286 |
| [TXN](../trees/TXN/quant_history.jsonl) | 2 | USD 264.36 | 529 | 1.2% | 0.63 | 360／187 |
| [AMZN](../trees/AMZN/quant_history.jsonl) | 2 | USD 258.63 | 517 | 1.2% | 0.54 | 346／170 |
| [AMBA](../trees/AMBA/quant_history.jsonl) | 7 | USD 73.73 | 516 | 1.2% | 0.67 | 118／40 |
| [AAOI](../trees/AAOI/quant_history.jsonl) | 4 | USD 124.82 | 499 | 1.1% | 0.65 | 185／43 |
| [AMD](../trees/AMD/quant_history.jsonl) | 1 | USD 473.25 | 473 | 1.1% | 0.67 | 960／210 |
| [POET](../trees/POET/quant_history.jsonl) | 46 | USD 8.25 | 380 | 0.9% | 0.49 | 16／5 |
| [PM](../trees/PM/quant_history.jsonl) | 2 | USD 188.23 | 376 | 0.9% | 0.37 | 262／159 |
| [GOOGL](../trees/GOOGL/quant_history.jsonl) | 1 | USD 344.82 | 345 | 0.8% | 0.34 | 501／276 |
| [ONDS](../trees/ONDS/quant_history.jsonl) | 39 | USD 8.71 | 340 | 0.8% | 0.33 | 8／3 |
| [NOK](../trees/NOK/quant_history.jsonl) | 33 | USD 10.21 | 337 | 0.8% | 0.40 | 33／4 |
| [QCOM](../trees/QCOM/quant_history.jsonl) | 2 | USD 160.75 | 322 | 0.7% | 0.36 | 281／118 |
| [APP](../trees/APP/quant_history.jsonl) | 1 | USD 305.77 | 306 | 0.7% | 0.22 | 922／242 |
| [ALAB](../trees/ALAB/quant_history.jsonl) | 1 | USD 284.97 | 285 | 0.7% | 0.59 | 493／123 |
| [PDD](../trees/PDD/quant_history.jsonl) | 3 | USD 88.38 | 265 | 0.6% | 0.30 | 154／64 |
| [MRVL](../trees/MRVL/quant_history.jsonl) | 1 | USD 237.04 | 237 | 0.5% | 0.72 | 298／88 |
| [CRDO](../trees/CRDO/quant_history.jsonl) | 1 | USD 230.57 | 231 | 0.5% | 0.49 | 469／94 |
| [ON](../trees/ON/quant_history.jsonl) | 3 | USD 74.21 | 223 | 0.5% | 0.51 | 123／48 |
| [NBIS](../trees/NBIS/quant_history.jsonl) | 1 | USD 219.13 | 219 | 0.5% | 0.40 | 741／52 |
| [AMKR](../trees/AMKR/quant_history.jsonl) | 4 | USD 50.26 | 201 | 0.5% | 0.31 | 106／38 |
| [UUUU](../trees/UUUU/quant_history.jsonl) | 12 | USD 15.14 | 182 | 0.4% | 0.67 | 20／7 |
| [PLTR](../trees/PLTR/quant_history.jsonl) | 1 | USD 179.94 | 180 | 0.4% | 0.46 | 176／53 |
| [CHYM](../trees/CHYM/quant_history.jsonl) | 4 | USD 32.78 | 131 | 0.3% | 0.75 | 39／14 |
| [HPQ](../trees/HPQ/quant_history.jsonl) | 4 | USD 29.71 | 119 | 0.3% | 0.42 | 40／20 |
| [SMR](../trees/SMR/quant_history.jsonl) | 8 | USD 9.40 | 75 | 0.2% | 0.31 | 22／4 |
| [TTD](../trees/TTD/quant_history.jsonl) | 235 | — | — | — | — | — |
| [000660.KS](../trees/000660.KS/quant_history.jsonl) | 30 | — | — | — | — | — |
| [OKLO](../trees/OKLO/quant_history.jsonl) | -48 | USD 42.09 | -2,020 | -4.6% | 0.38 | 126／24 |
| [COHR](../trees/COHR/quant_history.jsonl) | -8 | USD 289.52 | -2,316 | -5.3% | 0.58 | 478／124 |
| [ETN](../trees/ETN/quant_history.jsonl) | -6 | USD 419.20 | -2,515 | -5.8% | 0.78 | 496／272 |
| [NOW](../trees/NOW/quant_history.jsonl) | -30 | USD 128.48 | -3,854 | -8.8% | 0.56 | 179／84 |
| [UNH](../trees/UNH/quant_history.jsonl) | -13 | USD 390.11 | -5,071 | -11.6% | 0.69 | 504／225 |

持倉市值合計 ≈ $47,149（另有現金；快照價為名單日收市，未逐日重估）。無快照價者為當週不在名單內的存倉。

## Sleeve B 長短倉持倉（依 2026-08-23 名單，2026-08-24 開倉）

| 方向 | 股票 | 股數 | 入場價 | 目標權重 | 落單狀態 |
|---|---|---:|---:|---:|---|
| 🟢 買入 | [CBRS](../trees/CBRS/quant_history.jsonl) | 36 | 189.75 | 16.7% | PreSubmitted |
| 🟢 買入 | [HEI](../trees/HEI/quant_history.jsonl) | 19 | 357.00 | 16.7% | PreSubmitted |
| 🟢 買入 | [NBIS](../trees/NBIS/quant_history.jsonl) | 32 | 210.99 | 16.7% | PreSubmitted |
| 🔴 沽空 | [SMR](../trees/SMR/quant_history.jsonl) | 451 | 9.18 | 10.0% | PreSubmitted |

長 3 腿／短 1 腿。等權、長短各半、持有一週；缺腿不補平，淨曝險如實記錄。逐週結算與指數見 [`ls/`](ls/)；規則見 [`STRATEGY_SLEEVES_20260723.md`](STRATEGY_SLEEVES_20260723.md) §2。

## 交易日記（新在前）

旗標說明：λ 折減＝原始 Kelly 注碼按規則折減；上限封頂＝觸及單一持倉上限；低於交易門檻＝目標與現況差距太小，不動。

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
