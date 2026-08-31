# 同类工具对比与差异化定位 Comparison & Positioning

本文基于公开资料对同类「产品/创意验证」工具做横向对比，定位 Dandelion 的差异化。
Based on public materials, this compares similar "product/idea validation" tools and positions Dandelion.

## 直接同类 Direct Comparables
| 工具 Tool | 定位 Focus | 机制 Mechanism | 与 Dandelion 的差异 Difference |
| --- | --- | --- | --- |
| venture-analyst | 创意裁决 4 阶段 | 零 key、多阶段分析报告 | 面向「点子」而非已有产品/仓库；无修复闭环 |
| idea-os | 创始人工作流 | Mom Test 访谈 + /pmf 0-100 + /economics | 有访谈与单位经济，但不对接 GitHub 仓库检查与归属门禁 |
| Hermes biz-strategy | 商业策略 | 7 领域分析 + 需求四问 + EUREKA | 偏宏观策略，无证据打分与复检闭环 |
| reddit-business-idea-validator | 中文社区验证 | 抓 Reddit 出 HTML 报告 | 单社区抓取；Dandelion 用搜索引擎做全站社区信号 |
| Business Idea Validator MCP | 商业验证 MCP | Apify 付费（约 $0.25/次）8 维加权 | 付费依赖；Dandelion 无 key 可跑完整流程 |
| pmf-kit | PMF 工作流 | 18 个 agent 分角色 | 重流程编排；Dandelion 单 skill 轻量自包含 |
| launchlens | CLI 快速验证 | 本地 CLI 与竞品对比 | 无联网市场调研与证据打分 |
| startup-validator / ai-native-founder-playbook | 启动清单/手册 | 模板式清单 | 无程序化调研与 0-10 逐环打分 |

## 差异化定位 Positioning
1. **唯一「已有产品/项目」检查**：可以直接检查 GitHub 仓库 / 本地项目 / 产品描述，而不是只验证点子。
   The only one that inspects an EXISTING product/project (GitHub repo / local dir / description), not just an idea.
2. **全 7 链路 + 修复 → 复检闭环**：诊断不止打分，还输出每问题完整修改方案，落地后可复检对比分数。
   Full 7-stage loop + repair-to-recheck cycle: not just scores, but a complete fix plan per problem, re-checkable after execution.
3. **归属门禁**：检查他人项目时按公开证据出报告、不断言失败；自己的项目才允许追问补证并重新打分。
   Ownership gate: others' projects are reported from public evidence only (never declared failed); your own project can be probed and re-scored.
4. **无 key 默认可用**：市场调研引擎多后端联网，没配 key 自动降级为检索计划 + agent 补查，流程不中断。
   No-key by default: the research engine works without any API key (degrades to a search plan + agent-filled evidence).

## 本轮已补齐的差距 Gaps closed this round
- 访谈流程：references/interview.md（Mom Test 风格问题集、硬性纪律、记录与证据落地、AI 访谈教练）。
- 社区直抓：market_research.py 增加社区定向检索（site:reddit.com / news.ycombinator.com / zhihu.com 等）与报告「社区信号」板块。
- 单位经济学：references/economics.py（毛利率 / LTV / LTV:CAC / 回本周期，含交互模式）。
- 产品化输出：references/pitch-template.md（30 秒 pitch / 一句话价值主张 / 落地页首屏 / 三档定价卡 / 冷启动渠道）。

## 仍开放的机会 Open opportunities
- 分发渠道：提交到 Awesome 技能清单（如 awesome-claude-skills、awesome-cursor-rules）与主流 agent 市场。
- 社区直抓深度：直接接 Reddit / HN API（当前用搜索引擎 site: 检索，零 key 但深度有限）。
- 增长实验模板：AB 测试与增长实验设计（当前只到「复购与传播」的修复杠杆）。
- 多语言产品化输出：pitch / 落地页文案支持日、西、法等语言。