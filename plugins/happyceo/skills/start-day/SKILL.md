---
name: start-day
description: Morning briefing to set up your day
user-invocable: true
allowed-tools: AskUserQuestion, Bash, Read, Edit, Glob, Grep, WebSearch, mcp__notion__notion-search, mcp__notion__notion-create-pages, mcp__notion__notion-update-page, mcp__gmail__search_emails, mcp__gmail__read_email, mcp__gmail__send_email, mcp__gmail__draft_email, mcp__gmail__modify_email, mcp__gmail__batch_modify_emails
---

# Start Day Workflow

When this skill is invoked, generate a morning briefing to help you start your day productively.

## MANDATORY ACTIONS
This skill has FIVE required outputs:
1. **Display briefing** - Show the morning briefing
2. **Interactive check-in** - Use AskUserQuestion to gather priorities and take actions
3. **Full inbox triage** - Run the complete `/happyceo:inbox` workflow (if Gmail configured)
4. **Unwrapped meeting check** - Wrap any unwrapped meetings from yesterday via `/happyceo:meeting-wrap`
5. **Post to Slack** - Summary (if Slack configured)

Do NOT consider this skill complete until all are done.

## Step 0: Check Inbox Notes

**Read `data/inbox.md`.**

**If inbox has unprocessed items:**
```
AskUserQuestion:
- question: "You have X unprocessed inbox items from yesterday. What would you like to do?"
- options: [Process them now, Clear and start fresh, Leave them for later]
```

## Step 1: Gather Today's Schedule

**If Google Calendar is configured in CLAUDE.md:**
```bash
python3 scripts/get-calendar.py
```

**If not configured:** Ask the user about their schedule.

## Step 2: Query Notion Databases

Run these queries in parallel (skip any unconfigured databases):

### 2a. Pipeline Status (CRM)
If CRM configured: Search for leads and proposals.

### 2b. Recent Meetings (last 7 days)
If Meetings configured: Check for action items and follow-ups.

### 2c. Active Projects
If Projects configured: Note projects needing attention.

### 2d. My Tasks (In Progress / To Do)
If Tasks configured: Show active tasks.

### 2e. Gmail Inbox State
If Gmail configured: Fetch inbox counts (total, unread, stale > 3 days).

## Step 3: Check Content Calendar

**Read `content/content-calendar.md`.**

Determine today's content theme and whether it's a mandatory posting day (Mon/Wed/Fri).

## Step 3b: Weekly Priorities Check

**Read `content/weekly-priorities.md`** (if it exists).

### On Monday:
Use AskUserQuestion to set/review priorities.

### On Other Days:
Read and display current priorities in the briefing.

## Step 4: Generate Briefing

Present a structured morning briefing:

```markdown
# Good Morning, [Your Name from CLAUDE.md]

**Date:** [Today's date]

---

## Today's Content
**Theme:** [Day's theme from calendar]
*Run `/happyceo:draft-post` when ready*

---

## Today's Schedule
| Time | Meeting | Context |
|------|---------|---------|
| [time] | [meeting] | [relevant context] |

---

## Pipeline Check
**Leads:** [count] active
**Proposals:** [count] pending
**Action needed:**
- [ ] [Specific follow-up needed]

---

## Tasks
[Active tasks from Notion]

---

## Inbox
- **Unread:** [N] emails
- **Needs attention:** [N] (stale > 3 days)

---

## Data Hygiene Alert
**Stale Leads (>7 days):** [count]
**Overdue Tasks:** [count]
*Run `/happyceo:notion-health` for full report*

---

## This Week's Priorities
1. **[Priority 1]** - [Status]
2. **[Priority 2]** - [Status]

---

## Today's Focus
1. [Suggested focus 1]
2. [Suggested focus 2]
3. [Suggested focus 3]
```

## Step 5: Interactive Check-In

### 5a. Today's Priorities
```
AskUserQuestion:
- question: "What's your #1 priority today?"
- options: [From pipeline suggestions, From task list, Something else]
```

### 5b. Stale Lead Actions
For each stale lead (>14 days):
```
AskUserQuestion:
- question: "What should we do with [Lead Name]? (X days stale)"
- options: [Mark as Lost, Send follow-up, Schedule call, Keep watching]
```

### 5c. Meeting Prep
For each meeting on today's calendar:
```
AskUserQuestion:
- question: "Need any prep for [Meeting Name] at [Time]?"
- options: [Run full meeting prep, Pull CRM context, No prep needed]
```

If "Run full meeting prep": Execute the `/happyceo:meeting-prep` workflow.

### 5d. Blockers Check
```
AskUserQuestion:
- question: "Any blockers or concerns going into today?"
- options: [None, Need to reschedule something, Waiting on someone, Other]
```

## Step 6: Full Inbox Triage

If Gmail is configured:
```
AskUserQuestion:
- question: "Ready to triage your inbox?"
- options: [Yes - full triage, Quick summary only, Skip inbox today]
```

**If "Yes":** Execute the complete `/happyceo:inbox` skill workflow.
**If "Quick summary":** Show counts from Step 2e.
**If "Skip":** Continue.

## Step 7: Unwrapped Meeting Check

Check if there are meetings from **yesterday** that haven't been wrapped up yet.

If Meetings database is configured:
1. Fetch yesterday's meetings
2. For each: Check if it has a `## Post-Meeting Summary` section
3. If unwrapped meetings found, offer to wrap them via `/happyceo:meeting-wrap`

## Step 8: Monday Health Check

If today is Monday, offer to run `/happyceo:notion-health`.

## Step 9: Post to Slack

**If Slack is configured (.env has SLACK_BOT_TOKEN and SLACK_CHANNEL_ID):**

Post comprehensive summary to Slack with:
- Today's schedule
- Weekly priorities
- Pipeline snapshot
- Today's focus
- Content day theme (if applicable)
- Actions taken

```bash
source .env && curl -X POST 'https://slack.com/api/chat.postMessage' \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "channel": "'"$SLACK_CHANNEL_ID"'",
    "text": "[Comprehensive morning briefing summary]"
  }'
```

**If Slack is not configured:** Skip silently.

---

## Checklist

- [ ] Calendar checked (or asked manually)
- [ ] Notion databases queried (configured ones)
- [ ] Content calendar checked
- [ ] Briefing presented
- [ ] Interactive check-in completed
- [ ] Stale leads addressed
- [ ] Full inbox triage completed (if Gmail configured)
- [ ] Unwrapped meetings wrapped (if any)
- [ ] Slack summary posted (if configured)
