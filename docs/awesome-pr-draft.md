# Awesome 清单投稿草稿 Awesome List Submission Draft

本文件是给「分发」用的现成投稿材料：README 条目、PR 标题与正文、Git 命令、SKILL.md 适配清单。
Ready-to-paste materials for listing Dandelion on the major skill directories.

## 目标清单 Target lists
1. ComposioHQ/awesome-claude-skills — 最大清单（1000+ skills），明确支持 Codex / Cursor / Gemini CLI 等跨 agent
2. VoltAgent/awesome-agent-skills — 跨 agent 清单，一行命令安装：npx skills add QundaiCai314/Dandelion
3. (可选) FridrichMethod/awesome-skills — 表格形式目录

## 1. ComposioHQ/awesome-claude-skills
投稿方式 Submission flow：
1. Fork 仓库：gh repo fork ComposioHQ/awesome-claude-skills --clone
2. 建分支：git checkout -b add-business-chain-diagnosis
3. 新增目录 business-chain-diagnosis/，内含按对方 8 段结构适配的 SKILL.md（见下方清单）
4. 改 README.md：在 Business & Marketing 分类按字母序插入一行
5. 提交、推送、开 PR

### README 条目（Business & Marketing 分类，字母序在 Brand Guidelines 之后、Competitive Ads Extractor 之前）
- [Business Loop Diagnosis](./business-chain-diagnosis/) - Assess whether a digital product or SaaS design closes its business loop: market research first, 7-stage 0-10 scoring, complete fix plans and re-checks. By @QundaiCai314

### PR 标题 PR title
Add Business Loop Diagnosis skill

### PR 正文 PR body
**Problem** — Solo founders and indie hackers lack a rigorous way to check whether their product design actually closes the business loop (demand → value → acquisition → payment → delivery → retention). Most validation tools only evaluate raw ideas, not existing products or repositories.

**Who it is for** — Solo founders, indie hackers and product creators who want business thinking on their own product; also useful for evaluating other people's repos from public evidence only.

**What it does** — Every diagnosis starts with a web market-research pass (references/market_research.py: multi-backend search Tavily/Serper/Bing with a no-key fallback plus a free Hacker News capture), then scores 7 stages (Market Research → Real Demand → Value Proposition → Acquisition → Paid Conversion → Delivery & Experience → Retention & Referral) and outputs: a problem list, a complete fix plan per problem (goal, changes, steps, acceptance criteria), optional Mom Test interview coach, unit-economics calculator (LTV/CAC), productization templates (pitch/landing page), and a re-check workflow with score baselines.

**Usage example** — User: "Use the business-chain-diagnosis skill to review my product: <one-line description>" → a 0-10 scored report with fix plans. Or: "inspect this project: <repo URL>" → an evidence-based report with an ownership gate (own vs others' projects).

**Attribution** — Original work; concepts reference lean canvas, Mom Test and AARRR.

**Tested** — 7 sanity tests (tests/test_sanity.py, stdlib only) plus real product runs in no-key degraded mode and agent-filled scoring mode.

### Git 命令 Git commands
gh repo fork ComposioHQ/awesome-claude-skills --clone
cd awesome-claude-skills
git checkout -b add-business-chain-diagnosis
# 复制并适配 SKILL.md 到 business-chain-diagnosis/SKILL.md
git add business-chain-diagnosis/ README.md
git commit -m "Add Business Loop Diagnosis skill"
git push -u origin add-business-chain-diagnosis
gh pr create --title "Add Business Loop Diagnosis skill" --body-file pr-body.md

### SKILL.md 适配清单（对方要求的 8 段结构）
- [x] YAML frontmatter：name 必须与目录名 business-chain-diagnosis 一致；description 单句
- [x] # Skill Name（H1）
- [x] Description 段落
- [x] ## When to Use This Skill（可复用 frontmatter 里的 Use when 描述）
- [x] ## What This Skill Does（两条路线 + 诊断之后 + 核心规则）
- [x] ## How to Use（流程）
- [x] ## Example（补一个「用户说 X → 得到 Y」示例）
- [x] ## Tips（核心规则）
- [x] ## Common Use Cases（补 3-5 个典型场景）
提交前可按此清单把 SKILL.md 补齐（保持双语）。

## 2. VoltAgent/awesome-agent-skills
投稿方式：在该仓库提 Issue 或 PR，把仓库加进 community skills 区，附安装命令。
### Issue/PR 标题
Add QundaiCai314/Dandelion to community skills
### 内容 Content
- Repo: https://github.com/QundaiCai314/Dandelion
- Install: npx skills add QundaiCai314/Dandelion
- Description: A skill for any AI agent (Claude Code / Codex / Cursor / Gemini CLI) to assess whether a digital product or SaaS design closes its business loop — market research first (multi-backend search, no key required, free Hacker News capture), 7-stage 0-10 scoring, complete fix plans, re-checks with score baselines.
- Evidence: 7 sanity tests pass; runnable end-to-end without any API key.

## 3. (可选) FridrichMethod/awesome-skills
README 表格条目（复制到对应分类）：
| [Dandelion](https://github.com/QundaiCai314/Dandelion) | ★ | Assess whether a digital product/SaaS design closes its business loop: market research engine, 7-stage 0-10 scoring, complete fix plans, re-checks |

## 提交前自查 Pre-submit checklist
- [ ] README 条目：无 emoji、句号结尾、分类内字母序
- [ ] SKILL.md：8 段结构齐全、name 与目录一致
- [ ] PR 正文含：Problem / Who / What / Example / Attribution / Tested
- [ ] 分支名 add-business-chain-diagnosis；commit 与 PR 标题一致
