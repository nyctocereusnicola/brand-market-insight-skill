# Brand Market Insight Skill / 品牌市场洞察技能

A professional-grade brand market insight analysis skill for AI agents. Produces structured research reports covering market research, competitive analysis, consumer profiling, channel strategy, and trend forecasting.

**适用于 AI Agent 的专业品牌市场洞察分析技能。** 输出结构化调研报告，覆盖市场研究、竞品分析、消费者画像、渠道策略和趋势预测。

**Compatible with**: [OpenAI Codex CLI](https://github.com/openai/codex), [WorkBuddy](https://www.codebuddy.cn), [Claude Code](https://claude.ai/claude-code), and any [Agent Skills](https://agentskills.io)-compliant client.

---

## Features / 功能特性

- **5 Analysis Dimensions / 5大分析维度**: Market overview, competitive landscape, consumer profiling, channel strategy, trend forecasting / 市场概览、竞品分析、消费者画像、渠道策略、趋势预测
- **Local-First Research Protocol / 本土化调研规范**: Automatically adapts language, platforms, competitors, and benchmarks to the target market / 自动适配目标市场的语言、平台、竞品和基准
- **Data Verification Protocol / 数据交叉验证**: Cross-verification with 2+ independent sources, social buzz vs sales data distinction / 2+独立来源交叉验证，区分社交媒体声量与实际销量
- **Structured Output / 结构化输出**: Markdown reports with tables, frameworks, confidence labels, and actionable recommendations / 含表格、框架、置信度标签和可执行建议
- **HTML Export**: Built-in HTML template for web deployment
- **Report Generator / 报告生成器**: Python script for JSON-to-Markdown report generation

## Quick Start / 快速开始

### Codex CLI

```bash
# Install from this repository / 从本仓库安装
skill-installer install https://github.com/nyctocereusnicola/brand-market-insight-skill

# Or copy to local skills directory / 或复制到本地技能目录
cp -r brand-market-insight-skill ~/.agents/skills/
# Restart Codex after installing / 安装后重启 Codex
```

### WorkBuddy / CodeBuddy

```bash
# Copy to user-level skills / 复制到用户级技能目录
cp -r brand-market-insight-skill ~/.workbuddy/skills/
```

### Claude Code

```bash
# Copy to Claude Code skills directory / 复制到 Claude Code 技能目录
cp -r brand-market-insight-skill ~/.claude/skills/
```

## Directory Structure / 目录结构

```
brand-market-insight-skill/
├── SKILL.md                    # Skill definition + instructions / 技能定义与指令 (required)
├── references/
│   ├── methodology.md          # Analysis frameworks + local-first protocol / 分析框架 + 本土化规范
│   └── report-structure.md     # Standard report template / 标准报告模板
├── assets/
│   └── report-template.html    # HTML template for web deployment / 网页部署 HTML 模板
└── scripts/
    └── generate_report.py      # Python report generator / Python 报告生成器
```

## Supported Markets / 支持市场

| Market 市场 | Local Language 本地语言 | E-commerce 电商 | Social Platforms 社交平台 |
|-------------|----------------------|----------------|------------------------|
| China 中国 | Chinese 中文 | Taobao, JD, PDD, Douyin | Xiaohongshu, Douyin, Weibo, Bilibili |
| Thailand 泰国 | Thai + English 泰语+英语 | Shopee TH, Lazada TH, Konvy, 7-11 | Lemon8 TH, TikTok TH, Facebook TH, Jeban |
| Southeast Asia 东南亚 | English + local 英语+本地语言 | Shopee, Lazada | TikTok, Instagram, Facebook |
| LATAM 拉美 | Spanish / Portuguese 西语/葡语 | Mercado Libre, Amazon | TikTok LATAM, Instagram, Facebook |
| Middle East 中东 | Arabic + English 阿语+英语 | Noon, Amazon AE | Instagram, TikTok, Snapchat |
| Europe/US 欧美 | English 英语 | Amazon, Sephora, Ulta | Instagram, TikTok, YouTube, Reddit |

## Report Types / 报告类型

| Type 类型 | Sections 包含章节 | Use Case 适用场景 |
|-----------|-----------------|-----------------|
| Full Report 完整报告 | All 6 sections + appendix 全部6章+附录 | Comprehensive brand/market analysis 综合品牌/市场分析 |
| Market Entry 市场进入 | Market + Competitive + Consumer + Channel + Strategy | Entering a new market 进入新市场 |
| Competitor Scan 竞品扫描 | Exec summary + Matrix + Top 3 | Quick competitive overview 快速竞品概览 |
| Consumer Deep Dive 消费者洞察 | Demographics + Behavior + Content + Journey | Consumer research focus 消费者研究 |

## Example Usage / 使用示例

```
"Analyze the Thai beauty tools market, focusing on ONI Thailand brand"
"深度调研分析泰国美妆工具市场，聚焦 ONI Thailand 品牌"

"Competitive analysis of C-beauty brands entering Southeast Asia"
"中国美妆品牌进入东南亚市场的竞品分析"

"Consumer profiling for wellness supplements in LATAM"
"拉美保健补充剂市场的消费者画像"

"Channel strategy for a Korean skincare brand entering the Middle East"
"韩国护肤品牌进入中东市场的渠道策略"
```

## Methodology Highlights / 方法论亮点

### Local-First Research Protocol / 本土化调研规范

> **Core principle / 核心原则**: Research a market using that market's own language, platforms, KOLs, and channel logic. Never extrapolate other regions using China's market experience.
> 调研哪个市场，就用哪个市场的语言、平台、KOL、渠道逻辑。禁止用中国市场经验外推其他区域。

- Search using **target market's native language** keywords / 使用**目标市场本地语言**关键词搜索
- Prioritize **local e-commerce platforms** for sales data / 优先使用**本土电商平台**获取销量数据
- Benchmark against **local competitors**, not international brands / 对标**本土竞品**，而非国际品牌
- Use **local currency and purchasing power** for price analysis / 使用**本地货币和购买力**分析价格
- Match **local channel structure** / 匹配**本地渠道结构**

### Data Verification / 数据验证

- Cross-verify all key data points with 2+ independent sources / 所有关键数据点至少 **2个独立来源** 交叉验证
- Distinguish **social media buzz** from **actual sales data** / 区分**社交媒体声量**与**实际销量数据**
- Mark confidence levels: [High] / [Medium] / [Low] / 标注置信度
- Ask user to confirm when assumptions are uncertain / 假设不确定时**主动向用户确认**

## Categories / 覆盖品类

Beauty 美妆 (cosmetics, skincare, personal care / 彩妆、护肤、个护), Wellness 大健康 (health, supplements / 保健、补充剂), Lifestyle 生活方式

## Author / 作者

Created by [Nicola Chen](https://github.com/nyctocereusnicola) — Been through finance, branding, marketing, and cross-border commerce. Obsessed with brands and markets, drawn to interesting things, builds with attitude and personality. Serving global markets.

扎过金融、品牌、营销、跨境这几个坑。对品牌和市场有执念，喜欢有趣的玩意，做有态度有个性的东西。服务全球市场。

## License / 许可证

MIT License — free to use, modify, and distribute with attribution.
MIT 许可证 — 自由使用、修改和分发，需保留署名。
