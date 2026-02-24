# Client Proposal Template

Reusable template for `/happyceo:scope-proposal` skill. Sections 1-3 are boilerplate (same across clients). Sections 4-6 are generated per client.

---

## Section 1: Who We Are

### Boilerplate

```markdown
# [Company Name from CLAUDE.md]

**[Your mission/tagline from PERSONA.md]**

[2-3 sentences about your approach and what makes you different. Write this once and reuse.]

**[Your Name] — [Your Role]**
[1-2 sentences about why you started the company and what gap you fill.]
```

### When to skip
- Existing clients who know you well
- Follow-up proposals where intro was already shared

### When to abbreviate
- Clients who've worked with you before but are exploring a new service

---

## Section 2: How We've Helped Others

### Boilerplate

```markdown
## Results Our Clients Report

[1 sentence framing who you work with and what they get.]
```

### Selection logic
- Load case studies from `templates/case-studies.md`
- Always include at least 2 case studies
- Pick the most relevant to the client's industry/needs
- Match by tags: industry, engagement type, company size

---

## Section 3: How We Work

### Boilerplate

```markdown
## How We Work Together

We offer [number] ways to engage, depending on where you are and what you need.

[List your engagement models here — workshops, project-based, retainers, etc.]
```

### Pricing notes
- Define your pricing tiers in this template
- Always steer toward your recommended engagement model
- All prices are ranges — details discussed on call

---

## Section 4: What We'd Do For You

### Template (per item)

```markdown
## What We'd Do For [Client Name]

### [Request Name]

[2-3 sentence plain language description]

**What's included:**
- [Deliverable 1]
- [Deliverable 2]
- [Deliverable 3]

**Not included in this phase:**
- [Exclusion 1]
- [Exclusion 2]

**Estimated investment:** [Price range]
```

### Guidelines
- Use plain language, not technical jargon
- Each item should be understandable without context
- "Not included" section prevents scope creep
- Price ranges: low = optimistic, high = if complexity surfaces

---

## Section 5: Investment Summary

### Template

```markdown
## Investment Summary

| Item | Low Estimate | High Estimate |
|------|-------------|---------------|
| [Item 1] | $X,XXX | $X,XXX |
| [Item 2] | $X,XXX | $X,XXX |
| **Total** | **$X,XXX** | **$X,XXX** |

*Package discount: Save $X vs individual pricing (if applicable)*

### Additional Ongoing Costs

These are separate from project pricing and are the client's responsibility:

- **Infrastructure** (hosting, database): ~$20–100/month depending on usage
- **API costs** (AI models, third-party APIs): Usage-based. Client sets up their own API keys.
```

### Guidelines
- Always show a total row
- Package discount only when 3+ items bundled
- Infrastructure and API costs must always be called out
- Never hide ongoing costs in project pricing

---

## Section 6: Next Steps

### Template

```markdown
## Next Steps

### Our Recommendation
[1-2 sentences on where to start and why]

### What Happens Next
1. **Confirm scope** — We align on which items to proceed with
2. **Kickoff** — [Timeline] to get started
3. **First deliverable** — [What they'll see first and when]

### Timeline
[Estimated timeline for recommended option]

### Let's Talk
**[Your Name from CLAUDE.md]**
[your email]
[your booking link]
```

---

## Tone Guide (Proposals)

**Do:**
- Write like you're explaining to a smart peer, not pitching to a committee
- Be specific with numbers and deliverables
- Use "we" and "you" — it's a conversation
- Lead with outcomes, not features
- Keep sentences short

**Don't:**
- Use buzzwords ("leverage", "synergy", "holistic")
- Overpromise — ranges exist for a reason
- Get too technical — they don't care how it's built
- Write more than 2 pages per section — they won't read it
- Include disclaimers or legal language (that's for contracts)
