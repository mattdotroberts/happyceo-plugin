# HappyCEO Setup Guide

Detailed instructions for connecting each integration.

## 1. Notion (Required)

HappyCEO needs Notion for task management, CRM, meetings, and social content.

### Install the Notion MCP Server

Follow the [Notion MCP setup guide](https://github.com/anthropics/claude-code-mcp-servers) to connect your Notion workspace.

### Database Setup

The `/happyceo:setup` wizard can search for existing databases or create new ones. You need at minimum:

| Database | Purpose | Required? |
|----------|---------|-----------|
| Tasks | Task tracking with status, deadlines, hours | Yes |
| CRM | Contacts, leads, clients | Yes |
| Projects | Active projects | Recommended |
| Meetings | Meeting notes and follow-ups | Recommended |
| Subscribers | Email subscriber list | Optional |
| Socials | Social media content queue | Optional |

### Expected Schemas

**Tasks:** Task Name (title), Status (To Do/Backlog/In Progress/Done), Assignee (people), Deadline (date), Description (rich_text), Hours (number)

**CRM:** Name (title), Email (email), Status (Lead/Proposal/Active/Finished/Lost), Company (text), Notes (rich_text)

**Meetings:** Meeting Name (title), Date (date), Contact (relation to CRM), Notes (rich_text)

**Socials:** Name (title), Status (Ideas/Draft/Review/Scheduled/Published), Platform (multi_select), Content Text (rich_text), Day (select), Format (select)

## 2. Gmail (Optional)

Enables `/happyceo:inbox` for email triage, task creation from emails, and draft replies.

### Setup

Install the Gmail MCP server and authenticate with your Google account. The setup wizard will detect it automatically.

### What It Enables

- Full inbox triage in `/happyceo:start-day` and `/happyceo:end-day`
- Draft follow-up emails from `/happyceo:meeting-wrap`
- Email sending from `/happyceo:monthly-email`
- Archive noise emails automatically

## 3. Slack (Optional)

Enables daily briefing and wrap-up posts to a Slack channel.

### Setup

1. Create a Slack app at https://api.slack.com/apps
2. Add the `chat:write` scope
3. Install to your workspace
4. Copy the Bot User OAuth Token (starts with `xoxb-`)
5. Get the Channel ID of your target channel (right-click channel > View channel details)

### Configuration

The setup wizard will ask for:
- **SLACK_BOT_TOKEN** — Your bot's OAuth token
- **SLACK_CHANNEL_ID** — The channel to post to

These go in your `.env` file.

## 4. Google Calendar (Optional)

Enables meeting awareness in `/happyceo:start-day` and time-based meeting prep.

### Setup

1. Create a service account in Google Cloud Console
2. Enable the Google Calendar API
3. Download the service account JSON key
4. Share your calendar with the service account email address

### Configuration

The setup wizard will ask for:
- **Path to service account JSON** (e.g., `config/google-calendar-key.json`)
- **Calendar ID** (usually your email address)

### Dependencies

```bash
pip install google-auth google-auth-httplib2 google-api-python-client
```

## 5. Resend (Optional)

Enables sending monthly email roundups to your subscriber list.

### Setup

1. Create a Resend account at https://resend.com
2. Verify your sending domain
3. Create an API key

### Configuration

The setup wizard will ask for:
- **RESEND_API_KEY** — Your Resend API key
- **From email** — The verified sending address
- **From name** — Display name for emails

## 6. Brandfetch (Optional)

Used by `scripts/fetch-logo.py` to download client logos for proposals.

### Setup

1. Get an API key from https://brandfetch.com
2. Add `BRANDFETCH_API_KEY` to your `.env`

## Troubleshooting

### "Database not configured"
Run `/happyceo:setup` to connect your Notion databases.

### Notion search returns no results
Make sure your Notion MCP server has access to the databases. Check the MCP server configuration.

### Slack posts fail
Verify your bot token and channel ID. Make sure the bot has been invited to the channel.

### Calendar returns empty
Check that the service account email has been added to the calendar's sharing settings.

### Gmail MCP not found
Make sure the Gmail MCP server is installed and running. Check `claude mcp list` for status.
