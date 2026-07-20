# Evaluation: Amazon — Software Development Engineer

**Date:** 2026-07-19
**URL:** https://www.amazon.jobs/en/jobs/10476687/software-development-engineer?jr_id=6a593ae83ac7627fe9ffe19e
**Via:** —
**Archetype:** Backend / Distributed Systems Engineer + Platform / Cloud Infrastructure Engineer
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/179-amazon-harry-nguyen-2026-07-19.pdf

---

## Machine Summary

```yaml
company: "Amazon"
role: "Software Development Engineer"
score: 3.8
legitimacy_tier: "High Confidence"
archetype: "Backend / Distributed Systems Engineer + Platform / Cloud Infrastructure Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "JD asks for '1+ years of non-internship professional software development experience' -- TiMoto (Sep 2025-Present) is ~10 months as of 2026-07, crosses 1 year by Sep 2026"
  - "Onsite Seattle, WA -- requires relocation from Atlanta, GA"
  - "Serverless/Lambda-style AWS experience not directly on CV (TiMoto is ECS Fargate, container-based, not serverless)"
top_strengths:
  - "TiMoto AWS/Terraform/CI-CD automation directly maps to 'own automation of business processes ... using AWS services'"
  - "Backend/Distributed Systems and Platform/Cloud Infrastructure are both primary North Star archetypes"
  - "Advertised base ($143.7K-$194.4K) plus RSU/sign-on lands near the top of Harry's $150-200K target range"
risk_level: "Medium"
confidence: "Medium"
next_action: "Apply via the listed 'Apply now' link; be ready to address the sub-1-year non-internship experience question directly if asked"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "USA, WA, Seattle - 143,700.00 - 194,400.00 USD annually"
risk_summary:
  legitimacy: "high_confidence"
  classification: "clear"
  culture: "not_evaluated"
  interview_redflags: "not_evaluated"
  ai_infra: "consistent"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype | Backend / Distributed Systems Engineer (primary) + Platform / Cloud Infrastructure Engineer (primary) |
| Domain | Internal enterprise tooling — employee onboarding / workforce automation (not customer-facing) |
| Function | Build (full SDLC: design, develop, deploy, operate) |
| Seniority | SDE I / entry professional level — JD asks "1+ years of non-internship professional software development experience," no degree requirement stated as hard bar |
| Remote | Onsite — "USA, WA, Seattle" is the structured location field, no remote/hybrid language anywhere in the JD |
| Team size | Not stated — "Contingencies Tech team within the Employee Onboarding Experience (EOE) organization," part of the broader "Workforce Solutions" org (serves WW Stores, AWS, Devices, Talent Acquisition) |
| Culture screen | Not evaluated — no `culture_screen.require` configured in `config/profile.yml`; scored qualitatively in Block D/G instead |
| TL;DR | Entry-level backend automation role building serverless AWS tooling for Amazon's internal employee-onboarding pipeline — solid archetype and comp fit, tempered by a borderline experience bar and Amazon's 2026 layoff climate. |

No geo-mismatch: the JD names no remote option anywhere to contradict the Seattle onsite location field, so no flag applies.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| "1+ years non-internship professional software development" | TiMoto AI, Software Engineer, Sep 2025-Present — ~10 months as of 2026-07, non-internship title. Below the literal 1-year bar today, crosses it by Sep 2026. |
| "own automation of business processes ... using proven, as well as evolving native AWS services" | TiMoto: "architecting a multi-AZ ECS Fargate deployment with Terraform IaC" — direct AWS automation/IaC experience, container-based rather than serverless |
| "Develop code, build CI/CD pipelines, test automation, and dashboards for monitoring health of systems and data pipelines" | TiMoto: "deployed Prometheus and Grafana metrics alongside CloudWatch dashboards"; Develop for Good: "GitHub Actions CI/CD auto-scaling policy" cut deployment time 90% |
| "Solve the challenging problem of scaling these services ... in real-time" | Develop for Good: "Scaled a backend to support 500+ concurrent users"; TiMoto: sustained 99.9% uptime under production load |
| "data domain infrastructure and API primitives" | TiMoto gRPC/Protobuf inter-service layer; Google Chrome Protocol Buffers IPC transport — both are API/schema-design experience, though at a different layer (service-to-service, not internal HR data domain) |
| "Solve complex business and technical problems by diving deep, collecting data to make well informed decisions" | TiMoto gRPC deadlock fix: traced root cause via lock-acquisition-order analysis rather than guessing |
| "GenAI versus Agentic AI solutions" (nice-to-have context, not a hard requirement) | TiMoto vLLM/PagedAttention production serving experience — directly relevant if this ever surfaces in the role |

**Gaps:**

1. **Non-internship experience under 1 year (soft, not a blocker).** TiMoto is real production ownership, not an internship, but it's ~10 months old. Mitigation: lead with total engineering tenure across TiMoto + two internships in the cover letter/interview framing, and note the 1-year mark lands well before a typical Amazon SDE I offer/start date.
2. **Serverless (Lambda/API Gateway/Step Functions) vs. container-based (ECS Fargate).** Both are AWS IaC automation, but the JD explicitly says "mostly server-less environment." Mitigation: frame Terraform/IaC skill as transferable across AWS compute models; if asked directly, be honest that Fargate was the specific choice at TiMoto and explain why (multi-AZ container orchestration fit that use case better than a fully serverless design).
3. **No prior internal-enterprise-tooling experience** (this role serves 100,000s of *employees*, not customers). Mitigation: TiMoto and Develop for Good are both "internal system reliability for real users" stories — reframe from customer-facing to any-user-facing scale.

## C) Level and Strategy

1. **Level detected:** SDE I (entry professional) — the "1+ years non-internship" bar plus lack of any senior-scope language ("mentor," "drive strategy," "own a domain") both point to L4-equivalent, matching Harry's new-grad-adjacent profile.
2. **Sell senior without lying:** Lead with "primary engineer" framing from TiMoto — Harry didn't just contribute to infrastructure, he owns it end-to-end on a 3-person team, including the observability stack, the deadlock fix, and the cost-optimized multi-AZ redesign. That end-to-end ownership story reads above typical SDE I scope even though the title and tenure are entry-level.
3. **If downleveled:** N/A — this JD is already entry-level; there's no lower level to negotiate into. If Amazon's internal leveling puts this at SDE I but comp lands below $150K total, use the standard negotiation script (see `_profile.md` → Negotiation Scripts) to push toward the top of the advertised base band plus sign-on.

## D) Comp and Demand

**Company type:** Public big tech / mature tech — Confidence: High. Amazon.com Services LLC, structured SDE leveling (SDE I/II/III), large engineering org, standardized public salary-range disclosure per Washington state law.

**Compensation reliability:** High — the JD states an explicit base salary range as required by WA pay-transparency law, plus standard RSU/sign-on structure typical of Amazon offers.

| Component | Value | Source |
|---|---|---|
| Advertised (JD) | USA, WA, Seattle — 143,700.00 - 194,400.00 USD annually (base) | JD |
| Likely guaranteed base | $143.7K-$194.4K, per WA transparency-law disclosure | JD |
| Variable / conditional cash | Sign-on bonus (front-loaded, standard Amazon structure) | Market data |
| Non-cash benefits | RSUs (back-loaded vesting — 5%/15%/40%/40% schedule is Amazon's well-documented default), 401(k) match, health insurance, parental leave | JD "Benefits" section, market data |
| Market comparable — Amazon SDE I, Greater Seattle | $159K-$205K+ total comp, median ~$181K | [Levels.fyi](https://www.levels.fyi/companies/amazon/salaries/software-engineer/levels/sde-i/locations/greater-seattle-area) |

The advertised range is base salary only — total comp (base + RSU vesting once ramped + sign-on) typically lands close to or above the Levels.fyi SDE I Seattle median of ~$181K, which sits inside Harry's $150-200K target range and well above his $140K walk-away floor. Note the well-documented Amazon RSU back-loading: year-one and year-two effective TC is usually lower than the steady-state number due to the vesting schedule and reduced/expired sign-on bonus — worth factoring into any comparison against a flat-vesting offer from another company.

**Demand trend:** Mixed signal. Amazon eliminated roughly 30,000 corporate roles in 2026 (~10% of its corporate workforce), concentrated in AWS professional services, Alexa AI, Prime Video/Studios, Amazon Pharmacy, and Selling Partner Services (a **different** "onboarding" org — third-party seller onboarding, not the internal Employee Onboarding Experience team behind this JD). Against that backdrop, Amazon has also announced plans to hire roughly 11,000 SDE interns and full-time engineers in 2026, prioritizing AI-forward roles — and this JD's explicit "GenAI versus Agentic AI" language fits that stated hiring priority, not the divisions being cut.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Summary/headline | Backend/systems generalist framing | Lead with "AWS automation + backend infrastructure" framing | Matches JD's "automation of business processes ... using native AWS services" almost verbatim |
| 2 | TiMoto bullet order | Observability bullet first | Lead with the Multi-AZ ECS Fargate + Terraform IaC bullet | This is the single most directly relevant bullet — AWS automation, IaC, cost/reliability tradeoffs |
| 3 | Develop for Good bullet | As-is | Keep as-is, but emphasize "stateless AWS BaaS" phrasing | JD explicitly asks for "mostly server-less environment" — this bullet is the closest thing to serverless experience on the CV |
| 4 | Skills section | Cloud & Infrastructure row lists ECS Fargate, EKS, EC2, S3, RDS | No change needed — already lists the right AWS primitives | JD asks for "native AWS services," not a specific compute model |
| 5 | LinkedIn headline | Generic backend/systems | Add "AWS automation" as a keyword | Recruiter search surface for this team likely filters on AWS + automation terms |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Best for |
|---|---|---|---|
| 1 | "Own automation of business processes ... using AWS services" | Multi-AZ Circuit Breaker at TiMoto (story bank) | Reliability, SRE, Terraform/IaC, cost optimization |
| 2 | "Solve the challenging problem of scaling these services ... in real-time" | N+1 Fix at Develop for Good (story bank) | Backend, SQL, scaling, production problem-solving |
| 3 | "Build CI/CD pipelines, test automation, and dashboards for monitoring health of systems" | Building Observability Stack from Zero at TiMoto (story bank) | SRE, observability, CloudWatch, Prometheus/Grafana |
| 4 | "Solve complex business and technical problems by diving deep" | gRPC Deadlock Fix at TiMoto (story bank) | Debugging, concurrency, root-cause analysis |
| 5 | "Contribute to engineering excellence initiatives" | Post-Mortem Culture at TiMoto (story bank) | Process/culture building, incident management |
| 6 | "Work with your team to gather requirements, design, develop, deploy, operate" | Design Doc Review at Google Chrome (story bank) | Cross-functional collaboration, technical communication |

All six stories already exist in `interview-prep/story-bank.md` — no new stories needed for this evaluation.

**Recommended case study:** TiMoto's Multi-AZ Terraform/ECS Fargate redesign — it is the single closest match to "own automation of business processes ... using native AWS services," and demonstrates both IaC fluency and a measurable cost/reliability tradeoff (44% cost cut, 99.9% uptime).

**Red-flag questions and how to answer them:**
- *"You've only got ~10 months of non-internship experience — this role asks for 1+ years."* → Be direct: note the two prior internships (Google Chrome, Develop for Good) add production-adjacent depth beyond the literal number, and that by any realistic Amazon offer/start timeline the 1-year mark will already be crossed. Don't over-explain or sound defensive — state it once and move to strengths.
- *"Why isn't this AWS work serverless (Lambda) instead of ECS Fargate?"* → Explain the tradeoff explicitly: multi-AZ container orchestration with persistent gRPC connections fit TiMoto's workload better than event-driven serverless; frame it as a deliberate architecture decision, not a skill gap.
- *"Do you have experience with internal enterprise tooling, not just customer-facing products?"* → TiMoto and Develop for Good are both "reliability for real concurrent users" stories even though the end users weren't paying customers — reframe around scale and reliability, not audience.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | "Apply now" link resolves to a live, working application flow (`amazon.jobs/applicant/jobs/10476687/apply`); no expired/closed banner, no redirect to a generic search page | Positive |
| Description quality | Names a specific team ("Contingencies Tech" within "Employee Onboarding Experience," under the broader "Workforce Solutions" org), specific technologies (AWS, GenAI/Agentic AI, CI/CD), and a defined mission ("build modern replacements for legacy third-party systems") — well above boilerplate | Positive |
| Requirements realism | Basic qualifications (1+ years non-internship experience, one programming language) are realistic and modest for the described scope — no entry-level-title-with-staff-requirements contradiction | Positive |
| Salary transparency | Explicit base range disclosed (WA pay-transparency law) | Positive |
| Company hiring signals | Amazon cut ~30,000 corporate roles in 2026, but concentrated in AWS professional services, Alexa AI, Prime Video/Studios, Amazon Pharmacy, and Selling Partner Services — a distinct org from this JD's Workforce Solutions/EOE team. Amazon has separately announced plans to hire ~11,000 SDE interns/FTEs in 2026 focused on AI-forward roles, which this JD's "GenAI vs. Agentic AI" language fits. | Neutral (company-wide caution, no direct signal against this specific team) |
| Reposting pattern | No match for this exact req ID (10476687) in `data/scan-history.tsv`; other distinct Amazon SDE req IDs appear (different roles), not a repost of this one | Positive |
| Role market context | SDE I roles at large tech companies commonly fill in 4-8 weeks; nothing here suggests an outlier timeline | Neutral |

**Context notes:** Amazon's 2026 layoffs are real and large in scale, but public reporting consistently ties them to specific divisions (AWS professional services, Alexa AI, media, Pharmacy, third-party-seller Selling Partner Services) that are organizationally distinct from this JD's internal employee-facing Workforce Solutions/EOE team. Treat the company-wide layoff context as a reason for general caution about Amazon's near-term corporate stability, not as direct evidence against this specific opening.

**7. AI-Buzzword vs. Infrastructure Mismatch:** Not flagged — the JD's "GenAI versus Agentic AI" language is a single supporting phrase inside a concretely scoped backend-automation role, not a heavy transformation-buzzword layer; no team-size mismatch or legacy-industry base rate applies (Amazon is neither small-team nor legacy-industry). Fewer than 2 of the 3 signal classes are present.

**6. Employment Classification:** Not flagged — no contractor/services-status language ("1099," "independent contractor," "invoice for services"); this is a standard Amazon.com Services LLC employment posting with full benefits language (401(k), health insurance, parental leave).

**8. Benefits/Employment Terminology Country Mismatch:** Not flagged — location is USA, WA, Seattle, and the benefits section uses US-only terms (401(k)) consistently with that location. No mismatch.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence — live apply flow, specific team/scope, salary disclosed, no reposting detected |
| Employment classification | ✅ clear — standard US employment posting, no contractor-status language |
| Culture screen | — not evaluated (no `culture_screen.require` configured in `config/profile.yml`) |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | ✅ consistent — GenAI/Agentic AI language is a supporting detail in a concretely scoped role, not oversold transformation framing |

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 179-amazon` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Amazon's Workforce Solutions team is rebuilding the infrastructure behind how hundreds of thousands of Amazonians onboard and move through their careers — exactly the kind of high-stakes, high-scale automation work I want to build next.

**Profile introduction**
I'm a Computer Science student at Georgia State (May 2027) currently the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I own a production system end-to-end: gRPC services, AWS infrastructure via Terraform, and observability, sustaining 99.9% uptime on a 3-person team. Before that, I shipped a C++ IPC transport layer to Chrome's stable channel as a Google engineering intern, serving 3B+ users.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Multi-AZ ECS Fargate deployment,** sustaining 99.9% uptime and cutting infrastructure cost 44% via Terraform IaC and an auto-rollback circuit breaker pattern.
- **gRPC deadlock fix,** restoring 100% evaluation success rate at sub-50ms p99 by redesigning lock-acquisition ordering under concurrent calls.
- **C++ IPC transport layer,** shipped to Chrome's stable channel, serving 3B+ active users at sub-50ms p99 and 10K+ req/sec.
- **AWS BaaS backend,** scaled to 500+ concurrent users with 90% faster deployment via a GitHub Actions CI/CD auto-scaling policy.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: what challenges does Amazon Workforce Solutions/EOE face that you'd address? How would you approach the shift from legacy third-party onboarding systems to a "friction-free" serverless AWS automation layer?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- Experience bar: JD asks for "1+ years of non-internship professional software development experience"; TiMoto is ~10 months as of this evaluation. Address directly and briefly if raised — do not over-explain.
- Serverless vs. container-based AWS experience: TiMoto is ECS Fargate (containers), JD emphasizes "mostly server-less." Frame as transferable AWS/IaC skill, be honest about the specific choice if asked.
- Relocation: role is onsite Seattle, WA; candidate is based in Atlanta, GA — profile notes openness to relocation for the right role.

**JD keywords to mirror** *(extracted for ATS + human read)*
AWS, serverless, automation, API primitives, data domain infrastructure, CI/CD pipelines, test automation, monitoring dashboards, GenAI, Agentic AI, business process automation, full stack, software development lifecycle, scalability, legacy system replacement, cloud infrastructure, Workforce Solutions, employee onboarding, distributed workflows, country-specific rules/regulations

---
*Run `/career-ops cover 179-amazon` to complete angles, confirm research, and generate the PDF.*

---

## Keywords extracted

AWS, serverless architecture, API primitives, data domain infrastructure, CI/CD pipelines, test automation, monitoring dashboards, GenAI, Agentic AI, business process automation, full-stack development, software development lifecycle, scalability, legacy system replacement, cloud infrastructure, employee onboarding, contingency services, distributed workflows, country-specific regulations, engineering excellence
