# Evaluation: Astronomer — Software Engineer, Infra & Systems

**Date:** 2026-07-20
**URL:** https://jobs.ashbyhq.com/astronomer/540c1dd1-5658-49f9-b587-37865a360cd4
**Via:** —
**Archetype:** Platform / Cloud Infrastructure Engineer + Site Reliability Engineer
**Score:** 3.9/5
**Legitimacy:** High Confidence
**PDF:** output/183-astronomer-harry-nguyen-2026-07-20.pdf

---

## Machine Summary

```yaml
company: "Astronomer"
role: "Software Engineer - Infra & Systems"
score: 3.9
legitimacy_tier: "High Confidence"
archetype: "Platform / Cloud Infrastructure Engineer + Site Reliability Engineer"
final_decision: "Apply"
hard_stops: []
soft_gaps:
  - "Advertised base ($144-160K) is on the lower-middle end of Harry's $150-200K target, though above the $140K walk-away floor"
  - "Series D (May 2025) was at a $775M valuation, a 48% down-round from the ~$1.5B Series C peak (March 2022) -- a real caution on equity value, though $93M in fresh capital was raised"
  - "Kubernetes operators/controllers, Helm, container security (CVEs), and Apache Airflow are all listed 'nice to have' and not currently on Harry's CV"
top_strengths:
  - "On-call rotation, Terraform IaC, and multi-AZ/observability work at TiMoto map almost one-to-one onto this team's actual responsibilities"
  - "Distinct from report #146 (different req, different team -- Astro Core Services vs. Infrastructure and Systems) -- not a duplicate"
  - "Explicit mentorship structure ('guidance of senior engineers', 'pairing with senior engineers') matches an early-career candidate well"
  - "Platform/Cloud Infrastructure and SRE are both primary North Star archetypes -- direct title and scope match"
risk_level: "Medium"
confidence: "Medium"
next_action: "Apply -- no grad-date constraint found in this JD, so timing is not a blocker; note the 0-4 year experience band already spans SWE I and SWE II, so level is determined by the interview process, not the application"
discard_reasons: []
via: null
company_confidential: false
advertised_comp: "$144,000 - $160,000 (based on level and geography)"
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
| Archetype detected | Platform / Cloud Infrastructure Engineer (primary) + Site Reliability Engineer (primary) |
| Domain | DataOps platform infrastructure — the compute/networking/security layer underneath Astro (Astronomer's managed Apache Airflow platform), spanning both multi-tenant cloud and Astro Private Cloud (self-hosted, for regulated/air-gapped customers) |
| Function | Build and operate (IaC, Kubernetes, CI/CD, backend platform services in Go/TypeScript) |
| Seniority | Software Engineer I or II — the posting explicitly covers both levels; "the level you're hired at depends on experience and demonstrated scope," determined during the interview process rather than at application time |
| Remote | Hybrid — New York City |
| Team size | Not stated — final team assignment (multi-tenant cloud vs. Astro Private Cloud vs. both) "determined later in the interview process based on need and fit" |
| Culture screen | Not evaluated — no `culture_screen.require` configured in `config/profile.yml`; scored qualitatively in Block D instead |
| TL;DR | Entry-level (SWE I/II) infrastructure role at a well-funded DataOps company, with responsibilities (Terraform, Kubernetes, on-call, observability) that closely mirror Harry's actual TiMoto work — strong technical fit, moderate comp, real funding-trajectory nuance worth knowing. |

No geo-mismatch: the JD's structured location (New York City, Hybrid) is consistent throughout the body text, with no remote claim to contradict it.

## B) Match with CV

| JD Requirement | CV Evidence |
|---|---|
| "Infrastructure-as-Code (Terraform, Kubernetes manifests/operators, CI/CD pipelines)" | TiMoto: "architecting a multi-AZ ECS Fargate deployment with **Terraform IaC**"; CV Skills: Terraform, Kubernetes, Docker, CI/CD |
| "Backend services in Golang and/or TypeScript" | CV Skills: Go, TypeScript both listed; Pulumi project: "Submitted Go CLI features"; Google Chrome: TypeScript/React system |
| "Help operate and troubleshoot cloud resources, Kubernetes clusters, networking, and observability tooling" | TiMoto: "deployed Prometheus and Grafana metrics alongside CloudWatch dashboards"; multi-AZ circuit breaker/auto-rollback pattern |
| "Participate in on-call rotation, pairing with senior engineers to troubleshoot and resolve incidents" | TiMoto: "building a post-mortem practice with runbooks and a shared on-call rotation" — a direct, near-verbatim match |
| "0-4 years of experience... or equivalent internship/coursework" | TiMoto (~10 months, non-internship) + Google Chrome + Develop for Good internships — comfortably inside this wide band |
| "Working knowledge of Linux fundamentals, networking basics" | Implicit via AWS/Docker/ECS Fargate production work (Linux-based by default); coursework includes Computer Networks |
| "Exposure to a major cloud provider (AWS, GCP, or Azure)" | CV Skills: "AWS (ECS Fargate, EKS, EC2, S3, RDS)... GCP" — direct, strong match on AWS specifically |
| "Comfortable with version control (Git) and automated testing practices" | Google Chrome: "95% test coverage" cited twice across bullets |
| Nice to have: "Kubernetes... operators/controllers, Helm charts" | Kubernetes is on CV Skills, but no specific operator/controller/Helm experience — gap |
| Nice to have: "Container image security... CVEs, minimal base images" | Not on CV — gap |
| Nice to have: "Apache Airflow or other data-orchestration tools" | Not on CV — gap, though explicitly optional |

**Gaps:**

1. **Kubernetes depth beyond the basics (operators, controllers, Helm).** TiMoto's container orchestration was ECS Fargate, not Kubernetes specifically, so this is a real but explicitly "nice to have" gap. Mitigation: frame Kubernetes/Docker skill-list familiarity honestly as basics-level, and lean on the Terraform/multi-AZ/circuit-breaker story as the stronger, more directly comparable proof point.
2. **Container security (CVEs, minimal base images).** Not covered on CV. Mitigation: minor, nice-to-have only — don't over-address unless asked.
3. **Apache Airflow / data-orchestration tools.** Not covered on CV, but the JD explicitly frames this as optional, not required — no mitigation needed beyond genuine curiosity if it comes up.

## C) Level and Strategy

1. **Level detected:** SWE I or II — genuinely ambiguous by design; the posting states level is set by "experience and demonstrated scope" during the interview process, not a fixed bar at application time.
2. **Sell senior without lying:** Lead with the on-call/post-mortem/runbook story from TiMoto — it directly demonstrates the exact behavior this JD asks for ("participate in on-call rotation, pairing with senior engineers"), and it's real production ownership rather than coursework or a bootcamp project, which should help land toward SWE II rather than SWE I.
3. **If leveled at SWE I:** Given the advertised range already spans both levels within the same $144-160K band (level and geography both affect where in the range an offer lands), there's less room to negotiate level directly — focus any negotiation on landing toward the top of the stated range instead.

## D) Comp and Demand

**Company type:** Growth-stage / late-stage VC-backed startup — Confidence: Medium-High. Astronomer has raised $375M total across multiple rounds, most recently a $93M Series D (May 2025) — a well-capitalized company by startup standards, with structured, disclosed salary bands (a maturity signal), though not yet public.

**Compensation reliability:** Medium — the JD states an explicit base range tied to level and geography, which is more specific than many startup postings, but total comp (base + equity) is not broken out, and equity value is harder to assess given the company's recent valuation trajectory (see below).

| Component | Value | Source |
|---|---|---|
| Advertised (JD) | $144,000 - $160,000 (based on level and geography) | JD |
| Likely guaranteed base | $144K-$160K, as stated, level-dependent | JD |
| Variable / conditional cash | None stated | JD |
| Non-cash benefits | Equity component (unquantified), "comprehensive benefits package" (unspecified) | JD |
| Funding context | $375M total raised; $93M Series D (May 2025) at a $775M valuation | [PRNewswire](https://www.prnewswire.com/news-releases/astronomer-secures-93-million-series-d-funding-to-deliver-unified-dataops-platform-for-enterprise-ai-302443454.html) |

**Notable valuation context:** the May 2025 Series D valued Astronomer at $775M — a **48% decline** from the ~$1.5B valuation at its March 2022 Series C. This is worth naming plainly: it does not mean the company is in distress (fresh $93M in capital, 800+ enterprise customers, Apache Airflow used by 80K+ organizations with 324M+ downloads in 2024 alone are all real, positive scale signals), but it does mean equity granted today is priced against a lower company valuation than 2022 employees received, and any personal read on "upside potential" should account for that reset rather than assume straight-line growth from the 2022 peak.

**Demand trend:** No 2026-specific layoff or hiring-freeze signal found. The company's last confirmed layoff was in January 2023 (76 people, ~20% of staff) — a dated data point, over 3 years old as of this evaluation, and not indicative of current conditions. The May 2025 Series D and continued Airflow adoption growth both point to active, ongoing hiring rather than contraction.

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | TiMoto bullet order | Multi-AZ/Terraform bullet leads (from recent tailoring) | Keep leading with multi-AZ ECS Fargate/Terraform IaC; move the post-mortem/on-call bullet to second | On-call participation is an explicit JD responsibility, not just implied |
| 2 | TiMoto observability bullet | Third position | Keep in top 3 | Directly maps to "networking, and observability tooling" |
| 3 | Skills section | Cloud & Infrastructure row lists Terraform, Kubernetes, Docker, AWS, GCP already | No change needed | Already covers the JD's core technical ask |
| 4 | Summary/headline | Backend/systems generalist framing | Emphasize "platform infrastructure + on-call reliability" framing for this application | Matches this specific team's actual day-to-day scope |
| 5 | Cover letter | N/A | Note genuine interest in the multi-tenant vs. Private Cloud distinction, and ask which is the likelier fit | Shows engagement with the JD's own stated ambiguity about team placement |

## F) Interview Plan

| # | JD Requirement | STAR+R Story | Best for |
|---|---|---|---|
| 1 | "Participate in on-call rotation, pairing with senior engineers to troubleshoot and resolve incidents" | Post-Mortem Culture at TiMoto (story bank) | On-call, incident response, process building |
| 2 | "Write, test, and maintain infrastructure code... Infrastructure-as-Code (Terraform...)" | Multi-AZ Circuit Breaker at TiMoto (story bank) | Terraform/IaC, reliability, cost optimization |
| 3 | "Help operate and troubleshoot cloud resources... observability tooling" | Building Observability Stack from Zero at TiMoto (story bank) | Observability, CloudWatch/Prometheus/Grafana |
| 4 | "Identify and fix bugs, misconfigurations, and small-scope incidents" | gRPC Deadlock Fix at TiMoto (story bank) | Debugging, concurrency, root-cause analysis |
| 5 | "Backend services in Golang and/or TypeScript" | N+1 Fix at Develop for Good (story bank) | Backend, debugging, data layer |
| 6 | "Participate in code and infrastructure-change reviews" | Design Doc Review at Google Chrome (story bank) | Code review culture, collaboration |

All six stories already exist in `interview-prep/story-bank.md` — no new stories needed for this evaluation.

**Recommended case study:** TiMoto's multi-AZ Terraform/circuit-breaker build, paired with the post-mortem/on-call story — together they cover both halves of this JD's core ask ("build and operate"), and both are genuine production ownership rather than a one-off assignment.

**Red-flag questions and how to answer them:**
- *"Which team would you rather join — multi-tenant cloud or Astro Private Cloud?"* → Be honest that both map well to your background, but if pressed, the regulated/air-gapped Private Cloud environment shares more in common with TiMoto's security-conscious, cost-constrained infra (small team, high accountability) — a genuine, not performative, preference if true.
- *"Astronomer's valuation dropped significantly since 2022 — does that concern you?"* → Don't volunteer this unless asked; if raised, respond factually: fresh $93M raised in 2025, strong Airflow adoption numbers, and equity is one part of a package you're evaluating alongside base and role fit — not the deciding factor for an early-career move.
- *"You don't have deep Kubernetes operator/Helm experience — how would you ramp up?"* → Be honest about the gap, then pivot to how you've ramped on unfamiliar infra before (e.g., learning Terraform/ECS Fargate from scratch at TiMoto) as evidence of the learning pattern, not the specific tool.

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting freshness | "Apply for this Job" resolves to a live, functional Ashby application flow | Positive |
| Description quality | Names a specific team ("Infrastructure and Systems"), specific products (Astro multi-tenant cloud, Astro Private Cloud), specific technologies (Terraform, Kubernetes, Go/TypeScript, AWS/GCP/Azure), and an unusually candid note that team assignment happens post-hire based on fit | Positive |
| Requirements realism | Explicitly dual-level (SWE I/II) with a realistic, wide experience band (0-4 years); no internal contradictions between title and requirements | Positive |
| Salary transparency | Explicit base range disclosed, tied to level and geography | Positive |
| Company hiring signals | No 2026-specific layoffs or freeze found; last confirmed layoff was January 2023 (dated); $93M Series D raised May 2025 signals continued active operation and hiring capacity | Positive |
| Reposting pattern | Not found in `data/scan-history.tsv`; this specific req (`540c1dd1...`) has no prior scan history, and is a distinct req from report #146 (`de75aa5e...`, different team, different title) | Neutral |
| Role market context | Entry-level infrastructure reqs at funded, mid-size startups commonly fill within a normal 4-8 week window; nothing here suggests an outlier | Neutral |

**Context notes:** The 48% valuation decline from the 2022 Series C peak to the 2025 Series D is a real, material fact about the company's trajectory, but it is a company-health nuance for equity-value judgment, not a posting-legitimacy concern — the posting itself, application flow, and JD specificity are all unambiguous positive signals.

**6. Employment Classification:** Not flagged — standard full-time employment posting (`#LI-Fulltime`), no contractor-status language.

**7. AI-Buzzword vs. Infrastructure Mismatch:** Not flagged — the JD is a concretely scoped infrastructure/platform role; "AI" appears only in the company's one-line business description ("bring mission-critical software, analytics, and AI to life"), not as an oversold role-level claim. Not applicable.

**8. Benefits/Employment Terminology Country Mismatch:** Not flagged — location is New York City, US, no jurisdiction-mismatched benefits terms found.

## Risk Summary

| Signal | Status |
|--------|--------|
| Posting legitimacy | ✅ High Confidence — live application flow, specific team/tech/scope, salary disclosed, no current layoff signal |
| Employment classification | ✅ clear — standard full-time employment posting |
| Culture screen | — not evaluated (no `culture_screen.require` configured in `config/profile.yml`) |
| Interview red flags | — no interview sessions yet |
| AI claims vs. infrastructure | ✅ consistent — role is concretely scoped infrastructure work, no oversold AI-transformation framing |

---

## Cover Letter Draft

> Draft generated at evaluation time. Complete via `/career-ops cover 183-astronomer` to fill in angles, confirm research, and generate the PDF.
> Gaps flagged below — address them during the cover flow.

---

**Opening** *(placeholder — refine with your "why this role" angle)*
Astronomer's Infrastructure and Systems team owns the unglamorous, essential work of keeping a platform that 800+ enterprises depend on actually running — provisioning, reliability, on-call. That's the exact work I've been doing at TiMoto for the past year, just at a smaller scale.

**Profile introduction**
I'm a Computer Science student at Georgia State (May 2027) currently the primary engineer for backend, cloud infrastructure, and ML serving at TiMoto AI, where I own a production system end-to-end on a 3-person team: multi-AZ AWS infrastructure via Terraform, a full observability stack, and a shared on-call rotation with runbooks I built myself. Before that, I shipped production infrastructure code at Google as a Chrome engineering intern.

**Key achievements** *(selected from cv.md — exact wording preserved)*
- **Multi-AZ ECS Fargate deployment,** sustaining 99.9% uptime and cutting infrastructure cost 44% via Terraform IaC and an auto-rollback circuit breaker pattern.
- **Post-mortem practice with runbooks and a shared on-call rotation,** cutting mean-time-to-identify 68%.
- **Observability stack built from zero at TiMoto,** cutting incident root-cause time to under 15 minutes via Prometheus, Grafana, and CloudWatch.
- **Go CLI contributions to Pulumi,** enabling multi-cloud (AWS/Azure/GCP) provisioning, under active review by core maintainers.

**Problems I will solve** *(placeholder — requires company research + your input)*
> To be completed: are you more drawn to the multi-tenant cloud platform or Astro Private Cloud (the regulated/air-gapped side)? What specific reliability or provisioning challenge would you want to dig into first?

**Closing**
I am happy to discuss further at your convenience.

---

**Gaps flagged:**
- Kubernetes operators/controllers/Helm depth — explicitly "nice to have," not required; be honest if asked, lean on Terraform/ECS Fargate as the closer analog.
- Container security (CVEs, minimal base images) and Apache Airflow familiarity — both explicitly optional, no need to over-address.
- Series D valuation ($775M) is a 48% decline from the 2022 Series C peak ($1.5B) — a real equity-value nuance, not a posting legitimacy issue.

**JD keywords to mirror** *(extracted for ATS + human read)*
Infrastructure and Systems, Astro, multi-tenant cloud platform, Astro Private Cloud, Terraform, Kubernetes, CI/CD, Golang, TypeScript, on-call rotation, observability, networking, Linux fundamentals, AWS, GCP, Azure, distributed systems, production-ready, runbooks

---
*Run `/career-ops cover 183-astronomer` to complete angles, confirm research, and generate the PDF.*

---

## Keywords extracted

Infrastructure and Systems, Astro, DataOps, multi-tenant cloud platform, Astro Private Cloud, Apache Airflow, Terraform, Kubernetes, CI/CD, Golang, TypeScript, on-call rotation, observability, networking, Linux fundamentals, AWS, GCP, Azure, distributed systems, production-ready, runbooks, incident response

## Application Answers

**Date:** 2026-07-20
**State:** filled

### Free-text answers

1. **Please briefly describe your experience with Kubernetes, including years and project types.**

> At TiMoto AI, I originally ran both our backend services and AI/ML serving layer (vLLM-based inference) on AWS EKS. After evaluating the operational tradeoffs, I migrated the production deployment to a multi-AZ ECS Fargate design with Terraform IaC and an auto-rollback circuit breaker pattern -- cutting infrastructure cost 44% while improving stability and scaling flexibility. So my Kubernetes experience covers real production deployment and operation on EKS, plus the judgment to evaluate it against alternatives and choose the right tool for the constraints.

### Selections made

- None captured.

### Other field values

- None captured.

### Files used

- None captured.
