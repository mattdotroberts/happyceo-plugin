---
name: log-task
description: Quickly log a task you're working on
user-invocable: true
allowed-tools: AskUserQuestion, mcp__notion__notion-create-pages, mcp__notion__notion-search
---

# Log Task

Quickly capture a task to the Notion Tasks database.

## Step 1: Get Task Details

Ask user:
```
What task are you working on?
```

Then ask:
```
Any details? (Related project, deadline, hours estimate - or skip)
```

## Step 2: Create Task in Notion

Use mcp__notion__notion-create-pages:
```
Parent: data_source_id [Tasks database ID from CLAUDE.md]
Properties:
  - "Task Name": [Task description]
  - "Status": "In Progress"
  - "Description": [Details if provided]
  - "date:Deadline:start": [Date if provided]
  - "date:Deadline:is_datetime": 0
  - "Hours": [Hours if provided]
```

If a project is mentioned, search Projects database (ID from CLAUDE.md) to find the URL and add to "Projects" relation.

## Step 3: Confirm

```
Task logged: "[Task Name]"
Status: In Progress
Project: [Project name or "None"]
Deadline: [Date or "None set"]

View: [Notion URL]
```

## Quick Usage

User can also invoke with inline description:
- `/happyceo:log-task Fix the signup bug` - Creates task directly
- `/happyceo:log-task` - Prompts for details
