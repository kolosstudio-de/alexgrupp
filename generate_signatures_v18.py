# ─────────────────────────────────────────────────────────────
# generate_signatures_v18.py
# Modern, ultra-wide Horizontal Stretched Signature (Stripe Style)
# Beautiful vertical split, full-width design spanning 680px!
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

def link(href, text, color):
    return f'<a href="{href}" style="color:{color};text-decoration:none;font-weight:500;">{text}</a>'

def iglink(href, handle, color):
    return f'<a href="{href}" style="color:{color};text-decoration:none;">{handle}</a>'

# ── Card builder ───────────────────────────────────────────────
def card(card_id, subtitle, title_accent, wa_color, ig_html, logo_url,
         border_color='#cbd5e1', label_color='#64748b', value_color='#334155'):
    # Luxuriously stretched horizontal signature spanning 680px!
    # Spans elements horizontally in a wide grid with a full-width divider line.
    return f'''<table cellpadding="0" cellspacing="0" border="0" style="font-family:Arial,Helvetica,sans-serif;font-size:12px;line-height:1.5;max-width:680px;width:100%;border:0;" id="{card_id}">
  <tr>
    <td style="padding:10px 0;">
      
      <!-- TOP: Horizontal grid containing Logo, Name, Divider, Contacts, and Signature -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;">
        <tr>
          <!-- 1. Circular Monogram Logo (Left-aligned) -->
          <td style="vertical-align:middle;width:44px;padding-right:16px;">
            <img src="{logo_url}" width="44" alt="OH Monogram Logo" style="display:inline-block;border:0;width:44px;height:auto;" />
          </td>

          <!-- 2. Name & Title Block -->
          <td style="vertical-align:middle;padding-right:20px;min-width:150px;white-space:nowrap;">
            <div style="font-size:18px;font-weight:800;color:#0f172a;letter-spacing:-0.4px;line-height:1.2;">Oleksandr Halushka</div>
            <div style="font-size:9px;color:{title_accent};font-weight:700;letter-spacing:1px;text-transform:uppercase;margin-top:3px;">{subtitle}</div>
            <div style="font-size:9px;color:#94a3b8;margin-top:1px;">Einzelunternehmer</div>
          </td>

          <!-- 3. Elegant Vertical Divider Line -->
          <td style="vertical-align:middle;width:1px;border-left:1px solid {border_color};padding-left:20px;"></td>

          <!-- 4. Contacts in a Wide, Compact Table -->
          <td style="vertical-align:middle;">
            <table cellpadding="0" cellspacing="0" border="0" style="width:100%;font-size:11px;line-height:15px;color:{value_color};">
              <tr>
                <td style="padding-bottom:3px;white-space:nowrap;padding-right:15px;">
                  <span style="color:{label_color};text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Tel:</span>&nbsp;&nbsp;{link(f'tel:+4916093409671', PHONE, '#0f172a')}
                </td>
                <td style="padding-bottom:3px;white-space:nowrap;">
                  <span style="color:{label_color};text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">WhatsApp:</span>&nbsp;&nbsp;{link(WA_URL, 'Nachricht senden →', wa_color)}
                </td>
              </tr>
              <tr>
                <td style="padding-bottom:3px;white-space:nowrap;padding-right:15px;">
                  <span style="color:{label_color};text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Mail:</span>&nbsp;&nbsp;{link(f'mailto:{EMAIL}', EMAIL, '#0f172a')}
                </td>
                <td style="padding-bottom:3px;">
                  <span style="color:{label_color};text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Adr:</span>&nbsp;&nbsp;<span style="color:{value_color};">{ADDRESS}</span>
                </td>
              </tr>
              {ig_html}
            </table>
          </td>

          <!-- 5. Real Handwritten Signature (Right-aligned) -->
          <td style="vertical-align:middle;text-align:right;padding-left:16px;width:75px;">
            <img src="{sig_outlined}" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;height:42px;width:auto;" />
          </td>
        </tr>
      </table>

      <!-- MIDDLE: Full-width horizontal divider stretching 100% of 680px! -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;margin-top:12px;margin-bottom:8px;">
        <tr>
          <td style="border-top:1px solid {border_color};height:1px;"></td>
        </tr>
      </table>

      <!-- BOTTOM: Footer Links stretching cleanly -->
      <table cellpadding="0" cellspacing="0" border="0" style="width:100%;font-size:10px;">
        <tr>
          <td style="color:#64748b;">
            <a href="{SITE}" style="color:#64748b;text-decoration:none;font-weight:bold;">www.oleksandrhalushka.de</a>
          </td>
          <td style="text-align:right;color:#94a3b8;">
            <a href="{IMPRESSUM}" style="color:#94a3b8;text-decoration:none;">Impressum</a>
          </td>
        </tr>
      </table>

    </td>
  </tr>
</table>'''

# ─────────────────────────────────────────────────────────────
# Build all three signatures
# ─────────────────────────────────────────────────────────────

# 1. AUTO — blue accent
ig_auto_html = f'''<tr>
  <td colspan="2" style="padding-bottom:0;white-space:nowrap;">
    <span style="color:#94a3b8;text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Instagram:</span>&nbsp;&nbsp;{iglink(IG_AUTO, '@oleksandrhalushka.auto', '#3b7dd8')}
  </td>
</tr>'''

sig_auto = card(
    card_id='sig-auto-table',
    subtitle='Kfz-Kaufberatung · Bayern',
    title_accent='#3b7dd8',
    wa_color='#3b7dd8',
    ig_html=ig_auto_html,
    logo_url=logo_blue,
    border_color='#cbd5e1',
)

# 2. BAU — amber accent
ig_bau_html = f'''<tr>
  <td colspan="2" style="padding-bottom:0;white-space:nowrap;">
    <span style="color:#94a3b8;text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Instagram:</span>&nbsp;&nbsp;{iglink(IG_BAU, '@oleksandrhalushka.bau', '#d97706')}
  </td>
</tr>'''

sig_bau = card(
    card_id='sig-bau-table',
    subtitle='Innenausbau &amp; Fliesenarbeiten · Bayern',
    title_accent='#d97706',
    wa_color='#d97706',
    ig_html=ig_bau_html,
    logo_url=logo_amber,
    border_color='#f59e0b',
)

# 3. UNIVERSAL — slate accent, both instagrams side-by-side
ig_univ_html = f'''<tr>
  <td style="padding-bottom:0;white-space:nowrap;padding-right:15px;">
    <span style="color:#94a3b8;text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Instagram Auto:</span>&nbsp;&nbsp;{iglink(IG_AUTO, '@oleksandrhalushka.auto', '#3b7dd8')}
  </td>
  <td style="padding-bottom:0;white-space:nowrap;">
    <span style="color:#94a3b8;text-transform:uppercase;font-size:8px;letter-spacing:0.5px;">Instagram Bau:</span>&nbsp;&nbsp;{iglink(IG_BAU, '@oleksandrhalushka.bau', '#d97706')}
  </td>
</tr>'''

sig_univ = card(
    card_id='sig-univ-table',
    subtitle='Fahrzeugberatung &amp; Innenausbau · Bayern',
    title_accent='#64748b',
    wa_color='#64748b',
    ig_html=ig_univ_html,
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
      max-width: 1400px;
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
      grid-template-columns: 1fr;
      gap: 30px;
      margin-bottom: 20px;
    }}
    .preview-box {{
      border-radius: 8px;
      padding: 24px;
      border: 1px solid #e2e8f0;
      display: flex;
      justify-content: center;
      align-items: center;
      overflow-x: auto;
    }}
    .preview-box.light {{
      background: #ffffff;
    }}
    .preview-box.dark {{
      background: #151515;
    }}
    
    /* ── Precise simulated dark mode style overrides ── */
    .preview-box.dark td[style*="border-left"] {{
      border-color: #334155 !important;
    }}
    .preview-box.dark td[style*="border-top"] {{
      border-color: #334155 !important;
    }}
    .preview-box.dark table tr td a[style*="color:#0f172a"] {{
      color: #f1f5f9 !important;
    }}
    .preview-box.dark table tr td div[style*="color:#0f172a"] {{
      color: #ffffff !important;
    }}
    .preview-box.dark table tr td span[style*="color:#334155"] {{
      color: #cbd5e1 !important;
    }}
    .preview-box.dark table tr td span[style*="color:#0f172a"] {{
      color: #f1f5f9 !important;
    }}
    .preview-box.dark table tr td div[style*="color:#94a3b8"] {{
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
    <p>Ультра-широкий горизонтальный стиль (Horizontal Stretched Layout) — 680px Stripe-Style</p>
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

print('email-signatures.html v18 — ultra-wide compiled successfully!')
