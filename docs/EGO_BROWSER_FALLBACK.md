# ego-browser Fallback Cookbook

`ego-browser` (the "ego lite" Chromium runtime) is the standing **backup path** for JD extraction, apply-button verification, and liveness checks when the primary tools — Playwright/`Claude_Browser`, `browser-extract.mjs`, and `WebFetch` — can't do the job. It is not a replacement for those tools on ordinary ATS boards (Ashby, Greenhouse, Lever, Personio); it exists specifically for the cases those tools fail on.

## When To Reach For This

| Symptom | Why the primary path fails | Fix |
|---|---|---|
| `X is blocked by policy and cannot be opened in the Browser pane` | The Claude_Browser MCP has a domain blocklist (confirmed on `google.com`) | ego-browser opens the page instead — it is a separate runtime, not subject to that blocklist |
| `browser_snapshot` / `get_page_text` returns empty or near-empty text on a page that visibly has content | Client-side SPA that doesn't populate the accessibility tree the way `Claude_Browser`'s text extraction expects (seen on Lyft's Careerpuck-hosted JD, Snowflake's Workday-style search-results page) | ego-browser's `snapshotText()` + direct `js()` DOM queries read the live rendered DOM, not a cached a11y snapshot |
| `WebFetch` returns only nav/header boilerplate, or explicitly says the page needs a sign-in / is JS-rendered | `WebFetch` fetches static HTML and does not execute client-side JS | ego-browser actually renders the page in a browser before reading it |

If Playwright/`browser-extract.mjs` and `WebFetch` both work, use them — they're cheaper (no heredoc round-trip) and already wired into `scan.mjs`'s zero-token/Level-1/Level-2 flow. Reach for ego-browser only after one of the symptoms above shows up.

## Standing Workflow

1. `const task = await useOrCreateTaskSpace('<short task name>')` — one task space per logical job (e.g. `'google sre senior job check'`), reused across heredoc rounds for the same lookup.
2. `await openOrReuseTab(url, { wait: true, timeout: 25 })` then `await wait(2)` — SPAs (Google Careers, Workday, Careerpuck) need a beat after navigation before the DOM settles.
3. Read with `snapshotText()` for a structured pass, or `js(...)` for a targeted DOM query — see snippets below.
4. **Always** close out with `await completeTaskSpace(task.id, { keep: false })` in its own final heredoc once the lookup is done. Don't leave task spaces open — they accumulate across a session otherwise.

## Snippet A — Extract full JD text + detect an Apply control

Use this as the default lookup: it captures both the semantic snapshot (good for reading qualifications/comp/location text) and a direct DOM query for apply-like links/buttons (more reliable than searching the snapshot text for the word "Apply", since some ATS boards render the control as an SVG-icon button with no visible text).

```bash
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('<short task name>')
cliLog('task space id: ' + task.id)

await openOrReuseTab('<JD URL>', { wait: true, timeout: 25 })
await wait(2)

cliLog('pageInfo: ' + JSON.stringify(await pageInfo()))

const text = await snapshotText()
cliLog('snapshot length: ' + text.length)
cliLog(text.slice(0, 6000)) // widen/paginate as needed for long pages

// Direct DOM check — more reliable than scanning snapshot text for "Apply"
const applyLinks = await js(String.raw`(() => {
  const links = [...document.querySelectorAll('a')].filter(a =>
    a.href.includes('/apply') || (a.getAttribute('aria-label') || '').toLowerCase().includes('apply'))
  return links.map(a => ({ text: a.innerText, href: a.href, aria: a.getAttribute('aria-label') }))
})()`)
const applyButtons = await js(String.raw`(() => {
  const btns = [...document.querySelectorAll('button')].filter(b =>
    (b.innerText || '').toLowerCase().includes('apply') || (b.getAttribute('aria-label') || '').toLowerCase().includes('apply'))
  return btns.map(b => ({ text: b.innerText, aria: b.getAttribute('aria-label') }))
})()`)
cliLog('apply-like links: ' + JSON.stringify(applyLinks))
cliLog('apply-like buttons: ' + JSON.stringify(applyButtons))
EOF
```

Read the result: an empty `applyLinks`/`applyButtons` array plus a live, content-rich `snapshotText()` means the posting is real but not yet accepting applications (confirmed pattern on Google's early-career postings that go up before the Apply flow opens) — don't conclude "closed" or "fake" from that alone, say so plainly.

## Snippet B — Locate a specific JD section (qualifications, comp, responsibilities)

For long pages, pull the section around a known heading instead of reading the whole snapshot:

```js
const text = await snapshotText()
const idx = text.indexOf('Minimum qualifications')
cliLog(idx === -1 ? 'section not found' : text.slice(Math.max(0, idx - 500), idx + 2500))
```

Swap the search string for whatever heading the target board uses (`"Minimum qualifications"`, `"Requirements"`, `"What you'll bring"`, etc.) — check with a broad `snapshotText()` read first if the heading text is unknown.

## Snippet C — Liveness check (closed/expired detection)

Mirrors `modes/scan.md`'s Level-3 liveness classification, but via ego-browser for domains Playwright can't reach:

```js
const text = await snapshotText()
const lower = text.toLowerCase()
const expiredSignals = ['no longer accepting applications', 'position has been filled', 'job has been closed', 'no longer available']
const isExpired = expiredSignals.some(s => lower.includes(s)) || text.length < 500
cliLog(isExpired ? 'EXPIRED/CLOSED' : 'ACTIVE (has substantive content)')
```

## Cleanup

Every lookup ends with its own heredoc, once results are confirmed useful and nothing further is needed on that page:

```bash
ego-browser nodejs <<'EOF'
const task = await useOrCreateTaskSpace('<same short task name>')
cliLog(JSON.stringify(await completeTaskSpace(task.id, { keep: false })))
EOF
```

`{ keep: false }` is correct for essentially every career-ops lookup — there's no reason to leave a JD page open for the user afterward. Use `{ keep: true }` only if the user explicitly asked to keep a specific page open (e.g. they want to fill the form themselves right after).

## Non-Goals

- **Do not** use this to fabricate or force UI state that isn't real (e.g. injecting a fake Apply button into the DOM so it visually appears). That produces a non-functional element and misrepresents whether an application can actually be submitted — always read and report the real state instead.
- **Do not** make this the default path for boards that already work through Playwright/`scan.mjs`'s zero-token providers — that would add heredoc overhead with no benefit. Confirm one of the failure symptoms above first.
