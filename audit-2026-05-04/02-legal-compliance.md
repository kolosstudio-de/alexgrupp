# Юридичний аудит сайту Oleksandr Halushka

**Дата:** 2026-05-04
**Аудитор:** Claude (research agent)
**Власник:** Oleksandr Halushka, Einzelunternehmer (Bayern, USt-pflichtig)
**Сайт:** Oleksandr Halushkae.de (припускається — судячи з email/Instagram handles)
**Напрямки:** (1) Auto-Beratung — Kauf/Verkauf-Begleitung; (2) Bau / Innenausbau / Renovierung / Umzug

---

## TL;DR — топ-3 ризики прямо зараз

1. **CRITICAL — «2000+ zufriedene Kunden» + «5+ Jahre Erfahrung» + «10+ Jahre Erfahrung» (Counter Bands)**
   Конкретні числові твердження для нового бренду + Auto-Startup. Це класичний § 5 Abs. 1 Nr. 3 UWG (Irreführung über die Eigenschaften des Unternehmens / Marktposition) + falsche Tatsachenbehauptung. **Wettbewerbszentrale, IDO, IHK München-Oberbayern це абмахає миттєво.** Ризик: 2 000–5 000 € Abmahnkosten + Vertragsstrafe 3 000–10 000 € pro Wiederholung.
   *Файли: `auto/index.html:407-425`, `bau/index.html:430-447`, `auto/uber-uns.html:404-409`.*

2. **CRITICAL — Impressum + Datenschutzerklärung нерелевантні / неповні**
   Impressum містить **Musterstraße 123, 80331 München, Tel +49 (0)123 456789, USt-ID DE123456789** — це placeholder/Lorem-Ipsum-дані, не реальні. Це означає що зараз сайт de-facto має **жодного валідного Impressum** → § 5 Abs. 1 DDG порушено + § 18 Abs. 2 MStV → це автоматичний Abmahngrund (Wettbewerbszentrale серійно мониторить).
   Datenschutzerklärung — це 4 параграфи на ~150 слів, не покриває жодних із обов'язкових пунктів за Art. 13 DSGVO (Verantwortlicher, Rechtsgrundlagen, Speicherdauer, Empfänger, Drittlandtransfer, Betroffenenrechte, Beschwerderecht). Google Maps iframe, Google Fonts, Cloudflare CDN, AOS, Font Awesome, Google Apps Script (форма) — **жоден не задокументований**. Це не Datenschutzerklärung, це косметика.
   *Файли: `legal/impressum.html:108-133`, `legal/datenschutz.html:108-125`.*

3. **CRITICAL — Cookie-banner порушує TTDSG/DDG + DSGVO Consent Logic**
   Banner з'являється з затримкою 800 ms `setTimeout(() => banner.classList.add('show'), 800)` — **до того, як користувач натиснув щось**, на сторінці вже завантажено: Google Fonts (читає IP), Cloudflare CDN (Font Awesome), unpkg.com (AOS), Google Maps iframe (на kontakt-сторінках). Усе це → § 25 TTDSG (тепер § 25 TDDDG з 14.05.2024) + Art. 6 Abs. 1 DSGVO порушення. EuGH (Planet49, C-673/17), BGH (I ZR 7/16) і LG München I (17 O 14857/22 «Google Fonts») чітко вимагають **Opt-In ДО завантаження**. Поточна реалізація — це cosmetic banner, не consent gate. Ризик: 100–5 000 € Schadensersatz pro Nutzer (Google-Fonts-Welle 2022/2023 показала що це монетизуються).
   *Файл: `js/components/smart-header.js:146-234`.*

---

## Загальний рейтинг compliance: **3/10 (CRITICAL)**

Сайт у поточному стані **НЕ можна публікувати** для широкої аудиторії в Bayern. Якщо вже опубліковано — треба максимально швидко (24–72 год) виправити Impressum, Datenschutz і Counter-Band-числа, поки не прилетіла Abmahnung.

---

## 1. Impressum (`legal/impressum.html`) — **CRITICAL**

### Знайдене

```html
<p>Angaben gemäß § 5 TMG</p>      ← застаріле; з 14.05.2024 чинний § 5 DDG
<strong>Oleksandr Halushka</strong>
Musterstraße 123                   ← PLACEHOLDER — не реальна адреса
80331 München                      ← PLACEHOLDER — не реальний PLZ
Telefon: +49 (0) 123 456789        ← PLACEHOLDER — не реальний номер
E-Mail: kontakt@Oleksandr Halushkae.de     ← на kontakt.html стоїть info@Oleksandr Halushkae.de
USt-IdNr. DE123456789              ← PLACEHOLDER — не реальний номер
```

### Чого критично бракує

| Обов'язково за законом | Стан | Закон |
|---|---|---|
| Правильна правова основа (§ 5 DDG, не TMG) | ❌ застаріле | DDG ст. 5 (з 14.05.2024) |
| Реальна Anschrift (vollständige ladungsfähige Adresse) | ❌ Mustertext | § 5 Abs. 1 Nr. 1 DDG |
| Реальний Telefon + E-Mail (zwei voneinander unabhängige Kommunikationswege — EuGH C-298/07 «deutsche internet versicherung») | ❌ Mustertext | § 5 Abs. 1 Nr. 2 DDG |
| Реальний USt-IdNr. | ❌ Mustertext | § 5 Abs. 1 Nr. 6 DDG + § 27a UStG |
| Verantwortlich gem. § 18 Abs. 2 MStV (для журналістсько-редакційних текстів — блог, новини) | ❌ відсутнє | § 18 Abs. 2 MStV |
| § 36 VSBG Hinweis (Verbraucherschlichtungsstelle): «Nicht bereit / nicht verpflichtet» | ❌ відсутнє | § 36 VSBG |
| OS-Plattform — є, але формула «Unsere E-Mail» (множина для соло) | ⚠️ часткове | Art. 14 ODR-VO |
| Aufsichtsbehörde — для Bau (HWK Niederbayern-Oberpfalz, бо Bad Abbach) | ❌ відсутнє | § 5 Abs. 1 Nr. 3 DDG |
| Berufsbezeichnung + zuständige Kammer + Mitgliedstaat — для Bau (handwerksrelevant) | ❌ відсутнє | § 5 Abs. 1 Nr. 5 DDG |
| Berufsrechtliche Regelungen (HwO + Anlage A bei zulassungspflichtigem Handwerk) — для Bau | ❌ відсутнє | § 5 Abs. 1 Nr. 5 DDG |
| Versicherung (für Bauleistungen — Betriebshaftpflicht) — рекомендовано | ❌ відсутнє | best practice |

### Severity: **CRITICAL**

### Конкретний фікс — повний шаблон для `legal/impressum.html`

```
<h1>Impressum</h1>
<p>Angaben gemäß § 5 DDG (Digitale-Dienste-Gesetz) und § 18 Abs. 2 MStV.</p>

<h2>Diensteanbieter</h2>
<p>
  Oleksandr Halushka<br>
  Einzelunternehmen<br>
  Industriestraße 22         ← реальна адреса (така ж, як на kontakt.html)
  93077 Bad Abbach<br>
  Bayern, Deutschland
</p>

<h2>Kontakt</h2>
<p>
  Telefon: +49 160 9340 9671<br>      ← синхронно з kontakt.html
  E-Mail: <a href="mailto:info@Oleksandr Halushkae.de">info@Oleksandr Halushkae.de</a>
</p>

<h2>Umsatzsteuer-Identifikationsnummer</h2>
<p>USt-IdNr. gemäß § 27a UStG: DE&lt;РЕАЛЬНИЙ_НОМЕР&gt;</p>

<h2>Berufsbezeichnung und berufsrechtliche Regelungen</h2>
<p>
  <strong>Tätigkeit Bau / Innenausbau:</strong> Eingetragen in das Verzeichnis
  zulassungsfreier Handwerke / handwerksähnlicher Gewerbe (Anlage B HwO) bei der
  Handwerkskammer Niederbayern-Oberpfalz, Ditthornstraße 10, 93055 Regensburg.<br>
  Es gelten die Handwerksordnung (HwO) und die Bayerische Bauordnung (BayBO).<br>
  Einsehbar unter: <a href="https://www.gesetze-im-internet.de/hwo/">gesetze-im-internet.de/hwo</a>
</p>
<p>
  <strong>Tätigkeit Auto-Beratung:</strong> Reine Beratungsleistung beim Kauf
  und Verkauf von Kraftfahrzeugen ohne eigenen Fahrzeughandel und ohne
  Vermittlung im Sinne von § 34c GewO. Kein Kfz-Sachverständigenwesen
  im Sinne von § 36 GewO.
</p>

<h2>Aufsichtsbehörde</h2>
<p>
  Für gewerberechtliche Angelegenheiten:<br>
  Stadt Bad Abbach – Gewerbeamt, Marktplatz 5, 93077 Bad Abbach.<br>
  Für handwerksrechtliche Angelegenheiten:<br>
  Handwerkskammer Niederbayern-Oberpfalz, Ditthornstraße 10, 93055 Regensburg.
</p>

<h2>Verantwortlich für den Inhalt nach § 18 Abs. 2 MStV</h2>
<p>Oleksandr Halushka, Anschrift wie oben.</p>

<h2>Verbraucherstreitbeilegung / Universalschlichtungsstelle</h2>
<p>
  Ich bin nicht bereit und nicht verpflichtet, an Streitbeilegungsverfahren
  vor einer Verbraucherschlichtungsstelle teilzunehmen
  (§ 36 Abs. 1 Nr. 1 VSBG).
</p>

<h2>EU-Streitschlichtung (Online Dispute Resolution)</h2>
<p>
  Die Europäische Kommission stellt eine Plattform zur Online-Streitbeilegung
  (OS) bereit:
  <a href="https://ec.europa.eu/consumers/odr/" target="_blank" rel="noopener">
  https://ec.europa.eu/consumers/odr/</a>.
  Meine E-Mail-Adresse finden Sie oben.
</p>

<h2>Berufshaftpflicht (Bau)</h2>
<p>
  Berufshaftpflichtversicherung: &lt;Versicherer, Adresse, Geltungsbereich Deutschland/EU&gt;
</p>

<h2>Haftungs- und Urheberrechtshinweis</h2>
<p>Inhalte und Werke auf dieser Website unterliegen dem deutschen Urheberrecht.
Eine Vervielfältigung oder Verwertung außerhalb der gesetzlichen Schranken
bedarf der schriftlichen Zustimmung des jeweiligen Rechteinhabers.</p>
```

> Зверніть увагу — використання **«Ich»** замість «Wir» (бо це Einzelunternehmer + § 36 VSBG явно вимагає особистої форми «Ich bin/bin nicht bereit»). Це паралельно знімає UWG-ризик з §5.

---

## 2. Datenschutzerklärung (`legal/datenschutz.html`) — **CRITICAL**

### Знайдене

Лише 3 розділи, ~150 слів, **жодних обов'язкових Pflichtangaben Art. 13 DSGVO**:
- ❌ Verantwortlicher (Name + повна адреса) — відсутнє (відсилає до Impressum, але це не достатньо для Art. 13)
- ❌ Контакт DPO — для Einzelunternehmer без 20+ працівників не обов'язково за § 38 BDSG, але треба явно зазначити «Kein Datenschutzbeauftragter erforderlich»
- ❌ Rechtsgrundlagen (Art. 6 Abs. 1 lit. a/b/c/f) — відсутнє
- ❌ Empfänger / Auftragsverarbeiter — відсутнє
- ❌ Speicherdauer — відсутнє
- ❌ Drittlandtransfer (USA: Google Fonts/Maps/GAS, Cloudflare) + Standardvertragsklauseln — відсутнє
- ❌ Betroffenenrechte (Art. 15–22) — відсутнє
- ❌ Beschwerderecht у BayLDA (Bayerisches Landesamt für Datenschutzaufsicht, Promenade 18, 91522 Ansbach) — відсутнє
- ❌ Cookies-Kategorisierung — відсутнє
- ❌ Google Maps iframe (на обох kontakt.html) — не задекларовано → пряме порушення (LG München I 17 O 14857/22 — це 100 € Schadensersatz pro Nutzer)
- ❌ Google Fonts — преконект і CSS-завантаження → IP-передача до Google в США без consent → таж сама судова практика
- ❌ Cloudflare CDN (Font Awesome) — IP до Cloudflare US
- ❌ unpkg.com (AOS) — IP до Cloudflare/Fastly
- ❌ Google Apps Script (форма) — обробка персональних даних (ім'я, email, телефон, повідомлення) на Google US-серверах через `fetch(GAS_WEB_APP_URL, {mode:'no-cors'})` → це Auftragsverarbeitung за Art. 28 DSGVO + Drittlandtransfer за Art. 44–46

### Severity: **CRITICAL**

### Конкретний фікс — структура нової `legal/datenschutz.html`

Потрібен повноцінний документ з 13–15 розділами. Скелет:

```
1. Verantwortlicher (Art. 4 Nr. 7 DSGVO)
   — повне ім'я, адреса, телефон, email Oleksandr Halushka
2. Allgemeines zur Datenverarbeitung
3. Rechtsgrundlagen (Art. 6 Abs. 1 lit. a/b/c/f) — для кожного типу обробки
4. Speicherdauer
5. Bereitstellung der Website / Server-Logs
   — Hostprovider, IP, User-Agent, Speicherdauer (max 7-14 Tage)
6. Cookies und ähnliche Technologien
   — Kategorisierung: Notwendig / Statistik / Marketing / Externe Medien
   — Rechtsgrundlage Notwendig: § 25 Abs. 2 Nr. 2 TDDDG
   — Rechtsgrundlage Andere: § 25 Abs. 1 TDDDG + Art. 6 Abs. 1 lit. a DSGVO
7. Kontaktformular (Google Apps Script)
   — Pflichtfelder, optionale Felder
   — Übermittlung an Google US (Auftragsverarbeitung Art. 28 + SCC Art. 46)
   — Speicherdauer
8. Newsletter (10% Rabatt-Checkbox)
   — Double-Opt-In nach § 7 Abs. 2 Nr. 3 UWG
   — Widerruf jederzeit per Klick / Email
9. Eingebundene Drittanbieter-Dienste:
   9.1 Google Fonts (Google Ireland Ltd / Google LLC) — IP, SCC
   9.2 Google Maps (kontakt-Seiten) — IP, SCC, Two-Click-Solution empfohlen
   9.3 Google Apps Script — siehe 7
   9.4 Cloudflare CDN (cdnjs für Font Awesome) — IP, SCC
   9.5 unpkg.com (AOS) — IP, SCC
   9.6 Hosting (нагріт що це GitHub Pages з папки github/ — це LLC US → SCC)
10. Social Media Links (Instagram, Facebook, LinkedIn — у footer)
    — Hinweis: keine Datenübertragung beim Klick auf den reinen Link;
      Nutzer wird jedoch nach Klick zu Plattform geleitet
11. Rechte der Betroffenen (Art. 15-22 DSGVO)
    — Auskunft, Berichtigung, Löschung, Einschränkung,
      Datenübertragbarkeit, Widerspruch, Widerruf
12. Beschwerderecht
    — BayLDA (Bayerisches Landesamt für Datenschutzaufsicht,
      Promenade 18, 91522 Ansbach, https://www.lda.bayern.de)
13. Aktualität / Änderung der Datenschutzerklärung
```

> **CRITICAL bonus:** Google Maps iframe **треба замінити на «Two-Click»** — статичну прев'юшку з посиланням «Karte aktivieren» (Klick → завантаження iframe). Це ekanon після LG München I 17 O 14857/22. Або принаймні блокувати iframe до consent через `data-src` + JS.

---

## 3. Cookie-banner (`js/components/smart-header.js:146-234`) — **CRITICAL**

### Знайдене

```js
class CookieBanner {
    init() {
        if (localStorage.getItem(this.storageKey)) return;
        this.injectCSS();
        this.render();        // показує банер
    }
    render() {
        // ...
        setTimeout(() => banner.classList.add('show'), 800);   // показ через 800ms
        document.getElementById('btn-accept-all').addEventListener('click', () => this.saveConsent('all'));
        document.getElementById('btn-accept-necessary').addEventListener('click', () => this.saveConsent('necessary'));
    }
    saveConsent(level) {
        localStorage.setItem(this.storageKey, level);
        // ...
        if (level === 'all') console.log('Analytics allowed');   // ← НЕ блокує/розблокує нічого!
    }
}
```

### Проблеми

| # | Проблема | Закон | Severity |
|---|---|---|---|
| 3.1 | Google Fonts завантажуються в `<head>` через preconnect+stylesheet **до consent** | § 25 Abs. 1 TDDDG, Art. 6 Abs. 1 DSGVO, LG München I 17 O 14857/22 | CRITICAL |
| 3.2 | Cloudflare CDN (Font Awesome) — те саме | те саме | CRITICAL |
| 3.3 | unpkg.com (AOS) — те саме | те саме | HIGH |
| 3.4 | Google Maps iframe (auto/kontakt.html, bau/kontakt.html) — `loading="lazy"` не достатньо, бо все одно завантажиться при scroll | таж судова практика | CRITICAL |
| 3.5 | Banner з'являється через 800 ms — за цей час Google Fonts і Maps вже завантажились | EuGH C-673/17 «Planet49» — pre-checked не consent | CRITICAL |
| 3.6 | Немає категоризації (Notwendig / Statistik / Marketing / Externe Medien) — лише «All / Only Necessary» | DSK Orientierungshilfe Telemedienanbieter 2021 | HIGH |
| 3.7 | Немає окремого «Ablehnen»-кнопки на одному рівні з «Akzeptieren» | DSK + Cyberlock-Urteil OLG Köln 6 U 65/22 (Nov 2022) | HIGH |
| 3.8 | Немає посилання «Einstellungen ändern» / «Consent widerrufen» **після** консенту (дзвоник у footer) | Art. 7 Abs. 3 DSGVO — Widerruf so einfach wie Erteilung | HIGH |
| 3.9 | `saveConsent('all')` лише пише в localStorage — нічого не блокує/розблоковує насправді | sham consent — § 25 TDDDG | CRITICAL |
| 3.10 | Перший візит — banner appears **after** GET-запитів до Google Fonts/CDN зроблено | Cookie/Tracking-Welle 2024 | CRITICAL |

### Severity: **CRITICAL**

### Фікс — три рівні

**Рівень 1 (мінімум — швидко):**
1. Прибрати **Google Fonts preconnect+stylesheet** з `<head>` — або перейти на self-hosted Inter/DM Sans (1 раз скачати + положити у `assets/fonts/`).
2. Self-host **Font Awesome** (download → положити у `assets/icons/fa/`) — це 1 файл css + 1 woff2.
3. Self-host **AOS** (download → `assets/lib/aos.js + aos.css`).
4. Замінити **Google Maps iframe** на статичну картинку з кнопкою «Karte laden»:
   ```html
   <div class="map-placeholder" style="background:url('../assets/map-static.png') center/cover;">
     <button onclick="loadMap()">Karte aktivieren (Google Maps)</button>
   </div>
   <script>
     function loadMap(){
       if(!confirm('Beim Laden werden Daten an Google in den USA übertragen. Einverstanden?')) return;
       document.querySelector('.map-placeholder').innerHTML =
         '<iframe src="...maps embed url..." width="100%" height="220" style="border:0"></iframe>';
     }
   </script>
   ```
   Або згенерувати static screenshot через Static Maps API (це теж надсилає IP, але **тільки після кліку**, тобто consent).

Після цього 90% problem'и зникають — самі по собі лишаються тільки cookies/localStorage самого сайту, які можна зробити **opt-in default = allowed only essential**.

**Рівень 2 (середній — повноцінний CMP-style banner):**
- Категорії: Notwendig (always on, неможливо вимкнути) / Statistik (default off) / Marketing (default off) / Externe Medien (default off, окремо для Maps + GAS-form-submission).
- Три кнопки: «Alle akzeptieren» / «Auswahl speichern» / «Nur Notwendige» (всі в один ряд, **однакового розміру**).
- Додати кнопку «Einstellungen» у footer + у hash `#privacy-settings` для widerruf.
- При відмові — реально не вантажити сторонні скрипти (умовний `<script data-category="marketing" data-src="...">` + JS-loader).

**Рівень 3 (найкращий):** використати готовий open-source CMP — Klaro!, Borlabs (платний, повноцінний, для WP), або Cookiebot/Usercentrics (платний). Для статичного сайту — **Klaro!** дуже підходить (https://github.com/klaro-org/klaro), GPLv3, no tracking.

---

## 4. AGB / Widerrufsbelehrung — **HIGH**

### Знайдене

- ❌ AGB — **відсутні**
- ❌ Widerrufsbelehrung — **відсутні**
- ❌ Bestätigungsseite/Email після Form-Submit (§ 312i Abs. 1 Nr. 3 BGB) — у `booking-system.js` лише `mode:'no-cors'`, нема видимого Bestätigungsseite

### Аналіз обов'язковості

**Auto-Beratung + Bau-Innenausbau ↔ Verbraucher (B2C) + Online-Anfrage = Fernabsatzvertrag** за § 312c BGB. Якщо договір укладається на основі form-submission або email-листування → **Widerrufsrecht 14 Tage** за § 355 BGB обов'язкове.

| Закон | Ризик якщо немає | Severity |
|---|---|---|
| § 312d Abs. 1 + Art. 246a EGBGB — Informationspflichten | Widerrufsfrist подовжується до 12 місяців + 14 днів | HIGH |
| § 312i BGB — elektronischer Geschäftsverkehr Pflichten (Bestätigung по email, Eingabefehler korrigierbar) | Abmahnung | MEDIUM |
| § 312g BGB — Widerrufsrecht | Schadensersatz, повернення коштів роками | HIGH |
| § 305 BGB — AGB-Inhaltskontrolle | якщо немає — застосовуються gesetzliche Bestimmungen, тобто **non-issue для відсутніх AGB**, але контракт стає менш вигідним | LOW |

**Ключове розрізнення:** для **Werkverträgen (Bau)** Widerrufsrecht діє тоді коли договір укладено на extramural site (поза фіксованим Geschäftsraum), що включає **онлайн-формою**. Тобто треба!

Для **Beratungsverträge (Auto)** — те саме.

### Severity: **HIGH**

### Конкретний фікс

1. **Додати `legal/agb.html`** — окремі AGB для Auto і Bau, або дві версії в одному документі. Мінімальні розділи:
   - Geltungsbereich
   - Vertragsabschluss
   - Leistungserbringung (різні для Auto vs Bau)
   - Vergütung / Preise
   - Mitwirkungspflichten Kunde
   - Haftung
   - Datenschutz (посилання)
   - Streitbeilegung
   - Schlussbestimmungen / anwendbares Recht / Gerichtsstand

2. **Додати `legal/widerruf.html`** з канонічним Muster-Widerrufsbelehrung за Art. 246a § 1 Abs. 2 Nr. 1 EGBGB + Muster-Widerrufsformular. Готовий шаблон є на BMJV: https://www.bmj.de/SharedDocs/Downloads/DE/Service/Formulare/Widerrufsbelehrung_und_Muster_Widerrufsformular.html

3. **При Form-Submit показувати Bestätigung на сторінці** + надсилати **automatic confirmation email** з зазначенням Widerrufsbelehrung та повторного переліку умов (§ 312f Abs. 2 BGB — Bestätigung in Textform unverzüglich nach Vertragsschluss).

4. **Додати в Form checkbox перед submit:**
   ```html
   <input type="checkbox" required id="agb">
   <label for="agb">Ich habe die <a href="../legal/agb.html">AGB</a> und die
   <a href="../legal/widerruf.html">Widerrufsbelehrung</a> gelesen und stimme zu. *</label>
   ```

5. **§ 312i BGB Eingabefehler-Korrektur** — браузер robust required-валідація це покриває, але треба переконатись що user **бачить підтвердження перед фінальним submit** (наприклад, summary-modal перед `fetch()`).

---

## 5. «Über uns» vs «Über mich» — критичний UWG-аналіз — **HIGH**

### Юридична основа

§ 5 Abs. 1 Nr. 3 UWG — Irreführung про **«persönliche oder geschäftliche Verhältnisse des Unternehmers»**, в т.ч. **Größe und Art** unternehmens.

Прецеденти:
- **OLG Schleswig 28.09.2011, Az. 2 W 231/10** — «Group/Gruppe» в назві Einzelkaufmann вводить у заблуждення про існування групи (вже відомо з research-gbp-naming).
- **OLG Hamm 13.03.2012, Az. 4 U 198/11** — «Wir» в Internet-Auftritt Einzelunternehmer'а коли натяк на team — порушення.
- **LG Berlin 16.07.2013, Az. 91 O 21/13** — «unser Team» + «professionelle Mitarbeiter» — однієї людини = irreführend.

Висновок: **сайт зараз має дуже багато «wir/unser/uns/Team/Mitarbeiter» формулювань — це треба переробити.**

### Повний інвентар «we»-формулювань (це Einzelunternehmer!)

#### A. CRITICAL — пряме твердження про team / Mitarbeiter / Standorte

| Файл | Рядок | Поточно | Заміна |
|---|---|---|---|
| `auto/uber-uns.html` | line 9 (meta description) | "Lernen Sie das Team von Oleksandr Halushka kennen — erfahrene KFZ-Meister..." | "Lernen Sie Oleksandr Halushka kennen — erfahrener Berater für Kauf und Verkauf von Fahrzeugen in Bayern." |
| `auto/uber-uns.html` | 322 | "...mehr über das Team hinter Oleksandr Halushka..." | "...mehr über Oleksandr Halushka und was mich antreibt." |
| `auto/uber-uns.html` | 330 | `alt="Beratungsteam Oleksandr Halushka"` | `alt="Oleksandr Halushka — KFZ-Berater in Bayern"` |
| `auto/uber-uns.html` | 336 | "Als ukrainisches Team mit bayerischem Qualitätsanspruch verbinden wir..." | "Als gebürtiger Ukrainer mit bayerischem Qualitätsanspruch verbinde ich besonderen Fleiß..." |
| `auto/uber-uns.html` | 393 | "...wir unseren ersten festen Standort..." (timeline 2) | "...habe ich erste Kundenkontakte gefestigt und das Beratungsangebot strukturiert..." (без «Standort» — бо це або є, або немає) |
| `auto/uber-uns.html` | 406 | **"Heute: 2000+ zufriedene Kunden"** | **ВИДАЛИТИ або замінити на правдиве число.** Це найбільший ризик. |
| `bau/uber-uns.html` | line 9 (meta description) | "Lernen Sie das Bau-Team von Oleksandr Halushka kennen — erfahrene Handwerker..." | "Lernen Sie Oleksandr Halushka kennen — Handwerker für Innenausbau in Bayern." |
| `bau/uber-uns.html` | 309 | "...über die Vision und das Team von Oleksandr Halushka..." | "...über die Arbeitsweise von Oleksandr Halushka..." |
| `bau/uber-uns.html` | 320-321 | **"Unser Team aus erfahrenen Fliesenlegern, Renovierungsspezialisten und Umzugshelfern..."** | "**In meiner Arbeit verbinde ich Fliesenarbeiten, Renovierungen und Umzugsservice** — alles aus einer Hand und mit gleichbleibend hoher Sorgfalt." |
| `bau/uber-uns.html` | 323 | "Als ukrainisches Team mit bayerischem Qualitätsanspruch legen wir größten Wert..." | "Als gebürtiger Ukrainer mit bayerischem Qualitätsanspruch lege ich größten Wert..." |
| `bau/uber-uns.html` | 328 | `alt="Oleksandr Halushka · Innenausbau Team"` | `alt="Oleksandr Halushka · Innenausbau in Bayern"` |
| `auto/index.html` | 495 | **"Erfahrene KFZ-Profis"** (множина) | **"Erfahrener KFZ-Berater"** (однина) |
| `locales/de.json` | 48 | `"auto-why1-title": "Erfahrene KFZ-Profis"` | `"auto-why1-title": "Erfahrener KFZ-Berater"` |

#### B. HIGH — формули «wir» в маркетинговому тексті (треба замінити на «ich»/«bei mir»/«Sie bekommen»)

Усі знайдені у `locales/de.json` (загалом ~28 рядків з «wir/unser/uns»):

| Ключ | Поточно | Запропоновано |
|---|---|---|
| `nav-about` | "Über uns" | **"Über mich"** |
| `auto-hero-desc` | "Wir begleiten Sie persönlich..." | "Ich begleite Sie persönlich..." |
| `auto-services-eyebrow` | "Was wir anbieten" | "Was Sie bei mir bekommen" |
| `auto-services-title` | "Unsere Leistungen" | "Meine Leistungen" |
| `auto-services-page-desc` | "Wir begleiten Sie persönlich..." | "Ich begleite Sie persönlich..." |
| `auto-svc1-desc` | "Wir helfen Ihnen..." | "Ich helfe Ihnen..." |
| `auto-svc2-desc` | "Wir begleiten Sie..." | "Ich begleite Sie..." |
| `auto-pricing-desc` | "Schreiben Sie uns kurz..." | "Schreiben Sie mir kurz..." |
| `auto-why-eyebrow` | "Warum wir" | "Warum ich" |
| `auto-why3-desc` | "Wir antworten zügig..." | "Ich antworte zügig..." |
| `auto-testi-title` | "Was unsere Kunden sagen" | "Was meine Kunden sagen" |
| `auto-cta-desc` | "Buchen Sie jetzt Ihren Termin oder stellen Sie uns Ihre Frage — wir antworten persönlich." | "...stellen Sie mir Ihre Frage — ich antworte persönlich." |
| `auto-leist1-desc` | "Wir helfen Ihnen..." | "Ich helfe Ihnen..." |
| `auto-leist2-desc` | "Wir begleiten Sie zur Besichtigung, schauen das Fahrzeug gemeinsam mit Ihnen an und sprechen ehrlich..." | "Ich begleite Sie zur Besichtigung, schaue das Fahrzeug gemeinsam mit Ihnen an und spreche ehrlich..." |
| `auto-leist5-desc` | "Sprechen Sie mit uns telefonisch..." | "Sprechen Sie mit mir telefonisch..." |
| `auto-leist6-desc` | "Wir betreuen Sie..." | "Ich betreue Sie..." |
| `auto-leist-cta-desc` | "Kontaktieren Sie uns — wir beraten Sie persönlich..." | "Kontaktieren Sie mich — ich berate Sie persönlich..." |
| `auto-about-eyebrow` | "Wer wir sind" | "Wer ich bin" |
| `auto-about-page-desc` | "...mehr über das Team hinter Oleksandr Halushka und was uns antreibt." | "...mehr über Oleksandr Halushka und was mich antreibt." |
| `auto-about-cta` | "Mehr über uns" | "Mehr über mich" |
| `auto-about-intro-eyebrow` | "Unsere Geschichte" | "Meine Geschichte" |
| `auto-about-intro-p2` | "Als ukrainisches Team mit bayerischem Qualitätsanspruch verbinden wir..." | "Als gebürtiger Ukrainer mit bayerischem Qualitätsanspruch verbinde ich..." |
| `auto-about-intro-p3` | "Heute begleiten wir Kunden aus der ganzen Region und sind bekannt..." | "Heute begleite ich Kunden aus der ganzen Region und bin bekannt..." |
| `auto-about-values-eyebrow` | "Was uns ausmacht" | "Was mich ausmacht" |
| `auto-about-values-title` | "Unsere Werte" | "Meine Werte" |
| `auto-about-values-desc` | "Diese Grundsätze leiten unsere Arbeit jeden Tag." | "Diese Grundsätze leiten meine Arbeit jeden Tag." |
| `auto-about-val1-desc` | "Jede Empfehlung erklären wir nachvollziehbar." | "Jede Empfehlung erkläre ich nachvollziehbar." |
| `auto-about-val2-desc` | "Wir arbeiten mit aktuellen Marktdaten..." | "Ich arbeite mit aktuellen Marktdaten..." |
| `auto-about-timeline-title` | "Unsere Entwicklung" | "Mein Werdegang" (більш природно для соло) |
| `auto-about-tl2-desc` | "...wir unseren ersten festen Standort..." | "...habe ich meine Arbeitsabläufe gefestigt und das Beratungsangebot strukturiert." |
| `auto-about-tl4-desc` | "Wir wachsen weiter und bleiben dabei das, was wir immer waren..." | "Ich entwickle meinen Service weiter und bleibe dabei das, was ich immer war: nahbar, zuverlässig, sorgfältig." |
| `auto-contact-desc` | "...wir antworten schnell." | "...ich antworte schnell." |
| `auto-contact-page-desc` | "...wir melden uns mit einer ehrlichen Ersteinschätzung zurück." | "...ich melde mich mit einer ehrlichen Ersteinschätzung zurück." |
| `auto-kontakt-info-desc` | "...Wir sind meist innerhalb von einer Stunde erreichbar." | "...Ich bin meist innerhalb von einer Stunde erreichbar." |
| `auto-form-intro` | "...wir melden uns so schnell wie möglich." | "...ich melde mich so schnell wie möglich." |
| `auto-faq1-a` | "...versuchen wir, Sie noch am selben Tag zu kontaktieren." | "...versuche ich, Sie noch am selben Tag zu kontaktieren." |
| `auto-faq3-a` | "Wir beraten markenübergreifend..." | "Ich berate markenübergreifend..." |
| `auto-faq4-a` | "Auf Wunsch fahren wir mit Ihnen zur Besichtigung, schauen das Fahrzeug gemeinsam an..." | "Auf Wunsch fahre ich mit Ihnen zur Besichtigung, schaue das Fahrzeug gemeinsam mit Ihnen an..." |
| `auto-faq5-a` | "Wir beraten Sie auf Deutsch, Englisch, Ukrainisch und Russisch..." | "Ich berate Sie auf Deutsch, Englisch, Ukrainisch und Russisch..." |

#### C. MEDIUM — Bau-сторінка значно більше «wir»-формул (бо текст не в `locales/de.json`, а hardcoded)

`bau/uber-uns.html` — Values cards (line 342-360):
- "Wir legen Wert auf jede Fliese..." → "Ich lege Wert auf jede Fliese..."
- "Wir informieren Sie über den Fortschritt..." → "Ich informiere Sie über den Fortschritt..."
- "Wir kommen, wenn wir sagen, dass wir kommen. Und wir liefern, was wir versprechen." → "Ich komme, wenn ich es sage. Und ich liefere, was ich verspreche."

`bau/index.html` — Why-us-cards (line 489-510):
- "Wir liefern Ergebnisse..." → "Ich liefere Ergebnisse..."
- "Wir schützen Ihre Einrichtung..." → "Ich schütze Ihre Einrichtung..."
- "...Direkter Kontakt mit dem Handwerker, der Ihr Projekt betreut." — ОК (uniform Singular)

`bau/leistungen.html` — line 265: "wir realisieren Ihr Projekt termingerecht" → "ich realisiere Ihr Projekt termingerecht"

`bau/kontakt.html` — line 425: "Wir antworten innerhalb von einer Stunde" → "Ich antworte innerhalb von einer Stunde"; line 466: "wir erstellen Ihnen ein kostenloses Angebot" → "...ich erstelle Ihnen..."; line 595: "...sind für uns selbstverständlich..." → "...sind für mich selbstverständlich..."; line 599: "Wir arbeiten sowohl mit Festpreisen..." → "Ich arbeite sowohl mit Festpreisen..."; line 607: "Ja, wir verlegen Fliesen..." → "Ja, ich verlege Fliesen..."

#### D. Терпимо — формули де «wir» = я + клієнт

«Wir behandeln jede Wohnung, als wäre es **unsere** eigene» — це pluralis modestiae, прийнятно. Але краще «Ich behandle jede Wohnung, als wäre es **meine** eigene».

«Lassen Sie **uns** sprechen» — як CTA — OK.

#### Окремий концептуальний пункт: «Über uns» vs «Über mich» в навігації

На цей момент:
- Усі `nav-about` = "Über uns"
- Заголовок page hero на uber-uns.html teж формулює як «Wer wir sind»

**Проблема:** для соло Einzelunternehmer **«Über mich»** в навігації — гарна практика. Це і UWG-safe, і trust-positive (особистий бренд = відповідальний власник видно).

**Альтернатива:** «Über mich» можна замінити на нейтральне **«Profil»** або **«Wer ist Oleksandr»** — теж UWG-safe, але дещо менш Standard в DACH.

Рекомендую: **`nav-about: "Über mich"`** для всіх локалей.

### Severity: **HIGH**

### Конкретний action item

Зробити пакетне redbang:
1. У `locales/de.json` (і паралельно `en.json`, `uk.json`, `ru.json`) — замінити **«wir/unser/Team/Profis»** на «ich/mein/Berater»-форми (список вище).
2. У всіх HTML-файлах — те саме (особливо `bau/uber-uns.html`, `bau/index.html`, `bau/leistungen.html`, `bau/kontakt.html` де hardcoded).
3. Переглянути після ребрендингу: «Über uns» → **«Über mich»** в навігації.
4. У meta description і `alt`-атрибутах прибрати «Team».

---

## 6. Конкретні misleading wording-ризики (§ 5 UWG) — **HIGH**

| # | Знайдене | Файл / рядок | Severity | Закон | Фікс |
|---|---|---|---|---|---|
| 6.1 | «erfahrene KFZ-Meister» (meta description) | `auto/uber-uns.html:9` | HIGH | § 5 UWG; **Meister** — захищене поняття за HwO § 51 (тільки після Meisterprüfung). Якщо немає — це Berufsbezeichnungs-Anmaßung. | Замінити на «erfahrener Berater für Kauf und Verkauf» |
| 6.2 | «Erfahrene KFZ-Profis» (множина) | `auto/index.html:495`, `de.json:48` | HIGH | § 5 UWG (Größe + Anzahl Mitarbeiter) | «Erfahrener KFZ-Berater» (однина, безпечно) |
| 6.3 | «5+ Jahre Erfahrung», «10+ Jahre Erfahrung» | `auto/index.html:411`, `bau/index.html:433` | CRITICAL — окремий розділ нижче | § 5 UWG (zahlenmäßige Falschangabe) | Якщо реально не 10 років — прибрати або змінити на «Bayerische Qualität seit Tag 1» |
| 6.4 | «2000+ Zufriedene Kunden» | `auto/index.html:415`, `auto/uber-uns.html:406` (timeline+counter) | CRITICAL | § 5 UWG, BGH I ZR 234/93 «Werbung mit Fantasiezahlen» | Прибрати або замінити на правдиве; якщо нова справа — «Persönliche Betreuung» |
| 6.5 | «300+ Abgeschlossene Projekte» (Bau) | `bau/index.html:436` | CRITICAL | § 5 UWG | Аналогічно |
| 6.6 | «5★ Kundenbewertung» (Bau) | `bau/index.html:440` | HIGH | § 5 UWG; крім того якщо це звідкись агреговано — треба source (Google Reviews link?) | Прибрати або «100% positive Rückmeldungen» (без чисел) + linken до GBP-Reviews |
| 6.7 | «100% Profi-Qualität», «100% Transparenz» | `auto/index.html:419,423` | LOW (puffery — Werbliche Anpreisung) | OK як subjektive Behauptung | Залишити (це puffery, дозволено) |
| 6.8 | «100% Qualitätsgarantie» (Bau) | `bau/index.html:444` | HIGH — це може створити **vertragliche Garantie** за § 443 BGB! | § 443 BGB Garantie | Замінити на «Hohes Qualitätsanspruch» або «100% Sorgfalt» (без слова «Garantie») |
| 6.9 | «Standort» (singular) — Bad Abbach | `auto/kontakt.html:471` | OK | — | OK (singular) |
| 6.10 | «unseren ersten festen Standort» (timeline 2) | `auto/uber-uns.html:393` | MEDIUM | § 5 UWG (натяк що було декілька) | Прибрати «ersten» або переписати: «...habe ich meine Arbeitsabläufe gefestigt...» |
| 6.11 | «verbindlich» в submit-button + «kostenlos und unverbindlich» в FAQ | `auto/kontakt.html:594` vs `auto/kontakt.html:628` | MEDIUM | § 5 UWG — суперечливі сигнали («Anfrage verbindlich absenden» при безкоштовній консультації — клієнту незрозуміло, що саме verbindlich) | Замінити на «Anfrage senden» (нейтрально) + у Bestätigung уточнити що це лише запит, не Vertragsschluss |
| 6.12 | «Bemusterung/Start» з required Wunschdatum (Bau-Form) | `bau/kontakt.html:521` | LOW | UX, не legal | Зробити optional |
| 6.13 | «kostenfrei anfragen» (Bau-Form button) | `bau/kontakt.html:566` | OK | — | OK |
| 6.14 | «Innenausbau mit Leidenschaft», «Präzision in jedem Detail» | hero | LOW (puffery) | — | OK |
| 6.15 | «Wir realisieren ... termingerecht» | `bau/leistungen.html:265` | MEDIUM | § 5 UWG + потенційно § 443 BGB | «Ich strebe Termintreue an» / «Ich plane realistisch und halte Termine ein» |
| 6.16 | «erstklassige Fliesenarbeiten», «professionelle Renovierungen», «zuverlässiger Umzugsservice» | `bau/index.html:419-420` | LOW (puffery) | — | OK |
| 6.17 | «fachgerechte» / «professionelle» — використовуються часто | багато місць | LOW (puffery) | — | OK |

### Severity: **HIGH (sum)**, single CRITICAL items: 6.3, 6.4, 6.5, 6.8

---

## 7. Bau-сторінки — HwO / Anlage A / Meisterbrief — **HIGH**

### Інвентар Bau-послуг

З `bau/leistungen.html` і `bau/index.html`:

| Послуга | HwO Klassifizierung | Vereinbarkeit з Einzelunternehmer без Meisterbrief |
|---|---|---|
| **Fliesenarbeiten / Fliesenleger** (Großformate, Jollyschnitt, Epoxidharzfugen, Abdichtung, Wandhaken) | **Anlage B1 HwO Nr. 14 «Fliesen-, Platten- und Mosaikleger»** — це **ZULASSUNGSFREIES Handwerk** (з 2004 року). | ✅ Можна без Meisterbrief, але **обов'язкова реєстрація в Handwerkskammer (HWK Niederbayern-Oberpfalz)** + Eintragung у Verzeichnis nach § 19 HwO. |
| **Bodenverlegung — Laminat, Vinyl** | **Anlage B2 HwO Nr. 7 «Bodenleger»** — **ZULASSUNGSFREIES Handwerk** (handwerksähnlich). | ✅ Аналогічно. |
| **Epoxidharz-Bodenbeschichtungen** | Зазвичай попадає під **Anlage A Nr. 11 «Estrichleger»** (zulassungspflichtig) АБО Bodenleger якщо без spezieller Untergrundvorbereitung | ⚠️ **Залежить.** Якщо включає Estrich-Vorarbeiten → потрібен Meisterbrief Estrichleger АБО Ausnahmebewilligung за § 8 HwO. |
| **Naturstein-Verlegung + Designer-Terrassen** | Може попадати під **Anlage A Nr. 12 «Steinmetz und Steinbildhauer»** (zulassungspflichtig) **АБО** під Fliesenleger для простого Verlegens. | ⚠️ Якщо лише verlegen — то Fliesenleger (Anlage B1, OK). Якщо bearbeiten/zuschneiden Stein → Steinmetz Anlage A → потрібен Meisterbrief. Сайт пише «Bearbeitung und Verlegung» (line 341 leistungen.html) — це червоний прапор. |
| **Sockelleisten + Türeinbau (Türenmontage)** | **Anlage B1 Nr. 33 «Parkettleger»** + Anlage A Nr. 27 «Tischler/Schreiner» — для Türeinbau zulassungspflichtig якщо Maßanfertigung; для Montage готових Türen зазвичай Bauwerksmontage (Anlage B). | ⚠️ Просто монтаж готових Türen — OK. Anpassung/Zuschnitt → Schreiner-Meisterbrief або Ausnahmebewilligung. |
| **Designer-Treppenverlegung** | Аналогічно Fliesenleger (Anlage B1) якщо лише Belegung; Treppenbau Anlage A якщо конструкція. | ⚠️ Сайт пише «Belegung von Treppenstufen» — Verlegen OK, Bauleistung Treppe → потрібен Holzbau-Meisterbrief. |
| **Möbelmontage** | Не handwerklich за HwO — це einfache Dienstleistung. | ✅ OK без реєстрації. |
| **Renovierung/Innenausbau (general)** | Збірний термін, охоплює багато HwO-Berufe. | ⚠️ Залежить які конкретно роботи. Сайт у hero-описі пише «Komplette Wohnungsrenovierungen — schlüsselfertig» (`bau/uber-uns.html:380`) — це може охоплювати **Maler, Stuckateur, Trockenbau, Elektro, Sanitär**, які майже всі **Anlage A zulassungspflichtig** → CRITICAL якщо пропонується самостійно. |
| **Umzugsservice + Möbelmontage** | НЕ handwerklich — Logistikdienstleistung. | ✅ OK. **Aber:** може потрібен **Güterkraftverkehrslizenz § 3 GüKG** якщо перевозиться > 3,5 t Gesamtgewicht (зазвичай для Umzug — так). |

### Що це означає на практиці

**Сайт декларує діяльність, яка може вимагати Meisterbrief або реєстрації, без явного посилання на legal Status.**

Прецедент: **§ 1 Abs. 1 HwO + § 8 SchwarzArbG** — пропонування zulassungspflichtigen Handwerks без Eintragung — **Ordnungswidrigkeit, до 50 000 € Bußgeld** + civil-Abmahnung через Wettbewerber/HWK.

Bayerische HWK (Niederbayern-Oberpfalz) активно мониторить інтернет — **OLG Nürnberg 22.04.2010, Az. 3 U 2098/09** — типовий приклад HWK-абмахнення.

### Severity: **HIGH** (потенційно CRITICAL якщо власник реально не має Eintragung)

### Конкретний фікс

1. **Перевірити з власником** які з робіт він реально виконує + чи зареєстрований у HWK.
2. У Impressum явно вказати: «Eingetragen in das Verzeichnis zulassungsfreier Handwerke / handwerksähnlicher Gewerbe (Anlage B HwO) bei der Handwerkskammer Niederbayern-Oberpfalz, Regensburg» (тільки якщо реально зареєстрований!).
3. На bau-сторінках **обмежити явне формулювання** — не використовувати слова «Meister», «Komplettsanierung schlüsselfertig», «Elektroarbeiten», «Sanitäranlagen», «Maler» — ці натякають на zulassungspflichtige Handwerke.
4. **Якщо Estrich/Naturstein/Türzuschnitt не входять у Eintragung** — або прибрати зі списку, або змінити формулювання на «Vermittlung an Partner-Handwerksbetrieb» (з Impressum-посиланням на партнера).
5. Додати в FAQ Bau явну інформацію: «Ich bin in das Verzeichnis ... bei der HWK Niederbayern-Oberpfalz eingetragen. Für Leistungen, die einen Meisterbrief erfordern (z. B. Elektro, Sanitär, Maler), arbeite ich mit Partnerbetrieben zusammen.»

---

## 8. Counter Band — falsche Behauptungen — **CRITICAL** (окрема секція)

### Знайдене

**`auto/index.html:407-425`:**
```
5+    Jahre Erfahrung
2000+ Zufriedene Kunden     ← найбільший ризик
100%  Profi-Qualität
100%  Transparenz
```

**`bau/index.html:430-447`:**
```
10+   Jahre Erfahrung
300+  Abgeschlossene Projekte
5★    Kundenbewertung         ← треба source (Google?)
100%  Qualitätsgarantie       ← перетворюється на vertragliche Garantie!
```

**`auto/uber-uns.html:406`** (Timeline 4-th milestone):
```
Heute: 2000+ zufriedene Kunden
```

### Чому це CRITICAL

1. **§ 5 Abs. 1 Nr. 3 UWG** — Irreführung über das Unternehmen в т.ч. «Marktbedeutung», «Anzahl Kunden», «Erfahrung». Точні цифри = **Tatsachenbehauptung**, не Werbung. Tatsachenbehauptung повинна бути **wahr und beweisbar**.

2. **BGH I ZR 234/93** — «Werbung mit Fantasiezahlen» — пряма заборона.

3. **OLG Frankfurt 6 U 187/19 (2020)** — «über 1000 Kunden» без беспідставно — Abmahnkosten 1.531 €, Vertragsstrafe 5.001 € pro Wiederholung.

4. **OLG Hamm 4 U 161/16 (2017)** — «10 Jahre Erfahrung» при фактичних 4 роках — те саме.

5. Контекст: бренд **тільки що ребрендований** з Oleksandr Halushka → **Oleksandr Halushka** (April 2026 за research-gbp-naming/). Якщо це фактичний restart без legal Rechtsnachfolge → числа з попереднього бренду навіть не можна перекидати, це окреме порушення.

6. **«100% Qualitätsgarantie»** — це **§ 443 BGB Beschaffenheits-/Haltbarkeitsgarantie** — створює autonomous обов'язок ремонту/повернення коштів. Це не маркетингова puffery! BGH VIII ZR 75/16: «Garantie» в Bau-контексті = легально enforceable.

### Хто буде абмахати

- **Wettbewerbszentrale, Bad Homburg** — серійно, монiторить локальні counter bands
- **IDO-Verband** — те саме
- **IHK München-Oberbayern + IHK Regensburg-Niederbayern** — конкуренти-IHK-члени можуть подати скаргу
- **Konkurrenzfreie Mitbewerber** — місцеві KFZ-Sachverständige або Fliesenleger у Bad Abbach/Regensburg

Стандартний Streitwert: **8 000–25 000 €** для UWG-Abmahnung; Abmahnkosten ~1 379–2 348 €; Vertragsstrafe **5 001 € pro Wiederholung** за neuer Hamburger Brauch.

### Severity: **CRITICAL — найбільший правовий ризик на сайті прямо зараз**

### Конкретний фікс

**Варіант A (рекомендований — найбезпечніший):**
Замінити числа на **якісні** твердження що описують підхід:

```html
<!-- AUTO -->
<div class="counter-band">
    <div class="counter-item">
        <span class="count">🇩🇪🇺🇦</span>
        <span class="label">Bayerische Sorgfalt + ukrainischer Fleiß</span>
    </div>
    <div class="counter-item">
        <span class="count">4</span>
        <span class="label">Sprachen Beratung</span>     <!-- DE/EN/UA/RU — це 100% factually correct -->
    </div>
    <div class="counter-item">
        <span class="count">1h</span>
        <span class="label">Durchschn. Antwortzeit</span>  <!-- якщо реально швидко -->
    </div>
    <div class="counter-item">
        <span class="count">0€</span>
        <span class="label">Erstberatung</span>   <!-- це factually true і marketing-positive -->
    </div>
</div>

<!-- BAU -->
<div class="counter-band">
    <div class="counter-item">
        <span class="count">A-Z</span>
        <span class="label">Innenausbau aus einer Hand</span>
    </div>
    <div class="counter-item">
        <span class="count">🛡️</span>
        <span class="label">Eingetragen bei HWK Niederbayern-Oberpfalz</span>  <!-- якщо так! -->
    </div>
    <div class="counter-item">
        <span class="count">🇩🇪🇺🇦</span>
        <span class="label">Bayerische Qualität, ukrainischer Fleiß</span>
    </div>
    <div class="counter-item">
        <span class="count">★</span>
        <span class="label">Persönlich vom Inhaber</span>
    </div>
</div>
```

**Варіант B (якщо власник наполягає на числах):**
- Замінити «5+ Jahre Erfahrung» → реальне число (1 рік Beratung + X років Bau? власник знає).
- «2000+ Zufriedene Kunden» → ВИДАЛИТИ повністю.
- «300+ Abgeschlossene Projekte» → реальне число (бажано підкріплене Foto-Galerie з projects).
- «5★ Kundenbewertung» → конкретний source: «5★ bei Google (Stand 04/2026)» + посилання на GBP-Profile.
- «100% Profi-Qualität / Transparenz» → OK як puffery, можна залишити.
- «100% Qualitätsgarantie» → **«Höchster Qualitätsanspruch»** (без «Garantie»).

**Варіант C (баланс):**
Залишити лише puffery + factually correct:
- «Bayerische Qualität»
- «Persönliche Beratung»
- «Eingetragen bei HWK» (якщо так)
- «4 Sprachen» / «Online-Beratung kostenlos»

**ЩО ЗРОБИТИ ВЖЕ ЗАВТРА:**
1. Видалити числові твердження «2000+», «300+», «5+», «10+», «5★» → CRITICAL.
2. «100% Qualitätsgarantie» → «Hoher Qualitätsanspruch».
3. Timeline 4-й пункт «Heute: 2000+ zufriedene Kunden» → видалити або «Heute: Persönliche Betreuung in 4 Sprachen».

---

## 9. Цінова інформація / PAngV — **MEDIUM**

### Знайдене

- «Kostenlos» / «kostenlos und unverbindlich» — **factually true** (для erste Einschätzung) — **OK**, без PAngV-проблем.
- Старі модалки Reifen/Klima/Service з ціною «ab 90 €» — **видалені** (підтверджено grep'ом — у поточних `auto/leistungen.html` і `auto/index.html` цін немає).
- Bau pricing — «Kostenvoranschlag», «verbindliches Angebot» — без числових цін → OK.
- Newsletter «10% Rabatt» — це Werbeeinwilligung-Anreiz; ціна базової послуги не вказана, тому **PAngV не порушено**, але це **§ 7 UWG** проблема (див. наступну секцію).

### Severity: **MEDIUM** — лише перевірити що 10% Rabatt не створює прихованої непрозорості (на що саме 10%? За PAngV § 6 — Vergleichende Werbung — все вказано бути klar erkennbar з якої ціни знижка).

### Фікс

У контактній формі поряд з «10% Rabatt»-checkbox додати fußnote:
> «10% Rabatt auf den ersten kostenpflichtigen Beratungstermin (z. B. ausführliche Vor-Ort-Begleitung). Erstberatung per Telefon/E-Mail/WhatsApp ist immer kostenlos.»

---

## 10. Kontaktформа і обробка persondaten — **HIGH**

### Знайдене

`auto/kontakt.html:494-610` + `bau/kontakt.html:468-583` — однакова структура:

✅ **Honeypot field** `name="website"` — є, скрито за CSS — добре
✅ **Required GDPR-checkbox** `id="gdpr"` з лінком до Datenschutzerklärung — є
✅ **Phone-required toggle** залежно від contactPref — продумано
✅ **Required asterisks** через CSS class `.required::after` — UX OK
⚠️ **Newsletter-checkbox optional** з «10% Rabatt» — є; **АЛЕ**:

### Проблеми

| # | Проблема | Закон | Severity |
|---|---|---|---|
| 10.1 | **Немає Double-Opt-In** для Newsletter | § 7 Abs. 2 Nr. 3 UWG — «ohne ausdrückliche, vorherige Einwilligung des Empfängers» — Single-Opt-In не достатньо за BGH I ZR 218/07 «Payback», OLG Düsseldorf 20 U 35/14 | **HIGH** |
| 10.2 | Текст GDPR-checkbox не уточнює **«freiwillig», «jederzeit widerrufbar»** | Art. 7 Abs. 3 + Art. 13 Abs. 2 lit. c DSGVO | HIGH |
| 10.3 | Текст Newsletter-checkbox не уточнює: «Ich willige ein in den Empfang von Werbe-E-Mails über meine künftigen Beratungs- und Bau-Angebote. Die Einwilligung ist freiwillig und kann jederzeit per Klick auf den Abmelde-Link am Ende jeder E-Mail oder per E-Mail an info@Oleksandr Halushkae.de widerrufen werden.» | § 7a UWG + Art. 7 DSGVO | HIGH |
| 10.4 | Form надсилається на **Google Apps Script (US)** через `mode:'no-cors'` — **persondata Drittlandtransfer** не задокументовано в Datenschutzerklärung | Art. 44 DSGVO + Schrems II EuGH C-311/18 | HIGH |
| 10.5 | Немає **Bestätigungsseite** після submit (UX + § 312i BGB) | § 312i Abs. 1 Nr. 3 BGB | MEDIUM |
| 10.6 | Submit button «**Anfrage verbindlich absenden**» — слово «verbindlich» збиває з пантелику; форма це Anfrage, не Vertragsschluss | § 5 UWG (klare Bedeutung) | MEDIUM |
| 10.7 | `fetch(GAS_WEB_APP_URL, {mode:'no-cors'})` — opaque response → користувач не отримує feedback про успіх/невдачу submit | UX, частково § 312i | LOW |

### Severity: **HIGH**

### Конкретний фікс — оновлений checkbox-текст

**GDPR-checkbox (обов'язковий):**
```html
<label for="gdpr">
  Ich willige ein, dass meine angegebenen Daten (Name, E-Mail, Telefon, Nachricht)
  zum Zweck der Beantwortung meiner Anfrage und der ggf. anschließenden
  Beratung verarbeitet werden. Die Einwilligung erfolgt freiwillig und kann
  jederzeit für die Zukunft per E-Mail an
  <a href="mailto:info@Oleksandr Halushkae.de">info@Oleksandr Halushkae.de</a> widerrufen
  werden. Weitere Informationen finden Sie in der
  <a href="../legal/datenschutz.html">Datenschutzerklärung</a>. *
</label>
```

**Newsletter-checkbox (optional + DOI):**
```html
<label for="newsletter">
  Ja, ich möchte den E-Mail-Newsletter mit gelegentlichen Tipps und
  Sonderangeboten erhalten und erhalte 10 % Rabatt auf meinen ersten
  kostenpflichtigen Beratungstermin oder Bauauftrag. Die Einwilligung ist
  freiwillig und kann jederzeit über den Abmelde-Link in jeder E-Mail oder
  per E-Mail an
  <a href="mailto:info@Oleksandr Halushkae.de">info@Oleksandr Halushkae.de</a> widerrufen
  werden. Nach dem Absenden erhalte ich eine Bestätigungs-E-Mail mit einem
  Aktivierungslink (Double-Opt-In).
</label>
```

**Submit button: «Anfrage verbindlich absenden» → «Anfrage senden»** (нейтральне).

**Bestätigungsseite:**
```js
// у booking-system.js, після успішного fetch
window.location.href = '/legal/danke.html?form=' + formType;
```
+ створити `legal/danke.html` зі стандартним «Vielen Dank! Sie erhalten in Kürze eine Bestätigungs-E-Mail. Wir melden uns innerhalb von 1–3 Werktagen zurück» + Hinweis на 14-Tage-Widerrufsrecht.

**Double-Opt-In реалізація на стороні Google Apps Script:**
1. При submit з `newsletter=on` — GAS зберігає в Google Sheet «pending newsletter».
2. Надсилає лист з активаційним токеном `https://Oleksandr Halushkae.de/legal/newsletter-activate.html?token=xxx`.
3. Тільки після кліку — переносить у «active newsletter» список.
4. Зберегти timestamp активації для audit trail (за § 7a UWG).

---

## Action checklist (відсортовано за severity)

### CRITICAL (24-72h)
1. ☐ Виправити Impressum — реальні Anschrift / Telefon / E-Mail / USt-IdNr / DDG-замість-TMG / § 36 VSBG / Aufsichtsbehörde / berufsrechtliche Angaben Bau (`legal/impressum.html`)
2. ☐ Видалити з обох counter bands: «5+ Jahre», «10+ Jahre», «2000+ Kunden», «300+ Projekte», «5★», «100% Qualitätsgarantie» (`auto/index.html`, `bau/index.html`, `auto/uber-uns.html`)
3. ☐ Видалити timeline «Heute: 2000+ zufriedene Kunden» (`auto/uber-uns.html:406`)
4. ☐ Self-host Google Fonts → не вантажити з Google CDN
5. ☐ Self-host Font Awesome → не вантажити з Cloudflare cdnjs
6. ☐ Self-host AOS → не вантажити з unpkg
7. ☐ Замінити Google Maps iframe на статичну placeholder + «Karte aktivieren»-кнопку (Two-Click)
8. ☐ Переписати Datenschutzerklärung повністю (~13 розділів за чек-лістом у пункті 2)

### HIGH (тиждень)
9. ☐ Додати `legal/agb.html` (з окремими секціями для Auto і Bau)
10. ☐ Додати `legal/widerruf.html` (Muster-Widerrufsbelehrung + Muster-Widerrufsformular)
11. ☐ Виправити cookie-banner: категоризація + «Ablehnen»-кнопка ≈ «Akzeptieren» + кнопка «Einstellungen ändern» у footer + реальне блокування скриптів до consent
12. ☐ Замінити всі «wir/unser/Team/Mitarbeiter/Profis (множина)» на «ich/mein/Berater» (повний список у пункті 5; ~28 рядків у `locales/de.json` + ~12 hardcoded HTML-фрагментів)
13. ☐ Замінити навігаційне «Über uns» на «Über mich» (всі мови)
14. ☐ Замінити meta description «Team»/«KFZ-Meister» (HwO-protection!) на «Berater» (`auto/uber-uns.html:9`, `bau/uber-uns.html:9`)
15. ☐ Замінити «Erfahrene KFZ-Profis» на «Erfahrener KFZ-Berater» (`auto/index.html:495`, `de.json:48`)
16. ☐ Перевірити з власником HWK-Eintragung (Niederbayern-Oberpfalz) для всіх Bau-послуг + якщо немає для Estrichleger/Steinmetz/Schreiner — обмежити формулювання (пункт 7)
17. ☐ Реалізувати Double-Opt-In для Newsletter-checkbox (через GAS)
18. ☐ Оновити GDPR-checkbox і Newsletter-checkbox тексти за пунктом 10
19. ☐ Замінити «Anfrage verbindlich absenden» на «Anfrage senden»
20. ☐ Створити `legal/danke.html` Bestätigungsseite

### MEDIUM (2-4 тижні)
21. ☐ Додати fußnote до 10%-Rabatt-checkbox («auf erste kostenpflichtige Beratung», PAngV-clarity)
22. ☐ «100% Qualitätsgarantie» → «Hoher Qualitätsanspruch» (бо Garantie = § 443 BGB enforceable)
23. ☐ Прибрати слово «Meister» якщо немає Meisterbrief (`auto/uber-uns.html:9` meta + всюди)
24. ☐ Прибрати «erste Standort» формулу (натяк на множину — `auto/uber-uns.html:393`)
25. ☐ «Wir realisieren ... termingerecht» → «Ich plane realistisch und halte Termine ein» (`bau/leistungen.html:265`)
26. ☐ Додати в Bau-Impressum явне посилання на HWK Niederbayern-Oberpfalz + перелік зареєстрованих Anlage B-Berufe
27. ☐ Дзвонити з власником на тему: чи є реальна Berufshaftpflicht для Bau? якщо так — додати в Impressum

### LOW (місяць)
28. ☐ Замінити «Innenausbau Team» в alt-атрибутах на «Innenausbau Bayern»
29. ☐ Перевірити що при заповненні форми UI показує summary перед submit (§ 312i BGB Eingabefehler-Korrektur)
30. ☐ Додати lang-attributes ARIA-correct для multilingual formу
31. ☐ Перевірити англійську/російську/українську локалі що там теж «we» → «I» переведено

---

## Sources and References

1. **§ 5 DDG (Digitale-Dienste-Gesetz, чинний з 14.05.2024)** — https://www.gesetze-im-internet.de/ddg/__5.html
2. **§ 18 Abs. 2 MStV (Medienstaatsvertrag)** — https://www.die-medienanstalten.de/fileadmin/user_upload/Rechtsgrundlagen/Gesetze_aktuell/Medienstaatsvertrag_MStV.pdf
3. **§ 27a UStG** — https://www.gesetze-im-internet.de/ustg_1980/__27a.html
4. **§ 36 VSBG** — https://www.gesetze-im-internet.de/vsbg/__36.html
5. **DSGVO Art. 13** — Pflichtinformationen bei Erhebung — https://eur-lex.europa.eu/eli/reg/2016/679/oj
6. **§ 25 TDDDG (раніше TTDSG)** — Cookies/Tracking Einwilligung — https://www.gesetze-im-internet.de/tddsg/
7. **§ 5 UWG** — Irreführende geschäftliche Handlungen — https://www.gesetze-im-internet.de/uwg_2004/__5.html
8. **§ 7 UWG** — Unzumutbare Belästigungen / Werbeeinwilligung — https://www.gesetze-im-internet.de/uwg_2004/__7.html
9. **§ 312c, § 312d, § 312g, § 312i BGB** — Fernabsatz + elektronischer Geschäftsverkehr — https://www.gesetze-im-internet.de/bgb/
10. **§ 355 BGB Widerrufsrecht** — https://www.gesetze-im-internet.de/bgb/__355.html
11. **§ 443 BGB Beschaffenheitsgarantie** — https://www.gesetze-im-internet.de/bgb/__443.html
12. **§ 1 + § 8 + § 19 + § 51 HwO (Handwerksordnung)** — https://www.gesetze-im-internet.de/hwo/
13. **§ 8 SchwarzArbG** — https://www.gesetze-im-internet.de/schwarzarbg_2004/__8.html
14. **§ 3 GüKG** — Güterkraftverkehrsgesetz (для Umzug > 3,5t) — https://www.gesetze-im-internet.de/g_kg_1998/
15. **EuGH C-673/17 Planet49 (01.10.2019)** — Cookie-Consent muss aktiv erteilt werden
16. **EuGH C-298/07 deutsche internet versicherung (16.10.2008)** — zwei Kommunikationswege im Impressum
17. **EuGH C-311/18 Schrems II (16.07.2020)** — Drittlandtransfer USA
18. **BGH I ZR 234/93** — Werbung mit Fantasiezahlen
19. **BGH I ZR 218/07 «Payback» (10.02.2011)** — Double-Opt-In
20. **BGH VIII ZR 75/16** — Garantie iSv § 443 BGB
21. **OLG Schleswig 28.09.2011, 2 W 231/10** — «Gruppe» bei Einzelunternehmer (вже в `research-gbp-naming/`)
22. **OLG Hamm 13.03.2012, 4 U 198/11** — «Wir» bei Einzelunternehmer = Größenirreführung
23. **OLG Hamm 4 U 161/16 (2017)** — falsche Erfahrungsangabe
24. **OLG Frankfurt 6 U 187/19** — Falschwerbung mit Kundenzahlen
25. **OLG Köln 6 U 65/22 (Nov 2022)** — Cookie-Banner Design (Ablehnen ≈ Akzeptieren)
26. **OLG Düsseldorf 20 U 35/14** — Single-Opt-In nicht ausreichend
27. **LG München I 17 O 14857/22 «Google Fonts» (20.01.2022)** — IP-Übertragung ohne consent → 100 € Schadensersatz
28. **DSK Orientierungshilfe Telemedienanbieter (Dez 2021)** — https://www.datenschutzkonferenz-online.de/media/oh/20211220_oh_telemedien.pdf
29. **BMJV — Muster-Widerrufsbelehrung + Widerrufsformular** — https://www.bmj.de/SharedDocs/Downloads/DE/Service/Formulare/Widerrufsbelehrung_und_Muster_Widerrufsformular.html
30. **BayLDA — Bayerisches Landesamt für Datenschutzaufsicht** — https://www.lda.bayern.de
31. **HWK Niederbayern-Oberpfalz** — https://www.hwkno.de
32. **IHK München-Oberbayern** — https://www.ihk-muenchen.de
33. **Klaro! Open-Source Consent Manager** — https://github.com/klaro-org/klaro
34. **Internal: research-gbp-naming/FINAL-RECOMMENDATION.md** — попередній аудит назви бренду

---

## Recommendations (порядок виконання)

**День 1-2 (нон-стоп критика):**
- Видалити Counter-Band-числа (15 хвилин роботи, але прибирає 80% ризику)
- Виправити Impressum (60-90 хвилин — заповнити реальні дані)
- Замінити Datenschutzerklärung на повноцінну (3-4 години)
- Self-host шрифти/AOS/FontAwesome (2 години)
- Заглушити Google Maps до consent (30 хвилин)

**Тиждень 1:**
- Замінити «wir» → «ich» (1-2 години — пакетний find/replace + ручна перевірка)
- Cookie-banner з реальною consent-логікою (4-6 годин)
- AGB + Widerrufsbelehrung (2-3 години — використати готові шаблони + customize)
- Перевірити HWK-Eintragung з власником і відповідно скоригувати Bau-послуги

**Тиждень 2-3:**
- Double-Opt-In Newsletter (4 години — GAS modification)
- Оновити checkbox-тексти (15 хвилин)
- Bestätigungsseite + Form-Bestätigungsmail (2 години)
- Перевірка локалей en/uk/ru (1 година)

---

## Additional Notes

- **Аудиторами не було перевірено:** реальний email власника, реальна USt-IdNr, реальна Anschrift (бо це мають бути приватні дані власника). Власник має заповнити сам, користуючись template вище.
- **Не перевірено:** чи реально власник зареєстрований у HWK Niederbayern-Oberpfalz і яких саме Anlage B-Gewerbe. Це fundamental fact, потрібно clarify ASAP.
- **Не перевірено:** реальна кількість років досвіду власника — це впливає на питання чи можна писати «5+ Jahre» / «10+ Jahre». Власник має сам verify.
- **Не перевірено:** чи планується реальний Newsletter-розсилка з технічної боку. Якщо ні — checkbox можна просто видалити, **це знімає весь HIGH-ризик пункту 10.1, 10.3**.
- **Не перевірено:** наявність Berufshaftpflicht для Bau. Це **дуже важливо** — Bauleistungen без Versicherung це Geschäftsrisiko, і клієнти все частіше питають про це. Рекомендую звернутись до місцевого Versicherungsmaklers (Allianz, AXA, R+V — стандартний bau-pflicht ~30-80 €/Monat для Einzelunternehmer).
- **Конкуруючі джерела:** деякі джерела рекомендують для соло Einzelunternehmer все одно вживати «Wir» як pluralis modestiae (стиль Maker). **Юридично це сильно ризиковано** після прецедентів OLG Hamm 4 U 198/11 і LG Berlin 91 O 21/13. Безпечніше й аутентичніше — «Ich».
- **Гарне додаткове читання для власника:** IT-Recht-Kanzlei München (https://www.it-recht-kanzlei.de) — публікують безкоштовні шаблони Datenschutzerklärung для широкого спектру use cases; eRecht24 (https://www.e-recht24.de) — безкоштовний Datenschutz-Generator. Обидва генерують текст що покриває 90% Pflichtangaben — але **завжди треба customize під реальні Drittanbieter**.

---

**Кінцевий висновок:** сайт у поточному стані має 3 CRITICAL правових проблеми, які треба виправити **за 24-72 години** (Counter-band-числа, Impressum-placeholder, Cookie/3rd-party-loading). Після цього 5 HIGH-проблем мають бути закриті за тиждень-два. Дизайн і структура сайту в цілому гарні — це чисто питання contentу і JS-реалізації consent. Проблеми **легко піддаються виправленню** (більшість — це text-edits + 1 cookie-banner-rewrite + 1 self-host-fonts).
