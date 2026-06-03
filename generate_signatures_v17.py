# ─────────────────────────────────────────────────────────────
# generate_signatures_v17.py
# Modern, spacious Inline-flow layout with a vertical colored divider line
# Works perfectly in light & dark mode, desktop & mobile
# ─────────────────────────────────────────────────────────────

# Permanent CDN assets (Catbox) - High-res, correct mapping
logo_blue    = 'https://files.catbox.moe/aln5jw.png'  # clean circular blue monogram logo (OH)
logo_amber   = 'https://files.catbox.moe/x31v8f.png'  # clean circular amber monogram logo (OH)
logo_slate   = 'https://files.catbox.moe/5mkatp.png'  # clean circular slate monogram logo (OH)
sig_outlined = 'https://files.catbox.moe/05gl5o.png'  # real handwritten signature (O. Halushka) with soft 5px glow

# ── Shared contact data ────────────────────────────────────────
PHONE    = '+49 160 9340 9671'
WA_URL   = 'https://wa.me/4916093409671'
EMAIL    = 'info@oleksandrhalushka.de'
ADDRESS  = 'Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach'
IG_AUTO  = 'https://www.instagram.com/oleksandrhalushka.auto/'
IG_BAU   = 'https://www.instagram.com/oleksandrhalushka.bau/'
SITE     = 'https://www.oleksandrhalushka.de'
IMPRESSUM= 'https://www.oleksandrhalushka.de/legal/impressum.html'

# ── Helper: builds the contacts table ─────────────────────────
def row(label, value_html, label_color, pb='6px'):
    return f'''  <tr>
    <td style="vertical-align:middle;width:78px;padding-bottom:{pb};font-size:9px;color:{label_color};letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;">{label}</td>
    <td style="vertical-align:middle;padding-bottom:{pb};font-family:Arial,sans-serif;line-height:16px;">{value_html}</td>
  </tr>'''

def link(href, text, color):
    return f'<a href="{href}" style="color:{color};text-decoration:none;font-size:12px;font-weight:500;">{text}</a>'

def iglink(href, handle, color):
    return f'<a href="{href}" style="color:{color};text-decoration:none;font-size:12px;">{handle}</a>'

# ── Card builder ───────────────────────────────────────────────
def card(card_id, subtitle, title_accent, wa_color, ig_rows_html, logo_url,
         border_color='#e2e8f0', label_color='#64748b', value_color='#334155'):
    # Pure transparent, extremely responsive and dark-mode friendly HTML structure
    # Standard-width 520px fits perfectly in every desktop/mobile screen
    return f'''<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;max-width:520px;width:100%;border:0;" id="{card_id}">
  <tr>
    <!-- LEFT: Circular Logo Monogram Badge -->
    <td style="vertical-align:top;width:44px;padding-right:18px;text-align:center;">
      <img src="{logo_url}" width="44" alt="OH Monogram Logo" style="display:inline-block;border:0;width:44px;height:auto;" />
    </td>

    <!-- RIGHT: Content Area with Vertical Divider Line -->
    <td style="vertical-align:top;border-left:2px solid {title_accent};padding-left:20px;">
      
      <!-- Name and Subtitle Block -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
        <tr>
          <td style="vertical-align:top;padding-bottom:10px;">
            <div style="font-size:20px;font-weight:800;color:#0f172a;letter-spacing:-0.4px;line-height:1.2;">Oleksandr Halushka</div>
            <div style="font-size:10px;color:{title_accent};font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:4px;">{subtitle}</div>
            <div style="font-size:9px;color:#94a3b8;margin-top:2px;">Einzelunternehmer</div>
          </td>
        </tr>
      </table>

      <!-- Horizontal divider between header and contacts -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-bottom:10px;">
        <tr>
          <td style="border-top:1px solid {border_color};height:1px;"></td>
        </tr>
      </table>

      <!-- Contacts Block & Cursive Signature side-by-side -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
        <tr>
          <!-- Contacts details (left side of content) -->
          <td style="vertical-align:top;width:310px;">
            <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
{row('Telefon',  link(f'tel:+4916093409671', PHONE, '#0f172a'), label_color)}
{row('WhatsApp', link(WA_URL, 'Nachricht senden →', wa_color), label_color)}
{row('E-Mail',   link(f'mailto:{EMAIL}', EMAIL, '#0f172a'), label_color)}
{row('Adresse',  f'<span style="color:{value_color};font-size:12px;">{ADDRESS}</span>', label_color)}
{ig_rows_html}
            </table>
          </td>
          
          <!-- Signature Image (right side of content) -->
          <td style="vertical-align:bottom;text-align:right;padding-left:10px;padding-bottom:2px;width:75px;">
            <img src="{sig_outlined}" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;height:42px;width:auto;" />
          </td>
        </tr>
      </table>

      <!-- Horizontal divider before footer -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:10px;margin-bottom:8px;">
        <tr>
          <td style="border-top:1px solid {border_color};height:1px;"></td>
        </tr>
      </table>

      <!-- Footer Info -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
        <tr>
          <td>
            <a href="{SITE}" style="color:#64748b;text-decoration:none;font-size:11px;">www.oleksandrhalushka.de</a>
          </td>
          <td style="text-align:right;">
            <a href="{IMPRESSUM}" style="color:#94a3b8;text-decoration:none;font-size:11px;">Impressum</a>
          </td>
        </tr>
      </table>

    </td>
  </tr>
</table>'''

# ── Instagram row helper ───────────────────────────────────────
def ig_row(href, handle, color, pb='6px'):
    return row('Instagram', iglink(href, handle, color), '#94a3b8', pb)

# ─────────────────────────────────────────────────────────────
# Build all three signatures
# ─────────────────────────────────────────────────────────────

# 1. AUTO — blue accent
ig_auto_only = ig_row(IG_AUTO, '@oleksandrhalushka.auto', '#3b7dd8', pb='0')

sig_auto = card(
    card_id='sig-auto-table',
    subtitle='Kfz-Kaufberatung · Bayern',
    title_accent='#3b7dd8',
    wa_color='#3b7dd8',
    ig_rows_html=ig_auto_only,
    logo_url=logo_blue,
    border_color='#cbd5e1',
)

# 2. BAU — amber accent
ig_bau_only = ig_row(IG_BAU, '@oleksandrhalushka.bau', '#d97706', pb='0')

sig_bau = card(
    card_id='sig-bau-table',
    subtitle='Innenausbau &amp; Fliesenarbeiten · Bayern',
    title_accent='#d97706',
    wa_color='#d97706',
    ig_rows_html=ig_bau_only,
    logo_url=logo_amber,
    border_color='#f59e0b',
)

# 3. UNIVERSAL — slate accent, both instagrams
ig_both = (
    ig_row(IG_AUTO, '@oleksandrhalushka.auto', '#3b7dd8', pb='6px') +
    '\n' +
    ig_row(IG_BAU,  '@oleksandrhalushka.bau',  '#d97706', pb='0')
)

sig_univ = card(
    card_id='sig-univ-table',
    subtitle='Fahrzeugberatung &amp; Innenausbau · Bayern',
    title_accent='#64748b',
    wa_color='#64748b',
    ig_rows_html=ig_both,
    logo_url=logo_slate,
    border_color='#cbd5e1',
)

# ─────────────────────────────────────────────────────────────
# HTML wrapper page with side-by-side Light / Dark previews
# ─────────────────────────────────────────────────────────────
html = f"""<!DOCTYPE html>
<html lang="de">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Email Signaturen — Oleksandr Halushka</title>
  <style>
    body {{
      font-family: Arial, Helvetica, sans-serif;
      background: #f8fafc;
      padding: 40px;
      display: flex;
      flex-direction: column;
      gap: 60px;
      max-width: 1200px;
      margin: 0 auto;
      color: #0f172a;
    }}
    .header {{
      text-align: center;
      margin-bottom: 20px;
    }}
    .header h1 {{
      font-size: 28px;
      font-weight: 800;
      color: #1e293b;
      margin: 0 0 8px 0;
    }}
    .header p {{
      font-size: 15px;
      color: #64748b;
      margin: 0;
    }}
    .signature-section {{
      background: white;
      border-radius: 12px;
      padding: 30px;
      box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
      border: 1px solid #e2e8f0;
    }}
    .label {{
      font-family: Arial, sans-serif;
      font-size: 14px;
      font-weight: 800;
      color: #334155;
      margin-bottom: 20px;
      text-transform: uppercase;
      letter-spacing: 1.5px;
      display: flex;
      align-items: center;
      gap: 8px;
      border-bottom: 2px solid #e2e8f0;
      padding-bottom: 10px;
    }}
    .preview-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 30px;
      margin-bottom: 20px;
    }}
    @media (max-width: 900px) {{
      .preview-grid {{
        grid-template-columns: 1fr;
      }}
    }}
    .preview-box {{
      border-radius: 8px;
      padding: 24px;
      border: 1px solid #e2e8f0;
      display: flex;
      justify-content: center;
      align-items: center;
    }}
    .preview-box.light {{
      background: #ffffff;
    }}
    .preview-box.dark {{
      background: #151515;
    }}
    
    /* ── Precise simulated dark mode style overrides ── */
    .preview-box.dark td[style*="border-left"] {{
      border-color: #3b82f6 !important; /* blue */
    }}
    .preview-box.dark #sig-bau-table td[style*="border-left"] {{
      border-color: #d97706 !important; /* amber */
    }}
    .preview-box.dark #sig-univ-table td[style*="border-left"] {{
      border-color: #64748b !important; /* slate */
    }}
    
    .preview-box.dark td[style*="border-top"] {{
      border-color: #334155 !important;
    }}
    .preview-box.dark table tr td table tr td a[style*="color:#0f172a"] {{
      color: #f1f5f9 !important;
    }}
    .preview-box.dark table tr td table tr td div[style*="color:#0f172a"] {{
      color: #ffffff !important;
    }}
    .preview-box.dark table tr td table tr td span[style*="color:#334155"] {{
      color: #cbd5e1 !important;
    }}
    .preview-box.dark table tr td table tr td div[style*="color:#94a3b8"] {{
      color: #64748b !important;
    }}
    .preview-box.dark table tr td a[style*="color:#64748b"] {{
      color: #94a3b8 !important;
    }}
    .preview-box.dark table tr td a[style*="color:#94a3b8"] {{
      color: #475569 !important;
    }}

    .preview-title {{
      font-size: 11px;
      font-weight: bold;
      text-transform: uppercase;
      letter-spacing: 1px;
      color: #94a3b8;
      margin-bottom: 8px;
    }}
    .copy-btn {{
      background: #3b7dd8;
      color: white;
      border: none;
      padding: 12px 24px;
      font-size: 14px;
      font-weight: bold;
      border-radius: 6px;
      cursor: pointer;
      display: inline-flex;
      align-items: center;
      gap: 8px;
      transition: background 0.2s, transform 0.1s;
      font-family: Arial, sans-serif;
      box-shadow: 0 4px 6px rgba(0,0,0,0.1);
    }}
    .copy-btn:hover {{ background: #2b63b0; }}
    .copy-btn:active {{ transform: scale(0.98); }}
    .copy-btn.bau-btn {{ background: #d97706; }}
    .copy-btn.bau-btn:hover {{ background: #b45309; }}
    .copy-btn.univ-btn {{ background: #475569; }}
    .copy-btn.univ-btn:hover {{ background: #334155; }}
  </style>
  <script>
    function copySignature(tableId) {{
      var table = document.getElementById(tableId);
      var htmlBlob = new Blob([table.outerHTML], {{ type: 'text/html' }});
      var textBlob = new Blob([table.innerText], {{ type: 'text/plain' }});
      navigator.clipboard.write([new ClipboardItem({{
        'text/html': htmlBlob,
        'text/plain': textBlob
      }})]).then(function() {{
        alert("Подпись скопирована! Вставьте в Gmail (Cmd+V / Ctrl+V).");
      }}).catch(function() {{
        alert("Ошибка копирования. Выделите карточку вручную и скопируйте.");
      }});
    }}
  </script>
</head>
<body>

  <div class="header">
    <h1>Email Signaturen — Oleksandr Halushka</h1>
    <p>Свободный стиль (Inline-flow Layout) с вертикальным разделителем брендов</p>
  </div>

  <!-- SIGNATURE 1 — AUTO -->
  <div class="signature-section">
    <div class="label">🔵 Signatur 1 — AUTO (Kfz-Kaufberatung)</div>
    <div class="preview-grid">
      <div>
        <div class="preview-title">☀️ Light Mode Preview</div>
        <div class="preview-box light">
          {sig_auto}
        </div>
      </div>
      <div>
        <div class="preview-title">🌙 Dark Mode Simulation</div>
        <div class="preview-box dark">
          {sig_auto}
        </div>
      </div>
    </div>
    <button class="copy-btn" onclick="copySignature('sig-auto-table')">
      <span>📋</span> Скопировать подпись для Gmail
    </button>
  </div>

  <!-- SIGNATURE 2 — BAU -->
  <div class="signature-section">
    <div class="label">🔶 Signatur 2 — BAU (Innenausbau)</div>
    <div class="preview-grid">
      <div>
        <div class="preview-title">☀️ Light Mode Preview</div>
        <div class="preview-box light">
          {sig_bau}
        </div>
      </div>
      <div>
        <div class="preview-title">🌙 Dark Mode Simulation</div>
        <div class="preview-box dark">
          {sig_bau}
        </div>
      </div>
    </div>
    <button class="copy-btn bau-btn" onclick="copySignature('sig-bau-table')">
      <span>🔨</span> Скопировать подпись для Gmail
    </button>
  </div>

  <!-- SIGNATURE 3 — UNIVERSAL -->
  <div class="signature-section">
    <div class="label">💼 Signatur 3 — UNIVERSAL (Allgemein)</div>
    <div class="preview-grid">
      <div>
        <div class="preview-title">☀️ Light Mode Preview</div>
        <div class="preview-box light">
          {sig_univ}
        </div>
      </div>
      <div>
        <div class="preview-title">🌙 Dark Mode Simulation</div>
        <div class="preview-box dark">
          {sig_univ}
        </div>
      </div>
    </div>
    <button class="copy-btn univ-btn" onclick="copySignature('sig-univ-table')">
      <span>💼</span> Скопировать подпись для Gmail
    </button>
  </div>

</body>
</html>
"""

with open('email-signatures.html', 'w') as f:
    f.write(html)

print('email-signatures.html v17 — compiled successfully!')
