---
name: meeting-wrap
description: Post-meeting wrap-up — extract insights, update meeting and CRM records, create follow-up task, and draft follow-up email. Trigger with "just had a call with [name]", "meeting wrap [company]", "post-meeting notes", or "follow up from my meeting".
---


# Meeting Wrap

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |
| **~~email** | Inbox triage, draft replies, send follow-up emails |
| **~~chat** | Post briefings and wrap-ups to your team channel |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


Post-meeting wrap-up skill that extracts insights, creates tasks, drafts elite follow-up email, and sets systematic follow-up cadence.

## MANDATORY ACTIONS

This skill is **interactive**. You MUST:
1. **Find the meeting** - Identify from argument or today's meetings
2. **Gather insights** - Ask clarifying questions about outcomes
3. **Update Meeting record** - Add Post-Meeting Summary section (if Meetings DB configured)
4. **Update CRM record** - Set Last date, update Status if applicable (if CRM configured)
5. **Create tasks** - Action items with smart deadlines (if Tasks DB configured)
6. **Draft follow-up email** - Save as Gmail draft (if Gmail configured)
7. **Post to Slack** - Summary (if Slack configured)

**Graceful degradation:** Skip any step where the required integration is not configured in CLAUDE.md. Note what was skipped.

## Usage

- `/happyceo:meeting-wrap` — Interactive mode (finds today's most recent meeting)
- `/happyceo:meeting-wrap Chris Cockton` — Wrap up meeting with specific person
- Can also be called from `/happyceo:end-day`

---

## Step 1: Identify Meeting

**If person/company provided:** Search for that meeting.

If Meetings database is configured in CLAUDE.md:
```
mcp__notion__notion-search with:
- query: "[person name]"
- data_source_url: [Meetings database ID from CLAUDE.md]
```

**If no argument:**
```
AskUserQuestion:
- question: "Which meeting are we wrapping up?"
- options: [Show my calendar, I'll type the name]
```

---

## Step 2: Check Already Processed

If meeting record found, check if it already has a `## Post-Meeting Summary` section.

If already wrapped:
```
AskUserQuestion:
- question: "This meeting was already wrapped up. What would you like to do?"
- options: [View existing summary, Replace with new wrap-up, Skip this meeting]
```

---

## Step 3: Gather Context & Parse Transcript

Fetch meeting record and linked CRM record (if configured).

**If transcript present in meeting page:**
- Extract mentioned action items
- Identify key topics discussed
- Note any objections or concerns raised
- Pull quotes that reveal needs/pain points

---

## Step 4: Clarifying Questions

Use **AskUserQuestion** for each:

**4a. Overall Outcome**
```
AskUserQuestion:
- question: "How did the meeting go overall?"
- options: [Interested - moving forward, Needs more info, Requested proposal, Not a fit, Unclear outcome]
```

**4b. Key Insights** (only if transcript didn't capture this)
```
AskUserQuestion:
- question: "What were the key insights from this meeting?"
- options: [I'll type them out, Use transcript insights, Nothing notable]
```

**4c. Their Specific Needs**
```
AskUserQuestion:
- question: "What do they need clarity on?"
- multiSelect: true
- options: [Pricing clarity, Product/service clarity, Process clarity, Case studies/proof, Nothing specific]
```

**4d. Your Action Items**
```
AskUserQuestion:
- question: "What are you committing to do?"
- multiSelect: true
- options: [Send proposal/quote, Send information, Schedule next call, Send case study, Custom action]
```

**4e. Their Commitments**
```
AskUserQuestion:
- question: "What did they commit to do?"
- options: [Review materials, Get internal approval, Schedule follow-up, Send requirements, Nothing specific]
```

---

## Step 5: Update Meeting Record

If Meetings database is configured, add `## Post-Meeting Summary` section to meeting page.

**Update Meeting Status -> "Completed"**

---

## Step 6: Update CRM Record

If CRM database is configured:
- Update `Last` date to today
- Update Status if applicable (Requested proposal -> "Proposal", Not a fit -> "Lost")
- Append meeting summary to Notes field

---

## Step 7: Create Follow-up Tasks

If Tasks database is configured, create task for each action item with smart deadline:

| Action Type | Default Deadline |
|-------------|------------------|
| Send proposal/quote | Same day or +1 day |
| Send information | Same day |
| Schedule follow-up call | +2-3 days |
| Check-in if no response | +5-7 days |

Create **1 follow-up task** (a check-in/follow-up call). Do NOT create multi-touch cadence tasks — keep it lightweight.

---

## Step 8: Draft Elite Follow-up Email

If Gmail is configured:

**Email Structure (Elite Sales Techniques):**

1. **Thanks + specific thing they shared** (shows you were listening)
2. **Summary of what THEY said** (not what you pitched)
3. **Address their specific needs** (based on Step 4c)
4. **Value add** - share relevant resource (teach, don't pitch)
5. **Clear next step with specific date** (not "let me know")

**Template:**
```
Subject: Following up on our conversation - [specific topic discussed]

Hi [Name],

Thanks for taking the time to chat today. I especially appreciated hearing about [specific thing they mentioned].

To recap what you shared:
- [Their situation/challenge]
- [Their goal or desired outcome]
- [Any concerns or questions they raised]

As discussed, I'm [action you're taking]. Specifically:
[Address their needs from Step 4c]

I thought you might find [this resource] useful - [brief description of relevance].

How about we [specific next step] on [specific date]? I'll send a calendar invite.

Best,
[Your Name from CLAUDE.md]
```

**Create draft using Gmail MCP:**
```
mcp__gmail__draft_email with:
- to: "[contact email from CRM]"
- subject: "[subject line]"
- body: "[composed email]"
```

---

## Step 9: Present Summary & Post to Slack

**Display completion summary.**

**If Slack is configured in CLAUDE.md (.env has SLACK_BOT_TOKEN and SLACK_CHANNEL_ID):**

Post summary to Slack:
```bash
source .env && curl -X POST 'https://slack.com/api/chat.postMessage' \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "channel": "'"$SLACK_CHANNEL_ID"'",
    "text": "*Meeting Wrapped:* [Contact] ([Company])\n\n*Outcome:* [Outcome]\n*Key insight:* [One-liner insight]\n\n*Actions:*\n- [Task 1]\n\n*Follow-up:* Email drafted"
  }'
```

**If Slack is not configured:** Skip silently.

---

## Elite Sales Techniques Embedded

1. **Same-day follow-up** - Shows responsiveness
2. **Active listening proof** - Summarize what THEY said
3. **Address objections proactively** - Don't wait for them to ask
4. **Teach, don't pitch** - Value-add resources
5. **Specific next step with date** - Not "let me know"
6. **Track their commitments** - Mutual action plan

---

## Checklist

- [ ] Meeting identified or selected
- [ ] Already-processed check passed
- [ ] Context gathered (CRM, transcript if available)
- [ ] Clarifying questions completed
- [ ] Meeting record updated (if configured)
- [ ] CRM updated (if configured)
- [ ] Follow-up task created (if configured)
- [ ] Follow-up email drafted (if Gmail configured)
- [ ] Summary presented
- [ ] Slack posted (if configured)