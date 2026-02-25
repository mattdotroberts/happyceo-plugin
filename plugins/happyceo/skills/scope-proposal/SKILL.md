---
name: scope-proposal
description: Scope work and produce a shareable client proposal document. Interactive process: context gathering, outline review, full document generation. Trigger with "write a proposal for [client]", "scope proposal", "client proposal", "quote for [company]", or "proposal for [project]".
---


# Scope Proposal Skill

> If you see unfamiliar placeholders or need to check which tools are connected, see [CONNECTORS.md](../../CONNECTORS.md).

## Connectors

| Connector | What It Adds |
|-----------|-------------|
| **~~knowledge base** | Task management, CRM records, meeting notes, social content queue |

> No connectors? No problem. Tell me what you need and I'll work with whatever you provide.


Produces a professional, modular client proposal document from post-meeting notes. Combines your company story (credibility, case studies) with client-specific scope and pricing.

## MANDATORY ACTIONS

This skill is **interactive and staged**. You MUST:
1. **Read context** - Load PERSONA.md, ICP, and meeting notes
2. **Check CRM** - Look up client in Notion CRM (if configured)
3. **Ask clarifying questions** - Understand client needs and document scope
4. **Generate outline** - Present section outline for review before writing
5. **Generate full document** - Section by section with approval
6. **Save to proposals/** - Output final document as markdown
7. **Post to Slack** - Summary (if Slack configured)

## Usage

- `/happyceo:scope-proposal` — Interactive mode, asks for client context
- `/happyceo:scope-proposal ClientName` — Generate proposal for specific client
- `/happyceo:scope-proposal [paste meeting notes]` — Feed in notes directly

---

## Step 1: Load Context

**Always read these files:**
```
PERSONA.md
content/icp.md
templates/proposal.md
templates/case-studies.md
```

**If CRM database is configured in CLAUDE.md:** Search for client.
**If Meetings database is configured:** Search for recent meetings with client.

**Display what you found.**

---

## Step 2: Gather Requirements

If meeting notes were provided, parse them first. Then ask clarifying questions.

**2a. What does the client need?**
```
AskUserQuestion:
- question: "What's the client's primary need?"
- multiSelect: true
- options: [Workshop/Training, Tool Build, UX/Design Updates, Ongoing Partnership, Audit/Discovery]
```

**2b. Document scope**
```
AskUserQuestion:
- question: "Should we include the full company story, or is this for an existing client?"
- options: [Full story (new prospect), Skip intro (existing client), Abbreviated intro]
```

**2c. Budget signal**
```
AskUserQuestion:
- question: "Any budget signal from the client?"
- options: [They gave a number, They said 'ballpark', No budget discussed, Price sensitive]
```

**2d. Case studies — smart ranking**

Read `templates/case-studies.md` for available case studies.

**Phase 1 — Auto-rank.** Using the client's needs, CRM data, and meeting notes, rank the available case studies by relevance.

**Phase 2 — Confirm with user.** Present ranked suggestion and let user approve, reorder, or remove.

**2e. Engagement model preference**
```
AskUserQuestion:
- question: "Which engagement model do you want to lead with?"
- options: [Retainer/Partnership (Recommended), Project-based scoping, Workshop first, Present all options equally]
```

---

## Step 3: Generate Outline

Based on context gathered, produce a section-by-section outline using the structure from `templates/proposal.md`.

**Present to user for approval before proceeding.**

---

## Step 4: Generate Full Document

Once outline is approved, generate the full document section by section.

### Reusable Sections (1-3)
Pull boilerplate from `templates/proposal.md`:
- Section 1: Who We Are
- Section 2: How We've Helped Others (with selected case studies)
- Section 3: How We Work (engagement models and pricing)

### Client-Specific Sections (4-6)
- Section 4: What We'd Do For You (per-item scope and pricing)
- Section 5: Investment Summary (table with ranges)
- Section 6: Next Steps (recommendation, timeline, contact)

**Generate section by section.** After each major section, briefly confirm before continuing.

---

## Step 5: Save & Output

Save markdown document to `proposals/[client-name]-[YYYY-MM-DD].md`.

**Confirm output:**
```markdown
## Proposal Ready

**Markdown:** proposals/[client-name]-[YYYY-MM-DD].md
**Total estimated range:** $X,XXX - $X,XXX
```

---

## Step 6: Post to Slack

**If Slack is configured (.env has SLACK_BOT_TOKEN and SLACK_CHANNEL_ID):**

```bash
source .env && curl -X POST 'https://slack.com/api/chat.postMessage' \
  -H "Authorization: Bearer $SLACK_BOT_TOKEN" \
  -H 'Content-Type: application/json' \
  -d '{
    "channel": "'"$SLACK_CHANNEL_ID"'",
    "text": "*Proposal Generated:* [Client Name]\n\n*Scope:* [Brief summary]\n*Investment Range:* [Range]\n*Recommended:* [Engagement model]\n*File:* proposals/[filename].md"
  }'
```

**If Slack is not configured:** Skip silently.

---

## Pricing Reference

Configure your pricing in `templates/proposal.md` Section 3. The setup wizard pre-populates this, but you can update it anytime.

---

## Case Study Relevance

Case studies are loaded from `templates/case-studies.md`. Add your case studies there with tags so the auto-ranking can match them to client needs.

**Default ranking bias:** Case studies tagged with your ICP's industry rank higher by default.

---

## Checklist

- [ ] Context loaded (PERSONA, ICP, CRM, meetings)
- [ ] Clarifying questions asked
- [ ] Case studies ranked and confirmed
- [ ] Outline generated and approved
- [ ] Full document generated section by section
- [ ] Markdown document saved to proposals/
- [ ] Slack summary posted (if configured)