# Prymm Enterprises GitHub Pages Site

## Overview
This repository hosts the static GitHub Pages site for Prymm Enterprises as one cohesive, single-scrolling landing page.

## Site Structure
- `index.html` - single-page experience composed as:
  - Statement (hero)
  - Explanation (category coverage)
  - Value (industry alignment + procurement process)
  - Proof (trust signals + resources)
  - Action (FAQ + contact/request-a-quote)
- `404.html` - custom not-found page with homepage and contact links
- `robots.txt` - crawler instructions
- `sitemap.xml` - sitemap for the canonical homepage
- `CNAME` - custom domain configuration

## Modernist Design System
- Direction: calm, authoritative, disciplined, and functional.
- Foundation: neutral architectural surfaces with two controlled accents:
  - Primary accent: `#3158f5`
  - Secondary accent: `#d67b11`
- Typography roles:
  - Display: Cabinet Grotesk (headings)
  - Body: Satoshi/Inter fallback stack
- Layout: generous whitespace, measured cards, subtle grid overlay, restrained asymmetry.
- Motion: subtle hover/focus transitions only; full reduced-motion support via `prefers-reduced-motion`.
- Themes: light and dark modes via `data-theme` toggle.

## Editable Content Areas
Look for **"Editable content placeholder"** text in `index.html`. Replace only with verified business facts:
- Catalog SKU/detail expansions
- Procurement documents/timelines
- Case studies and measurable outcomes
- Company profile download link target

## Breakpoints
- Mobile-first baseline: 375px+
- Tablet: `@media (min-width: 768px)`
- Desktop: `@media (min-width: 1280px)`

## Interaction Rules
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
- [ ] No visible layout shift during interactions/theme toggles

## Validation Steps Used In This Repository
- Static integrity check: Python `html.parser` parse + internal anchor target check for `index.html`
- Inline JS syntax check: `node --check` against extracted inline script

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
