---
name: draft-post
description: Refine rough drafts into polished LinkedIn posts with 2-3 variations
user-invocable: true
allowed-tools: AskUserQuestion, Read, Edit, Bash, Glob
---

# Draft Post Workflow

When this skill is invoked, help the user refine a rough post idea into polished LinkedIn content with multiple variations to choose from.

## Usage

- `/happyceo:draft-post` - Interactive mode, will ask for your draft
- `/happyceo:draft-post "Just ran a workshop teaching 20 founders Claude Code"` - Inline mode with draft

---

## Step 1: Get the Draft

**If inline argument provided:** Parse the draft from the command.

**If no argument:** Ask:
```
What's your rough draft or post idea?

(Can be a few bullet points, a rough paragraph, or just the key message you want to convey)
```

**If user needs ideas:** Check if `content/post-ideas.md` exists and suggest 3-5 relevant ideas.

---

## Step 2: Context (Optional)

Ask:
```
Any images to reference? (paste a path, or skip)
```

---

## Step 3: Check Day & Load Context

**First, check what day it is** using `date`.

**Then read the content calendar:**
```
content/content-calendar.md
```

**Apply the day's format:**

| Day | Theme | Key Format |
|-----|-------|------------|
| Monday | Week Ahead | Short punchy list, 3-5 bullets, energetic |
| Wednesday | Hot Take | Single strong opinion with reasoning |
| Friday | Field Notes | Numbered observations, casual, reflective |
| Saturday | Long-form | Lighter blog post, thesis/analysis |
| Other days | Flexible | Use content from ideas bank or user direction |

**If user specifies a different format:** Override the calendar.

**Then read style guide and ICP:**
```
content/linkedin-style.md
content/icp.md
```

**From style guide, extract:**
- Voice & tone preferences
- Format preferences (hook style, length, emoji, hashtags)
- Example posts
- Learned preferences from past choices

**From ICP, apply:**
- Target audience characteristics
- Messaging principles
- Content themes to align with

---

## Step 4: Generate Variations

**If day-specific format applies (Monday/Wednesday/Friday/Saturday):**
Generate 2-3 variations within that format.

**If flexible day or override requested:**
Create 3 polished versions with different approaches:

### Option A: Concise & Punchy
- Short, direct
- One clear message
- Strong hook
- Under 500 characters if possible

### Option B: Story-Driven
- Opens with a scene or moment
- Builds to insight
- Personal angle
- Medium length (500-1000 characters)

### Option C: Educational/Insight-Focused
- Leads with the lesson or takeaway
- Provides context/evidence
- Ends with action or question
- Can be longer if content warrants

**Apply from style guide:**
- Match hook style preference
- Apply emoji and hashtag preferences
- Mirror sentence rhythm from examples
- Reference example posts for format

---

## Step 5: Present & Refine

Display all 3 options clearly:

```markdown
## Option A: Concise & Punchy

[Post content]

---

## Option B: Story-Driven

[Post content]

---

## Option C: Educational/Insight-Focused

[Post content]
```

Then ask:
```
Which do you prefer?
- A, B, or C as-is
- Combine elements (e.g., "A's hook with B's ending")
- Specific feedback for refinement
```

**If refinement requested:** Create a final hybrid version based on feedback.

---

## Step 6: Final Output

Present the chosen/refined post in a clean format:

```markdown
## Final Post

[Post content]

---
Character count: X
```

Add:
- Ready to copy/paste to LinkedIn
- If image was referenced, remind which photo to attach

---

## Step 7: Log Preference (Learning)

After user selects a variation, update `content/linkedin-style.md`:

1. Add a row to the **Learned Preferences > Variation Style Preferences** table:
   - Date
   - Topic (brief)
   - Chosen style (A/B/C + label)
   - Notes (what they liked about it)

2. Update **Patterns Emerging** section if a clear pattern is forming

This builds a learning loop so future posts better match your voice.

---

## Checklist

- [ ] Got draft or idea from user
- [ ] Offered image context option
- [ ] Read style guide (or noted it's empty)
- [ ] Generated 3 distinct variations
- [ ] Presented options for selection
- [ ] Delivered final polished post
- [ ] Logged choice to style guide (learning loop)
