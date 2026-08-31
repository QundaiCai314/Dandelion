---
name: business-chain-diagnosis
description: 商业链路诊断（Business Loop Diagnosis）。当用户想判断一个数字产品/SaaS/软件/App/订阅服务的设计是否打通了商业链路，或希望 AI 帮助补充商业思维时使用。支持两条路线：1）自检模式——用户是创造者，AI 一问一答帮其自检正在做的产品；2）项目检查模式——用户给出 GitHub 仓库/本地项目/产品描述，AI 直接检查整个项目并诊断，发现问题时询问项目归属并决定是否追问。诊断后支持修复模式：AI 为每个问题输出完整修改方案（目标、具体改动、实施步骤、验收标准），由用户自己执行，AI 负责方案细化、答疑与复检。支持结论输出：生成可保存/分享的 Markdown 诊断报告文件。输出包括：逐环节诊断、0-10 打分、链路结论（打通/接近打通/未打通）、问题清单、完整修改方案、修复进度、行动清单。Use when the user wants to assess whether a digital product or SaaS design closes the business loop, either as a creator self-checking their own product via Q&A, or by directly inspecting a project/repo; after diagnosis, provide complete fix plans for the user to execute, and export a shareable report.
---

# 商业链路诊断 Business Loop Diagnosis

判断一个数字产品/SaaS 的设计是否打通了商业链路，帮助创造者补充商业思维。所有判断必须基于证据；他人项目证据不足时明确标记，禁止臆测。
Assess whether a digital product/SaaS design closes the business loop, helping creators build business thinking. Every judgment must be evidence-based; clearly flag missing evidence for projects of others; never speculate.

## 两条路线 Two Modes
- **自检模式 Self-Check**：用户是创造者，对自己的产品做检查。默认一问一答，AI 按 6 环节依次提问，用回答打分。
  Self-Check: the user is the creator reviewing their own product. By default one question at a time; the AI walks through the 6 stages in order and scores from the answers.
- **项目检查模式 Project Inspection**：用户给出项目本身（GitHub 仓库 / 本地目录 / 产品描述），AI 直接检查整个项目。发现问题时询问项目归属：别人的项目按公开证据出报告；自己的项目则请用户补充材料或切换为一问一答追问，重新打分。
  Project Inspection: the user provides the project itself (GitHub repo / local directory / product description) and the AI inspects it directly. When problems are found, the AI asks who owns the project: for projects of others it reports from public evidence; for your own, it asks you to supply materials or switches to one-question-at-a-time follow-up, then re-scores.

## 诊断之后 After Diagnosis
- **修复模式 Repair**：诊断报告后，AI 为每个问题输出**完整修改方案**（目标、具体改动、实施步骤、验收标准），由用户自己执行；AI 负责方案细化、答疑与复检，不直接修改用户的产品。
  After the report, the AI outputs a **complete fix plan** per problem (goal, concrete changes, steps, acceptance criteria) for the user to execute themselves; the AI only refines plans, answers questions, and re-checks — it never directly modifies the product.
- **结论输出 Export**：把完整结论输出为可保存/分享的 Markdown 报告文件。
  Export the full conclusion as a shareable Markdown report file.

## 流程 Process
1. 判断模式：用户给的是项目/链接/目录，或要求「检查这个项目」→ 项目检查模式；用户说「帮我自检我的产品 / 看看我做得怎么样」→ 自检模式；不确定时先问一句：这是你自己的项目，还是要检查别人的？
   Determine the mode: a project/link/directory or a request to "inspect this project" → Project Inspection; "help me self-check my product / see how I am doing" → Self-Check; if unclear, ask first whether the project belongs to the user or to someone else.
2. 项目检查：多通道收集证据（README、docs、代码结构、官网、定价页、应用商店页、公开报道与社区讨论），逐环节诊断打分。
   Inspection: gather evidence from multiple channels (README, docs, code structure, website, pricing page, app store listing, public reports and community discussions), then diagnose and score each stage.
3. 发现问题时（任一环节 <5，或 ≥2 个环节 <7）：必须问「这是你自己的项目吗？」
   When problems are found (any stage <5, or ≥2 stages <7): you MUST ask "Is this your own project?"
   - 别人的 → 直接输出报告，无证据环节标注「证据不足」并列出需补充的信息，结论注明「基于公开证据，不代表产品真实状态」。
     Projects of others → output the report directly, mark evidence-starved stages as "insufficient evidence" and list what to supply, and note the verdict is "based on public evidence, not the true state of the product".
   - 自己的 → 问用户要「补充材料」还是「一个一个提问」（默认一个一个提问），补齐后重新打分再出报告。
     Your own → ask whether to supply materials or answer questions one by one (one-by-one is the default), then re-score with the new evidence and report.
   - 打分校验（可选）：把六环分数写成 JSON，运行 references/scoring.py，用脚本输出的平均分、结论与行动优先级（防止判定漂移）。
     Score verification (optional): write the six scores to JSON, run references/scoring.py, and use its average, verdict and action priority (to prevent judgment drift).
4. 全部环节健康时 → 直接输出报告，不追问。
   If all stages are healthy → output the report directly, no follow-up.
5. 自检：按 6 环节顺序提问，默认一次一个问题；答不上来的题记录为「未验证/未设计」并继续，不卡住；问完打分出报告。
   Self-Check: ask through the 6 stages in order, one question at a time by default; unanswered questions are recorded as "unverified/undesigned" and you continue without blocking; score and report when done.
6. 修复：按优先级逐项进行（断裂 → 薄弱 → 全部健康后找增长杠杆）。每项修复：AI 输出**完整修改方案**——目标、具体改动、实施步骤、验收标准（如定价方案、落地页文案、激活指标、推荐机制等），用户确认或要求细化，然后**由用户自己执行修改**；一项落地后再进入下一项。AI 不直接改动用户的产品。用户可随时要求「复检」，用当前证据重新打分并对比变化（规则见 references/framework.md）。
   Repair: work through priorities one item at a time (broken → weak → growth levers once all healthy). For each item, the AI outputs a **complete fix plan** — goal, concrete changes, steps, acceptance criteria (e.g., pricing, landing-page copy, activation metrics, referral mechanics); the user confirms or asks to refine, then **executes the changes themselves**; move to the next item after one lands. The AI never directly modifies the product. The user may request a "re-check" anytime to re-score with current evidence and compare changes (see references/framework.md).
7. 输出：用户要求或一轮修复完成后，将结论输出为 Markdown 报告文件（默认保存到工作目录 business-chain-report.md），包含：报告信息、产品画像、逐环节诊断与打分、结论、问题清单、修复方案、修复进度、行动清单；也可直接在对话中展示或按需转换格式。
   Export: on request or after a repair round, output the conclusion as a Markdown report (default business-chain-report.md in the working directory) containing: report info, product snapshot, per-stage diagnosis and scores, verdict, problem list, fix plan, repair progress, action plan; may also be shown in chat or converted to another format on request.

## 核心规则 Core Rules
- 证据优先：每个分数必须写明依据。无证据环节最高 3 分并标注「证据不足」。禁止臆测。
  Evidence first: every score must state its basis. Stages without evidence cap at 3 and are flagged "insufficient evidence". Never speculate.
- 他人项目：低分只代表「公开证据不足或设计缺失」，报告必须区分两者，不得断言产品失败。
  Projects of others: a low score only means "insufficient public evidence or missing design"; the report must distinguish the two and must not declare the product a failure.
- 自己项目：「答不出 / 没验证过」是真实的薄弱信号，按正常规则打分。
  Your own project: "cannot answer / never verified" is a real weakness signal; score by normal rules.
- 真实需求与付费转化最难判断：要求更严格证据（用户访谈、付费数据、对标验证），无证据不得给高分。
  Real Demand and Paid Conversion are hardest to judge: they demand stricter evidence (user interviews, payment data, benchmarking); no evidence, no high score.
- 复购与传播最容易断：无任何留存或传播设计时直接判断裂（不高于 3 分）。
  Retention & Referral break most easily: no retention or referral design at all → broken outright (no higher than 3).
- 修复输出**完整修改方案**：每项包含目标、具体改动、实施步骤、验收标准，由用户自己执行；AI 不直接修改用户产品，只负责方案设计、细化与复检。
  Fix output is a **complete plan**: goal, concrete changes, steps, acceptance criteria per item, executed by the user; the AI designs, refines, and re-checks only.
- 修复逐项进行，一项落地后再进入下一项；用户可随时「复检」对比分数变化。
  Fixes proceed item by item; the user may re-check anytime to compare score changes.
- 输出语言跟随用户提问语言；说明文档为中英双语。
  Output language follows the language of the user; the documentation is bilingual (Chinese & English).

## 资源 Resources
- references/framework.md — 链路模型、每环节检查项、自检提问清单、打分细则、判定规则、修复工作法与复检规则
  Loop model, per-stage checklists, self-check questions, scoring, verdict rules, repair playbook and re-check rules
- references/scoring.py — 打分计算器（可选）：校验平均分、结论与行动优先级 Scoring calculator (optional): verifies average, verdict and action priority
- references/output-template.md — 报告模板与导出说明
  Report template and export notes
- examples/example-output.md — 示例报告（含修复与输出示例）
  Example report (including repair and export examples)

