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
GRADE_ORDER = ["致命", "重創", "明顯受損", "輕微", "邊緣"]   # 儲存鍵，永不改


def _glabel(key: str) -> str:
    """儲存鍵 → 讀者顯示標籤「●●●●● 極高」。事實源 _lib/tree_quant.py。

    公開的 calibration/CALIBRATION.md 由本檔生成，等級欄從前直接印儲存鍵
    （致命／重創／明顯受損），與訊號板、Slack 的重要度刻度各講一套。
    """
    try:
        import sys as _sys
        _d = str(Path(__file__).resolve().parent)
        if _d not in _sys.path:
            _sys.path.insert(0, _d)
        from tree_quant import grade_label
        return grade_label(key)
    except Exception:  # noqa: BLE001
        return str(key or "")


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

def load_pool_legs(quant_root: str) -> tuple[dict, dict]:
    """回傳 (pool_legs, ticker_legs)：
    pool_legs   {(start_date, h): [每棵樹該 leg 的回報]}——沿用引擎同一套
                leg 有效性規則（起訖 snapshot_price_date 相同者不算）。
    ticker_legs {ticker: {start_date: +1 行回報}}——斷 state 比較（§8）用。
    歷史價回補 sidecar（price_history_backfill.jsonl）只在該樹首個實時行
    之前合併——與引擎 cmd_calib_table 同一規則。"""
    legs: dict = {}
    tlegs: dict = {}
    for p in glob.glob(str(Path(quant_root) / "*" / "quant_history.jsonl")):
        tdir = Path(p).parent
        rows = [json.loads(ln) for ln in open(p, encoding="utf-8") if ln.strip()]
        rows.sort(key=lambda r: r.get("date", ""))
        bp = tdir / "price_history_backfill.jsonl"
        if bp.exists():
            first_live = str(rows[0].get("date", "")) if rows else ""
            # 邊界剪裁（與引擎同一規則，v3.2）：sidecar 週六行日期 ≥ 首個
            # 實時行價格日 − 1 日者剪走——首個實時行常帶對上一個週末舊價
            # （同一個收盤價掛兩行），否則產生 0% 假 leg 污染全池中位。
            flp = _pdate(str(rows[0].get("snapshot_price_date", ""))) if rows else None
            pre = [json.loads(ln) for ln in
                   bp.read_text(encoding="utf-8").splitlines() if ln.strip()]
            keep = []
            for r in pre:
                if first_live and str(r.get("date", "")) >= first_live:
                    continue
                rd_ = _pdate(str(r.get("date", "")))
                if flp and rd_ and (flp - rd_).days <= 1:
                    continue
                keep.append(r)
            rows = keep + rows
            rows.sort(key=lambda r: r.get("date", ""))
        for i in range(len(rows)):
            for h in HORIZONS:
                if i + h >= len(rows):
                    break
                a, b = rows[i], rows[i + h]
                if (b.get("snapshot_price_date")
                        and b.get("snapshot_price_date") == a.get("snapshot_price_date")):
                    continue
                da = _pdate(str(a.get("snapshot_price_date")))
                db = _pdate(str(b.get("snapshot_price_date")))
                if da and db and abs((db - da).days) <= 1:
                    continue
                try:
                    r = float(b["snapshot_price"]) / float(a["snapshot_price"]) - 1
                except (TypeError, ValueError, ZeroDivisionError, KeyError):
                    continue
                legs.setdefault((a.get("date"), h), []).append(r)
                if h == 1:
                    tlegs.setdefault(tdir.name, {})[a.get("date")] = r
    return legs, tlegs


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
            ev[f"excess_h{h}"] = (fw - pm
                                  if (fw is not None and pm is not None) else None)
            if ev[f"excess_h{h}"] is not None:
                ev[f"excess_h{h}"] = round(ev[f"excess_h{h}"], 6)
        # 事前窗口超額（SPEC §8）：pre_row_date→row_date 之回報對池——
        # 分辨「市場唔理」與「市場早已反應」。
        prd = ev.get("pre_row_date")
        pre = _f(ev, "pre_h1")
        pm0 = pool_median(legs, prd, 1) if prd else None
        ev["excess_pre"] = (round(pre - pm0, 6)
                           if (pre is not None and pm0 is not None) else None)
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

def _hold_ok(e: dict, h: int) -> bool:
    """state 持有規則（§5 預登記、v3.4 起強制執行）：+h 週窗口不得跨越
    同一假說的下一次轉變——跨了就是下一個 state 的行情，不入本 state 賬。"""
    nd = _f(e, "next_transition_days")
    return nd is None or nd >= 7 * h


def _curve_cells(rows: list[dict], key_prefix: str, cl_of) -> str:
    cells = []
    for h in HORIZONS:
        vals = [(r, _f(r, f"{key_prefix}{h}")) for r in rows if _hold_ok(r, h)]
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


# ---- §8 特徵重要度工程（v3.0 預登記） --------------------------------------

K_BRANCH = 10   # 分支層 credibility 常數（§8 預登記）
K_GRADE = 30    # 等級層（同 §6）
T_HURDLE = 3.0  # Harvey–Liu 多重檢定門檻（factor zoo：t>3 方算候選）


def _spearman(xs: list, ys: list):
    n = len(xs)
    if n < 3:
        return None

    def rank(v):
        order = sorted(range(n), key=lambda i: v[i])
        r = [0.0] * n
        i = 0
        while i < n:  # 平手取平均秩
            j = i
            while j + 1 < n and v[order[j + 1]] == v[order[i]]:
                j += 1
            avg = (i + j) / 2 + 1
            for k2 in range(i, j + 1):
                r[order[k2]] = avg
            i = j + 1
        return r
    rx, ry = rank(xs), rank(ys)
    mx, my = sum(rx) / n, sum(ry) / n
    num = sum((a - mx) * (b - my) for a, b in zip(rx, ry))
    den = (sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry)) ** 0.5
    return num / den if den else None


def ic_section(clusters: list[dict]) -> list:
    """每週橫截面 rank IC（訊號＝grade_weighted_delta，結果＝+1 週超額）
    ＋ ICIR——Grinold–Kahn 口徑；週樣本 ≥3 方計。"""
    by_week: dict = {}
    for c in clusters:
        v, s = _f(c, "excess_h1"), _f(c, "grade_weighted_delta")
        if v is None or s is None:
            continue
        wk = str(c.get("cluster_id", "")).split("@")[-1]
        by_week.setdefault(wk, []).append((s, v))
    rows = []
    for wk in sorted(by_week):
        pts = by_week[wk]
        ic = _spearman([p[0] for p in pts], [p[1] for p in pts])
        rows.append((wk, len(pts), ic))
    out = ["", "### 訊號 IC 序列（§8：每週橫截面 rank IC；訊號＝等級加權淨變化）",
           "", "| 週 | n | rank IC |", "|---|---|---|"]
    for wk, n, ic in rows:
        out.append(f"| {wk} | {n} | {'—（n<3）' if ic is None else f'{ic:+.2f}'} |")
    ics = [ic for _, _, ic in rows if ic is not None]
    out.append("")
    if ics:
        m = statistics.mean(ics)
        sd = statistics.pstdev(ics) if len(ics) > 1 else None
        icir = (m / sd) if sd else None
        out.append(f"**IC 均值 {m:+.2f}｜有效週數 {len(ics)}"
                   + (f"｜ICIR {icir:.2f}" if icir is not None else "｜ICIR 樣本不足")
                   + "**。ICIR≥0.5 為佳；Fundamental Law（IR ≈ IC×√breadth）："
                   "本系統每週獨立事件約 5–10 個，breadth 有限，IC 再高，策略層 "
                   "IR 亦有數學上限——如實聲明。")
    else:
        out.append("有效週樣本不足（每週需 ≥3 個對齊 cluster）——IC 序列隨數據"
                   "累積自動出現。")
    return out


def branch_audit_section(events: list[dict]) -> list:
    """§8 分支審計：逐分支實現超額（兩層 empirical-Bayes shrinkage：
    branch→grade→global）＋事前窗口（分辨「市場唔理」與「市場先行」）＋
    Harvey–Liu t≥3 旗。只 flag 不自動改——等級語義為「證偽時對論點的
    承諾後果」，改動須人手重答該問題並記 grade_history。"""
    pts = [e for e in events if e.get("direction") == "downgrade"
           and _f(e, "excess_h1") is not None and _hold_ok(e, 1)]
    if not pts:
        return ["", "### 分支審計（§8）", "", "暫無有效降級樣本。"]
    glob_mean = statistics.mean(_f(e, "excess_h1") for e in pts)
    by_grade: dict = {}
    for e in pts:
        by_grade.setdefault(e.get("impact_grade") or "—", []).append(_f(e, "excess_h1"))
    grade_shrunk = {}
    for g, vals in by_grade.items():
        z = len(vals) / (len(vals) + K_GRADE)
        grade_shrunk[g] = z * statistics.mean(vals) + (1 - z) * glob_mean
    by_branch: dict = {}
    for e in pts:
        key = (e.get("ticker"), e.get("branch") or "?", e.get("impact_grade") or "—")
        by_branch.setdefault(key, []).append(e)
    out = ["", "### 分支審計（§8：實現衝擊 vs 聲明重要度；兩層 shrinkage "
           f"k_branch={K_BRANCH}／k_grade={K_GRADE}；旗＝n≥3 且 |t|≥{T_HURDLE:g}）",
           "", "| 分支 | 重要度 | n | 原始超額均值 | shrunk 估計 | 事前超額 | 旗 |",
           "|---|---|---|---|---|---|---|"]
    rows = []
    for (t, b, g), evs in by_branch.items():
        vals = [_f(e, "excess_h1") for e in evs]
        pre = [x for x in (_f(e, "excess_pre") for e in evs) if x is not None]
        n = len(vals)
        raw = statistics.mean(vals)
        z = n / (n + K_BRANCH)
        shrunk = z * raw + (1 - z) * grade_shrunk.get(g, glob_mean)
        flag = ""
        if n >= 3:
            sd = statistics.stdev(vals)
            tstat = raw / (sd / n ** 0.5) if sd else None
            if tstat is not None and abs(tstat) >= T_HURDLE:
                if raw > 0 and g in ("致命", "重創"):
                    flag = "⚠️ 高重要度無負反應（降級候選）"
                elif raw < -0.03 and g in ("輕微", "邊緣"):
                    flag = "⬆️ 低重要度強反應（升級候選）"
        pre_m = statistics.mean(pre) if pre else None
        if flag.startswith("⚠️") and pre_m is not None and pre_m < -0.02:
            flag += "｜事前已大幅負向——疑屬市場先行，非重要度評錯"
        nh = sum(1 for e in evs if e.get("price_era") == "hist_backfill")
        ncell = f"{n}（回補{nh}）" if nh else str(n)
        rows.append((f"{t}:{b}", g, ncell, raw, shrunk, pre_m, flag))
    for name, g, n, raw, shrunk, pre_m, flag in sorted(rows, key=lambda x: x[4]):
        out.append(f"| {name} | {_glabel(g)} | {n} | {_pct(raw)} | {_pct(shrunk)} | "
                   f"{_pct(pre_m) if pre_m is not None else '—'} | {flag} |")
    out += ["", f"全域降級超額均值 {_pct(glob_mean)}＝shrinkage 最外層先驗。"
            "審計**只 flag 不自動改**：重要度改動須人手重答「證偽後跌到哪」並記 "
            "grade_history（§8）；t≥3 為 Harvey–Liu 多重檢定門檻。"]
    return out


AGE_BUCKETS = [(0, 30, "≤30日"), (31, 60, "31–60日"), (61, 10 ** 6, ">60日")]


def age_section(events: list[dict]) -> list:
    """H-age（論點時效，§5.6）：樹的論點寫於建樹一刻，時效可能衰減——
    判定轉變的訊號強度按樹齡分桶呈報。雙尾、不預設方向；state 持有規則
    照剔。識別警示：現階段樹齡與日曆週高度共線（艦隊同期出生），本表
    屬監察位，首讀門檻＝每桶 ≥10 個獨立 cluster。"""
    out = ["", "### 樹齡 × 訊號強度（§5.6 H-age：論點時效——監察表，"
           "首讀門檻每桶 ≥10 個獨立 cluster）", "",
           "| 方向×樹齡 | 事件數 | cluster 數 | 超額+1週 | 超額+2週 | "
           "超額+4週 | +1週負超額比例 |", "|---|---|---|---|---|---|---|"]
    any_row = False
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級")):
        for lo, hi, bl in AGE_BUCKETS:
            grp = [e for e in events if e.get("direction") == dr
                   and (a := _f(e, "tree_age_days")) is not None
                   and lo <= a <= hi]
            if not grp:
                continue
            any_row = True
            ncl = len({e.get("cluster_id") for e in grp})
            cells = []
            neg = "—"
            for h in (1, 2, 4):
                vals = [x for x in (_f(e, f"excess_h{h}") for e in grp
                                    if _hold_ok(e, h)) if x is not None]
                cells.append(f"{_pct(statistics.mean(vals)) if vals else '—'}"
                             f"（{len(vals)}）")
                if h == 1 and vals:
                    neg = f"{sum(1 for x in vals if x < 0) / len(vals) * 100:.0f}%"
            out.append(f"| {zh}×{bl} | {len(grp)} | {ncl} | "
                       + " | ".join(cells) + f" | {neg} |")
    if not any_row:
        return []
    out += ["", "識別警示：現階段大部分樹同一週出生，**樹齡與日曆週近乎完全"
            "共線**（老齡桶可能全部來自同一名單週）——本表暫不可識別樹齡"
            "效應，屬監察位；分離依賴出生日分散的後期 cohort 累積事件。"
            "確認 |t|≥3 前，訊號分不加任何樹齡衰減因子（§5.6 H-age 行動鏈）。"]
    return out


def era_section(events: list[dict]) -> list:
    """§8 價格年代分層：回補段（Yahoo 歷史日線 sidecar）vs 實時段（週六
    快照）。兩段數據源與判讀模型年代都唔同——必須分開睇，先可以合埋講。"""
    aligned = [e for e in events if e.get("row_date")]
    n_hist = sum(1 for e in aligned if e.get("price_era") == "hist_backfill")
    if not n_hist:
        return []
    out = ["", "### 價格年代分層（§8：回補段 vs 實時段——數據源與判讀模型"
           "年代不同，必須分層呈報）", "",
           "| 方向×年代 | 事件數 | 超額+1週 | 超額+2週 | 超額+4週 |",
           "|---|---|---|---|---|"]
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級")):
        for era, ezh in (("hist_backfill", "回補段"), ("live", "實時段")):
            grp = [e for e in aligned if e.get("direction") == dr
                   and (e.get("price_era") or "live") == era]
            cells = []
            for h in (1, 2, 4):
                vals = [x for x in (_f(e, f"excess_h{h}") for e in grp
                                    if _hold_ok(e, h))
                        if x is not None]
                cells.append(f"{_pct(statistics.mean(vals)) if vals else '—'}"
                             f"（{len(vals)}）")
            out.append(f"| {zh}×{ezh} | {len(grp)} | " + " | ".join(cells) + " |")
    out += ["", f"回補段共 {n_hist} 個對齊事件——價格為 Yahoo 歷史日線（sidecar"
            "，逐行 `backfilled_hist` 標記，不入 quant_history），判讀屬 "
            "grok-4.5 年代；實時段為週六快照。兩段結論方向一致方可視為穩健。"]
    return out


PRE_BUCKETS = [(-10**6, -0.08, "≤−8pp（深負）"), (-0.08, -0.03, "−8..−3pp"),
               (-0.03, 0.03, "−3..+3pp"), (0.03, 10**6, ">+3pp")]


def priced_in_section(events: list[dict]) -> list:
    """H-priced-in（§5.6）：按事前一週超額分桶，**兩個方向都做**。

    原版只分降級側。2026-07-26 的實測顯示這個假設本身不完整：該批名單裡
    升級組事前平均 −11.0%、降級組 −5.9%，升級組其後平均 +9.9%——買入側
    7/7 的命中率有相當部分來自「跌殘反彈」而非判定。同一個反轉效應同時
    抬高買入側、壓低沽空側，只檢降級側會把它誤讀成「降級訊號較弱」。

    行動鏈亦隨之改寫（見 SPEC §5.6）：由連續阻尼 λ(pre) 改為二元 gate。
    連續函數需要估計門檻與折扣率兩個參數，單週約 20 個樣本估不出來；二元
    gate 只需一個預登記門檻，且失敗時的後果是「不入籃」而非「注碼算錯」。
    """
    out = []
    for direc, zh, worse in (("downgrade", "降級", lambda x: x < 0),
                             ("upgrade", "升級", lambda x: x > 0)):
        pts = [e for e in events if e.get("direction") == direc
               and _f(e, "excess_h1") is not None
               and _f(e, "excess_pre") is not None and _hold_ok(e, 1)]
        if not pts:
            continue
        out += ["", f"### 市場先行分桶 · {zh}側（§5.6 H-priced-in）", "",
                "| 事前一週超額 | 事件數 | 命中率（+1週方向正確） | "
                "超額+1週均值 | 超額+2週均值 |", "|---|---|---|---|---|"]
        for lo, hi, lbl in PRE_BUCKETS:
            grp = [e for e in pts if lo < _f(e, "excess_pre") <= hi]
            if not grp:
                continue
            h1 = [_f(e, "excess_h1") for e in grp]
            hit = sum(1 for x in h1 if worse(x)) / len(h1)
            h2 = [x for x in (_f(e, "excess_h2") for e in grp if _hold_ok(e, 2))
                  if x is not None]
            out.append(f"| {lbl} | {len(grp)} | {hit*100:.0f}% | "
                       f"{_pct(statistics.mean(h1))} | "
                       f"{_pct(statistics.mean(h2)) if h2 else '—'} |")
    if out:
        out += ["", "讀法：若**兩側**的深負桶都偏向正回報，那是市場反轉效應而非"
                "判定訊號強弱——它同時抬高買入側、壓低沽空側，須先控制再讀策略"
                "回報（計分板已並排報「控制事前走勢後」一行）。gate 門檻由本表"
                "累積估計，預登記後方可生效（§5.6 行動鏈）。"]
    return out


VERDICT_SCORE = {"Validated": 2, "Trending positive": 1, "Inconclusive": 0,
                 "Trending negative": -1, "Approaching falsification": -2,
                 "Falsified": -3,
                 "supported": 2, "partially_supported": 0, "pending": 0,
                 "challenged": -2}
_STATE_ZH = {2: "成立（Validated）", 1: "偏正（Trending positive）",
             0: "未決（Inconclusive）", -1: "偏負（Trending negative）",
             -2: "近證偽（Approaching falsification）", -3: "已證偽（Falsified）"}


def state_segment_section(all_events: list[dict], legs: dict, tlegs: dict) -> list:
    """§8 斷 state 比較：每個假說的時間線按判定 state 切段（轉變事件為
    界），逐段收集期間的每週超額 leg（tree leg − 同期全池中位），按 state
    分數分組——檢驗「state 愈差，期間超額愈差」是否單調。
    去重單位＝ticker×週×state 分數（同一棵樹同週多片葉同 state 只計一次）；
    同一 ticker 同週可同時出現於不同 state 組（不同葉不同 state），屬結構
    現實，如實保留。樣本只含曾轉變的假說（無轉變的樹不入 events）——
    存活偏差如實聲明。"""
    by_hyp: dict = {}
    for e in all_events:
        if e.get("date") and e.get("ticker") and e.get("hypothesis"):
            by_hyp.setdefault((e["ticker"], e["hypothesis"]), []).append(e)
    seen: set = set()
    buckets: dict = {}
    n_segs: dict = {}
    for (t, _hid), evs in by_hyp.items():
        evs.sort(key=lambda e: e["date"])
        segs = [(evs[0].get("from"), None, evs[0]["date"])]
        for j, e in enumerate(evs):
            end = evs[j + 1]["date"] if j + 1 < len(evs) else None
            segs.append((e.get("to"), e["date"], end))
        for state, s0, s1 in segs:
            sc = VERDICT_SCORE.get(str(state))
            if sc is None:
                continue
            n_segs[sc] = n_segs.get(sc, 0) + 1
            for d0, ret in (tlegs.get(t) or {}).items():
                if (s0 and d0 < s0) or (s1 and d0 >= s1):
                    continue
                pm = pool_median(legs, d0, 1)
                if pm is None:
                    continue
                key = (t, d0, sc)
                if key in seen:
                    continue
                seen.add(key)
                buckets.setdefault(sc, []).append(ret - pm)
    if not buckets:
        return []
    out = ["", "### 斷 state 比較（§8：state 期間每週超額——轉變事件切段，"
           "非事件窗口）", "",
           "唔只睇轉變嗰一刻：假說**處於**某個 state 的整段期間，股價相對"
           "全池係咪都有分別？單位＝ticker×週×state（去重）。", "",
           "| state | 段數 | 週樣本 | 週超額均值 | 週超額中位 |",
           "|---|---|---|---|---|"]
    for sc in sorted(buckets, reverse=True):
        vals = buckets[sc]
        out.append(f"| {_STATE_ZH.get(sc, sc)} | {n_segs.get(sc, 0)} | "
                   f"{len(vals)} | {_pct(statistics.mean(vals))} | "
                   f"{_pct(statistics.median(vals))} |")
    mono = [statistics.mean(buckets[sc]) for sc in sorted(buckets, reverse=True)]
    is_mono = all(a >= b for a, b in zip(mono, mono[1:]))
    out += ["", ("週超額均值隨 state 轉差而單調下行 ✓——state 唔只喺轉變一刻"
                 "有訊息，期間都有。" if is_mono else
                 "週超額均值**未**隨 state 單調下行——state 層訊息可能集中喺"
                 "轉變一刻（事件窗口），期間持有無著數；如實呈報。"),
            "誠實聲明：樣本只含曾轉變的假說（存活偏差）；同一 ticker 的多個"
            "假說共用同一條價格序列，組間非獨立；回補段與實時段混合（分層"
            "見上表）。"]
    return out


def markdown_tables(events: list[dict], clusters: list[dict],
                    all_events: list[dict] | None = None,
                    legs: dict | None = None,
                    tlegs: dict | None = None) -> str:
    cl_of = lambda r: r.get("cluster_id")  # noqa: E731
    head = "| " + " | ".join(f"+{h}週" for h in HORIZONS) + " |"
    sep = "|" + "---|" * HORIZONS[-1]
    out = []

    out += ["### 超額回報曲線（主表：扣除同期全池中位；每格＝均值（事件數/獨立cluster數）；窗口跨越同假說下一次轉變的格＝下一個 state 的行情，按 state 持有規則剔除）", ""]
    out += ["| 方向 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級"), ("lateral", "橫向")):
        grp = [e for e in events if e.get("direction") == dr]
        out.append(f"| {zh} | {len(grp)} | {_curve_cells(grp, 'excess_h', cl_of)} |")
    out += ["", "### 原始回報曲線（參考：未扣大盤）", ""]
    out += ["| 方向 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    for dr, zh in (("downgrade", "降級"), ("upgrade", "升級")):
        grp = [e for e in events if e.get("direction") == dr]
        out.append(f"| {zh} | {len(grp)} | {_curve_cells(grp, 'fwd_h', cl_of)} |")

    out += ["", "### 降級事件 × 重要度（超額口徑）", ""]
    out += ["| 重要度 | 事件數 | " + head[2:], "|---|---|" + sep[1:]]
    downs = [e for e in events if e.get("direction") == "downgrade"]
    for g in GRADE_ORDER:
        grp = [e for e in downs if (e.get("impact_grade") or "") == g]
        out.append(f"| {_glabel(g)} | {len(grp)} | "
                   f"{_curve_cells(grp, 'excess_h', cl_of)} |")

    # 訊號純度（H-purity）：同週淨方向——純降／混合／純升，逐類對照。
    out += ["", "### 訊號純度 × 結果（假說 H-purity：同週有升有降＝訊號抵銷，"
            "不應與純降級週混計）", "",
            "逐檔股票逐週看：該週是全部降級、有升有降、還是全部升級？"
            "混合週的降級不是乾淨的壞消息——同一棵樹另一條分支同週在改善。",
            "",
            "| 週類型 | cluster 數 | 有價格 | 平均超額 +1週 | 平均超額 +2週 | 28日內再有降級 |",
            "|---|---|---|---|---|---|"]
    _MIX_ZH = {"down_only": "純降級週", "mixed": "混合週（有升有降）",
               "up_only": "純升級週", "lateral_only": "僅橫向週"}
    def _cl_hold(c: dict, h: int) -> bool:
        nd = c.get("next_state_change_days")
        return nd is None or nd >= 7 * h

    for m in ("down_only", "mixed", "up_only", "lateral_only"):
        grp = [c for c in clusters if c.get("mix_type") == m]
        if not grp:
            continue
        e1 = [x for x in (_f(c, "excess_h1") for c in grp if _cl_hold(c, 1))
              if x is not None]
        e2 = [x for x in (_f(c, "excess_h2") for c in grp if _cl_hold(c, 2))
              if x is not None]
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
        e1 = [x for x in (_f(c, "excess_h1") for c in grp if _cl_hold(c, 1))
              if x is not None]
        p_dn = (sum(1 for c in grp if c["fut_downgrades_28d"] > 0) / len(grp)
                if grp else 0)
        out.append(
            f"| {label} | {len(grp)} | {len(e1)} | "
            f"{_pct(statistics.mean(e1)) if e1 else '—'} | — | {p_dn * 100:.0f}% |")
    out += ["", "純度注意：H-purity 由維護者於 2026-07-22 檢視樣本後提出，上表對"
            "現有樣本屬 in-sample 探索（假說由同一批數據啟發，不能用同一批數據"
            "證明自己）；對之後累積的新樣本才具預登記檢定效力。"]

    # 廣度 × cascade：同週轉變愈多，未來 28 日是否更大機會繼續轉差？
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

    out += era_section(events)
    out += age_section(events)
    out += priced_in_section(events)
    out += ic_section(clusters)
    out += branch_audit_section(events)
    if legs is not None and tlegs is not None:
        out += state_segment_section(all_events or events, legs, tlegs)
    return "\n".join(out)


# ---- 入口 ------------------------------------------------------------------

def build(raw_events_path: str, quant_root: str, outdir: str) -> str:
    """讀 raw 事件表 → 寫 events.csv（v2）＋ clusters.csv → 回傳結果表 markdown。

    model_transition 事件（判讀模型切換首個判讀日的重新評分潮）**自
    2026-07-28 起計入統計**：維護者逐筆覆核後確認該批判定改動本身站得住，
    非單純換模型造成的雜訊，故當背景資料照計。旗保留於 events.csv，任何人
    可自行剔走重算。

    vocab_migration 則仍然剔除——那批是同一個判斷換一套詞彙重述一次，
    不是新資訊，與 recode 同性質。"""
    with open(raw_events_path, encoding="utf-8") as f:
        all_events = list(csv.DictReader(f))
    legs, tlegs = load_pool_legs(quant_root)
    all_events = enrich(all_events, legs)
    # 2026-07-28：模型遷移旗由「剔除」改為「照計」（維護者覆核後認可）。
    n_trans = sum(1 for e in all_events if str(e.get("model_transition")) == "True")
    events = list(all_events)
    # 詞彙遷移剔除（SPEC §7，v3.3）：05-12..15 舊 3 值詞彙成批 remap 至
    # 6 值制＋其後首個判讀週（05-16）的重新評分潮——一次性系統事件，非
    # 市場新聞——統計表剔除，原始行連 vocab_migration／tree_age_days 保留。
    n_setup = sum(1 for e in events if str(e.get("vocab_migration")) == "True")
    events = [e for e in events if str(e.get("vocab_migration")) != "True"]
    clusters = build_clusters(events)
    # state 持有時鐘（cluster 層，v3.4）：該 ticker 下一次升／降級事件
    # （不論任何旗——判定變了，state 就變）距 cluster 最後事件的日數；
    # 純度表以此剔除「窗口已跨入下一個 state」的格。
    _td: dict = {}
    for e in all_events:
        d = _pdate(e.get("date"))
        if d and e.get("direction") in ("downgrade", "upgrade"):
            _td.setdefault(e["ticker"], []).append(d)
    for t in _td:
        _td[t].sort()
    for c in clusters:
        last = _pdate(c.get("last_event") or "")
        nxt = next((d for d in _td.get(c["ticker"], []) if last and d > last), None)
        c["next_state_change_days"] = (nxt - last).days if (last and nxt) else None

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
    if n_setup:
        note += (f"\n**詞彙遷移剔除**：{n_setup} 個事件帶 `vocab_migration` 旗"
                 "（2026-05-12..15 艦隊由舊 3 值判定詞彙成批 remap 至 6 值制，"
                 "加上其後首個判讀週的重新評分潮——05-12..16 一週集中了 86% "
                 "的歷史升級事件；屬一次性系統事件，非市場新聞亦非樹齡效應："
                 "六月後新建樹首 14 日僅 1.8 事件/棵、方向均衡），已於上列"
                 "全部統計表剔除；原始行連 `tree_age_days` 保留於 events.csv，"
                 "供外部自行檢視。\n")
    if n_trans:
        note += (f"\n**模型遷移照計**：{n_trans} 個事件帶 `model_transition` 旗"
                "（2026-07-16/18 由 grok-4.5 遷移至 deepseek-v3.2／v4-pro，"
                "當日轉變量為常態 4–6 倍）。2026-07-28 起**計入**上列全部統計"
                "表——維護者逐筆覆核後確認該批判定改動本身站得住，非單純換"
                "模型造成的雜訊。旗完整保留於 events.csv，`model` 欄記錄每個"
                "事件的判讀模型年代，要剔走重算隨時可以。\n")
    return markdown_tables(events, clusters, all_events, legs, tlegs) + note


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
