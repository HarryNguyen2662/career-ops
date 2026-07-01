# Evaluation: Snowflake — Software Engineer, Secret, Cryptographic and Identity Infrastructure (SCII)

**Date:** 2026-06-12
**URL:** https://careers.snowflake.com/us/en/job/SNCOUS90B6253AC6CE4D27AA4BC6C927C4B525EXTERNALENUSEB7042104C4A4AB788388BA7ABD55AF3/Software-Engineer-Secret-Cryptographic-and-Identity-Infrastructure
**Archetype:** Platform / Cloud Infrastructure Engineer + Backend / Distributed Systems Engineer
**Score:** 3.8/5
**Legitimacy:** High Confidence
**PDF:** output/122-snowflake-software-engineer-scii-harry-nguyen-2026-06-12.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Platform / Cloud Infrastructure + Security Automation — build foundational security systems that let Snowflake engineers deliver a secure Data Cloud; secret management, key management, service identity, E2EE |
| Domain | Snowflake SCII (Secret, Cryptographic and Identity Infrastructure) — internal platform security; builds tooling, enforcement pipelines, developer-facing security automation across natively multi-cloud environment |
| Function | Build — software systems, security tooling, automation/self-service, core security infrastructure |
| Seniority | Not explicitly stated — no years-of-experience requirement in JD; bonus points framing suggests accessible to strong new grads / junior engineers with production experience |
| Location | Bellevue, WA |
| Comp | **$160,000–$230,000 base + bonus + equity** — Snowflake IC1 median TC ~$237K+ (Seattle, Levels.fyi 2026) |
| Company | Snowflake — fast-growing Data Cloud; "agentic enterprise" strategic direction at Snowflake Summit 2026; SCII is foundational internal infrastructure team |
| TL;DR | No explicit years requirement; languages, AWS/Kubernetes, reliability/scale all land as bonus points; security infrastructure gap (secrets management, key management, E2EE) is real but JD is written for engineers who want to learn the security layer. Comp is excellent. Score 3.8 — apply with honest framing. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| **BS in CS or equivalent** | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ Direct |
| **Hands-on experience: JavaScript, Java, Python, C, C++, Go, or Rust** | CV: Python, C++, Go, TypeScript (JS-adjacent), Rust — 5 of the 7 listed languages | ✅ Strong — multiple required languages covered |
| Strong communication, cross-team collaboration | Chrome: delivered design docs adopted by senior engineers; worked with Chrome infra team across functions | ✅ Demonstrated |
| Genuine interest in security and reliability at scale | TiMoto: 99.9% uptime SLO, circuit breakers, auto-rollback, fault tolerance; Chrome: zero production regressions to 3B+ users | ✅ Reliability at scale is direct evidence |
| **Experience designing, building, testing, maintaining reliable, scalable software (bonus)** | TiMoto: primary engineer for distributed production systems (gRPC, ECS Fargate, Terraform, CloudWatch); Chrome: 25K+ Chromium lines at 95% test coverage; Develop for Good: CI/CD, auto-scaling | ✅ Strong bonus hit |
| **Experience with Kubernetes (bonus)** | CV skills: AWS (ECS Fargate, **EKS**), Kubernetes, Docker | ✅ Direct bonus hit |
| **Production services on AWS, Azure, or GCP (bonus)** | TiMoto: AWS ECS Fargate + RDS + CloudWatch; Develop for Good: AWS BaaS with auto-scaling; Terraform IaC provisioning multi-AZ | ✅ Strong bonus hit |
| **Familiarity with SSDLC / security infrastructure: secret management, service identity, auth/authz (bonus)** | Develop for Good: JWT auth for stateless horizontal scale; TiMoto: gRPC service-to-service + circuit breakers; Terraform IAM provisioning; Chrome: 95% test coverage at Google's security review bar | ⚠️ Adjacent — no direct experience with HSMs, SPIFFE/SPIRE, certificate authorities, or key management systems |
| Multi-cloud environment design | Snowflake is natively multi-cloud; Harry: AWS primary, GCP in skills, Pulumi for multi-cloud IaC | ✅ Directly relevant via Pulumi + AWS depth |
| Automation and self-service tooling | TiMoto: LLM-as-a-judge automated evaluation pipeline; Develop for Good: 90% deployment time reduction via CI/CD (GitHub Actions) | ✅ Automation/self-service pattern direct hit |
| On-call rotations, production health | TiMoto: on-call rotation, incident triage, runbooks, post-mortems | ✅ Direct |
| Design reviews and code reviews | Chrome: design docs + code reviews adopted by senior Chrome engineers; TiMoto: primary engineer owns architectural decisions | ✅ Direct |

**Gaps:**

1. **Security infrastructure domain depth (moderate gap):** SCII's core work is secrets management (e.g., HashiCorp Vault, AWS Secrets Manager), key management (HSMs, KMS), service identity (SPIFFE/SPIRE, mTLS), and E2EE (customer data encryption). Harry has JWT auth and gRPC service-to-service — secure patterns but not cryptographic infrastructure. This is the learning curve entering SCII, not a blocker (the JD says "genuine interest" not "deep expertise").

2. **Grad year / experience timeline (soft gap):** May 2027 graduation with ~9 months non-internship experience. No explicit years requirement in JD — this is the key difference from the Amazon Payments role. Snowflake's "bonus points" section implies they'll accept candidates who meet most but not all preferred criteria.

3. **Multi-cloud breadth (minor):** Harry is AWS-strong but Azure is absent and GCP is listed in skills without specific proof points. Snowflake is genuinely multi-cloud across AWS/Azure/GCP. Not a blocker but worth acknowledging.

---

## C) Level and Strategy

**Level detected:** IC1 (entry/junior) — no explicit experience requirement; bonus points framing is accessible; comp range ($160K–$230K base) is at the low end of Snowflake's IC2+ range, suggesting IC1/IC2. Snowflake IC1 base typically $160K–$190K.

**Core pitch:**
> "I build reliable distributed infrastructure at production scale — 99.9% uptime SLO with circuit breakers and multi-AZ failover on AWS, using Terraform IaC. My Pulumi open-source contributions demonstrate multi-cloud (AWS/Azure/GCP) provisioning expertise. At Google, I shipped code to 3B+ users at Google's security review standard — 95% test coverage, zero regressions. I'm genuinely interested in learning the security layer from the inside: I understand service-to-service communication (gRPC, Protobuf) and infrastructure provisioning (Terraform, IAM) — SCII is the natural extension into secret management and identity."

**Why SCII specifically:**
> "SCII sits at the infrastructure layer I know well — you're building software systems that other engineers depend on, with reliability and security as first-class constraints. That's the same discipline as what I built at TiMoto: production infrastructure that cannot fail, with automated enforcement instead of manual checks."

**If asked about security depth:**
> "I don't come with a deep cryptographic background, but I know the patterns that surround it — JWT auth, service-to-service trust via gRPC, infrastructure IAM via Terraform. I want to learn secrets management, key management, and service identity from the team that builds it for one of the largest data platforms in the world. That's the right place to develop that expertise."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Snowflake stated base | $160,000–$230,000 |
| Bonus | Variable; Snowflake equity-heavy comp |
| Equity (IC1 RSU) | Snowflake IC1 TC median ~$237K+ (Seattle, Levels.fyi 2026); IC1 base typically $160K–$190K, RSUs substantial |
| Estimated TC | **$220K–$300K** at IC1/IC2 depending on equity grant |
| Harry target | $150K–$200K TC |
| Harry minimum | $140K |
| Assessment | Strongly exceeds Harry's target. Base alone ($160K–$230K) exceeds the $150K target. IC1 TC at Snowflake (~$237K+) well above the $200K ceiling of Harry's range. Outstanding comp for any level. |
| Snowflake H-1B sponsorship | Confirmed — h1bgrader.com shows Snowflake Inc. H-1B filings FY 2026; Snowflake actively sponsors. SCII is a high-value infrastructure team — sponsorship should be available. |
| Snowflake hiring health | Snowflake is post-IPO growth phase; announced major AI/agentic strategy at Snowflake Summit 2026; SCII as foundational security team is stable hiring through product expansion |

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Experience order | TiMoto first (default) | **TiMoto first** — lead with reliability + infra angle, not ML serving | SCII values platform reliability and infrastructure; 99.9% uptime + circuit breakers + Terraform is the core pitch |
| 2 | TiMoto bullets | ML serving lead | **Lead with infrastructure reliability**: "Architected multi-AZ ECS Fargate with Terraform IaC, circuit breaker pattern, auto-rollback on health check failure — 99.9% uptime SLO; CloudWatch + Prometheus/Grafana observability; triaged incidents via root-cause analysis, runbooks, post-mortem; 44% cost reduction" | JD: "reliable, scalable software" + "on-call rotations" + "keep critical systems healthy" |
| 3 | TiMoto bullets | LLM-as-a-judge later | Second bullet: gRPC inter-service layer (service-to-service security patterns) | JD: "service identity, authentication" — gRPC + exactly-once delivery is the closest analog to service identity |
| 4 | Develop for Good | JWT buried | Surface JWT auth explicitly: "selected JWT over session auth for stateless horizontal scalability — secure auth design choice" | JD: "authentication" in security infrastructure; "familiarity with auth/authz" is bonus point |
| 5 | Skills row order | Distributed Systems first | **Cloud & Infrastructure first** (AWS ECS/EKS/K8s/Terraform/CI-CD); Distributed Systems second; Languages third (Python/Go/C++ prominent) | Bonus points are Kubernetes + AWS; recruiter will scan these first; security infra team cares about cloud-native tooling |

---

## F) Interview Plan

| # | JD Area | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Reliable, scalable infrastructure | TiMoto multi-AZ + circuit breaker design | Production single-AZ, no failover, no automated recovery | Architect for production-grade reliability | Designed multi-AZ ECS Fargate; added circuit breaker pattern with auto-rollback on health check failure; set up CloudWatch alarms | 99.9% uptime SLO; 44% cost reduction; zero manual intervention needed on health failures | Security infrastructure requires the same discipline as reliability infrastructure — if the circuit breaker fires on a secret rotation failure, the system needs to degrade gracefully, not cascade fail |
| 2 | Automation / self-service tooling | TiMoto LLM-as-a-judge + Develop for Good CI/CD | Manual review before deployment didn't scale; manual deploy process was slow | Automate quality enforcement and deployment | Built LLM-as-a-judge automated assessment pipeline; Develop for Good: automated GitHub Actions CI/CD (90% deploy time reduction) | Automated regression detection; no manual review bottleneck; 90% faster deploys | Self-service security tooling follows the same pattern — when enforcement is automated and invisible, engineers adopt it without friction. When it requires manual steps, they route around it |
| 3 | Secure backend code + design reviews | Chrome C++ IPC transport | Chrome settings needed new IPC serialization | Design and ship production C++ data transport at Google's security bar | Evaluated Protobuf vs custom serialization (security angle: schema evolution prevents breaking changes that create security gaps); shipped to Chrome stable with senior review | Sub-50ms p99, 3B+ users, zero regressions, 95% test coverage | Security review at Google's standard means every change must have a threat model — what can break, what's the rollback, what's the test coverage. That's the mindset I'd bring to SCII |
| 4 | Service-to-service communication (proto-auth/authz) | TiMoto gRPC deadlock root-cause | Production deadlock under concurrent gRPC calls | Find and fix root cause of concurrent service failure | Traced shared resource acquisition conflicts; redesigned call sequencing for exactly-once delivery | 100% evaluation success rate; zero deadlocks post-fix | Service-to-service trust is about knowing who called what and in what order. Debugging deadlocks in concurrent gRPC taught me that the service identity model (who is allowed to call whom, in what sequence) is as important as the authentication mechanism |
| 5 | Multi-cloud / Kubernetes / AWS | TiMoto + Pulumi | Production infrastructure on AWS; contributed multi-cloud IaC to Pulumi | Build cloud-native infra + contribute to multi-cloud tooling | Deployed ECS Fargate with Terraform; Kubernetes in AWS (EKS); contributed Go CLI features for AWS/Azure/GCP provisioning to Pulumi | 99.9% uptime; Pulumi contributions under active review | Snowflake's multi-cloud-native architecture is exactly the environment Pulumi addresses. My contributions give me a bottom-up understanding of how multi-cloud provisioning works — not just as a user, but as a contributor |

**Recommended case study:** TiMoto infrastructure design — walk through the reliability architecture (multi-AZ, circuit breakers, observability) and connect it to the SCII problem: "reliable infrastructure for security tooling that cannot fail." Comp: Snowflake's SCII is building the equivalent of what Terraform + circuit breakers provides for reliability, but for secrets and identity.

**Red-flag questions:**
- *"No cryptographic or security infrastructure background."* → "Correct — my security exposure is at the engineering discipline level (secure coding at Google's standard, JWT auth, service-to-service gRPC trust) rather than the cryptographic layer. SCII is building the infrastructure that enables security — and that's 80% distributed systems, automation, and reliability engineering, which is exactly my background. The 20% that's domain-specific (key management, SPIFFE, HSMs) I'd learn from the team that builds it best."
- *"When would you be available?"* → "May 2027 graduation — I have F-1 status with OPT eligible then and will need H-1B sponsorship long-term. Can you confirm Snowflake sponsors for this team?"
- *"Grad year 2027 — this is a full-time role."* → "Correct — applying for the May 2027 start. If there's a fall 2026 intern cohort on SCII, that would also be of interest."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active "APPLY NOW" on Snowflake careers — confirmed via Playwright | Positive |
| Comp disclosed | $160,000–$230,000 base + bonus + equity — transparent | Positive |
| JD specificity | Named team (SCII), specific ownership areas (E2EE, secret management, key management, service identity), specific multi-cloud context | Positive |
| Req ID | REQ19880 — valid Snowflake Req ID format | Positive |
| Similar jobs shown | "Senior Software Engineer, Identity & Access Management" also posted at Bellevue — the team is actively hiring across levels | Positive |
| Snowflake hiring health | Snowflake announced agentic enterprise strategy at Summit 2026; SCII as foundational security team is stable; Snowflake also showing Fall 2026 intern postings on the same team | Positive |

**Context:** No concerns. Snowflake's SCII team has multiple active openings (this role + Senior IAM), both at Bellevue. The posting is specific, comp-transparent, and matches Snowflake's known hiring patterns.

---

## Keywords extracted

Software Engineer, SCII, secret management, cryptographic infrastructure, identity infrastructure, security tooling, multi-cloud, Snowflake, E2EE, end-to-end encryption, key management, service identity, authentication, authorization, Kubernetes, AWS, GCP, Azure, Terraform, Python, Go, C++, Rust, reliability, scalable systems, on-call, Bellevue, security policy enforcement, automation

---

## Machine Summary

```yaml
company: Snowflake
role: "Software Engineer - Secret, Cryptographic and Identity Infrastructure (SCII)"
date: 2026-06-12
url: https://careers.snowflake.com/us/en/job/SNCOUS90B6253AC6CE4D27AA4BC6C927C4B525EXTERNALENUSEB7042104C4A4AB788388BA7ABD55AF3/Software-Engineer-Secret-Cryptographic-and-Identity-Infrastructure
score: 3.8
archetype: "Platform / Cloud Infrastructure + Backend / Distributed Systems Engineer"
location: "Bellevue, WA"
comp_range: "$160,000–$230,000 base + bonus + equity; Snowflake IC1 TC median ~$237K+ Seattle; strongly exceeds Harry's $150K–$200K target"
visa_risk: "F-1 — Snowflake sponsors H-1B (h1bgrader FY2026 confirmed); SCII high-value infra team; sponsorship should be available"
legitimacy: High Confidence
recommendation: "Apply (3.8/5) — no explicit years requirement; languages (Python/Go/C++/Rust), AWS/Kubernetes, reliability at scale all land as bonus points; security domain gap is real but JD is written for engineers who want to learn the layer; comp is exceptional. Pitch: production infrastructure reliability + multi-cloud IaC experience + genuine interest in building the security foundation."
```
