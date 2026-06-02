#!/usr/bin/env python3
"""
Brand Market Insight Report Generator

Reads a JSON input with report data and generates a formatted markdown report,
then optionally converts to HTML using the report-template.html.

Usage:
    python generate_report.py input.json --output report.md [--html report.html]
"""

import json
import sys
import os
from datetime import datetime


def load_template(name):
    """Load a template string from the report structures."""
    templates = {
        "full": """# {title}
## Executive Summary
{executive_summary}

## Key Findings at a Glance
{key_findings}

---

## 1. Market Overview
### 1.1 Market Size and Growth
{market_size}

### 1.2 Category Lifecycle Stage
{lifecycle}

### 1.3 Regional Variance Analysis
{regional}

## 2. Competitive Landscape
### 2.1 Competitor Identification
{competitor_id}

### 2.2 Competitor Matrix
{competitor_matrix}

### 2.3 Top Competitor Deep Dives
{competitor_deep}

### 2.4 SWOT Summary
{swot}

## 3. Consumer Profiling
### 3.1 Demographics
{demographics}

### 3.2 Consumption Behavior and Usage Scenarios
{behavior}

### 3.3 Content Preferences and Key Touchpoints
{content_prefs}

### 3.4 Purchase Decision Journey
{decision_journey}

## 4. Channel Analysis
### 4.1 Channel Structure Overview
{channel_structure}

### 4.2 Core Platform Strategy
{platform_strategy}

### 4.3 Channel ROI Assessment
{channel_roi}

## 5. Trends and Opportunities
### 5.1 Macro Consumer Trends
{macro_trends}

### 5.2 Category Innovation Direction
{innovation}

### 5.3 Potential Risks and Mitigation
{risks}

## 6. Brand Strategy Recommendations
### 6.1 Positioning Recommendation
{positioning}

### 6.2 Product Strategy
{product_strategy}

### 6.3 Channel Strategy
{channel_strategy}

### 6.4 Marketing Strategy
{marketing_strategy}

### 6.5 Risk Mitigation
{risk_mitigation}

## Appendix
### A. Data Sources and Methodology
{data_sources}

### B. Competitor List
{competitor_list}

### C. Disclaimer
{disclaimer}
""",
        "quick": """# {title} — Quick Competitor Scan
## Executive Summary
{executive_summary}

## Competitor Matrix
{competitor_matrix}

## Top 3 Competitor Depth
{competitor_deep}

## Key Takeaways
{key_takeaways}

---
*Data Sources: {data_sources}*
""",
        "entry": """# {title} — Market Entry Assessment
## Executive Summary
{executive_summary}

## Key Findings
{key_findings}

## 1. Market Opportunity
{market_size}

## 2. Competitive Landscape
{competitor_matrix}
{swot}

## 3. Target Consumer
{demographics}
{behavior}

## 4. Channel Entry Strategy
{channel_structure}
{platform_strategy}

## 5. Entry Recommendations
{positioning}
{product_strategy}
{marketing_strategy}
{risk_mitigation}

## Appendix
### Data Sources
{data_sources}
### Disclaimer
{disclaimer}
""",
    }
    return templates.get(name, templates["full"])


def generate_report(data, report_type="full"):
    """Generate a markdown report from structured data."""
    template = load_template(report_type)

    defaults = {
        "title": "Market Insight Report",
        "executive_summary": "[Executive summary to be provided]",
        "key_findings": "[Key findings table to be provided]",
        "key_takeaways": "[Key takeaways to be provided]",
        "market_size": "[Market size and growth data]",
        "lifecycle": "[Category lifecycle analysis]",
        "regional": "[Regional variance analysis]",
        "competitor_id": "[Competitor identification]",
        "competitor_matrix": "[Competitor matrix table]",
        "competitor_deep": "[Competitor deep dive analysis]",
        "swot": "[SWOT summary]",
        "demographics": "[Consumer demographics]",
        "behavior": "[Consumer behavior analysis]",
        "content_prefs": "[Content preference analysis]",
        "decision_journey": "[Purchase decision journey]",
        "channel_structure": "[Channel structure overview]",
        "platform_strategy": "[Platform strategy analysis]",
        "channel_roi": "[Channel ROI assessment]",
        "macro_trends": "[Macro consumer trends]",
        "innovation": "[Category innovation direction]",
        "risks": "[Risk analysis]",
        "positioning": "[Brand positioning recommendation]",
        "product_strategy": "[Product strategy recommendation]",
        "channel_strategy": "[Channel strategy recommendation]",
        "marketing_strategy": "[Marketing strategy recommendation]",
        "risk_mitigation": "[Risk mitigation recommendations]",
        "data_sources": "[Data sources to be listed]",
        "competitor_list": "[Competitor list to be provided]",
        "disclaimer": "This report is prepared for informational purposes only. Data sources include publicly available information and web research as of the report date. Market estimates involve inherent uncertainty. This report does not constitute investment or business advice.",
    }

    report_data = {**defaults, **data}
    report = template.format(**report_data)

    # Post-processing: add date if not present
    if "{{" not in report.get("title", ""):
        date_str = datetime.now().strftime("%Y-%m-%d")
        report = f"> Generated: {date_str} | Nicola Chen | Brand Market Insight System\n\n" + report

    return report


def markdown_to_html_sections(md_content):
    """Extract sections from markdown for HTML template population."""
    sections = {}
    current_section = None
    current_content = []

    for line in md_content.split("\n"):
        if line.startswith("## Executive Summary"):
            current_section = "executive_summary"
            current_content = []
        elif line.startswith("## Key Findings"):
            current_section = "key_findings"
            current_content = []
        elif line.startswith("## 1. Market"):
            if current_section and current_section not in ["executive_summary", "key_findings"]:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_1"
            current_content = []
        elif line.startswith("## 2. Competitive"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_2"
            current_content = []
        elif line.startswith("## 3. Consumer"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_3"
            current_content = []
        elif line.startswith("## 4. Channel"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_4"
            current_content = []
        elif line.startswith("## 5. Trends"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_5"
            current_content = []
        elif line.startswith("## 6. Brand"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "section_6"
            current_content = []
        elif line.startswith("## Appendix"):
            if current_section:
                sections[current_section] = "\n".join(current_content)
            current_section = "appendix"
            current_content = []
        elif current_section:
            current_content.append(line)

    if current_section and current_content:
        sections[current_section] = "\n".join(current_content)

    return sections


def generate_html(md_content, output_path):
    """Convert markdown report to HTML using the template."""
    skill_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.dirname(skill_dir) if os.path.basename(skill_dir) == "scripts" else skill_dir
    template_path = os.path.join(parent_dir, "assets", "report-template.html")

    if not os.path.exists(template_path):
        # Try alternative path
        template_path = os.path.join(os.path.dirname(skill_dir), "assets", "report-template.html")

    with open(template_path, "r", encoding="utf-8") as f:
        html_template = f.read()

    sections = markdown_to_html_sections(md_content)

    # Extract title from first line
    lines = md_content.strip().split("\n")
    title = lines[0].lstrip("# ").strip() if lines else "Market Insight Report"

    # Basic markdown-to-HTML conversion for sections
    def md_to_html(text):
        import re
        # Headers
        text = re.sub(r"^### (.+)$", r"<h3>\1</h3>", text, flags=re.MULTILINE)
        text = re.sub(r"^#### (.+)$", r"<h4>\1</h4>", text, flags=re.MULTILINE)
        # Bold
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        # Italic
        text = re.sub(r"\*(.+?)\*", r"<em>\1</em>", text)
        # Paragraphs
        paragraphs = text.split("\n\n")
        html_paragraphs = []
        for p in paragraphs:
            p = p.strip()
            if p.startswith("<h") or p.startswith("<table") or p.startswith("<ul") or p.startswith("<ol"):
                html_paragraphs.append(p)
            elif p and not p.startswith("|") and "|" not in p:
                html_paragraphs.append(f"<p>{p}</p>")
            elif p and "|" in p:
                # Simple table conversion
                rows = [r.strip() for r in p.split("\n") if r.strip()]
                if len(rows) >= 2:
                    html = ["<table>"]
                    for i, row in enumerate(rows):
                        cells = [c.strip() for c in row.split("|") if c.strip()]
                        tag = "th" if i == 0 else "td"
                        html.append("<tr>")
                        for cell in cells:
                            html.append(f"<{tag}>{cell}</{tag}>")
                        html.append("</tr>")
                    html.append("</table>")
                    html_paragraphs.append("\n".join(html))
        return "\n".join(html_paragraphs)

    # Populate template
    html = html_template
    html = html.replace("{{REPORT_TITLE}}", title)
    html = html.replace("{{REPORT_DATE}}", datetime.now().strftime("%Y-%m-%d"))
    html = html.replace("{{REPORT_AUTHOR}}", "Nicola Chen")
    html = html.replace("{{REPORT_MARKET}}", "Global Markets")
    html = html.replace("{{REPORT_CATEGORY}}", "Beauty & Wellness")

    for section_name, content in sections.items():
        placeholder = "{{" + section_name.upper() + "}}"
        html_content = md_to_html(content) if content else "<p>[Section content to be provided]</p>"
        html = html.replace(placeholder, html_content)

    with open(output_path, "w", encoding="utf-8") as f:
        f.write(html)

    return output_path


def main():
    if len(sys.argv) < 3:
        print("Usage: python generate_report.py <input.json> --output <output.md> [--html <output.html>] [--type full|quick|entry]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_md = None
    output_html = None
    report_type = "full"

    i = 2
    while i < len(sys.argv):
        if sys.argv[i] == "--output" and i + 1 < len(sys.argv):
            output_md = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--html" and i + 1 < len(sys.argv):
            output_html = sys.argv[i + 1]
            i += 2
        elif sys.argv[i] == "--type" and i + 1 < len(sys.argv):
            report_type = sys.argv[i + 1]
            i += 2
        else:
            i += 1

    with open(input_file, "r", encoding="utf-8") as f:
        data = json.load(f)

    report = generate_report(data, report_type)

    if output_md:
        os.makedirs(os.path.dirname(output_md) or ".", exist_ok=True)
        with open(output_md, "w", encoding="utf-8") as f:
            f.write(report)
        print(f"Markdown report written to: {output_md}")

    if output_html:
        html_path = generate_html(report, output_html)
        print(f"HTML report written to: {html_path}")

    if not output_md and not output_html:
        print(report)


if __name__ == "__main__":
    main()
