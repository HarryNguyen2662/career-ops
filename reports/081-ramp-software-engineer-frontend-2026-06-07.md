# Evaluation: Ramp — Software Engineer, Frontend

**Date:** 2026-06-07
**URL:** https://jobs.ashbyhq.com/ramp/4e64ab86-4e30-403b-b1b9-41dc052570ce
**Archetype:** Full-Stack (Frontend-Heavy)
**Score:** 2.8/5
**Legitimacy:** High Confidence
**PDF:** ❌

---

## Block A — Role Summary

| Field | Detail |
|---|---|
| **Archetype** | Full-Stack / Frontend-Heavy |
| **Domain** | Fintech / Expense Management |
| **Function** | Frontend Engineering |
| **Seniority** | Mid-level (2+ years preferred) |
| **Remote** | Hybrid (NY HQ, Miami, SF, Remote US/Canada) |
| **Comp** | $143.2K–$284K + Equity |
| **TL;DR** | Build performant, beautiful React/TypeScript UIs for Ramp's expense management platform serving 70,000+ companies and $200B+ annualized spend |

---

## Block B — Match with CV

| JD Requirement | CV Evidence | Strength |
|---|---|---|
| Proficiency in JavaScript / TypeScript | Chrome TypeScript/React work (25K+ lines of Chromium); TiMoto backend TS usage | ✅ |
| React proficiency | Chrome: observer pattern in TypeScript/React; 68% delivery acceleration | ✅ |
| 2+ years frontend experience | Harry has ~1 year total professional exp; Chrome internship was primarily C++/TypeScript (not pure frontend); TiMoto is backend/infra/ML | ⚠️ |
| Web performance focus | Chrome IPC sub-50ms p99, 10K+ req/sec — but that's transport layer, not UI perf | ⚠️ |
| Shipping high-quality products at scale | Chrome shipped to 3B+ users; TiMoto 99.9% uptime | ✅ |
| Design system / Vite / Ryu in-house system | No explicit design system experience mentioned | ❌ |
| "Knack for getting visuals right" / UX focus | No portfolio of UI work; no CSS/design evidence | ❌ |
| 2+ years frontend preferred | <1 year; primarily backend/systems/ML profile | ❌ |
| Mentoring / interviewing | No evidence | ❌ |

**Gaps:**
- Harry is fundamentally a backend/distributed systems/ML infra engineer — frontend is a secondary skill
- No CSS, design system, Figma, or UI/UX portfolio evidence
- Chrome React work is UI-adjacent but inside a massive C++ codebase; not standalone frontend product work
- Role requires deep React/TypeScript frontend ownership; Harry's TypeScript is backend-leaning
- No Vite, Ryu, or design-system experience

---

## Block C — Level and Strategy

**Detected Level:** Mid-level (2+ YOE preferred) — Harry is below this threshold with <1 year total professional experience.

**Pitch Script 1 (Lead with Chrome scale):**
> "At Google Chrome, I shipped TypeScript/React changes into 25K+ lines of the Chromium codebase serving 3B+ active users — including an observer pattern refactor that accelerated feature delivery by 68%. I understand that frontend code at scale requires thoughtful state management and rigorous testing (95% coverage). At Ramp, I'd bring that same attention to correctness and performance to your fintech UI."

**Pitch Script 2 (Performance angle):**
> "I'm drawn to Ramp's emphasis on web performance — my Chrome internship centered on sub-50ms p99 latency targets. While my TypeScript work there was inside a browser engine context, the discipline of profiling, optimizing, and shipping zero-regression code maps directly to Ramp's high-stakes fintech UX requirements."

**Pitch Script 3 (Builder mentality):**
> "Ramp's 'everyone is a builder' ethos resonates with me — at TiMoto I own backend, infra, and ML end-to-end as the primary engineer on a 3-person team. I'm looking to grow into frontend ownership at a company where the product directly shapes how businesses manage money."

---

## Block D — Comp and Demand

| Field | Value |
|---|---|
| **Stated Range** | $143.2K–$284K + Equity |
| **Harry's Target** | $150K–$200K |
| **Harry's Minimum** | $140K |
| **Range vs. Target** | Floor ($143.2K) is just above Harry's minimum; very achievable even at entry of band |
| **Market (SF/NY SWE Frontend, 0-2yr)** | $140K–$180K base typical for new grad / junior at top fintech |
| **Assessment** | Comp range is wide — likely $143K–$160K for entry-level hire. Aligns with Harry's targets. |

---

## Block E — Customization Plan

**Archetype: Full-Stack (Frontend-Heavy)**

| Section | Reorder / Emphasis |
|---|---|
| **TiMoto** | Lead with TypeScript/React observer pattern work; mention 68% delivery acceleration; deprioritize gRPC/vLLM bullets |
| **Chrome** | Bullet 3 (TypeScript/React) leads; Bullet 1 (C++ IPC) moves to 3rd or 4th |
| **Develop for Good** | Keep as-is; PostgreSQL N+1 fix shows full-stack thinking |
| **Skills — Languages** | TypeScript, JavaScript first; then Python, Go, C++, etc. |
| **Skills — Frameworks** | React, Node.js, FastAPI, Django first; gRPC/Protobuf row deprioritized |
| **Skills — ML & AI Infra** | Move to last (before AI Dev Tools) or omit |

---

## Block F — Interview Plan

| # | Question | Situation | Task | Action | Result | Reflection |
|---|---|---|---|---|---|---|
| 1 | Tell me about a time you shipped UI code at scale | Chrome React/TypeScript observer pattern | Decouple UI state from rendering logic | Implemented observer pattern across 25K+ lines, 95% test coverage | 68% feature delivery acceleration | Learned that clean abstractions pay compounding dividends in large codebases |
| 2 | How do you approach web performance? | Chrome sub-50ms p99 requirement | Achieve low-latency transport for IPC in browser | Profiled bottlenecks, implemented lock-free trie for search | 96% latency reduction | Performance requires measurement-first discipline, not intuition |
| 3 | Describe handling a production reliability issue | TiMoto production deadlock | Restore 100% uptime under real traffic | Traced shared resource acquisition conflicts via gRPC logs | Resolved deadlock, maintained sub-50ms p99 | Systems-level debugging skills transfer to frontend async bugs |
| 4 | How do you collaborate cross-functionally? | TiMoto 3-person team, Chrome design doc reviews | Drive technical decisions with PM + design input | Wrote design docs reviewed by senior Chrome engineers; adopted into prod branch | Feature shipped to stable Chrome | Documentation and async communication are force multipliers |
| 5 | How do you grow junior engineers? | No direct report experience | (Hypothetical) | Approach: structured code reviews, pair programming, creating clear RFC templates | Demonstrated through mentoring design | Would reference Chrome team review culture as model |

**Recommended Case Study:** The Chrome TypeScript/React observer pattern refactor — quantified impact (68% delivery accel, 25K+ lines, 95% test coverage, 3B+ user reach) is the strongest frontend proof point.

**Red-Flag Q&As:**

1. **"Your background is mostly backend/ML — why frontend?"**
   > "My Chrome internship gave me direct frontend product experience inside the world's most demanding codebase. The React/TypeScript work I shipped reaches 3B users. I'm not switching away from systems thinking — I'm bringing it to the frontend, which is exactly what performance-focused fintech UI needs."

2. **"You only have ~1 year of experience. How do you meet the 2-year bar?"**
   > "My internship at Google and current role at TiMoto compressed what many engineers do in 3-4 years into 18 months — I shipped to 3B users at Google and own the full backend+infra+ML stack at TiMoto. The 2-year bar measures readiness, not calendar time."

3. **"Do you need visa sponsorship?"**
   > "I'm on F-1 OPT eligible May 2027, which gives me 3 years of work authorization for STEM fields. H-1B sponsorship would be needed by 2030. Ramp has a strong H-1B sponsorship history as a Series D company — I'm happy to discuss details."

---

## Block G — Posting Legitimacy

**Verdict: High Confidence**

| Signal | Status |
|---|---|
| Ashby-hosted posting | ✅ Legitimate ATS |
| "Apply for this Job" button present and active | ✅ Confirmed via Playwright snapshot |
| Full JD with responsibilities, requirements, benefits | ✅ Complete |
| Comp range disclosed | ✅ $143.2K–$284K |
| Official Ramp branding + ramp.com cross-links | ✅ |
| No suspicious patterns (payment requests, vague contact) | ✅ Clean |
| Anti-scam notice from Ramp itself | ✅ "Only @ramp.com emails" warning included |

Posting is live and legitimate. No red flags.

---

## Score Rationale

| Dimension | Score | Notes |
|---|---|---|
| Role-CV Archetype Fit | 2.0/5 | Harry is backend/ML/infra; this is a frontend role |
| Experience Level Match | 3.0/5 | <1 yr vs 2+ yr preferred; but Google pedigree helps |
| Technical Stack Overlap | 3.5/5 | TypeScript/React present but secondary in Harry's profile |
| Comp Alignment | 4.5/5 | $143K floor meets Harry's minimum |
| Company Quality | 5.0/5 | Ramp is Series D ($8.1B), strong eng culture |
| Visa Risk | 3.0/5 | Ramp sponsors H-1B but uncertainty remains |
| **Overall** | **2.8/5** | Below threshold — archetype mismatch is the core issue |

**Recommendation:** Apply per policy (no blockers), but note archetype mismatch. Harry's strength is backend/distributed systems/ML infra — this frontend role does not showcase his best work. If Ramp has backend openings, those would be a much stronger fit.

---

## Machine Summary

```yaml
company: Ramp
role: Software Engineer, Frontend
date: 2026-06-07
url: https://jobs.ashbyhq.com/ramp/4e64ab86-4e30-403b-b1b9-41dc052570ce
score: 2.8
archetype: Full-Stack (Frontend-Heavy)
location: "New York, NY / Miami, FL / SF / Remote US+Canada — Hybrid"
comp_range: "$143.2K–$284K + Equity"
visa_risk: "F-1 OPT eligible May 2027; H-1B needed ~2030; Ramp has strong sponsorship history"
legitimacy: High Confidence
recommendation: "Apply per policy but flag archetype mismatch; Harry's backend/ML profile is not optimally positioned for this frontend role"
```
