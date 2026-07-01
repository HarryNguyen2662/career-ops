# Evaluation: Meta -- Software Engineer

**Date:** 2026-06-02
**URL:** https://www.metacareers.com/profile/job_details/1926156754682227
**Archetype:** Systems Software Engineer / Backend -- Distributed Systems Engineer (hybrid)
**Score:** 3.2/5
**Legitimacy:** Proceed with Caution
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Systems Software Engineer / Backend Engineer (generic funnel posting -- team unspecified) |
| Domain | Platform / product (no team assigned yet) |
| Function | Build |
| Seniority | E3 -- E4 (new grad to SWE II equivalent; JD says "moderate scope") |
| Location | Menlo Park, CA (onsite -- Meta office) |
| Team size | Not mentioned |
| Comp (posted) | $222,950 -- $250,250/year base + bonus + equity + benefits |
| TL;DR | Broad new-grad-to-mid-level SWE opening at Meta Menlo Park; team placement determined post-hire; requirements are CS fundamentals only -- no specialized stack. |

---

## B) Match with CV

### Requirement Mapping

| JD Requirement | CV Match | Strength |
|---|---|---|
| BS in CS or Engineering | Georgia State CS, GPA 3.75, May 2027 | Strong -- meets requirement on graduation |
| Coding in C, C++, Java, or C# | C++ shipped to Chrome stable (IPC transport layer, lock-free trie); C++ listed in skills | Strong |
| Web apps: Python, PHP, Ruby, Node.js, or React | Django (FastAPI) backend at TiMoto; React/TypeScript in Chromium (25K+ lines); Node.js in skills | Strong |
| Relational databases and SQL | PostgreSQL N+1 fix at Develop for Good (sub-100ms on 10K+ records); PostgreSQL + gRPC layer at TiMoto | Strong |
| Web interfaces: JavaScript, HTML, CSS | TypeScript/React UI in Chromium; JS/HTML listed in skills | Strong |
| High-quality code with test coverage | 95% test coverage norm from Chrome team (stated in cv.md) | Strong |
| Proficiency in data analysis, programming, software engineering | Sub-50ms p99 gRPC; 96% Chrome settings latency reduction; production distributed systems | Strong |
| Understand product and codebase deeply | Owns backend + infra + ML at TiMoto; contributor to Pulumi codebase | Good |

### Gaps

| Gap | Type | Mitigation |
|---|---|---|
| No specific team/product area specified | Informational -- cannot prep for a specific domain | N/A -- all teams evaluate the same pool |
| "May be assigned to infrastructure or product" -- product experience thinner than systems | Nice-to-have | Lead with systems/infra fit; mention breadth (Chromium, Django product APIs) |
| Graduation May 2027 -- role says "Requires a Bachelor's degree" (present tense) | Potential timing risk | Many Meta new-grad postings accept expected-grad; confirm in recruiter screen |

### F-1 / Sponsorship

Meta filed 858 H-1B LCAs for FY2026 (down from 5,704 in 2025 -- significant drop due to layoffs). Meta historically sponsors and has confirmed infrastructure. Post-layoff environment increases individual lottery risk. **Flag for recruiter screen; do not skip.**

---

## C) Level and Strategy

**Level detected:** Moderate scope + "within defined procedures" = E3 (entry-level SWE). JD language is intentionally generic for a funnel pool.

**Natural level for Harry:** New grad / E3 -- exactly matched.

### "Sell Senior Without Lying" Plan

Harry's profile is actually *above* the JD floor -- lead with production credibility:

1. **Open with Google Chrome scope:** "I shipped C++ IPC to 3B+ users with sub-50ms p99 and 95% test coverage -- this is the bar I hold myself to." Meta interviewers know Chrome is high-bar.
2. **TiMoto as production ML systems owner:** "I own backend, infra, and ML serving for a distributed production system -- not a toy project." This signals E4-readiness even when interviewing for E3.
3. **Breadth + depth:** C++ (Chrome), Python/Django (TiMoto), TypeScript/React (Chromium), Go (Pulumi) -- Meta values polyglot engineers.
4. **Test coverage norm:** 95% from Chrome is a strong cultural signal for Meta's production standards.

### "If They Downlevel Me" Plan

Not applicable -- posting is already E3. If Meta offers E2 (non-standard for new grad), negotiate up citing Google internship production scope and TiMoto distributed systems ownership.

---

## D) Comp and Demand

| Source | Data | Notes |
|---|---|---|
| **JD posted** | $222,950 -- $250,250 base/yr + bonus + equity | For California hire; this is the stated range |
| Levels.fyi E3 (SWE) | ~$193K -- $250K total comp at E3 | Based on June 2026 data; equity at Meta typically $50K--$200K RSUs over 4 yr |
| 6figr new grad | $176K -- $412K TC (new grad range across all levels) | Wide range -- E3 floor ~$176K TC |
| Glassdoor new grad | $125K -- $185K base (25th -- 75th pct) | Lower bound but includes non-CA locations |
| Meta total comp (all SWE) | Median $444K across all levels | Reference for long-term trajectory |

**Assessment:** The posted base range ($223K -- $250K) is top-tier for new grad Bay Area. This is likely the E3 California posting range. Total comp at E3 with equity would realistically be $250K -- $350K TC in year 1. Well above Harry's $150K -- $200K target range.

**Demand trend:** Meta is actively cutting headcount (8,000 layoffs, May 2026; 6,000 planned hires cancelled). This posting may be a retained evergreen or a specific backfill -- verify with recruiter. Despite layoffs, Meta is *growing* AI headcount.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Summary | "CS @ Georgia State + Google + TiMoto AI" | Lead with "production C++ systems engineer who shipped to 3B+ Chrome users and owns distributed ML serving" | Meta SWE interviews are systems-heavy; position as systems-credible, not student-credible |
| 2 | TiMoto experience | Full as-is | Keep all bullets; add "end-to-end ownership" framing in cover letter | Meta values production ownership; gRPC + vLLM + Terraform all map to Meta's infra stack |
| 3 | Google Chrome | Full as-is | Keep prominent; mention Protocol Buffers (Meta uses Thrift, Protobuf; cross-over knowledge) | Chrome internship = proven bar at production scale |
| 4 | Skills section | Listed broadly | Highlight C++, Python, TypeScript, SQL, PostgreSQL, gRPC in cover letter keywords | Map directly to Meta's most common backend/infra stacks |
| 5 | Pulumi project | Brief as-is | In cover letter: tie Go OSS contributions to Meta's OSS culture (Meta OSS: React, PyTorch, Presto) | Shows open-source values alignment |

**Top 5 LinkedIn changes:**
1. Headline: "SWE @ Google Chrome (3B+ users) · Distributed ML Serving @ TiMoto · CS @ Georgia State 2027"
2. About: Add "C++ IPC and settings perf shipped to Chrome stable" as first proof point
3. TiMoto: Add "primary engineer on 3-person team, distributed production systems" framing
4. Featured: Link github.com/HarryNguyen2662 and timoto.ai
5. Skills: Elevate C++, Protocol Buffers, gRPC, PostgreSQL, Terraform to top

---

## F) Interview Plan

Meta's SWE interview loop: coding (2 rounds, LeetCode-style), system design (1 round), behavioral/leadership (1 round). For E3 new grad: coding is primary filter; system design is lighter.

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | "Produce high-quality code with good test coverage" | Lock-free trie at Chrome | Mutex contention causing 1,200ms p99 on Chrome settings search | Reduce latency without regression | Profiled hotspot; replaced mutex with lock-free concurrent trie; verified linearizability | 96% latency reduction; shipped to stable; zero regressions; 95% test coverage | Lock-free needs formal correctness proof, not just benchmarks |
| 2 | "Work on problems of moderate scope" | N+1 fix at Develop for Good | N+1 query causing 3s+ response on 10K+ records | Fix without breaking existing APIs | Diagnosed via query logging; redesigned with PostgreSQL indexing | Sub-100ms on 10K+ records | Query planning should be checked before launch, not after user complaints |
| 3 | "Master internal development standards" | Chrome Chromium codebase navigation | Joining Chrome team with 25K+ lines of Chromium TS/React | Understand the codebase and ship a feature within internship | Read design docs; followed code review culture; got changes adopted by senior Chrome engineers | 68% feature delivery acceleration; changes merged into production branch | Reading existing code is 70% of the job -- invest in this before writing |
| 4 | "Demonstrate proficiency in data analysis, programming, software engineering" | gRPC deadlock fix at TiMoto | Concurrent gRPC calls causing intermittent deadlock in production AI evaluation | Eliminate deadlock without service restart or data loss | Traced shared resource acquisition; identified circular lock dependency; redesigned call sequencing | 100% evaluation success rate, sub-50ms p99, zero recurrence | Map lock acquisition order before any concurrent handler goes to production |
| 5 | "Develop a strong understanding of relevant product areas" | vLLM architecture decision at TiMoto | TiMoto needed concurrent LLM inference without OOM under load | Evaluate serving options and build production inference layer | Compared naive batching vs vLLM/PagedAttention; selected vLLM; deployed with continuous batching | Zero OOM failures, sub-50ms p99, 100% eval success rate | Document architecture decisions -- the "why" matters more than the config |
| 6 | "May be assigned to infrastructure" | Multi-AZ circuit breaker at TiMoto | Single-AZ backend with no failover | Design multi-AZ with auto-rollback | Terraform IaC for multi-AZ ECS Fargate, CloudWatch alarms, circuit breaker, auto-rollback | 99.9% uptime, 44% cost reduction ($40--60/mo), zero unplanned outages | Treat AZ isolation as Day 1 requirement, not retrofit |

**Recommended case study to present:** Google Chrome IPC + lock-free trie -- demonstrates C++ production rigor, quantified latency win, shipped to billions. Meta interviewers recognize Chrome as a high bar.

**Red-flag questions to prep:**
- "You're still a student -- why should we trust you with production?" → "I own distributed production systems at TiMoto and shipped to Chrome stable. I've been operating, not studying."
- "Meta is going through layoffs -- are you worried?" → "Meta is growing AI headcount aggressively. I'm targeting teams where the investment is going." (Research target team before interview.)
- "Do you need visa sponsorship?" → Use the F-1 script from _profile.md -- early disclosure, confident framing.
- "Why Meta specifically, not the university grad posting?" → "I saw this opening and my background is a direct match -- production C++ systems, ML serving, backend at scale. I'm happy to discuss which team would be the best fit."

**Story Bank:** Stories #1, 3, 4, 5, 6 above overlap with existing story bank entries (gRPC deadlock, lock-free trie, multi-AZ, vLLM). Story #2 (N+1 fix) and Story #3 (Chromium onboarding) are new additions -- see below.

---

## G) Posting Legitimacy

**Assessment: Proceed with Caution**

| Signal | Finding | Weight |
|---|---|---|
| Apply button active | Yes -- "Apply now" button present and active | Positive |
| Posting age | No date visible on page; cannot confirm freshness | Neutral |
| Salary posted | Yes -- $222,950 -- $250,250 (CA transparency law) | Positive |
| JD specificity | Very generic -- no team, no tech stack, no scope. Standard Meta funnel posting language. | Concerning |
| Requirements realism | Minimum quals are CS fundamentals only -- appropriate for E3 pool | Positive |
| Meta layoffs (May 2026) | 8,000 jobs cut; 6,000 planned hires cancelled. Same month as this posting. | Concerning |
| H-1B LCA volume | Down from 5,704 LCAs (2025) to 858 LCAs (FY2026) -- 85% reduction | Concerning |
| Reposting detection | scan-history.tsv shows Meta "Software Engineer (University Grad)" at different URL (first seen 2026-05-27); this URL (1926156754682227) is new and distinct -- different job ID. Not an exact duplicate but same company. | Neutral |
| Role-company fit | Generic SWE pool posting is a standard Meta practice (they batch-hire E3 and place after interview) | Positive -- this is how Meta hires |

**Context Notes:**
- Meta's generic funnel SWE posting is a documented practice, not a ghost job signal. Meta regularly posts undifferentiated SWE requisitions and assigns candidates to teams post-offer. The lack of specificity in JD is by design.
- The timing overlap with major layoffs (8,000 cuts, May 2026) is a legitimate concern. This posting may be a backfill, a retained open headcount, or a posting that predates the layoff announcement.
- The 85% LCA volume drop is significant -- Meta is filing fewer H-1B applications in FY2026. For F-1 candidates, this is a risk signal worth confirming with the recruiter before investing heavily in prep.
- Recommend: verify posting is still active by applying or contacting a Meta recruiter, and ask about team placement, layoff-affected headcount, and H-1B policy early in the process.

---

## H) Draft Application Answers

*Score is 3.2/5 -- below 4.0 threshold. Block H not generated.*

*Given the layoff context and legitimacy concerns, investing heavily in application materials is not recommended until: (a) posting confirmed as backfill/active headcount and (b) H-1B sponsorship status for F-1 2027 grads is confirmed with recruiter.*

---

## Keywords Extracted (ATS)

Software Engineer, C++, Python, TypeScript, JavaScript, React, Node.js, PostgreSQL, SQL, distributed systems, gRPC, Protocol Buffers, backend, infrastructure, production systems, test coverage, data analysis, software engineering, system design, web applications

---

## Machine Summary

```yaml
report: "039"
company: "Meta"
role: "Software Engineer"
date: "2026-06-02"
score: 3.2
archetype: "Systems Software Engineer / Backend Engineer"
location: "Menlo Park, CA"
remote: "onsite"
comp_posted: "$222,950--$250,250 base + bonus + equity"
comp_score: 5.0
fit_score: 3.5
legitimacy: "Proceed with Caution"
f1_risk: "medium-high -- H-1B LCA volume dropped 85% in FY2026; still apply but confirm sponsorship early"
recommendation: "Proceed with caution -- apply if Meta specifically desired; verify sponsorship and active headcount before heavy prep"
blockers:
  - "May 2026 layoffs (8K cuts, 6K planned hires cancelled) create headcount uncertainty"
  - "H-1B LCA volume down 85% in FY2026 -- F-1 risk elevated"
  - "Generic JD -- no team, no stack, no scope"
strengths:
  - "All minimum quals met (C++, Python, SQL, React, BS CS expected 2027)"
  - "Google Chrome production C++ directly relevant"
  - "Comp posted well above target range ($222K--$250K base)"
```
