**English** | [中文](README.zh-CN.md)

# Dandelion · Business Loop Diagnosis

A skill for any AI agent: assess whether a **digital product / SaaS / software / App / subscription service** design closes the business loop, helping creators build business thinking.

一个面向所有 AI agent 的 skill（技能）：判断一个数字产品 / SaaS 的设计是否打通了商业链路，帮助创造者补充商业思维。

## What It Does
- **Two modes**: ① Self-Check — creators review their own product via one-question-at-a-time Q&A; ② Project Inspection — directly inspect a GitHub repo / local project / product description and produce a report.
- Six-stage loop model: Real Demand → Value Proposition → Acquisition → Paid Conversion → Delivery & Experience → Retention & Referral
- Each stage scored 0-10, with clear verdict rules: **Loop Closed / Nearly Closed / Not Closed**
- Full report: Diagnosis → Scores → Problem List → Fix Plan → Action Plan
- When inspection finds problems, the skill asks **"Is this your own project?"**: for others' projects it reports based on public evidence and flags missing evidence; for your own, it asks you to supply materials or answers questions one by one, then re-scores
- **Repair Mode**: after diagnosis, outputs a complete fix plan per problem (goal, concrete changes, steps, acceptance criteria) for YOU to execute; the AI only refines the plan, answers questions, and re-checks — it never modifies your product directly
- **Export**: generates a shareable Markdown report (`business-chain-report.md`)
- Evidence-first: stages without evidence are capped at 3 and flagged; no guessing
- **Scoring calculator**: optional `references/scoring.py` verifies the average, verdict and action priority for consistent results

## Install
Copy this repository directory (default folder name `dandelion`, containing SKILL.md) into your agent's skills directory.

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

## License
Released under the [MIT License](LICENSE).

