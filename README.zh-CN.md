[English](README.md) | **中文**

# Dandelion · 商业链路诊断 Business Loop Diagnosis

一个面向所有 AI agent 的 skill（技能）：判断一个**数字产品 / SaaS / 软件 / App / 订阅服务**的设计是否打通了商业链路，帮助创造者补充商业思维。

A skill for any AI agent: assess whether a digital product or SaaS design closes the business loop, helping creators build business thinking.

## 它能做什么 What It Does
- **两条路线**：① 自检模式——创造者对自己的产品，AI 一问一答逐环节提问后出报告；② 项目检查模式——直接检查 GitHub 仓库 / 本地项目 / 产品描述后出报告。
- **市场调研先行**：每次诊断先跑全网桌面研究——`references/market_research.py` 联网搜索 8 项市场指标（用户画像/群体范围/痛点/付费意愿/付费习惯/竞品/市场规模/渠道）并按证据 0-10 打分；没有 API key 时自动降级为检索清单 + agent 补查证据
- **社区直抓**：调研引擎增加社区定向查询（`site:reddit.com`、`site:news.ycombinator.com`、`site:zhihu.com`、`site:indiehackers.com` 等），报告输出「社区信号 Community Signals」板块，列出目标用户的真实讨论用于核对需求
- 按 7 环节链路模型逐环诊断：市场调研 → 真实需求 → 价值主张 → 获客 → 付费转化 → 交付与体验 → 复购与传播
- 每环节 0-10 打分，按明确规则判定：**链路打通 / 接近打通 / 未打通**
- 输出完整报告：诊断 → 打分 → 问题清单 → 修复方案 → 行动清单
- 项目检查发现问题时会问「这是你自己的项目吗」：别人的项目按公开证据出报告并标注证据不足；自己的项目会请你补充材料或一个一个提问，重新打分
- **修复模式**：诊断后为每个问题输出**完整修改方案**（目标、具体改动、步骤、验收标准），由你自己执行；AI 负责方案细化、答疑与复检，不直接改动你的产品
- **访谈模式（可选）**：Mom Test 风格访谈教练（`references/interview.md`）——一次一问、记录证据、回填证据表单后复检
- **单位经济学（可选）**：`references/economics.py` 在有数字时测算毛利率、LTV、LTV/CAC 与回本周期
- **产品化输出（可选）**：`references/pitch-template.md` 把结论转成 30 秒 pitch、一句话价值主张、落地页首屏、三档定价卡与冷启动渠道清单
- **结论输出**：生成可保存/分享的 Markdown 诊断报告文件（business-chain-report.md）
- **增长实验**：references/growth-experiments.md 把「做点推广」变成可验证的 A/B 实验（假设、指标、样本、门槛、决策规则），用于获客与复购传播
- 证据优先：证据不足的环节最高 3 分并标记，禁止臆测
- **打分计算器**：可选的 `references/scoring.py`，用脚本校验平均分、结论与行动优先级，防止判定漂移

## 市场调研引擎 Market Research Engine
每次诊断都从市场调研开始。引擎 `references/market_research.py` 联网搜索 8 项市场指标（每项 0-10 机器证据分）：

| 指标 | 查证什么 |
| --- | --- |
| 用户画像 | 目标人群真实存在、活跃、有公开讨论 |
| 群体范围 | 人群规模可界定与估算 |
| 痛点需求 | 痛点被公开讨论、场景/频率具体 |
| 付费意愿 | 有付费产品、定价基准、付费讨论 |
| 付费习惯 | 支付方式、订阅习惯、价格敏感度 |
| 竞品分析 | 竞品数量、头部玩家、差异化空间 |
| 市场规模 | TAM/SAM、公开数据与趋势 |
| 渠道分布 | 目标用户聚集的平台/社区 |

**社区信号**：除常规检索词外，检索计划为社区相关指标（用户画像/痛点/付费意愿/竞品/渠道）增加 site: 定向查询。联网模式把结果收进报告的「社区信号 Community Signals」板块；无 key 降级时把直查清单写进 evidence_fill_form.json 的 community_plan 字段，由 agent 补查后回填 community_signals。

即使没有任何 API key，引擎也会用 Hacker News 免费公开接口自动直抓社区讨论（无需 key）并加入「社区信号」板块。

**搜索后端**（按顺序自动检测，配置任意一个即可）：
- `TAVILY_API_KEY` — https://tavily.com（推荐）
- `SERPER_API_KEY` — https://serper.dev（Google 结果）
- `BING_API_KEY` — Bing 网页搜索 API

**配置搜索 key（可选，约 2 分钟）** —— 只有当你想让脚本自己联网搜索时才需要：
1. 选一个服务商，注册并免费领取 API key：
   - Tavily（推荐，为 agent 设计）：https://tavily.com → Dashboard → API Keys
   - Serper（Google 结果）：https://serper.dev → API Key
   - Bing：Azure 门户 → Bing Web Search 资源 → Keys & Endpoint
2. 把 key 设成环境变量（变量名必须与上面一致）：
   - Windows PowerShell：`$env:TAVILY_API_KEY="tvly-xxxx"`（仅当前会话）或 `setx TAVILY_API_KEY "tvly-xxxx"`（永久）
   - macOS/Linux：`export TAVILY_API_KEY="tvly-xxxx"`（写入 `~/.zshrc` 或 `~/.bashrc` 持久生效）
3. 验证：`python references/market_research.py --product "测试产品"` 显示 live 后端（如 `tavily`）而不是 `no API key`。

运行：
```
python references/market_research.py --product "产品一句话描述"
```

可选参数：`--target-user "<目标用户>"`、`--market "<目标市场>"`、`--lang zh|en|auto`（与 product.json 字段一致）。

**没有 API key？** 程序自动降级：生成检索计划 + `evidence_fill_form.json`，由 agent 用自己的联网搜索补完证据后打分：
```
python references/market_research.py --score-only evidence_fill_form.json
```
分数 = 结果数量 + 可信来源 + 具体数字 + 弱相关性折扣；agent 阅读实际结果后可用 `--calibrate <file>` 人工校准。
重跑不会覆盖已填证据：已填证据会保留、只刷新检索词；表单属于其他产品时脚本会拒绝并提示 `--force`。
路径以 skill 目录为基准：若当前工作目录不是 skill 根目录，请先解析绝对路径（如 `<skill_dir>/references/market_research.py`）再运行；需要 Python 3.8+。

## 单位经济学测算器 Unit Economics Calculator
`references/economics.py` 把定价/成本数字转成付费转化环节使用的单位经济指标：
- 输入：`price`（月/年/买断）、`unit_cost`、`cac`、`monthly_churn`（或 `annual_churn`）、可选 `gross_margin_pct`
- 输出：毛利率、客户生命周期、LTV、LTV/CAC、回本周期
- 判定：LTV/CAC ≥ 3 健康 · 1-3 需优化 · <1 断裂信号
- 用法：`python references/economics.py economics.json --json` 或 `--interactive`
- 规则：有数字必须测算；没数字按「未测算」记，绝不臆测

## 访谈模式（可选）Interview Mode (optional)
`references/interview.md` —— Mom Test 风格访谈脚本：硬性纪律（少于 3 个真实目标用户不得声称「已访谈」；只记录过去行为；不推销）、按环节分组的问题集、好问题 vs 坏问题对照表、访谈记录模板，以及如何把证据回填到 `evidence_fill_form.json` 后复检。访谈是可选环节——没有访谈不是低分理由；它把「定义清晰但未核对」升级为「深度对齐 + 已核对」。

## 产品化输出（可选）Productize (optional)
`references/pitch-template.md` —— 诊断后说「给我做产品化输出」，AI 生成：30 秒 pitch、一句话价值主张、落地页首屏结构、三档定价卡、冷启动渠道清单。产出的是给用户的材料，AI 不直接修改用户产品。

## 安装 Install
任何支持 skill 机制的 agent，把本仓库目录（克隆后默认名 `Dandelion`，内含 SKILL.md）复制到 agent 的 skills 目录，或克隆后复制：
```
git clone https://github.com/QundaiCai314/Dandelion.git
```

| Agent | 目录 Directory |
| --- | --- |
| Claude Code | ~/.claude/skills/ 或项目 .claude/skills/ |
| Codex | ~/.codex/skills/ 或项目 .codex/skills/ |
| Cursor | 项目 .cursor/skills/ |
| 其他 | 按该 agent 的 skills 安装目录 |

## 使用 Usage
- 自检：用 business-chain-diagnosis skill 帮我检查我的产品：<一句话描述>
- 项目检查：用 business-chain-diagnosis skill 检查这个项目：<仓库链接 / 本地路径>
- 访谈：对我的产品做一次访谈加深
- 修复：诊断后帮我修复获客环节
- 复检：按我当前的情况复检
- 产品化：给我的产品做产品化输出
- 导出：把报告导出成文件

## 结构 Structure
- SKILL.md — 主 skill 文件（触发描述、两种模式工作流、修复与导出工作流、核心规则）
- references/market_research.py — 市场调研引擎（多后端搜索：Tavily/Serper/Bing；社区定向查询与社区信号板块；无 key 降级生成检索计划+证据表单）
- references/framework.md — 链路模型、自检提问清单、每环节检查项、打分细则、判定规则、修复工作法与复检规则
- references/interview.md — Mom Test 风格访谈脚本（可选加深证据）
- references/economics.py — 单位经济学测算器（毛利率、LTV/CAC、回本周期）
- references/pitch-template.md — 产品化输出模板（pitch / 落地页首屏 / 定价卡）
- references/growth-experiments.md — 增长实验模板（获客 / 复购传播 A/B 设计）
- references/output-template.md — 报告模板与导出说明
- references/scoring.py — 打分计算器（可选）：校验平均分、结论与行动优先级
- docs/comparison.md — 同类工具对比与差异化定位
- examples/example-output.md — 示例报告
- tests/test_sanity.py — 自检测试（`python tests/test_sanity.py`，纯标准库）
- LICENSE — MIT License

## 同类对比 How It Compares
详见 [docs/comparison.md](docs/comparison.md)：与 venture-analyst、idea-os、Hermes biz-strategy、reddit-business-idea-validator、Business Idea Validator MCP、pmf-kit、launchlens 等对比。Dandelion 的差异点：检查**已有**项目/仓库（不只是点子）、全 7 环节 + 修复→复检闭环、归属门禁（自己的 vs 别人的项目）、无 key 也能跑完整流程的调研引擎。

## 判定规则速览 Scoring Rules
- 每环节 0-10 分：≥7 健康；5-6.9 薄弱；<5 断裂
- 链路打通：全部环节 ≥7 且平均分 ≥7.5
- 接近打通：无环节 <5，平均分 ≥7，但存在 <7 的环节
- 未打通：任一环节 <5，或平均分 <7
- 真实需求、付费转化要求严格证据；复购与传播无任何设计时直接判断裂
- 他人项目：结论注明「基于公开证据」；自己的项目：答不出/没验证按薄弱处理
- 市场调研：未跑调研 ≤3；已调研但证据单薄 ≤6；8 项指标全部有证据且与产品主张一致才可 ≥7
- 深度判断：模糊/未对齐 ≤3；定义清晰但未外部核对 ≤6；7 分以上需深度对齐 + 桌面研究核对（不要求访谈/数据）；复购传播无设计 ≤2
- 单位经济：有数字必须用 references/economics.py 测算（≥3 健康、<1 断裂）；没数字按「未测算」记

## 测试与版本 Tests & Version
- `python tests/test_sanity.py` — 打分启发式、计算器与社区查询的自检测试（纯标准库，无第三方依赖）
- 版本 Version：1.2.0

## License
本项目基于 MIT License 开源，见 [LICENSE](LICENSE)。

Released under the [MIT License](LICENSE).
