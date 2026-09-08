# Custom Instructions -- career-ops

<!-- ============================================================
     THIS FILE IS YOURS. It will NEVER be auto-updated.

     Put your own house rules, custom workflows, and automations
     here -- anything you want the agent to ALWAYS do (or never do).

     This is for PROCEDURAL rules ("HOW I want things done").
     For WHO you are (archetypes, narrative, comp, negotiation),
     use modes/_profile.md instead. Keeping the two separate keeps
     each one readable.

     The agent reads this file alongside the system instructions;
     your rules here take precedence over the defaults, as long as
     they don't break the Data Contract (your files are never
     touched, and we never auto-submit an application for you).

     Because this is a user-layer file, anything you write here
     survives `node update-system.mjs`. Put customizations HERE,
     not in CLAUDE.md / modes/_shared.md / other system files --
     those get overwritten on update.
     ============================================================ -->

## House Rules

<!-- Rules the agent should always follow. Examples:
     - Always write evaluation summaries in British English.
     - Never include a photo in my CV (US / ATS-first market).
     - Cap each batch run at 20 listings unless I say otherwise.
     - If a report scores below 6, skip the cover letter. -->

- **Generated CVs (via build-cv-latex.mjs) must always include BOTH Personal Projects — Pulumi and NextStep (ClearDesk) — never drop one to save space, and never trim Work Experience bullets to make room either.** `templates/cv-template.tex` was fixed on 2026-08-05 (missing negative `\vspace` after bullet lists and section rules — it was wasting ~30pt/page vs. `cv.md`'s own template) and now fits full, uncut content (both projects, all Experience bullets) on 1 page. If a future edit to the template or a JD with unusually long bullets ever makes it not fit, treat that as a template/formatting bug to fix (tighter spacing, not content cuts) — ask before cutting any content. Always verify the result is exactly 1 page (`pdfinfo | grep Pages`) and has 0 stray asterisks (`pdftotext -layout | grep -c '\*\*'`) before delivering.

- **Internship-track CV variant — "Expected Dec 2027" graduation date (added 2026-08-21):** Harry is willing to postpone his graduation from May 2027 to Dec 2027 if it means landing the right internship (e.g. Databricks' "2027 Start — Winter" intern cohort, which needs a candidate still enrolled deeper into 2027 than a May grad would be). `cv.md`'s canonical Education date stays **Expected May 2027** — do not change the master file. Instead, when tailoring a CV specifically for an **internship** posting (not a new-grad/full-time role) where the JD's stated timing needs a later-than-May-2027 student status, use **"Expected Dec 2027"** in that generated CV's Education section only, and note in the report/tracker that this variant uses the postponed-graduation date by Harry's own stated preference. Default (new-grad/full-time roles) stays May 2027 unless Harry says otherwise for that specific application.

- **CV tailoring may rewrite bullets — but every rewrite must clear an explicit anti-AI-signs gate before delivery (added 2026-09-09, revised same day per Harry's feedback — root-cause fix for a project-wide AI-writing-sign problem).** Audited `output/` on 2026-09-09: 343 of 350 generated `.tex` files (everything before this rule) had em-dash/en-dash-parallelism bullets — "X -- Y -- Z" clause chains — that read as an AI tell. Root cause: every tailoring pass rewrote `cv.md`'s bullets (adding elaboration, JD keywords, extra clauses) to emphasize JD-relevant framing, and nobody ever checked the *rewritten* text against the anti-AI-signs standard already in force for every other piece of generated prose (see `feedback_avoid_ai_writing_signs.md`). Rewriting itself is not the problem — an unreviewed rewrite is. Banning rewriting entirely (the first version of this rule) was an overcorrection: it removes real tailoring value (leading with a JD's own terms, adjusting emphasis) for no reason beyond "we forgot to check it."

  **The actual fix, mandatory for every CV generated from now on:**
  1. **Facts are locked; wording is not.** Every metric, technology name, company, timeframe, and claim in a bullet must match `cv.md` exactly — no new numbers, no new named technologies, no exaggerated scope, nothing `cv.md` doesn't already say. Within that constraint, the *sentence itself* may be rewritten to lead with JD-relevant terms, reorder clauses, or tighten/loosen phrasing. This is unchanged from the Source-of-Truth Boundary and was never the actual failure mode.
  2. **Every rewritten bullet (and every bullet copied verbatim, as a matter of course) must pass this checklist before the CV is delivered — not "try to," pass it, checked mechanically:**
     - No em-dash (`—`) or en-dash-as-clause-connector (`--` joining two independent clauses) anywhere inside a bullet's prose. Date-range fields ("Sep 2025 -- Present") are exempt — those aren't prose.
     - No negative parallelism: "not just X, but Y" / "not only... but" / "it's not X, it's Y" / "X rather than Y" used as a rhetorical device.
     - No AI-vocabulary words: delve, crucial, robust, testament, underscore (as a verb), leverage, foster/fostering, showcase, tapestry, pivotal, boasts (meaning "has"), meticulous, intricate/intricacies, garner, enhance, align with, key (as a vague adjective), landscape (as an abstract noun).
     - No formulaic rule-of-three padding, and no bullet ending in a bolted-on present-participle ("-ing") clause purely for "so-what" emphasis rather than because the sentence naturally needs it.
     - Vary sentence rhythm across the CV's bullets — not every bullet should follow the identical "[verb] [result with metric] by [method]" template back to back.
  3. **Run this mechanical check on every generated `.tex` before calling it done, require 0 hits on all four:**
     ```bash
     grep -c '—' path/to/file.tex
     grep -cE 'resumeItem\{[^}]*--[^}]*\}' path/to/file.tex
     grep -icE 'delve|crucial|\brobust\b|testament|underscore|leverage|foster(ing)?|showcas|tapestry|pivotal|\bboasts\b|meticulous|intricat|garner|\benhance\b|align with' path/to/file.tex
     grep -icE 'not (just|only) .* but|it.?s not .*, it.?s' path/to/file.tex
     ```
     Any non-zero result means the bullet needs a genuine rewrite (fix the actual sentence), not a find-and-replace patch over the flagged word.
  4. If a report's Customization Plan section describes reordering bullets, and a bullet's wording was also adjusted (not just reordered), say so explicitly in that section — keeps every generated CV auditable against `cv.md`.

- **Standard tailoring level, NOT aggressive (set 2026-10-03; Harry reverted a heavier rewrite the same day):** keep the sentences of `cv.md` and change phrasing lightly to mirror the JD's vocabulary, plus reorder bullets and Skills lines. Do not rewrite every bullet results-first. Leave the Pulumi and Develop for Good bullets as in `cv.md`. Target is the level of the 2026-10-02 builds (average similarity to the master bullets about 0.88; 7 or 8 of 19 bullets unchanged). Run a numeric check against `output/master-harry-nguyen-resume.tex` after every build (no figure added or lost). Skills lines only: for ML, inference, serving or HPC JDs, add PyTorch, NVIDIA Triton, Ray, GPU and performance profiling (Harry stated he has them); never write a bullet claiming a project with them, and never add tools he has not stated (Hugging Face, LangChain, Datadog, Kafka, Rails, Vue). Pulumi stays "Open Source Contributor"; no authorship claims. No Summary section unless Harry asks. If Harry asks for "aggressive" again, ask how far before rewriting everything.

- **ATS keyword coverage pass (added 2026-10-03, Harry's request; this is separate from rewriting sentences):** Harry wants every job-specific CV to cover the JD's keywords broadly so it is not filtered by ATS, while the sentences stay at the standard tailoring level. After each build, compare the JD text with the PDF text (`output/ats-coverage.py`: `run(jd_txt, pdf, master_tex_text, label)`). For every JD keyword missing from the CV: add it to the Skills lines (or one light wording change in a bullet) when `cv.md` supports it directly, when facts already on the CV support it (for example Algorithms from Raft/Paxos and the trie, Embeddings from pgvector, Security from RLS/KMS, Scalability from multi-AZ and the throughput numbers), or when Harry stated he has it (PyTorch, Triton, Ray, GPU, profiling). Do not add terms with no support (Vue, Kafka, Rails, Hugging Face, LangChain, Datadog, mentoring, code review); list them in the chat summary as real gaps. If Harry pastes a checker's missing-keyword list, add the supportable ones the same way and flag the weakest evidence. Report the coverage percentage before and after. Keep the CV at 1 page (drop MongoDB first if needed). Added 2026-10-04 after the Pinterest #672 rejection (CV had 53% coverage because it was a reorder-only build): (1) every SWE job-specific CV gets a `CS Fundamentals` Skills row whenever the JD names data structures, algorithms, software design, concurrency, distributed systems or testing (all supported by the trie, Raft/Paxos tests, design docs and the test fix); (2) put the JD's generic category words into Skills when they are true in plain terms (for example `Artificial Intelligence`, `Security`, `Reliability`, `Software Design (Design Docs)`); (3) mirror verb phrases the JD uses only where the fact already says so (`Worked cross-functionally`, `Owned ... end to end`); (4) never insert a phrase that adds a claim (`applying data structures principles to eliminate N+1 queries`, `improving release consistency` are the stuffing patterns a keyword tool produces); (5) report the coverage percentage and the real gaps in the chat summary. Target is **95% or higher** (Harry, 2026-10-04). Harry stated on 2026-10-04 that he has full-stack/frontend, code review, mentoring, on-call, customer-facing work, prompt engineering, Jest/Playwright, C#, LangChain, Hugging Face, Kafka, Spark and TensorFlow (see `modes/_profile.md`): add the ones the JD names to the Skills lines (use a `Practices` row for Code Review, Mentoring, On-Call, Automated Testing; `Full-Stack Development` next to React), never inside bullets, and never add one the JD does not name. Count the whole JD keyword list from `output/ats-coverage.py`; do not shrink the denominator to reach the number. Every supportable term goes on the CV; a term with no support stays out unless Harry states he has it (then it goes in Skills only, like PyTorch), and the chat summary lists each such gap and the exact percentage. If the target cannot be reached honestly, say so and name the missing terms.

- **Confirmed CV approach (Harry, 2026-10-03): the #692 PathAI build is the reference.** Standard tailoring level (light rewording, original sentences kept, about 0.88 similarity to the master) plus the ATS keyword coverage pass. Three things not to do, learned from a tool-generated PathAI resume Harry pasted for comparison: (1) never turn an achieved result into a target or goal ("bringing it under 50ms" must not become "targeting sub-50ms"), and keep "wrote the design doc" as is; (2) no keyword-stuffing phrases such as "using data structures and algorithms principles" inside a bullet, put such terms in Skills (a "CS Fundamentals" row) or use a natural wording; (3) keep the role (Founder, Open Source Contributor) in the project heading, never as a bullet. Do not tick skills Harry lacks (GitLab CI when he has GitHub Actions).

(none yet -- add more above)

## Custom Workflows

<!-- Multi-step routines you run often, given a short name. Examples:
     - "weekly review": scan my saved portals, evaluate the new roles,
       then give me a one-paragraph summary of the top 3.
     - "prep <company>": pull the JD, generate STAR stories from
       article-digest.md, and draft 5 likely interview questions. -->

- **Auto-draft the Work at a Startup outreach message with every WAS evaluation (added 2026-09-09).** Whenever the auto-pipeline evaluates a posting from `workatastartup.com` (URL contains that domain, or the pasted JD is clearly a Work at a Startup listing -- comp shown as a range with an equity percentage, a "Will sponsor"/"Any (new grads ok)"-style tag line, an "About {Company}" section), don't wait for Harry to ask separately -- generate the "Start a conversation with the team at {Company}" draft in the same turn as the report/CV, right after delivering the evaluation summary. No need to re-ask each time; this is now the default for every WAS posting.
  - Same rules as every other written deliverable: source only from `cv.md`/`config/profile.yml`/`modes/_profile.md`/`article-digest.md`, no em dash, run the 4-check anti-AI-signs gate plus a manual re-read for rule-of-three padding and negative-parallelism, never mention team size ("3-person team", "small team," etc.) since Harry also targets mid-size companies.
  - Draft-only, same as every outreach message this session -- never send it, just hand Harry the text.
  - Skip this for non-WAS postings (Ashby, Greenhouse, Lever, direct company career pages, etc.) unless Harry asks for outreach separately -- this rule is scoped to the WAS "Start a conversation" format specifically, since that's the platform's own outreach mechanism.

## Output Preferences

<!-- How you like results formatted. Examples:
     - Reports: lead with the score and the one-line verdict.
     - Show the per-step token breakdown after a batch run.
     - Save PDFs date-first: YYYY-MM-DD-company.pdf -->

- **Generated CV filenames (added 2026-08-30): `{report#}-harry-nguyen-resume.pdf` / `.tex` -- no company slug, no date.** Previously used `{report#}-{company-slug}-harry-nguyen-{date}.pdf`; Harry wants it shorter since the report number alone is enough to cross-reference which company/role it's for (via `reports/{report#}-*.md` and the tracker row). Applies to every future CV saved to `output/`. Existing files already in `output/` don't need to be renamed retroactively unless Harry asks.

- **No em dash (—), ever, in any output (added 2026-09-08).** This is a hard ban, not a "reduce overuse" guideline: zero em dashes in reports, CVs, tracker notes, form answers, cover letters, AND in plain chat replies to Harry -- not just career-ops-generated files. Use a comma, colon, period, or parentheses instead. Use `--` (double hyphen) only where LaTeX resume bullets need it, never a real em-dash character. Before sending any chat message or writing any file, check it doesn't contain a `—` character.

## Off-Limits

<!-- Things the agent must never do for you. Examples:
     - Never auto-fill or submit an application without showing me first.
     - Never edit a system file to customize my setup -- put it here. -->

(none yet -- add yours above)
