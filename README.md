# CV Resume Builder

An ATS-friendly, evidence-based CV skill for Product Designers and adjacent product roles.

## What it does

- Builds master and tailored CVs from verified evidence.
- Uses results-first XYZ bullets and preserves metric attribution.
- Tailors Summary, Skills, and experience keywords to a target job description.
- Checks ATS parsing risks, recruiter red flags, NDA-safe wording, forecasts, and work-authorization claims.
- Includes templates, checklists, metric guidance, and a lightweight validation script.

## Install in Codex

Copy this repository into your Codex skills directory as `cv-resume-builder`, then invoke:

```
Use $cv-resume-builder to create or tailor my ATS-ready CV.
```

## Claude

Use the same `SKILL.md` and reference files as project instructions or a Claude skill package.

## Validation

```bash
python3 scripts/validate_resume.py path/to/extracted_resume.txt
```

The validator is a lightweight check and does not replace human, recruiter, or visual review.
