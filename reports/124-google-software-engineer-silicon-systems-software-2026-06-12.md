# Evaluation: Google — Software Engineer, Silicon Systems Software

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/130983342701978310-software-engineer/
**Archetype:** Systems Software Engineer (Embedded OS / Silicon / Hardware-Software Interface)
**Score:** 1.5/5
**Legitimacy:** High Confidence
**PDF:** N/A (score below 3.0 threshold)

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Silicon Systems Software — hardware-software interface engineer for Google's Tensor SoC and Pixel devices; embedded OS, low-level C/C++/Rust, hypervisors, drivers, firmware, Android kernel |
| Domain | Google Silicon / Pixel hardware — Tensor SoC systems software; hardware/software co-design with silicon architecture, product, and Android teams; performance modeling, power analysis |
| Function | Build — low-level system software (C/C++/Rust) at the hardware boundary; prototypes/POCs across simulation, emulation, and physical silicon; performance and power optimization |
| Seniority | Mid, L3–L4 — 2-year minimums; same comp band as other Google SWE roles |
| Location | San Diego, CA / Mountain View, CA |
| Comp | **$147,000–$211,000 base + 15% bonus + equity** — L3/L4 Google range |
| Company | Google Silicon (part of Google Devices & Services / Hardware team) — builds Tensor SoC, the custom ARM-based chip powering Pixel phones and Generative AI workloads on-device |
| TL;DR | Hard domain mismatch — this requires embedded OS experience (hypervisors, firmware, drivers, SoC systems) that Harry has zero background in. C++ is present but user-space application C++ (Chrome) is a different subdomain from embedded/kernel C++. Same structural mismatch as #119 (Android mobile, 2.0). Score 1.5 — SKIP. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|-------------|----------|
| **Bachelor's degree or equivalent** | Georgia State BS CS, GPA 3.75, Expected May 2027 | ✅ Direct |
| **2 years C, C++, or Rust (minimum, hard)** | Chrome: C++ IPC transport + lock-free trie (3-month internship); Rust in skills (not production). Total: ~3 months production C++ | ❌ Language present; duration and domain both short — Chrome C++ is user-space application code, not embedded/kernel C++ |
| **2 years embedded operating systems (minimum, hard)** | No embedded OS experience. TiMoto: distributed cloud systems (AWS ECS, not embedded). Chrome: user-space application on standard OS. No hypervisors, drivers, firmware, or RTOS experience | ❌ Hard blocker — zero embedded OS background |
| **Performance modeling, performance analysis, or simulation tools (minimum)** | Chrome: profiled critical path (1,200ms → lock-free CAS) using Chrome DevTools; TiMoto: CloudWatch + Prometheus/Grafana production profiling | ⚠️ Performance analysis ✅; silicon simulation tools (e.g., gem5, QEMU, cycle-accurate simulators) ❌ — different toolchain and methodology |
| **Embedded systems, OS internals (preferred)** | No hypervisors, device drivers, firmware, RTOS, or embedded Linux. Coursework: OS (studied OS concepts, not kernel development) | ❌ Preferred miss — no practical embedded OS work |
| **Android system architecture (preferred)** | No Android development or Android system-layer (Linux kernel, system services, HAL) experience | ❌ Hard miss — same as #119 Android mobile role |
| **System performance, power consumption, memory management + Python (preferred)** | Chrome: memory safety analysis (Protobuf schema evolution); TiMoto: vLLM KV cache memory fragmentation; Python in skills. BUT: mobile SoC power modeling and memory management at silicon level is a different domain | ⚠️ Memory management philosophy present; mobile power analysis (DVFS, thermal throttling, big.LITTLE) ❌ |
| Low-level C/C++/Rust for Tensor SoC | Chrome: user-space IPC (Mojo/Protobuf serialization, application-layer C++). Not SoC systems software | ❌ C++ domain mismatch — application-layer vs silicon systems layer |
| Hardware/software co-design | No hardware background. Pure software engineer path (no FPGA, HDL, hardware architecture, or SoC design experience) | ❌ No hardware context |

**Gaps:**

1. **Embedded OS experience (hard blocker, primary):** The minimum quals explicitly require "2 years of experience working with embedded operating systems." Harry has none — no RTOS, no device driver development, no hypervisor work, no firmware, no embedded Linux. This is a categorical mismatch, not a gap in quantity.

2. **Silicon-domain C++/Rust (hard blocker):** Harry's C++ is Chrome application code (Mojo IPC, Protocol Buffers, Chromium observer pattern). Silicon systems C++ is a completely different subdomain — writing device drivers, HAL implementations, SoC initialization sequences, power management stubs. These require knowledge of memory-mapped I/O, interrupt handling, real-time constraints, and hardware register interaction. Not transferable from application-layer C++.

3. **Android system architecture (hard gap):** The preferred qualifier asks for Android system architecture (Linux kernel, system services). Harry has zero Android background — same as the #119 Android role (XR/Mobile, score 2.0 SKIP).

4. **Performance modeling for silicon (domain gap):** Harry's performance work is application profiling and latency reduction (p99, mutex contention). Silicon performance modeling uses cycle-accurate simulators, power analysis (DVFS, thermal), and architectural trade-off tools — a specialized discipline not adjacent to Harry's background.

5. **Hardware/software co-design context:** Role requires cross-functional work with Hardware, Architecture, and Silicon teams. Harry has no hardware-adjacent experience (no FPGA, no HDL, no circuit design, no chip architecture).

---

## C) Level and Strategy

**Level detected:** L3–L4 — same comp band as other Google SWE roles, but this is a specialist embedded systems role.

**Why this is a harder mismatch than #119 (Android mobile, 2.0):**
- #119 had a mobile language barrier (Kotlin/Java/Swift) but is still user-space software
- This role requires actual OS-level and hardware-interface experience — firmware, hypervisors, drivers — which is a more fundamental domain shift than just language
- Harry's C++ is present, which narrowly separates this from #119's language blocker, hence 1.5 rather than 2.0

**If Harry applies anyway (policy: apply regardless of blockers):**
- State honestly: "I have production C++ at Google's standard (Chrome stable) and strong systems software fundamentals; I haven't worked in embedded OS/silicon domains but I have the OS coursework and C++ foundation to grow into it"
- Flag: This is a multi-year investment to become a realistic candidate — not just experience quantity but categorical domain knowledge
- The Tensor SoC team likely interviews for domain-specific knowledge (interrupt handlers, memory-mapped I/O, power management stubs) that Harry has not studied

**Better path for Harry:** The Systems Software archetype is adjacent but the right entry point would be through OS-adjacent roles (e.g., Chrome OS kernel team, Android framework layer, or embedded systems internship) before targeting silicon systems software. Harry's lock-free trie and Chrome C++ are the foundation — add OS/kernel context.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| Google stated base | $147,000–$211,000 |
| Bonus | 15% target |
| Equity | ~$100K–$200K/4yr RSU at L3 |
| Estimated TC | ~$200K–$280K at L3/L4 |
| Harry target | $150K–$200K TC |
| Assessment | Comp is excellent and meets target — but comp is not the constraint here. Domain mismatch is the blocker. |
| Google H-1B | Google sponsors H-1B. Silicon team in San Diego / Mountain View — sponsorship available. |

---

## E) Customization Plan

No LaTeX CV generated — score 1.5/5 is below the 3.0 threshold.

If Harry applies anyway, minimum viable framing (truthful, not overclaiming):

| # | Section | Framing | Why |
|---|---------|---------|-----|
| 1 | Chrome C++ | Emphasize low-level nature: "C++ IPC transport layer at Google's security review standard — memory safety tradeoffs (Protocol Buffers schema evolution), lock-free data structures (CAS operations)" | Gets as close to systems-level C++ as possible without overstating |
| 2 | Chrome lock-free trie | "Profiled and optimized Chrome's critical path using performance analysis — identified mutex contention, redesigned with lock-free CAS" | Maps to "performance analysis" minimum qualifier |
| 3 | TiMoto vLLM | "Memory management for production ML serving — KV cache fragmentation analysis and zero-copy optimization" | Maps obliquely to memory management preferred qualifier |
| 4 | Honest gap statement | In cover letter: "I'm applying from a user-space systems background — Chrome C++ and distributed systems; I haven't worked at the firmware or driver layer. I'm targeting this role as an entry into silicon systems software." | Better to acknowledge than be rejected for overclaiming |

---

## F) Interview Plan

**Abbreviated** — full investment not recommended at score 1.5.

| LP area | Harry's best story | Gap |
|---------|-------------------|-----|
| Low-level C++ | Chrome IPC transport + lock-free trie | Strong story; interviewers will probe deeper into kernel/driver territory |
| Performance analysis | Chrome 96% latency reduction via profiling | Application profiling ≠ silicon performance modeling |
| OS concepts | OS coursework; distributed systems concepts | Conceptual only; no implementation at kernel level |
| Systems design | TiMoto distributed systems design | Cloud distributed ≠ embedded systems design |

**Red-flag questions:**
- *"What's your embedded OS or driver experience?"* → "I don't have embedded OS experience — my OS work is at the application layer (Chrome C++ on standard Linux/macOS) and distributed systems level (gRPC, multi-AZ). I'm applying to understand how deep the gap is and whether Google has a growth path into silicon systems software from an application/systems software background."
- *"Have you worked with Android kernel or HAL?"* → "No — I've worked with the Chrome browser codebase in C++ but not at the Android system layer. I'm aware that's a significant gap for this role."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active "Apply" on Google Careers — confirmed via Playwright | Positive |
| Comp disclosed | $147,000–$211,000 + 15% bonus + equity — transparent | Positive |
| JD specificity | Named product (Tensor SoC, Pixel), specific technical scope (hypervisors, drivers, firmware, Android kernel, power modeling), cross-functional team structure described | Positive |
| Location choice | San Diego / Mountain View — San Diego is Google's Silicon hardware team hub; matches known Tensor SoC location | Positive |
| Google Silicon strategy | Google Tensor SoC (Gen 1 in Pixel 6, Gen 2 in Pixel 7, Gen 3 in Pixel 8) is a confirmed, active product line; hiring for next generation is consistent | Positive |

**Context:** Google's Silicon team (Google Silicon) is a real, large team building custom Tensor SoCs for Pixel devices and for on-device AI inference. San Diego is their primary silicon engineering location. This is not a ghost posting — it's for an active, multi-year product roadmap.

---

## Keywords extracted

Software Engineer, Silicon Systems Software, Tensor SoC, Pixel, embedded operating systems, C++, C, Rust, hardware-software interface, hypervisors, drivers, firmware, Android, Linux kernel, system services, performance modeling, simulation, power consumption, memory management, hardware co-design, San Diego, Mountain View

---

## Machine Summary

```yaml
company: Google
role: "Software Engineer, Silicon Systems Software"
date: 2026-06-12
url: https://www.google.com/about/careers/applications/jobs/results/130983342701978310-software-engineer/
score: 1.5
archetype: "Systems Software Engineer (Embedded OS / Silicon / Hardware-Software Interface)"
location: "San Diego, CA / Mountain View, CA"
comp_range: "$147,000–$211,000 base + 15% bonus + equity; TC ~$200K–$280K at L3/L4; meets target but domain mismatch is the blocker"
visa_risk: "F-1 — Google sponsors H-1B; sponsorship not the concern here"
legitimacy: High Confidence
recommendation: "SKIP (1.5/5) — hard blocked by embedded OS requirement (zero embedded/kernel experience: no hypervisors, firmware, drivers, Android kernel); C++ is present (Chrome) but user-space application code is categorically different from silicon systems C++; same structural mismatch as #119 (Android mobile, 2.0). Apply per policy only if Harry has specific interest in pivoting to embedded/silicon — requires honest framing about the gap. No LaTeX CV generated."
```
