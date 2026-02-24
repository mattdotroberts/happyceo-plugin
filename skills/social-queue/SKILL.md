---
name: social-queue
description: Review queued social post ideas
user-invocable: true
allowed-tools: Bash, mcp__notion__notion-fetch
---

# Social Queue

Browse and review your queued social post ideas from Notion.

## Storage

**Notion Socials Database:** Use the Socials database ID from CLAUDE.md.

**If Socials database is not configured:** Tell the user to run `/happyceo:setup` to connect a Socials database, or skip this skill.

## Usage

- `/happyceo:social-queue` — Show all queued ideas grouped by day

## Workflow

### Step 1: Get Current Day

Run `date "+%A"` to get the current day of the week.

### Step 2: Query Notion

Fetch the Socials database using `mcp__notion__notion-fetch` with the Socials data source URL from CLAUDE.md.

Parse all entries from the database.

Filter to show only entries where Status is NOT "Published" (i.e., Ideas, Draft, Review, Scheduled).

### Step 3: Group by Day

Organize ideas into groups:
- Monday — Week Ahead
- Tuesday — Tutorial
- Wednesday — Hot Take
- Thursday — Case Study
- Friday — Field Notes
- Weekend — Personal
- Flexible — Any day

### Step 4: Display Queue

**Format:**

```markdown
## Social Queue

**Today is [Day]** — showing [Day] ideas first

### [Today's Day] — [Format] ([count] ideas)
1. "[Name]" — [truncated Content Text ~50 chars...] — [Platform]
   [+ image] (if Image field set)
2. "[Name]" — [truncated Content Text...] — [Platform]

### [Next Day] — [Format] ([count] ideas)
1. "[Name]" — [truncated Content Text...] — [Platform]

### Flexible ([count] ideas)
1. "[Name]" — [truncated Content Text...] — [Platform]

---

**Total:** [X] queued ideas | [Y] published all-time

Run `/happyceo:social-post` to polish and post one.
Run `/happyceo:social-idea` to add a new idea.
```

**Ordering:**
1. Today's day first (if it's a posting day)
2. Then by content calendar order: Monday -> Wednesday -> Friday -> Tuesday -> Thursday -> Weekend
3. Flexible ideas last
4. Within each group, oldest first (FIFO)

### Step 5: Show Published Count

Count entries where Status is "Published" to show total published all-time.

## Empty Queue

If no queued ideas:

```
## Social Queue

Queue is empty.

Run `/happyceo:social-idea` to capture your first idea.
```

## Notes

- This is view-only — no modifications
- Use `/happyceo:social-post` to select and work on an idea
- Use `/happyceo:social-idea` to add new ideas
- Truncate long Content Text to ~50 chars with "..." for readability
- Show Platform badge (LinkedIn, X, etc.) next to each idea
