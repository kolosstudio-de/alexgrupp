# AlexGroup.d Website Design

## 1. Project Overview & Vibe
**Client:** Oleksandr Halushka
**Goal:** Create a premium, bilingual (4 languages) website split into two main business directions: Auto (Service Station) and Bau (Construction/Renovation).
**Architecture:** Pure HTML, CSS, JS stack with a strictly modular structure to ensure extremely easy migration to WordPress in the future. Mobile-first and fully responsive design is mandatory.

## 2. Design Concept (Split-Screen & Contrast)
- **Home Page:** A diagonal or vertical split screen dividing the Auto and Bau sections.
  - **Left (Auto):** Dark theme (graphite/black) with neon accents (blue/red). Brutal, tech-oriented, reliable.
  - **Right (Bau):** Light theme (white/beige/wood) with clean, spacious layouts. Elegant, minimalistic, premium.
- **Interaction:** Dynamic expansion on hover (the hovered side smoothly expands, the other shrinks).

## 3. Navigation & Header
- **Global Header:** Fixed, glassmorphism effect, present across the entire site.
- **Integrated Switcher:** A custom toggle switch in the center: `[ Auto | Bau ]` to quickly jump between the two worlds.
- **Language Selector:** Dropdown for 4 languages: 🇩🇪 (Default), 🇺🇦, 🇷🇺, 🇬🇧.

## 4. Modular File Structure (WordPress-Ready)
To ensure simple translation into a WordPress theme, the project will strictly separate concerns:

**CSS Structure:**
- `styles/global.css`: Base resets, variables, typography, glassmorphism header, global footer.
- `styles/auto.css`: Variables and component styles unique to the dark Auto section.
- `styles/bau.css`: Variables and component styles unique to the light Bau section.

**JS Structure:**
- `js/main.js`: Split-screen hover logic, mobile menu, language switcher functionality.
- `js/i18n.js`: Dictionary logic to swap text between DE, UK, RU, EN. (Later replaced by WP plugins like WPML/Polylang).

**HTML Pages:**
- `index.html`: The main split-screen entry point.
- `/auto/index.html`: Auto home page.
- `/auto/services.html`: Diagnostics, repair, buy/sell help.
- `/auto/about.html`: Team, trust, about.
- `/bau/index.html`: Bau home page.
- `/bau/services.html`: Renovation, exclusive tiles, moving help.
- `/bau/portfolio.html`: Gallery of works.
- `/global/contact.html`: Shared or dynamically themed contact page.
- `/legal/impressum.html` & `/legal/datenschutz.html`: Mandatory German legal pages.

## 5. Mobile Responsiveness & UI/UX
- **Mobile First:** The split screen on mobile will stack vertically (Auto on top, Bau on bottom) instead of side-by-side.
- **Touch-Friendly:** The integrated switcher in the header remains accessible on mobile via an off-canvas menu or fixed bottom bar.
- **Forms & GDPR:** Contact forms will have clear, required checkboxes for DSGVO/Datenschutz consent before submission.

## 6. Next Steps
Move to creating the detailed Implementation Plan, starting with scaffolding the directories, `global.css`, and the `index.html` split-screen shell and header.
