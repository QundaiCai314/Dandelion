#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Dandelion sanity tests (stdlib only, no third-party deps).

Run: python tests/test_sanity.py
"""

import importlib.util
import io
import json
import os
import subprocess
import sys
import tempfile

REPO = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def load_module(name, relpath):
    path = os.path.join(REPO, relpath)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_market_research():
    mr = load_module("market_research", os.path.join("references", "market_research.py"))
    # is_credible: hostname-based, no substring false positives
    assert mr.is_credible("https://www.wsj.com/foo") is True
    assert mr.is_credible("https://github.com/org/repo") is True
    assert mr.is_credible("https://notgithub.com/x") is False
    assert mr.is_credible("https://www.hey.com/x") is False  # "ey.com" substring trap
    assert mr.is_credible("https://state.gov/page") is True
    assert mr.is_credible("") is False
    # is_specific: digits with units + Chinese 成
    assert mr.is_specific("增长 40%") is True
    assert mr.is_specific("近八成用户愿意付费") is True
    assert mr.is_specific("团队 3 人") is True
    assert mr.is_specific("毫无信息") is False
    # score_evidence: empty, relevance discount
    assert mr.score_evidence([]) == 0.0
    on_topic = [{"title": "报告：某市场增长 40%", "url": "https://www.wsj.com/a",
                 "snippet": "用户 10 万人，订阅 9.9 元/月"}]
    off_topic = [{"title": "天气晴", "url": "https://example.org/x",
                  "snippet": "今天气温 30 度"}]
    high = mr.score_evidence(on_topic, "用户 市场 订阅 付费 增长")
    low = mr.score_evidence(off_topic, "出海 一人公司 工具箱")
    assert high > low
    assert mr.score_evidence(on_topic, "") == mr.score_evidence(on_topic)  # backward compatible
    assert mr.score_evidence(on_topic, ["用户", "市场"]) == mr.score_evidence(on_topic, "用户 市场")  # list queries
    # query_keywords: strips stopwords, keeps CJK runs
    kw = mr.query_keywords("面向国内出海创业者的一人公司工具箱：自动化建站")
    assert "一人公司" in kw and kw == kw.strip()
    # default_queries: 8 metrics, <=3 queries each
    qs = dict(mr.default_queries(
        "面向国内出海创业者的一人公司工具箱：自动化建站、营销与合规检查的 SaaS",
        "已决定出海、正在选工具的一人创业者（Solopreneur）", "zh"))
    assert len(qs) == 8
    assert all(qs[mid] for mid, _, _ in mr.METRICS)
    assert all(len(q) <= 3 for q in qs.values())


def _run_scoring(data, allow_nan=False):
    sc = load_module("scoring", os.path.join("references", "scoring.py"))
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, "s.json")
        with open(p, "w", encoding="utf-8") as f:
            json.dump(data, f, allow_nan=allow_nan)
        out = io.StringIO()
        old = sys.stdout
        sys.stdout = out
        try:
            rc = sc.main([p, "--json"])
        finally:
            sys.stdout = old
        raw = out.getvalue()
        return rc, (json.loads(raw) if rc == 0 else None), sc


def test_scoring_calculator():
    keys = ["market_research", "real_demand", "value_proposition", "acquisition",
            "paid_conversion", "delivery", "retention_referral"]
    data = {"scores": {k: 8 for k in keys}, "evidence": {k: "strong" for k in keys}}
    rc, parsed, _ = _run_scoring(data)
    assert rc == 0 and parsed["verdict"] == "loop_closed"
    # NaN must be rejected, not reported healthy
    bad = dict(data)
    bad["scores"]["real_demand"] = float("nan")
    rc, _, _ = _run_scoring(bad, allow_nan=True)
    assert rc == 1
    # evidence caps: weak -> 6, none -> 3
    capped = {"scores": {k: 8 for k in keys}, "evidence": {"real_demand": "weak"}}
    rc, parsed, _ = _run_scoring(capped)
    assert rc == 0
    assert parsed["scores"]["real_demand"] == 6.0
    assert any("封顶" in w or "cap" in w for w in parsed["warnings"])
    # missing evidence defaults to none (cap 3)
    no_ev = {"scores": {k: 8 for k in keys}}
    rc, parsed, _ = _run_scoring(no_ev)
    assert rc == 0 and parsed["scores"]["real_demand"] == 3.0


def test_community_queries():
    mr = load_module("market_research", os.path.join("references", "market_research.py"))
    assert mr.is_community("https://www.reddit.com/r/SaaS/comments/x") is True
    assert mr.is_community("https://news.ycombinator.com/item?id=1") is True
    assert mr.is_community("https://www.wsj.com/foo") is False
    cm = mr.community_queries("出海一人公司工具箱", "已决定出海的一人创业者", "zh")
    assert sorted(cm.keys()) == sorted(mr.COMMUNITY_METRICS)
    for mid in mr.COMMUNITY_METRICS:
        assert cm[mid] and any("site:" in q for q in cm[mid])
    cm_en = mr.community_queries("solo founder toolbox", "", "en")
    assert "site:reddit.com" in cm_en["channels"][0]


def test_economics_calculator():
    ec = load_module("economics", os.path.join("references", "economics.py"))
    healthy = ec.calculate({"price": 20, "unit_cost": 4, "cac": 100, "monthly_churn": 0.04})
    assert healthy["verdict"] == "healthy" and healthy["ltv_cac"] == 4.0
    broken = ec.calculate({"price": 20, "cac": 200, "monthly_churn": 0.3})
    assert broken["verdict"] == "broken"
    insufficient = ec.calculate({"price": 20})
    assert insufficient["verdict"] == "insufficient"
    one_time = ec.calculate({"price": 299, "unit_cost": 30, "cac": 500, "period": "one_time"})
    assert one_time["ltv"] == 269.0


def test_cli_help():
    for rel in ("references/market_research.py", "references/scoring.py"):
        r = subprocess.run([sys.executable, os.path.join(REPO, rel), "--help"],
                           capture_output=True, text=True)
        assert r.returncode == 0


def test_cli_flags():
    mr = os.path.join(REPO, "references", "market_research.py")
    with tempfile.TemporaryDirectory() as td:
        r = subprocess.run(
            [sys.executable, mr, "--product", "测试产品X", "--target-user", "已决定出海的一人创业者",
             "--market", "全球", "--lang", "zh", "--out", "r.json", "--format", "md"],
            cwd=td, capture_output=True, text=True, encoding="utf-8")
        assert r.returncode == 0, r.stderr
        with open(os.path.join(td, "evidence_fill_form.json"), encoding="utf-8") as f:
            form = json.load(f)
        assert form["product"] == "测试产品X"
        assert form["metrics"]["user_persona"]["queries"]
        assert "community_plan" in form and form["community_plan"]["pain_point"]
        with open(os.path.join(td, "r.json"), encoding="utf-8") as f:
            rep = json.load(f)
        assert rep["product"] == "测试产品X" and rep["target_user"] == "已决定出海的一人创业者"


if __name__ == "__main__":
    failed = 0
    for name in sorted(globals()):
        fn = globals()[name]
        if name.startswith("test_") and callable(fn):
            try:
                fn()
                print("PASS %s" % name)
            except Exception as e:  # noqa: BLE001
                failed += 1
                print("FAIL %s: %s" % (name, e))
    if failed:
        print("%d test(s) failed" % failed)
        sys.exit(1)
    print("all tests passed")
