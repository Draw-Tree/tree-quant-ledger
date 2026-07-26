# 📊 draw-tree 訊號板

> 更新於 2026-07-26（每週日名單發佈後自動重生成；數據源＝公開名單帳本 [`portfolio/verdict_watch.jsonl`](portfolio/verdict_watch.jsonl)＋各樹每週快照價，人手零落數）。超額＝該股一週回報 − 全池中位；研究用途，非投資建議。

## 本週發生了什麼（名單日 2026-07-26）（非正式：名單早於預登記正式起始日，不入正式比分）

本週 73 棵樹掃描完成：🔺 升級 3 檔｜🔻 降級 3 檔｜⚖️ 混合不入名單 1 檔

### 🔻 降級（研究上預期其後跑輸全池）

| 股票 | 最重等級 | 訊號 | 觸發 | 判定變化 |
|---|---|---|---|---|
| **ISRG** | 明顯受損 | -0.9 | 🗓️ 週掃描 | B1 Trending negative→Approaching falsification |
| **PLTR** | 重創 | -1.6 | 🗓️ 週掃描 | B2 Approaching falsification→Falsified |
| **NET** | 致命 | -2.5 | 🗓️ 週掃描 | A3 Approaching falsification→Falsified |

### 🔺 升級（預期跑贏）

| 股票 | 最重等級 | 訊號 | 觸發 | 判定變化 |
|---|---|---|---|---|
| **AMD** | 明顯受損 | +0.9 | 🗓️ 週掃描 | D3 Trending positive→Validated |
| **IFNNY** | 重創 | +1.6 | 🗓️ 週掃描 | C3 Trending positive→Validated |
| **CEG** | 致命 | +2.5 | 🗓️ 週掃描 | C2 Trending negative→Validated |

## 訊號生命線

每個訊號一行：名單公開後逐週相對全池的表現（綠＝跑贏、紅＝跑輸，色深＝幅度），**⚡＝判定翻轉**（訊號生命完結）。降級訊號整行應為紅、升級整行應為綠——預測正確與否，一眼看完。

![訊號生命線](dashboard.svg)

截至 2026-07-26：追蹤中訊號 6 個｜✓ 符合 0｜✗ 反向 0。

方法一句話：名單先公開、後對答案（append-only 帳本）；混合週（同股同週有升有降）依純度規則不入名單；財報觸發之訊號以事件日收盤開錶。詳見 [`calibration/SPEC.md`](calibration/SPEC.md)。

*研究用途，非投資建議。*