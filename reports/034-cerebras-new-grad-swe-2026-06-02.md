# Evaluation: Cerebras Systems -- New Graduate Software Engineer (Sunnyvale)

**Date:** 2026-06-02
**URL:** https://job-boards.greenhouse.io/earlytalentcerebras/jobs/7621174003
**Archetype:** Systems Software Engineer / ML Infrastructure Engineer (hybrid)
**Score:** 4.3/5
**Legitimacy:** High Confidence
**PDF:** output/034-cerebras-new-grad-swe-harry-nguyen-2026-06-02.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | Systems Software / ML Infrastructure (hybrid) |
| **Domain** | AI accelerator hardware + software stack (wafer-scale chip, compilers, distributed systems, ML frameworks) |
| **Function** | Build -- design, implement, and test software across the full stack |
| **Seniority** | New Graduate (graduating 2026 -- note: Harry graduates May 2027) |
| **Location** | Hybrid, Sunnyvale, CA (relocation required) |
| **Team placement** | General pool -- team assigned based on skills, experience, and team needs at time of hire |
| **Team size** | ~700 employees company-wide; team size unspecified |
| **TL;DR** | Cerebras, the world's largest AI chip company (just IPO'd at $95B, $10B OpenAI contract), seeks a new grad SWE for its Sunnyvale HQ to work anywhere across the hardware-software stack -- compilers, distributed systems, ML frameworks, or hardware-adjacent software. |

**Company snapshot:** Cerebras IPO'd May 14, 2026 on Nasdaq at $350/share (opening), $510M in 2025 revenue, $10B OpenAI multi-year inference deal. One of the highest-growth AI infrastructure companies in the world. Startup vitality + public company stability.

**Critical note -- graduation year:** The JD says "graduating 2026." Harry graduates May 2027. This is the primary risk factor. The role is described as "a new graduate position" and the form asks "When are you graduating?" -- Harry should answer honestly (May 2027) and clarify this early. Some companies accept May 2027 starts for new grad roles posted in 2026; others enforce it strictly.

---

## B) Match with CV

### Requirements mapping

| JD Requirement | Match in cv.md | Strength |
|---------------|----------------|----------|
| Recently graduated / enrolled, CS/CE degree | Georgia State CS, GPA 3.75, Expected May 2027 | Strong (year caveat) |
| Strong problem-solving skills | Google: lock-free trie eliminating mutex contention (96% latency cut); TiMoto: gRPC deadlock fix under concurrent load | Strong |
| Excellent communication skills | Google: design documents + code reviews adopted by senior Chrome engineers; 95% test coverage discipline | Strong |
| Proficient in one or more language | C++, Python, Go, TypeScript, Java, Rust -- full stack | Strong |
| C++ experience (asset) | Google Chrome: "Designed C++ IPC transport layer with Protocol Buffers -- shipped to Chrome stable, 3B+ users, sub-50ms p99, 10K+ req/sec" | Very strong -- direct match |
| Distributed systems | TiMoto: gRPC inter-service layer, multi-AZ ECS Fargate, circuit breakers, 99.9% uptime; Pulumi: Raft/Paxos analysis | Strong |
| Advanced hardware / compilers experience | Adjacent -- no direct compiler or hardware-level work, but: low-level C++ IPC, Protocol Buffers schema design, lock-free data structures | Adjacent |
| ML frameworks | TiMoto: vLLM, PyTorch, PagedAttention, LangChain, LLM-as-a-judge eval | Strong |
| Collaborate with world-class engineers | Google Chrome: collaborated with Chrome infrastructure team, changes reviewed by senior Chrome engineers | Direct proof |

### Gaps

| Gap | Hard blocker? | Mitigation |
|-----|--------------|------------|
| Compiler / hardware-adjacent software (likely team Cerebras cares about most) | No -- listed as "exposure/gain" in JD, not required | Frame C++ IPC + lock-free work as low-level systems experience; express interest in compiler/hardware track explicitly in cover letter |
| "Graduating 2026" -- Harry is May 2027 | Moderate risk -- not a blocker if Cerebras does rolling new grad cohorts | State May 2027 clearly; ask recruiter if role accepts 2027 cohort; many AI companies run "new grad" batches year-round |
| Wafer-scale chip architecture knowledge | None listed -- learning on the job | Express genuine interest in the hardware-software co-design angle |
| Team placement uncertainty | Low -- Harry's skills (C++, distributed systems, ML infra) map to multiple Cerebras teams | Highlight breadth as an asset; mention interest in compiler, distributed inference, or ML framework teams |

**Net assessment:** Harry's C++ IPC work at Google is the single strongest match signal -- Cerebras builds custom silicon and needs engineers who can reason about hardware-software boundaries at the C++ level. The ML serving experience (vLLM/PagedAttention) is a secondary strong signal for Cerebras's inference software stack. The graduation year is the primary risk factor to clarify.

---

## C) Level and Strategy

**Level detected:** New Graduate (entry-level SWE, team placement model)

**Harry's natural level:** New grad -- appropriate match. No "sell senior without lying" dynamic; the role is designed for new grads.

**Application strategy:**

1. **Lead with C++ production experience.** Cerebras is a hardware company -- they need engineers who can write C++ that talks to silicon. The Chrome IPC/Protobuf story (shipped to 3B users, sub-50ms, 10K req/sec) is the strongest opening.

2. **Frame TiMoto ML serving as inference-stack familiarity.** Cerebras is in the business of fast inference. vLLM/PagedAttention knowledge + production SLOs signals Harry already thinks about the problems Cerebras solves.

3. **Express team preference.** The JD says team placement is skills/experience-based. In the application and early interview, proactively state interest in the compiler, distributed systems, or inference software teams -- engineers who know what they want signal maturity.

4. **Handle graduation year proactively.** On the form, answer "May 2027." In free text or cover letter, note: "I'm available for a May 2027 start date and am happy to discuss internship or co-op formats if that better fits the 2026 cohort timeline."

**If they want a 2026 start only:** This is a genuine blocker. Ask recruiter directly -- do not waste interview cycles if start date is a hard constraint.

**Downlevel risk:** N/A -- role is already new grad level. No promotion path discussion needed at application stage.

---

## D) Comp and Demand

| Source | Data point | Notes |
|--------|-----------|-------|
| Levels.fyi | SWE L2 (entry): $194K total comp | Bay Area range -- likely closer to new grad band |
| 6figr (Sunnyvale) | Cerebras Sunnyvale: $184K--$580K | Very wide range; new grad at lower end |
| Glassdoor | 145 salary data points; SWE median ~$194K | All levels combined |
| Salary.com | Graduate SWE: $80K--$93K base | Likely underestimates total comp (excludes equity at pre/post-IPO company) |
| H1B filings (FY2026) | Data available -- indicates range | Relevant since Harry is F-1 |

**Key context:** Cerebras just IPO'd at $95B valuation. New grad equity grants issued at IPO price will vest in public market -- significantly more valuable and liquid than pre-IPO equity. For a new grad at a company with this growth trajectory, TC at the new-grad band is likely $180K--$220K total (base + RSUs), competitive with Tier 1 (Google, Meta) new grad packages. This is above Harry's $150K--200K target.

**Demand trend:** Very strong. Cerebras's $10B OpenAI deal + IPO + 750MW deployment = massive hiring need in software infrastructure. The company has ~700 employees and 89 open roles as of June 2026.

**Visa/sponsorship:** H1B sponsorship is likely -- Cerebras is a well-funded public company with H1B filing history. The application form asks about export control / US person status (EAR compliance) rather than visa sponsorship directly -- Harry should disclose F-1 status and confirm they are not subject to EAR restriction as a Vietnamese national (EAR99 items do not require license for most nationalities; Cerebras will assess at offer stage).

---

## E) Customization Plan

| # | Section | Current | Proposed change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary / cover letter opener | Generic distributed systems framing | Lead with: "Production C++ engineer (Google Chrome, 3B users) + ML serving (vLLM on AWS, sub-50ms p99) -- excited to work at the hardware-software boundary on Cerebras's inference stack" | Cerebras is a hardware company; C++ + inference is their sweet spot |
| 2 | TiMoto bullet 3 | "Architected vLLM inference engine with PagedAttention" | Add explicit inference speed framing: "...unlocking real-time inference SLOs -- directly aligned with Cerebras's core inference value proposition" | Mirrors Cerebras's product framing |
| 3 | Google Chrome bullets | IPC/Protobuf is already strong | Move C++ IPC bullet to first position under Google to ensure it's the opening signal | Recruiters scan first bullet of each job; C++ first is critical for Cerebras |
| 4 | Skills -- Distributed Systems | Current list is comprehensive | Reorder to put C++, low-level systems, compilers-adjacent terms first | Cerebras's software stack is primarily C++/compilers/hardware-adjacent |
| 5 | Projects -- Pulumi | "Analyzed Raft/Paxos consensus in distributed state synchronization layer" | Add: "-- applying linearizability guarantees to Cerebras-scale distributed inference synchronization" (cover letter only, not CV) | Shows ability to connect academic CS to Cerebras's real distributed system challenges |

**Top 5 LinkedIn changes:**
1. Headline: "New Grad SWE (May 2027) · C++ IPC at Google Chrome · ML Serving @ TiMoto AI · Distributed Systems"
2. About section: Lead with C++ production work + inference SLOs matching Cerebras's stack
3. Featured section: Pin TiMoto AI (timoto.ai) demo + Pulumi contribution link
4. Skills: Ensure C++, Protocol Buffers, vLLM, Distributed Systems rank in top 5
5. Education: Add relevant coursework explicitly (Distributed Systems, OS, Compilers if taken)

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|----------------|-------------|---|---|---|---|------------|
| 1 | C++ proficiency + hardware-adjacent systems | Google Chrome C++ IPC | Chrome needed a high-throughput settings IPC layer | Design a transport layer that handles 10K+ req/sec with schema evolution | Chose Protocol Buffers over custom serialization for cross-language compatibility and schema evolution; implemented C++ IPC layer | Shipped to stable channel, 3B+ users, sub-50ms p99 | Would evaluate QUIC/IPC alternatives; schema evolution constraint was the right decision driver |
| 2 | Problem-solving under concurrency | TiMoto gRPC deadlock fix | Production deadlock under concurrent gRPC evaluation calls | 100% evaluation failure rate; blocking prod | Traced shared resource acquisition conflicts; redesigned call sequencing | 100% success rate, sub-50ms p99 restored | Root cause analysis + instrumentation approach -- would add distributed tracing earlier |
| 3 | ML frameworks / inference stack | TiMoto vLLM/PagedAttention | Naive inference triggered OOM under concurrent load | Production ML serving SLOs at risk | Selected vLLM with PagedAttention to eliminate KV cache fragmentation; deployed with continuous batching | Zero OOM failures at production traffic | KV cache memory management is the key insight -- would benchmark latency vs memory tradeoffs earlier |
| 4 | Performance engineering | Google lock-free trie | Settings search p99 at 1,200ms; identified as bottleneck | Reduce latency in a Chromium path serving billions of users | Designed lock-free concurrent trie eliminating mutex contention | 96% latency reduction, zero regressions | Would add systematic profiling to design phase; the bottleneck was obvious in retrospect but required instrumentation to confirm |
| 5 | Distributed systems at scale | TiMoto multi-AZ ECS Fargate | Single-AZ infra risking availability SLOs | 99.9% uptime target; cost target $40--60/mo | Architect multi-AZ ECS Fargate + Terraform + circuit breaker + auto-rollback | 99.9% uptime, 44% cost reduction | Cost and reliability tradeoffs are symmetric -- circuit breaker removed the cost of bad health states |
| 6 | Collaborate with world-class engineers | Google Chrome design docs | Chrome infrastructure team standards for code adoption | Get changes into production branch reviewed by senior Chrome engineers | Wrote design documents, submitted for review, iterated on feedback | Changes adopted into production at 95% test coverage | High bar for review quality improved final design -- would engage reviewers earlier in design phase |

**Recommended case study to present:** TiMoto vLLM serving platform. Why: directly maps to Cerebras's core business (inference infrastructure). Walk through: problem (OOM under concurrent load) → technology selection (vLLM/PagedAttention vs naive inference) → deployment (AWS, continuous batching) → outcome (sub-50ms p99, zero OOM). Show timoto.ai live demo.

**Red-flag questions and how to answer:**

- "You graduate in 2027, this says graduating 2026 -- are you eligible?" → "I'm graduating May 2027. I should have flagged that earlier. I'm interested in whether Cerebras accepts 2027 cohort candidates for this role, or if there's an intern/co-op path for the 2026--2027 period. Happy to discuss what start date works."
- "You're at a 3-person startup -- how will you handle working at a larger company?" → "At TiMoto I owned backend, infra, and ML serving -- I had to hold the context of every system. At Google I embedded in a large team with design doc reviews and cross-team dependencies. I've operated at both ends of the collaboration spectrum. Cerebras's size (~700) is a great middle ground."
- "What team do you want to join?" → "Based on my background -- compiler-adjacent systems in C++ or the distributed inference stack. My C++ IPC work at Google and vLLM serving at TiMoto both touch hardware-software boundaries. I'd love to work where software meets the WSE chip."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button active | Active "Apply" button, full Greenhouse form live | Positive |
| JD specificity | Named technologies: C++, compilers, distributed systems, ML frameworks -- specific domain signals | Positive |
| Company trajectory | IPO'd May 2026 at $95B; $10B OpenAI deal; $510M revenue; Series G + H rounds | Positive (strong) |
| Active hiring | 89 open roles as of June 2026 per Trueup | Positive |
| Reposting | No prior Cerebras entries in scan-history.tsv | Neutral (first scan) |
| Layoff history | Jan 2023: 70 employees; Aug 2022: 40 employees -- both pre-revenue-scale; Jan 2026 discussion on Blind (limited data) | Neutral -- historical, pre-IPO era |
| JD graduation year | Says "graduating 2026" -- Harry is 2027 | Neutral (clarify with recruiter; does not indicate ghost posting) |
| No salary range | Not posted | Neutral (CA law may require range; worth noting) |

**Context notes:**
- The Jan 2026 layoff discussion on Blind predates the IPO (May 2026) and the $10B OpenAI deal announcement (Jan 2026). Post-IPO with a major revenue contract, the company is in expansion mode.
- "earlytalentcerebras" subdomain confirms this is a dedicated early talent / campus recruiting track -- not a generic posting.
- The role is a "general pool" new grad position -- Cerebras hires from this pipeline and assigns teams, which is common at hardware companies with differentiated software stacks.

---

## H) Draft Application Answers

### "When are you graduating?"
May 2027. I'm currently a junior at Georgia State University (CS, GPA 3.75) and on track to graduate in May 2027. I'm happy to discuss whether the role accepts 2027 cohort candidates or if there's a co-op/internship path for the 2026--2027 academic year.

### "When are you available to join?"
May 2027 for a full-time position. Available for internship / co-op starting May 2026 if that better fits the timeline.

### "Are you eligible to work in Canada and will you require visa sponsorship in the future?"
I am not eligible to work in Canada. In the US, I'm on F-1 status and currently eligible for CPT/OPT. I will require H-1B sponsorship for long-term employment beyond OPT. I understand Cerebras assesses export control (EAR) compliance separately -- I'm a Vietnamese national and will cooperate fully with that assessment.

### "Export Administration Regulations (EAR) -- citizenship / permanent residency"
Neither a US citizen nor a US permanent resident. I am a Vietnamese national on F-1 status. I understand Cerebras may need to perform an export compliance assessment and I will cooperate fully.

### Cover letter (1 paragraph)
I want to work at the hardware-software boundary, and Cerebras is the most interesting place to do that. At Google, I shipped a C++ IPC transport layer with Protocol Buffers to Chrome stable -- 3B+ users, sub-50ms p99, 10K+ req/sec -- and cut a settings-search bottleneck 96% with a lock-free concurrent trie. At TiMoto AI, I own the production ML serving stack: vLLM with PagedAttention (zero OOM failures under concurrent load), gRPC inter-service layer (fixed a production deadlock, 100% eval success rate), and multi-AZ Terraform infrastructure (99.9% uptime, 44% cost cut). Cerebras is building the fastest inference in the world -- I want to help build the software that runs on top of that chip.

---

## Keywords extracted

C++, Protocol Buffers, distributed systems, ML frameworks, compilers, wafer-scale, AI accelerator, inference, software stack, hardware-software co-design, new graduate, Sunnyvale, vLLM, gRPC, IPC, lock-free, performance, low-latency, systems programming, AI chip

---

## Machine Summary

```yaml
report: "034"
company: "Cerebras Systems"
role: "New Graduate Software Engineer"
location: "Sunnyvale, CA (hybrid)"
score: 4.3
archetype: "Systems Software Engineer / ML Infrastructure Engineer"
legitimacy: "High Confidence"
apply_recommendation: true
graduation_year_risk: true
visa_sponsorship: "likely (public company, H1B history)"
top_signals:
  - "C++ IPC at Google Chrome (ships to 3B users) -- direct Cerebras stack match"
  - "vLLM/PagedAttention production serving -- mirrors Cerebras inference product"
  - "IPO May 2026 at $95B + $10B OpenAI deal -- strong company trajectory"
primary_risk: "JD says graduating 2026; Harry is May 2027 -- must clarify with recruiter"
```
