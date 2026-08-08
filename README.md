# Prymm Enterprises GitHub Pages Site

## Overview
This repository hosts the static GitHub Pages site for Prymm Enterprises as one cohesive single-scrolling landing page.

## Site Structure
- `index.html` - single-page narrative:
  - Hero impact
  - Capability overview
  - Industry sectors
  - Procurement process
  - Trust and proof
  - FAQ
  - Final CTA with contact and Request-a-Quote form
- `404.html` - custom not-found page with homepage and contact links
- `robots.txt` - crawler instructions
- `sitemap.xml` - sitemap for the canonical homepage
- `CNAME` - custom domain configuration

## Design System (Modernist + Corporate + Tech + Luxury Minimal)
- Foundation: neutral architectural surfaces with restrained accent hierarchy.
- Accents:
  - Primary: `#1a4fb7`
  - Secondary warm accent: `#6f5b3e`
  - Supporting cool accent: `#9db6eb`
- Typography:
  - Display: Cabinet Grotesk
  - Body: Satoshi/Inter fallback stack
- Principles used:
  - Modernist: strict spacing rhythm, clear lines, hierarchy-first grid.
  - Corporate professional: trust-focused messaging and procurement clarity.
  - Tech forward: precise states, subtle interaction feedback, practical data framing.
  - Luxury minimal: premium restraint, generous whitespace, reduced visual clutter.
- Themes: light/dark mode via `data-theme` toggle.
- Motion: subtle hover and state transitions; disabled under `prefers-reduced-motion`.

## Contact Details (Preserved)
- Website: `https://www.prymm.enterprises`
- Email: `info@prymm.enterprises`
- Phone: `+639524669089`

## Accessibility + UX Preserved
- Skip link to `#main`
- Keyboard navigation and visible focus
- 44px minimum interactive targets
- Accessible mobile nav: `aria-expanded`, Escape to close, focus trap + focus return
- FAQ semantic toggles with `aria-expanded`
- Form labels, inline validation, `aria-invalid`, `aria-live` status
- Reduced-motion support

## Analytics Hooks Preserved
The page emits `window.dataLayer` events:
- `menu_open`
- `contact_click`
- `form_start`
- `form_submit`
- `product_interest`
- `profile_download_click`
- `faq_toggle`

## Validation Notes
- Parsed `index.html` for internal anchor/ID integrity.
- Checked inline JavaScript syntax.
- Verified SEO/static assets remained intact (`CNAME`, canonical URL, JSON-LD, `robots.txt`, `sitemap.xml`, `404.html`).
- Reviewed recent GitHub Actions workflow runs and failed-job logs (none in latest Pages run).

## Deployment
This is a static GitHub Pages deployment.

### DNS / Custom Domain Notes
- `CNAME` is set to `prymm.enterprises`.
- If domain settings change, update `CNAME`, canonical URL metadata, `robots.txt`, and `sitemap.xml` together.
