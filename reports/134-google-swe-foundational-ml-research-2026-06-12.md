# Evaluation: Google — Software Engineer, Foundational ML Research

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/95219437891658438-software-engineer-foundational-ml-research
**Archetype:** ML Research Engineering
**Score:** 2.4/5
**Legitimacy:** High Confidence
**PDF:** N/A (score < 3.0 — per policy, still apply)

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Title | Software Engineer, Foundational ML Research |
| Team | Foundational ML Research (Gemini post-training) |
| Seniority | Mid ("Mid" badge), likely L4-L5 Research SWE |
| Location | New York, NY, USA |
| Comp | $174K–$253K base + 15% bonus + equity → TC ~$240K–$350K+ |
| Domain | ML research: reinforcement learning, optimization, privacy, game theory; Gemini post-training |

**What the team does:** Foundational ML research in specialized areas (RL, optimization, privacy, game theory) contributing to Gemini post-training. Strong academic research pedigree expected — publication record at NeurIPS/ICML/ICLR is preferred.

---

## B — CV Match

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or related, or equivalent | Georgia State, BS CS, GPA 3.75 | ✅ |
| 5 years experience programming in Python | ~15 months Python total (TiMoto FastAPI/Django + DfG) | ❌ Major gap: ~3.5 yrs short |
| Experience training ML models | vLLM serving at TiMoto; no model training from scratch | ⚠️ Serving ≠ training |
| PhD in CS (preferred) | BS, Expected May 2027 | ❌ No PhD |
| 5 years data structures/algorithms (preferred) | Strong CS foundation, GPA 3.75, DS&A coursework | ⚠️ Implied, not 5 years |
| Publications (NeurIPS/ICML/COLT/ICLR) (preferred) | None on record | ❌ |
| JAX/PyTorch large-scale model training (preferred) | PyTorch (via vLLM); no JAX; no large-scale training | ⚠️ Partial |
| Post-training Gemini models (preferred) | LLM-as-a-judge (tangential, RLHF-adjacent) | ⚠️ Very indirect |

**Gap analysis:**
- **Experience gap: CRITICAL.** Minimum requires 5 years Python — Harry has ~1.25 years. This is a 3.75-year gap that cannot be mitigated.
- **Research pedigree gap:** PhD + publication record at top venues is preferred. Harry has no research publications.
- **ML training gap:** Harry does inference/serving (vLLM), not model training. Foundational ML research requires training at scale (JAX/PyTorch, multi-GPU/TPU).
- **This is a research-track role**, not a product SWE role. The interview will probe deep ML theory (RL, optimization, game theory).

---

## C — Level & Interview Strategy

**Target level:** L4-L5 Research SWE (exceptionally high bar for new grad)

**Interview format (Google Research SWE):**
1. Coding (LC hard, algorithm-heavy)
2. ML Theory: RL fundamentals, optimization theory, PAC learning, game theory
3. ML System Design: training pipeline, distributed training, post-training RLHF
4. Research discussion: paper reading, contribution framing
5. Behavioral

**Strategy:**
- This is a reach application. Apply per policy.
- Lead with vLLM inference as proxy for ML systems understanding
- LLM-as-a-judge → frame as RLHF-adjacent: "reward modeling for evaluation"
- Study RL fundamentals (policy gradient, PPO, RLHF) before interview
- Acknowledge honestly: "I'm a new grad focused on ML infra today, planning PhD or research roles in 2-3 years"
- Disclose: "F-1 OPT at graduation May 2027; H-1B long-term. Google sponsors H-1B."

---

## D — Comp & Market

| Component | Range |
|-----------|-------|
| Base (L4-L5 Research) | $174K–$253K |
| Bonus | 15% target |
| Equity | Alphabet RSUs |
| TC estimate | $240K–$350K+ |

Comp significantly exceeds Harry's $150K-$200K TC target. This is an aspirational role — if somehow hired, it would be a major win.

---

## E — CV Customization Plan

**For this role, standard CV is best** — no major reordering needed since the role is research-oriented and Harry's ML experience is thin. If submitting:

**Skills row ordering (ML Research):**
1. ML & AI Infrastructure (lead: PyTorch, vLLM — closest to research stack)
2. Languages (Python **bolded** — core requirement)
3. Distributed Systems
4. Cloud & Infrastructure
5. Frameworks & Databases
6. AI Dev Tools (last)

**Key framing:**
- TiMoto LLM-as-a-judge → frame as "reward modeling / evaluation pipeline" (RLHF-adjacent)
- Avoid overstating — Google research teams will probe deeply; stay honest
- Add to TiMoto bullets: any training experiments, fine-tuning, or LoRA work if applicable

---

## F — Interview Preparation

### Topics to study for a research SWE interview
- **RL fundamentals:** MDPs, policy gradient, PPO, DPO, RLHF pipeline
- **Optimization:** convex optimization, gradient descent variants, Adam/AdaGrad
- **Game theory:** Nash equilibrium, mechanism design basics
- **Post-training:** SFT → RLHF → DPO pipeline for LLMs
- **JAX basics:** functional transformations (jit, vmap, grad)
- **Distributed training:** data parallelism, model parallelism, pipeline parallelism

### STAR+R Story (best available)
**"LLM evaluation as reward signal"**
> Situation: TiMoto needed quality signal for LLM outputs. Task: design objective evaluation pipeline. Action: built LLM-as-a-judge with LangChain, defined scoring rubrics aligned with user satisfaction signals — conceptually parallel to reward modeling in RLHF. Result: 100% evaluation success rate at sub-50ms. Reflection: this made me want to go deeper into reward model design and post-training alignment.

---

## G — Posting Legitimacy

**Verdict: High Confidence**

- Apply button present and functional (verified via Playwright)
- Full JD with responsibilities, qualifications, and compensation
- Official Google Careers domain
- Comp explicitly stated: "US: $174000 - $253000 (USD) + 15% bonus target"
- Specific team context (Gemini post-training, foundational ML)

---

## Summary & Recommendation

**Score: 2.4/5 — Below threshold; apply per policy**

**Critical gaps:** 5-year Python requirement (Harry has ~1.25 years); PhD preferred (Harry is BS); publication record at NeurIPS/ICML/ICLR required (Harry has none); no ML training-from-scratch experience; no RL/optimization research background.

**Why apply anyway (per policy):** Google's hiring system may route to a better-fit team; it's a reach that costs nothing to apply; alumni status from Chrome internship gives slight boost.

**Honest assessment:** This role is designed for PhD-track researchers or engineers with 5+ years of production ML research. Harry is 3-4 years away from being competitive for this specific role type. Focus interviews at ML infrastructure roles (#133, #136) where the fit is far stronger.

**Visa note:** F-1 OPT → H-1B. Google sponsors H-1B. Disclose proactively.

---

## Machine Summary

```yaml
report_num: 134
company: Google
role: Software Engineer, Foundational ML Research
team: Foundational ML Research (Gemini post-training)
date: 2026-06-12
score: 2.4
archetype: ML Research Engineering
seniority: Mid (L4-L5 Research SWE)
location: New York, NY, USA
comp_base_range: "$174K-$253K"
comp_tc_est: "$240K-$350K+"
legitimacy: High Confidence
apply_button: true
visa_flag: F-1 OPT → H-1B (Google sponsors)
critical_gaps:
  - 5-year Python minimum (Harry has ~1.25 years)
  - No PhD (preferred)
  - No publication record (NeurIPS/ICML/ICLR)
  - No ML training-from-scratch experience
  - No RL/optimization research background
key_strengths:
  - LLM-as-a-judge (RLHF-adjacent framing)
  - Google Chrome alumni
  - PyTorch/vLLM production depth
recommendation: Apply (per policy; reach application)
pdf_generated: false
```
