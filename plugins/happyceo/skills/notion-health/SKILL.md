---
name: notion-health
description: Data hygiene check — find stale leads, missing fields, overdue tasks, and records needing attention. Trigger with "check data health", "notion hygiene", "stale leads", "data cleanup", or "audit my CRM".
---


# Notion Health Check

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


Run a data hygiene check across CRM, Projects, and Tasks databases.

**If any required database is not configured in CLAUDE.md:** Skip that section and note it in the report.

## Step 1: Query CRM for Stale Leads

Search CRM for leads and proposals:
```
mcp__notion__notion-search with:
- query: "lead proposal"
- data_source_url: [CRM database ID from CLAUDE.md]
```

For each result with Status = "Lead" or "Proposal", check the timestamp:
- **>7 days:** Needs follow-up
- **>14 days:** Stale - review required
- **>30 days:** Consider closing as Lost

## Step 2: Check for Missing CRM Fields

Flag CRM contacts missing critical fields:
- No Email (for Lead/Proposal/Active)
- No Budget (for Proposal/Active)
- No Owner

## Step 3: Query Projects for Status Issues

Search Projects:
```
mcp__notion__notion-search with:
- query: "active parking"
- data_source_url: [Projects database ID from CLAUDE.md]
```

Flag:
- Status = "Active" with no recent meeting notes
- Status = "Parking Lot" for >30 days

## Step 4: Check Tasks Database

Search Tasks for overdue or stale items:
```
mcp__notion__notion-search with:
- query: "in progress to do"
- data_source_url: [Tasks database ID from CLAUDE.md]
```

Flag:
- Tasks with Deadline in the past
- Tasks "In Progress" for >14 days

## Step 5: Generate Health Report

Present findings:

```markdown
# Notion Health Report
**Date:** [Today]

## CRM - Attention Needed

### Stale Leads/Proposals
| Contact | Company | Days Stale | Suggested Action |
|---------|---------|------------|------------------|
| [Name] | [Company] | [X days] | Follow up / Close |

### Missing Data
| Contact | Missing Fields |
|---------|----------------|
| [Name] | Email, Budget |

## Projects - Attention Needed

### Long-term Parking Lot (>30 days)
| Project | Client | Days Parked |
|---------|--------|-------------|

## Tasks - Attention Needed

### Overdue
| Task | Deadline | Days Overdue |
|------|----------|--------------|

### Stale In Progress (>14 days)
| Task | Started | Days |
|------|---------|------|
```

## Step 6: Offer Quick Actions

Ask:
- "Would you like me to update any of these records?"
- "Should I draft follow-up emails for stale leads?"
- "Mark any leads as Lost?"
- "Complete or remove any stale tasks?"