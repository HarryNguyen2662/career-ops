# 155 — Everpure (Pure Storage) — Software Engineer Grad

> **Renumbered 2026-07-08:** was report #012, renumbered to resolve a filename collision with report #012 (Jane Street).

**Date:** 2026-05-28
**Score:** 3.8/5
**URL:** https://job-boards.greenhouse.io/embed/job_app?for=purestorage&token=7258968&utm_source=jobright
**PDF:** ❌
**Legitimacy:** High Confidence

---

## Machine Summary

```yaml
company: Everpure (Pure Storage)
role: Software Engineer Grad
date: 2026-05-28
score: 3.8
status: Evaluated
location: Santa Clara, CA — fully onsite, 5 days/week (relocation required)
comp_base: "$119,000–$179,000 USD"
comp_equity: "Pure Storage (NASDAQ: PSTG) RSU — public, liquid + incentive pay eligible"
archetype: "Systems Software / C++ — Data Storage & Infrastructure"
graduation_timing_risk: none — no graduation date requirement stated
visa_risk: medium — large company (Pure Storage ~7,000 employees) typically sponsors; form asks explicitly via dropdown (not a blocker); must confirm H-1B support
apply_rec: "Conditional Apply — near-perfect C++ systems match; comp floor below minimum ($119K), negotiate to $145K+; relocation to Santa Clara required; verify sponsorship and comp band before investing effort"
```

---

## ⚠️ Branding Note: Everpure = Pure Storage

The posting uses "Everpure" branding throughout, but:
- Greenhouse board slug: `purestorage`
- Company logo links to `purestorage.com/company/careers`
- HR email: `TA-Ops@purestorage.com`
- The company is Pure Storage (NASDAQ: PSTG) — $2.5B+ revenue, 7,000+ employees, NYSE-listed public equity

"Everpure" appears to be Pure Storage's branding for their new grad engineering program. Evaluate as Pure Storage.

---

## Block A — Match with CV

**Score: 4.5/5**

| JD Requirement | Harry's Evidence |
|---|---|
| **Proficiency in C++** | Google Chrome: designed C++ IPC transport layer serving 3B+ users at sub-50ms p99, 10K+ req/sec; lock-free concurrent trie eliminating mutex contention; shipped to Chrome stable channel — **primary JD requirement, directly evidenced** |
| **Data structures and algorithms** | Lock-free concurrent trie (96% latency reduction); DynamoDB hot-partition redesign (partition key strategy under 9K+ req/sec); N+1 query diagnosis (sub-100ms PostgreSQL indexing) |
| **Concurrency** | Lock-free trie eliminating mutex contention; gRPC deadlock traced to circular resource acquisition; exactly-once semantics under network partitions (Redis distributed caching) |
| **Design principles / SDLC** | Design documents adopted into Chrome production branch by senior engineers; 95% test coverage standard; zero production regressions in Chrome stable channel |
| **Problem-solving at scale** | Chrome IPC (3B+ users); CoderPush DynamoDB (9K+ req/sec); TiMoto gRPC deadlock fix (100% evaluation success rate) |
| **System performance and scalability** | 96% latency reduction (settings nav profiling); 44% cost reduction (ECS Fargate Terraform IaC); 30% read throughput improvement (DynamoDB partition redesign) |
| **Collaboration / cross-functional** | Chrome: partnered with infrastructure team on design docs; Develop for Good: stakeholder-facing BaaS; CoderPush: cross-team payment API integration |

**Gap:** No named data storage experience (deduplication, reclamation, WAN replication). Pure Storage builds enterprise flash storage arrays — specialized domain. However, the JD explicitly asks for CS fundamentals + C++ proficiency, not storage domain knowledge. The problems (data efficiency, scalability, replication) are distributed systems problems Harry has demonstrated.

**Strength:** C++ at production scale to 3B users is the rarest and most direct match to Pure Storage's engineering culture. Most new grad candidates have classroom C++ at best.

---

## Block B — North Star Alignment

**Score: 4.0/5**

Pure Storage builds high-performance enterprise flash storage systems. The engineering work is systems software at the intersection of hardware, performance, distributed replication, and reliability — precisely the Systems Software archetype that is Harry's primary.

**Where it aligns:**
- **C++ systems engineering** — Everpure's core is C++ native systems code; Harry's Chrome IPC work is the strongest new grad C++ proof point available
- **Performance + scalability** — data storage at enterprise scale requires the same p99 latency and throughput discipline Harry has demonstrated across Chrome, CoderPush, and TiMoto
- **Distributed systems** — WAN replication, data reclamation, deduplication are distributed systems problems; Harry has gRPC, exactly-once semantics, Raft/Paxos literacy
- **"Low-level hardware to large-scale cloud systems"** — Harry spans this range: Chrome (C++ IPC, OS-level) to TiMoto (multi-AZ ECS Fargate)
- **Graduate program** — structured onboarding designed for new grads; Harry's 2027 graduation is well-positioned
- **Public company stability** — PSTG is NYSE-listed, profitable, established employer — lower career risk than a Series B startup

**Where it misses:**
- **Storage domain** — data deduplication, reclamation, flash storage firmware are specialized; Harry has no direct storage engineering background; ramp required
- **Fully onsite Santa Clara** — Harry is in Atlanta; 5 days/week onsite is a hard relocation requirement, not hybrid
- **No ML/AI infrastructure angle** — Pure Storage is not an AI company (though they sell AI-adjacent storage products); no opportunity to apply Harry's ML serving work

**Career trajectory:** Joining Pure Storage's systems software team builds directly toward Harry's target archetype. C++ distributed systems at enterprise scale is resume-building. The storage domain is specialized but transferable — engineers from Pure Storage are hired by Google, Meta, AWS at senior levels.

---

## Block C — Compensation

**Score: 3.0/5**

| Component | Value | vs Target |
|---|---|---|
| Base | $119,000–$179,000 | **Floor $119K is $21K below walk-away minimum** |
| Equity | Public PSTG RSU — liquid | New grad grant typically $50K–$100K over 4 years (~$12K–$25K/year) |
| Incentive pay | Eligible (unspecified) | Typically 5–10% = $6K–$14K/year |
| Benefits | purebenefits.com | Fortune Best Workplaces level; standard large-company package |

**The comp challenge:** Pure Storage/Everpure's "start of range" for grad roles skews toward $119K–$135K — both below Harry's $140K walk-away. The phrasing "salary ranges are determined based on role, level and location" and the wide band ($119K–$179K) signal significant latitude — but recruiters anchor grads at the low end.

**Negotiation target:** Enter $155K as salary expectation. The upper end of the band is $179K — $155K is a defensible mid-point backed by Harry's Chrome internship (production C++ at FAANG scale is above-average for new grad comp positioning). With PSTG public equity and incentive pay, total comp at $150K base = ~$175K–$185K TC.

**Santa Clara CoL:** $150K in Santa Clara is roughly equivalent to $115K in Atlanta after rent delta (~$1,500/month). This matters for the comp assessment — the band must be interpreted against SF Bay Area living costs.

---

## Block D — Cultural Signals

**Score: 3.2/5**

**Positive signals:**
- Pure Storage culture: Fortune Best Workplaces in Technology, Fortune Best Workplaces Bay Area, Great Place to Work certified — not just self-reported
- Graduate program: structured investment in new grad development
- "We celebrate those who think critically" — engineering-first culture signal
- PSTG public equity: liquid, tradeable, no lock-in; ~$11B market cap; stable
- Established employer (~7,000 employees, 15+ years old) — lower startup risk

**Friction signals:**
- **Fully onsite Santa Clara, 5 days/week** — the JD explicitly states "expected to work each work day during a normal business week"; this is not hybrid, not flexible; relocation from Atlanta required
- Bay Area cost of living: Santa Clara rents ($2,500–$3,500/month vs Atlanta $1,200–$1,800/month) offset the comp range significantly
- Storage domain: specialized niche; not AI/cloud-native; may limit future mobility vs roles at hyperscalers
- Enterprise company: slower iteration cycles vs startup pace; more process

---

## Block E — Red Flags

| Flag | Severity | Action |
|---|---|---|
| **Comp floor $119K** — 21K below walk-away; grad entry likely $119K–$135K range | HIGH | Anchor at $155K in the form. Argument: Google Chrome C++ internship (FAANG benchmark) + production systems at 3B user scale justifies top-quartile grad offer. If recruiter counters below $140K, invoke full TC argument (equity + incentive). Do not accept below $140K base. |
| **Fully onsite Santa Clara, 5 days/week** — relocation from Atlanta mandatory | MEDIUM | Harry's profile says open to relocation for strong roles. Santa Clara is a strong role for systems software. Budget $5K–$10K relocation cost; ask if Pure Storage offers relocation support. |
| **Sponsorship** — form asks "Will you now or in the future require sponsorship?" (dropdown, not free text) | MEDIUM | Answer: Yes. Pure Storage is a large, established company that routinely sponsors H-1B (7,000+ employees, global workforce). Verify with recruiter: "Does Pure Storage sponsor H-1B for new grad engineers?" Likely yes. |
| **"Everpure" vs Pure Storage branding** — Greenhouse is purestorage but company is "Everpure" | LOW | The branding is internal (TA-Ops@purestorage.com, logo links to purestorage.com). Apply as if it's Pure Storage. Confirm in recruiter call: "Is Everpure the grad program brand for Pure Storage?" |
| **Deemed export rule question** — "Does the deemed export rule affect your employment?" | LOW | Harry is Vietnamese, not from a US-sanctioned nation. Answer: **No**. This question screens for citizens of sanctioned nations (Syria, Cuba, Iran, North Korea, etc.) who don't hold a second non-sanctioned nationality. |
| **No graduation timing restriction** | POSITIVE | No barrier — Harry can apply with May 2027 grad date. |

---

## Block F — Global Score

**3.8/5**

| Dimension | Score | Driver |
|---|---|---|
| CV Match | 4.5 | C++ at Chrome scale is the rarest grad-level proof point; concurrency, CS fundamentals, SDLC all covered |
| North Star | 4.0 | Systems Software archetype exact match; C++ distributed systems at enterprise scale; storage domain is learnable |
| Compensation | 3.0 | Floor well below minimum; wide band allows negotiation; PSTG equity + incentive helps TC |
| Culture | 3.2 | Fully onsite Santa Clara (relocation required); Fortune Best Workplace; stable public company |
| Red flag adj. | -0.9 | Comp floor risk (-0.4) + onsite relocation (-0.3) + sponsorship unconfirmed (-0.2) |
| **Global** | **3.8** | |

**Recommendation: Conditional Apply.**

Score 3.8/5 — in the "apply only with specific reason" band. The specific reasons that justify applying:

1. **C++ match is near-perfect** — Chrome IPC transport layer in production C++ directly maps to what Pure Storage engineering does every day; this is Harry's single strongest archetype match of the session
2. **Systems Software career trajectory** — Pure Storage engineers move to Google, AWS, Meta storage/infra teams; this is the right credential-building role for the target archetype
3. **Public liquid equity** — PSTG is a real, tradeable stock; no illiquidity risk like Warp
4. **No graduation timing barrier** — Harry applies honestly

**Before submitting:** Two questions for the recruiter: (1) "Does Pure Storage/Everpure sponsor H-1B for new grad engineers?" and (2) "Is the comp range flexible above $140K for candidates with FAANG C++ internship experience?" If both are yes → score rises to 4.2 → strong apply.

**Form answers:**
- Previously worked for Everpure? → **No**
- Deemed export rule? → **No**
- Require sponsorship? → **Yes**
- Able to work onsite Santa Clara? → **Yes** (confirming willingness to relocate)

---

## Block G — Posting Legitimacy

**Tier: High Confidence**

| Signal | Finding | Weight |
|---|---|---|
| Posting live | Active Greenhouse form; Apply button present; full JD rendered | Positive |
| Salary transparency | $119,000–$179,000 explicitly stated | Positive |
| Company verification | purestorage.com logo link + TA-Ops@purestorage.com HR email confirm Pure Storage entity | Positive |
| Company health | Pure Storage (NASDAQ: PSTG): $2.5B+ revenue, 7,000+ employees, profitable, NYSE-listed | Positive |
| JD specificity | Named work areas (deduplication, reclamation, WAN replication), explicit onsite requirement | Positive |
| Graduate program | Structured grad-specific role with development language ("grow along with us") | Positive |
| ATS | Greenhouse board `purestorage` matches company domain | Positive |

Real posting at a public company. "Everpure" branding is unusual but all evidence points to Pure Storage. No ghost signals.

**PDF: Skipped** — Score 3.8/5, below 4.0 threshold. Pending sponsorship + comp confirmation.
