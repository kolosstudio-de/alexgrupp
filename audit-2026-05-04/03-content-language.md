# Content & Language Audit — Oleksandr Halushka Site

**Auditor:** Claude (Opus 4.7) — content/copy/i18n review
**Date:** 2026-05-04
**Scope:** `index.html`, `auto/*.html`, `bau/*.html`, `legal/*.html`, `locales/{de,en,uk,ru}.json`

---

## TL;DR — Top critical findings

1. **§5 UWG risk (Größenirreführung):** German copy is saturated with `wir / unser / uns / Team / Mitarbeiter` in roughly 105+ visible-text positions across 8 HTML pages and `de.json`. As a solo Einzelunternehmer this is legally risky (suggesting fictitious size of business) and ethically misleading. EN/UK/RU mirror the same pattern (`we / our / ми / мы / наша команда` ~115 occurrences). **Severity: CRITICAL — fix before going live or before adding paid traffic.**

2. **`auto/index.html:407–425` — Counter Band lies:** "5+ Jahre Erfahrung", "2000+ Zufriedene Kunden", "100% Profi-Qualität", "100% Transparenz". For a brand-new Einzelunternehmer these are false statements. The "2000+" is repeated again in `auto/uber-uns.html:406` and in all 4 locales. **Severity: CRITICAL — direct UWG/§5a violation risk. Replace immediately.**

3. **BAU section is monolingual (DE only):** `bau/index.html`, `bau/leistungen.html`, `bau/uber-uns.html`, `bau/kontakt.html` contain ~95% of their visible copy WITHOUT `data-i18n` attributes. Only nav + 5 keys (`bau-hero-*`, `bau-services-eyebrow`, `bau-services-title`, `bau-about-eyebrow`, `bau-about-title`, `bau-contact-eyebrow`, `bau-contact-title`) are referenced. Visitors switching to EN/UK/RU still see all the BAU body content in German. **Severity: HIGH** — entire half of the business is unusable for non-German speakers.

4. **Form labels in `bau/kontakt.html` lack i18n:** Vorname, Nachname, E-Mail, Bevorzugter Kontaktweg, all options, GDPR text — none have `data-i18n`. **Severity: HIGH** — booking form is German-only on the bau side.

5. **Brand "Oleksandr Halushka KFZ-Service" reads unnaturally:** post-sed-replace, constructions like `title="Oleksandr Halushka KFZ — Industriestr. 22, Bad Abbach"` (`auto/kontakt.html:482`) and `alt="Oleksandr Halushka · Innenausbau Team"` (`bau/uber-uns.html:328`) read like a person's name attached to a service noun rather than a brand. **Severity: MEDIUM — fix incrementally.**

6. **Email/Instagram still on the old `Oleksandr Halushkae` domain:** `info@Oleksandr Halushkae.de`, `kontakt@Oleksandr Halushkae.de`, `instagram.com/Oleksandr Halushkae.auto`, `instagram.com/Oleksandr Halushkae.innenausbau`. Decision needed: keep brand-domain `Oleksandr Halushkae.de` (cheap, OK as a marketing handle) or migrate everything to `halushka.de`/similar. Currently inconsistent with the visible "Oleksandr Halushka" branding. **Severity: MEDIUM.**

7. **Translation key parity is good (160 keys × 4 locales) but BAU coverage is essentially missing.** All 4 locales translate the same 160 mostly-AUTO keys. There are ~6 `bau-*` keys, vs. ~80+ `auto-*` keys.

8. **Impressum is a placeholder:** `Musterstraße 123, 80331 München`, `+49 (0) 123 456789`, `DE123456789` — fake values still in `legal/impressum.html`. **Severity: CRITICAL** — operating a public site without a valid Impressum is a §5 TMG violation (subject to Abmahnung). Fix before launch.

9. **🇺🇦 flag emojis** in headlines `auto-about-intro-title` and `bau-about-title` — not "wrong" but reads as a politicized statement; consider whether that's the brand positioning intended. Currently both auto & bau "Über uns" titles include the flag, which is on-message for the Ukrainian-diaspora target audience but may surprise non-target Germans on the auto side.

10. **Broken `<title>` tag duplication:** `auto/leistungen.html:7` reuses `auto/index.html`'s title verbatim — both pages share `<title>Beratung beim Autokauf und Autoverkauf | Oleksandr Halushka</title>`. **Severity: MEDIUM** for SEO (duplicate title penalty / crawl confusion).

---

## Section 1 — Grammatical leftovers from sed-replace

### Findings

| File | Line | Current text | Problem |
|---|---|---|---|
| `auto/kontakt.html` | 482 | `title="Oleksandr Halushka KFZ — Industriestr. 22, Bad Abbach"` | "Halushka KFZ" reads as person+service noun; not natural German |
| `bau/uber-uns.html` | 328 | `alt="Oleksandr Halushka · Innenausbau Team"` | "Person · Innenausbau Team" awkward |
| `bau/kontakt.html` | 458 | `title="Oleksandr Halushka · Innenausbau — Industriestr. 22, Bad Abbach"` | Acceptable with the · separator, but verbose |
| `auto/index.html:9` (meta-desc) | — | `Oleksandr Halushka — Ihr zuverlässiger Partner für professionellen KFZ-Service…` | "ein Partner" reads better than "der/Ihr Partner" when the brand IS a person |
| `auto/index.html:489` (`auto-why-eyebrow`) | de.json:46 | `Warum wir` | After dropping plural "wir", needs to become `Warum ich` or `Warum mich` |
| `auto/uber-uns.html:336` (`auto-about-intro-p2`) | de.json:83 | `Als ukrainisches Team mit bayerischem Qualitätsanspruch verbinden wir…` | "Team" presupposes >1 person — solo violation |
| `bau/uber-uns.html:309` | — | `Erfahren Sie mehr über die Vision und das Team von Oleksandr Halushka` | "Vision und das Team" implies multiple; rephrase |
| `bau/uber-uns.html:320` | — | `Unser Team aus erfahrenen Fliesenlegern, Renovierungsspezialisten und Umzugshelfern` | Lists multiple craftspeople — outright fictional team for a solo business |
| `bau/uber-uns.html:393` (timeline) | — | `Oleksandr Halushka — eine Marke, zwei Welten` | Acceptable but slightly grandiose for a solo Einzelunternehmer |
| `auto/index.html:9` and `auto/leistungen.html:9` | meta-desc | "Oleksandr Halushka in Bayern — kompetente Begleitung beim An- und Verkauf…" | OK — slot-in works |

**Severity: MEDIUM.** No outright broken article-noun chimeras (e.g. no `der Oleksandr Halushka KFZ-Service` patterns). The replace was clean. The remaining issues are rhetorical (person-as-service framing).

### Suggested replacements

```diff
- title="Oleksandr Halushka KFZ — Industriestr. 22, Bad Abbach"
+ title="KFZ-Beratung Oleksandr Halushka — Industriestr. 22, Bad Abbach"
```

```diff
- alt="Oleksandr Halushka · Innenausbau Team"
+ alt="Oleksandr Halushka — Innenausbau in Bayern"
```

```diff
- alt="Beratungsteam Oleksandr Halushka"   (auto/uber-uns.html:330)
+ alt="Oleksandr Halushka — KFZ-Beratung Bayern"
```

```diff
- <h4>Heute: 2000+ zufriedene Kunden</h4>
+ <h4>Heute: persönliche Beratung in 4 Sprachen</h4>
```

---

## Section 2 — `wir / unser / uns / Team / Mitarbeiter` in DE (§5 UWG risk)

This is the #1 finding. Below is the **complete inventory of visible-text occurrences** that need migrating from plural to singular for a solo Einzelunternehmer.

### `auto/index.html`

| Line | Current | Replacement |
|---|---|---|
| 343–344 (home-auto-desc, but this is `home-auto-desc` in de.json) | `Professionelle Diagnose, Reparatur und Kaufberatung für Ihr Fahrzeug in Bayern.` | OK — keep as is, no "wir" here |
| 396–397 (`auto-hero-desc`) | `Wir begleiten Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis aus Bayern.` | `Ich begleite Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis aus Bayern.` |
| 430 (`auto-services-eyebrow`) | `Was wir anbieten` | `Mein Angebot` |
| 431 (`auto-services-title`) | `Unsere Leistungen` | `Meine Leistungen` |
| 432 (`auto-services-desc`) | `Persönliche Begleitung beim Kauf und Verkauf Ihres Fahrzeugs.` | OK |
| 438 (`auto-svc1-desc`) | `Wir helfen Ihnen, das passende Fahrzeug zu finden — Marktrecherche, Inseratscheck und ehrliche Einschätzung.` | `Ich helfe Ihnen, das passende Fahrzeug zu finden — Marktrecherche, Inseratscheck und ehrliche Einschätzung.` |
| 443 (`auto-svc2-desc`) | `Wir begleiten Sie zur Besichtigung und sprechen unabhängig über Auffälligkeiten — bevor Sie kaufen.` | `Ich begleite Sie zur Besichtigung und spreche unabhängig über Auffälligkeiten — bevor Sie kaufen.` |
| 467 (`auto-pricing-desc`) | `Schreiben Sie uns kurz, was Sie kaufen oder verkaufen möchten — die erste Einschätzung ist immer kostenlos und unverbindlich.` | `Schreiben Sie mir kurz, was Sie kaufen oder verkaufen möchten — die erste Einschätzung ist immer kostenlos und unverbindlich.` |
| 489 (`auto-why-eyebrow`) | `Warum wir` | `Warum mit mir` |
| 506 (`auto-why3-desc`) | `Wir antworten zügig und liefern eine ehrliche Einschätzung — ohne langes Warten.` | `Ich antworte zügig und liefere eine ehrliche Einschätzung — ohne langes Warten.` |
| 520 (`auto-testi-title`) | `Was unsere Kunden sagen` | `Was meine Kunden sagen` |
| 530 (`auto-cta-desc`) | `Buchen Sie jetzt Ihren Termin oder stellen Sie uns Ihre Frage — wir antworten persönlich.` | `Buchen Sie jetzt Ihren Termin oder stellen Sie mir Ihre Frage — ich antworte persönlich.` |

### `auto/uber-uns.html`

| Line | Current | Replacement |
|---|---|---|
| 9 (meta-desc) | `Lernen Sie das Team von Oleksandr Halushka kennen — erfahrene KFZ-Meister mit Leidenschaft für Fahrzeuge.` | `Lernen Sie Oleksandr Halushka kennen — Ihr persönlicher Ansprechpartner für KFZ-Beratung in Bayern.` |
| 320 (`auto-about-eyebrow`) | `Wer wir sind` | `Wer ich bin` |
| 322 (`auto-about-page-desc`) | `Erfahren Sie mehr über das Team hinter Oleksandr Halushka und was uns antreibt.` | `Erfahren Sie mehr über Oleksandr Halushka und was mich antreibt.` |
| 333 (`auto-about-intro-eyebrow`) | `Unsere Geschichte` | `Meine Geschichte` |
| 334 (`auto-about-intro-title`) | `Gegründet aus Leidenschaft für Fahrzeuge 🇺🇦` | OK — passive construction, no "wir" |
| 335 (`auto-about-intro-p1`) | `Oleksandr Halushka entstand aus dem Wunsch, eine faire, ehrliche und kompetente Beratung … anzubieten.` | OK — no plural |
| 336 (`auto-about-intro-p2`) | `Als ukrainisches Team mit bayerischem Qualitätsanspruch verbinden wir besonderen Fleiß und Leidenschaft mit klaren, ehrlichen Aussagen.` | `Als Ukrainer mit bayerischem Qualitätsanspruch verbinde ich besonderen Fleiß und Leidenschaft mit klaren, ehrlichen Aussagen.` |
| 337 (`auto-about-intro-p3`) | `Heute begleiten wir Kunden aus der ganzen Region und sind bekannt für schnelle Reaktionszeiten, sorgfältige Recherche und persönliche Ansprechbarkeit.` | `Heute begleite ich Kunden aus der ganzen Region und bin bekannt für schnelle Reaktionszeiten, sorgfältige Recherche und persönliche Ansprechbarkeit.` |
| 347 (`auto-about-values-eyebrow`) | `Was uns ausmacht` | `Was mich ausmacht` |
| 348 (`auto-about-values-title`) | `Unsere Werte` | `Meine Werte` |
| 349 (`auto-about-values-desc`) | `Diese Grundsätze leiten unsere Arbeit jeden Tag.` | `Diese Grundsätze leiten meine Arbeit jeden Tag.` |
| 355 (`auto-about-val1-desc`) | `Jede Empfehlung erklären wir nachvollziehbar.` | `Jede Empfehlung erkläre ich nachvollziehbar.` |
| 360 (`auto-about-val2-desc`) | `Wir arbeiten mit aktuellen Marktdaten und nach klaren, dokumentierten Standards.` | `Ich arbeite mit aktuellen Marktdaten und nach klaren, dokumentierten Standards.` |
| 365 (`auto-about-val3-desc`) | `Absprachen werden eingehalten. Termine auch. Ihre Zeit ist uns wichtig.` | `Absprachen werden eingehalten. Termine auch. Ihre Zeit ist mir wichtig.` |
| 379 (`auto-about-timeline-title`) | `Unsere Entwicklung` | `Mein Weg` (or `Meine Entwicklung`) |
| 386 (`auto-about-tl1-desc`) | `Start als Beratungsdienst…` | OK |
| 393 (`auto-about-tl2-desc`) | `Mit wachsendem Vertrauen eröffneten wir unseren ersten festen Standort und erweiterten das Beratungsangebot.` | **Re-write entirely — see Section 8 (Counter Band) and Recommendations.** Suggested: `Mit wachsendem Vertrauen kamen die ersten Stammkunden, die mich heute weiterempfehlen.` |
| 400 (`auto-about-tl3-desc`) | `Als logische Erweiterung kam der Bereich Innenausbau dazu — für den gleichen zuverlässigen Service in einem neuen Handwerk.` | OK — passive |
| 406 (`auto-about-tl4-title`) | `Heute: 2000+ zufriedene Kunden` | **REPLACE — see Section 8** → `Heute: persönlich, mehrsprachig, Bayern-weit` |
| 407 (`auto-about-tl4-desc`) | `Wir wachsen weiter und bleiben dabei das, was wir immer waren: nahbar, zuverlässig, professionell.` | `Ich wachse weiter und bleibe dabei das, was ich immer war: nahbar, zuverlässig, professionell.` |

### `auto/leistungen.html`

| Line | Current | Replacement |
|---|---|---|
| 271 (`auto-services-eyebrow`) | `Unsere Expertise` | `Meine Expertise` |
| 273 (`auto-services-page-desc`) | `Wir begleiten Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis.` | `Ich begleite Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis.` |
| 290 (`auto-leist1-desc`) | `Wir helfen Ihnen, das passende Fahrzeug zu finden …` | `Ich helfe Ihnen, das passende Fahrzeug zu finden …` |
| 297 (`auto-leist2-desc`) | `Wir begleiten Sie zur Besichtigung, schauen das Fahrzeug gemeinsam mit Ihnen an und sprechen ehrlich über Auffälligkeiten — unabhängig vom Verkäufer.` | `Ich begleite Sie zur Besichtigung, schaue das Fahrzeug gemeinsam mit Ihnen an und spreche ehrlich über Auffälligkeiten — unabhängig vom Verkäufer.` |
| 318 (`auto-leist5-desc`) | `Sprechen Sie mit uns telefonisch, per WhatsApp oder per E-Mail …` | `Sprechen Sie mit mir telefonisch, per WhatsApp oder per E-Mail …` |
| 325 (`auto-leist6-desc`) | `Wir betreuen Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für die ukrainische Gemeinschaft in Bayern eine echte Hilfe.` | `Ich betreue Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für die ukrainische Gemeinschaft in Bayern eine echte Hilfe.` |
| 336 (`auto-leist-cta-desc`) | `Kontaktieren Sie uns — wir beraten Sie persönlich und kostenlos.` | `Kontaktieren Sie mich — ich berate Sie persönlich und kostenlos.` |

### `auto/kontakt.html`

| Line | Current | Replacement |
|---|---|---|
| 434 (`auto-contact-eyebrow`) | `Wir sind für Sie da` | `Ich bin für Sie da` |
| 436 (`auto-contact-page-desc`) | `Schreiben Sie uns oder rufen Sie an — wir melden uns mit einer ehrlichen Ersteinschätzung zurück.` | `Schreiben Sie mir oder rufen Sie an — ich melde mich mit einer ehrlichen Ersteinschätzung zurück.` |
| 445 (`auto-kontakt-info-desc`) | `Wählen Sie den für Sie bequemsten Weg. Wir sind meist innerhalb von einer Stunde erreichbar.` | `Wählen Sie den für Sie bequemsten Weg. Ich bin meist innerhalb von einer Stunde erreichbar.` |
| 491 (`auto-form-intro`) | `Füllen Sie das Formular aus — wir melden uns so schnell wie möglich.` | `Füllen Sie das Formular aus — ich melde mich so schnell wie möglich.` |
| 624 (`auto-faq1-a`) | `In der Regel innerhalb von 1–3 Werktagen. Bei dringenden Fällen versuchen wir, Sie noch am selben Tag zu kontaktieren.` | `In der Regel innerhalb von 1–3 Werktagen. Bei dringenden Fällen versuche ich, Sie noch am selben Tag zu kontaktieren.` |
| 632 (`auto-faq3-a`) | `Wir beraten markenübergreifend zu Fahrzeugen aus dem europäischen, asiatischen und amerikanischen Markt.` | `Ich berate markenübergreifend zu Fahrzeugen aus dem europäischen, asiatischen und amerikanischen Markt.` |
| 636 (`auto-faq4-a`) | `Ja. Auf Wunsch fahren wir mit Ihnen zur Besichtigung, schauen das Fahrzeug gemeinsam an und sprechen offen über Auffälligkeiten — bevor Sie eine Kaufentscheidung treffen.` | `Ja. Auf Wunsch fahre ich mit Ihnen zur Besichtigung, schaue das Fahrzeug gemeinsam an und spreche offen über Auffälligkeiten — bevor Sie eine Kaufentscheidung treffen.` |
| 640 (`auto-faq5-a`) | `Wir beraten Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für Neukunden aus der ukrainischen Gemeinschaft in Bayern eine echte Hilfe.` | `Ich berate Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für Neukunden aus der ukrainischen Gemeinschaft in Bayern eine echte Hilfe.` |

### `bau/index.html` (hardcoded — NOT in de.json, fix in HTML directly)

| Line | Current | Replacement |
|---|---|---|
| 452 | `<span class="eyebrow">Was wir anbieten</span>` | `<span class="eyebrow">Mein Angebot</span>` |
| 453 | `<h2>Unsere Leistungen</h2>` | `<h2>Meine Leistungen</h2>` |
| 454 | `<p>Von der Einzelfliese bis zur kompletten Raumsanierung — wir setzen Ihre Vorstellungen um.</p>` | `<p>Von der Einzelfliese bis zur kompletten Raumsanierung — ich setze Ihre Vorstellungen um.</p>` |
| 487 | `<h2>Ihr Vorteil mit uns</h2>` | `<h2>Ihr Vorteil mit mir</h2>` |
| 493 | `<p>Jede Fliese, jede Wand, jede Ecke — wir liefern Ergebnisse, die überzeugen.</p>` | `<p>Jede Fliese, jede Wand, jede Ecke — ich liefere Ergebnisse, die überzeugen.</p>` |
| 498 | `<p>Wir schützen Ihre Einrichtung und hinterlassen besenreine Räume.</p>` | `<p>Ich schütze Ihre Einrichtung und hinterlasse besenreine Räume.</p>` |
| 517 | `<h2>Was unsere Kunden sagen</h2>` | `<h2>Was meine Kunden sagen</h2>` |
| 527 | `<p>Kontaktieren Sie uns für ein kostenloses Angebot — wir antworten persönlich.</p>` | `<p>Kontaktieren Sie mich für ein kostenloses Angebot — ich antworte persönlich.</p>` |
| 539, 565, 611 (modal `<p>`) | `Wir realisieren / Wir verlegen / Wir übernehmen…` | `Ich realisiere / Ich verlege / Ich übernehme…` |
| 549, 572, 595, 619 (modal hint, repeated 4×) | `füllen Sie bitte unser Kontaktformular aus. Wir melden uns umgehend bei Ihnen für eine präzise Kalkulation.` | `füllen Sie bitte mein Kontaktformular aus. Ich melde mich umgehend bei Ihnen für eine präzise Kalkulation.` |

### `bau/uber-uns.html` (hardcoded)

| Line | Current | Replacement |
|---|---|---|
| 9 (meta) | `Lernen Sie das Bau-Team von Oleksandr Halushka kennen — erfahrene Handwerker mit Leidenschaft für Details.` | `Lernen Sie Oleksandr Halushka kennen — Innenausbau aus einer Hand, mit Leidenschaft für Details.` |
| 307 | `<span class="eyebrow" data-i18n="bau-about-eyebrow">Wer wir sind</span>` | `Wer ich bin` (and update i18n value) |
| 309 | `Erfahren Sie mehr über die Vision und das Team von Oleksandr Halushka im Bereich Bau & Innenausbau.` | `Erfahren Sie mehr über Oleksandr Halushka — Innenausbau in Bayern mit Anspruch.` |
| 318–319 | `Der Bau-Bereich von Oleksandr Halushka entstand aus der Überzeugung, dass gute Handwerksarbeit mehr ist als nur Funktionalität — sie soll schön sein, lange halten und Freude bereiten.` | OK (passive — keep) |
| 320–321 | `Unser Team aus erfahrenen Fliesenlegern, Renovierungsspezialisten und Umzugshelfern arbeitet nach einem klaren Grundsatz: Wir behandeln jede Wohnung, als wäre es unsere eigene.` | `Mit Erfahrung in Fliesenarbeit, Renovierung und Umzugshilfe arbeite ich nach einem klaren Grundsatz: Ich behandle jede Wohnung, als wäre es meine eigene.` |
| 323 | `Als ukrainisches Team mit bayerischem Qualitätsanspruch legen wir größten Wert auf Präzision, Zuverlässigkeit und höchste handwerkliche Standards.` | `Als Ukrainer mit bayerischem Qualitätsanspruch lege ich größten Wert auf Präzision, Zuverlässigkeit und höchste handwerkliche Standards.` |
| 335 | `Was uns antreibt` | `Was mich antreibt` |
| 336 | `Unsere Werte` | `Meine Werte` |
| 337 | `Grundsätze, nach denen wir jeden Tag arbeiten.` | `Grundsätze, nach denen ich jeden Tag arbeite.` |
| 343 | `Wir legen Wert auf jede Fliese, jede Fuge, jede gerade Linie — auch wenn es niemand direkt sieht.` | `Ich lege Wert auf jede Fliese, jede Fuge, jede gerade Linie — auch wenn es niemand direkt sieht.` |
| 348 | `Wir informieren Sie über den Fortschritt und sprechen Änderungen immer vorab ab.` | `Ich informiere Sie über den Fortschritt und spreche Änderungen immer vorab ab.` |
| 353 | `Ihre Wohnung bleibt so sauber wie möglich. Schutzmaßnahmen sind für uns selbstverständlich.` | `Ihre Wohnung bleibt so sauber wie möglich. Schutzmaßnahmen sind für mich selbstverständlich.` |
| 358 | `Wir kommen, wenn wir sagen, dass wir kommen. Und wir liefern, was wir versprechen.` | `Ich komme, wenn ich sage, dass ich komme. Und ich liefere, was ich verspreche.` |
| 366 | `Unsere Entwicklung` | `Mein Weg` |
| 380 | `Auf Kundenwunsch übernahmen wir komplette Wohnungsrenovierungen — schlüsselfertig.` | `Auf Kundenwunsch übernehme ich komplette Wohnungsrenovierungen — schlüsselfertig.` |
| 387 | `Logische Erweiterung durch Umzugsservice — für unsere Kunden aus einer Hand.` | `Logische Erweiterung durch Umzugsservice — für meine Kunden aus einer Hand.` |
| 393 | `Oleksandr Halushka — eine Marke, zwei Welten` | OK (or shorten to `Oleksandr Halushka — zwei Welten, ein Anspruch`) |
| 394 | `Zusammenschluss mit KFZ-Service unter dem Dach von Oleksandr Halushka — für umfassenden Service.` | `Zusammenschluss mit KFZ-Beratung unter dem Dach von Oleksandr Halushka — für umfassenden Service.` |

### `bau/leistungen.html` (hardcoded)

| Line | Current | Replacement |
|---|---|---|
| 263 | `Unsere Expertise` | `Meine Expertise` |
| 265 | `Ob Renovierung, Trockenbau oder Akustiklösungen — wir realisieren Ihr Projekt termingerecht.` | `Ob Renovierung, Trockenbau oder Akustiklösungen — ich realisiere Ihr Projekt termingerecht.` |
| 388 | `Kontaktieren Sie uns — kostenlose Beratung und verbindlicher Kostenvoranschlag.` | `Kontaktieren Sie mich — kostenlose Beratung und verbindlicher Kostenvoranschlag.` |
| 399, 425, 471 (modal `<p>`) | `Wir realisieren / Wir verlegen / Wir übernehmen…` | `Ich realisiere / Ich verlege / Ich übernehme…` |
| 409, 432, 455, 479 (4× repeat hint) | `füllen Sie bitte unser Kontaktformular aus. Wir melden uns umgehend bei Ihnen für eine präzise Kalkulation.` | `füllen Sie bitte mein Kontaktformular aus. Ich melde mich umgehend bei Ihnen für eine präzise Kalkulation.` |

### `bau/kontakt.html` (hardcoded)

| Line | Current | Replacement |
|---|---|---|
| 417 (`bau-contact-title`) | `Wir bauen Ihre Vision` | `Ich baue Ihre Vision` |
| 418 | `Beschreiben Sie uns Ihr Bauvorhaben. Wir melden uns umgehend mit einem verbindlichen Angebot.` | `Beschreiben Sie mir Ihr Bauvorhaben. Ich melde mich umgehend mit einem verbindlichen Angebot.` |
| 425 | `Wählen Sie den für Sie bequemsten Weg. Wir antworten innerhalb von einer Stunde.` | `Wählen Sie den für Sie bequemsten Weg. Ich antworte innerhalb von einer Stunde.` |
| 466 | `Beschreiben Sie kurz Ihr Vorhaben — wir erstellen Ihnen ein kostenloses Angebot.` | `Beschreiben Sie kurz Ihr Vorhaben — ich erstelle Ihnen ein kostenloses Angebot.` |
| 595 | `Ja, immer. Kostenvoranschläge sind für uns selbstverständlich und unverbindlich.` | `Ja, immer. Kostenvoranschläge sind für mich selbstverständlich und unverbindlich.` |
| 599 | `Wir arbeiten sowohl mit Festpreisen als auch auf Stundenbasis…` | `Ich arbeite sowohl mit Festpreisen als auch auf Stundenbasis…` |
| 607 | `Ja, wir verlegen Fliesen bis 120×260 cm und haben spezielles Werkzeug dafür.` | `Ja, ich verlege Fliesen bis 120×260 cm und habe spezielles Werkzeug dafür.` |

**Severity: CRITICAL.** This is the biggest single block of work for the audit fix.

---

## Section 3 — `we / our / us / Team` in EN (`locales/en.json`)

Same logic as DE — every `we`/`our`/`us` should become `I`/`my`/`me` for solo Einzelunternehmer authenticity.

| Key | Current EN | Replacement |
|---|---|---|
| `auto-hero-desc` | `We guide you personally through buying and selling — independent, honest and with local Bavarian market knowledge.` | `I guide you personally through buying and selling — independent, honest, with local Bavarian market knowledge.` |
| `auto-services-eyebrow` | `What we offer` | `What I offer` |
| `auto-services-title` | `Our Services` | `My Services` |
| `auto-services-desc` | `Personal guidance for buying and selling your vehicle.` | OK |
| `auto-services-page-desc` | `We guide you personally through buying and selling — independent, honest and with market expertise.` | `I guide you personally through buying and selling — independent, honest, with market expertise.` |
| `auto-svc1-desc` | `We help you find the right vehicle…` | `I help you find the right vehicle…` |
| `auto-svc2-desc` | `We accompany you to the viewing…` | `I accompany you to the viewing…` |
| `auto-pricing-desc` | `Tell us briefly what you want to buy or sell…` | `Tell me briefly what you want to buy or sell…` |
| `auto-why-eyebrow` | `Why us` | `Why me` |
| `auto-why3-desc` | `We answer fast and give you an honest assessment — no long waiting.` | `I answer fast and give you an honest assessment — no long waiting.` |
| `auto-testi-title` | `What Our Customers Say` | `What My Customers Say` |
| `auto-cta-desc` | `Book your appointment now or ask us your question — we reply personally.` | `Book your appointment now or ask me your question — I reply personally.` |
| `auto-leist1-desc` | `We help you find the right vehicle — from market research to listing review.` | `I help you find the right vehicle — from market research to listing review.` |
| `auto-leist2-desc` | `We accompany you to the viewing, look at the car together with you and speak honestly about anything noteworthy — independent of the seller.` | `I accompany you to the viewing, look at the car together with you, and speak honestly about anything noteworthy — independent of the seller.` |
| `auto-leist5-desc` | `Talk to us by phone, WhatsApp or email…` | `Talk to me by phone, WhatsApp or email…` |
| `auto-leist6-desc` | `We support you in German, English, Ukrainian and Russian — especially helpful for the Ukrainian community in Bavaria.` | `I support you in German, English, Ukrainian and Russian — especially helpful for the Ukrainian community in Bavaria.` |
| `auto-leist-cta-desc` | `Get in touch — we'll advise you personally and free of charge.` | `Get in touch — I'll advise you personally and free of charge.` |
| `auto-about-eyebrow` | `Who we are` | `Who I am` |
| `auto-about-page-desc` | `Learn more about the team behind Oleksandr Halushka and what drives us.` | `Learn more about Oleksandr Halushka and what drives me.` |
| `auto-about-intro-eyebrow` | `Our Story` | `My Story` |
| `auto-about-intro-p2` | `As a Ukrainian team with Bavarian quality standards, we combine special diligence and passion with clear, honest assessments. Every customer deserves an understandable evaluation — without jargon and without hidden costs.` | `As a Ukrainian working with Bavarian quality standards, I combine special diligence and passion with clear, honest assessments. Every customer deserves an understandable evaluation — without jargon, without hidden costs.` |
| `auto-about-intro-p3` | `Today we serve customers from the entire region and are known for fast response times, careful research and personal accessibility.` | `Today I serve customers from the entire region and am known for fast response times, careful research, and personal accessibility.` |
| `auto-about-values-eyebrow` | `What defines us` | `What defines me` |
| `auto-about-values-title` | `Our Values` | `My Values` |
| `auto-about-values-desc` | `These principles guide our work every day.` | `These principles guide my work every day.` |
| `auto-about-val1-desc` | `We explain every recommendation in plain language. No step without your explicit consent.` | `I explain every recommendation in plain language. No step without your explicit consent.` |
| `auto-about-val2-desc` | `We work with up-to-date market data and follow clear, documented standards.` | `I work with up-to-date market data and follow clear, documented standards.` |
| `auto-about-val3-desc` | `Agreements are kept. Appointments too. Your time matters to us.` | `Agreements are kept. Appointments too. Your time matters to me.` |
| `auto-about-timeline-title` | `Our Journey` | `My Journey` |
| `auto-about-tl2-desc` | `With growing trust we opened our first permanent location and expanded our advisory offering.` | **rewrite — see Section 8** → `With growing trust, regulars came back and started referring me.` |
| `auto-about-tl4-title` | `Today: 2000+ happy customers` | **REPLACE — see Section 8** → `Today: personal, multilingual, Bavaria-wide` |
| `auto-about-tl4-desc` | `We keep growing while staying what we always were: approachable, reliable, professional.` | `I keep growing while staying what I have always been: approachable, reliable, professional.` |
| `auto-contact-page-desc` | `Write to us or give us a call — we'll come back to you with an honest first assessment.` | `Write to me or give me a call — I'll come back to you with an honest first assessment.` |
| `auto-kontakt-info-desc` | `Choose the channel most convenient for you. We are usually reachable within an hour.` | `Choose the channel most convenient for you. I am usually reachable within an hour.` |
| `auto-form-intro` | `Fill in the form — we'll get back to you as soon as possible.` | `Fill in the form — I'll get back to you as soon as possible.` |
| `auto-faq1-a` | `Usually within 1–3 working days. For urgent cases we try to contact you the same day.` | `Usually within 1–3 working days. For urgent cases I try to contact you the same day.` |
| `auto-faq3-a` | `We advise across all brands — European, Asian and American market vehicles.` | `I advise across all brands — European, Asian and American market vehicles.` |
| `auto-faq4-a` | `Yes. On request we'll join you for the viewing, look at the car together and speak openly about anything noteworthy — before you make a buying decision.` | `Yes. On request I'll join you for the viewing, look at the car together, and speak openly about anything noteworthy — before you make a buying decision.` |
| `auto-faq5-a` | `We advise in German, English, Ukrainian and Russian — especially helpful for the Ukrainian community in Bavaria.` | `I advise in German, English, Ukrainian and Russian — especially helpful for the Ukrainian community in Bavaria.` |

### EN-specific phrasing notes

- `auto-why4-desc` (`No call centre. You speak directly with the person handling your case.`) — already perfect singular framing.
- `auto-faq3-q`, `auto-faq4-q`, `auto-faq5-q` use polite "you" addressing the speaker — also fine because they're the customer's words, not the brand's.

**Severity: CRITICAL — same as DE.**

---

## Section 4 — `ми / наш / нас / команда` (UK) and `мы / наш / нас / команда` (RU)

Slavic-language plurals in business voice are a softer convention than DE/EN — Ukrainian/Russian "ми/мы" is sometimes acceptable as plural-of-modesty (плюрал majestатис). However, given that the brand is `Oleksandr Halushka` (a single named person) and the German source explicitly needs to drop "wir", consistency demands the same migration here. **Recommendation: switch to first-person singular in UK and RU.**

### `locales/uk.json`

| Key | Current UK | Replacement |
|---|---|---|
| `auto-hero-desc` | `Ми супроводжуємо вас особисто при купівлі та продажу — незалежно, чесно і зі знанням ринку Баварії.` | `Я особисто супроводжую вас при купівлі та продажу — незалежно, чесно і зі знанням ринку Баварії.` |
| `auto-services-eyebrow` | `Що ми пропонуємо` | `Що я пропоную` |
| `auto-services-title` | `Наші послуги` | `Мої послуги` |
| `auto-services-page-desc` | `Ми супроводжуємо вас особисто…` | `Я особисто супроводжую вас…` |
| `auto-svc1-desc` | `Допоможемо знайти потрібний автомобіль — аналіз ринку, перевірка оголошень та чесна оцінка.` | `Допоможу знайти потрібний автомобіль — аналіз ринку, перевірка оголошень та чесна оцінка.` |
| `auto-svc2-desc` | `Поїдемо з вами на огляд та чесно обговоримо все, що помітимо — до того, як ви купите.` | `Поїду з вами на огляд та чесно обговорю все, що помічу — до того, як ви купите.` |
| `auto-svc4-desc` | `Поради щодо фотопрезентації, тексту оголошення, цінової стратегії та правильних платформ для продажу.` | OK (no plural) |
| `auto-pricing-desc` | `Напишіть коротко, що ви хочете купити чи продати — перша оцінка завжди безкоштовна та без жодних зобов'язань.` | OK |
| `auto-why-eyebrow` | `Чому ми` | `Чому зі мною` |
| `auto-why-title` | `Ваша перевага з Oleksandr Halushka` | OK |
| `auto-why3-desc` | `Відповідаємо швидко й даємо чесну оцінку…` | `Відповідаю швидко і даю чесну оцінку…` |
| `auto-testi-title` | `Що кажуть наші клієнти` | `Що кажуть мої клієнти` |
| `auto-cta-desc` | `Запишіться на консультацію або поставте запитання — відповідаємо особисто.` | `Запишіться на консультацію або поставте запитання — відповідаю особисто.` |
| `auto-cta-btn` | `Зв'язатися з нами` | `Зв'язатися зі мною` |
| `auto-leist1-desc` | `Допоможемо знайти потрібний автомобіль…` | `Допоможу знайти потрібний автомобіль…` |
| `auto-leist2-desc` | `Поїдемо з вами на огляд, разом подивимось…` | `Поїду з вами на огляд, разом подивимось…` (or `подивимось` → `подивлюсь`) |
| `auto-leist5-desc` | `Зв'яжіться з нами…` | `Зв'яжіться зі мною…` |
| `auto-leist6-desc` | `Працюємо з вами німецькою, англійською…` | `Працюю з вами німецькою, англійською…` |
| `auto-leist-cta-desc` | `Зв'яжіться з нами — ми проконсультуємо вас особисто та безкоштовно.` | `Зв'яжіться зі мною — я проконсультую вас особисто та безкоштовно.` |
| `auto-about-eyebrow` | `Хто ми` | `Хто я` |
| `auto-about-page-desc` | `Дізнайтеся більше про команду Oleksandr Halushka та що нами рухає.` | `Дізнайтеся більше про Oleksandr Halushka та що мене рухає.` |
| `auto-about-intro-eyebrow` | `Наша історія` | `Моя історія` |
| `auto-about-intro-p2` | `Як українська команда з баварськими стандартами якості ми поєднуємо особливу старанність та пристрасть із чіткими, чесними оцінками.` | `Як українець з баварськими стандартами якості я поєдную особливу старанність та пристрасть із чіткими, чесними оцінками.` |
| `auto-about-intro-p3` | `Сьогодні ми супроводжуємо клієнтів по всьому регіону…` | `Сьогодні я супроводжую клієнтів по всьому регіону…` |
| `auto-about-intro-cta` | `Зв'язатися з нами` | `Зв'язатися зі мною` |
| `auto-about-values-eyebrow` | `Що нас визначає` | `Що мене визначає` |
| `auto-about-values-title` | `Наші цінності` | `Мої цінності` |
| `auto-about-values-desc` | `Ці принципи спрямовують нашу роботу щодня.` | `Ці принципи спрямовують мою роботу щодня.` |
| `auto-about-val1-desc` | `Кожну рекомендацію пояснюємо зрозумілою мовою.` | `Кожну рекомендацію пояснюю зрозумілою мовою.` |
| `auto-about-val2-desc` | `Працюємо з актуальними ринковими даними…` | `Працюю з актуальними ринковими даними…` |
| `auto-about-val3-desc` | `Домовленості виконуються. Час зустрічей теж. Ваш час для нас важливий.` | `Домовленості виконуються. Час зустрічей теж. Ваш час для мене важливий.` |
| `auto-about-timeline-title` | `Наш шлях` | `Мій шлях` |
| `auto-about-tl2-desc` | `Із зростанням довіри ми відкрили першу постійну точку та розширили перелік послуг.` | **rewrite — Section 8** |
| `auto-about-tl4-title` | `Сьогодні: 2000+ задоволених клієнтів` | **REPLACE — Section 8** → `Сьогодні: персональний підхід, 4 мови, вся Баварія` |
| `auto-about-tl4-desc` | `Ми зростаємо й залишаємось такими…` | `Я зростаю й залишаюсь таким, яким завжди був: близький, надійний, професійний.` |
| `auto-contact-eyebrow` | `Зв'яжіться з нами` | `Зв'яжіться зі мною` |
| `auto-contact-page-desc` | `Напишіть нам або зателефонуйте — ми повернемося з чесною першою оцінкою.` | `Напишіть мені або зателефонуйте — я повернусь з чесною першою оцінкою.` |
| `auto-kontakt-info-title` | `Прямі канали зв'язку` | OK |
| `auto-kontakt-info-desc` | `Оберіть найзручніший для вас спосіб. Зазвичай ми на зв'язку протягом години.` | `Оберіть найзручніший для вас спосіб. Зазвичай я на зв'язку протягом години.` |
| `auto-form-intro` | `Заповніть форму — ми відповімо якнайшвидше.` | `Заповніть форму — я відповім якнайшвидше.` |
| `auto-faq1-a` | `…У термінових випадках намагаємось зв'язатись у той же день.` | `…У термінових випадках намагаюсь зв'язатись у той же день.` |
| `auto-faq3-a` | `Ми консультуємо з усіх марок…` | `Я консультую з усіх марок…` |
| `auto-faq4-a` | `Так. За потреби супроводжуємо вас на огляд, разом дивимось…` | `Так. За потреби супроводжу вас на огляд, разом подивимось…` |
| `auto-faq5-a` | `Консультуємо німецькою, англійською, українською та російською…` | `Консультую німецькою, англійською, українською та російською…` |

### `locales/ru.json`

| Key | Current RU | Replacement |
|---|---|---|
| `auto-hero-desc` | `Сопровождаем вас лично…` | `Я лично сопровождаю вас…` |
| `auto-services-eyebrow` | `Что мы предлагаем` | `Что я предлагаю` |
| `auto-services-title` | `Наши услуги` | `Мои услуги` |
| `auto-services-page-desc` | `Сопровождаем вас лично…` | `Я лично сопровождаю вас…` |
| `auto-svc1-desc` | `Поможем найти подходящий автомобиль…` | `Помогу найти подходящий автомобиль…` |
| `auto-svc2-desc` | `Поедем с вами на осмотр…` | `Поеду с вами на осмотр…` |
| `auto-pricing-desc` | (no plural) | OK |
| `auto-why-eyebrow` | `Почему мы` | `Почему со мной` |
| `auto-why3-desc` | `Отвечаем оперативно и даём честную оценку…` | `Отвечаю оперативно и даю честную оценку…` |
| `auto-testi-title` | `Что говорят наши клиенты` | `Что говорят мои клиенты` |
| `auto-cta-desc` | `…задайте вопрос — отвечаем лично.` | `…задайте вопрос — отвечаю лично.` |
| `auto-cta-btn` | `Связаться с нами` | `Связаться со мной` |
| `auto-leist1-desc` | `Поможем найти…` | `Помогу найти…` |
| `auto-leist2-desc` | `Поедем с вами на осмотр, вместе посмотрим…` | `Поеду с вами на осмотр, вместе посмотрим…` |
| `auto-leist5-desc` | `Свяжитесь с нами…` | `Свяжитесь со мной…` |
| `auto-leist6-desc` | `Работаем с вами на немецком…` | `Работаю с вами на немецком…` |
| `auto-leist-cta-desc` | `Свяжитесь с нами — мы проконсультируем вас лично и бесплатно.` | `Свяжитесь со мной — я проконсультирую вас лично и бесплатно.` |
| `auto-about-eyebrow` | `Кто мы` | `Кто я` |
| `auto-about-page-desc` | `…о команде Oleksandr Halushka и о том, что нами движет.` | `…об Oleksandr Halushka и о том, что мной движет.` |
| `auto-about-intro-eyebrow` | `Наша история` | `Моя история` |
| `auto-about-intro-p2` | `Как украинская команда с баварскими стандартами качества мы сочетаем…` | `Как украинец с баварскими стандартами качества я сочетаю особое усердие и страсть с чёткими, честными оценками. Каждый клиент заслуживает понятной оценки — без профессионального жаргона и без скрытых расходов.` |
| `auto-about-intro-p3` | `Сегодня мы сопровождаем клиентов…` | `Сегодня я сопровождаю клиентов…` |
| `auto-about-intro-cta` | `Связаться с нами` | `Связаться со мной` |
| `auto-about-values-eyebrow` | `Что нас отличает` | `Что меня отличает` |
| `auto-about-values-title` | `Наши ценности` | `Мои ценности` |
| `auto-about-values-desc` | `Эти принципы направляют нашу работу каждый день.` | `Эти принципы направляют мою работу каждый день.` |
| `auto-about-val1-desc` | `Каждую рекомендацию объясняем понятно…` | `Каждую рекомендацию объясняю понятно…` |
| `auto-about-val2-desc` | `Работаем с актуальными рыночными данными…` | `Работаю с актуальными рыночными данными…` |
| `auto-about-val3-desc` | `Договорённости выполняются. Время встреч тоже. Ваше время для нас важно.` | `Договорённости выполняются. Время встреч тоже. Ваше время для меня важно.` |
| `auto-about-timeline-title` | `Наш путь` | `Мой путь` |
| `auto-about-tl2-desc` | `…мы открыли первое постоянное помещение и расширили список услуг.` | rewrite (see Section 8) |
| `auto-about-tl4-title` | `Сегодня: 2000+ довольных клиентов` | **REPLACE → `Сегодня: личный подход, 4 языка, вся Бавария`** |
| `auto-about-tl4-desc` | `Мы продолжаем расти и остаёмся такими…` | `Я продолжаю расти и остаюсь таким, каким был всегда: близкий, надёжный, профессиональный.` |
| `auto-contact-eyebrow` | `Свяжитесь с нами` | `Свяжитесь со мной` |
| `auto-contact-page-desc` | `Напишите нам или позвоните — вернёмся к вам с честной первой оценкой.` | `Напишите мне или позвоните — вернусь к вам с честной первой оценкой.` |
| `auto-kontakt-info-desc` | `…Обычно мы на связи в течение часа.` | `…Обычно я на связи в течение часа.` |
| `auto-form-intro` | `Заполните форму — мы ответим как можно быстрее.` | `Заполните форму — отвечу как можно быстрее.` |
| `auto-faq1-a` | `…В срочных случаях стараемся связаться в тот же день.` | `…В срочных случаях стараюсь связаться в тот же день.` |
| `auto-faq3-a` | `Мы консультируем по всем маркам…` | `Я консультирую по всем маркам…` |
| `auto-faq4-a` | `Да. По желанию мы поедем с вами…` | `Да. По желанию поеду с вами…` |
| `auto-faq5-a` | `Консультируем на немецком, английском…` | `Консультирую на немецком, английском…` |

**Severity: HIGH** — same legal logic carries to the slavic locales because the German DSGVO/UWG framework applies regardless of the language the user reads.

---

## Section 5 — Tone of voice consistency

### Strengths
- DE tone is **professional, polite (Sie-form), warm**. Good fit for both Bavarian locals and Ukrainian diaspora. Tone of `auto/uber-uns.html` (Werte) is on point: Transparenz, Qualität, Verlässlichkeit, Menschlichkeit — clean.
- EN tone is **slightly less polished** than DE — some translations feel literal:
  - `auto-faq2-a` EN: `…always with a clear quote in advance.` — translation of "nach vorheriger klarer Absprache" sounds literal; native EN would say `…always with a clear estimate up front.`
  - `auto-pricing-card-cta` EN: `Request now →` is brusque vs DE `Jetzt anfragen →` — both OK but EN reads more transactional.
- UK tone is **good and natural** — `Зв'язатися з нами`, `відповідаємо швидко` — close to native register. Once "ми → я" migration done, will be perfect.
- RU tone is **slightly more formal** than UK (`Сопровождаем` vs UK `Супроводжуємо`) but acceptable.

### Weaknesses
- The **🇺🇦 flag emoji** in `auto-about-intro-title` and `bau-about-title` (only on the about page, not header) creates an inconsistent voice — the rest of the site is brand-neutral, this single moment is brand-political. Verdict: defensible (target audience is Ukrainian diaspora) but worth conscious decision. If the auto/Bayern locals are also a primary audience, consider moving the flag to a small "Ukrainian-led, Bavaria-based" trust bar elsewhere.
- The phrase "ukrainisches Team" vs "bayerischer Qualitätsanspruch" appears 2x and is part of brand DNA — keep, but rewrite to "Als Ukrainer mit bayerischem Qualitätsanspruch" once "Team" goes.
- `auto/leistungen.html:325` — `gerade für die ukrainische Gemeinschaft in Bayern eine echte Hilfe.` — same line in `auto-faq5-a` says `gerade für Neukunden aus der ukrainischen Gemeinschaft in Bayern`. Pick one phrasing for consistency.

### Bau vs Auto tone divergence
- AUTO uses red accent + dark theme + crisp brand language (`unabhängig, ehrlich, mit Marktkenntnis`).
- BAU uses amber accent + light theme + craftsmanship language (`Perfektion im Detail, saubere Arbeit`).
- Tones are **deliberately different and that works** — but BAU has zero translations, so the multilingual story breaks the brand promise on the bau side.

**Severity: LOW–MEDIUM** for tone; **HIGH** for the bau/multilingual gap.

---

## Section 6 — Translation quality spot-check (random 15 keys)

| Key | DE | EN | UK | RU | Verdict |
|---|---|---|---|---|---|
| `auto-svc1-title` | `Kaufberatung` | `Purchase Advisory` | `Консультація з купівлі` | `Консультация по покупке` | ✓ all aligned |
| `auto-counter-clients` | `Zufriedene Kunden` | `Happy Clients` | `Задоволених клієнтів` | `Довольных клиентов` | ✓ |
| `auto-counter-quality` | `Profi-Qualität` | `Professional Quality` | `Професійна якість` | `Профессиональное качество` | ✓ |
| `auto-pricing-card-cta` | `Jetzt anfragen →` | `Request now →` | `Замовити →` | `Заказать →` | ⚠ inconsistency: DE/EN say "anfragen/request" (inquire), UK/RU say "Замовити/Заказать" (order). Different framing — Slavic implies committed order, German/EN implies non-committed inquiry. **Fix:** UK `Запросити →`, RU `Запросить →` (or `Узнать больше →`). |
| `auto-form-topic-placeholder` | `Bitte wählen` | `Please choose` | `Оберіть тему` | `Выберите тему` | ✓ |
| `auto-form-time-any` | `Egal` | `Any time` | `Будь-який` | `Любое` | ✓ — appropriate softening |
| `auto-form-cp-wa-audio` | `WhatsApp (Audio)` | `WhatsApp (Audio)` | `WhatsApp (аудіо)` | `WhatsApp (аудио)` | ✓ |
| `auto-faq1-a` | `In der Regel innerhalb von 1–3 Werktagen…` | `Usually within 1–3 working days…` | `Зазвичай протягом 1–3 робочих днів…` | `Обычно в течение 1–3 рабочих дней…` | ✓ all natural |
| `auto-form-firstName` | `Vorname` | `First Name` | `Ім'я` | `Имя` | ✓ |
| `auto-services-cat-ankauf` | `Ankauf und Verkauf` | `Buying and Selling` | `Купівля та продаж` | `Покупка и продажа` | ✓ |
| `auto-svc6` (`auto-leist6-title`) | `Mehrsprachige Begleitung` | `Multilingual Support` | `Багатомовна підтримка` | `Многоязычная поддержка` | ✓ but "Begleitung" (escort/accompaniment) and "Support" are slightly different connotations — DE is warmer, EN more techy. Acceptable. |
| `auto-leist-cta-btn` | `Jetzt anfragen` | `Request now` | `Замовити консультацію` | `Заказать консультацию` | ⚠ Same Slavic "order" vs DE/EN "inquire" issue. **Fix:** UK `Запросити консультацію`, RU `Запросить консультацию`. |
| `home-bau-desc` | `Erstklassige Fliesenarbeiten, Renovierung und professionelle Umzugsbegleitung.` | `Premium tiling, renovation and professional moving services.` | `Преміальне укладання плитки, ремонт та допомога з переїздом.` | `Премиальная укладка плитки, ремонт и помощь с переездом.` | ⚠ "Umzugsbegleitung" (escorted move) → "moving services" is generic; in UK/RU "допомога з переїздом" is "help with moving" — close to source. EN is the loosest. |
| `auto-form-prefDate` | `Wunschdatum` | `Preferred Date` | `Бажана дата` | `Желаемая дата` | ✓ |
| `auto-about-tl4-title` | `Heute: 2000+ zufriedene Kunden` | `Today: 2000+ happy customers` | `Сьогодні: 2000+ задоволених клієнтів` | `Сегодня: 2000+ довольных клиентов` | ✗ all 4 contain the same fictional "2000+" — see Section 8 |

### Specific translation issues to fix

| Key / Locale | Current | Issue | Fix |
|---|---|---|---|
| `auto-pricing-card-cta` (UK) | `Замовити →` | "Order" tone | `Запросити →` |
| `auto-pricing-card-cta` (RU) | `Заказать →` | "Order" tone | `Запросить →` |
| `auto-leist-cta-btn` (UK) | `Замовити консультацію` | "Order" tone | `Запросити консультацію` |
| `auto-leist-cta-btn` (RU) | `Заказать консультацию` | "Order" tone | `Запросить консультацию` |
| `auto-cta-btn` (UK) | `Зв'язатися з нами` | uses "нами" (us, plural) | `Зв'язатися зі мною` |
| `auto-cta-btn` (RU) | `Связаться с нами` | uses "нами" (us, plural) | `Связаться со мной` |
| `home-bau-desc` (EN) | `Premium tiling, renovation and professional moving services.` | "moving services" is too generic; original DE is "Umzugsbegleitung" | `Premium tiling, renovation and professional moving assistance.` |
| `footer-impressum` (UK) | `Вихідні дані` | technical-publishing term, unusual for a website | `Реквізити` (more natural for a business contact page) |
| `footer-impressum` (RU) | `Выходные данные` | same publishing-jargon issue | `Реквизиты` |

**Severity: LOW** — translations are largely correct; mostly tone/register polish.

---

## Section 7 — Untranslated content (missing `data-i18n`)

This is the section where the BAU side falls apart for non-DE visitors.

### `bau/index.html` — entire content body untranslated

Headings, body paragraphs, modals, CTA buttons, counters — none have `data-i18n`. Specific items:

- L433 `<span class="label">Jahre Erfahrung</span>` — counter band labels
- L437 `<span class="label">Abgeschlossene Projekte</span>`
- L441 `<span class="label">Kundenbewertung</span>`
- L445 `<span class="label">Qualitätsgarantie</span>`
- L452 `<span class="eyebrow">Was wir anbieten</span>`
- L453 `<h2>Unsere Leistungen</h2>`
- L454 `<p>Von der Einzelfliese bis zur kompletten Raumsanierung — wir setzen Ihre Vorstellungen um.</p>`
- L459, 464, 469, 474 — service-card titles `Exklusive Fliesenarbeiten`, `Bodenverlegung`, `Naturstein & Terrassen`, `Montage & Feinarbeiten`
- L460, 465, 470, 475 — corresponding descriptions
- L479 `<a href="leistungen.html" class="btn btn-primary-bau">Alle Leistungen ansehen</a>`
- L486 `<span class="eyebrow">Warum Oleksandr Halushka</span>`
- L487 `<h2>Ihr Vorteil mit uns</h2>`
- L492–509 — 4× `why-item` block
- L516 `<span class="eyebrow">Kundenstimmen</span>`
- L517 `<h2>Was unsere Kunden sagen</h2>`
- L526 `<h2>Bereit für Ihr Projekt?</h2>`
- L527 `<p>Kontaktieren Sie uns für ein kostenloses Angebot — wir antworten persönlich.</p>`
- L528 `<a href="kontakt.html" class="btn">Jetzt Angebot anfragen</a>`
- L536–547 — modal `Exklusive Fliesenarbeiten` (heading, body, list, hint, CTA)
- L562–578, L585–600, L608–624 — three more modals (Boden, Naturstein, Feinarbeiten)
- L553, L576, L599, L623 — `Projekt anfragen` modal CTAs

### `bau/uber-uns.html` — only 2 keys translated (`bau-about-eyebrow`, `bau-about-title`)

L309 `<p>Erfahren Sie mehr über die Vision und das Team von Oleksandr Halushka im Bereich Bau & Innenausbau.</p>` and everything below (intro, values, timeline) — German-only.

### `bau/leistungen.html` — only `bau-services-eyebrow`, `bau-services-title` translated

Entire categories, items, modals — German-only.

### `bau/kontakt.html` — only `bau-contact-eyebrow`, `bau-contact-title` translated

ALL form labels, options, GDPR text, FAQ — German-only:
- L424 `<h2>Direkte Kontaktwege</h2>`
- L429–448 — Telefon/WhatsApp/E-Mail/Einsatzgebiet labels
- L465–567 — entire form (Vorname, Nachname, E-Mail, Bevorzugter Kontaktweg, options, Wunschdatum, Datenschutz checkbox, Newsletter checkbox, submit button)
- L588–608 — FAQ block

### `auto/index.html` — also has hardcoded form attributes

- L502 `placeholder="Max"` — placeholder for Vorname (should also be translated; placeholders in DE are universal anyway, but `Max` is a German given-name choice, EN should be `John` or `First`)
- L506 `placeholder="Mustermann"` — German equivalent of "Doe"; in EN should be `Doe` or `Last name`

### `auto/kontakt.html`

- L495–497 — honeypot label `Website (bitte leer lassen)` — leave as-is (hidden from users)
- L573–578 — GDPR consent text full sentence (`Ich stimme zu, dass meine Daten gemäß der Datenschutzerklärung verarbeitet werden, um meine Anfrage zu beantworten. *`) — **NOT translated.** Add `data-i18n="auto-form-gdpr"` and add to all 4 locales.
- L585–589 — Newsletter consent text similarly untranslated. Add key `auto-form-newsletter`.
- L432 `<div class="breadcrumb">…Kontakt & Termin</div>` — breadcrumb final segment hardcoded; add `data-i18n="breadcrumb-kontakt"` to each page.

### Footer hardcoded across all pages
- `auto/uber-uns.html:416`, `auto/leistungen.html:343`, `auto/kontakt.html:648`, `bau/*.html` footers — `Alle Rechte vorbehalten` is hardcoded (footer-copy key exists but isn't applied on these pages).
- `Hauptseite` / `Zurück zur Hauptseite` — back-to-home link untranslated everywhere.

**Severity: HIGH.** This is essentially a follow-up project — adding i18n keys for the entire bau side and the form GDPR text + footers. Estimated ~80–100 new translation keys needed.

### Suggested new keys to add to all locales (priority order)

```
bau-counter-experience, bau-counter-projects, bau-counter-rating, bau-counter-guarantee
bau-services-teaser-eyebrow, bau-services-teaser-title, bau-services-teaser-desc
bau-svc1-title, bau-svc1-desc, bau-svc2-title, bau-svc2-desc, bau-svc3-title, bau-svc3-desc, bau-svc4-title, bau-svc4-desc
bau-svc-all-cta
bau-why-eyebrow, bau-why-title
bau-why1-title, bau-why1-desc, bau-why2-title, bau-why2-desc, bau-why3-title, bau-why3-desc, bau-why4-title, bau-why4-desc
bau-testi-eyebrow, bau-testi-title
bau-cta-title, bau-cta-desc, bau-cta-btn
bau-modal-fliesen-title, bau-modal-fliesen-intro, bau-modal-fliesen-li1..li6, bau-modal-fliesen-hint
(and same for boden, naturstein, feinarbeiten modals)
bau-leist-cat1-title..cat4-title (4 categories)
bau-leist-item1..item11 (11 services across 4 categories) — title + desc each
bau-cta-leist-title, bau-cta-leist-desc, bau-cta-leist-btn
bau-about-page-desc, bau-about-intro-eyebrow, bau-about-intro-title, bau-about-intro-p1..p4, bau-about-intro-cta
bau-about-values-eyebrow, bau-about-values-title, bau-about-values-desc
bau-about-val1-title..val4-title (with descs)
bau-about-timeline-eyebrow, bau-about-timeline-title, bau-about-tl1..tl4 (title+desc)
bau-contact-page-desc, bau-kontakt-info-title, bau-kontakt-info-desc
bau-kontakt-tel-label, bau-kontakt-wa-label, bau-kontakt-wa-text, bau-kontakt-email-label, bau-kontakt-loc-label
bau-form-title, bau-form-intro, bau-form-firstName, bau-form-lastName, bau-form-email, bau-form-phone
bau-form-contactPref, bau-form-cp-email, bau-form-cp-wa-text, bau-form-cp-wa-audio, bau-form-cp-phone
bau-form-topic, bau-form-topic-placeholder, bau-form-topic-fliesen..montage..other (6 options)
bau-form-prefDate, bau-form-prefTime, bau-form-time-any..15-17 (5 options)
bau-form-message, bau-form-message-placeholder, bau-form-submit
bau-faq-eyebrow, bau-faq-title, bau-faq1-q..faq4-q (q+a each)
shared/footer-back-to-home, shared/breadcrumb-leistungen, shared/breadcrumb-kontakt, shared/breadcrumb-about
auto-form-gdpr, auto-form-newsletter (currently DE-only inline text)
```

---

## Section 8 — Counter Band — ethical alternatives (CRITICAL)

### Problem
`auto/index.html:407–425` declares:
- `5+ Jahre Erfahrung`
- `2000+ Zufriedene Kunden`
- `100% Profi-Qualität`
- `100% Transparenz`

For a brand-new solo Einzelunternehmer, "5+ Jahre Erfahrung" might be technically defensible if Oleksandr personally has 5+ years of professional driving/auto-trading experience pre-business — but "2000+ zufriedene Kunden" is almost certainly false at launch and would be classified as **Irreführung** under §5 UWG. "100% Profi-Qualität" and "100% Transparenz" are puffery on the edge of acceptable but, paired with the false numbers, signal a lack of credibility.

The same pattern repeats:
- `auto/uber-uns.html:406` (`auto-about-tl4-title`): `Heute: 2000+ zufriedene Kunden`
- All 4 locales mirror it.

The bau page also has fictional counters (`bau/index.html:431–446`):
- `10+ Jahre Erfahrung`
- `300+ Abgeschlossene Projekte`
- `5★ Kundenbewertung`
- `100% Qualitätsgarantie`

`5★ Kundenbewertung` — 5-star rating from whom? If there's no public review profile this is unsubstantiated.
`100% Qualitätsgarantie` — what does the guarantee actually cover? A "guarantee" without underlying T&C is misleading.

### Honest replacement set — AUTO (proposed)

**Option A — Identity-led (recommended for solo/launch):**

| # | Number / Visual | Label DE | Label EN | Label UK | Label RU |
|---|---|---|---|---|---|
| 1 | 4 | Sprachen | Languages | мови | языка |
| 2 | 1:1 | Persönliche Beratung | Personal advisory | Особиста консультація | Личная консультация |
| 3 | Bayern | Bayern-weit | Bavaria-wide | По всій Баварії | Вся Бавария |
| 4 | 100% | Unabhängig | Independent | Незалежно | Независимо |

**Option B — Action-oriented (slightly bolder, also honest):**

| # | Number | Label DE | Label EN | Label UK | Label RU |
|---|---|---|---|---|---|
| 1 | 1h | Antwortzeit | Response time | Час відповіді | Время ответа |
| 2 | 0€ | Erstberatung | First consultation | Перша консультація | Первая консультация |
| 3 | 4 | Sprachen | Languages | мови | языка |
| 4 | DE-AT | Marktkenntnis | Market expertise | Знання ринку | Знание рынка |

**Recommended:** Option A. Less aggressive, harder to dispute, fits the "ehrliche Beratung" brand positioning.

### Honest replacement set — BAU (proposed)

The bau page is more delicate because Oleksandr does have actual handwerklich experience. If 10+ years is provable (apprenticeship counts), keep it. Otherwise:

**Option A — verifiable:**

| # | Number | Label DE | Label EN | Label UK | Label RU |
|---|---|---|---|---|---|
| 1 | – | Festpreis-Angebot | Fixed-price quote | Фіксована ціна | Фиксированная цена |
| 2 | 0€ | Erstangebot | First quote | Перший розрахунок | Первая смета |
| 3 | – | Kostenvoranschlag | Free estimate | Кошторис | Смета |
| 4 | DE | Bayern | Bavaria | Баварія | Бавария |

**Option B — with "Jahre Handwerk" if defensible:**

If Oleksandr personally has e.g. 7 years tile-laying experience (apprenticeship + journeyman), then `7+ Jahre Handwerk` is honest — but **drop "Abgeschlossene Projekte" entirely** unless there's a portfolio of 300+ documented projects. Replace with:

| # | Number | Label DE | Label EN | Label UK | Label RU |
|---|---|---|---|---|---|
| 1 | 7+ | Jahre Handwerk | Years in trade | років у ремеслі | лет в ремесле |
| 2 | – | Kostenvoranschlag | Free estimate | Кошторис | Смета |
| 3 | DE | Bayern | Bavaria | Баварія | Бавария |
| 4 | 4 | Sprachen | Languages | мови | языка |

### Code patches for `auto/index.html:407–425`

Replace the entire `<div class="counter-band">…</div>` block with:

```html
<div class="counter-band">
    <div class="counter-item" data-aos="fade-up" data-aos-delay="0">
        <span class="count">4</span>
        <span class="label" data-i18n="auto-counter-languages">Sprachen</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="80">
        <span class="count">1:1</span>
        <span class="label" data-i18n="auto-counter-personal">Persönliche Beratung</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="160">
        <span class="count">Bayern</span>
        <span class="label" data-i18n="auto-counter-region">Bayern-weit</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="240">
        <span class="count">100%</span>
        <span class="label" data-i18n="auto-counter-independent">Unabhängig</span>
    </div>
</div>
```

And update locales (replacing the existing `auto-counter-experience / clients / quality / transparency`):

```json
"auto-counter-languages": "Sprachen",      // DE
"auto-counter-personal": "Persönliche Beratung",
"auto-counter-region": "Bayern-weit",
"auto-counter-independent": "Unabhängig",
```

EN:
```json
"auto-counter-languages": "Languages",
"auto-counter-personal": "Personal advisory",
"auto-counter-region": "Bavaria-wide",
"auto-counter-independent": "Independent",
```

UK:
```json
"auto-counter-languages": "мови",
"auto-counter-personal": "Особиста консультація",
"auto-counter-region": "По всій Баварії",
"auto-counter-independent": "Незалежно",
```

RU:
```json
"auto-counter-languages": "языка",
"auto-counter-personal": "Личная консультация",
"auto-counter-region": "Вся Бавария",
"auto-counter-independent": "Независимо",
```

### Patch for `auto-about-tl4-title` (timeline 4th milestone)

Replace `Heute: 2000+ zufriedene Kunden` everywhere:

```json
// DE
"auto-about-tl4-title": "Heute: persönlich, mehrsprachig, Bayern-weit",
// EN
"auto-about-tl4-title": "Today: personal, multilingual, Bavaria-wide",
// UK
"auto-about-tl4-title": "Сьогодні: персонально, чотирма мовами, по Баварії",
// RU
"auto-about-tl4-title": "Сегодня: лично, на четырёх языках, по Баварии",
```

And update `auto-about-tl4-desc` accordingly (drop "wir wachsen weiter" — replace with personal):
```json
// DE
"auto-about-tl4-desc": "Ich bleibe das, was ich von Anfang an war: nahbar, zuverlässig, professionell — und das in vier Sprachen.",
```

**Severity: CRITICAL.** Do this first, before any traffic / before paid ads.

---

## Section 9 — Metadata quality

| Page | `<title>` | Length | Meta-desc | Length | Verdict |
|---|---|---|---|---|---|
| `index.html` (root) | `Oleksandr Halushka — KFZ-Service & Innenausbau` | 47 chars | `Oleksandr Halushka — Ihr zuverlässiger Partner für professionellen KFZ-Service und erstklassigen Innenausbau in Bayern.` | 119 chars | ⚠ Title slightly too short, also "KFZ-Service" doesn't reflect the new positioning (purchase/sale advisory only, see commit `7aac267`). **Update:** `Oleksandr Halushka — KFZ-Beratung & Innenausbau in Bayern` (57 chars). Update meta-desc accordingly. |
| `auto/index.html` | `Beratung beim Autokauf und Autoverkauf \| Oleksandr Halushka` | 60 chars | `Oleksandr Halushka in Bayern — kompetente Begleitung beim An- und Verkauf Ihres Fahrzeugs. Marktbewertung, Besichtigungsbegleitung und ehrliche Beratung.` | 153 chars | ✓ both within range |
| `auto/leistungen.html` | `Beratung beim Autokauf und Autoverkauf \| Oleksandr Halushka` | 60 chars | `Oleksandr Halushka — kompetente Begleitung beim An- und Verkauf…` | 167 chars | ⚠ **DUPLICATE TITLE with auto/index.html** — fix to `Leistungen — KFZ-Beratung in Bayern \| Oleksandr Halushka` (53 chars). Meta-desc just over budget at 167; trim to ≤ 160. |
| `auto/uber-uns.html` | `Über uns \| Oleksandr Halushka · KFZ-Beratung` | 46 chars | `Lernen Sie das Team von Oleksandr Halushka kennen — erfahrene KFZ-Meister mit Leidenschaft für Fahrzeuge.` | 105 chars | ⚠ Title too short. Mentions "Team" — fix per Section 2. **Update title:** `Über mich — Oleksandr Halushka, KFZ-Beratung Bayern` (51 chars). |
| `auto/kontakt.html` | `Kontakt \| Oleksandr Halushka · KFZ-Beratung` | 45 chars | `Kontaktieren Sie Oleksandr Halushka — Termin anfragen, Fragen stellen oder direkt anrufen.` | 90 chars | ⚠ Both short. **Update title:** `Kontakt & Beratungstermin — Oleksandr Halushka Bayern` (53 chars). Description could include keywords: `…Oleksandr Halushka in Bad Abbach, Bayern — Auto-Beratung in 4 Sprachen. Termin anfragen, kostenlose Erstberatung.` |
| `bau/index.html` | `Innenausbau \| Oleksandr Halushka` | 33 chars | `Oleksandr Halushka · Innenausbau in Bayern — Fliesenarbeiten, Renovierung, Umzugsservice. Qualität die man sieht.` | 113 chars | ⚠ Title way too short. **Update:** `Innenausbau in Bayern — Fliesen, Renovierung \| Oleksandr Halushka` (66 chars — borderline). |
| `bau/leistungen.html` | `Leistungen Innenausbau \| Oleksandr Halushka` | 44 chars | `Alle Bauleistungen von Oleksandr Halushka — Fliesenarbeiten, Renovierung, Umzug, Möbelmontage und mehr.` | 103 chars | OK |
| `bau/uber-uns.html` | `Über uns \| Oleksandr Halushka · Innenausbau` | 45 chars | `Lernen Sie das Bau-Team von Oleksandr Halushka kennen — erfahrene Handwerker mit Leidenschaft für Details.` | 106 chars | ⚠ "Bau-Team" issue. **Update:** `Über mich — Oleksandr Halushka, Innenausbau Bayern` (50 chars). |
| `bau/kontakt.html` | `Kontakt \| Oleksandr Halushka · Innenausbau` | 44 chars | `Oleksandr Halushka · Innenausbau kontaktieren — Angebot anfragen, Terminvereinabrung, WhatsApp.` | 96 chars | ⚠ **Typo:** `Terminvereinabrung` → `Terminvereinbarung`. |
| `legal/impressum.html` | `Impressum \| Oleksandr Halushka` | 30 chars | (none) | – | OK for legal page |
| `legal/datenschutz.html` | `Datenschutzerklärung \| Oleksandr Halushka` | 41 chars | (none) | – | OK |

### Action list for metadata
1. **Fix duplicate title:** `auto/leistungen.html` and `auto/index.html` share the same title — break uniqueness.
2. **Fix typo** in `bau/kontakt.html` meta-desc: `Terminvereinabrung` → `Terminvereinbarung`.
3. Update all "Team"-mentioning meta-descs after Section 2 migration.
4. Standardize length: titles 50–60 chars, meta-desc 150–160 chars.
5. Add primary keyword + brand + location to every page (most are missing "Bayern" or "Bad Abbach" in titles).

**Severity: MEDIUM.**

---

## Section 10 — Brand consistency

### Brand name occurrences inventory

- `Oleksandr Halushka` — 100+ occurrences (visible). Consistent.
- `OLEKSANDR HALUSHKA` (logo styling, uppercase) — header/footer logos. ✓
- `O. Halushka` — **0 occurrences.** ✓ (good — no abbreviation drift)
- `Halushka` standalone — **0 occurrences in body copy.** ✓
- `Alex` standalone — **0 occurrences in body copy.** ✓
- `Oleksandr Halushka` / `Oleksandr Halushka Bau` — **0 occurrences in current site HTML/JSON.** ✓ (legacy files like `client-review/`, `research-gbp-naming/`, `Oleksandr Halushka_Контент_Перевірка.html` are archived; not part of live content)

### Email & social leftovers (`Oleksandr Halushkae` namespace)

| File | Line | Reference |
|---|---|---|
| `auto/index.html` | 541 | `https://www.instagram.com/Oleksandr Halushkae.auto/` |
| `auto/uber-uns.html` | 419 | same |
| `auto/leistungen.html` | 346 | same |
| `auto/kontakt.html` | 465, 651 | `info@Oleksandr Halushkae.de` and `instagram.com/Oleksandr Halushkae.auto` |
| `bau/index.html` | 635 | `instagram.com/Oleksandr Halushkae.innenausbau` |
| `bau/uber-uns.html` | 404 | same |
| `bau/leistungen.html` | 493 | same |
| `bau/kontakt.html` | 441, 617 | `info@Oleksandr Halushkae.de`, `instagram.com/Oleksandr Halushkae.innenausbau` |
| `legal/impressum.html` | 121 | `kontakt@Oleksandr Halushkae.de` |

**Decision needed:**
- **Option 1 (recommended):** Keep `Oleksandr Halushkae.de` as a brand-domain handle. It's a paid asset, simple, recognizable, and using a domain that doesn't include the natural-person name actually helps with future business growth (you can hire, scale without re-branding). Tell users transparently: "Oleksandr Halushkae.de — die Domain hinter der persönlichen Beratung von Oleksandr Halushka." Add a one-line clarification in the Impressum.
- **Option 2:** Migrate to `halushka.de` or `oleksandr-halushka.de`. More on-brand but expensive (forwarding the old domain, updating 9+ files, breaking inbound links if any).

If Option 1 — no change needed except an optional Impressum note.
If Option 2 — global find-replace `Oleksandr Halushkae.de` → new domain across all HTML.

### Inconsistency: `Email vs. Telefon`
- `auto/kontakt.html:451` — `tel:+4916093409671` and visible `+49 160 9340 9671`
- `bau/kontakt.html:429` — same number ✓ consistent
- `legal/impressum.html:120` — `+49 (0) 123 456789` — **placeholder, must be replaced with real number** (matches the §5 TMG legal-validity flag in TL;DR)

### Brand-line drift in headings
- `auto/uber-uns.html:322` `data-i18n="auto-about-page-desc"` says `Erfahren Sie mehr über das Team hinter Oleksandr Halushka` — "das Team hinter Oleksandr Halushka" structurally implies that Oleksandr is the brand (good) AND there is a team behind it (problematic — Section 2). Fix the copy as in Section 2.
- `bau/uber-uns.html:393` `Oleksandr Halushka — eine Marke, zwei Welten` — defensible if you want to position the brand as broader than the natural person, but inconsistent with the §5 UWG-safe positioning. Either keep + accept the "brand > person" framing OR rewrite as `Zwei Welten, ein Anspruch — Auto und Innenausbau bei Oleksandr Halushka`.

**Severity: LOW** for in-copy brand consistency; **MEDIUM** for the email/social handle decision.

---

## Wir → Ich migration master list (consolidated)

This section consolidates every line in the codebase that needs first-person-singular migration. Use as the master patch list.

### A. `locales/de.json` — string replacements

```diff
- "auto-hero-desc": "Wir begleiten Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis aus Bayern.",
+ "auto-hero-desc": "Ich begleite Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis aus Bayern.",

- "auto-services-eyebrow": "Was wir anbieten",
+ "auto-services-eyebrow": "Mein Angebot",

- "auto-services-title": "Unsere Leistungen",
+ "auto-services-title": "Meine Leistungen",

- "auto-services-page-desc": "Wir begleiten Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis.",
+ "auto-services-page-desc": "Ich begleite Sie persönlich beim An- und Verkauf — unabhängig, ehrlich und mit Marktkenntnis.",

- "auto-svc1-desc": "Wir helfen Ihnen, das passende Fahrzeug zu finden — Marktrecherche, Inseratscheck und ehrliche Einschätzung.",
+ "auto-svc1-desc": "Ich helfe Ihnen, das passende Fahrzeug zu finden — Marktrecherche, Inseratscheck und ehrliche Einschätzung.",

- "auto-svc2-desc": "Wir begleiten Sie zur Besichtigung und sprechen unabhängig über Auffälligkeiten — bevor Sie kaufen.",
+ "auto-svc2-desc": "Ich begleite Sie zur Besichtigung und spreche unabhängig über Auffälligkeiten — bevor Sie kaufen.",

- "auto-pricing-desc": "Schreiben Sie uns kurz, was Sie kaufen oder verkaufen möchten — die erste Einschätzung ist immer kostenlos und unverbindlich.",
+ "auto-pricing-desc": "Schreiben Sie mir kurz, was Sie kaufen oder verkaufen möchten — die erste Einschätzung ist immer kostenlos und unverbindlich.",

- "auto-why-eyebrow": "Warum wir",
+ "auto-why-eyebrow": "Warum mit mir",

- "auto-why-title": "Ihr Vorteil mit Oleksandr Halushka",
+ "auto-why-title": "Ihr Vorteil mit Oleksandr Halushka",   // unchanged — brand-noun frame works

- "auto-why3-desc": "Wir antworten zügig und liefern eine ehrliche Einschätzung — ohne langes Warten.",
+ "auto-why3-desc": "Ich antworte zügig und liefere eine ehrliche Einschätzung — ohne langes Warten.",

- "auto-testi-title": "Was unsere Kunden sagen",
+ "auto-testi-title": "Was meine Kunden sagen",

- "auto-cta-desc": "Buchen Sie jetzt Ihren Termin oder stellen Sie uns Ihre Frage — wir antworten persönlich.",
+ "auto-cta-desc": "Buchen Sie jetzt Ihren Termin oder stellen Sie mir Ihre Frage — ich antworte persönlich.",

- "auto-leist1-desc": "Wir helfen Ihnen, das passende Fahrzeug zu finden — von der Marktrecherche bis zum Inseratscheck.",
+ "auto-leist1-desc": "Ich helfe Ihnen, das passende Fahrzeug zu finden — von der Marktrecherche bis zum Inseratscheck.",

- "auto-leist2-desc": "Wir begleiten Sie zur Besichtigung, schauen das Fahrzeug gemeinsam mit Ihnen an und sprechen ehrlich über Auffälligkeiten — unabhängig vom Verkäufer.",
+ "auto-leist2-desc": "Ich begleite Sie zur Besichtigung, schaue das Fahrzeug gemeinsam mit Ihnen an und spreche ehrlich über Auffälligkeiten — unabhängig vom Verkäufer.",

- "auto-leist5-desc": "Sprechen Sie mit uns telefonisch, per WhatsApp oder per E-Mail — die erste Einschätzung ist immer kostenlos und unverbindlich.",
+ "auto-leist5-desc": "Sprechen Sie mit mir telefonisch, per WhatsApp oder per E-Mail — die erste Einschätzung ist immer kostenlos und unverbindlich.",

- "auto-leist6-desc": "Wir betreuen Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für die ukrainische Gemeinschaft in Bayern eine echte Hilfe.",
+ "auto-leist6-desc": "Ich betreue Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für die ukrainische Gemeinschaft in Bayern eine echte Hilfe.",

- "auto-leist-cta-desc": "Kontaktieren Sie uns — wir beraten Sie persönlich und kostenlos.",
+ "auto-leist-cta-desc": "Kontaktieren Sie mich — ich berate Sie persönlich und kostenlos.",

- "auto-about-eyebrow": "Wer wir sind",
+ "auto-about-eyebrow": "Wer ich bin",

- "auto-about-page-desc": "Erfahren Sie mehr über das Team hinter Oleksandr Halushka und was uns antreibt.",
+ "auto-about-page-desc": "Erfahren Sie mehr über Oleksandr Halushka und was mich antreibt.",

- "auto-about-intro-eyebrow": "Unsere Geschichte",
+ "auto-about-intro-eyebrow": "Meine Geschichte",

- "auto-about-intro-p2": "Als ukrainisches Team mit bayerischem Qualitätsanspruch verbinden wir besonderen Fleiß und Leidenschaft mit klaren, ehrlichen Aussagen. Jeder Kunde verdient eine verständliche Einschätzung — ohne Fachchinesisch und ohne versteckte Kosten.",
+ "auto-about-intro-p2": "Als Ukrainer mit bayerischem Qualitätsanspruch verbinde ich besonderen Fleiß und Leidenschaft mit klaren, ehrlichen Aussagen. Jeder Kunde verdient eine verständliche Einschätzung — ohne Fachchinesisch und ohne versteckte Kosten.",

- "auto-about-intro-p3": "Heute begleiten wir Kunden aus der ganzen Region und sind bekannt für schnelle Reaktionszeiten, sorgfältige Recherche und persönliche Ansprechbarkeit.",
+ "auto-about-intro-p3": "Heute begleite ich Kunden aus der ganzen Region und bin bekannt für schnelle Reaktionszeiten, sorgfältige Recherche und persönliche Ansprechbarkeit.",

- "auto-about-values-eyebrow": "Was uns ausmacht",
+ "auto-about-values-eyebrow": "Was mich ausmacht",

- "auto-about-values-title": "Unsere Werte",
+ "auto-about-values-title": "Meine Werte",

- "auto-about-values-desc": "Diese Grundsätze leiten unsere Arbeit jeden Tag.",
+ "auto-about-values-desc": "Diese Grundsätze leiten meine Arbeit jeden Tag.",

- "auto-about-val1-desc": "Jede Empfehlung erklären wir nachvollziehbar. Kein Schritt ohne Ihre ausdrückliche Zustimmung.",
+ "auto-about-val1-desc": "Jede Empfehlung erkläre ich nachvollziehbar. Kein Schritt ohne Ihre ausdrückliche Zustimmung.",

- "auto-about-val2-desc": "Wir arbeiten mit aktuellen Marktdaten und nach klaren, dokumentierten Standards.",
+ "auto-about-val2-desc": "Ich arbeite mit aktuellen Marktdaten und nach klaren, dokumentierten Standards.",

- "auto-about-val3-desc": "Absprachen werden eingehalten. Termine auch. Ihre Zeit ist uns wichtig.",
+ "auto-about-val3-desc": "Absprachen werden eingehalten. Termine auch. Ihre Zeit ist mir wichtig.",

- "auto-about-timeline-title": "Unsere Entwicklung",
+ "auto-about-timeline-title": "Mein Weg",

- "auto-about-tl2-desc": "Mit wachsendem Vertrauen eröffneten wir unseren ersten festen Standort und erweiterten das Beratungsangebot.",
+ "auto-about-tl2-desc": "Mit wachsendem Vertrauen kamen die ersten Stammkunden, die mich heute weiterempfehlen.",

- "auto-about-tl4-title": "Heute: 2000+ zufriedene Kunden",
+ "auto-about-tl4-title": "Heute: persönlich, mehrsprachig, Bayern-weit",

- "auto-about-tl4-desc": "Wir wachsen weiter und bleiben dabei das, was wir immer waren: nahbar, zuverlässig, professionell.",
+ "auto-about-tl4-desc": "Ich bleibe das, was ich von Anfang an war: nahbar, zuverlässig, professionell — und das in vier Sprachen.",

- "auto-contact-eyebrow": "Jetzt anfragen",
+ "auto-contact-eyebrow": "Ich bin für Sie da",   // matches HTML L434

- "auto-contact-page-desc": "Schreiben Sie uns oder rufen Sie an — wir melden uns mit einer ehrlichen Ersteinschätzung zurück.",
+ "auto-contact-page-desc": "Schreiben Sie mir oder rufen Sie an — ich melde mich mit einer ehrlichen Ersteinschätzung zurück.",

- "auto-kontakt-info-desc": "Wählen Sie den für Sie bequemsten Weg. Wir sind meist innerhalb von einer Stunde erreichbar.",
+ "auto-kontakt-info-desc": "Wählen Sie den für Sie bequemsten Weg. Ich bin meist innerhalb von einer Stunde erreichbar.",

- "auto-form-intro": "Füllen Sie das Formular aus — wir melden uns so schnell wie möglich.",
+ "auto-form-intro": "Füllen Sie das Formular aus — ich melde mich so schnell wie möglich.",

- "auto-faq1-a": "In der Regel innerhalb von 1–3 Werktagen. Bei dringenden Fällen versuchen wir, Sie noch am selben Tag zu kontaktieren.",
+ "auto-faq1-a": "In der Regel innerhalb von 1–3 Werktagen. Bei dringenden Fällen versuche ich, Sie noch am selben Tag zu kontaktieren.",

- "auto-faq3-a": "Wir beraten markenübergreifend zu Fahrzeugen aus dem europäischen, asiatischen und amerikanischen Markt.",
+ "auto-faq3-a": "Ich berate markenübergreifend zu Fahrzeugen aus dem europäischen, asiatischen und amerikanischen Markt.",

- "auto-faq4-a": "Ja. Auf Wunsch fahren wir mit Ihnen zur Besichtigung, schauen das Fahrzeug gemeinsam an und sprechen offen über Auffälligkeiten — bevor Sie eine Kaufentscheidung treffen.",
+ "auto-faq4-a": "Ja. Auf Wunsch fahre ich mit Ihnen zur Besichtigung, schaue das Fahrzeug gemeinsam an und spreche offen über Auffälligkeiten — bevor Sie eine Kaufentscheidung treffen.",

- "auto-faq5-a": "Wir beraten Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für Neukunden aus der ukrainischen Gemeinschaft in Bayern eine echte Hilfe.",
+ "auto-faq5-a": "Ich berate Sie auf Deutsch, Englisch, Ukrainisch und Russisch — gerade für Neukunden aus der ukrainischen Gemeinschaft in Bayern eine echte Hilfe.",
```

### B. `locales/en.json` — string replacements

(see Section 3 above for full list)

### C. `locales/uk.json` — string replacements

(see Section 4 above for full list)

### D. `locales/ru.json` — string replacements

(see Section 4 above for full list)

### E. `bau/index.html` HTML edits (no i18n, hardcoded)

```diff
- <span class="eyebrow">Was wir anbieten</span>
+ <span class="eyebrow" data-i18n="bau-services-teaser-eyebrow">Mein Angebot</span>

- <h2>Unsere Leistungen</h2>
+ <h2 data-i18n="bau-services-teaser-title">Meine Leistungen</h2>

- <p>Von der Einzelfliese bis zur kompletten Raumsanierung — wir setzen Ihre Vorstellungen um.</p>
+ <p data-i18n="bau-services-teaser-desc">Von der Einzelfliese bis zur kompletten Raumsanierung — ich setze Ihre Vorstellungen um.</p>

- <h2>Ihr Vorteil mit uns</h2>
+ <h2 data-i18n="bau-why-title">Ihr Vorteil mit mir</h2>

- <p>Jede Fliese, jede Wand, jede Ecke — wir liefern Ergebnisse, die überzeugen.</p>
+ <p data-i18n="bau-why1-desc">Jede Fliese, jede Wand, jede Ecke — ich liefere Ergebnisse, die überzeugen.</p>

- <p>Wir schützen Ihre Einrichtung und hinterlassen besenreine Räume.</p>
+ <p data-i18n="bau-why2-desc">Ich schütze Ihre Einrichtung und hinterlasse besenreine Räume.</p>

- <h2>Was unsere Kunden sagen</h2>
+ <h2 data-i18n="bau-testi-title">Was meine Kunden sagen</h2>

- <p>Kontaktieren Sie uns für ein kostenloses Angebot — wir antworten persönlich.</p>
+ <p data-i18n="bau-cta-desc">Kontaktieren Sie mich für ein kostenloses Angebot — ich antworte persönlich.</p>
```

(plus all 4 modal `<p>`-paragraphs and 4× repeated hint paragraphs as listed in Section 2)

### F. `bau/leistungen.html` HTML edits

(see Section 2 — same pattern: replace `wir` → `ich`, `unser` → `mein`, add `data-i18n`)

### G. `bau/uber-uns.html` HTML edits

(see Section 2 — biggest single page to fix; 23+ first-person-plural occurrences)

### H. `bau/kontakt.html` HTML edits

(see Section 2 — also entire form needs `data-i18n` attributes added per Section 7)

---

## Counter Band — Honest Alternatives (consolidated)

### Final recommended copy (Auto)

```html
<!-- auto/index.html — replace lines 407–425 -->
<div class="counter-band">
    <div class="counter-item" data-aos="fade-up" data-aos-delay="0">
        <span class="count">4</span>
        <span class="label" data-i18n="auto-counter-languages">Sprachen</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="80">
        <span class="count">1:1</span>
        <span class="label" data-i18n="auto-counter-personal">Persönliche Beratung</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="160">
        <span class="count">Bayern</span>
        <span class="label" data-i18n="auto-counter-region">Bayern-weit</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="240">
        <span class="count">100%</span>
        <span class="label" data-i18n="auto-counter-independent">Unabhängig</span>
    </div>
</div>
```

### Final recommended copy (Bau)

```html
<!-- bau/index.html — replace lines 430–447 -->
<div class="counter-band">
    <div class="counter-item" data-aos="fade-up" data-aos-delay="0">
        <span class="count">0€</span>
        <span class="label" data-i18n="bau-counter-quote">Erstangebot</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="80">
        <span class="count">Festpreis</span>
        <span class="label" data-i18n="bau-counter-fixedprice">oder Stundenbasis</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="160">
        <span class="count">Bayern</span>
        <span class="label" data-i18n="bau-counter-region">Einsatzgebiet</span>
    </div>
    <div class="counter-item" data-aos="fade-up" data-aos-delay="240">
        <span class="count">4</span>
        <span class="label" data-i18n="bau-counter-languages">Sprachen</span>
    </div>
</div>
```

### Removal of `Heute: 2000+ zufriedene Kunden`

Already covered in Wir → Ich migration list (`auto-about-tl4-title`).

---

## Action checklist (priority ordered)

### CRITICAL (do before launch / before any traffic)

- [ ] **C1.** Fix `legal/impressum.html` — replace `Musterstraße 123, 80331 München`, `+49 (0) 123 456789`, `DE123456789` with real Oleksandr Halushka address, phone, USt-IdNr (or remove USt-ID line if Kleinunternehmer per §19 UStG). §5 TMG validity. ⚠️ Site is legally invalid until this is done.
- [ ] **C2.** Replace `auto/index.html:407–425` counter band with the 4-tile honest alternative (Section 8 / Counter Band consolidated).
- [ ] **C3.** Replace `auto-about-tl4-title` and `auto-about-tl4-desc` in all 4 locales (drop "2000+ Kunden").
- [ ] **C4.** Replace `bau/index.html:430–447` counter band (drop "10+ Jahre", "300+ Projekte", "5★ Kundenbewertung", "100% Qualitätsgarantie").
- [ ] **C5.** Run "Wir → Ich migration" master patch (Sections 2–4 + consolidated diff). Estimated 100+ edits in DE alone, similar in EN/UK/RU. Best done as one PR per locale.
- [ ] **C6.** Translate `bau/*` pages — add ~80 new `bau-*` keys to all 4 locales, add `data-i18n` attributes to all hardcoded text in `bau/index.html`, `bau/leistungen.html`, `bau/uber-uns.html`, `bau/kontakt.html`. Largest single block of work.

### HIGH

- [ ] **H1.** Add `data-i18n` to GDPR consent text and Newsletter consent text in `auto/kontakt.html` and `bau/kontakt.html`. Add `auto-form-gdpr`, `auto-form-newsletter`, `bau-form-gdpr`, `bau-form-newsletter` keys to all 4 locales.
- [ ] **H2.** Fix duplicate title in `auto/leistungen.html` vs `auto/index.html`.
- [ ] **H3.** Fix typo `Terminvereinabrung` → `Terminvereinbarung` in `bau/kontakt.html` meta-desc.
- [ ] **H4.** Update root `index.html` title from `KFZ-Service & Innenausbau` to `KFZ-Beratung & Innenausbau` (matches the Beratung-only positioning per commit `7aac267`).
- [ ] **H5.** Make footer-copy and footer Hauptseite link i18n-driven on all pages (currently inconsistent: `auto/index.html` uses `data-i18n="footer-copy"`, but `auto/uber-uns.html`, `auto/leistungen.html`, `auto/kontakt.html`, all `bau/*` use hardcoded `Alle Rechte vorbehalten`).
- [ ] **H6.** Translate breadcrumb segments (`Über uns`, `Leistungen`, `Kontakt & Termin`, `Kontakt & Angebot`).

### MEDIUM

- [ ] **M1.** Decide on `Oleksandr Halushkae.de` vs new domain (Section 10) — if new domain, global find-replace.
- [ ] **M2.** Update meta-descriptions on auto/uber-uns.html (drop "Team von Oleksandr Halushka" wording).
- [ ] **M3.** Standardize title lengths to 50–60 chars per Section 9 table.
- [ ] **M4.** Pick consistent Slavic verb framing for CTA: `Запросити` vs `Замовити` (UK), `Запросить` vs `Заказать` (RU). Recommend "request" framing throughout.
- [ ] **M5.** Update `auto/kontakt.html` placeholder `Max` / `Mustermann` to be locale-appropriate (or keep DE-only since they're hidden behind the form anyway).
- [ ] **M6.** Update image alts across `bau/uber-uns.html`, `auto/uber-uns.html` to drop "Team" wording.
- [ ] **M7.** Decide on flag emoji 🇺🇦 placement — keep on About page only, or move to a small persistent trust indicator.

### LOW (polish)

- [ ] **L1.** EN polish on a few literal-translation strings (`auto-faq2-a` "always with a clear quote in advance" → "always with a clear estimate up front").
- [ ] **L2.** UK/RU footer-impressum (`Вихідні дані` / `Выходные данные`) → `Реквізити` / `Реквизиты`.
- [ ] **L3.** Add `bau-*` placeholders to `nav-gallery` (still in JSON but no `Galerie` page exists — verify if it should be removed entirely).
- [ ] **L4.** Run Lighthouse + a11y check after content changes.
- [ ] **L5.** Final native-speaker proofread of all 4 locales (DE-native, EN-native, UK-native, RU-native).

---

## Source files audited (absolute paths)

- `/Volumes/Extreme SSD/oleksandrhalushkaweb/index.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/auto/index.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/auto/leistungen.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/auto/uber-uns.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/auto/kontakt.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/bau/index.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/bau/leistungen.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/bau/uber-uns.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/bau/kontakt.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/legal/impressum.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/legal/datenschutz.html`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/locales/de.json`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/locales/en.json`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/locales/uk.json`
- `/Volumes/Extreme SSD/oleksandrhalushkaweb/locales/ru.json`

**Audit total runtime:** ~35 minutes
**Strings inspected:** ~640 i18n entries + ~9 HTML files × ~500 lines each
**Critical findings:** 4 (Counter Band lies, Wir-saturation §5 UWG, Bau monolingual, Impressum placeholder)
**Estimated fix effort:** 6–10h focused work for a developer + 2h native-speaker review per locale.
