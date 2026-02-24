---
description: Capture a social post idea to the queue
argument-hint: "<idea text>"
---

# Social Idea

Quickly capture a social post idea to the Notion Socials database.

## Storage

**Notion Socials Database:** Use the Socials database ID from CLAUDE.md.

**If Socials database is not configured:** Tell the user to run `/happyceo:setup` to connect a Socials database.

**Schema:**
| Property | Type | Notes |
|----------|------|-------|
| Name | title | Short descriptive title |
| Status | status | Ideas, Draft, Review, Scheduled, Published |
| Platform | multi_select | LinkedIn, X, Blog, Newsletter, YouTube |
| Publish Date | date | Set when published |
| Content Text | text | The raw idea / post text |
| Content Type | select | LinkedIn, Blog Post, Newsletter, Video, Workshop Content |
| Author | select | [Your Name from CLAUDE.md] |
| Day | select | Monday, Tuesday, Wednesday, Thursday, Friday, Weekend, Flexible |
| Format | select | Week Ahead, Tutorial, Hot Take, Case Study, Field Notes, Personal, Event Promo |
| Image | url | URL or local path to image |

## Usage

- `/happyceo:social-idea` — Interactive mode
- `/happyceo:social-idea "rough idea here"` — Inline with text
- `/happyceo:social-idea "idea" /path/to/image.jpg` — Inline with image path

## Workflow

### Step 1: Get the Idea

**If inline text provided:** Use it directly.

**If interactive mode:**
```
AskUserQuestion:
- question: "What's the idea? (rough is fine)"
- options: [I'll type it out]
```

Accept freeform text input.

### Step 2: Check for Image

**If image path provided inline:** Use it directly.

**Otherwise ask:**
```
AskUserQuestion:
- question: "Any image to go with this?"
- options: [No image, I'll paste one, I'll provide a path]
```

**If "I'll paste one":**
- Wait for user to paste image in next message
- Grab the latest image from Downloads:
  ```bash
  ls -t ~/Downloads/*.{png,jpg,jpeg,gif,webp} 2>/dev/null | head -1
  ```
- Copy to `data/social-images/` with timestamp prefix

### Step 3: Suggest Day/Format

Read `content/content-calendar.md` to understand the formats:
- Monday: Week Ahead (short punchy list)
- Tuesday: Tutorial/How-To
- Wednesday: Hot Take (single strong opinion)
- Thursday: Case Study/Win
- Friday: Field Notes (numbered observations)
- Weekend: Personal/Long-form

Analyze the idea content and suggest the best fit:

```
AskUserQuestion:
- question: "This feels like a [Day] post ([Format]). Sound right?"
- options: [Yes, Monday - Week Ahead, Wednesday - Hot Take, Friday - Field Notes, Tuesday - Tutorial, Thursday - Case Study, Flexible - any day]
```

### Step 4: Determine Platform

Default to LinkedIn unless the idea clearly fits another platform.

```
AskUserQuestion:
- question: "Platform?"
- options: [LinkedIn (Recommended), X, Both LinkedIn + X]
```

### Step 5: Save to Notion

Create a page in the Socials database using `mcp__notion__notion-create-pages`:

```json
{
  "parent": {"data_source_id": "[Socials database ID from CLAUDE.md]", "type": "data_source_id"},
  "pages": [{
    "properties": {
      "Name": "[Short descriptive title from idea]",
      "Status": "Ideas",
      "Platform": "[LinkedIn/X/both]",
      "Content Text": "[Full idea text]",
      "Content Type": "LinkedIn",
      "Author": "[Your Name from CLAUDE.md]",
      "Day": "[Selected day]",
      "Format": "[Selected format]",
      "Image": "[image path or omit if none]"
    }
  }]
}
```

**Title generation:** Create a short (3-8 word) descriptive title from the idea text.

### Step 6: Confirm

Show confirmation:

```
Idea saved to Notion Socials

"[truncated idea preview...]"
Day: [Day] | Format: [Format] | Platform: [Platform]
[+ image: filename.jpg] (if applicable)

Run `/happyceo:social-queue` to see all ideas.
Run `/happyceo:social-post` when ready to polish and post.
```

## Notes

- Keep capture fast — under 30 seconds
- Rough ideas are fine, polishing happens at post time
- Images are optional but encouraged
- Day/format is a suggestion, can be changed when posting
- Default author is the user's name from CLAUDE.md