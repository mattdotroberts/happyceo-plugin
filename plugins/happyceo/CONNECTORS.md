# Connectors

## How tool references work

Plugin files use `~~category` as a placeholder for whatever tool the user connects in that category. For example, `~~knowledge base` might mean Notion, Confluence, or any other knowledge base with an MCP server.

Plugins are **tool-agnostic** — they describe workflows in terms of categories (knowledge base, email, chat, etc.) rather than specific products. The `.mcp.json` pre-configures specific MCP servers, but any MCP server in that category works.

## Connectors for this plugin

| Category | Placeholder | Included servers | Other options |
|----------|-------------|-----------------|---------------|
| Knowledge base | `~~knowledge base` | Notion | Confluence, Coda |
| Email | `~~email` | Gmail | Microsoft 365 |
| Chat | `~~chat` | Slack | Microsoft Teams |
| Calendar | `~~calendar` | Google Calendar | Microsoft 365 |

## Required vs Optional

| Connector | Required? | What it enables |
|-----------|-----------|-----------------|
| **Knowledge base** | Required | Task management, CRM, meetings, social content queue |
| **Email** | Optional | Inbox triage, draft replies, monthly email sending |
| **Chat** | Optional | Daily briefings and wrap-ups posted to a channel |
| **Calendar** | Optional | Meeting awareness in daily briefings |

Skills gracefully skip unconfigured connectors — start with just a knowledge base and add more over time.
