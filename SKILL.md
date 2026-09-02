---
name: business-chain-diagnosis
description: '商业链路诊断（Business Loop Diagnosis）。每次诊断先跑全网市场调研：运行 references/market_research.py 联网搜索 8 项市场指标（用户画像/群体范围/痛点/付费意愿/付费习惯/竞品/市场规模/渠道）并按证据打分，无 API key 时自动降级为检索清单+agent 补查。当用户想判断数字产品/SaaS/软件/App/订阅服务的设计是否打通商业链路，或希望 AI 帮助补充商业思维时使用。支持自检模式（一问一答逐环节自检）与项目检查模式（直接检查 GitHub 仓库/本地项目/产品描述，发现问题时询问项目归属）。诊断后提供修复模式：AI 为每个问题输出完整修改方案（目标、具体改动、实施步骤、验收标准），由用户自己执行；支持导出可分享的 Markdown 诊断报告。可选：Mom Test 访谈教练、社区直抓信号、单位经济学测算（LTV/CAC）、产品化输出（pitch/落地页文案）。输出：逐环节诊断、0-10 打分、链路结论、问题清单、修复方案、行动清单。Use when the user wants to assess whether a digital product or SaaS design closes the business loop, either as a creator self-checking via Q&A, or by inspecting a project/repo; provide complete fix plans for the user to execute, and export a shareable report. Optional: Mom Test interview coach, community-signal capture, unit-economics (LTV/CAC) calculator, productization (pitch/landing copy).'
---

# 商业链路诊断 Business Loop Diagnosis

判断一个数字产品/SaaS 的设计是否打通了商业链路，帮助创造者补充商业思维。判断严格与否，看的是「想得够不够深、需求有没有对齐」，而不是有没有访谈或使用数据——个人做工具在起步阶段没有这些是正常的。他人项目证据不足时明确标记，禁止臆测。
Assess whether a digital product/SaaS design closes the business loop, helping creators build business thinking. Strictness is about depth of thinking and whether the demand is aligned — not about having interviews or usage data, which a solo founder naturally lacks at the start. Clearly flag missing evidence for projects of others; never speculate.

## When to Use This Skill 何时使用
当出现以下情况时使用本 skill：
Use this skill when:
- 用户想判断自己的数字产品 / SaaS / 软件 / App / 订阅服务设计是否打通了商业链路，或希望 AI 帮助补充商业思维。
  The user wants to assess whether their digital product / SaaS / software / App / subscription design closes the business loop, or wants the AI to help build business thinking.
- 用户给出 GitHub 仓库、本地项目目录或产品描述，要求检查其商业链路是否成立。
  The user provides a GitHub repo, a local project directory, or a product description and asks whether its business loop holds.
- 用户拿到诊断结论后，希望为每个问题得到可执行的完整修改方案（目标、具体改动、步骤、验收标准）。
  After a diagnosis, the user wants a complete, executable fix plan per problem (goal, changes, steps, acceptance criteria).
- 用户希望做商业链路自检、访谈加深证据、单位经济测算或产品化输出（pitch / 落地页）。
  The user wants a self-check, deeper evidence via interview, unit-economics calculation, or productization output (pitch / landing page).
- 不需要使用的情况：纯技术实现、代码审查、与商业模式无关的问题。
  Not for: pure technical implementation, code review, or questions unrelated to business model.
## 两条路线 Two Modes
- **自检模式 Self-Check**：用户是创造者，对自己的产品做检查。默认一问一答，AI 按 7 环节依次提问（先跑市场调研再自检），用回答打分。
  Self-Check: the user is the creator reviewing their own product. By default one question at a time; the AI walks through the 7 stages in order (market research first) and scores from the answers.
- **项目检查模式 Project Inspection**：用户给出项目本身（GitHub 仓库 / 本地目录 / 产品描述），AI 直接检查整个项目。发现问题时询问项目归属：别人的项目按公开证据出报告；自己的项目则请用户补充材料或切换为一问一答追问，重新打分。
  Project Inspection: the user provides the project itself (GitHub repo / local directory / product description) and the AI inspects it directly. When problems are found, the AI asks who owns the project: for projects of others it reports from public evidence; for your own, it asks you to supply materials or switches to one-question-at-a-time follow-up, then re-scores.
- **访谈加深 Interview**：可选。用户要求「访谈 / 访谈加深」时，AI 按 references/interview.md 扮演访谈教练：一次一问、记录证据并回填证据表单，再复检。
  Optional. On "interview" / "deep-dive", the AI coaches per references/interview.md: one question at a time, logs evidence back into the evidence form, then re-checks.

## 诊断之后 After Diagnosis
- **修复模式 Repair**：诊断报告后，AI 为每个问题输出**完整修改方案**（目标、具体改动、实施步骤、验收标准），由用户自己执行；AI 负责方案细化、答疑与复检，不直接修改用户的产品。
  After the report, the AI outputs a **complete fix plan** per problem (goal, concrete changes, steps, acceptance criteria) for the user to execute themselves; the AI only refines plans, answers questions, and re-checks — it never directly modifies the product.
- **结论输出 Export**：把完整结论输出为可保存/分享的 Markdown 报告文件。
  Export the full conclusion as a shareable Markdown report file.
- **产品化输出 Productize**：可选。按 references/pitch-template.md 生成 30 秒 pitch、一句话价值主张、落地页首屏、三档定价卡与冷启动渠道清单，作为给用户的材料。
  Optional. Produce pitch / value prop / landing hero / pricing cards / cold-start channels per references/pitch-template.md — materials for the user.

## 流程 Process
1. 判断模式：用户给的是项目/链接/目录，或要求「检查这个项目」→ 项目检查模式；用户说「帮我自检我的产品 / 看看我做得怎么样」→ 自检模式；不确定时先问一句：这是你自己的项目，还是要检查别人的？
   Determine the mode: a project/link/directory or a request to "inspect this project" → Project Inspection; "help me self-check my product / see how I am doing" → Self-Check; if unclear, ask first whether the project belongs to the user or to someone else.
2. 市场调研：正式诊断前，先运行 python references/market_research.py --product "<产品描述>"（有 API key 自动联网搜索；无 key 时按生成的 evidence_fill_form.json 由 agent 用自己的联网搜索补完证据，再以 --score-only 计算分数），产出 8 项市场指标（用户画像/群体范围/痛点/付费意愿/付费习惯/竞品/市场规模/渠道）的分数与证据来源，作为后续环节的外部核对依据；未运行调研时市场调研环节 ≤3 分。检索计划含社区定向查询（site:reddit.com / news.ycombinator.com / zhihu.com 等），报告输出「社区信号 Community Signals」板块；付费转化环节有定价/成本数字时运行 references/economics.py 测算 LTV/CAC。
   Market research: before diagnosis, run python references/market_research.py --product "<product>" (live search with an API key; without a key, complete evidence_fill_form.json via the agent's own web search, then --score-only), producing scores and evidence sources for the 8 market metrics (persona/scope/pain/willingness/habits/competitors/size/channels) as the external cross-checking basis; no research → the stage caps at 3.
   Paths & Python: all script/doc paths are relative to the skill directory — resolve the absolute path (e.g. <skill_dir>/references/market_research.py) when the working directory is not the skill root; requires Python 3.8+. The script preserves filled evidence (refuses to overwrite another product's form without --force); stage score = round(machine overall) capped by coverage, rules in references/framework.md. 路径以 skill 目录为基准：当前目录不是 skill 根目录时先解析绝对路径；需要 Python 3.8+；脚本不会覆盖已填证据；环节分 = 机器总体分按覆盖率封顶（见 references/framework.md）。附加参数 Additional flags：--target-user/--market/--lang（与 product.json 字段一致，便于命令行直接带参）。
3. 项目检查：多通道收集证据（README、docs、代码结构、官网、定价页、应用商店页、公开报道与社区讨论），逐环节诊断打分。
   Inspection: gather evidence from multiple channels (README, docs, code structure, website, pricing page, app store listing, public reports and community discussions), then diagnose and score each stage.
4. 发现问题时（任一环节 <5，或 ≥2 个环节 <7）：必须问「这是你自己的项目吗？」
   When problems are found (any stage <5, or ≥2 stages <7): you MUST ask "Is this your own project?"
   - 别人的 → 直接输出报告，无证据环节标注「证据不足」并列出需补充的信息，结论注明「基于公开证据，不代表产品真实状态」。
     Projects of others → output the report directly, mark evidence-starved stages as "insufficient evidence" and list what to supply, and note the verdict is "based on public evidence, not the true state of the product".
   - 自己的 → 问用户要「补充材料」还是「一个一个提问」（默认一个一个提问），补齐后重新打分再出报告。
     Your own → ask whether to supply materials or answer questions one by one (one-by-one is the default), then re-score with the new evidence and report.
   - 打分校验（可选）：把七环分数写成 JSON，运行 references/scoring.py，用脚本输出的平均分、结论与行动优先级（防止判定漂移）。
     Score verification (optional): write the seven scores to JSON, run references/scoring.py, and use its average, verdict and action priority (to prevent judgment drift).
5. 全部环节健康时 → 直接输出报告，不追问。
   If all stages are healthy → output the report directly, no follow-up.
6. 自检：按 7 环节顺序提问（市场调研先跑程序，其余环节一问一答），默认一次一个问题；答不上来的题记录为「未验证/未设计」并继续，不卡住；问完打分出报告。
   Self-Check: walk through the 7 stages in order (run the research script first, then one question at a time); unanswered questions are recorded as "unverified/undesigned" and you continue without blocking; score and report when done.
7. 修复：按优先级逐项进行（断裂 → 薄弱 → 全部健康后找增长杠杆）。每项修复：AI 输出**完整修改方案**——目标、具体改动、实施步骤、验收标准（如定价方案、落地页文案、激活指标、推荐机制等），用户确认或要求细化，然后**由用户自己执行修改**；一项落地后再进入下一项。AI 不直接改动用户的产品。用户可随时要求「复检」，用当前证据重新打分并对比变化（规则见 references/framework.md）。
   Repair: work through priorities one item at a time (broken → weak → growth levers once all healthy). For each item, the AI outputs a **complete fix plan** — goal, concrete changes, steps, acceptance criteria (e.g., pricing, landing-page copy, activation metrics, referral mechanics); the user confirms or asks to refine, then **executes the changes themselves**; move to the next item after one lands. The AI never directly modifies the product. The user may request a "re-check" anytime to re-score with current evidence and compare changes (see references/framework.md).
8. 输出：用户要求或一轮修复完成后，将结论输出为 Markdown 报告文件（默认保存到工作目录 business-chain-report.md），包含：报告信息、产品画像、逐环节诊断与打分、结论、问题清单、修复方案、修复进度、行动清单；也可直接在对话中展示或按需转换格式。
   Export: on request or after a repair round, output the conclusion as a Markdown report (default business-chain-report.md in the working directory) containing: report info, product snapshot, per-stage diagnosis and scores, verdict, problem list, fix plan, repair progress, action plan; may also be shown in chat or converted to another format on request.

## Example 示例
- 用户说：「检查这个项目的商业链路 https://github.com/QundaiCai314/pufa-hackathon-ai」
  → AI 先运行 references/market_research.py 做全网市场调研，再检查整个项目；输出逐环节诊断、七环 0-10 打分、链路结论、问题清单与每个问题的完整修复方案；发现问题时询问「这是你的项目还是别人的项目」；用户回答后按归属分支补充材料或按公开证据出报告，需要时复检重新打分。
  User: "Check whether this project closes the business loop: https://github.com/QundaiCai314/pufa-hackathon-ai"
  → The AI runs references/market_research.py first, then inspects the whole project; it outputs per-stage diagnosis, seven-stage 0-10 scores, a verdict, a problem list, and a complete fix plan per problem; when it finds problems it asks "is this your project or someone else's?" and then either collects more materials (own) or reports from public evidence (others), re-scoring on re-check.
- 用户说：「帮我的 SaaS 做一次商业链路自检」
  → AI 先跑市场调研程序，然后按 7 环节一问一答（一次一个问题，答不上记为未验证、不卡住），问完打分、出结论与修复优先级，可导出报告；用户可选择进入修复模式逐项落地。
  User: "Run a business-loop self-check on my SaaS"
  → The AI runs the research script first, then walks through the 7 stages one question at a time (unanswered → "unverified", no blocking), scores, gives the verdict and fix priorities, and can export a report; the user may enter Repair Mode to land fixes one by one.

## Common Use Cases 常见场景
1. 创造者上线前自检：SaaS / App 发布前用一问一答自查商业链路，得到分数、短板清单与修复优先级。
   Pre-launch self-check: a creator sanity-checks their SaaS/App via Q&A before launch and gets scores, weak spots, and fix priorities.
2. 评估他人的开源项目：只看公开证据判断一个 repo 是否具备商业闭环，明确区分「证据不足」与「设计缺失」。
   Evaluating someone else's open-source repo: judge whether it closes the business loop from public evidence only, distinguishing "insufficient evidence" from "missing design".
3. 需求对齐澄清：判断目标用户是否精确到「人群 + 决策状态 + 场景」，避免把「还没决定要不要出海」和「已决定出海在选工具」混为一谈。
   Demand alignment: check whether the target user is precise to "segment + decision state + scenario", avoiding conflation of adjacent segments.
4. 复购与传播设计：检查留存与推荐机制，无任何设计时直接判裂，并输出完整修复方案。
   Retention & referral: check retention and referral mechanics; none at all → broken outright, with a complete fix plan.
5. 上架 / 融资前的商业闭环体检：生成可分享的 Markdown 报告，用于内部对齐或对外展示。
   Pre-launch / pre-pitch health check: produce a shareable Markdown report for internal alignment or external presentation.
## 核心规则 Core Rules
- 市场调研证据先行：诊断开始前先跑 references/market_research.py。8 项指标全部有证据、且与产品主张一致 → 市场调研环节可 ≥7；已调研但证据单薄 → ≤6；未跑调研 → ≤3。
- 市场调研环节分换算：环节分 = round(机器总体证据分)，按覆盖率封顶——8/8 指标有证据且与主张一致 → strong 不封顶；4-7/8 → weak ≤6；<4/8 或未跑 → none ≤3。机器分是证据强度，0 分不代表市场不存在。
  Stage score = round(machine overall) capped by coverage: 8/8 evidenced & consistent → strong (no cap); 4-7/8 → weak (≤6); <4/8 or no research → none (≤3). Machine scores measure evidence strength; 0 does not mean the market does not exist.
  Market research evidence first: run references/market_research.py before scoring. All 8 metrics backed by evidence consistent with the product claims → 7+; researched but thin → ≤6; no research → ≤3.
- 判断深度优先：分数 = 定义深度 × 外部核对。起步阶段没有访谈/使用数据是正常的，不算低分理由；**说不清用户、需求未对齐（如相邻人群混淆）才是低分理由**。深度对齐 + 桌面研究核对 → 7 分以上；定义清晰但未核对 → ≤6；模糊未对齐 → ≤3。禁止臆测。
  Judgment depth first: score = definition depth × external cross-checking. Having no interviews/usage data at the start is normal and not a reason for a low score; **being unable to state the user or misaligning the demand (e.g., conflating adjacent segments) is**. Aligned demand cross-checked via desk research → 7+; clearly defined but not cross-checked → ≤6; vague/misaligned → ≤3. Never speculate.
- 他人项目：低分只代表「公开证据不足或设计缺失」，报告必须区分两者，不得断言产品失败。
  Projects of others: a low score only means "insufficient public evidence or missing design"; the report must distinguish the two and must not declare the product a failure.
- 自己项目：「答不出 / 没想清楚」是真实的薄弱信号，按深度封顶规则打分（模糊未对齐 ≤3，定义清晰未核对 ≤6）。
  Your own project: "cannot answer / not thought through" is a real weakness signal; score with depth caps (vague ≤3, defined but not cross-checked ≤6).
- 真实需求与付费转化最难判断：看**需求是否对齐**——目标用户是否精确到「人群 + 决策状态 + 场景」（例如「还没决定要不要出海」和「已决定出海、在选工具」需求不同，不能混为一谈）；以及付费逻辑是否成立。说不清就是未对齐。
  Real Demand and Paid Conversion are hardest to judge: check whether the demand is **aligned** — is the target user precise to "segment + decision state + scenario" (e.g., "undecided about going overseas" vs "decided, choosing a tool" have different needs and cannot be conflated)? And whether the payment logic holds. If you cannot state it, it is misaligned.
- 复购与传播最容易断：无任何留存或传播设计时直接判断裂（不高于 2 分）。
  Retention & Referral break most easily: no retention or referral design at all → broken outright (no higher than 2).
- 修复输出**完整修改方案**：每项包含目标、具体改动、实施步骤、验收标准，由用户自己执行；AI 不直接修改用户产品，只负责方案设计、细化与复检。
  Fix output is a **complete plan**: goal, concrete changes, steps, acceptance criteria per item, executed by the user; the AI designs, refines, and re-checks only.
- 修复逐项进行，一项落地后再进入下一项；用户可随时「复检」对比分数变化；每次出报告时把七环分数与结论保存到工作目录 dandelion-scores.json，复检先读取该基线再对比。
  Fixes proceed item by item; the user may re-check anytime; each report also saves the seven scores to dandelion-scores.json (working directory) as the re-check baseline.
  Fixes proceed item by item; the user may re-check anytime to compare score changes.
- 输出语言跟随用户提问语言；说明文档为中英双语。
  Output language follows the language of the user; the documentation is bilingual (Chinese & English).
- 访谈可选不算低分；单位经济有数字必须测算（references/economics.py），缺数字按「未测算」记、不臆测；社区信号用于核对真实需求与付费意愿。
  Interviews are optional (no interviews is not a low-score reason); unit economics must be computed with numbers (references/economics.py) and "not measured" otherwise; community signals cross-check demand and willingness to pay.

## 资源 Resources
- references/market_research.py — 市场调研引擎（必跑）：全网搜索 8 项市场指标并按证据打分；多后端（Tavily/Serper/Bing）+ 无 key 自动降级
  Market research engine (required): searches the web for 8 market metrics and scores by evidence; multi-backend (Tavily/Serper/Bing) with no-key fallback
- references/framework.md — 链路模型、每环节检查项、自检提问清单、打分细则（深度三档+硬门槛）、判定规则、修复工作法与复检规则
  Loop model, per-stage checklists, self-check questions, strict scoring (depth tiers + hard gates), verdict rules, repair playbook and re-check rules
- references/scoring.py — 打分计算器（可选）：校验平均分、结论与行动优先级 Scoring calculator (optional): verifies average, verdict and action priority
- references/output-template.md — 报告模板与导出说明
  Report template and export notes
- references/interview.md — 访谈脚本（Mom Test 风格，可选加深证据）Interview script (Mom Test style, optional)
- references/growth-experiments.md — 增长实验模板（获客/复购传播 A/B 设计）Growth experiment template (A/B design)
- references/economics.py — 单位经济学测算器（LTV/CAC、毛利率、回本周期）Unit economics calculator (LTV/CAC, margin, payback)
- references/pitch-template.md — 产品化输出模板（pitch/落地页/定价卡）Productize template (pitch/landing/pricing)
- docs/comparison.md — 同类工具对比与差异化定位 Comparison & positioning
- examples/example-output.md — 示例报告（含修复与输出示例）
- tests/test_sanity.py — 自检测试（`python tests/test_sanity.py`）Sanity tests (stdlib only)
  Example report (including repair and export examples)

