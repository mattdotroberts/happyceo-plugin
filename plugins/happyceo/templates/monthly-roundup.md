# Monthly Roundup Email Template

Use this template structure when composing the monthly customer email.

---

## Email Metadata

**Subject Line Format:** `[Month Roundup] [Key Hook]`
- Example: `[January Roundup] New workshops + what we're building`
- Keep under 50 characters
- Lead with value, not brand

**Preview Text:** 60-90 characters that complement (not repeat) the subject
- Example: `Plus: 3 new use cases and our upcoming events`

---

## Email Structure

### Opening (2-3 sentences)

```
Hi {{first_name}},

[Warm opening that feels personal. Reference the time of year, something relevant happening, or a shared experience. Transition to what's in this email.]
```

**Tips:**
- Don't start with "Happy [Month]!" - too generic
- Make it feel like a note from a person, not a newsletter
- One short paragraph max

---

### Section 1: What We're Shipping

```
## What We're Shipping

[Products, tools, or projects that are live or close to live. Tangible things people can use or see.]

{{#each shipping_items}}
**{{name}}** {{status}}
{{description}}
[Check it out →]({{url}})

{{/each}}
```

**AskUserQuestion prompt:**
```
"What shipped or is close to shipping this month?"
- Product updates
- Client projects completed
- New tools/resources
- Nothing significant
```

---

### Section 2: What We're Doing

```
## What We're Doing

[Workshops, events, meetups, and experiences you're hosting or participating in.]

{{#each events}}
**{{name}}** — {{date}}
{{description}}
[Join us →]({{url}})

{{/each}}
```

**AskUserQuestion prompt:**
```
"What events/workshops are coming up?"
- Pull from calendar
- I'll list them
- Nothing scheduled
```

---

### Section 3: What We're Exploring

```
## What We're Exploring

[Learnings, experiments, and interesting things you're digging into. Shows thought leadership and invites conversation.]

{{#each explorations}}
**{{topic}}**
{{insight}}

{{/each}}
```

**Tips:**
- Be specific about what you learned
- Okay to share incomplete thoughts - invites replies
- 2-3 items max

---

### Closing

```
## Let's Chat

[Personal invitation to connect. Could be booking a call, replying to the email, joining an event, etc.]

[Primary CTA button/link]

Cheers,
[Your Name from CLAUDE.md]

P.S. [Optional personal note, behind-the-scenes tidbit, or secondary CTA]
```

---

### Footer

```
---

You're receiving this because you signed up for updates from [Company Name].

[Unsubscribe]({{unsubscribe_url}}) | [Update preferences]({{preferences_url}})

[Company Name]
```

---

## Tone Guide

**Do:**
- Write like you're emailing a smart friend
- Be specific (numbers, names, details)
- Show personality
- Keep paragraphs short (2-3 sentences)

**Don't:**
- Use buzzwords ("synergy", "leverage", "unlock")
- Start with "I hope this email finds you well"
- Include everything - curate ruthlessly
- End with "Best regards" (too formal)

---

## Length Guide

- **Total:** 300-500 words
- **Opening:** 2-3 sentences
- **Each section:** 3-5 sentences or 2-4 bullets
- **Closing:** 2-3 sentences + P.S.

If it takes more than 2 minutes to read, cut something.

---

## Subject Line Formulas

1. `[Month]: [What's shipping] + what's next`
2. `What we shipped in [Month]`
3. `[Product] is live + [Event] coming up`
4. `[Number] things we learned in [Month]`
5. `Building [X], exploring [Y]`
