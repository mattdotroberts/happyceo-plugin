---
name: meeting-prep
description: Prepare for an upcoming meeting with context, bio, and discovery questions
user-invocable: true
allowed-tools: AskUserQuestion, Bash, Read, WebSearch, mcp__notion__notion-search, mcp__notion__notion-create-pages, mcp__notion__notion-update-page
---

# Meeting Prep

Prepare comprehensively for a meeting. Ensures CRM and meeting records exist, researches the contact, and generates tailored discovery questions.

## Usage

- `/happyceo:meeting-prep` — Interactive mode (asks who the meeting is with)
- `/happyceo:meeting-prep Chris Cockton` — Prep for specific person
- `/happyceo:meeting-prep 10am` — Prep for meeting at specific time today

Can also be called programmatically from other skills (e.g., `/happyceo:start-day`).

## Workflow

### Step 1: Identify the Meeting

**If person/company provided:** Use it directly.

**If time provided:** Look up calendar for that time slot (if Google Calendar is configured in CLAUDE.md).

**If interactive mode:**
```
AskUserQuestion:
- question: "Who's the meeting with?"
- options: [Check my calendar, I'll type the name]
```

**If "Check my calendar":**
- If Google Calendar configured: run `python3 scripts/get-calendar.py 1`
- Present list and let user select
- If not configured: ask user to type the name

### Step 2: Check/Create CRM Record

**If CRM database is not configured in CLAUDE.md:** Skip CRM steps and note it.

Search CRM for the contact:
```
mcp__notion__notion-search with:
- query: "[person name] OR [company name]"
- data_source_url: [CRM database ID from CLAUDE.md]
```

**If found:**
- Read existing record
- Note any gaps (missing company, email, etc.)

**If not found:**
- Create new CRM record with:
  - Name
  - Company (if known)
  - Status: Lead
  - Notes: "Created during meeting prep"

### Step 3: Check/Create Meeting Record

**If Meetings database is not configured in CLAUDE.md:** Skip meeting record steps.

Search Meetings database:
```
mcp__notion__notion-search with:
- query: "[person name] [today's date]"
- data_source_url: [Meetings database ID from CLAUDE.md]
```

**If found:** Use existing record.

**If not found:** Create meeting record with:
- Title: "[Person Name] ([Company]) - [Date]"
- Date/time of meeting
- **Link to CRM record** (use relation property or embed URL)

### Step 3b: Link Records

Ensure bidirectional linking:

1. **Meeting -> CRM:** Add CRM page URL/link in meeting record
2. **CRM -> Meeting:** Update CRM record notes with link to meeting record

### Step 4: Research the Contact

**Gather info from multiple sources:**

1. **LinkedIn search:**
```
WebSearch: "[person name] [company] LinkedIn"
```

2. **Company search:**
```
WebSearch: "[company name] what they do"
```

3. **Recent news/activity:**
```
WebSearch: "[person name] OR [company] recent news"
```

**Extract and compile:**
- Current role and title
- Company description (what they do, size, industry)
- Career background (previous roles)
- Recent activity or posts (if visible)
- Any mutual connections or shared context

### Step 5: Generate Bio

Create a concise bio section:

```markdown
## Bio: [Person Name]

**Role:** [Title] at [Company]
**Company:** [Brief description of what they do]
**Background:** [1-2 sentences on career history]
**Recent:** [Any recent posts, news, or activity]

**How we connected:** [Source - referral, LinkedIn, event, etc.]
```

### Step 6: Generate Discovery Questions

Create 3 tailored discovery questions based on:
- Their role and responsibilities
- Their company's likely pain points
- Your ICP alignment (read `content/icp.md` if it exists)

```markdown
## Discovery Questions

### Role-Specific
1. [Question about their specific responsibilities or challenges]

### Company/Industry
2. [Question about their company's situation or market]

### Pain Points
3. [Question that uncovers potential needs you can solve]
```

### Step 7: Generate Opening Questions

Create 2-3 open-ended questions for early rapport:

```markdown
## Opening Questions (Early in Call)

- [Warm question about their work or recent activity]
- [Question that shows you've done research]
- [Question that invites them to share context]
```

### Step 8: Update Meeting Record

If Meetings database is configured, add all prep content to the meeting record.

### Step 9: Present Summary

Show the prep summary to the user:

```markdown
# Meeting Prep Complete

**Meeting:** [Person] @ [Time]
**CRM:** [Link to CRM record or "Not tracked"]
**Meeting Notes:** [Link to meeting record or "Not tracked"]

---

## Quick Bio
[1-2 sentence summary]

## Opening Questions
1. [Question 1]
2. [Question 2]

## Discovery Questions
1. [Question 1]
2. [Question 2]
3. [Question 3]

---

*Full prep saved to meeting record*
```

---

## Notes

- Always check if records exist before creating duplicates
- Bio should be factual, not flattering
- Questions should be genuinely curious, not leading
- If research returns nothing, note it and ask user for context
- Meeting record becomes the single source of truth for that meeting
