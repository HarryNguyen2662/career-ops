# Evaluation: StubHub — Software Engineer I, Core Compute Platform

**Date:** 2026-07-19
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=stubhubinc&token=4921819101
**Via:** —
**Archetype:** Platform / Cloud Infrastructure Engineer + Backend / Distributed Systems Engineer
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/181-stubhub-harry-nguyen-2026-07-19.pdf

---

## Machine Summary

```yaml
company: "StubHub"
role: "Software Engineer I, Core Compute Platform"
score: 3.8
legitimacy_tier: "High Confidence"
archetype: "Platform / Cloud Infrastructure Engineer + Backend / Distributed Systems Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "JD explicitly targets candidates 'Graduating in Spring/Summer 2026' -- Harry graduates May 2027, a full year later than the named cohort"
  - "Advertised base ($120-150K) undershoots the top of Harry's $150-200K target range; Levels.fyi StubHub L3 figure ($242K median) is far higher but inconsistent with the JD's own number -- treat as low-confidence context, not a substitute"
  - "Hybrid onsite New York, NY (3 days/week) -- requires relocation from Atlanta"
  - "Glassdoor overall rating 2.4/5, with recurring reviewer complaints about junior engineers being under-supported ('can't afford senior engineers, hire junior ones and put them in charge')"
top_strengths:
  - "EKS is literally named on Harry's CV (AWS ECS Fargate, EKS, EC2, S3, RDS) -- direct, specific match to 'core compute platform, primarily EKS in AWS'"
  - "Terraform IaC experience at TiMoto maps directly onto the JD's Terraform/Crossplane ask"
  - "'AI Readiness' / 'Agentic development workflows' platform focus is conceptually adjacent to TiMoto's production vLLM/PagedAttention serving work"
  - "Platform/Cloud Infrastructure and Backend/Distributed Systems are both primary North Star archetypes"
risk_level: "Medium"
confidence: "Medium"
next_action: "Apply -- select 'Less than 1 year' on the experience-level question (TiMoto is non-internship, ~10 months); be ready to address the Spring/Summer 2026 grad-cohort mismatch directly if raised"
discard_reasons:
  - "seniority_mismatch"
via: null
company_confidential: false
advertised_comp: "$120,000 - $150,000 USD"
risk_summary:
  legitimacy: "high_confidence"
  classification: "clear"
  culture: "caution"
  interview_redflags: "not_evaluated"
  ai_infra: "consistent"
```

## A) Role Summary

| Field | Value |
|---|---|
| Archetype detected | Platform / Cloud Infrastructure Engineer (primary) + Backend / Distributed Systems Engineer (primary) |
| Domain | Internal developer platform — Core Compute team, EKS/AWS-based, serving "hundreds of services across StubHub" |
| Function | Build (design, develop, maintain platform interfaces/tooling); explicitly "Platform as a product, not a service desk" |
| Seniority | SDE1 / entry professional — application form's own experience-level question caps expected experience at "Less than 1 year" for the intended pipeline, with 1-2 years and 2+ years as broader buckets |
| Remote | Hybrid — 3 days/week in office, New York, NY (`emphasis` tag confirms explicitly in JD body) |
| Team size | Not stated — "Core Compute team" within a larger platform org |
| Culture screen | Caution — no `culture_screen.require` configured in `config/profile.yml`, so scored qualitatively: the JD's "self-service, easy buttons, empowerment over rigid controls" framing is a genuine positive signal, but it's directly contradicted by a real, corroborating negative signal found in Block D/G research (Glassdoor 2.4/5 rating, recurring reviewer complaints specifically about under-supported junior engineers) — see Block D for detail |
| TL;DR | Strong technical-fit platform engineering role at a newly-public ticketing marketplace — excellent EKS/Terraform/AWS overlap, tempered by a named grad-cohort mismatch and mixed employee-review signal. |

No geo-mismatch: the JD's structured location and body text both consistently state hybrid onsite New York, NY — no contradiction to flag.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| "Core compute platform, primarily EKS in AWS" | CV Skills: "AWS (ECS Fargate, **EKS**, EC2, S3, RDS)" — EKS is named explicitly, plus Terraform and Kubernetes in the same skills row |
| "Infrastructure as Code (Terraform, Crossplane)" | TiMoto: "architecting a multi-AZ ECS Fargate deployment with **Terraform IaC**" — direct IaC production experience (Crossplane specifically not on CV, but Terraform is the dominant IaC tool named in the JD) |
| "Facilitate AI Agent and model training" / "AI Readiness... Agentic development workflows" | TiMoto: production **vLLM/PagedAttention** inference engine, solving KV cache memory fragmentation for LLM serving — this is model-serving experience, one layer up from platform-hosting-for-AI, but directly demonstrates fluency with the workload type this platform needs to support |
| "Designing and building powerful, reusable tools, including high-leverage SDKs, services, and shared packages" | TiMoto: "building TiMoto's observability stack from zero" (Prometheus/Grafana/CloudWatch) — a reusable internal tooling build, same shape as "developer enablement" |
| "Programming languages such as Python, Go, Java, or C#" | CV Skills: "C++, Python, Go, TypeScript, Java, JavaScript, SQL, Bash, Rust" — three of the four named languages directly covered |
| "Curiosity about how complex systems work together in production... reliable, scalable services" | TiMoto: 99.9% uptime multi-AZ deployment; gRPC deadlock fix restoring 100% evaluation success rate |
| "Bonus: Kubernetes, Terraform, AWS, DynamoDB, SQS, platform engineering, developer tooling, AI infrastructure" | Kubernetes/Terraform/AWS all on CV directly; DynamoDB is in `config/profile.yml`'s narrative (Develop for Good: "AWS, PostgreSQL, and DynamoDB at scale") though not in the cv.md bullet text itself; SQS not on CV |
| "Graduating in Spring/Summer 2026" | Georgia State, **Expected May 2027** — a full year after the named cohort |

**Gaps:**

1. **Grad-cohort mismatch (the primary gap).** This JD names a specific graduating window (Spring/Summer 2026) more explicitly than most "new grad" postings, which often just say "0-2 years" or leave the window open. Harry graduates a full year later. Mitigation: the application form's experience-level question (0 years / less than 1 year / 1-2 years / more than 2 years) doesn't hard-gate on grad date, only on experience — select "Less than 1 year" honestly and, if a recruiter raises the grad-date question directly, be upfront that you're targeting a May 2027 start but are open to discussing timing.
2. **Crossplane and SQS** — not on CV. Mitigation: minor, both are explicitly "bonus" items in the JD, not core requirements; Terraform (the more commonly used IaC tool of the two named) is on CV, and SQS gap can be framed as "familiar with the message-queue pattern via other AWS primitives" if asked, without overclaiming.
3. **DynamoDB** — present in `config/profile.yml`'s narrative but not spelled out in the cv.md Develop for Good bullets themselves. Mitigation: safe to mention in interview/cover letter since it's backed by a source-of-truth file, but do not add it to the CV bullets unless the underlying cv.md is updated first (out of scope for this evaluation).

## C) Level and Strategy

1. **Level detected:** SDE1 / entry-level — the application form itself defines this pipeline as "designed for new graduates or engineers with less than 1 year of professional experience," matching Harry's actual level closely (TiMoto is non-internship, ~10 months as of this evaluation).
2. **Sell senior without lying:** Lead with the "platform as a product" framing from the JD itself — TiMoto's observability stack was built the same way: as reusable infrastructure other people depend on, not a one-off fix. The multi-AZ Terraform/ECS Fargate work is the strongest single proof point for this specific team.
3. **If downleveled or grad-date questioned:** This is already the entry-level tier, so there's no lower level to negotiate into. If the grad-cohort mismatch becomes a hard blocker in the recruiter screen, there's little to negotiate — but many "new grad" pipelines at this seniority flex on start date for genuinely strong technical fits, so it's worth letting the interview process play out rather than pre-emptively assuming disqualification.

## D) Comp and Demand

**Company type:** Public big tech / mature tech, recently IPO'd — Confidence: Medium-High. StubHub Holdings, Inc. (NYSE: STUB) completed its IPO on September 17-18, 2025, reaching an $8.6B market valuation. Public-company disclosure norms apply to base salary, but the company has under a year of public-market trading history, which adds volatility/uncertainty specifically to equity compensation (less price history, less certainty about vesting-value realization) compared to a long-established public company.

**Compensation reliability:** High for base (explicit disclosed range, standard public-company gross base pay language); Medium for total comp (equity mentioned but not quantified, and the company's short public trading history is itself a source of equity-value uncertainty).

| Component | Value | Source |
|---|---|---|
| Advertised (JD) | $120,000 - $150,000 USD | JD |
| Likely guaranteed base | $120K-$150K, as stated ("anticipated gross base pay range") | JD |
| Variable / conditional cash | None stated (no bonus/commission mentioned) | JD |
| Non-cash benefits | Equity ("competitive base, equity, and upside that tracks with your impact"), 401(k), unlimited Flex Time Off, health/vision/dental | JD "What We Offer" |
| Market comparable — StubHub SWE L3 (entry), United States | Median total comp $242,359 | [Levels.fyi](https://www.levels.fyi/companies/stubhub/salaries/software-engineer/levels/l3) |

**Flag on the market comparable:** the Levels.fyi L3 figure ($242K median) is dramatically higher than the JD's own advertised base-only range ($120-150K) — a gap too large to explain by equity alone at a company only ~10 months post-IPO. This likely reflects either a small/noisy self-reported sample, a leveling mismatch (StubHub's internal L3 may not map cleanly onto this JD's "SDE1" title), or genuine total-comp upside once equity vests. Treat the Levels.fyi figure as directional context only — anchor expectations on the JD's own advertised base, and use the standard negotiation script to ask directly about total comp (base + equity) once in the process, rather than assuming the higher figure applies.

**Demand trend:** No confirmed 2026 layoffs or hiring-freeze announcements found for StubHub specifically. Historical context: StubHub closed its San Francisco office and conducted layoffs in August 2022 (pre-IPO, under different ownership structure), and the company filed 18 H-1B Labor Condition Applications for FY2025-2026, indicating active, ongoing hiring including for visa-sponsored roles. Employee sentiment on Glassdoor is notably weak (2.4/5 overall rating across 801 reviews), with a recurring specific complaint that the company "hire[s] junior [engineers] and then put[s] them in charge of pumping out code" without adequate senior support — this is a genuine culture-fit caution signal for an entry-level candidate, independent of the posting's legitimacy.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | Skills section | AWS row already lists ECS Fargate, EKS, EC2, S3, RDS | No change needed — EKS is already present and prominent | JD's core ask is "primarily EKS in AWS" |
| 2 | TiMoto bullet order | Multi-AZ/Terraform bullet leads (from prior tailoring) | Keep leading with the multi-AZ ECS Fargate/Terraform IaC bullet | Most direct match to "provisioning, maintaining, and optimizing the platform" |
| 3 | TiMoto observability bullet | Second position | Keep in top 2 — emphasizes "designing and building powerful, reusable tools" | Directly maps to the JD's "Developer Enablement" responsibility |
| 4 | Summary/headline | Backend/systems generalist framing | Emphasize "platform engineering + AWS/Kubernetes" framing for this application | JD is explicitly platform-team-focused, not general backend |
| 5 | Cover letter | N/A | Address the grad-timing question proactively and briefly, framed as enthusiasm rather than apology | Better to control the narrative on the one real gap than let it surface unaddressed |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Best for |
|---|---|---|---|
| 1 | "Provisioning, maintaining, and optimizing the platform" | Multi-AZ Circuit Breaker at TiMoto (story bank) | Reliability, Terraform/IaC, AWS platform design |
| 2 | "Designing and building powerful, reusable tools... SDKs, services, and shared packages" | Building Observability Stack from Zero at TiMoto (story bank) | Internal tooling, developer enablement |
| 3 | "Facilitate AI Agent and model training" / platform for AI workloads | vLLM Serving Architecture at TiMoto (story bank) | ML infrastructure, AI workload hosting, tradeoff analysis |
| 4 | "Curiosity about how complex systems work together in production" | gRPC Deadlock Fix at TiMoto (story bank) | Debugging, distributed systems, production troubleshooting |
| 5 | "Quality and Best Practices... software development best practices" | Post-Mortem Culture at TiMoto (story bank) | Process discipline, engineering culture |
| 6 | "Strategic Partnership: Collaborate with senior engineers" | Design Doc Review at Google Chrome (story bank) | Cross-functional collaboration, working with senior engineers |

All six stories already exist in `interview-prep/story-bank.md` — no new stories needed for this evaluation.

**Recommended case study:** TiMoto's Multi-AZ Terraform/ECS Fargate build — it is the single closest analog to "the design, development, and maintenance of our end-to-end Compute Platform," and pairs well with the observability-stack story as a "platform, then the tools on top of it" narrative arc.

**Red-flag questions and how to answer them:**
- *"This role targets Spring/Summer 2026 grads — you're graduating May 2027. Why should we move forward?"* → Be direct and confident, not defensive: TiMoto is real, non-internship, production ownership experience that most Spring 2026 grads won't have; the skills match (EKS, Terraform, AWS) is exact regardless of grad date; and you're happy to discuss a start-date that works for both sides.
- *"Glassdoor reviews mention junior engineers being under-supported here — what's your take?"* → Only answer if asked; don't raise it. If asked directly, frame it as a question back to the interviewer: ask what mentorship/onboarding structure exists for SDE1s specifically on the Core Compute team.
- *"What's your experience with EKS specifically, versus ECS Fargate?"* → Be honest: TiMoto's production experience is ECS Fargate, not EKS; both are AWS container-orchestration platforms, and the underlying Kubernetes concepts (from the Skills list) transfer, but be ready to discuss the specific differences if pressed (EKS is managed Kubernetes; ECS Fargate is AWS's own serverless container orchestration).

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | Application form is fully live and functional (all fields present, reCAPTCHA active, real "Submit application" flow) | Positive |
| Description quality | Specific team name ("Core Compute team"), specific technologies (EKS, AWS, Terraform, Crossplane, DynamoDB, SQS), a clearly articulated team philosophy ("Platform as a product, not a service desk"), and realistic entry-level requirements with no internal contradictions | Positive |
| Requirements realism | Explicitly scoped to "new graduates or engineers with less than 1 year of professional experience" via the application form's own screening question — internally consistent with the "SDE1" title and JD body | Positive |
| Salary transparency | Explicit gross base pay range disclosed ($120,000-$150,000) | Positive |
| Company hiring signals | No confirmed 2026 layoffs or hiring-freeze found; company is newly public (Sept 2025 IPO, $8.6B valuation) and filed 18 H-1B LCAs for FY2025-2026, indicating active, ongoing engineering hiring including visa-sponsored roles | Positive |
| Reposting pattern | No prior StubHub entries found in `data/scan-history.tsv` — first time this company has surfaced in the pipeline, so no reposting history to evaluate | Neutral |
| Role market context | Entry-level platform-engineering reqs at a mid-size public company commonly fill within a normal 4-8 week window; nothing here suggests an outlier | Neutral |

**Context notes:** The named Spring/Summer 2026 grad-cohort targeting is unusually specific compared to most "new grad" postings, which suggests this is a real, actively-managed campus-style pipeline rather than an evergreen placeholder — a positive legitimacy signal even though it creates the timing gap noted above.

**6. Employment Classification:** Not flagged — standard US employment posting with full benefits language (401(k), health/vision/dental, paid parental leave), no contractor-status wording.

**7. AI-Buzzword vs. Infrastructure Mismatch:** Not flagged — "AI Readiness" and "Agentic development workflows" appear as one bullet within a concretely scoped platform-engineering role at an established, funded, newly-public company; no team-size mismatch or legacy-industry base rate applies. Fewer than 2 of the 3 signal classes present.

**8. Benefits/Employment Terminology Country Mismatch:** Not flagged — location is New York, NY, and all benefits/employment terms (401(k), etc.) are consistent with a US posting.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence — live application flow, specific team/tech/philosophy, salary disclosed, active hiring signals (H-1B filings) |
| Employment classification | ✅ clear — standard US full-time employment posting |
| Culture screen | ⚠️ caution — JD's stated "self-service, empowerment" platform philosophy is a positive signal, but Glassdoor 2.4/5 rating with recurring specific complaints about under-supported junior engineers is a real, corroborating counter-signal for an entry-level hire |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | ✅ consistent — "AI Readiness"/"Agentic workflows" is one bullet within a concretely scoped platform role at a funded, newly-public company, not oversold transformation framing |

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 181-stubhub` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
StubHub's Core Compute Platform team treats infrastructure as a product, not a service desk — building the "easy buttons" that let hundreds of engineering teams move fast without fighting their own tooling. That's the exact problem I've spent the last year solving at TiMoto AI, just at a smaller scale.

**Profile introduction**
I'm a Computer Science student at Georgia State (May 2027) currently the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I own a production system end-to-end on a 3-person team: multi-AZ AWS infrastructure via Terraform, a full observability stack built from zero, and a production LLM-serving layer. Before that, I shipped production infrastructure code at Google as a Chrome engineering intern.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Multi-AZ ECS Fargate deployment,** sustaining 99.9% uptime and cutting infrastructure cost 44% via Terraform IaC and an auto-rollback circuit breaker pattern.
- **Observability stack built from zero at TiMoto,** cutting incident root-cause time to under 15 minutes via Prometheus, Grafana, and CloudWatch across the gRPC and ML serving layers.
- **vLLM/PagedAttention inference engine,** eliminating OOM failures under concurrent production load by solving KV cache memory fragmentation for LLM serving.
- **C++ IPC transport layer,** shipped to Chrome's stable channel, serving 3B+ active users at sub-50ms p99.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: what specific pain points on the Core Compute Platform team would you want to dig into first — service discovery, deployment tooling, or AI/agentic workload support? Any specific StubHub engineering blog posts or public talks worth referencing?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- Grad-cohort mismatch: JD targets Spring/Summer 2026 grads; Harry graduates May 2027. Address directly and briefly if raised in the process — don't over-explain.
- Advertised base ($120-150K) is below the top of target range; Levels.fyi's much higher StubHub L3 figure is inconsistent with the JD's own number and should not be assumed — clarify total comp directly with the recruiter.
- Crossplane and SQS not on CV (both explicitly "bonus" items, not requirements) — don't over-address unless asked.

**JD keywords to mirror** *(extracted for ATS + human read)*
Core Compute Platform, EKS, AWS, Kubernetes, Terraform, Crossplane, platform engineering, developer tooling, SDKs, self-service, AI Agent, model training, Agentic development workflows, distributed systems, scalability, reliability, DynamoDB, SQS, infrastructure as code, developer enablement, high-velocity execution

---
*Run `/career-ops cover 181-stubhub` to complete angles, confirm research, and generate the PDF.*

---

## Keywords extracted

Core Compute Platform, EKS, AWS, Kubernetes, Terraform, Crossplane, platform engineering, developer tooling, SDKs, self-service infrastructure, AI Agent, model training, Agentic development workflows, distributed systems, scalability, reliability, DynamoDB, SQS, infrastructure as code, developer enablement, service discovery, day 2 operations, high-velocity execution
