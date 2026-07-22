#!/usr/bin/env python3
"""校準資料集第二層：enrichment ＋ 分析表（數字唯一來源）。

輸入：tree_quant cmd_calib_table 之 raw 事件表（一行一個判定轉變事件）。
輸出：
  events.csv   — schema v2：raw 欄 ＋ cluster_id/cluster_size ＋ 同期全池
                 中位 leg（pool_h*）＋ 超額回報（excess_h*）
  clusters.csv — 一行一個 ticker×事件週 cluster：廣度特徵（幾多葉/幾多支/
                 淨分數變化/等級加權變化/必要葉旗）＋ 未來 28 日 cascade
                 結果（同 ticker 之後仲有幾多次轉變/降級/升級）＋ cluster
                 層超額回報
  markdown     — CALIBRATION.md 的全部結果表（超額曲線、raw 曲線、等級
                 曲線、廣度×cascade 表、permutation 檢定）

紀律：所有公開數字必須由本腳本生成；本腳本隨出口一併發布到公開庫
（calibration/analysis.py），外部人跑同一份 code 得同一份數。
規格與預登記協議見 CALIBRATION_SPEC.md。

用法：python3 _lib/calib_analysis.py --events raw.csv --quant-root . --outdir out/
"""
from __future__ import annotations

import argparse
import csv
import glob
import json
import random
import statistics
from datetime import date, timedelta
from pathlib import Path

SCHEMA_VERSION = 2
HORIZONS = list(range(1, 9))
CASCADE_WINDOW_DAYS = 28
PERM_N = 20000
PERM_SEED = 42  # 固定種子：同一份數據永遠得同一個 p 值（可重現）

GRADE_WEIGHTS = {"致命": 2.5, "重創": 1.6, "明顯受損": 0.9, "輕微": 0.4, "邊緣": 0.15}
GRADE_ORDER = ["致命", "重創", "明顯受損", "輕微", "邊緣"]


def _pdate(s):
    try:
        y, m, d = str(s).split("-")
        return date(int(y), int(m), int(d))
    except (ValueError, AttributeError):
        return None


def _f(row: dict, key: str):
    v = row.get(key)
    if v is None or v == "":
        return None
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


def _pct(x) -> str:
    if x is None:
        return "—"
    return f"{'+' if x >= 0 else '−'}{abs(x) * 100:.1f}%"


# ---- 全池同期 leg（超額回報基準） ---------------------------------------

def load_pool_legs(quant_root: str) -> dict:
    """{(start_date, h): [每棵樹該 leg 的回報]}——沿用引擎同一套 leg 有效性
    規則（起訖 snapshot_price_date 相同者不算）。"""
    legs: dict = {}
    for p in glob.glob(str(Path(quant_root) / "*" / "quant_history.jsonl")):
        rows = [json.loads(ln) for ln in open(p, encoding="utf-8") if ln.strip()]
        rows.sort(key=lambda r: r.get("date", ""))
        for i in range(len(rows)):
            for h in HORIZONS:
                if i + h >= len(rows):
                    break
                a, b = rows[i], rows[i + h]
                if (b.get("snapshot_price_date")
                        and b.get("snapshot_price_date") == a.get("snapshot_price_date")):
                    continue
                try:
                    r = float(b["snapshot_price"]) / float(a["snapshot_price"]) - 1
                except (TypeError, ValueError, ZeroDivisionError, KeyError):
                    continue
                legs.setdefault((a.get("date"), h), []).append(r)
    return legs


def pool_median(legs: dict, start_date: str, h: int):
    vals = legs.get((start_date, h))
    return statistics.median(vals) if vals else None


# ---- enrichment ------------------------------------------------------------

def cluster_key(ev: dict) -> str:
    d = _pdate(ev.get("date"))
    if not d:
        return f"{ev.get('ticker')}@unknown"
    iy, iw, _ = d.isocalendar()
    return f"{ev.get('ticker')}@{iy}-W{iw:02d}"


def enrich(events: list[dict], legs: dict) -> list[dict]:
    counts: dict = {}
    for ev in events:
        counts[cluster_key(ev)] = counts.get(cluster_key(ev), 0) + 1
    for ev in events:
        ev["schema_version"] = SCHEMA_VERSION
        ev["cluster_id"] = cluster_key(ev)
        ev["cluster_size"] = counts[ev["cluster_id"]]
        rd = ev.get("row_date")
        for h in HORIZONS:
            pm = pool_median(legs, rd, h) if rd else None
            fw = _f(ev, f"fwd_h{h}")
            ev[f"pool_h{h}"] = round(pm, 6) if pm is not None else None
            ev[f"excess_h{h}"] = (round(fw - pm, 6)
                                  if (fw is not None and pm is not None) else None)
    return events


def build_clusters(events: list[dict]) -> list[dict]:
    by_ticker_dates: dict = {}
    for ev in events:
        d = _pdate(ev.get("date"))
        if d:
            by_ticker_dates.setdefault(ev["ticker"], []).append((d, ev))
    for t in by_ticker_dates:
        by_ticker_dates[t].sort(key=lambda x: x[0])

    groups: dict = {}
    for ev in events:
        groups.setdefault(ev["cluster_id"], []).append(ev)

    clusters = []
    for cid, evs in sorted(groups.items()):
        t = evs[0]["ticker"]
        dates = [x for x in (_pdate(e.get("date")) for e in evs) if x]
        last = max(dates) if dates else None
        # cascade：cluster 最後事件日之後 28 日內，同 ticker 仲有幾多次轉變
        fut = fut_dn = fut_up = 0
        if last:
            for d, e in by_ticker_dates.get(t, []):
                if last < d <= last + timedelta(days=CASCADE_WINDOW_DAYS):
                    fut += 1
                    if e.get("direction") == "downgrade":
                        fut_dn += 1
                    elif e.get("direction") == "upgrade":
                        fut_up += 1
        gw = 0.0
        for e in evs:
            sd = _f(e, "score_delta")
            w = GRADE_WEIGHTS.get(e.get("impact_grade") or "", None)
            if sd is not None and w is not None:
                gw += sd * w
        aligned = [e for e in evs if e.get("row_date")]
        n_dn = sum(1 for e in evs if e.get("direction") == "downgrade")
        n_up = sum(1 for e in evs if e.get("direction") == "upgrade")
        # 訊號純度（H-purity，2026-07-22 維護者提出）：同週淨方向。
        # mixed＝同週有升有降，訊號互相抵銷，不應與純降級週混為一談。
        mix_type = ("mixed" if (n_dn and n_up) else
                    "down_only" if n_dn else
                    "up_only" if n_up else "lateral_only")
        row = {
            "cluster_id": cid, "ticker": t,
            "mix_type": mix_type,
            "first_event": min(dates).isoformat() if dates else None,
            "last_event": last.isoformat() if last else None,
            "n_events": len(evs),
            "n_hypotheses": len({e.get("hypothesis") for e in evs}),
            "n_branches": len({e.get("branch") for e in evs if e.get("branch")}),
            "n_down": sum(1 for e in evs if e.get("direction") == "downgrade"),
            "n_up": sum(1 for e in evs if e.get("direction") == "upgrade"),
            "n_lateral": sum(1 for e in evs if e.get("direction") == "lateral"),
            "sum_score_delta": sum(x for x in (_f(e, "score_delta") for e in evs)
                                   if x is not None),
            "grade_weighted_delta": round(gw, 3),
            "any_necessity_down": any(str(e.get("is_necessity_leaf")) == "True"
                                      and e.get("direction") == "downgrade"
                                      for e in evs),
            "aligned": bool(aligned),
            "fut_transitions_28d": fut,
            "fut_downgrades_28d": fut_dn,
            "fut_upgrades_28d": fut_up,
        }
        for h in HORIZONS:
            vals = [x for x in (_f(e, f"excess_h{h}") for e in aligned) if x is not None]
            row[f"excess_h{h}"] = round(statistics.mean(vals), 6) if vals else None
        clusters.append(row)
    return clusters


# ---- 分析表 ----------------------------------------------------------------

def _curve_cells(rows: list[dict], key_prefix: str, cl_of) -> str:
    cells = []
    for h in HORIZONS:
        vals = [(r, _f(r, f"{key_prefix}{h}")) for r in rows]
        vals = [(r, v) for r, v in vals if v is not None]
        if not vals:
            cells.append("—")
            continue
        m = statistics.mean(v for _, v in vals)
        ncl = len({cl_of(r) for r, _ in vals})
        cells.append(f"{_pct(m)}（{len(vals)}/{ncl}）")
    return " | ".join(cells)


def _perm(down: list, other: list) -> float | None:
    if len(down) < 2 or len(other) < 1:
        return None
    obs = statistics.mean(down) - statistics.mean(other)
    vals = down + other
    rng = random.Random(PERM_SEED)
    cnt = 0
    for _ in range(PERM_N):
        rng.shuffle(vals)
        if statistics.mean(vals[:len(down)]) - statistics.mean(vals[len(down):]) <= obs:
            cnt += 1
    return cnt / PERM_N


def permutation_p(clusters: list[dict]) -> tuple:
    """cluster 層：降級 cluster 的 excess_h1 是否低於其他（單尾）。"""
    pts = [(c, _f(c, "excess_h1")) for c in clusters if c.get("aligned")]
    pts = [(c, v) for c, v in pts if v is not None]
    down = [v for c, v in pts if c["n_down"] > 0]
    other = [v for c, v in pts if c["n_down"] == 0]
    return (_perm(down, other), len(down), len(other))


def permutation_p_purity(clusters: list[dict]) -> tuple:
    """純度口徑：純降級週 vs 純升級／僅橫向週（混合週剔除——訊號抵銷，
    歸邊不明）。H-purity 於 2026-07-22 見樣本後提出，本檢定對現有樣本屬
    in-sample 探索，只對之後累積的新樣本具預登記效力。"""
    pts = [(c, _f(c, "excess_h1")) for c in clusters if c.get("aligned")]
    pts = [(c, v) for c, v in pts if v is not None]
    down = [v for c, v in pts if c.get("mix_type") == "down_only"]
    other = [v for c, v in pts if c.get("mix_type") in ("up_only", "lateral_only")]
    return (_perm(down, other), len(down), len(other))


def markdown_tables(events: list[dict], clusters: list[dict]) -> str:
    cl_of = lambda r: r.get("cluster_id")  # noqa: E731
    head = "| " + " | ".join(f"+{h}週" for h in HORIZONS) + " |"
    sep = "|" + "---|" * HORIZONS[-1]
    out = []

    out += ["### 超額回報曲線（主表：扣除同期全池中位；每格＝均值（事件數/獨立cluster數））", ""]
    out += ["| 方向 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級"), ("lateral", "橫向")):
        grp = [e for e in events if e.get("direction") == dr]
        out.append(f"| {zh} | {len(grp)} | {_curve_cells(grp, 'excess_h', cl_of)} |")
    out += ["", "### 原始回報曲線（參考：未扣大市）", ""]
    out += ["| 方向 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級")):
        grp = [e for e in events if e.get("direction") == dr]
        out.append(f"| {zh} | {len(grp)} | {_curve_cells(grp, 'fwd_h', cl_of)} |")

    out += ["", "### 降級事件 × 衝擊等級（超額口徑）", ""]
    out += ["| 衝擊等級 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    downs = [e for e in events if e.get("direction") == "downgrade"]
    for g in GRADE_ORDER:
        grp = [e for e in downs if (e.get("impact_grade") or "") == g]
        out.append(f"| {g} | {len(grp)} | {_curve_cells(grp, 'excess_h', cl_of)} |")

    # 訊號純度（H-purity）：同週淨方向——純降／混合／純升，逐類對照。
    out += ["", "### 訊號純度 × 結果（假說 H-purity：同週有升有降＝訊號抵銷，"
            "不應與純降級週混計）", "",
            "逐隻股票逐週看：該週是全部降級、有升有降、還是全部升級？"
            "混合週的降級不是乾淨的壞消息——同一棵樹另一條分支同週在改善。",
            "",
            "| 週類型 | cluster 數 | 有價格 | 平均超額 +1週 | 平均超額 +2週 | 28日內再有降級 |",
            "|---|---|---|---|---|---|"]
    _MIX_ZH = {"down_only": "純降級週", "mixed": "混合週（有升有降）",
               "up_only": "純升級週", "lateral_only": "僅橫向週"}
    for m in ("down_only", "mixed", "up_only", "lateral_only"):
        grp = [c for c in clusters if c.get("mix_type") == m]
        if not grp:
            continue
        e1 = [x for x in (_f(c, "excess_h1") for c in grp) if x is not None]
        e2 = [x for x in (_f(c, "excess_h2") for c in grp) if x is not None]
        p_dn = sum(1 for c in grp if c["fut_downgrades_28d"] > 0) / len(grp)
        out.append(
            f"| {_MIX_ZH[m]} | {len(grp)} | {len(e1)} | "
            f"{_pct(statistics.mean(e1)) if e1 else '—'} | "
            f"{_pct(statistics.mean(e2)) if e2 else '—'} | {p_dn * 100:.0f}% |")
    pd1 = [c for c in clusters if c.get("mix_type") == "down_only"
           and c["n_down"] == 1]
    pdm = [c for c in clusters if c.get("mix_type") == "down_only"
           and c["n_down"] >= 2]
    for grp, label in ((pd1, "　純降級：單葉"), (pdm, "　純降級：多葉（≥2）")):
        e1 = [x for x in (_f(c, "excess_h1") for c in grp) if x is not None]
        p_dn = (sum(1 for c in grp if c["fut_downgrades_28d"] > 0) / len(grp)
                if grp else 0)
        out.append(
            f"| {label} | {len(grp)} | {len(e1)} | "
            f"{_pct(statistics.mean(e1)) if e1 else '—'} | — | {p_dn * 100:.0f}% |")
    out += ["", "純度注意：H-purity 由維護者於 2026-07-22 檢視樣本後提出，上表對"
            "現有樣本屬 in-sample 探索（假說由同一批數據啟發，不能用同一批數據"
            "證明自己）；對之後累積的新樣本才具預登記檢定效力。"]

    # 廣度 × cascade：同週轉變愈多，未來 28 日係咪愈大機會繼續轉差？
    out += ["", "### 轉變廣度 ×未來 cascade（預登記假說 H-breadth）", "",
            "同一 ticker 同一週有多片葉／多支分支齊轉變，是否預示未來仲有更多轉變、"
            "以及更差的超額回報？bucket 按該週降級事件數；cascade＝其後 28 日內"
            "同 ticker 再現任何轉變／降級的 cluster 比例。", "",
            "| 該週降級數 | cluster 數 | 28日內再有轉變 | 28日內再有降級 | "
            "平均超額 +1週 | 平均超額 +2週 |",
            "|---|---|---|---|---|---|"]
    dcl = [c for c in clusters if c["n_down"] > 0]
    for lo, hi, label in ((1, 1, "1"), (2, 3, "2–3"), (4, 99, "≥4")):
        grp = [c for c in dcl if lo <= c["n_down"] <= hi]
        if not grp:
            out.append(f"| {label} | 0 | — | — | — | — |")
            continue
        p_any = sum(1 for c in grp if c["fut_transitions_28d"] > 0) / len(grp)
        p_dn = sum(1 for c in grp if c["fut_downgrades_28d"] > 0) / len(grp)
        e1 = [x for x in (_f(c, "excess_h1") for c in grp) if x is not None]
        e2 = [x for x in (_f(c, "excess_h2") for c in grp) if x is not None]
        out.append(
            f"| {label} | {len(grp)} | {p_any * 100:.0f}% | {p_dn * 100:.0f}% | "
            f"{_pct(statistics.mean(e1)) if e1 else '—'}（{len(e1)}） | "
            f"{_pct(statistics.mean(e2)) if e2 else '—'}（{len(e2)}） |")
    nec = [c for c in dcl if c["any_necessity_down"]]
    if nec:
        p_dn = sum(1 for c in nec if c["fut_downgrades_28d"] > 0) / len(nec)
        e1 = [x for x in (_f(c, "excess_h1") for c in nec) if x is not None]
        out.append(
            f"| 含必要葉降級 | {len(nec)} | "
            f"{sum(1 for c in nec if c['fut_transitions_28d'] > 0) / len(nec) * 100:.0f}% | "
            f"{p_dn * 100:.0f}% | {_pct(statistics.mean(e1)) if e1 else '—'}（{len(e1)}） | — |")
    base = [c for c in clusters if c["n_down"] == 0]
    if base:
        p_dn = sum(1 for c in base if c["fut_downgrades_28d"] > 0) / len(base)
        out.append(
            f"| （基準：無降級週） | {len(base)} | "
            f"{sum(1 for c in base if c['fut_transitions_28d'] > 0) / len(base) * 100:.0f}% | "
            f"{p_dn * 100:.0f}% | — | — |")
    out += ["", "cascade 注意：本管道每週重審同一批假說，同一單新聞可以連續兩週觸發"
            "轉變——「再有轉變」部分是管道自身的持續反應，不全是新資訊；"
            "解讀以對比基準行（無降級週）為準。"]

    p, nd, no = permutation_p(clusters)
    p2, nd2, no2 = permutation_p_purity(clusters)
    out += ["", "### 顯著性（cluster 層 permutation 檢定）", ""]
    if p is None:
        out.append(f"樣本不足（降級 cluster {nd}、對照 {no}），未能檢定。")
    else:
        out.append(
            f"1. **原始口徑**：有降級的 cluster（{nd} 個）對無降級 cluster"
            f"（{no} 個）的 +1 週超額回報差異，單尾 p = **{p:.3f}**"
            f"（{PERM_N:,} 次重抽，固定種子）。")
    if p2 is not None:
        out.append(
            f"2. **純度口徑**（剔除混合週）：純降級週（{nd2} 個）對純升級／"
            f"僅橫向週（{no2} 個），單尾 p = **{p2:.3f}**。對現有樣本屬"
            f" in-sample 探索（見純度注意）。")
    out.append("p ≥ 0.05 即未達顯著——如實呈報，不因結果不好看而隱藏。")
    return "\n".join(out)


# ---- 入口 ------------------------------------------------------------------

def build(raw_events_path: str, quant_root: str, outdir: str) -> str:
    """讀 raw 事件表 → 寫 events.csv（v2）＋ clusters.csv → 回傳結果表 markdown。

    model_transition 事件（判讀模型切換首個判讀日的重新評分潮，非市場事件）
    完整保留於 events.csv（帶旗），但統計表與 clusters 一律剔除——與 recode
    同一邏輯，只是 recode 於引擎層剔、transition 於分析層剔（旗留覆核）。"""
    with open(raw_events_path, encoding="utf-8") as f:
        all_events = list(csv.DictReader(f))
    legs = load_pool_legs(quant_root)
    all_events = enrich(all_events, legs)
    n_trans = sum(1 for e in all_events if str(e.get("model_transition")) == "True")
    events = [e for e in all_events if str(e.get("model_transition")) != "True"]
    clusters = build_clusters(events)

    outp = Path(outdir)
    outp.mkdir(parents=True, exist_ok=True)
    ev_fields: list[str] = []
    for e in all_events:
        for k in e:
            if k not in ev_fields:
                ev_fields.append(k)
    with open(outp / "events.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=ev_fields)
        w.writeheader()
        w.writerows(all_events)
    cl_fields = list(clusters[0].keys()) if clusters else []
    with open(outp / "clusters.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=cl_fields)
        w.writeheader()
        w.writerows(clusters)
    note = ""
    if n_trans:
        note = (f"\n**模型遷移剔除**：{n_trans} 個事件帶 `model_transition` 旗"
                "（判讀模型切換首個判讀日的重新評分潮，非市場事件——2026-07-16/18"
                " 由 grok-4.5 遷移至 deepseek-v3.2／v4-pro，當日轉變量為常態"
                " 4–6 倍），已於上列全部統計表剔除；原始行連旗完整保留於"
                " events.csv，`model` 欄記錄每個事件的判讀模型年代。\n")
    return markdown_tables(events, clusters) + note


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--events", required=True, help="raw events csv (cmd_calib_table output)")
    ap.add_argument("--quant-root", default=".", help="stock-trees checkout root")
    ap.add_argument("--outdir", required=True)
    args = ap.parse_args()
    md = build(args.events, args.quant_root, args.outdir)
    print(md)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
