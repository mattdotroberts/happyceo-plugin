# HappyCEO — Co-CEO Plugin for Claude Code

Run your agency like a CEO with an AI chief of staff. 19 skills for daily briefings, meetings, CRM, content, proposals, and email.

## Install

```bash
# 1. Add the marketplace
claude plugin marketplace add mattdotroberts/happyceo-plugin

# 2. Install the plugin
claude plugin install happyceo
```

## Setup

Once installed, run the setup wizard:

```
/happyceo:setup
```

This will walk you through connecting your Notion databases, optional integrations (Gmail, Slack, Calendar, Resend), and generating your config.

## Requirements

- [Claude Code](https://claude.ai/download) 2.0+
- [Notion MCP server](https://modelcontextprotocol.io/integrations/notion) configured

## What's Included

19 commands organized by workflow:

| Category | Commands |
|----------|----------|
| **Daily Ops** | `start-day`, `end-day`, `day-update` |
| **Meetings** | `meeting-prep`, `meeting-wrap` |
| **Tasks & CRM** | `log-task`, `log-time`, `notion-health` |
| **Email** | `inbox`, `monthly-email`, `note` |
| **Content** | `draft-post`, `social-idea`, `social-queue`, `social-post`, `event` |
| **Business Dev** | `scope-proposal`, `spec` |
| **Setup** | `setup` |

All commands are prefixed with `happyceo:` — e.g., `/happyceo:start-day`.

## Connectors

The plugin auto-configures MCP connectors for Notion, Gmail, Slack, and Google Calendar. Connect them during setup and commands will use them automatically.

| Connector | What It Enables |
|-----------|----------------|
| Notion | Task management, CRM, meetings, social content (required) |
| Gmail | Inbox triage, email drafting |
| Slack | Daily briefings posted to a channel |
| Google Calendar | Meeting awareness in briefings |

Commands gracefully skip unconfigured connectors — start with just Notion and add more over time.

## Documentation

- [Detailed setup guide](plugins/happyceo/SETUP-GUIDE.md)
- [Full README](plugins/happyceo/README.md)

## License

MIT — [Happy Operators](https://happyoperators.com)
