# HappyCEO — Co-CEO Plugin for Claude Code

Run your agency like a CEO with an AI chief of staff. HappyCEO is a 19-skill system that handles your daily briefings, meeting prep and follow-up, CRM hygiene, social content pipeline, client proposals, monthly emails, and task management.

## Quick Start

```bash
# Add the marketplace
claude plugin marketplace add mattdotroberts/happyceo-plugin

# Install the plugin
claude plugin install happyceo
```

Then run the setup wizard:
```
/happyceo:setup
```

The setup wizard will:
1. Gather your company identity
2. Connect your Notion databases (Tasks, CRM, Projects, Meetings, Subscribers, Socials)
3. Optionally connect Slack, Gmail, Google Calendar, and Resend
4. Generate your PERSONA.md, CLAUDE.md, .env, and content scaffolding

## Requirements

- [Claude Code](https://claude.com/claude-code) 2.0+
- [Notion MCP server](https://github.com/anthropics/claude-code-mcp-servers) configured
- A Notion workspace with (or the wizard will create): Tasks, CRM, and optionally Meetings, Projects, Subscribers, Socials databases

### Optional Integrations

| Integration | What It Enables | Setup |
|-------------|----------------|-------|
| Gmail MCP | Inbox triage, email drafting | Gmail MCP server |
| Slack | Daily briefings posted to a channel | Bot token + channel ID |
| Google Calendar | Meeting awareness in briefings | Service account JSON |
| Resend | Monthly email sending | API key |
| Brandfetch | Logo fetching for proposals | API key |

## Connectors

The plugin auto-configures MCP connectors for Notion, Gmail, Slack, and Google Calendar. See [CONNECTORS.md](CONNECTORS.md) for details.

## Commands

### Daily Operations
| Command | Description |
|---------|-------------|
| `/happyceo:start-day` | Morning briefing — calendar, pipeline, tasks, inbox, content calendar |
| `/happyceo:end-day` | Daily wrap-up — log tasks, capture wins, update CRM, prep tomorrow |
| `/happyceo:day-update` | Quick mid-day check-in to update task progress and log time |

### Meetings
| Command | Description |
|---------|-------------|
| `/happyceo:meeting-prep` | Research contact, create CRM/meeting records, generate discovery questions |
| `/happyceo:meeting-wrap` | Extract insights, create tasks, draft follow-up email, update CRM |

### Tasks & CRM
| Command | Description |
|---------|-------------|
| `/happyceo:log-task` | Quick task capture to Notion |
| `/happyceo:log-time` | Log hours spent on a task |
| `/happyceo:notion-health` | Data hygiene check — stale leads, missing fields, overdue tasks |

### Email
| Command | Description |
|---------|-------------|
| `/happyceo:inbox` | Process Gmail — triage, archive noise, create tasks, draft replies |
| `/happyceo:monthly-email` | Compose and send the monthly customer email roundup |
| `/happyceo:note` | Quick capture to inbox scratchpad |

### Content & Social
| Command | Description |
|---------|-------------|
| `/happyceo:draft-post` | Refine rough drafts into polished LinkedIn posts with 2-3 variations |
| `/happyceo:social-idea` | Capture a social post idea to Notion |
| `/happyceo:social-queue` | View queued social post ideas grouped by day |
| `/happyceo:social-post` | Polish a queued idea and prepare it for posting |
| `/happyceo:event` | Generate event content — Luma descriptions, promotions, recaps |

### Business Development
| Command | Description |
|---------|-------------|
| `/happyceo:scope-proposal` | Interactive proposal builder with case study ranking |
| `/happyceo:spec` | Deep interview to create a detailed spec before building |

### Setup
| Command | Description |
|---------|-------------|
| `/happyceo:setup` | Guided wizard to configure everything |

## How It Works

HappyCEO uses your project's `CLAUDE.md` as its configuration. The setup wizard generates this file with your Notion database IDs, integration settings, and company identity. Commands read from CLAUDE.md to know where your data lives.

### Graceful Degradation

Every command checks which connectors are configured before running. If Gmail isn't set up, inbox commands skip email processing. If Slack isn't connected, Slack posting is skipped silently. You can start with just Notion and add connectors over time.

### Content System

The plugin includes a content calendar (`content/content-calendar.md`) and LinkedIn style guide (`content/linkedin-style.md`). The `/happyceo:draft-post` skill learns your writing preferences over time by logging which variations you choose.

### Memory

- `data/inbox.md` — Quick capture scratchpad, processed at end of day
- `data/archive.md` — Permanent organized notes
- `PERSONA.md` — Your company identity and communication style

## File Structure

```
your-project/
├── CLAUDE.md              # Generated config (database IDs, integrations)
├── PERSONA.md             # Generated company identity
├── .env                   # API keys (gitignored)
├── content/
│   ├── content-calendar.md
│   ├── linkedin-style.md
│   ├── icp.md
│   ├── post-ideas.md
│   └── weekly-priorities.md
├── data/
│   ├── inbox.md
│   └── archive.md
├── templates/
│   ├── proposal.md
│   ├── case-studies.md
│   ├── monthly-roundup.md
│   └── email-html.html
├── proposals/             # Generated proposals
├── specs/                 # Generated specs
└── scripts/
    ├── get-calendar.py
    └── fetch-logo.py
```

## License

MIT

## Credits

Built by [Happy Operators](https://happyoperators.com). Originally developed as a Co-CEO system for running an AI training agency, then packaged as a distributable plugin for other agency founders.
