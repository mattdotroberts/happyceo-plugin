---
name: log-time
description: Log hours spent on a task
user-invocable: true
allowed-tools: AskUserQuestion, mcp__notion__notion-search, mcp__notion__notion-update-page
---

# Log Time

Log hours spent on a task in the Notion Tasks database.

## Quick Usage

User can invoke with inline syntax:
- `/happyceo:log-time Fix signup bug 2.5` - Logs 2.5 hours to matching task
- `/happyceo:log-time 1.5` - Prompts for task, then logs 1.5 hours
- `/happyceo:log-time` - Prompts for both task and hours

## Step 1: Identify Task

**If inline with task name and hours:** Parse both from input
- Example: "Fix signup bug 2.5" → task="Fix signup bug", hours=2.5

**If inline with hours only:** Parse hours, then ask for task
- Example: "1.5" → hours=1.5, ask "Which task did you work on?"

**If no args:** Ask the user:
```
Which task did you work on?
```

Search Tasks database using mcp__notion__notion-search:
```
data_source_url: [Tasks database ID from CLAUDE.md]
query: [user's task description]
```

Present matching tasks and let user confirm or clarify.

## Step 2: Get Hours

**If hours already parsed from inline:** Skip to Step 3

**Otherwise ask:**
```
How many hours? (decimals OK: 0.5, 1.5, 2, etc.)
```

Accept decimal values (0.25, 0.5, 1, 1.5, 2, etc.)

## Step 3: Update Notion

Use mcp__notion__notion-update-page:
```
page_url: [task's Notion URL]
properties:
  - "Hours": [new hours value]
```

Note: This replaces the existing Hours value (does not add to it).

## Step 4: Confirm

Show confirmation:
```
Logged [hours] hours to "[Task Name]"
```

If the task previously had hours logged, show:
```
Logged [hours] hours to "[Task Name]" (was: [old hours] hours)
```
