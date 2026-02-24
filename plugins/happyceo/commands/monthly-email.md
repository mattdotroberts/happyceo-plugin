---
description: Compose and send the monthly customer email roundup
---

# Monthly Email Workflow

When this skill is invoked, follow these steps to compose the monthly customer email.

## Step 1: Gather Automated Content

**If website repo is configured in CLAUDE.md:**
Collect recent content from the website repo:

1. **Recent Blog Posts** - Check `[Website Repo Path from CLAUDE.md]/src/content/blog/` for posts from the last 30 days
2. **New Use Cases** - Check for recent use case additions
3. **Service Updates** - Note any changes to services

Extract for each item: Title, Brief description, URL path, Image path

**If website repo is not configured:** Skip automated content gathering and rely on manual input.

## Step 2: Gather Content for Three Sections

Use AskUserQuestion to collect information for each section:

### Section 1: What We're Shipping
```
AskUserQuestion:
- question: "What shipped or is close to shipping this month?"
- options: [Product updates, Client projects completed, New tools/resources, I'll describe]
```

### Section 2: What We're Doing
```
AskUserQuestion:
- question: "What events/workshops are coming up?"
- options: [Pull from calendar, I'll list them, Nothing scheduled]
```

### Section 3: What We're Exploring
```
AskUserQuestion:
- question: "What have you been exploring/learning this month?"
- options: [AI tools or techniques, Business insights, I'll share some thoughts, Skip this section]
```

## Step 3: Get Customer List

**If Subscribers database is configured in CLAUDE.md:**
Query Notion Subscribers database using the Subscribers data source URL.

**If not configured:**
Ask the user: "How many subscribers should I prepare this for? And do you have the list ready in your email service?"

## Step 4: Compose the Email

**Read your ICP** (`content/icp.md`) for messaging alignment.

Use templates:
- `templates/monthly-roundup.md` for structure
- `templates/email-html.html` for formatting

### Email Format
Create a beautiful HTML email with:
- Logo header
- Styled sections with accent color
- Event cards with cover images
- Content cards with left border accent
- CTA button
- Proper footer with unsubscribe link

### Structure:
1. **Opening** - Warm greeting
2. **What We're Shipping** - Products/projects
3. **What We're Doing** - Events/workshops
4. **What We're Exploring** - Learnings/experiments
5. **CTA** - Primary action
6. **Sign-off** - Personal close from [Your Name from CLAUDE.md]

Keep it:
- Under 500 words
- Scannable with visual hierarchy
- Value-focused
- Mobile-friendly (max-width: 600px)

## Step 5: Present Draft for Review

Show the complete email draft with:
- Subject line options (2-3 variations)
- Preview text suggestion
- The full email body

Ask: "Here's the draft. What would you like to change?"

## Step 6: Finalize and Send

**If Resend is configured in CLAUDE.md (.env has RESEND_API_KEY):**
- Make requested edits
- Confirm final version
- Offer test send to user first
- Send via Resend API:

```bash
source .env && curl -X POST 'https://api.resend.com/emails' \
  -H "Authorization: Bearer $RESEND_API_KEY" \
  -H 'Content-Type: application/json' \
  -d '{
    "from": "[From Name from CLAUDE.md] <[From Email from CLAUDE.md]>",
    "to": ["recipient@email.com"],
    "subject": "Subject line here",
    "html": "<html>...</html>"
  }'
```

**If Resend is NOT configured:**
- Provide the final HTML formatted for easy paste
- Suggest: "You can copy this into your email service to send"

## Step 7: Log the Send

After sending (or preparing to send):
- Note the date and subject line

---

## Checklist Before Sending

- [ ] Subject line is compelling and under 50 characters
- [ ] Preview text adds context
- [ ] All links are correct
- [ ] Tone matches company voice
- [ ] CTA is clear
- [ ] User has approved final version