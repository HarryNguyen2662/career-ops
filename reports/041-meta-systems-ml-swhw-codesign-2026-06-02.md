# Evaluation: Meta -- Software Engineer, Systems ML - SW/HW Co-design

**Date:** 2026-06-02
**URL:** https://www.metacareers.com/profile/job_details/1108948753413269/
**Archetype:** ML / AI Infrastructure Engineer (hybrid: Systems Software Engineer)
**Score:** 3.6/5
**Legitimacy:** Proceed with Caution
**PDF:** pending

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | ML / AI Infrastructure Engineer + Systems Software Engineer (hybrid) |
| **Domain** | AI/ML infrastructure, hardware acceleration, SW/HW co-design |
| **Function** | Build + optimize ML systems; define benchmarks; mentor engineers |
| **Seniority** | Mid-level (E5 implied by scope: "drive large efforts", "mentor engineers") -- not new grad |
| **Location** | Sunnyvale, CA + 1 additional location; onsite |
| **Compensation** | $121,992--$181,000/year base + bonus + equity + benefits |
| **Team size** | Not specified |
| **TL;DR** | Systems ML role targeting hardware-aware ML infra engineers: GPU/HW accelerators, ML compilers, performance optimization, PyTorch-level. Not a new-grad entry point -- scope implies E4+ minimum. |

---

## B) Match with CV

### Requirements vs CV

| JD Requirement | Match | CV Evidence |
|----------------|-------|-------------|
| Bachelor's in CS/CE or equivalent | Strong | Georgia State BS CS, GPA 3.75, expected May 2027 |
| C/C++ or Python experience | Strong | C++ (Google Chrome IPC, lock-free trie); Python (TiMoto vLLM, Django, FastAPI) |
| ML infrastructure / AI algorithms | Moderate | TiMoto: vLLM/PagedAttention, continuous batching, gRPC inference layer; sub-50ms p99 |
| Hardware accelerator arch / GPU arch / ML compilers | Weak | vLLM implies GPU-aware serving, but no explicit GPU kernel writing, CUDA, or compiler work |
| Machine learning compilers / SW/HW co-design | Weak | No direct experience; cv.md does not mention CUDA, Triton, XLA, or compiler backends |
| High performance computing / performance optimizations | Moderate | Lock-free trie (96% latency reduction) at Google; gRPC deadlock fix; sub-50ms p99 inference |
| ML frameworks (PyTorch, etc.) | Moderate | PyTorch listed in skills; used for model serving but no training or kernel optimization |
| Distributed systems / on-device algorithms | Moderate | gRPC, multi-AZ ECS, exactly-once semantics, circuit breakers |
| Goal-setting, cross-team influence, mentorship | Weak | 3-person team -- too small to demonstrate org-level influence expected at E4-E5 |
| Recommendation / ranking models (preferred) | Weak | No ad/rec system experience |
| AI tools integration (preferred) | Strong | vLLM deployment, Claude Code, Cursor in skills section |

### Skills Match Summary

**Strong:** C++, Python, ML serving (vLLM), performance measurement mindset, distributed systems  
**Moderate:** PyTorch (usage only, not kernel-level), GPU-adjacent (vLLM runs on GPU but no CUDA work)  
**Weak/Absent:** Hardware accelerator architecture, ML compilers (XLA/Triton/TVM), SW/HW co-design, GPU kernel writing, recommendation/ranking models, cross-team org influence at Meta scale

### Gaps and Mitigation

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| GPU/HW accelerator architecture | Hard -- core of the role | Adjacent: vLLM manages GPU memory (PagedAttention). Frame KV cache fragmentation fix as memory-hierarchy optimization. Does not fully cover CUDA kernel or hardware design experience. |
| ML compiler knowledge | Hard -- "SW/HW co-design" is the title | No direct mitigation available. Could study PyTorch compiler (torch.compile, TorchScript) and mention awareness. |
| E4-E5 seniority gap | Hard -- role expects "drive large efforts" and "mentor" | At 3-person team, framing as founding engineer partially mitigates. Will likely be screened for level. |
| Recommendation / ranking models | Soft (preferred) | Not on profile -- skip |
| No CS degree yet (in process) | Not a blocker | JD says "currently has or is in the process of obtaining" -- explicit allowance |

**Overall match: Moderate-Weak.** The role is a specialized ML systems + hardware position at likely E4-E5 level. Harry's profile is production ML serving (vLLM) and distributed backend, which is adjacent but not the core of SW/HW co-design.

---

## C) Level and Strategy

### Level Analysis

| | JD Signals | Harry's Natural Level |
|--|------------|----------------------|
| **Level implied** | E4-E5 ("drive large efforts", "mentor engineers", "influence partners", "deep data-driven analysis") | E3 new grad 2027 |
| **Gap** | 2-3 years typical experience gap | New grad with strong internship + startup experience |

### "Sell Senior Without Lying" Plan

1. **Lead with production ownership:** "Primary engineer for backend, infra, and ML serving on a 3-person team -- not a student project, production traffic with SLOs." Avoids sole-engineer claim; highlights breadth and accountability.
2. **Quantified hardware-adjacent work:** "vLLM/PagedAttention selection specifically to eliminate KV cache memory fragmentation under concurrent GPU load -- chose the serving engine based on GPU memory management properties." This bridges toward hardware-aware thinking without overclaiming.
3. **Performance engineering depth:** Chrome lock-free trie story (mutex -> lock-free, 96% latency cut) demonstrates systems-level profiling and correctness thinking -- closest analog to hardware optimization mindset.
4. **Tradeoff framing:** "Benchmarked vLLM continuous batching vs naive batching under concurrent load before committing -- zero OOM in production is the result of the methodology, not luck."

### "If They Downlevel" Plan

- E3 new grad band at Meta is $170K-$215K TC based on Levels.fyi. If offered E3, comp is favorable -- accept if equity vesting and growth path to E4 within 18 months is confirmed.
- Ask for performance criteria and promotion timeline in writing.
- Note: base in JD ($121K-$181K) may understate TC (bonus + RSUs typically add 30-50% at Meta E3-E4).

---

## D) Comp and Demand

### Compensation Data

| Level | Base | Bonus | RSUs | Total TC | Source |
|-------|------|-------|------|----------|--------|
| E3 (new grad) | ~$170K-$180K | ~$20K-30K | ~$50K-80K/yr | ~$220K-$280K | Levels.fyi, Blind |
| E4 | ~$200K-$230K | ~$30K-50K | ~$100K+/yr | ~$320K-$400K | Levels.fyi |
| JD posted range | $121,992-$181,000 | + bonus | + equity | Estimated $200K-$280K TC at E3 | JD + market data |

**Assessment:** The posted base ($121K-$181K) is below top-of-band for Meta E3 new grads per Levels.fyi and Blind, but total compensation (+ RSUs + bonus) typically reaches $220K-$280K. This is above Harry's $150K-$200K base target and meaningfully above the $140K walk-away -- **comp is strong if TC is competitive.**

**Harry's target:** $150K-$200K base. Meta E3 base at ~$170K-$180K is within range. TC of $220K-$280K substantially exceeds target. **Comp is a positive signal if level is E3.**

**Demand for SW/HW co-design:** Specialized and growing. Meta, Google, Apple, Nvidia, and Qualcomm all compete for this profile. Harder to fill than generic SWE, legitimately stays open longer. Harry's profile is not the target persona (GPU kernel engineers, ML compiler researchers) but the adjacent ML serving experience is relevant.

Sources: [Levels.fyi Meta SWE salaries](https://www.levels.fyi/companies/meta/salaries/software-engineer) | [6figr Meta SWE 2026](https://6figr.com/us/salary/meta--software-engineer) | [Leon Consulting Meta Salary Breakdown 2026](https://leonstaff.com/blogs/meta-software-engineer-salary-2026/)

---

## E) Customization Plan

| # | Section | Current Status | Proposed Change | Why |
|---|---------|---------------|-----------------|-----|
| 1 | **Summary** | "Distributed systems & ML serving" | Add: "GPU-aware ML serving: vLLM/PagedAttention for KV cache memory optimization under concurrent load" | Directly maps to hardware-aware ML infra; shows GPU memory hierarchy awareness |
| 2 | **TiMoto vLLM bullet** | "Architected vLLM inference engine with PagedAttention -- eliminated KV cache memory fragmentation" | Expand: "...applied GPU memory paging analogy (PagedAttention maps KV cache to non-contiguous blocks, mirroring OS virtual memory) to eliminate fragmentation under concurrent inference; validated with load tests at Nx production traffic" | Demonstrates HW/SW co-design thinking at serving layer |
| 3 | **Google Chrome bullet** | "lock-free concurrent trie search eliminating mutex contention" | Add: "...analyzed memory access patterns and cache line behavior to design lock-free structure; verified linearizability proof before shipping to stable" | Shows hardware-conscious low-level thinking (cache lines, memory ordering) |
| 4 | **Skills section** | "ML & AI Infrastructure: vLLM, PagedAttention..." | Add: "GPU memory management, continuous batching, inference SLO benchmarking" | Reinforces ML systems vocabulary from the JD |
| 5 | **LinkedIn headline** | Current: "CS @ Georgia State (May 2027)" | Update: "ML Systems Engineer -- vLLM/PagedAttention · C++/Python · Google Chrome · Distributed Inference · Georgia State 2027" | Keywords match this JD archetype |

**Top 5 LinkedIn changes:**
1. Headline: add "ML Systems" and "inference optimization" keywords
2. About section: lead with "I build ML serving infrastructure that runs at production scale" -- match JD language
3. TiMoto experience: expand vLLM selection rationale (GPU memory management decision)
4. Google experience: frame lock-free trie as low-level systems + memory optimization
5. Skills: add "High Performance Computing", "ML Systems", "GPU Memory Management"

---

## F) Interview Plan

### STAR+R Stories Mapped to JD Requirements

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---------------|-------|---|---|---|---|------------|
| 1 | Hardware-aware ML systems | **vLLM/PagedAttention selection** | TiMoto needed concurrent LLM inference; naive batching caused OOM under load | Evaluate serving engines and deploy without OOM at production concurrency | Benchmarked naive inference vs vLLM; chose vLLM for non-contiguous KV cache block management (GPU memory paging analog); deployed with continuous batching | Zero OOM failures; sub-50ms p99; 100% evaluation success rate | Would run GPU memory profiling earlier (before choosing the engine) to have quantitative evidence for the decision, not just architecture comparison |
| 2 | Performance optimization / benchmarking | **Lock-free trie at Google Chrome** | Chrome settings search hitting 1,200ms p99; mutex contention on trie traversal | Cut p99 to target without correctness regression | Profiled hot path; replaced mutex-protected trie with lock-free structure; verified linearizability before shipping | 96% latency reduction; zero production regressions; shipped to Chrome stable (3B+ users) | Lock-free structures need correctness proof, not just benchmarks; verified linearizability as precondition to ship |
| 3 | Debugging / concurrent systems | **gRPC deadlock fix at TiMoto** | Concurrent gRPC calls from 3 clients causing intermittent deadlocks in evaluation service | Debug and eliminate deadlock without service restart | Traced shared resource acquisition conflict in handler sequencing; identified circular lock acquisition; redesigned call sequencing with consistent ordering | 100% evaluation success rate; sub-50ms p99; zero recurrence | Always instrument concurrent call paths with distributed tracing before launch; lock acquisition order diagram would have caught this pre-production |
| 4 | Cross-team influence / mentorship | **C++ IPC design at Google Chrome** | Chrome infrastructure team needed IPC transport layer between browser components | Design IPC, get it reviewed by senior engineers, and ship to stable | Chose Protocol Buffers over custom serialization (schema evolution rationale); wrote design doc; got reviews from senior Chrome engineers; shipped to stable | 3B+ active users; sub-50ms p99; 10K+ req/sec | Design docs are force multipliers -- senior engineers gave much better feedback once the decision rationale was written down |
| 5 | Goal-setting / project scope | **Multi-AZ circuit breaker architecture** | TiMoto single-AZ; zone failure = full outage; infra budget constrained | Design multi-AZ failover with auto-rollback within startup cost constraints | Designed topology with Terraform IaC, CloudWatch alarms, circuit breaker, health-check-triggered rollback; modeled cost tradeoffs before implementation | 99.9% uptime; 44% cost reduction ($40-60/mo); zero unplanned outages | AZ isolation is a Day 1 infrastructure requirement, not a retrofit -- cost to add later is disproportionate |
| 6 | Define use cases / methodology / benchmarks | **gRPC + vLLM load testing methodology** | Need to validate inference SLOs before production launch; no existing benchmarks | Define benchmarking methodology for concurrent LLM evaluation requests | Defined concurrent load profiles (N simultaneous gRPC calls), measured p99 latency and OOM rate at each concurrency level, used results to tune continuous batching queue depth | Validated sub-50ms p99 at production concurrency; zero OOM in production | Benchmarks should simulate real usage patterns, not peak theoretical load -- the queue depth tuning came from realistic workload simulation, not synthetic extremes |

**Red-flag questions and how to answer them:**

- *"Do you have experience with CUDA or GPU kernels?"* → "My experience is at the ML serving layer -- vLLM/PagedAttention, KV cache management, continuous batching. I understand GPU memory hierarchy at the system level but haven't written CUDA kernels directly. I'm studying PyTorch compiler internals (torch.compile, TorchScript) and would ramp into lower-level work with mentorship."
- *"This role expects E4-E5. Where do you see yourself level-wise?"* → "I've been the primary backend, infra, and ML serving engineer on a production team -- full ownership of system design through production incidents. I'd expect to be evaluated at the level my work demonstrates; I'm open to how Meta calibrates that in the loop."
- *"Do you have sponsorship?"* → Use the F-1 negotiation script from profile.yml.

**Recommended case study to present:** TiMoto vLLM serving architecture. Walk through: problem (OOM under concurrent load) → decision tree (naive vs vLLM, why PagedAttention) → deployment (gRPC front-end, continuous batching config) → results (zero OOM, sub-50ms p99). Shows systems thinking, GPU memory awareness, and production discipline.

*Story bank additions -- these stories are already present or closely related to existing entries. No new additions needed this evaluation.*

---

## G) Posting Legitimacy

### Signals Analysis

| Signal | Finding | Weight |
|--------|---------|--------|
| **Apply button** | Active "Apply now" button confirmed via Playwright | Positive |
| **Posting freshness** | No date visible on page; separate job ID from #039 (3414246448833665 also exists for same title) | Neutral |
| **JD specificity** | High specificity: names PagedAttention-adjacent concepts (ML compilers, HW accelerators, GPU arch, PyTorch, numerics, SW/HW co-design). Not generic. | Positive |
| **Comp transparency** | $121,992-$181,000/year explicitly stated + bonus + equity | Positive |
| **Team/org context** | "Research & Development teams" -- somewhat generic, no specific team named | Neutral |
| **Requirements realism** | "Currently obtaining" degree explicitly allowed -- honest new-grad framing mixed with "drive large efforts" and "mentor" expectations (E4-E5 scope at E3 pay) | Neutral/Concerning |
| **Meta layoffs** | 8,000 layoffs May 2026 (~10% workforce) to fund AI infrastructure; **BUT** Meta stated active hiring for AI/ML/infrastructure roles | Neutral (role-dependent) |
| **Meta H-1B LCA** | Prior report #039 noted 85% drop in Meta H-1B LCA filings for generic SWE. SW/HW co-design is specialized -- harder to fill domestically; sponsorship risk may be lower for this role | Neutral |
| **Reposting check** | No Meta SW/HW co-design role in scan-history.tsv. Different job ID from #039. | Positive |
| **Role-company fit** | Meta's AI infrastructure investment ($125-145B capex 2026) directly motivates SW/HW co-design hiring | Positive |

**Assessment: Proceed with Caution**

**Reasoning:** Multiple positive legitimacy signals (specific JD, explicit comp, active apply button, unique job ID, Meta's confirmed AI infra hiring push). The main caution flags are: (1) Meta's 8,000-person layoff and hiring freeze affecting general SWE, (2) the role's seniority mismatch vs posted compensation (E4-E5 scope at E3-ish base), suggesting the role may be hard to fill or may be intentionally recruiting at senior levels. This is a specialized niche (HW/ML co-design) that Meta would legitimately have open and actively hiring -- not a ghost job signal.

**For Harry specifically:** Sponsorship risk from report #039 (85% H-1B LCA drop) is partially mitigated here because specialized ML systems roles are harder to staff with domestic talent alone. Still recommend asking recruiter directly about sponsorship policy for this specific team.

---

## Keywords Extracted

`ML systems`, `SW/HW co-design`, `hardware accelerators`, `GPU architecture`, `ML compilers`, `PyTorch`, `ML infrastructure`, `high performance computing`, `performance optimization`, `AI infrastructure`, `machine learning frameworks`, `distributed systems`, `numerics`, `inference engine`, `benchmarking`, `data-driven analysis`, `AI system design`, `responsible AI`, `agent orchestration`, `C++`, `Python`, `deep learning`
