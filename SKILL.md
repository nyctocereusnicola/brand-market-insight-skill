---
name: brand-market-insight
description: "Professional brand market insight analysis system. Triggers when user asks for market research, brand analysis, competitive intelligence, consumer profiling, channel analysis, trend research, or market entry assessment. Covers beauty, wellness, lifestyle categories across China, SEA, LATAM, Europe, Africa, and Middle East markets. Produces structured reports with tables, frameworks, and actionable insights. Local-first research methodology — adapts language, platforms, and benchmarks to the target market."
---

# Brand Market Insight System

## Overview

A professional-grade brand market insight analysis skill that produces structured research reports. Covers five analysis dimensions — market/category, competitive landscape, consumer profiling, channel strategy, and trend forecasting — integrated into a single cohesive report output.

## When to Use

Trigger this skill when the user mentions any of:

- **Market research**: "analyze X market", "market size", "category landscape", "market entry assessment"
- **Competitive analysis**: "competitor analysis", "competitor matrix", "brand comparison", "SWOT analysis"
- **Consumer profiling**: "consumer persona", "target audience", "demographics", "purchase behavior"
- **Channel analysis**: "channel strategy", "distribution", "platform strategy", "retail analysis"
- **Trend research**: "market trends", "category innovation", "future outlook"
- **Brand entry strategy**: "brand entry", "market opportunity", "go-to-market", "GTM"

**Categories**: beauty (cosmetics/skincare/personal care), wellness (health/supplements), lifestyle
**Markets**: China, Southeast Asia, LATAM, Europe, Africa, Middle East

## Core Workflow

When the user provides a research request, execute this sequence:

### Phase 1: Intent Parsing

Extract structured parameters from the request:

```
Brand: [target brand name]
Category: [beauty/wellness/lifestyle sub-category]
Market: [target region(s)]
Task Type: [market_overview | competitor_analysis | consumer_profile | channel_analysis | trend_forecast | full_report]
Scope: [broad overview | deep dive | comparison]
```

### Phase 2: Local-First Research Setup

> **CRITICAL: Local-First Research Protocol**
>
> Research must be conducted from the perspective of the **target market**, not exported from another market's data.
>
> See `references/methodology.md#local-first-research` for the complete protocol.

**Before searching, determine:**
1. Target market's primary local language(s) for search keywords
2. Target market's dominant e-commerce and social platforms
3. Target market's local competitor set (not international brands)
4. Target market's price benchmarks and purchasing power context

**Market-specific reference table** (see `references/methodology.md` for full details):

| Market | Search Language | E-commerce Platforms | Social Platforms | Local Competitors |
|---------|----------------|---------------------|------------------|-------------------|
| China | 中文 | Taobao, JD, PDD, Douyin Shop | Xiaohongshu, Douyin, Weibo, Bilibili | Local C-beauty brands |
| Thailand | **Thai** + English | Shopee TH, Lazada TH, Konvy, 7-11 | Lemon8 TH, TikTok TH, Facebook TH, Jeban | Mistine, Cute Press, 3CE TH |
| Southeast Asia | English + local | Shopee, Lazada | TikTok, Instagram, Facebook | Local beauty brands per country |
| LATAM | Spanish / Portuguese | Mercado Libre, Amazon | TikTok LATAM, Instagram, Facebook | Local beauty brands |
| Middle East | Arabic + English | Noon, Amazon AE | Instagram, TikTok, Snapchat | Local beauty brands |

### Phase 3: Multi-Dimensional Research

For each applicable dimension, execute research in parallel:

**3.1 Market/Category Analysis** — Load `references/methodology.md#market-analysis`
- Market size (TAM/SAM/SOM), growth rate (YoY CAGR)
- Category lifecycle stage, segment breakdown
- Regional differences, regulatory environment

**3.2 Competitive Landscape** — Load `references/methodology.md#competitive-analysis`
- Competitor identification (direct, indirect, emerging) — **use local competitors first**
- 4P framework: Product, Price, Place, Promotion
- Competitor matrix: positioning x price band
- SWOT summary for top 5 competitors

**3.3 Consumer Profiling** — Load `references/methodology.md#consumer-analysis`
- Demographics, psychographics
- Behavior: usage scenarios, purchase frequency
- Content preferences: **local social platforms and KOL types**
- Decision journey: awareness → consideration → purchase

**3.4 Channel Analysis** — Load `references/methodology.md#channel-analysis`
- Channel structure: online vs offline split
- Platform strategy: **local platform penetration and dynamics**
- Touchpoint ROI assessment
- Distribution model: DTC, wholesale, hybrid

**3.5 Trend Forecasting** — Load `references/methodology.md#trend-analysis`
- Macro consumer trends in target market
- Category innovation direction
- Technology impact, policy/regulatory changes

### Phase 4: Report Assembly

Generate the final report following `references/report-structure.md`:

1. **Executive Summary** (300 words max)
2. **Key Findings at a Glance** (summary table)
3. Market overview
4. Competitive landscape
5. Consumer profiling
6. Channel analysis
7. Trends and opportunities
8. Brand entry/strategy recommendations (if applicable)
9. Appendix: data sources, methodology, disclaimer

## Output Standards

Every report must satisfy:

- **Conclusion-first**: Each section opens with the key finding, then evidence
- **Data-sourced**: Every claim has a source annotation; uncertainties marked [unverified]
- **Table minimum**: At least 3 tables per full report
- **Framework minimum**: At least 2 analysis frameworks applied
- **Actionable**: 3-5 specific, executable recommendations
- **Confidence labels**: [High/Medium/Low] on key data points
- **Bilingual annotation**: English terms for key metrics (CAGR, TAM, GMV)
- **No filler**: Zero generic statements like "market has broad prospects"

## Quality Gates

Before delivering, self-check:

- [ ] Search used **target market's local language** keywords (not only English)
- [ ] Sales/category priority data comes from **local e-commerce platforms** (not social media buzz)
- [ ] Competitor list prioritizes **local competitors** (international brands as reference only)
- [ ] Price analysis based on **local currency and purchasing power**
- [ ] Channel strategy matches **local channel structure** (not another market's model)
- [ ] Key assumptions (category priority, brand attribution) **confirmed with user**
- [ ] Every data point has source annotation
- [ ] At least 3 tables, at least 2 frameworks
- [ ] No hallucinated data — if no reliable source exists, explicitly state [data unavailable]

## Data Verification Protocol

- **Cross-verify all key data points** with at least 2 independent sources
- **Social media data** must be cross-checked against e-commerce sales data
- **User-provided information** takes priority over web-sourced data
- When uncertain, **ask the user directly** rather than making assumptions

## Resources

- `references/methodology.md` — Complete analysis frameworks, methodologies, and local-first research protocol
- `references/report-structure.md` — Standard report template with all sections
- `assets/report-template.html` — HTML template for web deployment
- `scripts/generate_report.py` — Python script to generate formatted markdown reports from JSON input

## Compatibility

This skill follows the [Open Agent Skills standard](https://agentskills.io) and is compatible with:
- OpenAI Codex CLI
- WorkBuddy / CodeBuddy
- Claude Code
- Other agents skills-compliant clients
