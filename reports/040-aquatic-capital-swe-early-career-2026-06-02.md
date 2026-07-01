# Evaluation: Aquatic Capital Management -- Software Engineer, Early Career

**Date:** 2026-06-02
**URL:** https://job-boards.greenhouse.io/aquaticcapitalmanagement/jobs/8489226002
**Archetype:** Backend / Distributed Systems Engineer (primary) + Systems Software Engineer (hybrid)
**Score:** 4.4/5
**Legitimacy:** High Confidence
**PDF:** output/040-aquatic-capital-swe-early-career-harry-nguyen.tex (LaTeX)

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Backend / Distributed Systems Engineer + Systems Software Engineer |
| **Domain** | Quantitative finance -- research & trading infrastructure |
| **Function** | Build -- full-time, rotation through 2--3 tech teams |
| **Seniority** | Early Career (0--3 years post-degree; full-time, NOT intern) |
| **Remote** | Onsite -- Chicago, IL or New York, NY (London also listed in form) |
| **Team size** | Not specified; rotation model: 1-on-1 mentoring with senior engineers |
| **Comp disclosed** | $150,000--$200,000 base + discretionary bonus (significant) |
| **TL;DR** | Full-time early-career role at a fast-growing Chicago/NY quant shop (ex-Citadel DNA). Rotate through 2--3 tech teams building systems that directly drive firm profitability; Python or C++; distributed systems + event-driven architecture valued. |

Key distinction from report #038 (token 8489233002, Intern Summer 2027): this is a **full-time new-grad role**, not an internship. No graduation-window restriction ("no more than 3 years of professional experience" is the only constraint). Harry's May 2027 graduation makes him a natural applicant -- he'd start ~May/June 2027.

---

## B) Match with CV

### Requirements Mapping

| JD Requirement | CV Evidence | Strength |
|---|---|---|
| BS in CS or equivalent | Georgia State, BS CS, Expected May 2027, GPA 3.75 | Excellent |
| Python or C++ | C++ (Google Chrome IPC/Protobuf, 3B+ users); Python (TiMoto vLLM/ML serving, Django, FastAPI) | Excellent |
| Event-driven architectures | TypeScript/React observer pattern in Chromium (68% delivery acceleration); multi-AZ ECS event-driven ops | Strong |
| Distributed systems | gRPC inter-service layer + deadlock RCA, multi-AZ ECS Fargate, 99.9% uptime, sub-50ms p99 | Excellent |
| Strong quantitative skills | GPA 3.75; Distributed Systems, OS, DB, Networks coursework; lock-free trie analysis; Raft/Paxos study | Strong |
| No more than 3 years post-education | Harry graduates May 2027 -- 0 years at application | Excellent (clean) |
| Software design + TDD/refactoring | 95% test coverage norm from Chrome; design docs reviewed by senior Chrome engineers | Strong |
| Bias for action | Proactive deadlock RCA, profiling-driven perf optimization, OOM prevention via architecture choice | Strong |
| Collaboration + mentoring receptiveness | Chromium code reviews with senior Chrome engineers; 3-person TiMoto team ownership | Strong |

### Gaps

| Gap | Blocker? | Mitigation |
|---|---|---|
| No quantitative finance / trading systems experience | Nice-to-have | Frame distributed systems work as reliability-critical, low-latency -- same constraints as trading infra. Google at 3B+ user scale is a direct comp. |
| No math competition background (Putnam, USAMO, etc.) | Nice-to-have (form question, not hard requirement) | Honest "no" on form. GPA 3.75 + production system design proof compensates. |
| No prior hedge fund / prop trading internship | Nice-to-have | Honest "no" on form. Google Chrome and TiMoto are strong alternatives at comparable or larger scale. |
| Event-driven architectures (not a headline item on CV) | Nice-to-have | ECS event-driven infra (TiMoto) + observer pattern (Chrome) demonstrate the concept; highlight in cover letter. |

**F-1 visa:** JD does not state sponsorship policy explicitly. Aquatic has sponsored H-1B in the past (see #038 context). The form asks employment eligibility status and whether sponsorship is required. **Still apply**; flag it early in the recruiter screen.

**Graduation timing:** May 2027 is clean for this role -- no window constraint like #038. Harry could start June 2027 under OPT.

---

## C) Level and Strategy

**Level detected:** Early Career (0--3 years post-degree). This is the full-time new-grad tier -- exactly Harry's target window.

**Harry's natural level for this archetype:** Harry's profile is strong for this level. Production C++ at Chrome scale and production ML infra at TiMoto put him in the top tier of early-career applicants. This is arguably the best-fit role type of all Aquatic postings evaluated: no graduation window mismatch, no experience overcalibration issue.

### Sell senior without overselling

- Lead with the Google Chrome IPC story: designed and shipped a C++ Protobuf transport to 3B+ users at sub-50ms p99, 10K+ req/sec. This is exactly the "Python or C++, high-performance, distributed systems" language in the JD.
- TiMoto gRPC deadlock fix: production concurrency debugging with root-cause analysis. The "system reliability" signal they want in a rotation engineer.
- vLLM/PagedAttention architecture: demonstrates understanding of memory models under concurrent load -- trading infra pattern.
- Rotation model (2--3 teams) aligns well with Harry's breadth: backend/infra/ML serving at TiMoto, plus Chrome systems, plus open source (Pulumi). Frame this as "I've already done rotations -- by necessity on a 3-person team."
- Raft/Paxos study (Pulumi) signals intellectual curiosity into distributed consensus -- exactly the "curiosity-driven" desired quality.

### If they ask about trading/finance experience

> "I haven't worked on trading systems specifically, but at TiMoto I owned a distributed ML serving platform with the same constraints -- sub-50ms SLOs, concurrent gRPC load, zero tolerance for memory or correctness failures. The reliability and latency problems are identical; the domain is different. I'd be excited to learn the domain from senior engineers in the rotation model."

### "If they downlevel me" plan

This is an entry-level role by design -- there's no downleveling risk. If Aquatic offers below $150K:

> "Based on my research, top quant early-career bands run $150K--$200K base plus discretionary bonus. Given my production background at Google and TiMoto, I'm targeting the upper half of that range. Is there flexibility?"

---

## D) Comp and Demand

### Aquatic Early Career Compensation

| Source | Data |
|---|---|
| JD (explicit) | $150,000--$200,000 base + discretionary bonus (described as "significant") |
| Levels.fyi (Aquatic SWE, early career) | Limited data; FT SWE total comp reported $325K--$425K+ |
| Aquatic intern (~$135/hr annualized) | ~$270K/yr equivalent; FT base likely below this (equity/bonus structure differs) |
| Comparable quant early-career (Jane Street, Citadel) | $150K--$200K base + discretionary performance bonus commonly 50--150%+ of base |

### Market Context

| Firm | Early Career Base (reported) | Bonus structure |
|---|---|---|
| Jane Street (SWE) | $175K--$200K+ | Discretionary, can 2--3x base |
| Citadel / Citadel Securities | $150K--$200K base | Large discretionary |
| D.E. Shaw | $175K--$200K | Discretionary, significant |
| Aquatic (JD explicit) | $150K--$200K | Discretionary bonus, significant |
| Top FAANG new grad (2026) | $150K--$180K base + RSU | More predictable structure |

**Verdict:** Aquatic's $150K--$200K base range meets Harry's target ($150K--$200K) exactly at the minimum and exceeds it at the top. Discretionary bonus at quant firms can be 50--200%+ of base, so total comp in a strong first year could reach $300K--$400K+. This is top-quartile new-grad comp regardless of sector. The tradeoff vs. FAANG is that quant bonus variability is high -- exceptional upside but less predictable than RSU vesting.

**F-1 comp note:** For internship (if they have a CPT/OPT-eligible summer path), the rate is ~$135/hr (~$270K annualized). For full-time starting May/June 2027 under OPT, the base applies directly.

---

## E) Customization Plan

| # | Section | Current status | Proposed change | Why |
|---|---|---|---|---|
| 1 | **Professional Summary** | Generic distributed systems framing | Open with: "CS @ Georgia State (GPA 3.75, May 2027) -- Google Chrome SWE intern (C++ IPC, 3B+ users) -- Primary engineer at TiMoto AI (distributed ML serving, gRPC, AWS). Built and maintained high-performance distributed systems in production. Seeking early-career role where I can apply systems depth to quantitative research infrastructure." | JD explicitly asks for distributed systems + event-driven; mirror the language; connect to quant domain |
| 2 | **TiMoto gRPC bullet** | Good but buries the RCA story | Tighten: "Debugged production gRPC deadlock under concurrent load via resource-acquisition conflict analysis -- restored 100% evaluation success rate at sub-50ms p99" | Quant firms value RCA proof and correctness under concurrency |
| 3 | **Google Chrome lock-free trie** | Correct but framing is broad | Surface as: "Identified settings-nav as p99 bottleneck at 1,200ms; replaced mutex-contended trie with lock-free structure -- 96% latency reduction, zero regressions" | Lock-free structures + profiling discipline = direct trading infra signal |
| 4 | **Skills section** | ML tools listed prominently | Reorder: Distributed Systems + Languages first; Cloud/Infra second; ML/AI Infrastructure third. This is a systems/infrastructure role, not an ML product role. | Role emphasizes systems, algorithms, event-driven architecture |
| 5 | **Pulumi project** | Listed as contributor with Go/TypeScript/IaC | Add: "Analyzed Raft/Paxos consensus in distributed state synchronization layer -- studied linearizability and correctness under partial failures" (already in CV; ensure it's surfaced near top of Projects) | Distributed consensus literacy signals quant-infrastructure readiness |

**LinkedIn (if applicable):**
1. Headline: "CS @ Georgia State (2027) · Google Chrome SWE · Distributed Systems + ML Infra"
2. About: Lead with Chrome IPC at scale + TiMoto reliability metrics
3. Featured: Pin GitHub (Pulumi contributions) -- quant firms review code quality
4. Skills: Pin C++, Python, Distributed Systems, gRPC, Protocol Buffers, Event-driven Architecture
5. Education: Confirm May 2027 graduation date is accurate

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Python/C++ in high-performance systems | **Google Chrome IPC Transport** | Chrome browser extension system needed inter-process serialization at scale | Ship C++ IPC with Protobuf to Chrome stable (3B+ users), sub-50ms p99, 10K+ req/sec | Evaluated Protobuf vs. custom serialization; chose Protobuf for schema evolution; designed C++ transport; collaborated with Chrome infra team on design docs + code review | Shipped to stable; 95% test coverage; adopted by Chrome engineers | Schema evolution tradeoff was the right call -- custom serialization would have been unmaintainable across 25K+ LOC Chromium codebase |
| 2 | Distributed systems + event-driven architecture | **gRPC Deadlock RCA at TiMoto** | Production deadlock under concurrent gRPC calls causing 100% evaluation failures | Debug and eliminate deadlock without service restart | Traced shared resource acquisition conflicts; redesigned call sequencing to enforce consistent lock ordering | 100% evaluation success rate at sub-50ms p99 | Instrument lock acquisition order diagrams before launch -- this class of bug is detectable before production with formal sequence analysis |
| 3 | Low-latency, profiling-driven optimization | **Lock-Free Trie at Chrome** | Settings search at 1,200ms p99 blocking real users | Drop p99 below 50ms without correctness regression | Profiling identified mutex contention on trie traversal; replaced with lock-free structure; verified linearizability before shipping | 96% latency reduction (1,200ms to ~50ms), zero regressions | Linearizability proof is mandatory before shipping lock-free structures -- benchmarks alone are not sufficient |
| 4 | System reliability and tooling | **Multi-AZ Terraform at TiMoto** | Single-AZ backend with no failover, no cost controls | Build fault-tolerant, cost-efficient multi-AZ infra | Multi-AZ ECS Fargate with Terraform IaC, CloudWatch observability, circuit breaker, health-check auto-rollback | 99.9% uptime, 44% cost reduction ($40--60/month), automated recovery | Cost and reliability are joint optimization targets -- you model both as constraints, not competing goals |
| 5 | Software design + test-driven development | **Chromium React Observer Pattern** | Feature delivery blocked by tight UI state coupling across 25K+ LOC | Decouple UI state propagation via event-driven architecture | Architected TypeScript/React system with observer pattern decoupling state; 95% test coverage maintained throughout | 68% feature delivery acceleration | Observer pattern is the right call when coupling cost grows with codebase size -- the test coverage discipline came directly from Chrome team norms |
| 6 | Algorithms + systems knowledge (quantitative skills) | **Pulumi Raft/Paxos Study** | Contributing to Pulumi's distributed state synchronization layer | Understand correctness guarantees under concurrent operations and partial failures | Analyzed Raft/Paxos consensus in Pulumi state engine; studied linearizability; shipped Go CLI features and bug fixes; under active maintainer review | Contributions under review by core Pulumi maintainers | Consensus algorithms define what guarantees you surface to the application layer -- trading infra needs the same clarity about what "consistent" means under partial failure |
| 7 | Rotation model -- breadth across teams | **TiMoto Primary Engineer breadth** | 3-person team with one engineer (Harry) owning backend + infra + ML serving | Ship distributed production systems end-to-end with no specialization | Designed gRPC inter-service layer, vLLM inference engine, multi-AZ ECS Fargate -- each a distinct domain | Sub-50ms p99, 99.9% uptime, zero OOM failures -- three separate system domains shipped concurrently | Working across domains in parallel is the closest civilian equivalent to the rotation model -- I already know how to context-switch between systems layers |

### Case study to present

**Recommend:** TiMoto gRPC deadlock + vLLM architecture decision as a combined story.

Frame as: "I had to design a serving layer that could not fail under concurrent load. I chose vLLM with PagedAttention because I understood KV cache fragmentation causes OOM under naive batching. Then -- separately -- I had to debug a production gRPC deadlock under concurrent calls. Two different concurrency failure modes in the same production system. That's the kind of correctness-under-load challenge I want more of."

### Red-flag questions

**"Have you worked in finance/trading before?"**
> "I haven't, but the distributed systems problems I find most interesting -- low-latency correctness under concurrent load, memory management under pressure, fault tolerance at scale -- are exactly what trading infrastructure requires. At TiMoto I owned a production serving platform with sub-50ms SLOs and zero tolerance for OOM or deadlocks. At Google I shipped C++ to 3B+ users at 10K+ req/sec. The domain is different; the engineering constraints are the same."

**"You're still in school -- why not wait and do an internship first?"**
> "I've been working as a primary engineer in production at TiMoto since September 2025 -- backend, cloud infra, and ML serving on a 3-person team. I'm not learning systems engineering; I'm doing it. This role's rotation model would accelerate that by exposing me to a broader set of systems problems with senior mentorship. The combination is what I'm looking for."

**"Do you need visa sponsorship?"**
> "I'm on F-1 status and will have OPT authorization starting May 2027, which covers the first 12 months of employment without firm action. For long-term employment I'd need H-1B sponsorship. I understand Aquatic has sponsored engineers in the past -- can you confirm that applies to early-career hires?"

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Apply button | Active -- full form visible, all fields functional | Positive |
| Role title | "Software Engineer, Early Career" -- specific level, distinct from intern posting (different token) | Positive |
| Salary disclosed | $150,000--$200,000 base explicitly stated in JD body; discretionary bonus described | Positive (strong) |
| JD specificity | Names specific technologies (Python, C++); clear rotation model (2--3 teams); concrete requirements (max 3 years post-degree) | Positive |
| Application form depth | Full custom form: comp expectations, GitHub username (SSH key required), education details, math competition history, employment eligibility -- significant employer investment | Positive |
| Locations | Chicago and New York explicitly stated (London in form) -- multi-office hiring signal | Positive |
| Company hiring signals | No layoffs found for Aquatic; ex-Citadel leadership; Glassdoor reviews describe growth culture | Positive |
| Reposting pattern | No Aquatic "Early Career" entry in scan-history.tsv; companion intern role (#038) also High Confidence | Neutral |
| Posting age | Exact post date unavailable from snapshot; early-career roles for 2027 grads typically open spring/summer 2026 -- timing consistent | Neutral |

**Context notes:**
- Aquatic is early-stage (founded post-2015, ex-Citadel DNA). This is a legitimate but smaller firm than Citadel or Jane Street. The "early stage" culture note is a work-environment signal, not a ghost-job signal.
- Salary transparency ($150K--$200K base) is a strong legitimacy indicator -- ghost postings rarely publish comp ranges.
- This role and #038 (intern) appear to be simultaneous pipelines for different candidate stages. Both are consistent with a firm actively building out its engineering org.
- The SSH key requirement on GitHub is a technical hiring signal consistent with a firm that actually reads candidate code.

---

## H) Draft Application Answers

*(Score 4.4/5 -- Block H included)*

### First Name / Last Name / Email / Phone
> Harry / Nguyen / harry.nguyen@timoto.ai / +1 470-667-9000

### Do you have any outstanding offers or deadlines?
> "No current offers with imminent deadlines. I am actively in other processes and would appreciate moving quickly -- happy to work with your timeline."

*(Adjust if live offers exist.)*

### Employment eligibility status
Select: **F-1 / OPT eligible** (or the equivalent dropdown option indicating work authorization via OPT).

The form note: "Will you require the firm's sponsorship to obtain, maintain, or extend your employment authorization?"
**Answer: Yes** -- for long-term employment (H-1B). For the first 12 months under OPT, no firm action is required.

### Current Location
> "Atlanta, GA"

### Location Preference
Check: **Chicago** and/or **New York** (both are acceptable; Chicago has the larger Aquatic presence historically).

### Current Professional Experience
Select: **Student / recent grad** or equivalent (Harry has ~1 year at TiMoto but is still enrolled -- select the option that matches being a current student with part-time/concurrent professional experience).

### What degree are you currently pursuing or have recently completed?
Select: **Bachelor's**

### Fields of study
Check: **Computer Science**

### What year are you expected to graduate?
Select: **2027**

### GPA
Select the bracket covering **3.75** (typically "3.5--4.0" or "3.75+").

### Have you completed any internships at a hedge fund or prop trading firm?
Select: **Yes, completed internships -- none at a hedge fund or prop trading firm**

> "I completed a Software Engineering internship at Google (Chrome team, summer 2025) and Develop for Good (summer 2024). Neither was in finance. The Google internship involved shipping C++ IPC infrastructure to 3B+ active users at sub-50ms p99; Develop for Good involved AWS infrastructure serving 500+ concurrent users."

### Have you participated in any mathematics competitions?
Check: **I have not participated in any of these competitions**

### What are your annualized total compensation expectations?
> "$175,000--$200,000 base, consistent with the upper half of the posted range, reflecting my production background at Google and TiMoto. Open to discussing the full package including discretionary bonus structure."

### LinkedIn Profile
> "linkedin.com/in/harrynguyen26"

### GitHub username
> **HarryNguyen2662**

*(Ensure a public SSH key is added to this account before submitting.)*

### How did you hear about this job?
> "Search engine / job board"

---

## Keywords extracted

early career, software engineer, distributed systems, event-driven architectures, Python, C++, quantitative, financial markets, scientific research, trading infrastructure, research infrastructure, system reliability, test-driven development, refactoring, low-latency, high-throughput, mentoring, rotation, technical excellence, performance, correctness, concurrency
