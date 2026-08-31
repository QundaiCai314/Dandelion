**English** | [中文](README.zh-CN.md)

# Dandelion · Business Loop Diagnosis

A skill for any AI agent: assess whether a **digital product / SaaS / software / App / subscription service** design closes the business loop, helping creators build business thinking.

一个面向所有 AI agent 的 skill（技能）：判断一个数字产品 / SaaS 的设计是否打通了商业链路，帮助创造者补充商业思维。

## What It Does
- **Two modes**: ① Self-Check — creators review their own product via one-question-at-a-time Q&A; ② Project Inspection — directly inspect a GitHub repo / local project / product description and produce a report.
- **Market research first**: every diagnosis starts with a web desk-research pass — `references/market_research.py` searches the web for 8 market metrics (user persona, market scope, pain points, willingness to pay, payment habits, competitors, market size, channels) and scores each 0-10 with evidence sources; without an API key it degrades to a search plan + agent-filled evidence form
- **Community signals**: the research engine adds site-targeted queries (`site:reddit.com`, `site:news.ycombinator.com`, `site:zhihu.com`, `site:indiehackers.com` ...) and the report gains a "Community Signals" section listing real user discussions to cross-check demand
- Seven-stage loop model: Market Research → Real Demand → Value Proposition → Acquisition → Paid Conversion → Delivery & Experience → Retention & Referral
- Each stage scored 0-10, with clear verdict rules: **Loop Closed / Nearly Closed / Not Closed**
- Full report: Diagnosis → Scores → Problem List → Fix Plan → Action Plan
- When inspection finds problems, the skill asks **"Is this your own project?"**: for others' projects it reports based on public evidence and flags missing evidence; for your own, it asks you to supply materials or answers questions one by one, then re-scores
- **Repair Mode**: after diagnosis, outputs a complete fix plan per problem (goal, concrete changes, steps, acceptance criteria) for YOU to execute; the AI only refines the plan, answers questions, and re-checks — it never modifies your product directly
- **Interview Mode (optional)**: a Mom Test-style interview coach (`references/interview.md`) — one question at a time, evidence logging, feed-back into the evidence form
- **Unit economics (optional)**: `references/economics.py` computes gross margin, LTV, LTV/CAC and payback period when you have numbers
- **Productize (optional)**: `references/pitch-template.md` turns the verdict into a 30-second pitch, one-line value proposition, landing-page hero, pricing cards and cold-start channels
- **Export**: generates a shareable Markdown report (`business-chain-report.md`)
- Evidence-first: stages without evidence are capped at 3 and flagged; no guessing
- **Scoring calculator**: optional `references/scoring.py` verifies the average, verdict and action priority for consistent results

## Market Research Engine
Every diagnosis starts with a market-research pass. The engine `references/market_research.py` searches the web and scores 8 metrics (each 0-10, machine evidence scores):

| Metric | What it verifies |
| --- | --- |
| User Persona | target segment exists, is active, discussed publicly |
| Market Scope | segment size can be bounded and estimated |
| Pain Points | pain is discussed publicly, concrete scenario/frequency |
| Willingness to Pay | paid products exist, pricing benchmarks, paid discussions |
| Payment Habits | payment methods, subscription habits, price sensitivity |
| Competitors | number, leaders, differentiation space |
| Market Size | TAM/SAM, public data and trends |
| Channels | where target users gather |

**Community signals**: besides general queries, the plan includes site-targeted queries for community-relevant metrics (user persona, pain points, willingness to pay, competitors, channels). Live search collects them into a "Community Signals" section of the report; in degraded mode the checklist is written to `community_plan` in `evidence_fill_form.json` for the agent to run and fill back into `community_signals`.

**Search backends** (auto-detected in order; set any one):
- `TAVILY_API_KEY` — https://tavily.com (recommended)
- `SERPER_API_KEY` — https://serper.dev (Google search)
- `BING_API_KEY` — Bing Web Search API

**Set up a search key (optional, ~2 min)** — only needed if you want the script to search the web by itself:
1. Pick one provider and get a free API key:
   - Tavily (recommended, agent-friendly): https://tavily.com → Dashboard → API Keys
   - Serper (Google results): https://serper.dev → API Key
   - Bing: Azure portal → Bing Web Search resource → Keys & Endpoint
2. Set the key as an environment variable (name must match the provider):
   - Windows PowerShell: `$env:TAVILY_API_KEY="tvly-xxxx"` (current session) or `setx TAVILY_API_KEY "tvly-xxxx"` (permanent)
   - macOS/Linux: `export TAVILY_API_KEY="tvly-xxxx"` (add to `~/.zshrc` or `~/.bashrc` to persist)
3. Verify: `python references/market_research.py --product "test product"` shows a live backend (e.g. `tavily`) instead of `no API key`.

Run:
```
python references/market_research.py --product "one-line product description"
```

Optional flags: `--target-user "<who>"`, `--market "<where>"`, `--lang zh|en|auto` — same fields as product.json.

**No API key?** The script degrades automatically: it writes a search plan + `evidence_fill_form.json`; the agent completes the evidence with its own web search, then scores:
```
python references/market_research.py --score-only evidence_fill_form.json
```
Scores combine result count + credible sources + concrete numbers + a weak relevance discount. The agent may calibrate with `--calibrate <file>` after reading the actual results.
Re-running never wipes a filled evidence form: evidence is preserved and only queries refresh; a form belonging to another product is refused unless `--force`.
Paths are relative to the skill directory — resolve the absolute path (e.g. `<skill_dir>/references/market_research.py`) when your working directory is not the skill root. Requires Python 3.8+.

## Unit Economics Calculator
`references/economics.py` turns pricing/cost numbers into the unit-economics metrics used by the Paid Conversion stage:
- Input: `price` (per month / year / one-time), `unit_cost`, `cac`, `monthly_churn` (or `annual_churn`), optional `gross_margin_pct`
- Output: gross margin %, customer lifetime, LTV, LTV/CAC, payback period
- Verdict: LTV/CAC ≥ 3 healthy · 1-3 needs work · <1 broken signal
- Usage: `python references/economics.py economics.json --json` or `--interactive`
- Rule: with numbers you must compute; without numbers the stage is marked "not measured" — never guessed

## Interview Mode (optional)
`references/interview.md` — a Mom Test-style interview script: hard rules (fewer than 3 real target users = never claim "interviewed"; past behavior only; never pitch), a per-stage question bank, a good-vs-bad question table, an interview log template, and how to feed evidence back into `evidence_fill_form.json` before re-scoring. Interviews are optional — having none is not a low-score reason; they upgrade "clearly defined but not cross-checked" into "aligned + cross-checked".

## Productize (optional)
`references/pitch-template.md` — after the diagnosis, ask "productize my pitch" and the AI produces: a 30-second pitch, a one-line value proposition, landing-page above-the-fold structure, a 3-tier pricing card, and a cold-start channel checklist. Materials are FOR the user; the AI never edits the product directly.

## Install
Copy this repository directory (default folder name `Dandelion`, containing SKILL.md) into your agent's skills directory, or clone and copy:
```
git clone https://github.com/QundaiCai314/Dandelion.git
```

| Agent | Directory |
| --- | --- |
| Claude Code | ~/.claude/skills/ or project .claude/skills/ |
| Codex | ~/.codex/skills/ or project .codex/skills/ |
| Cursor | project .cursor/skills/ |
| Others | follow the agent's skills install directory |

## Usage
Self-check: "Use the business-chain-diagnosis skill to review my product: <one-line description>"

Project inspection: "Use the business-chain-diagnosis skill to inspect this project: <repo URL / local path>"

Interview: "Use the skill for an interview deep-dive on my product"

Repair: "After the diagnosis, help me fix the acquisition stage"

Re-check: "Re-check with my current situation"

Productize: "Productize my pitch"

Export: "Export the report to a file"

## Structure
- SKILL.md — main skill file (trigger description, two-mode workflow, repair & export workflow, core rules)
- references/market_research.py — market research engine (multi-backend web search: Tavily / Serper / Bing; community-targeted queries + Community Signals section; no-key fallback generates a search plan + evidence fill form)
- references/framework.md — loop model, self-check questions, per-stage checklists, scoring, verdict rules, repair playbook & re-check rules
- references/interview.md — Mom Test-style interview script (optional evidence deep-dive)
- references/economics.py — unit economics calculator (gross margin, LTV/CAC, payback)
- references/pitch-template.md — productize template (pitch / landing hero / pricing cards)
- references/output-template.md — report template & export notes
- references/scoring.py — optional scoring calculator (average, verdict, action priority)
- docs/comparison.md — comparison vs similar tools & positioning
- examples/example-output.md — example report
- LICENSE — MIT License

## How It Compares
See [docs/comparison.md](docs/comparison.md) for a side-by-side with similar tools (venture-analyst, idea-os, Hermes biz-strategy, reddit-business-idea-validator, Business Idea Validator MCP, pmf-kit, launchlens, ...). Dandelion's edge: inspects EXISTING projects/repos (not just ideas), full 7-stage loop with a repair → re-check cycle, an ownership gate (own vs others' projects), and a no-key-first research engine.

## Scoring Rules
- Each stage 0-10: ≥7 healthy; 5-6.9 weak; <5 broken
- Loop closed: all stages ≥7 and average ≥7.5
- Nearly closed: no stage <5, average ≥7, but some stage <7
- Not closed: any stage <5, or average <7
- Real Demand and Paid Conversion demand strict evidence; Retention & Referral with zero design is broken outright
- Others' projects: verdict is labeled "based on public evidence"; your own project: unanswered/unverified counts as weak
- Market Research: no research ≤3; researched but thin ≤6; 7+ requires all 8 metrics backed by evidence consistent with the product claims
- Deep judgment: vague/misaligned ≤3; clearly defined but not cross-checked ≤6; 7+ requires aligned demand cross-checked via desk research (interviews/data not required); Retention & Referral with no design ≤2
- Unit economics: with numbers compute LTV/CAC via references/economics.py (≥3 healthy, <1 broken); without numbers mark "not measured"

## Tests & Version
- `python tests/test_sanity.py` — sanity tests for the scoring heuristics, the calculators and the community queries (stdlib only, no third-party dependencies)
- Version: 1.2.0

## License
Released under the [MIT License](LICENSE).
