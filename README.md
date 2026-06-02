# Brand Market Insight Skill

A professional-grade brand market insight analysis skill for AI agents. Produces structured research reports covering market research, competitive analysis, consumer profiling, channel strategy, and trend forecasting.

**Compatible with**: [OpenAI Codex CLI](https://github.com/openai/codex), [WorkBuddy](https://www.codebuddy.cn), [Claude Code](https://claude.ai/claude-code), and any [Agent Skills](https://agentskills.io)-compliant client.

## Features

- **5 Analysis Dimensions**: Market overview, competitive landscape, consumer profiling, channel strategy, trend forecasting
- **Local-First Research Protocol**: Automatically adapts language, platforms, competitors, and benchmarks to the target market (China, Thailand, SEA, LATAM, Middle East, Europe)
- **Data Verification Protocol**: Cross-verification with 2+ independent sources, social buzz vs sales data distinction
- **Structured Output**: Markdown reports with tables, frameworks, confidence labels, and actionable recommendations
- **HTML Export**: Built-in HTML template for web deployment
- **Report Generator**: Python script for JSON-to-Markdown report generation

## Quick Start

### Codex CLI

```bash
# Install from this repository
$skill-installer install https://github.com/nyctocereusnicola/brand-market-insight-skill

# Or copy to local skills directory
cp -r brand-market-insight-skill ~/.agents/skills/
# Restart Codex after installing
```

### WorkBuddy / CodeBuddy

```bash
# Copy to user-level skills
cp -r brand-market-insight-skill ~/.workbuddy/skills/
```

### Claude Code

```bash
# Copy to Claude Code skills directory
cp -r brand-market-insight-skill ~/.claude/skills/
```

## Directory Structure

```
brand-market-insight-skill/
├── SKILL.md                    # Skill definition + instructions (required)
├── references/
│   ├── methodology.md          # Analysis frameworks + local-first protocol
│   └── report-structure.md     # Standard report template
├── assets/
│   └── report-template.html    # HTML template for web deployment
└── scripts/
    └── generate_report.py      # Python report generator
```

## Supported Markets

| Market | Local Language | E-commerce | Social Platforms |
|--------|---------------|------------|------------------|
| China | Chinese | Taobao, JD, PDD, Douyin | Xiaohongshu, Douyin, Weibo, Bilibili |
| Thailand | Thai + English | Shopee TH, Lazada TH, Konvy, 7-11 | Lemon8 TH, TikTok TH, Facebook TH, Jeban |
| Southeast Asia | English + local | Shopee, Lazada | TikTok, Instagram, Facebook |
| LATAM | Spanish / Portuguese | Mercado Libre, Amazon | TikTok LATAM, Instagram, Facebook |
| Middle East | Arabic + English | Noon, Amazon AE | Instagram, TikTok, Snapchat |
| Europe/US | English | Amazon, Sephora, Ulta | Instagram, TikTok, YouTube, Reddit |

## Report Types

| Type | Sections | Use Case |
|------|----------|----------|
| Full Report | All 6 sections + appendix | Comprehensive brand/market analysis |
| Market Entry | Market + Competitive + Consumer + Channel + Strategy | Entering a new market |
| Competitor Scan | Exec summary + Matrix + Top 3 | Quick competitive overview |
| Consumer Deep Dive | Demographics + Behavior + Content + Journey | Consumer research focus |

## Example Usage

```
"Analyze the Thai beauty tools market, focusing on ONI Thailand brand"
"Competitive analysis of C-beauty brands entering Southeast Asia"
"Consumer profiling for wellness supplements in LATAM"
"Channel strategy for a Korean skincare brand entering the Middle East"
```

## Methodology Highlights

### Local-First Research Protocol
- Search using **target market's native language** keywords
- Prioritize **local e-commerce platforms** for sales data
- Benchmark against **local competitors**, not international brands
- Use **local currency and purchasing power** for price analysis
- Match **local channel structure** (not another market's model)

### Data Verification
- Cross-verify all key data points with 2+ independent sources
- Distinguish **social media buzz** from **actual sales data**
- Mark confidence levels: [High] / [Medium] / [Low]
- Ask user to confirm when assumptions are uncertain

## Categories

Beauty (cosmetics, skincare, personal care), Wellness (health, supplements), Lifestyle

## Author

Created by [Nicola Chen](https://github.com/nyctocereusnicola) — Brand strategist with 16 years FMCG marketing experience, specializing in beauty, wellness, and lifestyle brands across global markets.

## License

MIT License — free to use, modify, and distribute with attribution.
