# UX/UI / Design Audit — Oleksandr Halushka (Auto + Bau)

**Auditor:** AI design critic, perspective of average Bayern visitor (DE first, EN/UK/RU fallbacks)
**Date:** 2026-05-04
**Repo state:** post-rebrand from "Oleksandr Halushka" → "Oleksandr Halushka", `main` branch
**Pages reviewed:** `index.html` (split landing), `auto/{index,leistungen,uber-uns,kontakt}.html`, `bau/{index,leistungen,uber-uns,kontakt}.html`, `legal/impressum.html`
**Method:** static read of HTML/CSS/JS + asset inventory + i18n key counts. No live render performed (no headless browser executed) — visual judgements are derived from code + measurements.

---

## TL;DR — Executive Summary

The site has a **strong conceptual frame** (split-screen landing, dual themes, mehrsprachig, anti-spam form, smart-header) and a polished hero on both branches. But four **showstoppers** undermine its credibility before a customer ever fills the form:

1. **Impressum has placeholder data** ("Musterstraße 123 · 80331 München · DE123456789"). For a German Einzelunternehmer this is an actionable Abmahnung risk under § 5 TMG. **P0, fix today.**
2. **Auto theme has split brain** — design tokens declare Steel Blue (`#3b7dd8`) but every inline `<style>` block on Auto pages still uses the old red `#e63946` (eyebrows, icons, timeline dots, service-card borders, form-submit hover). The result on screen is a red-painted body with a blue header — visually broken.
3. **Bau translations are missing** — Bau pages have only 6–12 `data-i18n` attributes versus 23–55 on Auto. EN/UK/RU users drop into German on every Bau page. Lang-switcher silently does nothing on Bau.
4. **Bau hero promises "Umzugsservice / Möbelmontage"** but the Leistungen page has **no such block**. The form-select has a "Möbelmontage" option that maps to nothing. Promise/delivery mismatch.

Beyond those, brand-after-rebrand is patchy: instagram handles `@Oleksandr Halushkae.auto` / `@Oleksandr Halushkae.innenausbau` and email `info@Oleksandr Halushkae.de` remain (these may be intentional legacy URLs but should be confirmed). Hero PNGs are 600–730 KB **uncompressed PNG** — first-paint is heavy. No Open Graph, no canonical, no JSON-LD, no sitemap, no robots.txt — SEO baseline is essentially zero. One Bau page (`uber-uns.html`) has a malformed structure with the footer nested inside an unclosed `<section>`.

Despite this, the architecture, microinteractions, and form UX are above local-business average. With a focused 2-day fix sprint the site can move from "sketchy" to "trustworthy".

**Overall site grade: 2.8 / 5** — visually ambitious, conceptually right, executionally inconsistent.

---

## 1 — First impression / 5-second test (split-screen `index.html`)

**Score: 4 / 5**

### Findings

- The layout is genuinely distinctive: dark-left (Auto), warm-light-right (Bau), thin centered "AG" badge in a glass pill, hover-triggered flex 0.82↔1.18 split. Microcopy is clean: "Richtung wählen" → KFZ-Service / Innenausbau → button + arrow hint.
- Background images load `auto-bg.jpg` (305 KB) and `bau-bg.jpg` (203 KB). Both reasonably sized, both 100vh. Acceptable.
- 5-sec test verdict: a German visitor can identify "two services, one brand, choose your side" within 2 seconds. Strong.
- The fixed center "AG" monogram badge is a smart anchor — but post-rebrand this no longer matches the brand name "Oleksandr Halushka". "AG" is an old Oleksandr Halushka initial.
- Hover effect (lines 54–78 of `index.html`): scale(1.05) on bg, brightness/saturate dim on the non-hovered side, opacity 0.25 on the dimmed content. Tasteful and not nauseating.

### Issues

- **The "AG" badge is brand-stale** (legacy Oleksandr Halushka). For Oleksandr Halushka it should be "OH" or a wordmark-derived monogram. Current state communicates "we couldn't be bothered to update".
- **Mobile: header `splash-header` mode** never reveals on the splash unless mouse moves to top — but there is no mouse on mobile. The header on mobile is therefore **invisible** on the landing page (lines 499–510 of `global.css`: `splash-header` starts at opacity 0 and only `.visible` shows it; the SmartHeader code only adds `.visible` via `show()` which on splash is gated by mouseNearTop or scrollY≤10). On mobile splash there's no scroll past 10px, so initial show() *should* fire — but there's no language switcher, no theme switch, nothing reachable until the user taps a side. That's actually OK as-is, but the burger and lang-switcher are practically inaccessible on the splash.
- **Hover-effect on touch devices** does nothing — there's no tap-feedback before the click navigates away. A mobile user just taps and gets navigated. This is fine, but note: `cursor: pointer` is misleading on touch.
- The "Bereich betreten" arrow is hidden by default (opacity 0) and only appears on hover. On touch this animation is never seen. Not critical.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 1.1 | Replace "AG" monogram badge with wordmark "OH" or stylized lowercase "oh." | **P1** | 5 min |
| 1.2 | Drop `cursor: pointer` from `.split-side` on touch devices via `@media (hover: hover)` guard | **P3** | 5 min |
| 1.3 | Consider `<picture>` with WebP for `auto-bg.jpg` / `bau-bg.jpg` to shave ~30–50% off first-paint weight | **P2** | 30 min |

---

## 2 — Navigation & header

**Score: 3 / 5**

### Findings

- Smart header (`js/components/smart-header.js`) hides immediately on scroll-down, reveals only when scrollY≤10 OR mouse near top edge (<72px). On touch: swipe-up at top triggers reveal.
- Header is glass (backdrop-filter blur 18px, rgba(14,17,23,0.7)). Pretty.
- Theme switcher has two pill buttons "Auto" / "Bau". On Auto pages, "Auto" is `.active` (blue pill). On Bau, "Bau" is `.active` (amber pill). Click → location change. Functional.
- Lang-switcher renders 4 buttons (DE/EN/UK/RU) as text labels (no flags, just text). Active state is rgba white background.
- Burger menu at ≤768px: hamburger → fullscreen overlay nav, links centered, `body { overflow: hidden }` while open.
- Logo wordmark `OLEKSANDR<span>HALUSHKA</span>`: ~17 characters, two-tone (bold + thin). At 1rem font-size with 1.5px tracking that's ≈ 200px wide on desktop.

### Issues

- **`global.css` has `responsive` block defined TWICE** (lines 514–907 and again 909–1225). Identical-but-not-quite duplicates — older block uses `min-height: 100svh` for hero, etc. Whichever loads last wins (the second). This is dead 200+ lines of CSS shipped to every page. Verifiably unused/duplicated.
- **Logo wordmark + theme-switcher + langSwitcher + burger** are crammed into a 76px tall bar. On 1024–1280px viewports, the wordmark "OLEKSANDR HALUSHKA" + nav (4 links) + theme pill + lang (4 buttons) all compete for horizontal space. Almost certainly overflows or wraps awkwardly between 1024–1100px (no measured breakpoint addresses this). On tablet portrait it's masked by burger mode. **Visual regression risk between 1024–1280**.
- **Theme switcher is unlabeled and ambiguous**. A first-time visitor sees "Auto / Bau" pills next to language pills — what happens if I click? Does it filter? Switch language? Toggle theme? It actually navigates between completely different sites, which is a heavy action behind a small pill. Needs an `aria-label="Bereich wechseln"` AND a tooltip / hover hint.
- **Hide-on-scroll-down** is implemented well but creates UX paper-cut: a user reading a long Leistungen page who wants to switch language must scroll **all the way back up** before the header reappears. The mouse-near-top trigger helps on desktop, not on mobile or trackpad-down-scroll.
- **`#langSwitcher` is `display: none` at ≤480px** (line 727 + 1080). Mobile users on phones <480px wide cannot change language. That's roughly any iPhone in portrait that isn't a Pro Max. Significant for a multilingual ukrainian-targeted site.
- **No visible "skip to main content" link** — keyboard/screen-reader users tab through the nav each time.
- **Cookie banner** (smart-header.js lines 146–234) is German-only ("🍪 Ihre Privatsphäre ist uns wichtig…"). Hardcoded German text means EN/UK/RU visitors see German consent. **GDPR concern: consent must be in user's language to be informed**.
- **Cookie banner uses `localStorage` key `Oleksandr Halushkae_cookie_consent`** — leaks legacy brand into client storage. Cosmetic but consistent with brand drift.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 2.1 | Remove duplicated responsive blocks in `global.css` (lines 909–1225) | **P1** | 15 min |
| 2.2 | Add `aria-label="Sprache wechseln"` to lang switcher container; add `title="Bereich wechseln"` to theme-switcher pills | **P1** | 5 min |
| 2.3 | Show `#langSwitcher` on phones ≤480px (or move into burger overlay) | **P1** | 10 min |
| 2.4 | i18n the cookie banner text — load string from current locale, not hardcoded DE | **P0** (GDPR) | 20 min |
| 2.5 | Rename localStorage key `Oleksandr Halushkae_cookie_consent` → `oh_cookie_consent` (keep legacy read for migration) | **P3** | 10 min |
| 2.6 | Add a `<a href="#main" class="skip-link">Zum Inhalt springen</a>` at top of body, visually hidden until focused | **P2** | 10 min |
| 2.7 | Add a `1024–1280px` audit breakpoint or shrink logo wordmark when nav width tight | **P2** | 30 min |

---

## 3 — Hero sections (`auto/index.html`, `bau/index.html`)

**Score: 4 / 5**

### Findings

- Both heroes are 88vh tall, min-height 560px, with bg-image scaled 1.06 and animated to 1.0 over 8s (subtle Ken-Burns).
- Auto hero h1 uses `clamp(2.6rem, 5.5vw, 4.8rem)` — fluid, readable. White-to-blue gradient text-clip. Strong.
- Bau hero h1 uses two lines: `<strong>Innenausbau</strong>` + thin "mit Leidenschaft" — a good typographic hierarchy: one bold + one elegant thin (font-weight 300 + 800).
- Both heroes have eyebrow "Oleksandr Halushka · Bayern" — clear positioning.
- Two CTAs each: primary (Beratung anfragen / Angebot anfragen) + secondary (Alle Leistungen).

### Issues

- **Hero PNG sizes**: `auto_hero.png` 608 KB, `bau_hero.png` 670 KB. PNG for photographic content is wasteful; WebP would be ~120–180 KB. **First-paint LCP suffers**.
- **Auto eyebrow color is `#e63946` (red)** while the global token is `--color-auto-primary: #3b7dd8` (blue). The eyebrow + many other accents shout red while the H1 text gradient ends in blue. This is the **theme split-brain** mentioned in TL;DR.
- **Bau hero text legibility**: gradient overlay is `rgba(255,250,240,0.56)` to `rgba(250,245,235,0.65)` over `bau_hero.png`. With a hero photo that has bright zones, dark blue text (#0f172a) at font-weight 300 may dip below 4.5:1 contrast in the brightest patches. Without a test render I can't measure exactly, but the lightness of overlay + thin font weight is a known risk pattern. Worth a contrast check.
- **Auto hero gradient overlay `rgba(0,0,0,0.6) → rgba(5,5,18,0.7)`** is heavy enough to keep contrast safe. Auto is fine.
- **Hero CTA-secondary on Bau** (`btn-secondary-bau`) has `color: #0f172a, border-color: #0f172a` per `global.css` line 369–377. On a sunlit hero bg it should be readable but a backdrop-filter would make it bullet-proof.
- **`.hero-content p`** is gated to `max-width: 520px` — desktop fine, mobile fine. OK.
- **No `loading="eager"` / `fetchpriority="high"` hint for hero**. As LCP element it should be hinted.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 3.1 | Convert hero PNGs to WebP (with PNG fallback via `<picture>`); target ~150 KB each | **P1** | 30 min |
| 3.2 | Replace inline `#e63946` eyebrow color in `auto/*` with `var(--color-auto-accent)` (#4facf7) so accent matches steel-blue theme | **P0** (brand integrity) | 1 h |
| 3.3 | Run a Bau-hero contrast probe on `bau_hero.png`; if <4.5:1 increase overlay opacity to 0.72/0.80 | **P1** | 15 min |
| 3.4 | Add `<link rel="preload" as="image" href="../assets/auto_hero.webp" fetchpriority="high">` to head on each branch | **P2** | 10 min |

---

## 4 — Index page sections: Counter / Services teaser / Why / Pricing / Testimonials / CTA

**Score: 3 / 5**

### Findings

- Block sequence on `auto/index.html`: Hero → Counter → Services teaser (4 cards) → Pricing (Kostenlos card) → Why (4 items) → Testimonials → CTA band → Footer. Logical.
- Block sequence on `bau/index.html`: Hero → Counter → Services teaser (4 cards w/ modals) → Why → Testimonials → CTA → Modals → Footer. Logical.
- Counter band: 4 numbers each. **Auto: "5+ years, 2000+ clients, 100% Profi-Qualität, 100% Transparenz"**. **Bau: "10+ years, 300+ projects, 5★ rating, 100% Qualitätsgarantie"**.
- Service cards on Auto are static (no modal). Bau cards open `data-modal` overlays with detailed bullet lists. Different UX patterns between branches.
- Testimonial slider: `js/components/testimonial-slider.js` — 6 reviews per branch, auto-advance every 5s, hover-pause, dots + arrows. **Working** (data is hardcoded; not empty).
- The dialect is Bavarian-flavored ("nix aufschwatzen", "passt!", "der Chef") — gives authenticity.

### Issues

- **Counter values are not credible side-by-side**: Auto claims "2000+ Zufriedene Kunden" but Bau claims "300+ Abgeschlossene Projekte". For an Einzelunternehmer 2000 clients in 5 years = ~400/year = 1.5/day, every working day. That number reads inflated. The Über-uns timeline-4 also says "2000+ zufriedene Kunden". For a recently-rebranded solo business this risks losing trust if scrutinized. Recommend more conservative numbers ("100+ / 50+") or remove counters entirely.
- **"100% Profi-Qualität" is a meaningless metric** as a counter. Counters work when there's a number. Replace with something measurable: "4.9★ Bewertung" or "24h Antwortzeit".
- **Auto pricing card is a single card alone in a `.services-grid`** — visually it sits awkwardly as a lonely centered card with `max-width: 720px`. This works but looks like a placeholder-with-content — could be a band or a CTA stripe.
- **Bau index has NO equivalent "Kostenlose Erstberatung" pricing section** — asymmetry with Auto. Customers visiting both branches see different offer structures.
- **Testimonials**: 6 each, fine. But all display together in a `.testimonials-grid` layout AND simultaneously the slider rewrites that container. The container is a `.testimonials-grid` but testimonial-slider.js replaces innerHTML with a `.ts-wrapper` carousel — so the grid CSS is overridden. Clean but slightly confusing in source.
- **Pricing card is not on Leistungen** — it's only on `auto/index.html`. A user landing on `auto/leistungen.html` does not see the "kostenlose Erstberatung" hook.
- **Bau modals on the home page** are great, but they all end with the **same boilerplate paragraph** ("Hinweis: Für ein detailliertes Angebot...") — pasted 4× verbatim. A good copy reads "Skizzieren Sie Ihr Projekt — wir kalkulieren in 24h." once, in different words.
- **Auto Counter eyebrows** (Profi-Qualität, Transparenz) duplicate the meaning ("100% Transparenz", "100% Profi-Qualität"). Two cells of "100%" in a 4-cell row look like filler.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 4.1 | Reduce Auto "2000+" to a more credible "150+" or "300+"; align Bau wording | **P1** | 5 min |
| 4.2 | Replace "100% Profi-Qualität" + "100% Transparenz" with measurable counters (24h response, 4.9★, etc.) | **P1** | 10 min |
| 4.3 | Add a "Kostenlose Erstberatung" hook section on `bau/index.html` for parity | **P2** | 30 min |
| 4.4 | De-duplicate the Bau modal boilerplate — vary the copy or extract to one shared note | **P3** | 30 min |
| 4.5 | Surface the "kostenlose Erstberatung" on `auto/leistungen.html` too | **P2** | 20 min |

---

## 5 — Leistungen pages

**Score: 3.5 / 5**

### Findings

- **Auto Leistungen** has a single category "Ankauf und Verkauf" with 6 items (Kaufberatung, Ankaufsbegleitung, Wertermittlung, Verkaufsberatung, Persönliche Beratung, Mehrsprachige Begleitung). Clean, focused. Fully scoped to advisory — no STO / no inspection license required. Smart legal hygiene.
- **Bau Leistungen** has 4 categories: Fliesenarbeiten (4 items), Bodenverlegung (2 items), Naturstein & Terrassen (2 items), Montage & Feinarbeiten (3 items). Each item opens a modal explaining further. Total 11 service items across 4 modals.

### Issues

- **Bau hero promises "Umzugsservice" + meta description mentions "Umzug, Möbelmontage" — but Leistungen has NO Umzug, NO Möbelmontage**. The contact form's `topic` select even has an option `<option value="montage">Möbelmontage</option>` referencing a service that isn't listed. **Promise/delivery gap.** Either add a "Umzug & Möbelmontage" category or remove all mentions.
- **Auto leistungen page is short**: only 6 cards, 1 category. The page hero says "Beratung beim Autokauf und Autoverkauf" — accurate. But the page content density is thin compared to Bau Leistungen. Consider expanding each card's body, or grouping the 6 into 2 categories ("Beim Kauf" / "Beim Verkauf") for visual rhythm.
- **`auto/leistungen.html` page-hero h1** uses i18n key `auto-services-title` which is "Unsere Leistungen" in `de.json` — the title in HTML override says "Beratung beim Autokauf und Autoverkauf" but i18n will replace at runtime with "Unsere Leistungen". After language load, the H1 collapses to a generic "Unsere Leistungen", losing keyword strength. The same key is also used on `auto/index.html` services-teaser. **Same key used in two places with different intended meanings** — i18n key collision.
- **Bau Leistungen page-hero h1** has DE hardcoded "Hochwertiger Innenausbau" with `data-i18n="bau-services-title"` — but the JSON likely has only `de`. EN/UK/RU users will get either DE fallback or nothing.
- **Bau Leistungen breadcrumb** is non-i18n hardcoded "Startseite › Leistungen". Not localized.
- **Bau Leistungen page-hero `<p>` is not i18n'd at all** (line 265 — no `data-i18n` attribute).

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 5.1 | Resolve Umzug/Möbelmontage gap: either add a "Umzug & Möbelmontage" category to Bau Leistungen with proper modal, OR remove from hero/meta/form-select | **P0** | 1–2 h |
| 5.2 | Split the i18n key `auto-services-title` into `auto-services-page-title` (Leistungen H1) and `auto-services-section-title` (homepage section H2) | **P1** | 30 min |
| 5.3 | Add `data-i18n` to all Bau hero/breadcrumb/copy and create the Bau translation set in `locales/{en,uk,ru}.json` | **P0** | 3–4 h |

---

## 6 — Kontakt pages

**Score: 4 / 5**

### Findings

- Two-column layout (`1fr 1.4fr`): left = direct contact methods (Telefon / WhatsApp / E-Mail / Standort + embedded Google Map iframe with `loading="lazy"`), right = booking form card.
- Form on Auto: 4 form-rows = first/last name, email/phone, contactPref/topic, prefDate/prefTime, plus textarea, plus 2 checkboxes (GDPR required, Newsletter optional with 10% Rabatt incentive), plus submit button.
- Honeypot field `<input name="website">` hidden offscreen. Anti-spam fillTime captured. Strong.
- Required fields use a `.required` CSS class that adds a red asterisk via `::after { content: ' *'; color: #ef4444 }`. Decoupled from i18n textContent — clean implementation.
- `togglePhoneReq()` on contactPref change adds `.required` to phone label when WhatsApp/Anruf selected. Smart conditional logic.
- Form-validate.js uses `novalidate`, custom German error messages, shake animation, scroll-to-first-invalid. Good UX.
- FAQ section at the bottom (5 questions on Auto, 4 on Bau).

### Issues

- **Form `<button type="submit" class="form-submit btn-primary-auto">` has inline color `#fff` background `var(--color-auto-primary)` AND the CSS class `.form-submit:hover { background: #c1121f }`** — when hovered, button turns DARK RED on a steel-blue page. Looks like a bug/flash.
- **Auto form heading colors** mix red and blue throughout the styles block: `.contact-method-icon` uses red `rgba(230,57,70,0.1)` background but the icon `color` is `var(--color-auto-primary)` (blue). So you get red-tinted box with blue icon inside. Color clash.
- **Email is `info@Oleksandr Halushkae.de`** (legacy domain). For brand-consistent post-rebrand site, that domain should likely be `info@oleksandrhalushka.de` or a kept-as-legacy with explicit decision. Confirm with owner.
- **Google Map iframe URL uses `pb=` parameters that look unfinished** (`!1d2638.4!2d12.0432!3d48.9338` followed by truncated `!4v1234567890`) — the `4v` timestamp value `1234567890` is obviously a placeholder. Map likely loads but Google occasionally rewrites/refuses such URLs. Re-grab a real share URL from Google Maps.
- **The "Standort" pin is `Industriestraße 22, 93077 Bad Abbach`** but the **Impressum** says `Musterstraße 123, 80331 München`. **Two different addresses on the same site.** Whichever is real, the other is wrong, and the placeholder must go (legal requirement § 5 TMG).
- **Bau Kontakt form labels are NOT i18n'd** (only 6 `data-i18n` keys total on the page). EN/UK/RU users see all field labels in German.
- **Newsletter incentive copy** on Auto: "Ja, ich möchte mich für den Newsletter anmelden und 10% Rabatt auf meine nächste **kostenpflichtige Beratung** erhalten". The visible-pricing card on the index says "Online-Beratung kostenlos". So newsletter offers 10% off something the visitor was just told is free. The wording is technically OK ("kostenpflichtige Beratung" = "paid consultation, the next one") but a casual reader feels mismatch. Consider "10% Rabatt auf eine zukünftige kostenpflichtige Leistung" or drop the carrot.
- **GDPR checkbox text on Auto** is in plain DE without i18n: "Ich stimme zu, dass meine Daten gemäß der Datenschutzerklärung verarbeitet werden, um meine Anfrage zu beantworten. *". A non-DE-speaking user is asked to consent in a language they may not understand. **Compliance risk.**
- **Auto kontakt-info "WhatsApp" link**: `https://wa.me/4916093409671` — looks fine. Phone is `tel:+4916093409671`. Same number. Good.
- **No anti-spam reCAPTCHA / Turnstile** beyond honeypot + fillTime. The GAS endpoint is publicly known once anyone inspects DevTools — a determined botter can hit it. The fillTime check (3s server-side) is light. Probably fine for low-volume Bayern leads, but worth knowing.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 6.1 | Fix submit-button hover color (`#c1121f` → `var(--color-auto-primary-hover)` = `#2d68bf`) | **P0** | 2 min |
| 6.2 | Reconcile addresses: confirm Industriestr. 22, Bad Abbach is real → update Impressum; remove "Musterstraße 123" placeholder | **P0** (legal) | 15 min |
| 6.3 | i18n all labels/options on `bau/kontakt.html`; add EN/UK/RU keys for form fields | **P0** | 4–6 h |
| 6.4 | i18n the GDPR consent checkbox text on both forms (use `data-i18n-html` since it has anchor) | **P0** (GDPR) | 30 min |
| 6.5 | Update Google Maps iframe URL from a fresh "Embed map" share | **P1** | 5 min |
| 6.6 | Decide email: `info@Oleksandr Halushkae.de` legacy vs. `info@halushka.de`; document the choice in `docs/` | **P1** | 5 min |
| 6.7 | Consider Cloudflare Turnstile (free, GDPR-friendly) on form | **P2** | 1 h |

---

## 7 — Über uns / About

**Score: 3.5 / 5**

### Findings

- Auto Über-uns: page-hero ("Beratung, der man vertrauen kann") → about-intro (image left, text right with eyebrow + h2 "Gegründet aus Leidenschaft für Fahrzeuge 🇺🇦" + 3 paragraphs + CTA) → values-section (4 cards: Transparenz, Qualität, Verlässlichkeit, Menschlichkeit) → timeline (4 milestones) → footer.
- Bau Über-uns: similar structure but mirrored (text left, image right). Values cards: Perfektion, Kommunikation, Sauberkeit, Verlässlichkeit. Timeline: 4 milestones.
- Tone is honest and a bit warm. Use of 🇺🇦 emoji in headings signals Ukrainian heritage — appropriate for the niche audience but mildly polarizing for German visitors. Defensible choice for the target community.

### Issues

- **`bau/uber-uns.html` — broken HTML structure**: `<section class="timeline-section">` opens at line 363 and is **never closed**. The footer is nested inside the timeline section. Browsers tolerate it but: lighthouse, screen readers, and any future CSS tweak that targets `.timeline-section > *` will break unpredictably. **P1 fix.**
- **Timeline content is generic** ("Gründung in Bayern", "Erste eigene Räume", "Erweiterung um Innenausbau", "Heute: 2000+ zufriedene Kunden"). No years, no specific event. Reads like a placeholder. The "2000+" claim repeats here.
- **Bau Über-uns timeline-4 says "Oleksandr Halushka — eine Marke, zwei Welten"** — this phrasing announces the rebrand to the visitor. Not necessarily bad but unusual to brag about renaming.
- **Auto About — image alt** is `"Beratungsteam Oleksandr Halushka"` but the image is `auto_hero_v2.png` (the same hero photo reused). For a "team" alt text, an actual team photo would be far stronger. Note: the file is described as a hero image.
- **Bau About — image alt** is `"Oleksandr Halushka · Innenausbau Team"` for `bau_hero.png` — same reuse issue.
- **Values cards on Auto use red `#e63946` for icon color (`.value-card i`)** — the same theme split-brain. Should be steel-blue.
- **Bau Über-uns has only 6 `data-i18n` attributes** — entire about story (paragraphs) is in DE only.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 7.1 | Add `</section>` to close `bau/uber-uns.html` timeline-section before footer | **P1** | 1 min |
| 7.2 | Replace timeline placeholders with real events + years (e.g. "2018 — Erste Aufträge in Regensburg", "2022 — Spezialisierung auf Großformate") | **P1** | 30 min |
| 7.3 | Replace reused hero PNG with an actual team photo or workshop photo (when available) | **P2** | depends on owner |
| 7.4 | Replace inline `#e63946` accents with `var(--color-auto-accent)` | **P0** (with §3) | rolled into §3.2 |
| 7.5 | i18n the entire about story on Bau side | **P0** (with §5.3) | rolled in |

---

## 8 — Footer

**Score: 2.5 / 5**

### Findings

- Footer on each page: copyright "© 2026 Oleksandr Halushka · Alle Rechte vorbehalten", social icons (IG/FB/LinkedIn — vary per page), back-to-main link, Impressum, Datenschutz.
- Footer is repeated **inline** on every page rather than a shared component.

### Issues

- **Social links inconsistency**:
  - `auto/index.html` footer: IG + FB + LinkedIn (`Oleksandr Halushkae.auto`)
  - `auto/leistungen.html` + `auto/uber-uns.html`: **only IG** (FB / LinkedIn missing on leistungen, FB only — no LinkedIn — on uber-uns)
  - `auto/kontakt.html`: IG + FB + LinkedIn
  - `bau/leistungen.html`: only IG
  - `bau/uber-uns.html`: only IG
  - `bau/kontakt.html`: IG + FB + LinkedIn
  - `bau/index.html`: IG + FB + LinkedIn
  
  Inconsistent footer per page. A user clicking "FB" on home and then visiting Leistungen sees the icon disappear.
- **Facebook + LinkedIn URLs are `https://www.facebook.com/` and `https://www.linkedin.com/` — root URLs with no profile**. Clicking takes the user to the platform homepage. Either link to a real profile or remove the icons entirely. **Empty / "dead" social links damage trust.**
- **Instagram handles `Oleksandr Halushkae.auto` and `Oleksandr Halushkae.innenausbau`** — legacy brand handles. For a 2026 site that has been rebranded to Oleksandr Halushka, having IG handles still in the old brand confuses the user about which is the "real" identity.
- **Copyright year is 2026** (correct for current date 2026-05-04).
- **Footer NOT i18n'd** — "Hauptseite", "Impressum", "Datenschutz", "Alle Rechte vorbehalten" are mostly DE hardcoded (some have data-i18n on the copy span, but "Hauptseite" / labels are not).

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 8.1 | Standardize footer across all 9 pages (single template) — same set of social links everywhere | **P1** | 1 h |
| 8.2 | Either link Facebook/LinkedIn to real profiles, or remove the icons | **P0** (trust) | 5 min |
| 8.3 | Confirm IG handles `Oleksandr Halushkae.auto` / `Oleksandr Halushkae.innenausbau` are intended; if rebranded, update IG bio to reference Oleksandr Halushka | **P1** | depends on owner |
| 8.4 | Extract footer to a JS-injected component (or PHP/SSR if migrating) so future edits propagate | **P2** | 2 h |
| 8.5 | i18n footer link labels | **P1** | 30 min |

---

## 9 — Performance signals

**Score: 2.5 / 5**

### Findings

- **Asset weights** (rough measurements):
  - `auto-bg.jpg` 305 KB · `bau-bg.jpg` 203 KB (split landing)
  - `auto_hero.png` 608 KB · `auto_hero_v2.png` 571 KB · `bau_hero.png` 670 KB
  - `auto-leistungen-hero.png` 660 KB · `bau-leistungen-hero.png` 677 KB
  - `auto-uber-uns-hero.png` 665 KB · `auto-uber-uns-hero-v3.png` 727 KB · `bau-uber-uns-hero.png` 730 KB
  - `auto-kontakt-hero.png` 322 KB · `bau-kontakt-hero.png` 686 KB
  - **Total page-hero weight per branch path**: ~2 MB on first-paint chain just for hero PNGs.
- **Inline `<style>` blocks duplicated per page**: each of 8 pages has 200–400 lines of inline CSS that is *not* shared. Same `.page-hero`, `.cta-band`, `.section-head`, `.contact-form-card`, `.faq-section` etc. defined repeatedly. ≈ ~30–50 KB of CSS shipped 8 times instead of once.
- **External CDN scripts/fonts**:
  - Google Fonts (Space Grotesk + DM Sans — the DM Sans request is huge w/ italic + opsz axis).
  - Font Awesome 6.5.0 (~80 KB css + woff)
  - AOS 2.3.4 (~14 KB)
- **Lazy loading**: only the Google Maps iframe has `loading="lazy"`. Hero / image content has none. The about-section image (`auto_hero_v2.png`, 571 KB) is below-the-fold but loads eagerly.
- **No `preload` for fonts**, no `font-display: swap` declared (Google Fonts URL has `&display=swap` — OK for Google's hosted version).

### Issues

- **2 MB of PNG per page is a Lighthouse failure**. Mobile 4G LCP will be 4–6s+. Bayern has good LTE generally but rural / slow connections will struggle.
- **Inline-CSS-per-page duplication** prevents browser cache efficiency. Each page navigation re-downloads ~30 KB of identical CSS.
- **`cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css`** — uses *all* Font Awesome icons. The site uses ~30 distinct icons. Could subset or self-host. Each load is ~80 KB CSS + 200+ KB woff2 if all variants pulled.
- **AOS animations**: each `data-aos` triggers JS-controlled fade-in. With dozens of AOS elements per page and 650 ms duration, scroll feels janky on mid-tier mobile. Consider replacing with native `@scroll-driven-animations` or removing for blocks below the fold.
- **CSS responsive duplication** (see §2.1) — 200+ lines redundant in `global.css`.

### Fix recommendations

| # | Fix | Priority | Effort | Impact |
|---|-----|----------|--------|--------|
| 9.1 | Convert all hero PNGs → WebP via `<picture>`. Target ~75% size reduction | **P0** | 2 h | -1.5 MB per page |
| 9.2 | Extract repeated inline `<style>` blocks into a shared `styles/page-hero.css`, `styles/contact.css`, etc. | **P1** | 3 h | -25 KB per page |
| 9.3 | Self-host Font Awesome subset (only used icons) via SVG sprite | **P2** | 4 h | -200 KB |
| 9.4 | Add `loading="lazy"` to non-hero `<img>` and to `.about-intro img` background contexts | **P1** | 15 min | -500 KB defer |
| 9.5 | Add `<link rel="preload" as="image" href="hero.webp" fetchpriority="high">` after WebP conversion | **P2** | 10 min | LCP -200 ms |
| 9.6 | De-dupe `global.css` responsive blocks (§2.1) | **P1** | 15 min | -10 KB |
| 9.7 | Consider replacing AOS with one CSS `@keyframes` + IntersectionObserver-lite (~1 KB) | **P3** | 1 h | -14 KB JS |

---

## 10 — Accessibility (a11y)

**Score: 2.5 / 5**

### Findings

- HTML lang attribute is set per page (`<html lang="de">`) and i18n.js updates `documentElement.lang` on language change. Good.
- Most images have `alt` attributes. Hero / about images alt text mentions brand name ("Oleksandr Halushka", "Beratungsteam"). Acceptable but generic.
- Burger menu has no `aria-expanded` / `aria-controls`.
- Form fields have `<label for="...">` linked correctly.
- The split-screen sides have `role="link"` + `aria-label` (good for screen readers).

### Issues

- **No `<main>` landmark** on `index.html`, `auto/index.html`, `bau/index.html`, `auto/uber-uns.html`, `bau/uber-uns.html`, `auto/kontakt.html`, `bau/kontakt.html`. Only `auto/leistungen.html` and `bau/leistungen.html` use `<main>`. Screen readers cannot jump to "main content".
- **Burger menu** missing `aria-expanded="false"` and `aria-controls="headerNav"`.
- **Theme switcher pills** — `<button class="switch-btn">Auto</button>` has no `aria-label`, no `aria-pressed` toggle state.
- **Lang switcher** — buttons have an `aria-label="Sprache wechseln zu DE"` (good!) but the parent container has no `role="group"` or label.
- **Color contrast** — Auto theme uses `rgba(255,255,255,0.45)` and `0.42` for body text on `#161616`. That's roughly contrast 5.2:1 — passes WCAG AA. Borderline. `rgba(255,255,255,0.35)` and `0.3` text used for footer copyright: ~3.8:1 — **fails** AA for body text (AA requires 4.5:1 for body, 3:1 for large text). Many "muted" texts on Auto fall close to or below the line.
- **Bau theme** uses `#64748b` (gray-500) and `#94a3b8` (gray-400) on white: ~7:1 and ~4.2:1 respectively — gray-400 borderline AA fail for body.
- **Focus styles**: form inputs change `border-color` to primary on `:focus`. Buttons rely on default browser outline. Better: explicit `:focus-visible` styling.
- **Skip-to-content link**: missing entirely.
- **Cookie banner**: `<button>` elements have no `aria-label`; `🍪` emoji as decoration is OK because text is descriptive.
- **Iframe** (Google Maps) has `title` attribute (good) but `referrerpolicy="no-referrer-when-downgrade"` — fine.
- **`role="link"` on `<section>`** (split-side) — non-standard; better to use `<a>` wrapping the section or `<button>` with click handler. ARIA role link without `tabindex="0"` is inaccessible to keyboard users — pressing Tab will not focus it.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 10.1 | Add `<main id="main">…</main>` wrapper around content sections of every page | **P1** | 1 h |
| 10.2 | Add `aria-expanded` + `aria-controls` to burger button; toggle via JS | **P1** | 15 min |
| 10.3 | Add `aria-pressed` + `aria-label="Bereich Auto auswählen"` etc. to theme switcher buttons | **P1** | 10 min |
| 10.4 | Make split-side keyboard-accessible: change `<section role="link">` → `<a class="split-side">` OR add `tabindex="0"` + keypress handler | **P1** | 30 min |
| 10.5 | Bump muted-text colors so all body text is ≥ 4.5:1 (use `#475569` instead of `#94a3b8` for body on white) | **P1** | 30 min |
| 10.6 | Add `:focus-visible` outlines to all interactive elements | **P2** | 30 min |
| 10.7 | Add skip-to-main link | **P2** | 10 min |

---

## 11 — SEO basics

**Score: 1.5 / 5** (this is the weakest area)

### Findings

- Each page has a unique `<title>` and `<meta name="description">` — good.
- `<html lang="de">` set; i18n.js updates dynamically.

### Issues

- **No `<link rel="canonical">`** on any page. Crawlers seeing both `/auto/index.html` and possibly URL variants (with/without trailing slash, with/without `index.html`) will see duplicate content.
- **No Open Graph tags** (`og:title`, `og:description`, `og:image`, `og:type`, `og:url`). Social shares (WhatsApp / Facebook / LinkedIn / Telegram) will show URL only, no preview card.
- **No Twitter Card** (`twitter:card`, `twitter:image`).
- **No `hreflang` tags** despite 4-language site. Google can't surface UK/RU/EN versions to relevant searchers. Each language is invisible to non-DE Google.
- **No `sitemap.xml`**, no `robots.txt`. Google can crawl but the explicit signal is missing.
- **No JSON-LD / structured data** — no `LocalBusiness`, no `Service`, no `BreadcrumbList`, no `FAQPage` (despite having FAQs!), no `Person` for Oleksandr Halushka. The site forfeits rich-results visibility.
- **Title structure**: "Beratung beim Autokauf und Autoverkauf | Oleksandr Halushka" — 56 chars, OK. "Innenausbau | Oleksandr Halushka" — 32 chars, short. "Über uns | Oleksandr Halushka · KFZ-Beratung" — 47 chars, OK.
- **Meta description on `index.html`** is 130 chars — within 150–160 sweet spot. Good.
- **Meta description on `bau/index.html`**: 110 chars. OK.
- **Two pages share the same `<title>`**: `auto/index.html` and `auto/leistungen.html` both have "Beratung beim Autokauf und Autoverkauf | Oleksandr Halushka". Same H1 too. **Duplicate title — Google will pick one and demote the other**. Should be different (e.g., "Leistungen — Beratung beim Autokauf | Oleksandr Halushka").
- **No address microformat** on Kontakt pages — schema.org `PostalAddress` would help local SEO substantially.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 11.1 | Add unique `<link rel="canonical">` to every page | **P0** | 30 min |
| 11.2 | Add OG + Twitter card meta tags (one OG image per branch is fine) | **P0** | 1 h |
| 11.3 | Add hreflang link tags for the 4 languages | **P0** | 1 h |
| 11.4 | Add `JSON-LD LocalBusiness` schema on all kontakt + index pages with phone, address, openingHours | **P0** | 1 h |
| 11.5 | Add `JSON-LD FAQPage` schema on kontakt pages (already have the Q&A content) | **P1** | 30 min |
| 11.6 | Add `JSON-LD BreadcrumbList` on inner pages | **P2** | 30 min |
| 11.7 | Generate `sitemap.xml` (8 main pages × 4 langs = 32 URLs) and `robots.txt` | **P0** | 30 min |
| 11.8 | Differentiate `<title>` on `auto/index.html` vs `auto/leistungen.html` | **P1** | 5 min |

---

## 12 — Mobile responsiveness

**Score: 3.5 / 5**

### Findings

- 7 breakpoints declared in `global.css`: 1440px+, ≤1240px, ≤1024px, ≤768px, ≤480px, ≤360px, plus `(hover:none) and (pointer:coarse)`. Comprehensive intent.
- Hero `clamp()` font-size scales fluidly.
- Mobile navigation: burger toggles a fullscreen overlay.
- Touch breakpoint enforces `min-height: 48px` on `.btn`, `min-height: 56px` on `.header-nav a`. Good thumb targets.
- Counter-band collapses to single column on ≤480px. Pricing-card grid changes to 2-col then 1-col on ≤360px.

### Issues

- **Duplicated responsive blocks** (§2.1) — second occurrence partially overrides the first. Effective behavior is the LAST declaration wins, but 200 lines of dead CSS shipped. Risk of subtle conflicts if anyone edits one half.
- **`#langSwitcher { display: none }` on ≤480px** — language can't be changed on phones. Bad for UK/RU users who often arrive on phones.
- **Header height 76px (desktop) → 64px (≤768px) → 56px (≤480px) → 52px (≤360px)** — but the second responsive duplicate sets it to **58px at ≤480px**. Inconsistent. The duplicated 58px overrides the 56px because the second definition is later in the file. The single `--var` for header-height pattern would be cleaner.
- **Hero `min-height: 100svh`** at ≤480px is a clever choice (avoids iOS Safari URL-bar resize jumps).
- **Burger menu icon padding for tap target** is implemented (`padding: 12px 10px; margin: -12px -10px`) — clever invisible tap-area expansion.
- **Form `.form-row` flex column** at ≤768px — but the `form-row` is `display: grid` not flex, so `flex-direction: column` does nothing. Should be `grid-template-columns: 1fr`. **Bug**: the rule has no effect; on mobile the two-column form layout does not collapse via this rule. Saved by the `1fr` rule at lower breakpoint at ≤480 / ≤900.
- **Page-hero `padding: 160px 8% 80px`** on Leistungen / Kontakt — at 768px the override drops to `120px 6% 60px`. Hero is heavy on small phones.

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 12.1 | De-duplicate responsive blocks in `global.css` (rolled up with §2.1) | **P1** | 15 min |
| 12.2 | Fix `.form-row { flex-direction: column }` → `grid-template-columns: 1fr` (it's a grid) | **P1** | 5 min |
| 12.3 | Re-show `#langSwitcher` on phones (rolled up with §2.3) | **P1** | done above |
| 12.4 | Reconcile header-height tokens — define `--header-height` once and reuse | **P3** | 30 min |

---

## 13 — Brand consistency post-rebrand

**Score: 2.5 / 5**

### Findings

- Wordmark "OLEKSANDR HALUSHKA" appears on every page header. Bold + thin tracking. ~17 chars.
- Footer copyright says "Oleksandr Halushka" everywhere.

### Issues

- **Legacy brand traces remaining** (verified via grep):
  - `js/components/smart-header.js` — `bannerId = 'Oleksandr Halushkae-cookie-banner'`, `storageKey = 'Oleksandr Halushkae_cookie_consent'`.
  - `legal/impressum.html` — email `kontakt@Oleksandr Halushkae.de`.
  - All kontakt pages — `mailto:info@Oleksandr Halushkae.de`.
  - All page footers — `instagram.com/Oleksandr Halushkae.auto/`, `instagram.com/Oleksandr Halushkae.innenausbau/`.
  - The split-screen badge "AG" — old Oleksandr Halushka initial.
  - `styles/global.css` line 3 comment: `/* Global Design System — AlexGroup */`.
  
  Confirm with owner: are `Oleksandr Halushkae.de` domain and `@Oleksandr Halushkae` IG handles intentional legacy keepers, or pending update?
- **Logo wordmark "OLEKSANDR HALUSHKA" is wider than "Oleksandr Halushka"**. At 1rem font-size 1.5px tracking, that's ~50% more horizontal space. Header layout (nav + theme switch + lang switch + burger) was sized for the shorter wordmark. On 1024–1280px viewports the wordmark + nav + controls likely compete and may wrap or truncate (no measured visual confirmation without a render).
- **Tone-of-voice inconsistency**: the Auto pages mostly say "Wir begleiten Sie", "unabhängig, ehrlich". The Bau pages say "Wir realisieren Ihr Projekt", "Qualität die man sieht". Both are good but the *format* differs — Auto is advisory & ich-aware; Bau is action-oriented & quality-claim. Combined under one brand they should share a voice. Currently they read like two different copywriters.
- **The Über-uns "Gegründet aus Leidenschaft für Fahrzeuge 🇺🇦"** statement uses 🇺🇦 emoji as accent. The Bau About uses 🇺🇦 too. Consistent. But branding for a Bayern business with strong Ukrainian heritage is ambivalent — some German visitors may read this positively (community signal), others may bias against. Strategic call for the owner.
- **Title-case inconsistency**: "Über uns" (correct DE), "Über Uns" (would be wrong) — site uses correct lowercase. Good.
- **The Auto theme tokens declare "V4 Auto Theme: Midnight Steel + Ice Blue Metallic"** but inline page styles use the V3 red palette. Brand-system is split between the documented tokens and the actual paint. **Most visible brand inconsistency.**

### Fix recommendations

| # | Fix | Priority | Effort |
|---|-----|----------|--------|
| 13.1 | Replace "AG" splash badge with "OH" or wordmark monogram (rolled with §1.1) | **P1** | done above |
| 13.2 | Audit all inline `<style>` `#e63946` / `#c1121f` references — replace with `var(--color-auto-primary)` / `var(--color-auto-accent)` | **P0** | 2–3 h |
| 13.3 | Update `smart-header.js` brand strings (`Oleksandr Halushkae-cookie-banner` → `oh-cookie-banner`, etc.) | **P3** | 5 min |
| 13.4 | Update `global.css` comment header from "AlexGroup" → "Oleksandr Halushka" | **P3** | 1 min |
| 13.5 | Document an explicit "voice & tone guide" as `docs/brand-voice.md` and rewrite the most visible page-hero copy to match | **P2** | 4 h |
| 13.6 | Confirm with owner: keep `Oleksandr Halushkae.de` and `@Oleksandr Halushkae` IG handles, or migrate? | **P0** (decision) | 5 min talk |

---

## TOP-10 PRIORITY FIXES (impact × cost-of-not-fixing)

| # | Fix | Section | Priority | Effort | Impact |
|---|-----|---------|----------|--------|--------|
| **1** | **Replace placeholder Impressum data** (Musterstraße 123, DE123456789, fake phone) with real legal info | §6.2 + §13 | **P0 LEGAL** | 15 min | Avoids § 5 TMG Abmahnung. Existential. |
| **2** | **Resolve theme split-brain**: replace all inline `#e63946` red references on Auto pages with `var(--color-auto-primary)` (steel blue) per design tokens | §3.2, §13.2 | **P0 BRAND** | 2–3 h | Fixes the most jarring visual inconsistency on every Auto page |
| **3** | **Fix Bau Umzug/Möbelmontage promise gap** — either add the Leistung block + modal, or remove from hero/meta/form-select | §5.1 | **P0 TRUST** | 1–2 h | Eliminates promise/delivery mismatch that erodes credibility |
| **4** | **Add SEO baseline**: canonical URL, Open Graph, Twitter Cards, hreflang, JSON-LD LocalBusiness + FAQPage, sitemap.xml, robots.txt | §11.1, §11.2, §11.3, §11.4, §11.7 | **P0 DISCOVERY** | 4–5 h | Makes the site findable on Google for non-brand keywords |
| **5** | **i18n the Bau side** + GDPR consent + cookie banner — all currently DE-only. Add EN/UK/RU keys for Bau pages and form labels | §5.3, §6.4, §2.4 | **P0 GDPR + reach** | 6–8 h | Compliance + opens site to UK/RU users |
| **6** | **Fix invalid HTML in `bau/uber-uns.html`** — close the `<section class="timeline-section">` before footer | §7.1 | **P1** | 1 min | One-line fix, prevents future debugging | 
| **7** | **Verify or replace social-link URLs**: bare `facebook.com` / `linkedin.com` are dead. Either link to real profiles or remove icons. Standardize footer across all 9 pages | §8.1, §8.2 | **P1 TRUST** | 1 h | Stops appearing "low effort" |
| **8** | **Convert hero PNGs → WebP via `<picture>`** — drop ~1.5 MB per page | §9.1 | **P0 PERF** | 2 h | LCP improvement of 1–2 s on 4G |
| **9** | **Reconcile counters with reality**: drop "2000+ Kunden" and "100% Profi-Qualität / 100% Transparenz" — replace with credible measurable numbers (or remove) | §4.1, §4.2 | **P1 TRUST** | 15 min | Ten-minute fix that prevents the "this is too much for an Einzelunternehmer" red flag |
| **10** | **De-duplicate `global.css` responsive blocks + extract repeated inline `<style>` to shared CSS files** | §2.1, §9.2 | **P1 PERF + DX** | 3–4 h | -25 KB per page; one place to edit; eliminates drift |

---

## Honourable mentions (not in top-10 but worth fixing soon)

- **Form submit hover bug** — `#c1121f` red on a steel-blue button (§6.1). 2-minute fix.
- **`.form-row` flex-direction on grid** non-effective rule (§12.2). 5-minute fix.
- **Skip-to-content link** missing (§10.7). 10-minute fix.
- **Lang switcher hidden on ≤480px** (§2.3). 10-minute fix.
- **Newsletter "10% Rabatt auf kostenpflichtige Beratung"** wording confusing next to "Erstberatung kostenlos" (§6 issue 7).
- **Two `auto/index.html` and `auto/leistungen.html` share the same `<title>`** (§11.8). 5-minute fix.
- **Burger missing `aria-expanded`** (§10.2). 15-minute fix.
- **AOS scroll-jank on mobile mid-tier** (§9.7). 1-hour replacement with native CSS animations.

---

## Final note

The product has **good bones** — split-screen idea, dual themes, anti-spam form, smart header, Bavarian-flavored testimonials. The friction points are almost entirely about **execution discipline post-rebrand**:

- A theme tokens system was defined (V4 steel blue) but the inline page styles were never migrated.
- Translations were added for Auto but skipped for Bau.
- A rebrand was done via sed-replace but legacy strings (cookie banner ID, IG handles, monogram badge, email domain) survived.
- Placeholder content (Impressum) shipped to production.

A focused **2-day cleanup sprint** addressing items 1–10 above moves this from "concerning if scrutinized" to "trustworthy small-business site". The architectural foundation is solid.
