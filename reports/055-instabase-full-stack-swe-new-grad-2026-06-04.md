# Evaluation: Instabase -- Full-stack Software Engineer (New Grad)

**Date:** 2026-06-04
**URL:** https://job-boards.greenhouse.io/instabase/jobs/8548929002
**Archetype:** Full-Stack Engineer (adjacent) / AI Platform (secondary)
**Score:** 3.2/5
**Legitimacy:** Proceed with Caution
**PDF:** output/055-instabase-full-stack-swe-new-grad-harry-nguyen.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Full-Stack Engineer (adjacent) with AI platform product context |
| Domain | AI document processing / intelligent automation platform |
| Function | Build |
| Seniority | New Grad (preferred May–June 2026 graduation) |
| Remote | Hybrid — San Francisco, CA |
| Team size | Not specified |
| TL;DR | New grad full-stack SWE at an AI document-processing startup building UI components, platform features, and the core product stack (Go, Python, React, TypeScript, Kubernetes). |

**Key requirements extracted:**
- Languages/frameworks: Python, Go, React, REST APIs
- Frontend-first framing: UI dev, reusable components, frontend library evaluation
- Team-wide scope: product + infrastructure engineering tracks
- Graduation: preferred May–June 2026 (Harry graduates May 2027 — **1 year off**)
- Location: San Francisco, CA (onsite/hybrid)

---

## B) Match with CV

### Direct matches

| JD Requirement | CV Evidence |
|----------------|-------------|
| Python, Go | Skills: "Languages: C++, Python, Go, TypeScript…"; TiMoto uses Go/Python stack |
| React, TypeScript | Google: "event-driven TypeScript/React system … 25K+ lines of Chromium"; Skills: "Frameworks & Databases: …React, REST APIs" |
| REST APIs | Develop for Good: "Designed stateless BaaS … JWT over session auth … 500+ concurrent users"; TiMoto: Django/FastAPI REST serving layer |
| Kubernetes / Docker | TiMoto: "Architected multi-AZ ECS Fargate with Terraform IaC…"; Skills: "Cloud & Infrastructure: …Kubernetes, Docker, CI/CD" |
| Collaborate cross-functionally | Google: "Collaborated with Chrome infrastructure team … code reviews"; TiMoto: primary engineer across backend + infra + ML on 3-person team |
| Ship features to prod fast | Google: "shipped to Chrome stable channel serving 3B+ active users"; TiMoto: deployed production systems end-to-end |
| Reusable frontend components | Google: "event-driven TypeScript/React system with observer pattern decoupling UI state propagation — 25K+ lines of Chromium at 95% test coverage" |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|-----------|
| **Preferred graduation May–June 2026** (Harry: May 2027) | Soft blocker — preferred, not required | JD says "preferred," not hard requirement. Apply and address in application: "targeting May 2027 graduation; available for internship bridge or co-op; full availability from May 2027." |
| Pure frontend framing ("developing user interfaces," "evaluating frontend libraries") | Moderate — Harry is backend/systems-first | Lean on Google's Chromium TypeScript/React work (25K+ lines, 95% test coverage, observer-pattern state). Frame as: "Frontend experience in Chrome-scale codebase." |
| No direct experience with Instabase stack (Go for services, Java, C++) | Low | Go is in CV. C++ at Google. Adjacent. |
| "Move fast / make product decisions early" framing (startup pace) | Low | TiMoto: primary engineer, 3-person team, full ownership narrative covers this well. |

---

## C) Level and Strategy

**Level detected:** New Grad. No experience requirement. The JD is explicitly an entry-level role.

**Harry's positioning:** Strong for this level. Google internship + TiMoto primary engineer puts Harry above a typical new grad. The risk is over-qualifying as a pure backend candidate when the JD leans frontend.

**"Sell the right fit" plan:**
- Lead with Google Chrome TypeScript/React work — this is the most direct proof point for frontend development
- Mention TiMoto's full product ownership (backend + infra + ML) to hit the "full-stack" framing
- Do NOT over-pitch distributed systems / gRPC here — it may read as misaligned
- Frame narrative: "I've shipped frontend in a Chromium-scale React codebase and built the backend services it calls — I can contribute across both layers from week one."

**Graduation year risk:** Address proactively in application form. Instabase asks for graduation date. Select the option closest to May 2027 and add a note in the cover letter if allowed.

**"If they push back on graduation year":**
- Ask if there's a 2027 cohort or a co-op/internship bridge option
- Do not misrepresent graduation date

---

## D) Comp and Demand

| Data point | Value | Source |
|------------|-------|--------|
| JD base range | $140,000–$145,455 | Greenhouse JD |
| JD extras | + bonus + equity + US benefits | Greenhouse JD |
| Instabase SWE (all levels) median TC | ~$220K | Levels.fyi |
| Instabase SWE (all levels) Glassdoor range | $175K–$254K | Glassdoor (March 2026) |
| New grad SWE market (SF) | $140K–$175K base typical | Glassdoor/Levels.fyi |

**Assessment:** The base ($140K–$145K) sits exactly at Harry's walk-away minimum of $140K. Total comp with bonus and equity may exceed this, but the base alone does not clear the target. Instabase is a private company — equity upside is illiquid and speculative.

**Comp verdict:** At floor. Acceptable only if equity value + growth trajectory are strong. Negotiate upward if offer comes.

**Demand trend:** Full-stack new grad roles at AI-native companies are moderately competitive. Instabase's specific niche (document AI, enterprise automation) is growing but the company is smaller/less known than Tier 1 targets.

---

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---------|----------------|-----------------|-----|
| 1 | CV Summary (not currently present) | No summary section | Add 2-line professional summary: "CS @ Georgia State (May 2027) · Google Chrome intern (React/TypeScript, 25K+ lines Chromium) · primary engineer for backend + infra at TiMoto AI. Shipped frontend and backend systems to production." | Recruiter skims first 5 seconds |
| 2 | Google bullet order | IPC/C++ bullet is first | Reorder to lead with TypeScript/React bullet ("event-driven system, observer pattern, 25K+ lines, 68% faster delivery") | JD is frontend-first; match the scan order |
| 3 | TiMoto description | "backend, cloud infrastructure, and ML serving" | Add explicit mention: "…full product stack including Django REST APIs and Python service layer" | Signals full-stack capability |
| 4 | Skills section | Backend-heavy framing | Move "Frameworks & Databases: …React, REST APIs" higher in the list or bold React/TypeScript | Frontend skills are buried |
| 5 | Projects | Only Pulumi (IaC-focused) | Consider adding a brief note about any frontend work or leave as-is; Pulumi Go work is relevant for infra track | Instabase hires across product + infra tracks |

**LinkedIn:** Flag TypeScript/React skills, Chromium frontend work. Add Instabase as a followed company.

---

## F) Interview Plan

### STAR+R Stories

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|-----------|
| 1 | Frontend development, reusable components | Google Chrome: TypeScript/React observer pattern system | Chrome UI had tightly coupled state causing cascade bugs | Decouple UI state propagation across 25K+ lines of Chromium | Designed event-driven observer pattern in TypeScript/React | 68% faster feature delivery, 95% test coverage, shipped to stable | Would have proposed this refactor earlier; decoupling is cheaper before features multiply |
| 2 | Move fast, contribute from week 1 | TiMoto: gRPC deadlock fix | Concurrent calls hit shared resource lock in prod; evaluation pipeline failing | Fix under production load, no downtime | Traced call graph, identified acquisition conflict, redesigned sequencing | 100% eval success, sub-50ms p99, zero regressions | Root-cause analysis > hotfix; first instinct was a patch, but tracing the graph found the real cause |
| 3 | Drive features from ideation to production | TiMoto: vLLM + PagedAttention deployment | Existing naive inference OOM'd under concurrent load | Stand up production LLM serving on budget | Evaluated vLLM vs naive, selected PagedAttention for KV efficiency, deployed with continuous batching | Zero OOM failures at production traffic | Explicit "why this tool" narrative matters — PagedAttention choice was a decision, not an accident |
| 4 | Evaluate frontend libraries, iterate on stack | Google Chrome: Protocol Buffers vs. custom serialization | IPC layer needed a serialization choice for cross-language stability | Evaluate and justify the choice | Analyzed schema evolution and cross-language compatibility; chose Protobuf over custom | Shipped to 3B+ users, sub-50ms p99 | Framing a technology choice as a reasoned decision (not "we used X") signals engineering maturity |
| 5 | Collaborate with PMs and designers | Google Chrome: design docs + senior review process | Chrome team required design docs before implementation | Deliver design doc at Chrome bar | Wrote full design doc, iterated with senior Chrome engineers | Adopted into production branch | Senior review felt like overhead at first; it's actually the highest-leverage step for reducing rework |
| 6 | Cloud infrastructure / deployments (infra track) | TiMoto: multi-AZ ECS Fargate + Terraform | Need reliable, cost-efficient infra for small team | 99.9% uptime target on $40–60/month | Terraform IaC, circuit breaker, auto-rollback, CloudWatch observability | 99.9% uptime, 44% cost reduction | Circuit breakers saved us from cascading failures twice; now standard in every service |

**Case study to present:** TiMoto AI end-to-end — backend gRPC + Python serving layer + AWS infra. Show the full product stack. For a full-stack role at an AI-native company, the "I built the backend and deployed it on AWS" story is directly relevant. Demo at https://timoto.ai if walkthrough is requested.

**Red-flag questions:**
- "You prefer backend — will you be happy doing frontend?" → "My Chrome internship gave me a deep React/TypeScript project on a 25K-line codebase. I'm comfortable across the stack and interested in the product layer, especially at an AI-native company where backend and UI are tightly coupled."
- "Your preferred grad date is May 2027, not 2026 — can you still apply?" → "Yes. The JD says preferred, not required. I graduate May 2027 and am available for summer 2026 internship or co-op if there's a bridge program, or for the full-time new grad cohort in 2027."

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button active | Yes — full application form visible and interactive | Positive |
| JD specificity | Names specific stack (Go, Python, Java, React, TypeScript, Docker, Kubernetes); mentions both product and infra tracks | Positive |
| Salary transparency | $140K–$145K base explicitly stated | Positive |
| Preferred grad date | May–June 2026 preferred — this is a 2026 cohort posting; Harry is 2027 | Neutral (applies but risky) |
| Company layoffs | Instabase reported layoffs in October–November 2025 — exact scope unclear; company has not publicly disclosed headcount | Concerning |
| Reposting history | Instabase Full-stack SWE New Grad previously evaluated (#005, 2026-05-27) — same or similar posting; re-appearing 8 days later | Concerning |
| Posting age | No explicit date on page; previously seen May 2026 — could be an ongoing/rolling new grad hire | Neutral |
| Role-company fit | Full-stack SWE at an AI document processing company is coherent | Positive |

**Context notes:**
- The November 2025 layoffs are a real signal to note but do not automatically indicate a ghost posting. Instabase is still active, has VC backing (Greylock, a16z, Index Ventures), and is posting multiple roles. The layoffs may have been in a different function (e.g., go-to-market).
- The re-appearance of this exact same role 8 days after a prior evaluation is the most meaningful signal here — it could mean the role rolled over into a new Greenhouse posting, or the prior cohort closed and a new one opened.
- **Recommendation:** Apply. The form is active. But note the grad year gap and layoff signal to the recruiter early. Do not over-invest (custom cover letter is sufficient; no need for a deep-research deep-dive for this score level).

---

## Keywords extracted

Full-stack, software engineer, new grad, React, TypeScript, Go, Python, Java, REST APIs, Kubernetes, Docker, microservices, frontend, platform, AI, unstructured data, document processing, Instabase, user interface, reusable components, feature delivery, product engineering, infrastructure engineering

---

## Score Summary

| Dimension | Score | Notes |
|-----------|-------|-------|
| Match with CV | 3.5/5 | Strong backend; Google React/TS work covers frontend gap; grad year mismatch |
| North Star alignment | 2.5/5 | Full-stack is adjacent archetype — Harry's primary is backend/systems/ML infra |
| Comp | 3.0/5 | At walk-away floor ($140K base); private equity illiquid; bonus unknown |
| Cultural signals | 3.5/5 | Well-funded, global, people-first framing; layoffs in Nov 2025 cloud picture |
| Red flags | -0.3 | Grad year mismatch (soft); layoff history (moderate); role is adjacent not primary |
| **Global** | **3.2/5** | Apply if interested in full-stack product work at an AI-native company; not a top-priority role |

**Recommendation:** Apply — score is above the 3.0 threshold for CV generation. The graduation year mismatch is the biggest risk; address it proactively. Role is not in Harry's primary archetype (backend/systems) but the Google Chrome React work provides a credible bridge. Comp is at the walk-away floor — worth a conversation but negotiate.
