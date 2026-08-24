# Jaano — marketing site

The public site for **Jaano**, the configurable video-verification platform by
Blostem Fintech Pvt. Ltd.

Single self-contained page. No framework, no bundler, no build step required to
deploy — `index.html` plus `assets/` is the whole site.

---

## Deploy

Copy `index.html` and `assets/` to any static host:

```bash
# Netlify / Vercel / S3 / nginx — publish directory is the repo root
# Nothing to install, nothing to compile.
```

The only external requests are Google Fonts (Inter + JetBrains Mono), matching
the existing production site.

### The lead form

`#lead-form` POSTs JSON to **`/api/lead`** with a honeypot field (`website`) and
success/error states already wired. Point it at your existing endpoint or change
the URL in `build/09-js.part` and rebuild.

---

## Rebuild

The page is generated from parts so repeated structures stay uniform.

```bash
cd build
python3 dgm.py      # regenerate the SVG diagrams (lifecycle, Blostem bridge)
python3 rot.py      # regenerate the hero rotator scenes
python3 build.py    # assemble → ../index.html
```

`build.py` inlines every CSS part, injects the generated diagrams, and expands
the partner marquee from `logos.py`.

### Adding a partner logo

Drop the file into `assets/logos/` named after the brand, lowercase and
alphanumeric only (`shriramfinance.svg`), then rebuild. Brands without a file
render as a typographic chip, so the row is never broken and never shows a
missing image. See `NOTES.md` for the mono/mark/scale rules.

---

## Layout

```
index.html              the deployable page
assets/
  logos/                partner logos (19 of 20 brands)
  img/                  character portraits used in the hero rotator
build/
  *.part                CSS and markup sources, assembled by build.py
  build.py              assembler
  dgm.py                SVG diagram generator
  rot.py                hero rotator generator
  logos.py              partner-chip builder
  *.json                traced logo paths + measured logo aspect ratios
NOTES.md                design system, QA results, and decisions with rationale
```

---

## Before publishing

1. **Partner attribution.** Jaano is pre-launch. The partner marquee sits in the
   Blostem block and states this explicitly. Do not move it above the fold — next
   to the hero it reads as Jaano's own customers. See `NOTES.md`.
2. **Logo licensing.** Partner marks are used nominatively to identify Blostem's
   partners. Confirm against each partnership agreement.
3. **`--ink-faint` contrast.** Documented in `NOTES.md`.

---

© Blostem Fintech Pvt. Ltd.
