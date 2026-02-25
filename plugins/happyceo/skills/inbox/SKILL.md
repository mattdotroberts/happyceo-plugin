---
name: inbox
description: Process your email inbox — triage messages, archive noise, create tasks from actionable items, and draft replies. Trigger with "process my inbox", "check my email", "triage inbox", "email triage", or "what's in my inbox".
---


# Inbox Skill

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~email** | Inbox triage, draft replies, send follow-up emails |
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


Deep processing mode for triaging email, creating tasks, and drafting replies.

**Requires:** Gmail MCP server. If Gmail is not configured, tell the user to set it up and run `/happyceo:setup`.

## MANDATORY ACTIONS

This skill MUST:
1. **Show confirmation before archiving** - Never auto-archive without approval
2. **Show drafts before sending** - Never auto-send replies
3. **Create Notion tasks for actionable items** - Don't just summarize, capture

## Usage

- `/happyceo:inbox` - Full triage mode (process new + chip away at backlog)
- `/happyceo:inbox quick` - Summary only (for start-day integration)

## Workflow

### Step 1: Fetch Inbox State

Use `mcp__gmail__search_emails` to get inbox overview:

```
Query: "in:inbox"
MaxResults: 50
```

Also fetch oldest backlog items:
```
Query: "in:inbox older_than:7d"
MaxResults: 5
```

### Step 2: Categorize Each Email

Read each email with `mcp__gmail__read_email` and classify:

| Category | Criteria | Action |
|----------|----------|--------|
| **Noise** | Newsletters, notifications, receipts, marketing | Archive after summary |
| **FYI** | CC'd threads, announcements, no action needed | Archive silently |
| **Quick Reply** | Simple questions, scheduling, confirmations | Draft response |
| **Task** | Requests requiring work, follow-ups needed | Create Notion task |
| **Event Prep** | Workshops, meetings, events you're participating in | Create prep task with deadline |
| **CRM-related** | From someone in CRM database | Task + update CRM "Last" |
| **Urgent** | Deadlines, VIP senders, "ASAP" language, >3 days stale | Flag prominently |

**Task Detection - Create a task if email contains:**
- Direct requests: "can you...", "please...", "need you to...", "would you..."
- Action items: "action required", "todo", "follow up", "next steps"
- Deadlines: specific dates, "by Friday", "before the meeting"
- Bug reports or issues requiring investigation

**Event Prep Detection - Create a prep task if:**
- Email is about an event/workshop you're presenting, hosting, or contributing to
- Subject contains: "briefing", "prep", "submit", "your session"
- Email requests materials, slides, or content from you

**Priority Detection - Flag as URGENT if:**
- Contains deadline language: "by Friday", "EOD", "ASAP", "urgent"
- From CRM contact with Status = "Active" or "Proposal"
- Has been in inbox > 3 days without response

### Step 3: Process Noise

**Identify noise emails and present summary:**
```
Found [X] emails to archive:
- [N] newsletters
- [N] notifications
- [N] receipts/confirmations
- [N] marketing

Archive all? [Yes / Review individually / Skip]
```

**If approved:** Use `mcp__gmail__batch_modify_emails` to archive (remove INBOX label).

### Step 3b: Check Sent Messages

**Before drafting any replies, check what you've already sent:**

```
mcp__gmail__search_emails with:
- query: "in:sent newer_than:5d"
- maxResults: 20
```

Cross-reference sent messages against actionable inbox emails:
- If you've already replied to a thread, **do NOT offer to draft a reply**
- Note: "Already replied [date] — waiting on response"

### Step 4: Process Actionable Emails

For each email needing action:

#### 4a. Check CRM

If CRM database is configured in CLAUDE.md, search for sender:
```
mcp__notion__notion-search with:
- query: [sender email or name]
- data_source_url: [CRM database ID from CLAUDE.md]
```

#### 4b. Create Task (if needed)

If Tasks database is configured in CLAUDE.md:
```
mcp__notion__notion-create-pages with:
- parent: data_source_id [Tasks database ID from CLAUDE.md]
- properties:
  - "Task Name": "[Subject or AI-shortened version]"
  - "Status": "To Do"
  - "Description": "[1-2 sentence summary]\n\nSource: Email from [sender name]"
```

#### 4c. Draft Reply (if needed)

For emails needing response:
```
AskUserQuestion:
- question: "Email from [sender]: '[subject]' - How should we respond?"
- options: [Quick acknowledgment, Schedule meeting, Answer their question, I'll handle manually]
```

**If drafting:**
1. Generate reply draft
2. Show to user for approval
3. If "Send": Use `mcp__gmail__send_email` with `inReplyTo` and `threadId`
4. If "Save as draft": Use `mcp__gmail__draft_email`

### Step 5: Summary

Present final summary:

```markdown
## Inbox Processed

**Archived:** [N] emails ([N] newsletters, [N] notifications, [N] FYI)

**Tasks Created:**
- [ ] [Task 1] - from [Sender]
- [ ] [Task 2] - from [Sender]

**Replies Sent:**
- [Recipient 1] - [brief description]

**Replies Drafted (in Gmail):**
- [Recipient 1] - [brief description]

**Still in inbox:** [N] emails
**Backlog remaining:** [N] emails older than 7 days

---
*Next: Run `/happyceo:inbox` again tomorrow, or `/happyceo:inbox quick` in /happyceo:start-day*
```

## Quick Mode (`/happyceo:inbox quick`)

Summary only, no processing:

1. Fetch inbox counts
2. Return summary block:
```markdown
## Inbox
- **Unread:** [N] emails
- **Needs attention:** [N] (stale > 3 days)
- **Noise to archive:** ~[N]

*Run `/happyceo:inbox` for full triage*
```

## Error Handling

| Scenario | Handling |
|----------|----------|
| Gmail API error | Show error, continue with remaining emails |
| Email from unknown sender | Process normally, don't auto-create CRM entry |
| Very long thread (20+ messages) | Summarize last 5 only |
| Notion API failure | Complete email processing, note failed task for retry |
| Rate limiting | Back off, process fewer emails, warn user |

## Notes

- **Backlog strategy:** Each run processes newest first + oldest 5 from backlog
- **Never auto-send:** Always show drafts for approval
- **Never auto-archive actionable:** Only archive confirmed noise
- **CRM sync:** Update "Last" field whenever processing email from a contact