# Evaluation: Qualcomm — Entry level & Senior Software Engineer, Core AI Software (Onsite)

**Date:** 2026-06-06
**URL:** https://careers.qualcomm.com/careers/job/446718018413?hl=en-US
**Archetype:** ML/AI Infrastructure Engineer (edge inference / embedded AI)
**Score:** 3.7/5
**Legitimacy:** High Confidence
**PDF:** output/072-qualcomm-core-ai-software-harry-nguyen-2026-06-06.pdf

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | ML/AI Infrastructure Engineer — edge inference, LLM runtime on Snapdragon |
| Domain | On-device AI / Edge AI / LLM inference at the chip level |
| Function | Build — QAIRT SDK, Genie (GenAI inference extensions), DNN execution |
| Seniority | Entry level OR Senior (dual req) |
| Remote | **On-site San Diego, CA** |
| Comp | $140,800–$211,200 base + bonus + RSU |
| TL;DR | Build the AI runtime stack that runs LLMs and DNNs on Qualcomm's Snapdragon chips — C++ focused, low-power edge inference. Harry's cloud-based ML serving experience directly maps to the inference side; embedded/edge domain is a real gap. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| C/C++ proficiency (required) | Google Chrome: C++ IPC transport layer, lock-free trie; production at 3B users | ✅ Strong |
| LLM / GenAI familiarity (preferred) | TiMoto: vLLM + PagedAttention, zero OOM production inference | ✅ Direct |
| AI inference optimization | TiMoto: sub-50ms p99, continuous batching, KV cache management | ✅ Strong |
| Debug complex issues | gRPC deadlock root-cause at TiMoto; lock-free correctness at Chrome | ✅ Strong |
| Data structures + algorithms | Lock-free trie (Chrome), distributed state reasoning (Pulumi Raft/Paxos study) | ✅ |
| Linux development | AWS ECS/EC2 infra (TiMoto), CI/CD pipelines | ✅ Basic |
| BS in CS | Georgia State BS CS, GPA 3.75, May 2027 | ✅ |
| Embedded software (preferred) | Not in CV | ❌ Gap |
| Low-power / resource-constrained inference | TiMoto is cloud-based (AWS), not embedded | ⚠️ Partial |
| QAIRT / QNN / Genie experience | Not in CV (expected — internal tools) | ❌ Expected |
| CMake build environments | Not explicit | ❌ Minor gap |

**Gaps:**
1. **Embedded/edge inference** — TiMoto is cloud-based vLLM, not on-device. Mitigation: principles of inference efficiency (KV cache, batching, latency optimization) transfer; frame as "optimized inference for production constraints, ready to apply to device constraints."
2. **Low-power hardware constraints** — No embedded systems experience. Mitigation: entry-level path explicitly accepts project/internship experience; hardware intuition can be learned.
3. **San Diego relocation** — Harry is open; not a blocker.

---

## C) Level and Strategy

**Level detected:** Dual req (entry + senior). Harry fits entry-level by calendar time but has production depth above typical entry.

**Sell entry-level with unusual depth:**
- "I've run LLM inference in production — I know what KV cache fragmentation costs you at runtime, why PagedAttention matters, and how to tune batching for latency SLOs. The domain shifts from cloud to device, but the inference engineering thinking is the same."
- Chrome C++ IPC to 3B users demonstrates production-grade C++ beyond coursework.

**If pushed on embedded gap:**
- "I've optimized inference on the serving side (latency, memory, throughput). The hardware constraints change, but the performance engineering instincts transfer. I'm actively studying Qualcomm's AI Stack."

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Qualcomm stated range | $140,800–$211,200 base + bonus + RSU |
| Harry target | $150K–$200K |
| Harry minimum | $140K |
| Entry-level likely band | $140K–$165K base |

Comp at entry band ($140K-$165K) sits right at Harry's floor-to-target range. RSU at Qualcomm (public company, ~$180B market cap) adds meaningful upside. Total comp at entry likely $160K-$200K with bonus + RSU.

---

## E) Customization Plan

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | TiMoto bullet order | gRPC deadlock first | Lead with vLLM/PagedAttention inference bullet | AI inference optimization is the core match |
| 2 | TiMoto vLLM bullet | "LLM serving engine" | Add "KV cache memory optimization, inference latency SLOs" — device-adjacent language | Qualcomm cares about memory/latency trade-offs on constrained hardware |
| 3 | Chrome bullet order | C++ IPC leads (already) | Keep C++ IPC first — required skill | C++ is the primary requirement |
| 4 | Skills section | Distributed Systems leads | Swap: ML & AI Infrastructure leads, then Languages (C++ first) | Role is ML infra + C++; lead with those |
| 5 | Languages row | C++ listed third | Move C++ to first position in languages | C/C++ is the only required programming language |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | LLM inference optimization | TiMoto vLLM engine | OOM crashes under concurrent production LLM load | Zero OOM, sub-50ms p99 | vLLM + PagedAttention; analyzed KV cache fragmentation; tuned continuous batching | Zero OOM failures at production traffic | KV cache fragmentation is a latency and memory multiplier — understanding memory layout is the key |
| 2 | C++ production quality | Google Chrome C++ IPC | Chrome needed IPC between browser process and settings; schema must evolve | Ship to 3B users without breaking | Chose Protobuf over custom serialization; design doc; senior code review | Chrome stable, sub-50ms p99, 10K+ req/sec | Serialization choices outlive features — design for evolution |
| 3 | Debug complex issues | gRPC deadlock root-cause | Production deadlock under concurrent gRPC evaluation calls | Find root cause without senior help, fix without regression | Traced shared resource acquisition with logging; redesigned call sequencing | 100% success rate, sub-50ms p99 restored | Concurrent code requires explicit ownership models; instrument concurrency from day one |
| 4 | Performance optimization | Chrome lock-free trie | 1,200ms p99 settings nav in production Chrome | 96% latency reduction without correctness regression | Lock-free concurrent trie; linearizability proof by construction | 96% reduction, zero regressions | Profile before optimizing; then prove correctness mathematically |
| 5 | Cross-functional collaboration | Chrome infra team + code review | Joining Chrome infra as intern; zero Chromium context | Ramp in weeks, ship production C++ | Read design docs; followed Chrome code review culture; multiple senior reviewers | Changes in production branch at 3B+ scale | Large codebases: reading code is 70% of the work |

**Recommended case study:** TiMoto AI inference stack — "I built cloud LLM inference, here's the architecture, constraints I optimized for (memory, latency, concurrency), and how those principles translate to edge." Frame the conversation around inference engineering, not cloud vs. edge.

**Red-flag questions:**
- *"No embedded experience — how would you ramp?"* → "My inference optimization work at TiMoto gives me the performance engineering instincts. The domain shifts from DRAM to L2/L3 cache, from cloud GPU to Snapdragon NPU — I'm studying QAIRT and will have hands-on ramp in first 90 days."
- *"Work authorization?"* → "F-1 OPT from May 2027. I'll need H-1B sponsorship long-term. With Qualcomm's 3,700+ LCAs in FY2025 and 99% approval rate, I'm confident this is manageable — happy to discuss timing."
- *"Graduation?"* → "May 2027. Flexible on start date for the right role."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active | Positive |
| JD specificity | Named SDK (QAIRT, Genie), specific tech (C++, Linux, LLM), team context | Positive |
| Comp disclosed | $140,800–$211,200 explicitly stated | Positive |
| Company status | Qualcomm — public, ~$180B market cap, active AI hiring | Positive |
| Similar jobs | 10+ similar active roles on same careers page | Positive |
| H-1B track | 3,700+ LCAs FY2025, 99% approval — top-tier sponsor | Positive |

---

## Keywords extracted

C++, C/C++, LLM, generative AI, inference, QAIRT, Genie, AI Stack, Snapdragon, machine learning, embedded, Linux, low-power, latency, memory footprint, neural network, DNN, debugging, performance optimization, SDK, runtime framework, edge AI

---

## Machine Summary

```yaml
company: Qualcomm
role: Entry level & Senior Software Engineer, Core AI Software
date: 2026-06-06
url: https://careers.qualcomm.com/careers/job/446718018413
score: 3.7
archetype: ML/AI Infrastructure Engineer (edge inference)
location: San Diego, CA (on-site)
comp_range: "$140,800–$211,200 base + bonus + RSU"
visa_risk: "F-1 — H-1B strong positive (3,700+ LCAs FY2025, 99% approval)"
legitimacy: High Confidence
recommendation: "Conditional apply — strong C++ and LLM inference match; embedded/edge gap manageable at entry level; Qualcomm is excellent H-1B sponsor"
```
