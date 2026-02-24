---
name: note
description: Quick capture to inbox
user-invocable: true
allowed-tools: AskUserQuestion, Read, Edit
---

# Note Skill

Quick capture to inbox. No thinking, just dump.

## Usage

- `/happyceo:note Acme budget is $50k` - Inline capture
- `/happyceo:note` - Asks "What's on your mind?"

## Workflow

### Step 1: Get the Note

**If inline argument provided:**
- Use the text after the command as the note content

**If no argument:**
- Use AskUserQuestion:
```
AskUserQuestion:
- question: "What's on your mind?"
- options: [I'll type it out]
```
- Wait for user's text input

### Step 2: Append to Inbox

Read `data/inbox.md` and append a new bullet with the note content.

**Format:**
```markdown
- [note content]
```

Add the bullet on a new line after the last existing bullet.

### Step 3: Confirm

Simple confirmation:
```
Added to inbox: "[first 50 chars of note]..."
```

---

## Notes

- This is intentionally minimal - no categorization, no thinking
- Inbox gets processed during `/happyceo:end-day`
- Items either go to memory archive or get discarded
