# Evaluation: Starbucks -- Software Engineer (ST, Nashville TN)

**Date:** 2026-06-05
**URL:** https://apply.starbucks.com/careers/job/481078166214-software-engineer-st-nashville-tn-nashville-tennessee-united-states
**Archetype:** Platform / Cloud Infrastructure Engineer (primary) + Site Reliability Engineer (secondary)
**Score:** 3.0/5
**Legitimacy:** Proceed with Caution
**PDF:** output/065-starbucks-nashville-harry-nguyen-2026-06-05.pdf

---

## A) Role Summary

| Dimension | Detail |
|-----------|--------|
| Archetype | Platform / Cloud Infrastructure Engineer + SRE hybrid |
| Domain | Developer enablement, reliability, observability, security |
| Function | Build / operate / automate |
| Seniority | IC, 0-4 yrs exp (entry-to-mid) |
| Remote | In-Office 4 days/week -- Nashville, TN |
| Team | Starbucks Technology ("ST") org -- Nashville hub |
| TL;DR | Entry-level SWE/SRE-adjacent role focused on build+release pipelines, service monitoring, and security compliance in Starbucks' tech org; Nashville in-office 4d/wk, pay band $83K-$164K. |

**Role flavor:** This is an internal platform/reliability engineering role -- not product engineering. The work is squarely in build tooling, observability, incident response, and security posture. It is closer to SRE/DevOps/Platform than to a backend or systems software product role. The JD is deliberately generic -- no specific stack, no team name, no project context.

---

## B) Match with CV

| JD Requirement | Harry's Match | CV Source |
|----------------|---------------|-----------|
| 0-4 yrs professional SW dev | ~1.5 yrs (TiMoto Sep 2025-present + 2x internships) | cv.md -- Experience section |
| BS in CS or related | Georgia State CS, GPA 3.75, expected May 2027 | cv.md -- Education |
| Systems/network admin + production support (monitoring/telemetry, incident response, on-call) | Strong -- multi-AZ ECS ops, CloudWatch observability, circuit breaker, auto-rollback, on-call rotation at TiMoto | cv.md -- TiMoto bullet 4: "Maintained distributed production systems... participated in on-call rotation" |
| Automation + coding (Python, Java, Go, C/C++) | Strong -- Python, Go, C++, Java all on CV; scripting for automation | cv.md -- Skills: Languages |
| AWS/Azure, CI/CD, build/release tooling | Strong -- AWS ECS Fargate, Terraform, CI/CD GitHub Actions, CloudWatch, Prometheus, Grafana | cv.md -- TiMoto infra bullet; Skills: Cloud & Infrastructure |
| Distributed systems, TCP/IP networking, databases (SQL/NoSQL) | Strong -- distributed systems coursework + gRPC production; PostgreSQL + Redis in prod | cv.md -- Education coursework; TiMoto experience; Develop for Good |
| Service monitoring + deep telemetry | Good -- CloudWatch + Prometheus + Grafana stack; 99.9% uptime | cv.md -- TiMoto infra bullet |
| Security + compliance foundations | Indirect -- not explicitly in CV (gap) | N/A |
| Fast/reliable delivery, build/release processes | Partial -- CI/CD (GitHub Actions, 90% deploy time reduction); no dedicated build-tooling project | cv.md -- Develop for Good |

**Gaps:**

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| Security / compliance engineering | Nice-to-have | Adjacent: infrastructure hardening (circuit breakers, health checks); mention security-minded config in AWS setup |
| Named build/release tooling (Jenkins, Tekton, Argo, etc.) | Nice-to-have | Terraform + GitHub Actions CI/CD covers the spirit; call out explicitly in cover letter |
| Enterprise-scale org (vs startup) | Nice-to-have | Frame Google Chrome internship -- shipped to 3B users, worked with Chrome infra team |
| Graduated May 2027 (still in school) | Low risk | 0-4 yr band is inclusive; state start date as May 2027 on application |
| F-1 / sponsorship | Risk | Starbucks is a large employer; F-1 OPT covers initial tenure; H-1B sponsorship policy unclear -- ask recruiter early |

**Summary:** Technical skill overlap is excellent for the preferred qualifications. The role is broader/more ops-flavored than Harry's primary backend/systems pitch but his TiMoto production SRE experience (CloudWatch, multi-AZ, circuit breakers, on-call) maps directly. The main friction is role direction (infra ops vs. systems performance) and comp floor risk.

---

## C) Level and Strategy

**Level detected:** IC entry-level (0-4 yrs). The JD says "Individual Contributor" and the 0-4 yr band puts this at L25/L26 at Starbucks' internal levels.

**Harry's natural level for this archetype:** Entry-level to early-mid SWE -- aligned. He is a new grad (May 2027) with meaningful production infra experience.

**Sell senior without lying:**
- Lead with TiMoto's production scope: owned backend + cloud infra + ML serving end-to-end on 3-person team -- that is a larger operational surface than most entry-level SWEs at enterprises.
- Quantify observability: "CloudWatch + Prometheus telemetry across gRPC, ECS, and ML serving layers; participated in on-call rotation with runbooks and post-mortems."
- Frame Google internship for enterprise credibility: "changes adopted into production branch reviewed by senior Chrome engineers at 95% test coverage."
- Use the Terraform IaC angle: automated multi-AZ infra, health-check-driven auto-rollback, 44% cost reduction -- this is exactly "engineer build and release processes."

**If they downlevel / offer below range:**
- The $83K floor is well below Harry's $140K minimum. If the offer comes in below $140K, decline.
- If offer is $140K+, negotiate toward $155K base citing equivalent Nashville market rate for SWE with production infra experience.

---

## D) Comp and Demand

| Data Point | Value | Source |
|------------|-------|--------|
| JD posted range | $83,300 -- $163,800 base | Starbucks posting |
| Levels.fyi Starbucks SWE (US median) | $140K TC (L25 median ~$160K) | levels.fyi |
| Glassdoor Starbucks SWE avg | $147,834/yr (range $118K-$188K) | Glassdoor, Nov 2025 |
| 6figr Starbucks SWE 2026 | $144K-$265K | 6figr.com |
| Harry's minimum | $140K | profile.yml |
| Harry's target | $150K-$200K TC | profile.yml |

**Assessment:**
- The posted floor ($83K) is a wide low-anchor typical of large employers. The actual midpoint for a production-experienced new grad should land $130K-$155K.
- Nashville has ~10-15% lower COL vs Seattle; Starbucks' Nashville ST hub opened as a lower-cost alternative to Seattle HQ.
- **Risk:** the comp floor is below Harry's $140K minimum. It is possible an entry-level hire in Nashville is offered $110K-$130K base, which would be a no-go.
- Demand: SRE/platform engineering roles remain in strong demand. Starbucks' Nashville expansion (tech hub) signals active hiring in that market.

**Verdict:** Comp is a meaningful risk. Proceed only if willing to push hard on negotiation and can confirm $140K+ is achievable for this level in Nashville.

---

## E) Customization Plan

| # | Section | Current Status | Proposed Change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Summary | Distributed systems / ML serving focus | Shift to: "Production SWE with infra ownership -- CloudWatch telemetry, multi-AZ ECS, CI/CD automation, on-call at TiMoto AI; Google Chrome at 3B-user scale" | Matches reliability + observability emphasis of JD |
| 2 | TiMoto bullet 4 | "Maintained distributed production systems... participated in on-call rotation" | Expand: add "triaged incidents via runbooks and post-mortems; CloudWatch + Prometheus telemetry across gRPC, ECS, and ML serving layers" | Mirrors JD's "monitoring, troubleshooting, incident response" language exactly |
| 3 | TiMoto infra bullet | "Architected multi-AZ ECS Fargate with Terraform IaC" | Add: "GitHub Actions CI/CD pipeline with automated rollback on health-check failure -- 44% infra cost reduction" | JD explicitly asks for CI/CD + build/release tooling |
| 4 | Develop for Good bullet | "Designed stateless BaaS on AWS -- CI/CD 90% deployment time reduction" | Emphasize: "GitHub Actions CI/CD; auto-scaling policy for 500+ concurrent users" | More build/release resonance |
| 5 | Skills section | Cloud & Infrastructure row lists AWS, Terraform, K8s | Reorder to lead with observability tools: "CloudWatch, Prometheus, Grafana, AWS ECS/EKS, Terraform, CI/CD" | Observability is the first JD priority |

**Top 5 LinkedIn changes:**
1. Headline: add "SRE / Platform Infra" alongside "Distributed Systems"
2. TiMoto summary: call out on-call rotation + incident response explicitly
3. Featured section: link to GitHub with Terraform/infra work
4. Skills: pin Prometheus, Grafana, CI/CD, Incident Response to top
5. About section: add "build systems that stay up and stay cheap" framing

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---------------|--------------|---|---|---|---|------------|
| 1 | Service monitoring + telemetry | TiMoto -- CloudWatch + Prometheus infra | 3-person team, no SRE specialist | Own full observability stack across gRPC + ECS + ML serving | Set up CloudWatch dashboards, Prometheus scrape configs, Grafana alerts | 99.9% uptime; caught 2 production incidents before user impact | Would add distributed tracing (Jaeger/OpenTelemetry) earlier -- helped on deadlock diagnosis |
| 2 | Incident response + troubleshooting | TiMoto -- gRPC deadlock under concurrent calls | Production: 100% eval failure rate at spike | Tasked with diagnosing and fixing latency + failure spike | Traced shared resource acquisition conflict; redesigned call sequencing | 100% success rate, sub-50ms p99 restored | Learned to instrument lock acquisition paths proactively, not reactively |
| 3 | Build/release process | Develop for Good -- CI/CD GitHub Actions | Nonprofit org, no automated deploy pipeline | Build automated deploy pipeline for AWS BaaS | Designed GitHub Actions workflow; wrote deployment scripts; added auto-scaling policy | 90% deployment time reduction; supported 500+ concurrent users | Would add staging environment + smoke tests -- deployed straight to prod initially |
| 4 | Automation + scripting | TiMoto -- Terraform IaC for AWS infra | Manual infra changes causing drift | Automate full ECS + VPC + RDS stack provisioning | Wrote modular Terraform with remote state in S3; added circuit breaker + health checks | Auto-rollback on health check failure; 44% cost reduction ($40-60/mo) | Parameterizing environment configs earlier would have saved rework |
| 5 | Distributed systems + reliability | TiMoto -- vLLM inference engine | OOM failures under concurrent LLM inference | Deploy production-grade LLM serving | Selected vLLM/PagedAttention over naive inference; deployed with continuous batching | Zero OOM failures at production traffic | Benchmarked multiple serving backends before deciding -- would recommend this process more broadly |
| 6 | Large-scale build confidence | Google Chrome -- C++ IPC transport layer | Chrome stable release cycle | Ship IPC layer to billions of users at sub-50ms p99 | Designed with Protobuf for schema evolution; went through design doc + senior review | Shipped to stable channel, 3B+ active users | Enterprise process (design docs, senior review cycles) slows delivery but caught 2 correctness issues pre-ship |

**Case study to present:** TiMoto AI production ML serving stack -- demonstrates end-to-end infra ownership (Terraform, ECS, observability, CI/CD, on-call) which maps directly to this role's scope. Offer a 5-minute walkthrough of the architecture.

**Red-flag Q&A:**
- "You're still in school -- can you start?" → "I'm graduating May 2027 and targeting full-time roles for that cohort. I'm available for internship positions earlier if the timing works."
- "This seems more ops-heavy than your background -- are you comfortable with on-call?" → "Yes. At TiMoto I'm already on the on-call rotation. I wrote the runbooks, investigated incidents, and applied post-mortem learnings -- production reliability isn't new to me."
- "Do you need sponsorship?" → Use negotiation script from _profile.md: confirm F-1, OPT eligibility, ask about H-1B.

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|--------|---------|--------|
| Posting date | Posted 05/05/2026 -- 31 days ago | Neutral (at the 30-day line) |
| Apply button | Active -- "Apply Now" link confirmed via Playwright | Positive |
| Expiration date | Shows 12/31/1969 (Unix epoch zero) -- bad data field, not a real expiry | Neutral (system artifact) |
| JD specificity | Very low -- no team name, no stack, no product context; generic SWE/ops description | Concerning |
| Tech reorg context | April 2026: 61 tech jobs cut at Seattle HQ under new CTO Varadarajan (Amazon hire) | Concerning |
| Layoff dept overlap | Cuts were cybersecurity analysts, TPMs, sysadmins, scrum masters, architects -- similar ops/infra tier to this role | Concerning |
| Nashville context | Starbucks ST (Starbucks Technology) Nashville hub is an active expansion site -- multiple Nashville roles posted simultaneously | Positive |
| Similar jobs visible | Sr SWE Nashville, data engineer Nashville, app developer Nashville all posted 1+ months ago -- active Nashville hiring | Positive |
| Salary range width | $83K-$163K is an 88K spread -- unusually wide, often used for pooled/evergreen postings | Neutral-Concerning |
| Reposting | No prior Starbucks Nashville SWE in scan-history.tsv | Neutral |

**Context Notes:**
- The April 2026 cuts were at Seattle HQ; this role is in Nashville. The Nashville hub appears to be the receiving end of the reorganization -- Starbucks may be shifting tech headcount from Seattle to lower-cost Nashville. This is a plausible legitimate reason for simultaneously posting multiple Nashville roles.
- The very generic JD may reflect a large-employer template approach rather than a ghost posting.
- New CTO joined from Amazon in December 2025 -- first reorg action in April, Nashville expansion ongoing. Hiring could be part of the post-reorg team rebuild.
- Recommended action: verify Nashville role is still actively interviewing before investing significant application prep time. The active Apply button is a positive signal.

---

## Keywords Extracted

`software engineer`, `build and release`, `CI/CD`, `observability`, `telemetry`, `monitoring`, `incident response`, `on-call`, `automation`, `scripting`, `Python`, `Go`, `C++`, `AWS`, `Azure`, `distributed systems`, `TCP/IP`, `DNS`, `PostgreSQL`, `NoSQL`, `infrastructure`, `security`, `compliance`, `high-availability`

---

## Machine Summary

```yaml
report: "065"
company: "Starbucks"
role: "Software Engineer (ST, Nashville TN)"
score: 3.0
archetype: "Platform / Cloud Infrastructure Engineer + SRE hybrid"
legitimacy: "Proceed with Caution"
location: "Nashville, TN"
remote: "In-Office 4d/wk"
comp_range: "$83,300--$163,800 base (employer-posted)"
visa_sponsorship: "Likely (Starbucks sponsors H-1B; Nashville-specific unconfirmed)"
key_gap: "Comp floor risk -- Nashville new grad likely $110K--$130K, below $140K minimum; JD very generic; tech reorg context"
recommendation: "Apply with caution -- strong technical fit (infra/SRE overlap), but comp and location are meaningful blockers; confirm salary band + sponsorship before investing time"
date: "2026-06-05"
```
