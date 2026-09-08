# Evaluation: Figma — Software Engineer, Full Stack

**Date:** 2026-06-07
**URL:** https://job-boards.greenhouse.io/figma/jobs/5691911004
**Archetype:** Full-Stack Engineer (React/TypeScript + Backend)
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/082-harry-nguyen-resume.pdf (regenerated 2026-09-17; see re-verification note below)

---

## Re-verification (2026-07-20)

Same posting resurfaced via jobright (`token=5691911004` on a Greenhouse `embed/job_app` link matches this report's job ID exactly) — re-checked via Playwright before Harry acts on it, ~6.5 weeks after the original evaluation.

- **Posting confirmed live and unchanged in substance.** Title, JD body, and the `$153,000 - $376,000 USD` base range are identical to the original evaluation. The team list grew slightly — the current posting adds **Figma Buzz** and **Frontend Platform** to the original Editor/FigJam/Slides/Sites/Growth/Internal Tools/Foundations list — more placement breadth, not a material change to fit or score.
- **Score unchanged at 3.8/5.** No new gaps or new strengths found; the original Block A-G analysis (Internal Tools/Foundations positioning, C++/WASM gap only relevant to the Editor team, F-1/H-1B strong-sponsor read) still holds.
- **CV regenerated** with the now-fixed LaTeX template (one-line header, working `**bold**` emphasis via the fixed `escapeLatexWithBold` pipeline, corrected `mailto:` link): `output/082-figma-software-engineer-full-stack-harry-nguyen-2026-07-20.pdf`, 1 page, verified via `pdfinfo`. Bullet order follows the original Customization Plan (Section E): TypeScript/React Chrome bullet leads, TiMoto infra/observability ownership bullets lead the TiMoto block, Skills reordered to Frameworks & Databases first.
- **Recommendation unchanged: Apply**, targeting Internal Tools or Foundations in the application's team-interest question.

---

## Re-verification (2026-09-17)

Same URL pasted a third time (job ID `5691911004` on a fresh `gh_jid`/`gh_src`-tagged link), stripped token confirms identical posting. Re-navigated via Playwright: still live, same title ("Software Engineer - Full Stack"), same `$153,000 - $376,000 USD` base range, same team list (Editor, FigJam, Slides, Sites, Buzz, Growth & Monetization, Internal Tools, Frontend Platform, Foundations — matching the 2026-07-20 re-verification's expanded list). No new report or tracker row created; score, CV, and all findings above stand unchanged.

The actual application form was reached this time (not just the overview page), confirming the exact field text of the "Why do you want to join Figma?" question (max 3-4 sentences) already drafted for Harry in this session, plus several other structured questions worth flagging for when he fills the form: "Have you ever worked for Figma before, as an employee or a contractor/consultant?", "Which of the following best describes your primary technical expertise?" (per Section C, answer "Full-stack / backend"), "Our Full Stack Engineer role can lead to opportunities on a variety of teams... select a maximum of 2 areas" (per Section C's strategy, select Internal Tools and Foundations, not Editor), and "Which programming languages do you regularly use in a professional setting?" (Python, TypeScript, C++, Go per cv.md).

**CV regenerated (2026-09-17)** at Harry's request, rebuilt fresh from the current canonical `cv.md`. This surfaced a factual correction worth recording: the original Customization Plan (Section E, #1) and the "Sell Chrome at scale as frontend proof" quote in Section C describe the Google Chrome internship as having shipped "React/TypeScript... to 3 billion Chrome users." The current `cv.md`'s Chrome bullets are, and as far as can be determined always were in this evaluation's own scope, entirely C++ (privacy-sandbox-internals C++ interface, C++ Mojo IPC, a self-implemented lock-free concurrent trie, and a 25K+ line refactor) — no TypeScript or React appears anywhere in the Chrome block. The genuine React/TypeScript full-stack proof point on `cv.md` is **NextStep** (Founder), not Chrome. This regeneration does not repeat the earlier framing; the new CV keeps Chrome's bullets honestly C++-only (leading with the 25K+ line refactor and lock-free trie, both strong "reliability/scalability" proof for this JD) and relies on NextStep for the frontend/full-stack story. No new facts or metrics were added, only reordering, and the Skills section now leads with Frameworks & Databases and Languages (React, TypeScript, Python, Go, C++ all surfaced early) to match this JD's explicit stack list. Verified 1 page, passed the 4-check anti-AI-signs gate. New file: `output/082-harry-nguyen-resume.pdf` (current naming convention; the 2026-06-07 and 2026-07-20 dated files are left in place as history).

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Full-Stack Engineer — product features + platform infrastructure |
| Domain | Design collaboration / creative tooling (Figma Editor, FigJam, Slides, Sites, Growth, Internal Tools, Foundations) |
| Function | Build — full-stack features, platform infrastructure, real-time collaboration systems |
| Seniority | All levels (varying seniority; team placement after process) |
| Remote | SF or NYC hubs + fully remote US |
| Comp | $153,000–$376,000 base (SF/NY); remote 80–100% of range; equity + annual bonus |
| TL;DR | Figma's evergreen full-stack SWE posting across all product teams. Chrome TypeScript/React at 3B scale is the direct proof for the frontend requirement; TiMoto backend depth + vLLM/ML infra sets Harry apart on AI-forward teams (Internal Tools, Foundations). Strong H-1B sponsor. Main risk: Harry's primary pitch is backend/systems, Figma is a product company where passion for design tooling matters — frame around Internal Tools or Foundations teams, not Editor/C++/WASM. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| Shipping full-stack production apps | TiMoto: primary engineer backend+infra+ML; Chrome: TypeScript/React shipped to 3B+ users | ✅ Strong |
| React / TypeScript (required) | Chrome: observer pattern, 25K+ lines Chromium, 68% delivery accel, 95% test coverage | ✅ Direct |
| Backend: Python, Go, C++, PostgreSQL (required) | TiMoto: Python/Django/FastAPI; Chrome: C++ IPC/Protobuf; Pulumi: Go; Develop for Good: PostgreSQL | ✅ All covered |
| End-to-end project ownership | TiMoto: owned 0→1 architecture, infra, ML serving on 3-person team | ✅ |
| Reliability, scalability, observability | TiMoto: 99.9% uptime, circuit breakers, CloudWatch, multi-AZ; Chrome: zero production regressions | ✅ |
| Cross-functional collaboration | Chrome: design docs with Chrome infra team, senior code review; TiMoto: full-stack ownership | ✅ |
| AI dev tools (Copilot, Claude, ChatGPT) | Uses Claude Code daily; TiMoto uses LLM APIs (Claude, GPT) | ✅ |
| C++ / WebAssembly | Chrome: C++ IPC Protobuf; WASM not in CV — Figma Editor is C++/WASM compiled to browser | ⚠️ Partial |
| Growth engineering / billing / payments | No explicit payments (no CoderPush in current CV); growth eng not in CV | ❌ Gap |
| Stripe / Salesforce / Snowflake / SCIM / SAML | Not in CV | ❌ Bonus gaps |
| 0→1 product launches | TiMoto: built AI product from scratch; Pulumi upstream contributions | ✅ |
| Work auth (F-1) | F-1 — Figma H-1B confirmed strong sponsor; form asks authorization status | ✅ Positive |

**Gaps:**
1. **C++/WebAssembly** — Figma's core rendering engine is C++ compiled to WASM. Harry has Chrome C++ but no WASM. Only affects Editor/rendering team placement, not Internal Tools or Foundations teams.
2. **Primary identity is backend/systems, not product frontend** — The form asks "Which of the following best describes your primary technical expertise?" Harry should answer "Full-stack / backend" and emphasize Chrome React/TS as production-grade frontend experience.
3. **Billing/payments and growth engineering** — Nice-to-haves in JD; not in CV; doesn't block application.
4. **Figma-specific product passion framing** — Figma values engineers excited about design tools. Harry should frame around how he uses Figma + what Figma team (Internal Tools, Foundations) best fits his systems/AI profile.

---

## C) Level and Strategy

**Level detected:** All levels. At Harry's experience (~9 months TiMoto + Google Chrome + Develop for Good), he enters as L3 (junior SWE) or early L4. The form explicitly asks "How many years of professional experience (excluding internships)?" — Harry answers with TiMoto (~9 months, <1 year) but can frame the Chrome internship as production-level evidence.

**Target team positioning:** Internal Tools or Foundations — Harry's distributed systems + AI/LLM serving background fits internal tooling (automation, data pipelines, AI workflows) and cross-product platform infrastructure. Avoid positioning for Editor team unless asked (C++/WASM gap).

**Sell Chrome at scale as frontend proof:**
> "I shipped React/TypeScript to 3 billion Chrome users — observer-pattern state management across 25,000 lines of Chromium with 95% test coverage and 68% feature delivery acceleration. That's production frontend engineering at a bar most new grads don't reach."

**Sell TiMoto ownership as full-stack depth:**
> "At TiMoto I own the backend, infrastructure, and ML serving layer — not separate components but as a single production system. I've traced production deadlocks in gRPC, optimized LLM inference memory, and maintained 99.9% uptime on $40-60/month cloud spend. I understand the full stack because I've been responsible for all of it."

**On "why Figma":**
> "I've used Figma for every design handoff at TiMoto. But what I want to build at Figma isn't the rendering engine — I want to work on the platform that makes Figma work at enterprise scale: Internal Tools, Foundations, developer extensibility. The systems problems there are the same class I've been solving."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Figma stated base | $153,000–$376,000 (SF/NY); remote 80–100% of range |
| Figma new grad SWE TC (Levels.fyi est.) | ~$220K–$280K at L3 entry (equity + bonus) |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Base floor ($153K) clears Harry's $140K minimum and hits his target low-end. Equity in a pre-IPO Figma (rejected $20B Adobe acquisition, own terms) is potentially very significant. At L3-L4, total comp including equity vest is materially above base. Strong compensation picture.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Chrome bullet order | C++ IPC leads | Lead with TypeScript/React observer pattern (68% delivery, 25K+ lines, 95% coverage) | Full-stack role; Chrome TS/React is direct proof for front-end requirement |
| 2 | TiMoto bullet order | gRPC/deadlock varies | Lead with "Led backend, cloud infra, ML serving — primary engineer, 3-person team" | Shows end-to-end ownership; Figma wants full-stack product mindset |
| 3 | Skills: Languages | C++ or Go first | TypeScript, Python, Go, C++ first | TypeScript is Figma's primary stack; Python = backend; Go = infra |
| 4 | Skills row order | Distributed Systems leads | Frameworks & Databases leads, then Languages, then Distributed Systems | Full-stack/product role; React/Django/FastAPI/PostgreSQL are the most relevant |
| 5 | TiMoto bullet 3 | vLLM leads | vLLM second; "Led backend... AI product end-to-end" first | Product ownership framing over ML infra framing for Figma context |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Full-stack production at scale | Chrome React/TS + C++ IPC | Chrome needed UI state management + IPC between browser processes | Ship to 3B users without regressions | Observer pattern decoupling state; C++ Protobuf IPC; 95% test coverage | 68% delivery acceleration, sub-50ms p99, zero regressions | Full-stack means owning both sides of the layer boundary — the protocol AND the UI that consumes it |
| 2 | End-to-end ownership | TiMoto 0→1 | Primary engineer on 3-person startup, build AI product from scratch | Ship backend + infra + ML serving end-to-end | gRPC + Django + vLLM + ECS Fargate as cohesive system | 99.9% uptime, 44% cost reduction, sub-50ms p99 | Full ownership means you cannot punt on the hard parts — you debug the stack from browser to GPU |
| 3 | Performance optimization | Chrome lock-free trie | 1,200ms p99 settings navigation; mutex contention in production Chrome | 96% latency reduction without correctness regression | Lock-free concurrent trie; linearizability proof | 96% reduction, zero regressions | Profile before optimizing; measure the contention path, don't guess |
| 4 | Reliability + observability | TiMoto circuit breakers + CloudWatch | Distributed production system; failure modes span gRPC + DB + ML serving | 99.9% uptime with auto-rollback on health check failure | Circuit breaker pattern, CloudWatch alerts, multi-AZ failover, Terraform IaC | 44% cost cut, zero unplanned downtime | Observability is not monitoring — it's the ability to ask new questions about failure you haven't seen yet |
| 5 | Cross-functional collaboration | Chrome design docs + senior review | C++ IPC design needed cross-team alignment with Chrome infrastructure | Ship without breaking existing browser process boundaries | Design doc; Protobuf schema evolution rationale; senior Chrome engineer review | Adopted into production Chromium branch | Design documents are a forcing function for clarity — writing the design surfaces the gaps before code review |

**Recommended case study:** Chrome full-stack — "I designed the IPC transport layer in C++ and the React/TypeScript UI that consumed it on the same feature. I understood both sides of the boundary — the serialization protocol and the state propagation pattern. That's the kind of cross-stack thinking Figma needs on the Foundations team."

**Red-flag questions:**
- *"Backend is your primary identity — why full-stack?"* → "Chrome wasn't just a backend internship — I shipped observer-pattern React/TypeScript to 3B users and the C++ transport layer underneath it on the same feature. I understand how the stack connects because I've owned both ends."
- *"Work authorization?"* → "F-1, OPT from May 2027. Will need H-1B. Figma filed 100+ LCAs in recent years — happy to discuss timing."
- *"Why Figma, not a pure backend company?"* → "I use Figma at TiMoto. The platform problems at Figma — Internal Tools, Foundations, extensibility APIs — are the same distributed systems problems I've been solving, just at larger scale and for an audience of designers and developers who need it to be fast and reliable."
- *"C++/WebAssembly?"* → "C++ yes — I designed an IPC transport layer in C++ for Chrome. WASM is new to me. If I were placed on the Editor team I'd ramp on it, but I'd target Internal Tools or Foundations where my distributed systems + AI infra background lands better."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Greenhouse | Positive |
| Comp disclosed | $153K–$376K explicitly stated with remote modifier disclosure | Positive |
| Company status | Figma — independent design platform, rejected $20B Adobe acquisition, 4M+ users, IPO candidate | Positive |
| H-1B sponsorship | Form asks work authorization; Figma confirmed strong sponsor with 100+ LCA filings | Positive |
| JD specificity | Multiple named product teams, specific tech stack (React/TS, Ruby, Python, Go, C++, PostgreSQL), specific bonus skills (C++/WASM, Stripe, SCIM) | Positive |
| Seniority range | All levels — means Harry at entry/junior level is in scope | Positive |
| Remote option | US remote explicitly available | Positive |
| AI-focused bonus | "AI-assisted development tools" listed as a plus — Figma building AI into product (Figma AI, Dev Mode AI) | Positive |

---

## Keywords extracted

TypeScript, React, Python, Go, Ruby, C++, PostgreSQL, full-stack, production, real-time collaboration, scalability, reliability, design tools, product engineering, Internal Tools, Foundations, Growth, WebAssembly, WASM, developer tooling, extensibility, Stripe, AI-assisted, remote, San Francisco, New York

---

## Machine Summary

```yaml
company: Figma
role: Software Engineer, Full Stack
date: 2026-06-07
url: https://job-boards.greenhouse.io/figma/jobs/5691911004
score: 3.8
archetype: Full-Stack Engineer (React/TypeScript + Backend)
location: San Francisco, CA / New York, NY / Remote US
comp_range: "$153,000–$376,000 base (SF/NY); remote 80-100%; equity + bonus"
visa_risk: "F-1 — H-1B strong positive (Figma 100+ LCA filings; form asks work auth)"
legitimacy: High Confidence
recommendation: "Apply — Chrome React/TS 3B users + TiMoto backend ownership = genuine full-stack proof; target Internal Tools/Foundations team; $153K+ clears minimum; H-1B confirmed"
```

## Addendum 2026-10-03: link pasted again (fifth time), full CV rewrite

**Duplicate:** Same Greenhouse job `5691911004` (requisition 1918; the `jr_id` parameter is a tracking tag). No new report and no new tracker row.

**Check this first:** the tracker row for #82 says **Applied**, but this report's own re-verification notes (2026-07-20 and 2026-09-17) read as if you had not applied yet ("before Harry acts on it"), and the status ledger has no entry for it. If you did submit to Figma, the row is right and re-applying adds nothing. If you did not, the row is wrong and should go back to Evaluated; tell me which and I will fix it. Figma's posting does not say whether it ignores a second application from the same person.

**Liveness:** the Greenhouse board API still returns the posting (title "Software Engineer - Full Stack", first published 2025-11-01, last updated 2026-09-24). Pay is unchanged at $153,000 to $376,000 base (the range spans levels). The text says the opening applies at varying seniority levels across Figma Editor, FigJam, Slides, Sites, Buzz, Growth & Monetization, Internal Tools, Frontend Platform and Foundations, and can be held from a US hub or remotely in the United States. Score stays 3.8/5.

**Form (from the Greenhouse API), with suggestions from cv.md; each answer is yours to confirm:**
- Authorized to work in the country: Yes (F-1 with CPT/OPT). There is no sponsorship question on this form.
- Worked for Figma before: No.
- Years of professional experience excluding internships: 0-2 years.
- Full-time software engineer professionally, excluding internships: your TiMoto role is the basis; earlier reports describe it as full-time. Confirm.
- Built and maintained user-facing web applications professionally: your TiMoto work is the backend of a consumer app; the front end is another person's. Answer as you see it.
- Team areas: Internal Tools / Developer Platforms fits (your agent tool, the Chrome debugging page, CI/CD automation). Frontend Platform does not.
- Primary expertise: Backend, Infrastructure, ML/AI; Full-Stack only if you consider yourself that.
- Languages used professionally: TypeScript, Python, C++ (Chrome internship). Go comes from open source, not a professional role.
- From where do you intend to work: your choice (a US hub or remote).
- Why do you want to join Figma?, Additional Information, pronouns: yours to write or choose.

**Fresh CV:** `output/082-harry-nguyen-resume-2026-10-03.pdf` (1 page), rebuilt from scratch: every Experience bullet and the NextStep lead bullet were rewritten in the JD's vocabulary. A numeric check shows no figure added or lost against the master CV. It supersedes `output/082-harry-nguyen-resume.pdf`. MongoDB was dropped from the Frameworks line to keep one page.

| JD phrase | CV change |
|---|---|
| "shipping and maintaining ... applications in production", "own projects end-to-end" | TiMoto bullet 1: "Owned TiMoto's motorbike-valuation backend end to end, from zero to production ... a WebSocket service that notifies the app in real time when done"; `Full-Stack` added to the Frameworks line (React first) |
| "cross-functional partners in Product, Design, Research, and Data" | "Worked cross-functionally with ops, sales, marketing, product, and the founder" |
| "developer workflows", "developer tooling" | Bullet 3: "Shipped a developer-tooling agent that fixes production bugs"; Google Mojo bullet reads "a debugging tool for 200+ engineers" |
| "reliability, security, and scalability" | `Reliability` and `Observability` added; EKS to multi-AZ ECS Fargate bullet kept |
| "testing, launch, iteration" | Google leads with the test-suite design doc (2 hours to 10 min) |
| "AI-assisted development tools (GitHub Copilot, ChatGPT, Claude)" | AI Dev Tools line leads GitHub Copilot, Claude Code |
| "React/TypeScript ... Python, Go, C++, PostgreSQL" | Languages leads TypeScript, Python, Go, C++; Frameworks leads React, Node.js; PostgreSQL stays |

Not added because cv.md does not support them: WebAssembly, SAML/SCIM, Stripe or Salesforce integrations, billing or payments work, production React/TypeScript (the 2026-09-17 correction in this report stands: the Chrome internship was C++, not React). Gates: 1 page, 0 em dashes, 0 AI-vocabulary hits, 0 contrast frames, 0 stray asterisks.
