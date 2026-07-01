# Evaluation: Starbucks -- Engineer II, Data Platforms

**Date:** 2026-06-05
**URL:** https://apply.starbucks.com/careers/job/481078117766
**Archetype:** Backend / Distributed Systems Engineer (Java-flavored)
**Score:** 2.8/5
**Legitimacy:** Suspicious (posting CLOSED)
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Backend / Distributed Systems Engineer (Java-flavored) |
| Domain | Enterprise data platforms / retail ops |
| Function | Build -- Java reactive application development |
| Seniority | Engineer II (mid-level; 2+ yrs IT, 3+ yrs Java) |
| Remote | On-site -- Seattle, WA (2401 Utah Ave S) |
| Team size | Not mentioned |
| TL;DR | Java engineer building reactive, scalable backend apps for Starbucks data platforms using Kafka, cloud (AWS/Azure), K8s, and standard SDLC/Agile. |

**Posting Status: CLOSED -- "No longer accepting applications."**
The Playwright snapshot returned an explicit alert: `No longer accepting applications.` No Apply button present. This is a dead posting and the score/evaluation are for informational purposes only.

---

## B) Match with CV

### JD Requirements vs CV

| JD Requirement | Match | CV Evidence |
|----------------|-------|-------------|
| 2+ yrs IT industry experience | Partial | TiMoto AI (Sep 2025--Present) + Google Chrome intern (May--Aug 2025) + Develop for Good (May--Aug 2024) = ~2 yrs combined, still student |
| 3+ yrs Java hands-on | Gap | cv.md Skills: Java listed under Languages, but no Java-specific project or role in CV -- no JD-to-evidence mapping possible |
| Reactive Java (reactive application) | Gap | No reactive Java (Project Reactor, WebFlux, RxJava) experience in cv.md |
| Kafka / event hub / messaging broker | Partial | cv.md Skills: Kafka listed under Distributed Systems skills |
| Linux environment | Match | TiMoto: "deployed... in Cloud based Linux environments" implied via ECS Fargate; AWS infra |
| Java IDE (Eclipse, IntelliJ) | Unverifiable | Not mentioned in cv.md; likely fine operationally |
| Core Java, data structures, collections | Partial | Java in Languages; DSA from coursework (Data Structures coursework listed) |
| SDLC and Scrum | Match | Google Chrome intern: agile code review, backlog, design docs |
| Docker / Kubernetes | Match | cv.md Skills: Docker, Kubernetes; TiMoto: ECS Fargate + K8s-adjacent |
| AWS / Azure deploy | Match | cv.md: AWS (ECS, Fargate, EC2, S3, RDS), GCP; TiMoto: Terraform IaC |
| GitHub / config management | Match | cv.md Skills + Pulumi contributor |
| JBehave / JGiven / Gatling (BDD/load testing) | Gap | No BDD framework or Java load testing experience in cv.md |
| Distributed system application development | Match | TiMoto: gRPC, distributed production systems; Google: IPC/Protobuf |
| Code reviews, design specs | Match | Google Chrome: design docs + 95% test coverage + senior engineer review |
| Waterfall + Agile SDLC | Partial | Agile confirmed (Google internship); no waterfall context |

### Gaps Analysis

| Gap | Type | Mitigation |
|-----|------|------------|
| 3+ years Java hands-on | **Hard (title blocker)** | Harry has Java in skills but zero Java-specific production work in CV. This is the core requirement and there is no strong adjacent evidence. |
| Reactive Java (WebFlux / Reactor) | Hard | No analog in CV -- vLLM/gRPC async is Python/protobuf-flavored, not Java reactive patterns. |
| JBehave / JGiven / Gatling | Soft | BDD testing experience exists (95% test coverage at Google), but with Go/C++/TypeScript, not Java frameworks. Could bridge to "testing philosophy" |
| Waterfall SDLC | Soft | Irrelevant to Harry's trajectory; minor gap |

**Verdict:** Java experience is the foundational requirement (3+ years, named repeatedly) and Harry has none documented. Even if he has written Java in coursework, the CV does not reflect it. This is a structural mismatch, not a polish problem.

---

## C) Level and Strategy

**Level detected:** Engineer II = mid-level IC; JD requires 2+ years IT AND 3+ years Java. Harry has ~2 years total experience (student + internships + TiMoto), and Java is not his demonstrated primary language.

**"Sell senior without lying" plan:**
- This framing doesn't apply: the gap is language-specific (Java) and production-hours-specific, not a seniority/framing problem.
- Even aggressive positioning would not close the "3+ years Java" requirement.
- Harry's strengths (C++, Go, TypeScript, Python, distributed systems, ML infra) are not what this JD is buying.

**If downleveled:** Irrelevant -- role is closed. If it reopened, Harry would need to either skip it or document Java project work first.

---

## D) Comp and Demand

**Posted range:** $111,000 -- $185,000/annually (Bonus Eligible)

| Metric | Finding | Source |
|--------|---------|--------|
| Posted base | $111K -- $185K | JD snapshot |
| Entry-level Java SWE Seattle | $120K -- $155K base | Glassdoor estimates (Java Engineer II, Seattle) |
| Harry's minimum | $140K | profile.yml |
| Comp floor risk | Low end ($111K) is well below Harry's $140K minimum | -- |
| Comp ceiling | $185K is within Harry's $150K--$200K target range | -- |
| Bonus eligible | Yes (amount undisclosed) | JD |
| Sponsorship | Not mentioned in JD | -- |

**Note:** Starbucks Technology historically pays below FAANG but within large-enterprise bands. The $111K floor is a concern; the $185K ceiling is fine for mid-level. Without more specific Engineer II data at Starbucks, the actual median offer is likely $130K--$155K -- borderline for Harry's $140K minimum.

---

## E) Customization Plan

Not applicable -- posting is CLOSED. For reference only if role reopens.

| # | Section | Current Status | Proposed Change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | Summary | Python/Go/C++ oriented | Add Java production reference OR acknowledge gap | JD is Java-primary; honest framing needed |
| 2 | Skills | Java listed under Languages | Move Java up or add a Java project | "Java" buried in Languages row is weak vs 3+ years requirement |
| 3 | Experience | No reactive Java context | Could frame gRPC async patterns as adjacent concurrency model | Weakest mitigation; would need actual Java Reactor/WebFlux work |
| 4 | Projects | No Java projects visible | Add a Java project (Spring Boot, reactive pipeline) | The fastest way to close the gap -- if role mattered |
| 5 | LinkedIn | General | Java keyword surface in Skills | ATS keyword optimization |

---

## F) Interview Plan

Role is closed so full STAR prep is deprioritized. Documenting key story mappings for any future Java backend opportunity at Starbucks or similar enterprise.

| # | JD Theme | STAR+R Story | S | T | A | R | Reflection |
|---|----------|-------------|---|---|---|---|------------|
| 1 | Distributed system development | gRPC Deadlock Fix (TiMoto) | Concurrent gRPC calls causing production deadlocks | Debug + eliminate under load | Traced lock acquisition conflicts; redesigned call sequencing | 100% eval success rate, sub-50ms p99 | Always diagram lock ordering before concurrency goes live |
| 2 | Scalable application + testing frameworks | Chrome lock-free trie | Settings p99 at 1,200ms | Reduce latency without regression | Lock-free concurrent trie + linearizability proof | 96% latency reduction, shipped to stable | Correctness proof first, then benchmark |
| 3 | Kafka / event-driven | TiMoto event-driven architecture | Multiple async ML serving components | Decouple services to avoid cascading failure | Event-driven architecture with circuit breakers | 99.9% uptime, 44% cost reduction | Circuit breakers are ops insurance, not optionality |
| 4 | AWS/Azure deploy | TiMoto multi-AZ ECS | Single-AZ with no failover | Design HA topology | Multi-AZ ECS Fargate + Terraform + CloudWatch auto-rollback | 99.9% uptime | Infra-as-code is the safety net for day-2 ops |
| 5 | Code reviews + design docs | Google Chrome design docs | IPC design decision (Protobuf vs custom) | Produce reviewable design doc for senior Chrome engineers | Documented schema-evolution tradeoffs; reviewed by senior team | Shipped to stable channel | Design decisions are clearest when the rejected alternatives are explained |

**Recommended case study:** TiMoto AI (timoto.ai) -- demonstrates distributed production systems, cloud infra, and ML serving in production. Less relevant to Java-reactive framing but shows production engineering maturity.

**Red-flag questions (if role reopens):**
- "You have Java in your skills but no Java production work -- tell me about your Java experience." → Be direct: Java in coursework (GSU Data Structures / projects), not production-scale. Emphasize rapid ramp: shipped C++ to Chrome in 3 months, gRPC system at TiMoto in 4 months. Ask about onboarding support for language ramp.
- "Why are you applying if you're a new grad with 2027 graduation?" → TiMoto production work closes much of the experience gap; note engineer responsibilities, not student title.

---

## G) Posting Legitimacy

**Assessment: Suspicious (CLOSED)**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button active | CLOSED -- explicit alert: "No longer accepting applications." | Concerning (hard negative) |
| Posting age | No date available in snapshot; job ID 260032434 | Neutral |
| Description quality | Specific technologies (Java, Kafka, JBehave, Gatling, Docker/K8s, AWS/Azure); somewhat boilerplate in preferred section | Positive |
| Salary disclosed | Yes ($111K--$185K) | Positive |
| Company hiring signals | Starbucks Technology had April 2026 tech reorg (61 non-SWE cuts per report #064); this is SWE so different department | Neutral |
| Reposting in scan-history | No prior Starbucks Data Platforms entries in scan-history.tsv | Neutral |
| Job category | "Retail Operations" (not Technology) -- enterprise IT function, not product engineering | Neutral |
| Same company, same day | Third Starbucks role evaluated today (#064 Seattle SWE, #065 Nashville SWE, #066 this) | Neutral (batch scan) |

**Summary:** The posting is definitively closed. No application is possible at this time. If the role reopens, the Java experience gap and comp floor risk ($111K low end) are the two structural concerns.

**Context Notes:** Starbucks Technology is a large enterprise IT org. This category of posting ("Retail Operations" under Technology) fills cyclically for delivery of POS/ordering/data systems. Role may reappear with a new job ID.

---

## Keywords Extracted (ATS reference for future Java opportunities)

Java, reactive application, Kafka, event hub, messaging broker, JBehave, JGiven, Gatling, Linux, Kubernetes, Docker, AWS, Azure, distributed systems, CI/CD, GitHub, Agile, Scrum, SDLC, scalable applications, core Java, data structures, circuit breaker, continuous build, integration testing, code reviews, technical design specifications, backlog refinement, waterfall

---

## Machine Summary

```yaml
report: "066"
company: "Starbucks"
role: "Engineer II - Data Platforms"
date: "2026-06-05"
score: 2.8
archetype: "Backend / Distributed Systems Engineer (Java)"
legitimacy: "Suspicious"
posting_status: "CLOSED"
location: "Seattle, WA (on-site)"
comp_range: "$111K-$185K base"
comp_floor_risk: true
visa_sponsorship: "unconfirmed"
f1_risk: true
top_gap: "3+ years Java production experience (not in CV)"
recommendation: "SKIP -- posting closed; Java gap is structural"
```
