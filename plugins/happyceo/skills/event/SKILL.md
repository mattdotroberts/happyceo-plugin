---
name: event
description: Generate event content — Luma descriptions, LinkedIn promotions, day-before reminders, post-event recaps, and subscriber email announcements. Trigger with "create event content", "event promo", "event recap", "luma description", or "promote [event name]".
---


# Event Workflow

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


When this skill is invoked, generate event-related content for your events (workshops, meetups, hackathons).

## Usage

- `/happyceo:event luma "Workshop Title"` - Generate Luma event description
- `/happyceo:event promote "Event Name"` - Draft LinkedIn announcement post
- `/happyceo:event remind "Event Name"` - Draft reminder post (1 day before)
- `/happyceo:event recap "Event Name"` - Draft post-event summary/thank you
- `/happyceo:event email "Event Name"` - Draft email to subscribers about event

---

## Step 1: Parse Command

**Extract:**
1. **Action:** luma, promote, remind, recap, or email
2. **Event name:** The quoted event identifier

**If no action specified:** Ask which action is needed using AskUserQuestion.

**If no event name:** Ask for the event name.

---

## Step 2: Gather Event Details

**Ask for or fetch:**
- Event title (full name)
- Date and time
- Duration
- Location (online/in-person)
- Speaker/host name(s) and brief bio
- Key outcomes/what attendees will learn
- Target audience
- Price (free or paid)
- Registration link

---

## Step 3: Execute Action

### Action: `luma`

Generate a Luma event description following this format:

**Luma Style Guide:**
- Conversational, approachable tone
- "What to expect" bullet list (4-5 items)
- Bold text for key phrases using `**text**`
- Humanize the hosts (brief credibility without bragging)
- Hyperlinks to host profiles where relevant
- No emojis
- Focus on practical outcomes
- End with "Hosted by [Company Name from CLAUDE.md]" line

**Template Structure:**
```
[Opening line - who this is for and what they'll do]

**What to expect:**
- [Outcome 1]
- [Outcome 2]
- [Outcome 3]
- [Outcome 4]

[Paragraph about the speaker/host with credibility]

[Who should attend / why it matters]

Hosted by [Company Name]. [Brief description].
```

---

### Action: `promote`

Generate LinkedIn announcement post. Check the content calendar first:
```
content/content-calendar.md
```

**Apply day's format if applicable, otherwise use:**

**Promotion Post Structure:**
- Hook: What problem does this event solve?
- Event details: Date, time, what you'll learn
- Speaker credibility (1-2 lines)
- Clear CTA with registration link
- Keep under 1000 characters

**Read style guide:**
```
content/linkedin-style.md
```

Generate 2-3 variations and present for selection.

---

### Action: `remind`

Generate reminder post for 1-2 days before event.

**Reminder Post Structure:**
- Urgency hook: "Tomorrow" or "In 2 days"
- Quick recap of what attendees will get
- Registration link
- Shorter than promotion (under 500 characters)

---

### Action: `recap`

Generate post-event thank you / summary.

**Ask for:**
- How many attendees?
- Key moment or highlight?
- Any photos to reference?

**Recap Post Structure:**
- Thank attendees
- Share 1-2 key takeaways from the event
- Tease next event if applicable
- Tag speakers/co-hosts

---

### Action: `email`

Generate email to subscribers about the event.

**Read email template:**
```
templates/monthly-roundup.md
```

**Event Email Structure:**
- Subject line (compelling, under 60 chars)
- Brief intro (1-2 sentences)
- Event details box (title, date, time, duration)
- What you'll learn (3-4 bullets)
- Speaker bio
- CTA button: Register Now
- Reminder of who this is for

**If Subscribers database is configured in CLAUDE.md:**
Query subscribers for send using `mcp__notion__notion-search` with the Subscribers data source URL.

**If Resend is configured:** Offer to send via Resend after confirmation.

---

## Step 4: Present Output

**For luma:** Present the description ready to copy into Luma event page.

**For promote/remind/recap:** Present 2-3 variations with character counts, then ask for selection per `/happyceo:draft-post` workflow.

**For email:** Present full email with HTML formatting, offer to send if Resend is configured.

---

## Step 5: Log (Optional)

If user selects a variation for LinkedIn posts, log to style guide per `/happyceo:draft-post` learning loop.

---

## Checklist

- [ ] Parsed action and event name
- [ ] Gathered event details
- [ ] Generated content for requested action
- [ ] Applied appropriate format/style
- [ ] Presented output (with variations for LinkedIn posts)
- [ ] Offered to log preference (for LinkedIn posts)