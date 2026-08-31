[English](README.md) | **中文**

# Dandelion · 商业链路诊断 Business Loop Diagnosis

一个面向所有 AI agent 的 skill（技能）：判断一个**数字产品 / SaaS / 软件 / App / 订阅服务**的设计是否打通了商业链路，帮助创造者补充商业思维。

A skill for any AI agent: assess whether a digital product or SaaS design closes the business loop, helping creators build business thinking.

## 它能做什么 What It Does
- **两条路线**：① 自检模式——创造者对自己的产品，AI 一问一答逐环节提问后出报告；② 项目检查模式——直接检查 GitHub 仓库 / 本地项目 / 产品描述后出报告。
- 按 6 环节链路模型逐环诊断：真实需求 → 价值主张 → 获客 → 付费转化 → 交付与体验 → 复购与传播
- 每环节 0-10 打分，按明确规则判定：**链路打通 / 接近打通 / 未打通**
- 输出完整报告：诊断 → 打分 → 问题清单 → 修复方案 → 行动清单
- 项目检查发现问题时会问「这是你自己的项目吗」：别人的项目按公开证据出报告并标注证据不足；自己的项目会请你补充材料或一个一个提问，重新打分
- **修复模式**：诊断后为每个问题输出**完整修改方案**（目标、具体改动、步骤、验收标准），由你自己执行；AI 负责方案细化、答疑与复检，不直接改动你的产品
- **结论输出**：生成可保存/分享的 Markdown 诊断报告文件（business-chain-report.md）
- 证据优先：证据不足的环节最高 3 分并标记，禁止臆测
- **打分计算器**：可选的 `references/scoring.py`，用脚本校验平均分、结论与行动优先级，防止判定漂移

## 安装 Install
任何支持 skill 机制的 agent，把本仓库目录（克隆后默认名 `dandelion`，内含 SKILL.md）放入对应 skills 目录即可。

| Agent | 目录 |
| --- | --- |
| Claude Code | ~/.claude/skills/ 或项目根 .claude/skills/ |
| Codex | ~/.codex/skills/ 或项目根 .codex/skills/ |
| Cursor | 项目根 .cursor/skills/ |
| 其他 | 参照该 agent 的 skills 安装目录 |

## 使用示例 Usage
自检：「用商业链路诊断 skill 帮我自检一下我在做的产品：<产品一句话>」

项目检查：「用商业链路诊断 skill 检查这个项目：<GitHub 链接 / 本地目录>」

修复：「诊断完，帮我把获客这一环修好」

复检：「按现在的情况复检一下」

输出：「把报告导出成文件」

Self-check: "Use the business-chain-diagnosis skill to review my product: <one-line description>"

Project inspection: "Use the business-chain-diagnosis skill to inspect this project: <repo URL / local path>"

## 目录结构 Structure
- SKILL.md — 技能主文件（触发描述 + 两条路线流程 + 修复与输出流程 + 核心规则）
- references/framework.md — 链路模型、自检提问清单、每环节检查项、打分细则、判定规则、修复工作法与复检规则
- references/output-template.md — 报告模板与导出说明
- references/scoring.py — 打分计算器（可选）：校验平均分、结论与行动优先级
- examples/example-output.md — 示例报告
- LICENSE — MIT License

## 判定规则速览 Scoring Rules
- 每环节 0-10 分：≥7 健康；5-6.9 薄弱；<5 断裂
- 链路打通：全部环节 ≥7 且平均分 ≥7.5
- 接近打通：无环节 <5，平均分 ≥7，但存在 <7 的环节
- 未打通：任一环节 <5，或平均分 <7
- 真实需求、付费转化要求严格证据；复购与传播无任何设计时直接判断裂
- 他人项目：结论注明「基于公开证据」；自己的项目：答不出/没验证按薄弱处理

## License
本项目基于 MIT License 开源，见 [LICENSE](LICENSE)。

Released under the [MIT License](LICENSE).

