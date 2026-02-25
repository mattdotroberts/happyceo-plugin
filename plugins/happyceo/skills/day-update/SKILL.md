---
name: day-update
description: Quick mid-day check-in to update task progress and log time. Lighter than end-day. Trigger with "quick update", "update my tasks", "log progress", or "mid-day check-in".
---


# Day Update

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


A lightweight mid-day check-in to update task status and log time spent. Unlike `/happyceo:end-day`, this is quick and focused — just tasks.

## When to Use

- Mid-day progress check
- After completing a task
- Before switching contexts
- Quick time logging without full wrap-up

## Workflow

### Step 1: Fetch Active Tasks

Query Notion Tasks database for tasks where:
- Status = "In Progress" OR Status = "To Do"

```
Use mcp__notion__notion-search with data_source_url: [Tasks database ID from CLAUDE.md]
Filter for Status in ["In Progress", "To Do"]
```

**If Tasks database is not configured:** Tell the user to run `/happyceo:setup` first.

### Step 2: Display Task Summary

Show a quick overview:

```
## Your Active Tasks

1. [Task Name] - In Progress (2h logged)
2. [Task Name] - To Do (no time logged)
3. [Task Name] - In Progress (0.5h logged)
```

### Step 3: Per-Task Check-In

For each active task, use AskUserQuestion:

**Question format:**
```
"[Task Name] - currently [Status], [X]h logged. What's the update?"
```

**Options:**
1. "Still working" - Keep status, optionally add time
2. "Done" - Mark complete, log final hours
3. "Blocked" - Mark blocked, note blocker
4. "Not started" - No change
5. "Skip" - Move to next task

### Step 4: Collect Updates

Based on response:

**If "Still working" or "Done":**
- Ask: "How many hours on this? (current: Xh, or skip)"
- Accept decimal hours (0.5, 1, 2.5, etc.)
- Update Hours field in Notion

**If "Done":**
- Update Status to "Done" in Notion
- Log hours if provided

**If "Blocked":**
- Ask: "What's blocking this?"
- Offer to create a follow-up task for the blocker
- Keep Status as "In Progress" but note the blocker

### Step 5: Summary

After all tasks reviewed, show quick summary:

```
## Update Complete

**Tasks updated:** 3
**Hours logged:** 4.5h total
**Completed:** 1 task
**Blocked:** 1 task (created follow-up)

Run `/happyceo:end-day` for full wrap-up later.
```

## Notes

- This is meant to be quick — don't ask unnecessary questions
- Skip tasks the user doesn't want to update
- Hours are replaced, not accumulated (same as /happyceo:log-time)
- If no active tasks found, suggest running /happyceo:log-task to add one
- Don't post to Slack (save that for /happyceo:end-day)