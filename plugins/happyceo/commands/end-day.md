---
description: Daily wrap-up and tomorrow prep
---

# End Day Workflow

When this skill is invoked, help close out the day and set up for tomorrow.

## MANDATORY ACTIONS
This skill is **interactive**. You MUST:
1. **Ask questions** using AskUserQuestion at each step
2. **Take actions** based on responses (create tasks, update CRM, send emails)
3. **Run full /happyceo:meeting-wrap** for each of today's meetings
4. **Run full /happyceo:inbox** triage to process emails (if Gmail configured)
5. **Post to Slack** - Summary (if Slack configured)

Do NOT just present a summary — engage with questions and act on answers.

## Step 1: Log Today's Tasks

```
AskUserQuestion:
- question: "What tasks did you work on today?"
- options: [Show my active tasks, I'll type them out, Nothing significant]
```

**If "Show my active tasks":** Query Tasks database (if configured) for In Progress/To Do tasks.

**For each task completed:** Ask hours, update status to "Done" and log hours in Notion.

**Priority Alignment Check:**
After listing completed tasks, read `content/weekly-priorities.md` (if exists) and check alignment.

## Step 2: Capture Quick Wins & Blockers

```
AskUserQuestion:
- question: "How would you rate today's productivity?"
- options: [Great - crushed it, Good - solid progress, Meh - some blockers, Rough - lots of friction]
```

**If "Meh" or "Rough":** Ask what got in the way and offer to create follow-up tasks.

```
AskUserQuestion:
- question: "Any wins worth celebrating? (even small ones)"
- options: [Yes - let me share, Nothing specific, Skip]
```

## Step 2b: Weekly Priority Progress

Read `content/weekly-priorities.md` if it exists.

### On Tuesday-Thursday:
Ask if today's work moved the needle on weekly priorities.

### On Friday:
Show each priority for reflection and archive to Previous Weeks section.

## Step 2c: Process Inbox Notes

**Read `data/inbox.md`.**

**If inbox has items:** Process each item — ask keep/discard, categorize, archive to `data/archive.md`.

After processing: Clear inbox to empty template.

## Step 3: Meeting Wrap-ups

If Meetings database is configured: Query today's meetings.

**For each meeting that doesn't have a `## Post-Meeting Summary` section:**

```
AskUserQuestion:
- question: "Ready to wrap up your meeting with [Person/Company]?"
- options: [Yes - full wrap-up, Skip this one, No meetings to wrap]
```

**If "Yes":** Run the **full `/happyceo:meeting-wrap` workflow**.

## Step 4: Full Inbox Triage

If Gmail is configured:

```
AskUserQuestion:
- question: "Ready to process your inbox?"
- options: [Yes - full triage, Skip inbox today]
```

**If "Yes":** Execute the complete `/happyceo:inbox` skill workflow.

## Step 5: Tomorrow Preview

```
AskUserQuestion:
- question: "What's your biggest priority for tomorrow?"
- options: [A specific meeting, A project/task, Sales/pipeline, Content/marketing, I'll decide in the morning]
```

```
AskUserQuestion:
- question: "Anything you want me to prep for tomorrow?"
- options: [Pull context for a meeting, Create a task list, Draft something, Nothing needed]
```

## Step 6: Pipeline & CRM Update

If CRM database is configured:

```
AskUserQuestion:
- question: "Any pipeline updates from today?"
- options: [Sent a proposal, Had a sales call, Deal closed, Lead went cold, No updates]
```

Take actions based on response (update CRM Status, Last date, Budget, etc.)

## Step 7: Optional LinkedIn Post

```
Anything interesting from today worth sharing on LinkedIn? (Optional)
```

If yes, draft a quick post per `/happyceo:draft-post` logic.

## Step 8: Post Daily Summary to Slack

**If Slack is configured (.env has SLACK_BOT_TOKEN and SLACK_CHANNEL_ID):**

Post comprehensive wrap-up summary with:
- Wins
- Tasks completed with hours
- Pipeline activity
- Weekly priorities progress
- Tomorrow's focus
- Follow-ups sent/drafted

```bash
source .env && curl -X POST 'https://slack.com/api/chat.postMessage' \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "channel": "'"$SLACK_CHANNEL_ID"'",
    "text": "[Comprehensive daily wrap-up summary]"
  }'
```

**If Slack is not configured:** Skip silently.

## Step 9: Generate Summary

Present end-of-day summary:

```markdown
# Day Complete

**Date:** [Today's date]

---

## Wins Today
- [Accomplishment 1]
- [Accomplishment 2]

---

## Follow-ups Sent
- [ ] [Email to Person 1] - [status]

---

## Tomorrow's Setup
**Priorities:**
1. [Priority 1]
2. [Priority 2]

---

## Pipeline Notes
- [Any updates made or needed]
```

---

## Checklist

- [ ] Tasks logged with hours
- [ ] Priority alignment noted
- [ ] Productivity check-in completed
- [ ] Wins/blockers captured
- [ ] Weekly priority progress checked
- [ ] Inbox notes processed
- [ ] Each meeting wrapped via /happyceo:meeting-wrap
- [ ] Full inbox triage completed (if Gmail configured)
- [ ] Tomorrow's priority identified
- [ ] CRM/pipeline updated
- [ ] Slack summary posted (if configured)
- [ ] LinkedIn post drafted (optional)