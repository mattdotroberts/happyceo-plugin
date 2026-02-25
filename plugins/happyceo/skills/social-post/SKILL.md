---
name: social-post
description: Select an idea from your queue, polish it with 2-3 variations, and mark as published. Trigger with "publish a post", "social post", "post from queue", or "write today's post".
---


# Social Post

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


Select a queued idea from Notion, polish it with variations, and mark as posted.

## Storage

**Notion Socials Database:** Use the Socials database ID from CLAUDE.md.

**If Socials database is not configured:** Tell the user to run `/happyceo:setup` to connect a Socials database.

## Usage

- `/happyceo:social-post` — Interactive selection from queue
- `/happyceo:social-post 3` — Select idea #3 directly
- `/happyceo:social-post [topic]` — Select by topic description

## Workflow

### Step 1: Show Queue

Fetch the Socials database using `mcp__notion__notion-fetch` with the Socials data source URL from CLAUDE.md.

Filter to entries where Status is NOT "Published". Display using the same format as `/happyceo:social-queue`:
- Group by day, today first
- Number each idea for selection
- Show Name + truncated Content Text preview + Platform

### Step 2: Select Idea

```
AskUserQuestion:
- question: "Which idea do you want to work on?"
- options: [1, 2, 3, 4, 5, Let me describe it]
```

If "Let me describe it" — search entries for matching text.

If argument was provided (number or topic), auto-select the matching entry.

### Step 3: Show Full Idea

Display the complete idea from Notion:

```markdown
## Selected Idea

**Name:** [Name]
**Day/Format:** [Day] — [Format]
**Platform:** [Platform]

**Raw idea:**
> [full Content Text]

**Image:** [Image URL or "none"]
```

### Step 4: Auto-Polish with draft-post logic

1. Read `content/content-calendar.md` to get today's format requirements
2. Read `content/linkedin-style.md` for style guide
3. Read `content/icp.md` for messaging alignment
4. Generate 2-3 polished variations based on the idea's tagged format

Present variations:

```markdown
## Polished Variations

### Option A — [style description]
[full post text]
_[character count]_

### Option B — [style description]
[full post text]
_[character count]_

### Option C — [style description]
[full post text]
_[character count]_
```

### Step 5: User Selects

```
AskUserQuestion:
- question: "Which version?"
- options: [A, B, C, Refine one of these, Start over]
```

**If "Refine":** Ask what to change, regenerate.

### Step 6: Final Post

Show the selected post ready to copy:

```markdown
## Ready to Post

---
[final post text]
---

**Characters:** [count] (LinkedIn limit: 3000)
**Platform:** [Platform]
**Image:** [filename or "none"]

Copy the text above and paste into LinkedIn/X.
```

### Step 7: Mark as Posted

```
AskUserQuestion:
- question: "Mark as posted?"
- options: [Yes - I posted it, No - save for later, Delete - bad idea]
```

**If "Yes":**
Update the Notion page using `mcp__notion__notion-update-page`:
- Set Status to "Published"
- Set Publish Date to today
- Store final post text as page body content

**If "No":**
Update Status to "Draft" (still in queue but marked as worked on).

**If "Delete":**
Archive the page.

### Step 8: Confirmation

```
Marked as published ([date])

Queue now has [X] ideas remaining.
```

## Notes

- The polish step uses the same logic as `/happyceo:draft-post`
- Character count helps avoid LinkedIn truncation
- Images should be downloaded/saved separately for manual upload
- Final post text is stored as page body content in Notion for future reference
- When posting to both LinkedIn + X, note X has a 280-char limit — may need a shorter version