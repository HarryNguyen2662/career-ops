# Evaluation: Ellipsis Labs -- Software Engineer, 2027 New Grads

**Date:** 2026-06-04
**URL:** https://jobs.ashbyhq.com/ellipsislabs/256c2ec2-01c8-4ff6-9ad0-b926fe40472d
**Archetype:** Founding / Early-Stage Software Engineer (primary) + AI Platform / LLMOps (secondary)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Founding / Early-Stage Software Engineer (generalist new grad, high-ownership startup) |
| **Domain** | DeFi / on-chain financial infrastructure (Solana DEX) |
| **Function** | Build — full product features and/or platform components across full stack, back end, infra, or on-chain |
| **Seniority** | New Grad 2027 (explicitly labeled) |
| **Remote** | Hybrid — New York, New York |
| **Team size** | Not stated; early-stage startup (small) |
| **Comp** | $150K-$200K + equity |
| **TL;DR** | Solana-native DeFi startup ($285B+ volume) seeking a generalist new grad with strong CS fundamentals to build end-to-end across any part of their stack — front end, back end, infra, or on-chain. |

---

## B) Match with CV

### Required Qualifications

| JD Requirement | CV Evidence | Match |
|---|---|---|
| Hands-on experience building software in TypeScript/JavaScript, Python, Rust, Java, or C/C++ | Languages row: "C++, Python, Go, TypeScript, Java, JavaScript, SQL, Bash, Rust"; Google Chrome C++ IPC + TypeScript React; TiMoto AI Python/FastAPI | Strong |
| Solid CS fundamentals (data structures, algorithms, systems thinking) | GSU coursework: Distributed Systems, OS, DB, Networks, Data Structures; lock-free trie (algorithms); Raft/Paxos analysis (systems thinking) | Strong |
| Familiarity with Git and basic debugging | Implied throughout all three work experiences; Google Chrome "95% test coverage" shows debugging discipline | Strong |
| Ability to make informed trade-offs with business context | Explicit in CV: Protobuf vs custom serialization (schema evolution rationale), JWT vs session auth (horizontal scalability rationale), vLLM vs naive inference (OOM risk framing) | Strong |
| High agency and team-first mindset | Primary engineer at 3-person startup TiMoto AI; "Led backend, cloud infra, and ML serving for a 3-person engineering team" | Strong |
| Curiosity about DeFi/crypto (prior experience not required) | No direct DeFi experience, but: low-level systems (C++, lock-free structures), distributed correctness (Raft/Paxos literacy), high-throughput APIs all transfer directly | Partial |

### Preferred Qualifications

| JD Preference | CV Evidence | Match |
|---|---|---|
| Full-stack web (React/JavaScript) | TypeScript/React in Google Chrome (observer pattern, 25K+ lines Chromium, 68% delivery acceleration) | Strong |
| Backend APIs/services | gRPC inter-service layer at TiMoto AI; Django/FastAPI; PostgreSQL | Strong |
| Infrastructure/DevOps (Docker, CI/CD, cloud) | AWS ECS Fargate, Terraform IaC, GitHub Actions CI/CD, CloudWatch; 99.9% uptime, 44% cost cut | Strong |
| On-chain/low-level systems | C++ IPC (Protocol Buffers), lock-free trie, Raft/Paxos study; adjacent — no Solana/on-chain direct | Adjacent |
| Blockchain technology (Solana a plus) | No Solana experience | Gap |
| Interest/experience in fintech/trading | No fintech/trading experience directly; strong high-throughput, low-latency backend maps to trading infrastructure | Adjacent |
| Rust or TypeScript proficiency | Languages row lists both Rust and TypeScript; TypeScript shipped in Chrome; Rust in skills list | Strong |

### Gaps Analysis

| Gap | Blocker? | Mitigation |
|---|---|---|
| No Solana/blockchain experience | No -- JD says "prior domain experience not required" for DeFi/crypto curiosity | Frame CS fundamentals + distributed systems literacy; mention Raft/Paxos study from Pulumi contribution; express genuine curiosity in cover letter |
| No fintech/trading background | No -- listed as preferred interest, not required | Emphasize high-throughput, low-latency backend work (sub-50ms p99, 10K+ req/sec at Google Chrome) -- exactly the profile a DEX needs |
| Rust is listed in skills but no shipped Rust project | Soft -- Rust is "preferred" not required | List it accurately; mention systems-level proficiency in C++ as evidence of low-level capability; Pulumi Go CLI work shows production language breadth |

---

## C) Level and Strategy

**Level detected:** New Grad 2027 (exact match -- JD is explicitly labeled "2027 New Grads")

**Candidate's natural level:** New Grad / Intern -- perfect alignment.

**Sell new grad without underselling:**
- Lead with *breadth* -- "I've shipped across back end (gRPC/Python), infra (Terraform/ECS), ML serving (vLLM), and front end (TypeScript/React in Chromium) -- your generalist requirement is a fit, not a stretch."
- Lead with *ownership* -- "Primary engineer on backend + infra + ML at a 3-person startup. I owned decisions end-to-end: architecture, deploy, on-call, post-mortems."
- Frame Google as *bar* -- "Chrome stable channel + senior code review = I've shipped to billions of users under production quality bar."
- Frame Pulumi as *curiosity signal* -- open-source contribution to IaC platform signals the kind of side-project curiosity a DeFi startup wants.

**"If they push on domain knowledge":**
- "I've studied distributed consensus (Raft/Paxos) through my Pulumi work. Blockchain fundamentally is a consensus + state machine problem -- I know the underlying primitives."
- "My C++ and low-latency backend background (sub-50ms p99 under concurrent load) is directly applicable to order-book performance."

---

## D) Comp and Demand

| Data Point | Value | Source |
|---|---|---|
| JD listed comp | $150K-$200K + equity | Ashby posting |
| Harry's target | $150K-$200K | profile.yml |
| Harry's floor | $140K | profile.yml |
| New grad SWE NYC (top-tier startup, 2026) | $150K-$200K base typical for funded DeFi/fintech startups | Levels.fyi comparable (crypto/DeFi startups pay at or above FAANG new grad base) |
| Equity | Not quantified; venture-backed early-stage startup -- equity could be significant upside | JD: "Offers Equity" |
| Comp assessment | Floor of range ($150K) matches Harry's target exactly; ceiling ($200K) exceeds it. Excellent alignment. | |

**Assessment:** Comp is at the top of Harry's target band. Equity upside at an early-stage, profitable startup (stated profitable) with $285B+ volume could be meaningful. No comp gap -- this is a clean match.

**Market note:** Ellipsis Labs describes itself as "profitable" and "venture-backed" which is a rare combination for early-stage DeFi. Suggests runway stability is better than most crypto startups.

---

## E) Customization Plan

| # | Section | Current Status | Proposed Change | Why |
|---|---|---|---|---|
| 1 | Summary / Headline | "Distributed Systems / Backend Infrastructure" | Add "high-throughput systems + low-latency backend" framing | Matches DEX/order-book performance language |
| 2 | TiMoto bullet 1 | "Led backend, cloud infra, and ML serving for a 3-person engineering team" | Add: "-- owned full feature lifecycle from design to on-call" | Matches "Own scoped projects end-to-end" in JD |
| 3 | Google Chrome | Strong as-is | Optionally add "informed Protocol Buffers selection by studying schema evolution trade-offs" phrasing | JD emphasizes "informed trade-offs" -- show the reasoning, not just the result |
| 4 | Skills -- Languages | Currently lists Rust | Keep Rust; if applying via form, mention TypeScript and Rust first in language list | JD explicitly prefers Rust and TypeScript proficiency |
| 5 | Cover letter | Not yet drafted | Write one paragraph connecting Raft/Paxos study → blockchain interest → why Phoenix's order-book architecture is intellectually interesting | DeFi curiosity is required; this is the place to demonstrate it |
| 6 | LinkedIn | N/A for this application | N/A | Small startup unlikely to screen LinkedIn heavily before outreach |

---

## F) Interview Plan

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Own projects end-to-end (problem → design → implementation → testing → deploy → monitoring) | TiMoto vLLM architecture | ML serving was naive with OOM failures under concurrent load | Own end-to-end serving design for production AI product | Evaluated PagedAttention vs naive KV cache; chose vLLM with continuous batching; deployed on AWS with CloudWatch monitoring | Zero OOM failures at production traffic; sub-50ms p99 | Would have added circuit breaker earlier -- learned monitoring during, not before, deploy |
| 2 | Informed trade-offs with business context | Google Chrome -- Protocol Buffers selection | Needed IPC transport for Chrome settings feature shipped to 3B+ users | Choose serialization format: custom binary vs Protocol Buffers | Evaluated schema evolution risk, cross-language compatibility, maintenance cost; selected Protobuf | Shipped to Chrome stable; adopted by senior Chrome engineers | Trade-off documentation now part of my default process for any protocol decision |
| 3 | High performance, reliability | Google Chrome -- lock-free trie | Settings navigation at 1,200ms p99 was a bottleneck; mutex contention identified | Eliminate latency without regressions on Chrome stable | Profiled, identified mutex hot-path, designed lock-free concurrent trie | 96% latency reduction; zero production regressions | Learned to profile before optimizing -- first instinct was wrong about the bottleneck location |
| 4 | Instrument and improve reliability/observability | TiMoto -- multi-AZ ECS + circuit breaker | Production ML system with no auto-recovery -- single-AZ with manual restarts | Build resilient, self-healing infra under $60/month cost target | Multi-AZ ECS Fargate with Terraform, CloudWatch alarms, circuit breaker, auto-rollback | 99.9% uptime, 44% cost reduction | Cost and reliability are not in tension when you design IaC correctly from day one |
| 5 | Clear tests and documentation | Google Chrome -- 95% test coverage | Chromium is a massive, safety-critical codebase | Deliver features at 95%+ coverage bar to pass code review | Wrote unit + integration tests for C++ IPC and TypeScript components; design docs for senior review | Adopted into production branch with no regressions | High coverage discipline is now a default, not a requirement -- it reduces debugging time more than it costs writing time |
| 6 | Build across the stack | TiMoto -- gRPC deadlock fix | Production deadlock under concurrent gRPC calls causing evaluation failures | Restore 100% success rate without downtime | Traced shared resource acquisition conflicts, redesigned call sequencing | 100% evaluation success rate at sub-50ms p99 | Concurrency bugs require reading code as a state machine, not a sequence -- changed how I review concurrent code |
| 7 | Curiosity about DeFi/crypto | Pulumi -- Raft/Paxos analysis | Open-source contribution to distributed state synchronization | Understand correctness guarantees in distributed systems | Analyzed Raft consensus for linearizability under partial failures | Understanding of consensus directly maps to blockchain as a state machine | Blockchain is a specialized consensus problem -- the primitives transfer |
| 8 | Iterate and ship quickly | Develop for Good -- N+1 fix | Response times degraded to 3s+ on large datasets in production | Diagnose and fix without breaking live system | Identified N+1 via profiling, redesigned with PostgreSQL indexing | Sub-100ms for 10,000+ records | Diagnosing first, then fixing -- the instinct to rewrite can hide simpler root causes |

### Recommended Case Study
**TiMoto ML Serving Platform** -- walk through the full architecture decision: why vLLM over naive inference, how PagedAttention solved the OOM problem, what the monitoring setup looks like, and the cost/reliability outcome. This demonstrates end-to-end ownership + "instrument and improve" + trade-off reasoning -- all three are explicit in the Ellipsis JD.

### Red-Flag Questions
- **"Do you know Solana / blockchain?"** -- Answer: "No production Solana experience, but I've studied distributed consensus (Raft/Paxos) through my Pulumi work, and I'm genuinely curious about order-book mechanics. I learn new domains fast -- I came into TiMoto without ML serving experience and owned the stack within weeks."
- **"You're graduating in 2027 -- any conflict with a May start?"** -- Answer: "My last semester ends May 2027 and I'm targeting full-time roles starting then. Happy to discuss timeline flexibility if there's an earlier need."
- **"F-1 visa?"** -- Answer: "On F-1, eligible for OPT starting May 2027. Will need H-1B sponsorship for long-term. Happy to discuss your sponsorship policy."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Apply button | Active ("Apply for this Job" visible in Playwright snapshot) | Positive |
| JD specificity | Names specific role expectations (Phoenix Perpetuals, SolFi, Phoenix Legacy), volume metric ($285B), explicit 2027 cohort targeting | Positive |
| Compensation listed | $150K-$200K + equity stated in Ashby posting | Positive |
| Reposting detection | Not found in scan-history.tsv -- first time seen | Positive / Neutral |
| Company hiring signals | Profitable self-described startup; no layoff signals for a company of this size | Positive |
| Role-company fit | Small team needing generalist new grads is textbook early-stage hiring | Positive |
| JD quality | Names specific products, trading volume, and has realistic requirements for new grad level | Positive |

**Context Notes:** Ellipsis Labs is a small, profitable DeFi startup. JD is targeted (2027 cohort only), specific (lists exact products and mission), and comp is transparent. No concerning signals. High confidence this is a real, active opening.

---

## H) Draft Application Answers

*(Score >= 4.0 -- draft answers included)*

**Why Ellipsis Labs?**
> "Ellipsis Labs is building the financial system primitives that matter -- a central limit order book on Solana, not another wrapper. The Phoenix architecture is the kind of low-latency, high-correctness problem I care about: you can't afford soft failures in a live order book, same as you can't in Chrome IPC or production ML serving. I've shipped across backend, infra, and front end in production, and I want to do that at the layer where the performance guarantees actually matter."

**Tell us about a project you're proud of and why.**
> "At TiMoto AI, I owned the full ML serving stack for a 3-person team: chose vLLM with PagedAttention over naive KV caching after analyzing memory fragmentation under concurrent load, deployed it on multi-AZ ECS Fargate with Terraform, wrote the circuit breaker and CloudWatch runbooks, and stayed on-call. The result: zero OOM failures in production, sub-50ms p99, 44% infra cost reduction. What I'm proud of is not the numbers -- it's that I made the architecture decision, got it wrong on the first pass (naive batching), debugged it under load, and shipped the fix. That cycle -- design, break, learn, fix -- is how I expect to work."

**What's a trade-off you made recently and why?**
> "At Google Chrome, I chose Protocol Buffers over a custom binary serialization for a new IPC transport. Custom would have been ~20% faster for our specific schema but would have broken cross-language compatibility and made schema evolution painful as Chrome's codebase scales. I documented the trade-off, got senior engineer sign-off, and shipped to stable. The feature is now in Chrome used by 3B+ users with no serialization-related incidents. Performance trade-offs are only valid if the system actually ships and stays maintained."

---

## Keywords Extracted

solana, on-chain, order book, DEX, DeFi, perpetuals, TypeScript, Rust, React, JavaScript, backend, infrastructure, full-stack, CI/CD, Docker, cloud, deployment, monitoring, reliability, testing

---

## Machine Summary

```yaml
report: "054"
company: "Ellipsis Labs"
role: "Software Engineer -- 2027 New Grads"
score: 4.3
archetype: "Founding / Early-Stage Software Engineer"
status: "Evaluated"
date: "2026-06-04"
url: "https://jobs.ashbyhq.com/ellipsislabs/256c2ec2-01c8-4ff6-9ad0-b926fe40472d"
location: "New York, NY (Hybrid)"
comp_stated: "$150K-$200K + equity"
comp_match: "exact target range"
visa_risk: "F-1 -- sponsorship not mentioned; ask recruiter"
top_gaps:
  - "No Solana/blockchain experience (not required per JD)"
  - "No fintech/trading background (preferred, not required)"
legitimacy: "High Confidence"
recommendation: "Apply -- strong archetype match, explicit 2027 cohort, comp aligned, generalist ownership profile fits perfectly"
```
