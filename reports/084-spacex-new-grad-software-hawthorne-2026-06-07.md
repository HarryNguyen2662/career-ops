# Evaluation: SpaceX — New Graduate Engineer, Software

**Date:** 2026-06-07
**URL:** https://job-boards.greenhouse.io/spacex/jobs/8493079002
**Archetype:** Systems Software Engineer
**Score:** 2.5/5
**Legitimacy:** High Confidence
**PDF:** N/A (score below 3.0 threshold)

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| Archetype | Systems Software Engineer (primary) + Backend / Distributed Systems (secondary) |
| Domain | Aerospace / Launch / Satellite — autonomous flight software, simulations, vehicle systems |
| Function | Build — design, test, integrate, and deploy autonomous software systems |
| Seniority | New Graduate (Bachelor's/Master's/PhD graduating 2026 or 2027) |
| Remote | Onsite — Hawthorne, CA (SpaceX HQ) |
| Comp | $125,000–$145,000 base (Level I); LTI + ESPP + benefits |
| TL;DR | SpaceX general SWE new grad role (not Starlink — different posting from #077). Harry's C++/distributed systems profile is a strong technical match. Two hard blockers: (1) ITAR legally excludes F-1 visa holders — no waiver path; (2) comp floor at $125K is below Harry's $140K minimum. Apply only if Harry has a path to US citizenship/LPR status or is willing to accept below-minimum comp. |

---

## B) Match with CV

| JD Requirement | CV Evidence | Strength |
|----------------|------------|----------|
| CS/Software/EE degree, graduating 2026–2027 | Georgia State BS CS, Expected May 2027 | ✅ Direct |
| C++, Rust, or systems programming | Chrome: C++ IPC transport layer, Protocol Buffers; Skills: C++, Rust listed | ✅ Direct |
| Real-time embedded or distributed computing | TiMoto: gRPC inter-service layer, deadlock fix, multi-AZ ECS; Pulumi: Raft/Paxos study | ✅ Strong |
| Design, test, integrate software through full lifecycle | Chrome: design docs, 95% test coverage, shipped to Chrome stable; TiMoto: 0→1 production deployment | ✅ |
| Cross-disciplinary collaboration + system-level thinking | Chrome: worked with Chrome infra team; TiMoto: primary engineer across backend/infra/ML | ✅ |
| First-principles problem solving | Chrome lock-free trie (traced mutex contention → redesign); TiMoto gRPC deadlock (traced shared resource conflicts) | ✅ |
| GPA ≥ 3.5/4.0 | 3.75/4.0 ✅ | ✅ |
| "Scrappy, entrepreneurial" engineering | TiMoto: primary engineer on 3-person team, $40–60/month infra spend with 99.9% uptime | ✅ |
| Dynamic environment + high responsibility | TiMoto: owns backend + infra + ML serving; on-call rotation; incident RCA | ✅ |
| **ITAR: US citizen, LPR, Refugee, or Asylee** | **Harry is F-1 — none of the four ITAR-eligible categories** | ❌ Hard blocker |
| Onsite Hawthorne, CA | Harry is Atlanta-based; open to relocation | ⚠️ Relocation |
| Comp $125K–$145K (Level I) | Harry's minimum is $140K; low end ($125K) is below minimum | ⚠️ Comp floor |

**Gaps:**

1. **ITAR — hard legal exclusion (not a sponsorship issue).** ITAR (International Traffic in Arms Regulations) requires the applicant to be (i) US citizen, (ii) lawful permanent resident, (iii) refugee under 8 U.S.C. § 1157, or (iv) asylee under 8 U.S.C. § 1158. F-1 student visa does NOT qualify for any of these categories. This is a federal export control requirement, not a company sponsorship policy — SpaceX cannot waive it. The form has a mandatory "Citizenship Status" field. Harry answering "F-1 student" will not satisfy this requirement.
2. **Comp at low end below $140K minimum.** $125K–$145K range; high end ($145K) is above the $140K floor but below the $150K target. Hawthorne, CA cost of living is high.
3. **No WASM/firmware/RTOS experience** — JD mentions autonomous systems and flight hardware; Harry's experience is web/cloud stack, not real-time embedded. Adjacent but not direct.

---

## C) Level and Strategy

**Level detected:** New Graduate (Level I SWE). Exact match for Harry's stage (May 2027).

**Technical match is genuine.** Harry's C++ IPC at Chrome scale, lock-free concurrent trie, and distributed systems at TiMoto are exactly what SpaceX wants in systems programming depth. GPA 3.75 clears the 3.5 minimum. Presidential Scholarship and merit-based awards satisfy the "competitive environment" preferred signal.

**ITAR strategy — there is no workaround for F-1.** Unlike H-1B sponsorship (where you apply and ask), ITAR is a federal law. F-1 students are not on the eligible list. Possible paths: (a) Harry is currently in a green card / LPR process (unlikely as a current F-1 student), or (b) Harry is misclassifying — F-1 is not any of the four categories. If Harry has any other status (e.g., pending LPR), this changes. Otherwise, this is a disqualifying screen that will appear at the form-fill step.

**If applying anyway:** On the form's Citizenship Status field, Harry would need to answer honestly. F-1 will disqualify. The form also has an "If (f) Other" field — Harry could explain the situation, but this is unlikely to result in an exception for an ITAR role.

---

## D) Comp and Demand

| Metric | Data |
|--------|------|
| SpaceX stated base | $125,000–$145,000 (Level I) |
| SpaceX new grad TC (Levels.fyi est.) | ~$170K–$210K with LTI/ESPP (SpaceX stock is private; ESPP allows purchasing stock at discount) |
| Harry target | $150K–$200K base |
| Harry minimum | $140K |

Base range straddles Harry's minimum: $125K (below) to $145K (above but below $150K target). SpaceX does not disclose current stock price or LTI value — it's pre-IPO private. ESPP provides some upside but unquantifiable. Comp is below market for a top-tier new grad at this tech level; SpaceX historically compensates below FAANG/top-tier on base in exchange for mission/prestige.

---

## E) Customization Plan

Not generated — score below 3.0 threshold and ITAR blocker renders application preparation low-priority.

If Harry has a path to ITAR eligibility and wishes to apply:

| # | Section | Current | Proposed Change | Why |
|---|---------|---------|-----------------|-----|
| 1 | Chrome bullet order | C++ IPC leads | Keep C++ IPC leading — it is the strongest signal for SpaceX systems work | Direct C++ systems match |
| 2 | TiMoto bullet order | gRPC/deadlock | Lead with gRPC deadlock trace — shows autonomous/real-time systems debugging mindset | SpaceX values root-cause rigor in flight software |
| 3 | Skills: Languages | C++ listed | Move C++ to first in Languages row | SpaceX JD explicitly names C++/Rust first |
| 4 | Skills row order | Distributed Systems leads | Keep — SpaceX is distributed computing + autonomous systems | Direct alignment |
| 5 | Add "Rust" highlight | Rust in languages | Move Rust near C++ in languages row | SpaceX JD: "C++, Rust, or other systems programming" |

---

## F) Interview Plan

| # | JD Requirement | STAR+R Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Systems programming + correctness | Chrome C++ IPC | Chrome needed IPC transport across browser process boundaries | Ship to 3B users with zero breaking schema changes | C++ Protocol Buffers; design doc; schema evolution rationale | Chrome stable, sub-50ms p99, 10K+ req/sec | Schema choices in distributed systems are permanent API contracts — test for evolution, not just today's shape |
| 2 | Concurrent + lock-free | Chrome lock-free trie | 1,200ms p99 settings navigation; mutex contention in production | 96% latency reduction without correctness regression | Identified contention; designed lock-free concurrent trie; linearizability proof by construction | Zero regressions, 96% cut | Concurrent code needs a correctness argument, not just tests — test sampling doesn't cover interleavings |
| 3 | Distributed systems production | TiMoto gRPC deadlock | Production deadlock under concurrent gRPC calls | 100% evaluation success at sub-50ms p99 | Traced shared resource acquisition conflicts; redesigned call sequencing | Resolved, no recurrence | Deadlocks surface resource ordering violations — map all acquisition paths before fixing |
| 4 | Dynamic environment + ownership | TiMoto 0→1 | Primary engineer on 3-person startup; build AI product end-to-end | Ship distributed production system with no senior safety net | gRPC + vLLM + ECS Fargate as cohesive system; on-call rotation; incident RCA | 99.9% uptime, 44% cost reduction | Full ownership means you cannot punt on the hard parts — you either fix it or it stays broken |
| 5 | Highly competitive / rigorous academic | GPA + Chrome | Competed for and got Google Chrome internship from a non-target school | Ship to 3B Chrome users as intern | C++ IPC + lock-free trie + TypeScript/React; senior code review | Adopted into Chromium production branch | Non-target school signals nothing about output — the code either ships to stable or it doesn't |

**Red-flag questions:**
- *"ITAR — are you eligible?"* → Harry cannot truthfully claim eligibility as F-1. If applying, be direct: "I'm on F-1. I understand ITAR requires one of four citizenship categories. I want to be transparent rather than get to a form and misrepresent my status."
- *"Comp — $125K is well below your market?"* → "SpaceX's mission justifies a temporary comp trade-off. I'd want to be at the high end of the range given my production experience at Google and TiMoto, and I'd target advancement fast."
- *"Georgia State — not a target school"* → "I know. Google hired me at Chrome, and I shipped C++ to 3 billion users. TiMoto hired me as primary engineer on production distributed systems. Judge by what I shipped."

---

## G) Posting Legitimacy

**Assessment: High Confidence**

| Signal | Finding | Weight |
|--------|---------|--------|
| Apply button | Active on Greenhouse | Positive |
| Comp disclosed | $125K–$145K explicitly stated | Positive |
| Company status | SpaceX — active launch operations, real company, Hawthorne HQ | Positive |
| JD specificity | Named technologies (C++, Rust), specific requirements (GPA ≥ 3.5, ITAR, clearance), specific comp range | Positive |
| Graduation year | 2026 or 2027 — Harry's May 2027 is in scope | Positive |
| ITAR field | Form has mandatory Citizenship Status field consistent with ITAR compliance | Positive (confirms legitimacy of ITAR requirement) |
| Location | Hawthorne, CA — SpaceX HQ address, consistent with known operations | Positive |
| Prior SpaceX entries | #077 Starlink (different jr_id, different team) — not a duplicate | Neutral |

---

## Keywords extracted

C++, Rust, systems programming, embedded systems, distributed computing, autonomous software, real-time systems, flight software, simulations, design documents, test coverage, integration, ITAR, Hawthorne, new graduate, software engineer, first principles, cross-disciplinary, onsite, SpaceX

---

## Machine Summary

```yaml
company: SpaceX
role: New Graduate Engineer, Software
date: 2026-06-07
url: https://job-boards.greenhouse.io/spacex/jobs/8493079002
score: 2.5
archetype: Systems Software Engineer
location: Hawthorne, CA (onsite)
comp_range: "$125,000–$145,000 base (Level I); LTI + ESPP (private stock)"
visa_risk: "F-1 — ITAR hard exclusion (F-1 is not US citizen, LPR, refugee, or asylee); no waiver path"
legitimacy: High Confidence
recommendation: "SKIP — ITAR legally excludes F-1 students (not a sponsorship issue); comp $125K–$145K straddles $140K minimum; apply only if Harry has path to ITAR-eligible status"
```
