# Agent Skills Open Standard Compatible

This skill follows the [Agent Skills](https://agentskills.io) open standard.

## Installation

Codex CLI and other agents-skills clients can install this skill directly from GitHub:

```bash
$skill-installer install https://github.com/nyctocereusnicola/brand-market-insight-skill
```

## Directory Layout

```
brand-market-insight-skill/
├── SKILL.md                    # Required: metadata + instructions
├── references/                 # Optional: documentation
│   ├── methodology.md
│   └── report-structure.md
├── assets/                     # Optional: templates
│   └── report-template.html
└── scripts/                    # Optional: executable code
    └── generate_report.py
```

## Compatibility

| Client | Install Method | Status |
|--------|---------------|--------|
| OpenAI Codex CLI | `$skill-installer` or `~/.agents/skills/` | Compatible |
| WorkBuddy / CodeBuddy | `~/.workbuddy/skills/` | Native support |
| Claude Code | `~/.claude/skills/` | Compatible |
| Cursor | `.cursor/skills/` | Compatible |
| VS Code Copilot | `.github/skills/` | Compatible |
