# Prymm Enterprises GitHub Pages Site

## Overview
This repository hosts the static GitHub Pages site for Prymm Enterprises as one cohesive, single-scrolling landing page.

## Randomized Style Selection (Required)
To avoid defaulting to any preferred style, the redesign style was selected using cryptographically secure random choice:
- Method: `python` + `secrets.randbelow()` over the supplied shortlist
- Candidate order used:
  1. Swiss International Corporate
  2. Contemporary Corporate Gradient
  3. Geometric Minimal Grid
  4. Editorial Tech Modern
  5. Neo-Brutalism
- Random output: **index 2 → Geometric Minimal Grid**
- Rationale: this style best supports a professional corporate foundation with vibrant but controlled accents, strong hierarchy, and clear section-by-section procurement storytelling.

## Site Structure
- `index.html` - single-page experience composed as:
  - High-impact arrival (hero)
  - Capability coverage (product categories)
  - Sector alignment
  - Procurement workflow
  - Proof and resources
  - FAQ and final contact / request-a-quote action
- `404.html` - custom not-found page with homepage and contact links
- `robots.txt` - crawler instructions
- `sitemap.xml` - sitemap for the canonical homepage
- `CNAME` - custom domain configuration

## Design System (Professional, Corporate, Vibrant)
- Visual direction: **Geometric Minimal Grid** with corporate clarity and energetic restraint.
- Foundation: disciplined neutral surfaces with strategic vibrant accents:
  - Primary accent: `#0b5fe9`
  - Secondary accent: `#00b8a9`
  - Support accent: `#ff7a18`
- Typography roles:
  - Display: Cabinet Grotesk (headings)
  - Body: Satoshi/Inter fallback stack
- Narrative flow: arrival → capability → sectors → process → proof/resources → final CTA.
- Motion: purposeful micro-interactions only; fully disabled with `prefers-reduced-motion`.
- Themes: light and dark modes via `data-theme` toggle.

## Premium + Vibrant Refinement Layer
- Refined typography rhythm: tighter heading cadence, elevated spacing rhythm, and stronger section punctuation.
- Surface hierarchy: deeper premium shadows, polished borders, and accent-led top-edge detailing on capability/proof cards.
- Vibrancy strategy: controlled cobalt/teal/amber moments applied by section (`data-tone`) for contrast without visual clutter.
- CTA uplift: stronger gradient and depth treatment for primary actions while keeping form/contact trust cues clear.
- Interaction polish: hover/active transitions tuned with restrained easing, preserving keyboard visibility and reduced-motion behavior.

## Editable Content Areas
Look for **"Editable content placeholder"** text in `index.html`. Replace only with verified business facts:
- Catalog SKU/detail expansions
- Procurement documents/timelines
- Case studies and measurable outcomes
- Company profile download link target

## Responsive Rules
- Mobile-first baseline: 375px+
- Tablet: `@media (min-width: 768px)`
- Desktop: `@media (min-width: 1280px)`
- Must remain one cohesive scrolling page without horizontal overflow.

## Interaction Behavior
- Sticky header with desktop and accessible mobile navigation.
- Mobile menu supports:
  - `aria-expanded`
  - Escape to close
  - focus trap and focus return
- FAQ accordion supports keyboard and `aria-expanded` state.
- Contact actions and CTA clicks emit `dataLayer` events.
- Request-a-Quote form is static-only with:
  - inline validation
  - `aria-invalid` field states
  - `aria-live` status updates
  - honeypot anti-spam field
  - mailto fallback generation

## Contact Details (Preserved)
- Website: `https://www.prymm.enterprises`
- Email: `info@prymm.enterprises`
- Phone: `+639524669089`

## Accessibility + QA Checklist
- [ ] Keyboard navigation across links, buttons, form controls
- [ ] Skip link reaches `#main`
- [ ] Mobile menu works with button, Escape, and focus return
- [ ] Visible focus indicators present
- [ ] Form labels/errors/status are announced and readable
- [ ] FAQ toggles work with keyboard and semantic state
- [ ] Touch targets are at least 44px
- [ ] Reduced-motion preference is respected
- [ ] No horizontal overflow at 375px / 768px / 1280px
- [ ] Internal anchors map to existing section IDs
- [ ] Contact links (`https`, `mailto`, `tel`) and quote fallback behavior work

## Validation Steps Used In This Repository
- Static integrity check: Python `html.parser` parse + internal anchor target check for `index.html`
- Inline JS syntax check: `node --check` against extracted inline script
- Responsive QA pass: reviewed 375px, 768px, and 1280px layouts for no horizontal overflow and stable section rhythm

## Analytics Configuration
The site emits privacy-conscious `dataLayer` events only:
- `menu_open`
- `contact_click`
- `form_start`
- `form_submit`
- `product_interest`
- `profile_download_click`
- `faq_toggle`

To integrate analytics, add an approved analytics/tag-manager setup that consumes `window.dataLayer`.

## Deployment
This is a static GitHub Pages deployment.

### DNS / Custom Domain Notes
- `CNAME` is set to `prymm.enterprises`.
- If domain settings change, update `CNAME`, canonical URL metadata, `robots.txt`, and `sitemap.xml` together.
