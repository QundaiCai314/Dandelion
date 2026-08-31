**English** | [中文](README.zh-CN.md)

# Dandelion · Business Loop Diagnosis

A skill for any AI agent: assess whether a **digital product / SaaS / software / App / subscription service** design closes the business loop, helping creators build business thinking.

一个面向所有 AI agent 的 skill（技能）：判断一个数字产品 / SaaS 的设计是否打通了商业链路，帮助创造者补充商业思维。

## What It Does
- **Two modes**: ① Self-Check — creators review their own product via one-question-at-a-time Q&A; ② Project Inspection — directly inspect a GitHub repo / local project / product description and produce a report.
- **Market research first**: every diagnosis starts with a web desk-research pass — `references/market_research.py` searches the web for 8 market metrics (user persona, market scope, pain points, willingness to pay, payment habits, competitors, market size, channels) and scores each 0-10 with evidence sources; without an API key it degrades to a search plan + agent-filled evidence form
- Seven-stage loop model: Market Research → Real Demand → Value Proposition → Acquisition → Paid Conversion → Delivery & Experience → Retention & Referral
- Each stage scored 0-10, with clear verdict rules: **Loop Closed / Nearly Closed / Not Closed**
- Full report: Diagnosis → Scores → Problem List → Fix Plan → Action Plan
- When inspection finds problems, the skill asks **"Is this your own project?"**: for others' projects it reports based on public evidence and flags missing evidence; for your own, it asks you to supply materials or answers questions one by one, then re-scores
- **Repair Mode**: after diagnosis, outputs a complete fix plan per problem (goal, concrete changes, steps, acceptance criteria) for YOU to execute; the AI only refines the plan, answers questions, and re-checks — it never modifies your product directly
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

**No API key?** The script degrades automatically: it writes a search plan + `evidence_fill_form.json`; the agent completes the evidence with its own web search, then scores:
```
python references/market_research.py --score-only evidence_fill_form.json
```
Scores combine result count + credible sources + concrete numbers + a weak relevance discount. The agent may calibrate with `--calibrate <file>` after reading the actual results.
Re-running never wipes a filled evidence form: evidence is preserved and only queries refresh; a form belonging to another product is refused unless `--force`.
Paths are relative to the skill directory — resolve the absolute path (e.g. `<skill_dir>/references/market_research.py`) when your working directory is not the skill root. Requires Python 3.8+.

## Install
Copy this repository directory (default folder name `Dandelion`, containing SKILL.md) into your agent's skills directory.

| Agent | Directory |
| --- | --- |
| Claude Code | ~/.claude/skills/ or project .claude/skills/ |
| Codex | ~/.codex/skills/ or project .codex/skills/ |
| Cursor | project .cursor/skills/ |
| Others | follow the agent's skills install directory |

## Usage
Self-check: "Use the business-chain-diagnosis skill to review my product: <one-line description>"

Project inspection: "Use the business-chain-diagnosis skill to inspect this project: <repo URL / local path>"

Repair: "After the diagnosis, help me fix the acquisition stage"

Re-check: "Re-check with my current situation"

Export: "Export the report to a file"

## Structure
- SKILL.md — main skill file (trigger description, two-mode workflow, repair & export workflow, core rules)
- references/market_research.py — market research engine (multi-backend web search: Tavily / Serper / Bing; no-key fallback generates a search plan + evidence fill form)
- references/framework.md — loop model, self-check questions, per-stage checklists, scoring, verdict rules, repair playbook & re-check rules
- references/output-template.md — report template & export notes
- references/scoring.py — optional scoring calculator (average, verdict, action priority)
- examples/example-output.md — example report
- LICENSE — MIT License

## Scoring Rules
- Each stage 0-10: ≥7 healthy; 5-6.9 weak; <5 broken
- Loop closed: all stages ≥7 and average ≥7.5
- Nearly closed: no stage <5, average ≥7, but some stage <7
- Not closed: any stage <5, or average <7
- Real Demand and Paid Conversion demand strict evidence; Retention & Referral with zero design is broken outright
- Others' projects: verdict is labeled "based on public evidence"; your own project: unanswered/unverified counts as weak
- Market Research: no research ≤3; researched but thin ≤6; 7+ requires all 8 metrics backed by evidence consistent with the product claims
- Deep judgment: vague/misaligned ≤3; clearly defined but not cross-checked ≤6; 7+ requires aligned demand cross-checked via desk research (interviews/data not required); Retention & Referral with no design ≤2

## Tests & Version
- `python tests/test_sanity.py` — sanity tests for the scoring heuristics and the calculator (stdlib only, no third-party dependencies)
- Version: 1.1.0

## License
Released under the [MIT License](LICENSE).




