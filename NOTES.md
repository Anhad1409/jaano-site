# Jaano — full website (v2)

Single self-contained `index.html`, 175 KB. No framework, no build step.
Only external requests: Google Fonts (Inter + JetBrains Mono) — same as production.

## Deploy
Drop `index.html` at the web root. The lead form POSTs to `/api/lead` with the
same JSON contract, honeypot field and success/error states as the current site —
your existing endpoint works unchanged.

## Page (11 sections)
hero → trusted marquee → use cases (6) → lifecycle diagram → engine (6) →
capture modes (3) + coverage matrix → evidence integrity (hash chain) →
integration (code + steps + stats) → company (Blostem bridge) → trust
(banks + certs + session controls) → demo (what-you'll-see + working form) → footer

## Graphics — all computed, no hand-placed coordinates
- **Hero rotator (signature element)**: five scenes that *perform* the process rather
  than describe it, flipping every 3.2s with a 3D-tilt crossfade.
  Cadence: 3.2s per scene. Tabs double as a progress bar.

  1. **Live capture** — phone with face-landmark reticle, spoken liveness code, geo/time
     stamp; beside it the three evidence guarantees (geo-lock, live-only, gallery blocked)
  2. **Signals & OCR** — PAN card with field boxes resolving one by one, extracted values
     with confidence scores, and a doc-vs-live face-match strip
  3. **Human review** — auditor console: checklist, live tile, signal meters,
     maker–checker strip, Return / Approve
  4. **Signed decision** — webhook payload, tamper-evident seal, hash chain popping in
  5. **V-CIP approved** — verification record with a rubber stamp pressing down
     (`scale(2.3)→1`, multiply blend) and a deterministic QR built from the case hash

  Scenes are CSS grids, so nothing can clip or collide at any width. Tabs implement the
  WAI-ARIA tablist pattern: roving tabindex, ←/→/Home/End, auto-advance pauses on hover,
  on focus, and when the tab is backgrounded.
- **Lifecycle diagram**: 5 nodes on a computed grid (`build/dgm.py`), stroke-draw on
  scroll, travelling packets, retry loop and webhook return path.
- **Bridge diagram**: platforms → Blostem → banks, chip columns auto-sized from name
  length, real traced Blostem logo.
- **Hash chain**: 5 linked blocks, staggered pop-in, `← prev` pointers.
- **Coverage matrix**: 6 use cases × 3 capture modes.

## Brand logos — 20 of 20, in all three sections
Real logos are in `assets/logos/`, sourced from Wikipedia article images and the
companies' own homepages, then **each one rendered and visually verified** before use:

    Zerodha · MobiKwik · Upstox · Jupiter · Jio Finance · Tide
    Aditya Birla Capital · Kfintech · GoldenPi · Fello · Aspero · Centricity
    IndusInd Bank · Bajaj Finance · Mahindra Finance · Suryoday SFB
    Utkarsh SFB · Shivalik SFB

Logos render in **three** places, not just the marquee:
1. **Marquee** — logo alone (wordmarks already carry the name)
2. **Bridge diagram** — `<image>` inside each SVG chip, sized from a measured aspect
   ratio (`build/logo-aspect.json`). Chips share one width: a ragged column reads as
   broken layout, not as design.
3. **"Backed by" row** — Rainmatter, MobiKwik and AC Ventures marks

Aspect ratios are **measured in a browser**, not parsed from the file: `mobikwik.svg`
carries a viewBox (aspect 19.9) that contradicts its width/height (4.47), and trusting
the viewBox letterboxed it badly. `scripts/asp.cjs` regenerates the JSON.

A brand with a logo renders as the logo alone (these are wordmarks — the name is in the
mark). The other 9 render as typographic chips with matching metrics, so the row stays
uniform and never shows a broken image.

**Unity SFB** publishes only a square mark (no wordmark), so it renders via the
`MARK` set in `build/logos.py` as **mark + name** — a bare symbol is unidentifiable
in a row of wordmarks.

**All 20 brands now carry a verified logo.** Shriram Finance was the last holdout —
their header logo is JS-injected and absent from the homepage HTML, but interior pages
(`/about-us`, `/contact-us`) reference `cdn.shriramfinance.in`, which serves the real
`sw-logo.svg`. Note the trap: Wikipedia's Shriram article carries `Shriram Group.svg`,
which reads "SHRIRAM **Capital**" — a different group entity, and wrong on a chip
labelled Shriram Finance.

**Blue Lotus Ventures** is now a logo too (their real lockup lives at
`/wp-content/uploads/2023/04/Group-2.svg`, not the visitor-widget asset the
homepage advertises).

**GrowX stays text, deliberately.** Their mark is a tree built from tiny
letterforms — authentic, and legible at 150px+, but an unreadable smudge at the
~22px a chip renders. Their SVGs collapse to a single glyph (unembedded fonts).
A logo has to survive its render size to earn the slot.

Logos appear in THREE places and they are generated separately:
`logos.py` (marquee, backed-by), `dgm.py` (bridge diagram, base64-free `<image>`),
and the deck's `s12.part` (base64-embedded). **Adding a logo means re-running
`dgm.py` as well as `build.py`** — `build.py` injects a pre-generated bridge.

Two normalisations live in `build/logos.py`:
- `SCALE` — square marks (Jio, Bajaj, tide) read smaller than wordmarks at equal
  height, so they are scaled by eye, not by pixel height.
- `MONO` — Aspero, Centricity and Utkarsh publish white-on-transparent marks that are
  invisible on a white chip; `filter:brightness(0)` renders each in its own mono form.
  Verified against light, dark and darkened renders before enabling.

Rejected during verification, and why it matters: a Wikipedia *search* fallback
fuzzy-matched HDFC Bank's logo to Upstox, Mitsubishi's to Shriram and ICICI's to
Suryoday — all discarded. `kfintech` resolved to a bare triangle fragment;
`acv.vc` served a logo for a company called "OY!", `bluelotus.vc` served a visitor-counter
widget asset, and `kfintech/logo-shape.svg` is a bare triangle fragment — all discarded.
One file was rescued rather than rejected: Aditya Birla Capital publishes its logo at a
path ending `.webp` that is actually **SVG data**, so it decoded as a broken image until
renamed. Never ship a logo you have not looked at.

Licensing note: these are the companies' own marks used nominatively to identify
partners. Confirm with each partnership/marketing agreement before publishing.

## Cross-browser & motion safety
- Travelling dots on the diagrams ride `offset-path`, which Safari only supports from
  16. They carry no `cx`/`cy`, so unguarded they would paint as stray dots at each
  diagram's top-left corner on older Safari. They are `display:none` by default and
  enabled only inside `@supports (offset-path:path('M0 0'))`.
- Under `prefers-reduced-motion` the hero rotator keeps advancing (5s instead of 3.2s)
  but swaps instantly with no transform — a frozen carousel reads as broken, while
  parallax and 3D tilt are the parts that actually cause vestibular problems.

## Faces in the rotator
The camera tiles use real character portraits cropped from the approved Jaano hero
illustration (`assets/img/face-customer.webp`, `face-agent.webp`) with the detection
mesh drawn over them. The face-match strip compares the doc photo and the live tile
of the SAME person — never two different people.

## Brand attribution (pre-launch)
Jaano is pre-launch. The partner marquee therefore sits in the Blostem block
(between #company and #trust), NOT after the hero, and its lede states plainly:
"Jaano is pre-launch — no one is using it yet. Every name below is a partner of
Blostem." Do not move it back above the fold — placement next to the hero reads
as Jaano's own customers.

The 48-hour sandbox promise was removed here too (stat tile now "1 REST call to
integrate"; the form footnote drops the 48h line) — same feasibility call as the deck.

## Motion inventory
riseIn/zoomIn scroll reveal (with anchor-jump fallback sweep) · SVG stroke draw-in
(lengths measured per path at runtime) · offset-path travelling packets · dual
marquee at constant px/s · gradient-pan CTA · scan lines · count-up stats ·
scrollspy nav + progress bar · barGrow meters · chain pop-in.
Plus three borrowed from the GFF landing family: `jgrid` (blueprint grid drifts
slowly — the system is on), `beamPan` (a faint violet beam along the stuck nav's
border), and `lineLaunch` (hero headline lines rise with a slight rotateX on load).
`prefers-reduced-motion` disables every one of them; verified 0 invisible elements.

## DLS
All 16 tokens byte-identical to the deployed `styles.css`. Same type, same component
language. Additive tokens only (green-soft/deep, amber, danger).

## Verified
- 1440 / 768 / 390: no overflow, 0 console errors, 0 dead anchors, all reveals fire
- Form: empty submit blocked by native validation; network failure shows error state
  and re-enables the button; honeypot present
- 1 h1 · header/nav/main/footer landmarks · reduced-motion: marquee off, nothing hidden
- Rotator geometry: every scene checked for element-on-element overlap and for content
  escaping the stage, at 390 / 430 / 560 / 768 / 1440 — all clean
- Rotator: arrow/Home/End keys verified, roving tabindex correct, exactly one panel
  rendered at a time, auto-advance pauses on focus; under reduced-motion auto-advance
  is off, the stamp is shown statically, and manual tab switching still works

## Brand attribution — resolved
Naming these companies on a Jaano page is approved **on the condition that they are
labelled as Blostem relationships, never as Jaano customers.** Every mention on the page
is written to that rule, and the wording is load-bearing — do not loosen it in edits:

| Where | Label |
|---|---|
| Marquee eyebrow | "Platforms & institutions building on Blostem" |
| Marquee lede | "The names below are Blostem's platform and institutional relationships." |
| Bridge diagram | "30+ platforms building on Blostem" / "10+ banks & NBFCs on the other side" / "Jaano runs on this stack" |
| Bridge alt text | "Blostem sits between … Jaano runs on the same stack." |
| Trust label | "**Blostem is live with**" (not a bare "Live with") |
| Trust footnote | "These are Blostem platform relationships, not Jaano deployments." |
| Company section | "Backed by" — Blostem's investors |

The trust section originally read "Live with" directly under a sentence about Jaano,
which parses as *Jaano* being live with those banks. That was the page's only overclaim
and is fixed. An audit script pattern to re-check after edits:

    Jaano[^.]{0,120}?(clients?|customers?|live with|used by|trusted by)

should return no matches.

## Confirm before publishing
1. `--ink-faint` (#94a3b8) is 2.48:1 on the background — kept for DLS parity; below AA
   for the small mono labels. `#6b7190` reaches 4.6:1 if you ever want it.
2. Coverage-matrix cells are inferred from the use-case copy — confirm the ✓/— map.

## Source
`build/*.part` + `build/dgm.py` (diagram generator) + `build/build.py`. Rebuild:
`cd build && python3 dgm.py && python3 build.py`
