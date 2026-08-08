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

## Design System (Corporate Minimalist)
- Visual direction: refined corporate-minimalist presentation of the merged single-page layout.
- Foundation: disciplined neutral surfaces with one primary accent and restrained secondary sector accents:
  - Primary accent: `#0b5fe9`
  - Secondary accent: `#2c8f84`
  - Support accent: `#a86822`
- Typography roles:
  - Display: Cabinet Grotesk (headings)
  - Body: Satoshi/Inter fallback stack
- Narrative flow: arrival → capability → sectors → process → proof/resources → final CTA.
- Motion: precise micro-interactions only; fully disabled with `prefers-reduced-motion`.
- Themes: light and dark modes via `data-theme` toggle.

## Corporate-Minimalist Refinement Notes
- Reduced decorative gradients and ornamental geometry to improve scan speed and trust-oriented clarity.
- Simplified card/panel treatments with consistent alignment, lighter shadows, and cleaner section rhythm.
- Preserved high-contrast CTA emphasis while keeping accent usage disciplined.
- Maintained one-page narrative order from hero through capabilities, sectors, process, proof, FAQ, and final contact/quote action.
- Preserved accessibility behaviors (focus visibility, keyboard navigation, touch targets, reduced-motion support, form errors/status, FAQ semantics).

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
- CI status check: reviewed recent GitHub Actions workflow runs and confirmed no failed jobs in the latest Pages deployment run.

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
