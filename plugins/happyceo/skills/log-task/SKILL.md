---
name: log-task
description: Quick task capture to your knowledge base. Trigger with "log a task", "add a task", "I need to [task]", "remind me to [task]", or "create a task for [description]".
---


# Log Task

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


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