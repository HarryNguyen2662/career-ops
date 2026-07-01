# Evaluation: Google — Machine Learning Software Engineer

**Date:** 2026-06-12
**URL:** https://www.google.com/about/careers/applications/jobs/results/99351668776149702-machine-learning-software-engineer
**Archetype:** ML/AI Infrastructure · AI Serving · Ads ML
**Score:** 3.6/5
**Legitimacy:** High Confidence
**PDF:** output/133-google-ml-swe-travel-ads-harry-nguyen-2026-06-12.pdf

---

## A — Role Summary

| Field | Detail |
|-------|--------|
| Title | Machine Learning Software Engineer |
| Team | Travel Ads — AI Overviews / AI Mode integration |
| Seniority | Mid (L4 equivalent, "Mid" badge shown) |
| Location | Mountain View, CA, USA |
| Comp | $147K–$211K base + 15% bonus + equity → TC ~$200K–$280K |
| Domain | Ads ML: ranking, retrieval, deep learning, LLM integration |

**What the team does:** Integrates travel ads into AI Overviews and AI Mode using deep learning (Adbrain/TensorFlow/JAX), ranking/retrieval models, and LLM inference — bridging generative AI with core ads infrastructure.

---

## B — CV Match

| Requirement | Harry's Evidence | Strength |
|-------------|-----------------|----------|
| BS CS or equivalent | Georgia State, BS CS, GPA 3.75, Exp May 2027 | ✅ |
| 2 yrs software dev (C++, Python) | ~15 months total: Google Chrome C++ (4 mo) + TiMoto Python (9 mo) + Develop for Good (4 mo) | ⚠️ Gap: ~9 months short |
| 2 yrs testing/maintaining/launching software | Chrome 95% test coverage, production deployment at TiMoto and DfG | ⚠️ Same gap |
| Build/train/deploy ML models (TensorFlow/JAX/Adbrain) | vLLM inference engine at TiMoto (PyTorch-based), LLM-as-a-judge pipeline; **no TensorFlow/JAX/Adbrain** | ⚠️ Framework mismatch |
| Experience with ranking/retrieval/recommendation models | No direct ranking/retrieval experience | ❌ Gap |
| GenAI / LLM integration (preferred) | LangChain, vLLM, LLM-as-a-judge evaluation pipeline at TiMoto | ✅ Strong |
| Large-scale ML system management (preferred) | vLLM at production traffic, TiMoto end-to-end ownership | ✅ Partial |
| A/B testing / statistics / experiment design (preferred) | No explicit A/B testing experience on record | ⚠️ |
| Cross-functional collaboration | Chrome: design docs + code reviews; TiMoto: cross-role ownership | ✅ |

**Gap analysis:**
- **Framework gap:** TensorFlow/JAX/Adbrain are the stack; Harry has PyTorch/vLLM. Transferable but distinct.
- **Ranking/retrieval gap:** Core minimum qual — no direct evidence.
- **Experience gap:** ~9 months short of 2-year threshold. Mitigated by production ownership + Google internship.
- **Education gap:** BS (not MS/PhD) for preferred, but minimum is satisfied.

---

## C — Level & Interview Strategy

**Target level:** L3 (new grad track) or L4 (stretch given ML background)

**Interview format (Google ML SWE):**
1. Coding (LC medium/hard): Python or C++
2. System Design: ML system design (recommendation system, ranking pipeline)
3. ML Design: model architecture, training pipelines, evaluation metrics
4. Behavioral (Googleyness)

**Strategy:**
- Lead with LLM inference ownership at TiMoto (vLLM, production)
- Emphasize Chrome scale (3B users) for production credibility
- For ML design: study ranking/retrieval fundamentals (two-tower models, BERT retrieval, ads CTR prediction)
- For system design: recommendation system at scale (feature store → model serving → A/B)
- Disclose: "F-1 OPT at graduation May 2027; H-1B long-term. Google sponsors H-1B."
- Acknowledge experience gap proactively: "I have ~15 months of production experience but it includes Google-caliber code review and end-to-end ML production ownership"

---

## D — Comp & Market

| Component | Range |
|-----------|-------|
| Base (L3) | $147K–$175K |
| Base (L4) | $175K–$211K |
| Bonus | 15% target |
| Equity | Alphabet RSUs (4-yr vest) |
| TC estimate | $200K–$280K+ |

Harry's $150K–$200K TC target is **met at L3**. Mountain View cost of living is high but Google total comp is competitive.

---

## E — CV Customization Plan

**Skills row ordering (ML/AI role):**
1. ML & AI Infrastructure (first — vLLM, PagedAttention, LangChain, LLM-as-a-judge)
2. Languages (Python **bolded**)
3. Distributed Systems
4. Cloud & Infrastructure
5. Frameworks & Databases
6. AI Dev Tools (last)

**Bullet emphasis:**
- TiMoto: Lead with vLLM/PagedAttention bullet; add "LLM-as-a-judge evaluation pipeline" explicitly
- Chrome: Mention "shipped to production serving 3B users" — production credibility
- Add/emphasize: any PyTorch training experience; note LangChain orchestration

**Skills to add/surface:**
- PyTorch (add to ML & AI Infrastructure)
- Note: no TensorFlow/JAX — do not claim; frame as "PyTorch/vLLM inference stack, familiar with TF ecosystem"

**Customization delta for this role:**
- Reorder skills: ML & AI Infrastructure → Languages → Distributed Systems → Cloud → Frameworks → AI Dev Tools
- TiMoto summary bullet: emphasize ML model serving and LLM-as-a-judge evaluation
- Projects: Pulumi is weak signal for this role; consider adding any ML project if available

---

## F — Interview Preparation

### STAR+R Stories

**"Why ML at Google Ads?"**
> Situation: At TiMoto, built LLM-as-a-judge evaluation pipeline to score model output quality. Task: needed objective quality signal at inference time. Action: designed judge pipeline with LangChain, defined scoring rubrics, integrated with vLLM serving layer. Result: 100% evaluation success rate at sub-50ms. Reflection: realized I wanted to scale this to larger recommendation/ranking problems — ads ML is exactly that intersection.

**"Production ML ownership"**
> Situation: TiMoto had no ML serving infrastructure. Task: architect inference engine from scratch. Action: selected vLLM/PagedAttention for KV cache efficiency under concurrent load; deployed with continuous batching. Result: zero OOM failures at production traffic. Reflection: learned that ML infra is really distributed systems applied to model serving.

**"Scale and reliability"**
> Situation: Google Chrome internship. Task: IPC transport layer for Chrome settings serving 3B users. Action: designed with Protocol Buffers for schema evolution; achieved sub-50ms p99 at 10K+ req/sec. Result: shipped to Chrome stable channel. Reflection: production at Google scale demands defensive design from the first commit.

**ML Design prep topics:**
- Two-tower models for retrieval (query embedding + doc embedding)
- Ads CTR prediction (logistic regression → GBDT → deep learning progression)
- Feature store design for online/offline consistency
- A/B testing for ads: click-through rate, conversion rate, holdback experiments
- TensorFlow/JAX basics: computation graphs, gradient tapes (self-study 1 week)

---

## G — Posting Legitimacy

**Verdict: High Confidence**

- Apply button present and functional (verified via Playwright snapshot)
- Full JD with responsibilities, qualifications, compensation range ($147K–$211K)
- Google Careers official domain
- Compensation explicitly stated: "US: $147000 - $211000 (USD) + 15% bonus target + bonus + equity"
- Team context provided (Travel Ads, AI Overviews integration)

---

## Summary & Recommendation

**Score: 3.6/5 — Decent match, apply**

**Strengths:** Strong LLM inference production depth (vLLM), Google internship alumni (same code review bar), LLM-as-a-judge evaluation signal, Python + C++ combination.

**Gaps:** No TensorFlow/JAX/Adbrain experience; no ranking/retrieval model history; ~9 months short of 2-year experience threshold; no A/B testing record.

**Recommendation:** Apply. The GenAI integration angle (LLMs into ads) aligns well with Harry's LLM serving background. Frame as "LLM inference engineer expanding into ads ranking." Mitigate framework gap by noting PyTorch→TensorFlow transferability. Mitigate experience gap with Chrome internship and production ownership at TiMoto.

**Visa note:** F-1 OPT → H-1B. Google sponsors H-1B. Disclose proactively.

---

## Machine Summary

```yaml
report_num: 133
company: Google
role: Machine Learning Software Engineer
team: Travel Ads
date: 2026-06-12
score: 3.6
archetype: ML/AI Infrastructure
seniority: Mid (L4 target, L3 floor)
location: Mountain View, CA, USA
comp_base_range: "$147K-$211K"
comp_tc_est: "$200K-$280K"
legitimacy: High Confidence
apply_button: true
visa_flag: F-1 OPT → H-1B (Google sponsors)
exp_gap: ~9 months short of 2-year minimum
framework_gap: PyTorch/vLLM vs TensorFlow/JAX/Adbrain
key_strengths:
  - vLLM production inference ownership
  - LLM-as-a-judge evaluation pipeline
  - Google Chrome alumni (same code review bar)
  - Production scale (3B users)
key_gaps:
  - No TensorFlow/JAX/Adbrain experience
  - No ranking/retrieval model history
  - No A/B testing record
recommendation: Apply
```
