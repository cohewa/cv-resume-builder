---
name: cv-resume-builder
description: Create, tailor, review, and ATS-check evidence-based CVs and resumes for product designers and adjacent product roles. Use when a user asks to build a master CV, adapt a CV to a job description, improve recruiter impact, express achievements with metrics, resolve NDA-sensitive claims, or edit an existing DOCX, PDF, or Google Doc while preserving its layout.
---

# CV Resume Builder

Build concise, truthful, results-first CVs that a recruiter can scan quickly and an ATS can parse reliably. Treat the user's evidence, approvals, and existing document structure as authoritative; never invent achievements, metrics, work authorization, clients, tools, or credentials.

## Operating rules

- Keep the candidate's primary target role explicit (for example, `Product Designer`). Do not relabel someone as `Founding Designer`, `Lead`, or `Senior` unless the evidence supports that title or the user approves positioning language.
- Use only relevant experience from roughly the last 10 years unless older work is directly requested.
- For every employer, add one short company-context line: sector, product type, scale, region, or business model. Verify public scale figures and mark uncertain/NDA data for review.
- Use the XYZ pattern for experience bullets: **result/impact -> action/ownership -> measurement or evidence**. Start with a strong verb when the result cannot naturally come first.
- Separate evidence types: `achieved`, `contributed to`, `team outcome`, `forecast/potential`, and `NDA-sensitive`. Never convert a forecast, team result, or projected opportunity into an achieved personal result.
- Before editing an existing artifact, create a copy. Preserve font sizes, colors, spacing, margins, section order, and one-column layout unless the user explicitly approves a redesign. Change text only when that is the instruction.
- Ask only unresolved, decision-critical questions. If a claim cannot be verified, use a safe placeholder or flag it instead of guessing.
- Do not include photos, logos, graphics, skill bars, tables, columns, headers, footers, or decorative symbols in an ATS version.
- Use the user's current approved CV template as the only visual template. Do not offer or add alternative resume templates unless the user explicitly asks to redesign the layout.

## Workflow

### 0. Use Google Docs as the default CV workspace

- Create every new CV directly in Google Docs unless the user explicitly requests another format.
- Before creating or changing a Google Doc, confirm the intended document/destination when it is not already identified. If Google Docs access or a connected account is unavailable, explain the blocker and offer a local text/DOCX draft only after the user approves the fallback.
- For an existing CV supplied as a Google Doc, DOCX, PDF, or pasted text, read and analyze it before editing. Preserve the approved document's layout when the user asks for text-only changes.
- Before drafting or changing content, provide (or record internally) an ATS review and recruiter-risk review: parsing/format risks, keyword gaps, unclear attribution, unsupported metrics, missing links, chronology issues, work-authorization ambiguity, and other red flags.
- After edits, re-read the Google Doc and verify headings, links, dates, metrics, text order, and that the document remains selectable and ATS-readable. Export a searchable PDF or DOCX only when requested or required by the vacancy.
- If the current approved visual template is not available in context, ask for its Google Docs link or state that the previously approved structure will be used; do not invent a replacement template.

### 1. Reconcile the evidence

Collect the current CV, LinkedIn/profile data, portfolio/project notes, target job description, dates, roles, tools, metrics, and constraints. Build an internal evidence map with source and status; do not persist private evidence in the final CV. Read `references/evidence-and-metrics.md` when metrics, NDA, attribution, or work authorization are involved.

Resolve conflicts before drafting. Keep the strongest verified numbers, but retain contribution wording for team outcomes. For sensitive figures, use a qualitative result, percentage/range approved for external use, or a clearly labeled forecast.

Route the intake before collecting or rewriting content:

- **Existing CV uploaded:** extract it, map it into a structured evidence record, run ATS/recruiter diagnosis, and wait for approval before changing wording.
- **LinkedIn URL:** attempt one direct read. If login or access blocks it, ask for a LinkedIn PDF export or pasted sections; never pretend that an inaccessible profile was read.
- **No CV / build from scratch:** conduct a one-question-at-a-time interview, completing one role or project before moving to the next. Start by clarifying target role, remote/contract/freelance versus employee preference, and any work-authorization or sponsorship constraint that affects positioning.

Use a compact structured record for every role or project: employer/product, role, dates, mission, actions, outcome, metric, attribution, evidence source, confidentiality status, tools, and open questions. Re-display the record before drafting and list every number separately for confirmation.

### 2. Choose positioning

For a master CV, use the broadest truthful role that matches the candidate's target market. For a tailored CV, mirror the vacancy's role title, domain terms, seniority language, and tools only when supported by evidence.

Use this Summary formula:

> `[Role] with [years] across [domains/skills]. [Launched/led outcome summary]. [How the candidate creates value and works].`

Keep it to 3-4 lines. Prefer concrete scope and impact over personality claims. Expand an acronym on first use only when the audience or ATS requires it; common terms such as B2B, B2C, SaaS, UX, and ARPU may remain abbreviated in a compact master CV.

For a conversational build, ask one focused question at a time in this order: target role and availability; contact/links; each experience entry; projects; education and professional development; skills and languages. Read back each completed role and confirm its wording and numbers before continuing.

### 3. Structure experience

Use reverse chronological order and 2-4 bullets per role or product stream. A strong product-design entry usually contains:

1. one-line mission/ownership statement;
2. one or two impact bullets with metrics;
3. one leverage bullet showing research, experimentation, prototyping, AI, or cross-functional ownership when relevant.

Preferred patterns:

```text
Contributed to a [X%] increase in [business metric] by [specific design/product action].
Increased [metric] [X] by [action], moving [product] from [stage] to [stage].
Identified a potential [forecast] opportunity by [action]; label it as potential/forecast.
Cut [cycle/time] to [duration] by independently [action] with [tool/method].
```

Use personal ownership verbs precisely: `originated`, `proposed`, `designed`, `led`, `owned`, `validated`, `partnered`, `contributed to`. Avoid `responsible for`, `helped with`, and vague process lists unless no stronger evidence exists.

Use consistent date format and tense: `MMM YYYY` or `YYYY-MM` throughout; present tense for current roles and past tense for completed roles. Keep experience, education, and projects in reverse chronological order.

### 4. Make it ATS-friendly

Use standard headings: `SUMMARY`, `SKILLS`, `PROFESSIONAL EXPERIENCE`, `PROJECTS`, `EDUCATION`, `PROFESSIONAL DEVELOPMENT`, and `LANGUAGES` when needed. Use searchable text, conventional bullets, direct URLs, and a selectable-text PDF or DOCX. Keep acronyms and their expanded forms when a target job uses both. See `references/ats-and-role-tailoring.md`.

Keep Skills focused and deduplicated. Organize them into a small number of keyword groups such as `Product & Research`, `Tools & Methods`, and `Leadership & Collaboration`. Include a skill in the list only if the experience or portfolio can support it.

### 5. Run the recruiter/red-flag pass

Check for: missing portfolio, unclear work authorization, unexplained date gaps, inflated titles, ambiguous attribution, forecast presented as revenue, unsupported company scale, generic skills, poor English, excessive length, and a mismatch between the Summary and target role. Never hide a material authorization constraint; use a neutral CV line and answer application questions accurately. Do not imply that freelance/1099 work is automatically permitted in a jurisdiction.

For an uploaded or existing CV, return recommendations before making changes when the user has not yet approved edits. Separate findings into ATS, recruiter/readability, evidence/metrics, and content/positioning recommendations. Apply changes only after approval, and keep a copy of the source document.

### 6. Deliver and verify

- For text-only requests, return the proposed copy and a short change log.
- For an existing Google Doc/DOCX/PDF, create a copy first, apply only approved changes in Google Docs when possible, read back the result, and verify that links, headings, lists, and text order are intact.
- Export a selectable PDF and, when useful, DOCX. Check plain-text extraction for contact details, headings, dates, role titles, metrics, acronyms, and URLs. If visual rendering cannot be inspected, state that limitation explicitly.
- Do not submit, publish, email, or upload the CV without explicit user approval.
- Before final delivery, present a short change log and an approval gate covering facts, dates, metrics, attribution, confidentiality, links, and work-authorization wording.

## References

- `references/cv-quality-checklist.md` - final gate for every CV.
- `references/evidence-and-metrics.md` - attribution, NDA, forecast, and metric wording.
- `references/ats-and-role-tailoring.md` - parsing, keywords, layout, and role adaptation.
- `references/cv-templates.md` - compact section and bullet patterns.

## Validation script

Run `scripts/validate_resume.py path/to/extracted_resume.txt` after exporting or drafting plain text. It checks required headings, common placeholder leakage, malformed Skills tokens, and basic contact/metric presence; it does not replace human or visual review.
