# Prymm Enterprises GitHub Pages Site

## Overview
This repository hosts the static GitHub Pages site for Prymm Enterprises.

## Site Structure
- `index.html` - single-entry static page with:
  - Hero
  - Products/Catalog
  - Industries/Solutions
  - Procurement Process
  - Projects/Case Studies
  - Resources/Company Profile
  - FAQ
  - Contact + Request a Quote form
- `404.html` - custom not-found page with homepage and contact links
- `robots.txt` - crawler instructions
- `sitemap.xml` - sitemap for the canonical homepage
- `CNAME` - custom domain configuration

## Editable Content Areas
Look for **"Editable content placeholder"** text in `index.html`.
These are intentionally marked to be replaced only with verified data:
- Catalog SKU/detail expansions
- Procurement documents/timelines
- Case studies and outcomes
- Company profile download link target

## Contact Details (Preserved)
- Website: `https://www.prymm.enterprises`
- Email: `info@prymm.enterprises`
- Phone: `+639524669089`

## Form Behavior
The quote/inquiry form is static-only and GitHub Pages compatible:
- Client-side validation with inline errors
- `aria-live` feedback for status updates
- Honeypot field for lightweight spam filtering
- Mailto fallback generation with populated subject/body
- No backend storage is implemented

## Accessibility QA Checklist
- [ ] Keyboard navigation across all links, buttons, form controls
- [ ] Skip link reaches `#main`
- [ ] Mobile menu opens/closes with button, Escape, and focus return
- [ ] Visible focus indicator appears on interactive elements
- [ ] Form errors are announced via inline text and `aria-invalid`
- [ ] FAQ accordion works with keyboard and `aria-expanded`
- [ ] Touch targets are at least 44px where practical
- [ ] Reduced-motion preference respected

## Performance QA Checklist
- [ ] Confirm no unnecessary JS libraries are added
- [ ] Verify preconnect + limited font weights are used
- [ ] Verify no layout shift from interactive UI changes
- [ ] Validate page remains lightweight and static-host friendly

## Analytics Configuration
The site emits privacy-conscious `dataLayer` events only:
- `menu_open`
- `contact_click`
- `form_start`
- `form_submit`
- `product_interest`
- `profile_download_click`
- `faq_toggle`

To integrate analytics, add your approved tag manager/analytics setup that reads from `window.dataLayer`.
No external tracking service is injected by default.

## Deployment
This is a static GitHub Pages deployment.

### DNS / Custom Domain Notes
- `CNAME` is set to `prymm.enterprises`.
- Ensure DNS records for GitHub Pages point to the correct GitHub Pages endpoints.
- If domain settings change, update `CNAME`, `canonical`, `og:url`, `twitter` metadata, `robots.txt`, and `sitemap.xml` together.

## Placeholder Replacement Guidance
When replacing placeholders:
1. Use only verified business information.
2. Do not add unverified claims (location, certifications, customer counts, delivery guarantees, inventory, pricing).
3. Keep links relative for internal navigation and maintain accessibility attributes.
