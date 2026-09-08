# Evaluation: Intuit — Software Engineer 1

**Date:** 2026-06-04
**URL:** https://jobs.intuit.com/job/-/-/27595/87369448720
**Archetype:** Full-Stack Engineer (adjacent) / Backend / Distributed Systems Engineer (primary pitch)
**Score:** 3.4/5
**Legitimacy:** Proceed with Caution
**PDF:** output/051-intuit-software-engineer-1-2026-06-04.tex

---

## A) Role Summary

| Field | Detail |
|-------|--------|
| **Archetype** | Full-Stack / Backend Engineer (new grad catch-all) |
| **Domain** | Fintech SaaS — TurboTax, QuickBooks, Credit Karma, Mailchimp |
| **Function** | Build (across Frontend / Backend / Fullstack / Mobile tracks) |
| **Seniority** | New grad / SWE1 — "less than two years of industry experience" |
| **Remote** | Onsite/hybrid — Mountain View CA, Atlanta GA, New York NY, San Diego CA |
| **Team size** | Not specified; team assigned post-offer based on skills + interests |
| **TL;DR** | General new-grad SWE pool posting at Intuit; team placement happens after hire; Harry's Atlanta location is a listed office. |

---

## B) Match with CV

### Requirements map

| JD Requirement | Harry's CV Match | Strength |
|---|---|---|
| Backend: Python / Node.js / Java server-side | Django (FastAPI), Node.js in skills; Python throughout | Strong |
| Backend: PostgreSQL / MySQL / MongoDB | PostgreSQL (N+1 fix → sub-100ms, Develop for Good; TiMoto gRPC + PostgreSQL layer) | Strong |
| Backend: RESTful API design | "REST APIs" in skills; BaaS at Develop for Good with stateless JWT API | Strong |
| Fullstack: Git, CI/CD | GitHub Actions CI/CD, 90% deploy time reduction (Develop for Good) | Strong |
| Fullstack: Agile/Scrum | Implied via team environments at Google + Develop for Good | Adequate |
| Frontend: React / JavaScript | TypeScript/React event-driven system in Chromium (Google Chrome bullet); React in skills | Strong |
| Frontend: HTML/CSS/JavaScript | JavaScript/TypeScript in skills; Chrome UI work | Adequate |
| Qualifications: CS degree | Georgia State BS CS, GPA 3.75, May 2027 | Strong |
| Qualifications: OOP + Agile fundamentals | Distributed Systems + OS coursework; production system design | Strong |
| Qualifications: AI awareness / Generative AI | vLLM, LLM-as-a-judge, LoRA/QLoRA in skills; TiMoto ML serving stack | Exceptional |
| Mobile: Android/iOS / React Native / Flutter | Not on CV | Gap |
| Grad timeline | Expected May 2027 — within "new college grad" category | Meets bar |
| Visa / sponsorship | F-1 — no sponsorship stated in JD | Risk flag |

### Gaps

| Gap | Blocker? | Mitigation |
|-----|----------|------------|
| Mobile engineering (Android/iOS/React Native/Flutter) | No — mobile is one of four optional tracks; Harry applies to Backend or Fullstack track | State track preference clearly in application |
| No explicit Agile/Scrum certifications | No — common for new grads | Mention Chromium code-review cadence and sprint-style delivery at Google |
| Sponsorship (F-1, JD silent) | Risk, not blocker | Ask recruiter early; Intuit is a large employer with PERM history; apply policy says always apply |

**Red flag — MAJOR:** Intuit announced ~3,200 layoffs (17% of workforce) in May 2026 — simultaneous with this posting being live. CEO framed it as operational restructuring, not AI replacement. The new-grad posting remains active but context is concerning (see Block G). Warn but apply per policy.

---

## C) Level and Strategy

### Level detected vs. Harry's level

| Dimension | JD | Harry |
|---|---|---|
| Seniority | SWE1 / New Grad (<2 yr exp) | New grad 2027 — exact fit |
| Track flexibility | Backend, Frontend, Fullstack, or Mobile | Backend + Fullstack strongest |
| Team assignment | Post-offer, based on skills/interests | Advantage: can express preference for backend/platform |

### Sell senior without lying

For this SWE1 role, Harry is in fact **over-qualified by experience** for the typical applicant pool:

1. **Production systems at scale** — "shipped to Chrome stable (3B+ users)" is a statement most SWE1 candidates cannot make. Frame this as day-one production readiness.
2. **Lead anchor** — Primary engineer on 3-person team at TiMoto: "owned backend, cloud infra, and ML serving end-to-end." Most SWE1 peers have never designed and operated a production distributed system.
3. **AI literacy is explicit JD requirement** — "Awareness of AI concepts and a basic understanding of Generative AI" — Harry's vLLM + PagedAttention work is 5 levels above this bar. Use it as a differentiator without overplaying.
4. **Express team preference:** Ask to be placed on a backend/platform/AI-adjacent team. This is encouraged by the JD.

### If team placement feels like a mismatch

Accept if comp is fair — SWE1 at a large fintech is a legitimate 12-18 month ramp. Negotiate inclusion in a backend-heavy team at offer stage. Set 6-month promotion review criteria in writing.

---

## D) Comp and Demand

### JD stated pay (hourly — likely intern conversion or hourly new-grad band)

| Location | JD Pay Range |
|----------|-------------|
| Bay Area / Mountain View | $55.50–$75.00/hr |
| Southern California (San Diego) | $53.50–$72.00/hr |
| New York | $57.50–$78.00/hr |
| Atlanta, GA | $46.50–$62.50/hr |

**Note:** These appear to be hourly rates. At 2,080 hr/yr: Atlanta range = ~$96.7K–$130K/yr base. Bay Area = ~$115K–$156K/yr base.

### Market data (Levels.fyi, 2026)

| Source | Data Point |
|--------|-----------|
| [Levels.fyi — Intuit SWE1](https://www.levels.fyi/companies/intuit/salaries/software-engineer/levels/software-engineer-1) | Median TC = **$158,302** (all US) |
| [Levels.fyi — Intuit SWE1 US](https://www.levels.fyi/companies/intuit/salaries/software-engineer/levels/software-engineer-1/locations/united-states) | Median TC = **$156,172** |
| Atlanta band (JD stated) | ~$96.7K–$130K base annualized — **below Harry's $140K minimum** |
| Bay Area band (JD stated) | ~$115K–$156K base — approaches minimum at top of range |

### Assessment

The **Atlanta band** ($46.50–$62.50/hr, ~$96K–$130K annualized base) falls short of Harry's $140K walk-away. Total comp with bonus + RSUs could bridge the gap — Intuit is known to have equity grants at SWE1 — but this needs explicit confirmation before offer stage. **New York** band ($57.50–$78/hr, ~$120K–$162K) is closer to target. Bay Area base can reach $156K at the top.

**Verdict:** Comp is a risk if placed in Atlanta; negotiate for NY/Bay Area track or request equity breakdown upfront.

---

## E) Customization Plan

| # | Section | Current State | Proposed Change | Why |
|---|---------|--------------|-----------------|-----|
| 1 | Summary | Distributed systems / ML infra focus | Add one sentence bridging to full-stack product impact: "...and delivered full-stack features to billions of Chrome users." | JD is product-facing SaaS; soften infra-heavy framing |
| 2 | TiMoto bullets | All infra/ML focused | Lead with the gRPC + PostgreSQL + production reliability bullet; keep vLLM but move it second | Backend track is the strongest match; DB + API work leads |
| 3 | Develop for Good | Backend/AWS focus | Add "Node.js Express REST APIs" or "Django REST" framing if accurate | JD explicitly mentions Express, Django, Spring MVC |
| 4 | Google Chrome | IPC + C++ + React | Keep React/TypeScript bullet prominent — it directly maps to Frontend or Fullstack track | Intuit UI teams use React; Fullstack is a posted track |
| 5 | Skills section | ML/AI infra heavy | Move "Frameworks & Databases" row up — Node.js, React, Django, REST, PostgreSQL are exact JD keywords | ATS scan for standard web stack terms |

**LinkedIn:** Update headline to include "Full-Stack" or "Backend + AI" adjacent framing; add Intuit-specific keywords: Java, Spring, SaaS, fintech, Agile.

---

## F) Interview Plan

### STAR+R Stories

| # | JD Requirement | Story | S | T | A | R | Reflection |
|---|---|---|---|---|---|---|---|
| 1 | Backend: RESTful API, server-side scale | Develop for Good N+1 fix | Nonprofit BaaS with 500+ concurrent users hitting DB bottleneck | Diagnose and fix response time 3s+ on large datasets | Redesigned with PostgreSQL indexing + query restructuring | Sub-100ms for 10K+ records | Taught me to measure before optimizing — profiling first, index second |
| 2 | Backend: DB + server frameworks | TiMoto PostgreSQL + gRPC serving | ML serving system needing consistent low-latency inference | gRPC deadlock under concurrent calls | Traced shared resource acquisition; redesigned call sequencing | 100% evaluation success rate at sub-50ms p99 | Concurrency bugs hide in prod — reproduce locally with load testing first |
| 3 | Fullstack: CI/CD + Agile | Develop for Good AWS BaaS | Nonprofit needed repeatable, fast deploys | Deploy time was blocking iteration | JWT stateless arch + GitHub Actions CI/CD pipeline | 90% reduction in deploy time | Stateless design is a force multiplier — horizontal scale falls out of it |
| 4 | Frontend: React + collaboration with designers | Google Chrome TypeScript/React | Chromium settings had no clean state propagation model | Accelerate feature delivery across 25K+ lines of TypeScript | Observer pattern event-driven state system | 68% feature delivery acceleration, 95% test coverage | Decoupling state from UI components is the right default; we paid debt fast |
| 5 | AI awareness / Gen AI | TiMoto vLLM selection | Needed to serve LLMs in production under concurrent load | OOM failures and KV cache fragmentation at load | Evaluated vLLM with PagedAttention vs. naive HuggingFace serving | Zero OOM failures at production traffic | Memory fragmentation is not visible in benchmarks — load test with real traffic shapes |
| 6 | Cross-functional collaboration | Google Chrome IPC design | Cross-team C++ IPC transport needed for browser feature | Ship to stable channel serving 3B+ users | Chose Protobuf over custom serialization; wrote design doc reviewed by senior Chrome engineers | Shipped to stable, 10K+ req/sec, sub-50ms p99 | Document the tradeoff — reviewers care about the reasoning, not just the decision |

### Recommended case study to present
**TiMoto AI production ML serving stack** — walk through the architecture: gRPC layer → vLLM inference → PostgreSQL → AWS/Terraform. Show the deadlock fix as a debugging story. This demonstrates backend + infra + AI in one narrative, which is exactly what Intuit's "AI-aware" requirement asks for.

### Red-flag questions

| Question | How to answer |
|---|---|
| "You're graduating in 2027 — when can you start?" | "I'm available for co-op or internship immediately; full-time May 2027. For the right team, I'm also open to part-time during the semester." |
| "Do you need visa sponsorship?" | "I'm on F-1 OPT eligible May 2027, and I'll need H-1B sponsorship for long-term authorization. Can you confirm Intuit's sponsorship policy? I've seen Intuit sponsor H-1Bs historically and wanted to clarify early." |
| "Why Intuit given the recent layoffs?" | "I follow the restructuring news — the company is doubling down on AI-native products. That's exactly where I want to work: building backend systems and ML-adjacent features that serve 100M+ customers. The restructuring signal tells me the remaining team will be doing more meaningful work." |
| "Which track do you want — Frontend, Backend, Fullstack, or Mobile?" | "Backend, with fullstack capability. My production work at TiMoto and Google spans backend APIs, cloud infra, and UI layers — I'm most effective on teams where I own an API or service end-to-end." |

**Story bank:** These stories map to general new-grad interview patterns — append to `interview-prep/story-bank.md` if it exists.

---

## G) Posting Legitimacy

### Assessment: PROCEED WITH CAUTION

### Signals table

| Signal | Finding | Weight |
|---|---|---|
| Apply button | Active "Apply Now" button present, direct link to Avature ATS | Positive |
| Posting age | No date visible on page; job ID 14930 — posting appears current | Neutral |
| Description quality | Four distinct engineering tracks, specific frameworks named (React, Spring MVC, Django, PostgreSQL), realistic new-grad requirements | Positive |
| Salary transparency | Pay bands listed for all four locations — rare and positive for legitimacy | Positive |
| Reposting detection | No "Intuit" entries in scan-history.tsv — first time seen in pipeline | Neutral |
| Layoff context | **Major concern:** Intuit announced 17% workforce reduction (~3,200 employees) in May 2026 — just 2 weeks before this evaluation | Concerning |
| Post-layoff hiring signal | Multiple sources confirm layoffs were in progress; Intuit careers page still shows entry-level roles; simultaneous layoff + new-grad hire is common at large corps (different cost centers, campus recruiting cycle committed months prior) | Mixed |
| Role-company fit | New-grad SWE pool role at 100M-user fintech platform — completely plausible role to fill continuously | Positive |

### Context notes

The layoff is a significant flag. However, **large-company pattern is common:** campus recruiting cycles are committed 6-12 months ahead and are often protected from headcount freezes that affect mid-career roles. The Atlanta office is a listed location — less likely to be impacted by Bay Area/Reno hub closures. The posting has a real ATS link, listed pay, and specific tech stacks — not a ghost job pattern.

**Recommendation:** Apply, but verify with the recruiter that this role is actively filling and confirm the Atlanta office is accepting new grad applications. Ask: "Is this role still actively recruiting post the May restructuring?"

---

## H) Draft Application Answers

*(Score 3.4 — Block H applies only at 4.0+. Skipped.)*

---

## Keywords extracted

Java, Python, JavaScript, Node.js, React, AngularJS, Vue.js, HTML, CSS, RESTful API, PostgreSQL, MySQL, MongoDB, Django, Spring MVC, Express, TypeScript, React Native, Git, Jenkins, Agile, Scrum, CI/CD, cloud, SaaS, Generative AI, Fullstack, new college grad, Software Engineer 1

---

## Machine Summary

```yaml
role: Software Engineer 1
company: Intuit
date: 2026-06-04
score: 3.4
archetype: Full-Stack / Backend (new grad pool)
location: Mountain View CA | Atlanta GA | New York NY | San Diego CA
remote: false
visa_risk: true
comp_risk: true
legitimacy: Proceed with Caution
apply_recommendation: apply_with_caveats
top_risks:
  - 17% workforce layoff (May 2026) — hiring intent unclear for this cohort
  - Atlanta base pay band ($96K-$130K annualized) below $140K walk-away
  - F-1 sponsorship not confirmed
top_strengths:
  - Exact level match (new grad <2yr exp)
  - Atlanta is listed office (Harry is Atlanta-based)
  - Harry's AI + backend stack exceeds JD requirements significantly
  - Pay listed = legitimate posting signal
```


---

## Addendum 2026-10-18: re-posted requisition 102012325536

**URL:** https://jobs.intuit.com/job/-/-/27595/102012325536 (tracking params cid, p_sid, p_uid, ss, utm, fbclid ignored). Posted 2026-10-15 per the page's JobPosting data. Jobs: Mountain View, San Diego, New York, Charlotte, **Atlanta**.
**Why no new row:** same company and title as this row (#51, Applied); only the requisition id changed (87369448720 in June, 102012325536 now). Fresh CV built for this posting: `output/51-harry-nguyen-resume-2026-10-18.pdf`.

**What changed in the JD (compared with June):**
- Qualifications now say "completed a degree-seeking program in Computer Science or a related technical field within the last 12 months" and "less than 12 months of relevant professional work experience (not including internships)". You graduate May 2027, so the degree is not complete yet. Flag only; the earlier "new college grad" wording did not state a window.
- Adds "use AI tools responsibly to speed up your work" and "awareness of AI concepts, including Generative AI".
- Focus areas: Frontend (HTML, CSS, JavaScript, React, AngularJS, Vue.js), Backend (Java, Python or Node.js; MySQL, PostgreSQL or MongoDB; Express, Spring MVC or Django), Full stack (Agile/Scrum, Git, Jenkins or Travis), Mobile.
- Pay as printed: Mountain View $55.5 - $75, New York $57.5 - $78, San Diego $53.5 - $72 (unit not shown; the June report read these as hourly rates, about $115K to $156K a year for Mountain View). No Atlanta line is printed in the current text; the June text had Atlanta at $46.50 to $62.50 an hour (about $96.7K to $130K), under your $140K walk-away.

**Jobright:** not provided for this posting.

**Fresh CV (1 page):** Languages lead with Java, Python and JavaScript; AI Dev Tools adds AI-Assisted Development and Prompt Engineering; Agentic Systems adds Generative AI; Frameworks lead with Django, Node.js and React beside PostgreSQL and MongoDB; Practices adds Full-Stack Development, Code Review and Mentoring (all stated). TiMoto backend first, NextStep above Pulumi. Numbers match the master CV exactly. Not added (not stated): HTML, CSS, Vue.js, AngularJS, Spring MVC, MySQL, Express, Jenkins, Agile, Git as a skill.

**Score:** stays 3.4/5. **Legitimacy:** Proceed with Caution (real Intuit careers page, new req, pay printed; the 17% layoff noted in June still applies to hiring intent).

### Job Description 102012325536 (archived verbatim, Intuit careers JobPosting data)

This role is for engineers at the start of their careers who are eager to learn, grow, and make an immediate impact. It’s a general posting, so we’ll get to know your skills, interests, and career goals and align you with a team where you can do your best work. You’ll work on real problems alongside experienced engineers, designers, and cross-functional partners. You’ll get hands-on guidance, detailed feedback, and mentorship as you learn proven engineering practices and see your work launch. You’ll also build fluency with AI tools and learn to use them responsibly to work smarter. 
 We're cultivating a culture that prioritizes innovators, risk-takers, and imaginative thinkers. You’ll help create solutions that transform how millions of consumers and small businesses manage their finances in cloud, platform, mobile, and SaaS environments. Working in a culture that embraces experimentation and rapid prototyping, you’ll collaborate closely with customers and cross-functional teams, turning ideas into real impact while building the skills to launch a rewarding career. 
 Responsibilities 
 Across all tech stacks: 
 Build and ship features for our core products and the systems that power engineering operations, and see your work reach customers.
 Learn and apply proven practices for designing, building, testing, and supporting software.
 Use AI tools responsibly to speed up your work, and share what you learn with your team.
 Turn customer feedback into small, meaningful improvements, using methods like Design for Delight.
 Collaborate with peers, designers, and engineers, and use code reviews, mentorship, and feedback to grow.
 Focus areas: 
 Frontend: Build responsive, dynamic web applications with HTML, CSS, JavaScript, and frameworks such as React, AngularJS, or Vue.js. Partner with designers, UX specialists, and backend engineers.
 Backend: Build web services in Java, Python, or Node.js. Work with databases like MySQL, PostgreSQL, or MongoDB, and design and integrate RESTful APIs using frameworks such as Express, Spring MVC, or Django.
 Full stack: Work across frontend and backend, discuss application and API architecture, and contribute on Agile/Scrum teams using tools like Git, Jenkins, or Travis.
 Mobile: Build Android or iOS applications using tools such as React Native, Flutter, Xcode, Android Studio, Swift, Objective-C, or Java. Integrate them with cloud-based APIs.
 Qualifications 
 Completed a degree-seeking program in Computer Science or a related technical field within the last 12 months.
 Less than 12 months of relevant professional work experience (not including internships, co-ops, or work study).
 Foundational understanding of Agile development, object-oriented design, and programming principles.
 Coursework, internships, personal projects, or academic experience in one or more programming languages (e.g., Java, Python, JavaScript, C++).
 Basic knowledge of front-end web technologies (HTML, CSS, JavaScript) is a plus.
 Awareness of AI concepts, including Generative AI, plus curiosity about AI tools and a willingness to apply them in your daily work.
 Strong written, verbal, and collaboration skills.
 Willingness to learn and adapt to new priorities, tools, and technologies in a fast-paced environment.
 Intuit provides a competitive compensation package with a strong pay for performance rewards approach. This position will be eligible for a cash bonus, equity rewards and benefits, in accordance with our applicable plans and programs (see more about our compensation and benefits at Intuit®: Careers | Benefits ). Pay offered is based on factors such as job-related knowledge, skills, experience, and work location. To drive ongoing fair pay for employees, Intuit conducts regular comparisons across categories of ethnicity and gender.
 The expected base pay range for this position is: 
 Mountain View $55.5 - $75 
 New York $57.5- $78
 San Diego, CA $53.5- $72
