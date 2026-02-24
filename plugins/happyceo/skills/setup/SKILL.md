---
name: setup
description: "Guided setup wizard — configure HappyCEO for your business"
user-invocable: true
allowed-tools: AskUserQuestion, Write, Edit, Read, Bash, Glob, mcp__notion__notion-search, mcp__notion__notion-fetch, mcp__notion__notion-create-database, mcp__notion__notion-update-data-source
---

# HappyCEO Setup Wizard

Welcome! This wizard will configure HappyCEO as your Co-CEO assistant. It takes about 5 minutes.

## What Gets Created

1. **PERSONA.md** — Your company identity and communication style
2. **CLAUDE.md** — Project configuration with all your database IDs and integration settings
3. **.env** — API keys for Slack, Resend, Brandfetch (optional)
4. **content/** — Content calendar, LinkedIn style guide, ICP document
5. **data/** — Working directories for inbox and archive
6. **.claude/settings.json** — Tool permissions

---

## Step 1: Company Identity

Ask the user these questions using AskUserQuestion (one at a time for complex ones, batch simple ones):

**Batch 1 — Identity:**
```
Question: "Let's set up your Co-CEO. What's your name?"
Options: [I'll type it]
```

Then:
```
Question: "What's your company name?"
Options: [I'll type it]
```

Then:
```
Question: "What's your company website URL?"
Options: [I'll type it, Don't have one yet]
```

Then:
```
Question: "In one sentence, what does your company do?"
Options: [I'll type it]
```

**Batch 2 — Team:**
```
Question: "Who else is on the team? (Names and roles — or just you)"
Options: [Just me, I'll list them]
```

**Batch 3 — Tone:**
```
Question: "How would you describe your communication style?"
Options:
- Professional but friendly (Recommended)
- Casual and direct
- Formal and polished
- I'll describe it
```

Store all answers as variables for template generation.

---

## Step 2: Generate PERSONA.md

1. Read the persona template: `templates/persona.md` (relative to plugin directory)
2. Fill in all `[placeholders]` with the user's answers from Step 1
3. Write to `PERSONA.md` in the project root

---

## Step 3: Connect Notion

```
Question: "Do you use Notion? HappyCEO uses it for tasks, CRM, meetings, and social content."
Options:
- Yes, connect Notion (Recommended)
- Skip for now
```

**If connecting Notion:**

### 3a: Find or Create Databases

For each of the 6 databases, search Notion and ask:

**Tasks Database:**
```
Question: "Do you have an existing Tasks database in Notion, or should I create one?"
Options:
- Search my Notion for it
- Create a new one
- I'll paste the database URL
```

If searching: Use `mcp__notion__notion-search` with query "Tasks" and look for databases.
If creating: Use `mcp__notion__notion-create-database` with these properties:
- Task Name (title)
- Status (status: To Do, Backlog, In Progress, Done)
- Assignee (people)
- Deadline (date)
- Projects (relation — if Projects DB exists)
- Description (rich_text)
- Hours (number)

Present the found/created database and confirm with the user.

**Repeat for each database:**

| Database | Search Query | Key Properties |
|----------|-------------|----------------|
| Tasks | "Tasks" | Task Name, Status, Assignee, Deadline, Description, Hours |
| CRM | "CRM" or "Contacts" or "Leads" | Name, Email, Status (Lead/Proposal/Active/Finished/Lost), Company, Notes |
| Projects | "Projects" | Project Name, Status, Client |
| Meetings | "Meetings" | Meeting Name, Date, Contact, Notes |
| Subscribers | "Subscribers" or "Email List" | Name, Email, Source |
| Socials | "Socials" or "Social Media" or "Content Queue" | Name, Status, Platform, Content Text, Publish Date, Day, Format |

Store each database's data_source_id (the `collection://...` URL from Notion).

If the user skips any database, note it as unconfigured.

---

## Step 4: Connect Integrations (Optional)

### 4a: Slack
```
Question: "Connect Slack for daily briefings and alerts?"
Options:
- Yes, I have a Slack bot token
- Skip Slack
```

If yes, ask for:
- Bot token (starts with `xoxb-`)
- Channel ID for posting (e.g., `#ceo-bot`)

### 4b: Gmail
```
Question: "Connect Gmail for inbox processing?"
Options:
- Yes, I have Gmail MCP configured
- Skip Gmail
```

If yes: Gmail works via MCP server — just note it's enabled.

### 4c: Google Calendar
```
Question: "Connect Google Calendar for meeting awareness?"
Options:
- Yes, I have a service account JSON
- Skip Calendar
```

If yes, ask for:
- Path to service account JSON file
- Calendar ID (usually your email)

### 4d: Resend (Email Sending)
```
Question: "Connect Resend for sending monthly emails?"
Options:
- Yes, I have a Resend API key
- Skip email sending
```

If yes, ask for:
- API key
- From email address
- From name

### 4e: Website Repo
```
Question: "Do you have a website repo for content publishing?"
Options:
- Yes, I'll provide the path
- Skip website integration
```

If yes, ask for the absolute path. Verify it exists.

---

## Step 5: Create Content Scaffolding

Create the following directory structure in the project root:

```
content/
├── content-calendar.md    (copy from templates/content-calendar.md)
├── linkedin-style.md      (copy from templates/linkedin-style.md)
├── icp.md                 (copy from templates/icp.md)
├── post-ideas.md          (empty starter)
└── weekly-priorities.md   (empty starter)
data/
├── inbox.md               (empty)
└── archive.md             (empty)
specs/                     (empty directory)
proposals/                 (empty directory)
```

Copy template files using Read + Write.

---

## Step 6: Generate CLAUDE.md

Write a comprehensive CLAUDE.md to the project root. This is the core configuration file.

**Template — fill in all values from previous steps:**

```markdown
# HappyCEO — [Company Name] Configuration

## Identity

| Key | Value |
|-----|-------|
| Your Name | [name] |
| Company | [company name] |
| Website | [url] |
| Mission | [one-liner] |
| Team | [team members] |

## Notion Databases

| Database | Data Source ID | Status |
|----------|---------------|--------|
| Tasks | [collection://...] | [Connected/Not configured] |
| CRM | [collection://...] | [Connected/Not configured] |
| Projects | [collection://...] | [Connected/Not configured] |
| Meetings | [collection://...] | [Connected/Not configured] |
| Subscribers | [collection://...] | [Connected/Not configured] |
| Socials | [collection://...] | [Connected/Not configured] |

## Integrations

| Service | Status | Notes |
|---------|--------|-------|
| Notion | [Ready/Not configured] | MCP server |
| Slack | [Ready/Not configured] | Bot token in .env |
| Gmail | [Ready/Not configured] | MCP server |
| Google Calendar | [Ready/Not configured] | Service account |
| Resend | [Ready/Not configured] | API key in .env |
| Website Repo | [Ready/Not configured] | [path] |

## Slack Configuration

- Channel: [channel ID or "Not configured"]
- Post briefings: [true/false]

## Email Configuration

- From: [email or "Not configured"]
- From Name: [name or "Not configured"]
- Reply-To: [email or "Not configured"]

## Website Configuration

- Repo Path: [path or "Not configured"]
- Blog Path: [relative path to blog content]
- Content Types: [blog, use-cases, services, etc.]

## Calendar Configuration

- Calendar ID: [email or "Not configured"]
- Service Account: [path or "Not configured"]

## Key Files

| File | Purpose |
|------|---------|
| PERSONA.md | Company identity and communication style |
| CLAUDE.md | This configuration file |
| content/icp.md | Ideal Customer Profile |
| content/linkedin-style.md | LinkedIn writing style guide |
| content/content-calendar.md | Weekly posting schedule |
| content/weekly-priorities.md | Weekly priorities tracker |
| data/inbox.md | Daily scratchpad |
| data/archive.md | Permanent organized notes |
| templates/proposal.md | Client proposal template |
| templates/case-studies.md | Case studies for proposals |
| templates/monthly-roundup.md | Email template |
| templates/email-html.html | HTML email template |

## Session Startup

**Always read PERSONA.md** at the start of every session for company context.
**Always run `date`** to get current date, time, and day of week.

## Notion Database Schemas

### Tasks
Task Name (title), Status (To Do/Backlog/In Progress/Done), Assignee (people), Deadline (date), Projects (relation), Description (rich_text), Hours (number)

### CRM
Name (title), Email (email), Status (Lead/Proposal/Active/Finished/Lost), Company (text), Notes (rich_text)

### Meetings
Meeting Name (title), Date (date), Contact (relation to CRM), Notes (rich_text)

### Socials
Name (title), Status (Ideas/Draft/Review/Scheduled/Published), Platform (multi_select), Publish Date (date), Content Text (rich_text), Content Type (select), Author (select), Day (select), Format (select), Image (url)

### Subscribers
Name (title), Email (email), Source (text), Terms Accepted (checkbox)

## Skill Execution Rules

Skills have mandatory actions. When running a skill:
1. Read the skill file completely before starting
2. Look for "MANDATORY ACTIONS" or "REQUIRED" markers
3. Complete ALL required steps before considering the skill done

## Proactive Behaviors

### After Meetings
When you mention having a meeting with someone:
1. Check if they exist in CRM
2. Offer to update their record
3. If new contact, offer to create CRM entry

### Task Detection
When you say "I'm working on...", "I need to...", or "Today I'll...":
- Offer to log it: "Want me to add that to your Tasks?"

### Time Logging
When you say "spent X hours on..." or "worked X hours on...":
- Offer: "Want me to log X hours to '[Task]'?"
```

---

## Step 7: Generate .env

Write `.env` file with collected API keys:

```
# HappyCEO Environment Variables
# Generated by /happyceo:setup

# Slack (optional)
SLACK_BOT_TOKEN=[token or empty]
SLACK_CHANNEL_ID=[channel or empty]

# Resend (optional)
RESEND_API_KEY=[key or empty]
RESEND_FROM_EMAIL=[email or empty]
RESEND_FROM_NAME=[name or empty]

# Brandfetch (optional — used by fetch-logo.py)
BRANDFETCH_API_KEY=

# Google Calendar (optional)
GOOGLE_CALENDAR_ID=[calendar ID or empty]
GOOGLE_SERVICE_ACCOUNT_PATH=[path or empty]
```

---

## Step 8: Generate .claude/settings.json

```json
{
  "permissions": {
    "allow": [
      "Bash(python3 scripts/get-calendar.py*)",
      "Bash(python3 scripts/fetch-logo.py*)",
      "Bash(date*)",
      "mcp__notion__*",
      "Read(*)",
      "Write(*)",
      "Edit(*)",
      "Glob(*)",
      "Grep(*)"
    ]
  }
}
```

---

## Step 9: Smoke Test

Run quick checks on configured integrations:

1. **Notion:** Try `mcp__notion__notion-search` with a simple query. Confirm it returns results.
2. **Calendar:** If configured, run `python3 scripts/get-calendar.py 1` and check output.
3. **File structure:** Verify all key files exist with `Glob`.

---

## Step 10: Summary

Display a summary of everything that was configured:

```
✅ HappyCEO Setup Complete!

Company: [name]
Your Name: [name]

📋 Notion Databases:
  ✅ Tasks: Connected
  ✅ CRM: Connected
  ⏭️ Projects: Skipped
  ...

🔌 Integrations:
  ✅ Slack: Connected (#channel)
  ⏭️ Gmail: Not configured
  ...

📁 Files Created:
  - PERSONA.md
  - CLAUDE.md
  - .env
  - content/content-calendar.md
  - content/linkedin-style.md
  - data/inbox.md
  - data/archive.md

🚀 Next Steps:
1. Run /happyceo:start-day for your first morning briefing
2. Customize content/linkedin-style.md with your writing examples
3. Fill in templates/case-studies.md for better proposals
4. Run /happyceo:log-task to test task creation
```
