# ─────────────────────────────────────────────────────────────
# generate_signatures_v13.py
# Three WHITE signatures — works on every mail client, any mode
# ─────────────────────────────────────────────────────────────

# Permanent CDN assets (Catbox)
black_logo = 'https://files.catbox.moe/r9vk5r.png'   # dark icon — works on white
black_sig  = 'https://files.catbox.moe/8qnrz6.png'   # cursive ink — works on white

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
def contacts(rows_html, label_color, bg):
    return f'''<table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;background-color:{bg};">
{rows_html}
</table>'''

def row(label, value_html, label_color, bg, pb='6px'):
    return f'''  <tr>
    <td bgcolor="{bg}" style="vertical-align:middle;width:78px;padding-bottom:{pb};font-size:9px;color:{label_color};letter-spacing:1px;text-transform:uppercase;font-family:Arial,sans-serif;line-height:16px;background-color:{bg};">{label}</td>
    <td bgcolor="{bg}" style="vertical-align:middle;padding-bottom:{pb};font-family:Arial,sans-serif;line-height:16px;background-color:{bg};">{value_html}</td>
  </tr>'''

def link(href, text, color):
    return f'<a href="{href}" style="color:{color}!important;text-decoration:none;font-size:12px;font-weight:500;">{text}</a>'

def iglink(href, handle, color):
    return f'<a href="{href}" style="color:{color}!important;text-decoration:none;font-size:12px;">{handle}</a>'

# ── Card builder ───────────────────────────────────────────────
def card(card_id, subtitle, title_accent, wa_color, ig_rows_html,
         border_color='#e2e8f0',
         bg='#ffffff', footer_bg='#f8fafc',
         label_color='#94a3b8', address_color='#475569',
         footer_text_color='#64748b', footer_dim_color='#94a3b8'):
    return f'''<table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="font-family:Arial,Helvetica,sans-serif;font-size:13px;line-height:1.5;background:{bg};background-image:linear-gradient({bg},{bg});border-radius:10px;overflow:hidden;max-width:540px;width:100%;border:1px solid {border_color};" id="{card_id}">
  <tr>
    <td bgcolor="{bg}" style="padding:24px;background-color:{bg};background-image:linear-gradient({bg},{bg});">
      <table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;background-color:{bg};">
        <tr>
          <td bgcolor="{bg}" style="background-color:{bg};">

            <!-- NAME + LOGO -->
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;background-color:{bg};">
              <tr>
                <td bgcolor="{bg}" style="vertical-align:top;background-color:{bg};">
                  <div style="font-size:20px;font-weight:800;color:#0f172a!important;letter-spacing:-0.4px;line-height:1.2;" data-ogsc="color:#0f172a;">Oleksandr Halushka</div>
                  <div style="font-size:10px;color:{title_accent}!important;font-weight:600;letter-spacing:1px;text-transform:uppercase;margin-top:4px;" data-ogsc="color:{title_accent};">{subtitle}</div>
                  <div style="font-size:9px;color:#94a3b8!important;margin-top:2px;" data-ogsc="color:#94a3b8;">Einzelunternehmer</div>
                </td>
                <td bgcolor="{bg}" style="vertical-align:top;text-align:right;width:45px;padding-left:10px;background-color:{bg};">
                  <img src="{black_logo}" width="34" height="44" alt="OH Logo" style="display:inline-block;border:0;" />
                </td>
              </tr>
            </table>

            <!-- DIVIDER -->
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;margin-top:12px;margin-bottom:12px;background-color:{bg};">
              <tr>
                <td bgcolor="{bg}" style="border-top:1px solid {border_color};height:1px;background-color:{bg};"></td>
              </tr>
            </table>

            <!-- CONTACTS + HANDWRITTEN SIG -->
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;background-color:{bg};">
              <tr>
                <td bgcolor="{bg}" style="vertical-align:top;width:330px;background-color:{bg};">
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="{bg}" style="width:100%;background-color:{bg};">
{row('Telefon',  link(f'tel:+4916093409671', PHONE, '#0f172a'), label_color, bg)}
{row('WhatsApp', link(WA_URL, 'Nachricht senden →', wa_color), label_color, bg)}
{row('E-Mail',   link(f'mailto:{EMAIL}', EMAIL, '#0f172a'), label_color, bg)}
{row('Adresse',  f'<span style="color:{address_color}!important;font-size:12px;" data-ogsc="color:{address_color};">{ADDRESS}</span>', label_color, bg)}
{ig_rows_html}
                  </table>
                </td>
                <td bgcolor="{bg}" style="vertical-align:bottom;text-align:right;padding-left:10px;padding-bottom:2px;background-color:{bg};">
                  <img src="{black_sig}" height="42" alt="Handwritten Signature" style="display:inline-block;border:0;" />
                </td>
              </tr>
            </table>

          </td>
        </tr>
      </table>
    </td>
  </tr>

  <!-- FOOTER -->
  <tr>
    <td bgcolor="{footer_bg}" style="background:{footer_bg};background-image:linear-gradient({footer_bg},{footer_bg});padding:10px 24px;border-top:1px solid {border_color};">
      <table cellpadding="0" cellspacing="0" border="0" bgcolor="{footer_bg}" style="width:100%;background-color:{footer_bg};">
        <tr>
          <td bgcolor="{footer_bg}" style="background-color:{footer_bg};">
            <a href="{SITE}" style="color:{footer_text_color}!important;text-decoration:none;font-size:11px;" data-ogsc="color:{footer_text_color};">www.oleksandrhalushka.de</a>
          </td>
          <td bgcolor="{footer_bg}" style="text-align:right;background-color:{footer_bg};">
            <a href="{IMPRESSUM}" style="color:{footer_dim_color}!important;text-decoration:none;font-size:11px;" data-ogsc="color:{footer_dim_color};">Impressum</a>
          </td>
        </tr>
      </table>
    </td>
  </tr>
</table>'''

# ── Instagram row helper ───────────────────────────────────────
def ig_row(href, handle, color, bg, pb='6px'):
    return row('Instagram', iglink(href, handle, color), '#94a3b8', bg, pb)

# ─────────────────────────────────────────────────────────────
# Build all three signatures
# ─────────────────────────────────────────────────────────────

# 1. AUTO — blue accent
ig_auto_only = ig_row(IG_AUTO, '@oleksandrhalushka.auto', '#94a3b8', '#ffffff', pb='0')

sig_auto = card(
    card_id='sig-auto-table',
    subtitle='Kfz-Kaufberatung · Bayern',
    title_accent='#3b7dd8',
    wa_color='#3b7dd8',
    ig_rows_html=ig_auto_only,
    border_color='#e2e8f0',
)

# 2. BAU — amber accent
ig_bau_only = ig_row(IG_BAU, '@oleksandrhalushka.bau', '#94a3b8', '#ffffff', pb='0')

sig_bau = card(
    card_id='sig-bau-table',
    subtitle='Innenausbau &amp; Fliesenarbeiten · Bayern',
    title_accent='#d97706',
    wa_color='#d97706',
    ig_rows_html=ig_bau_only,
    border_color='#fde68a',
)

# 3. UNIVERSAL — slate accent, both instagrams
ig_both = (
    ig_row(IG_AUTO, '@oleksandrhalushka.auto', '#94a3b8', '#ffffff', pb='6px') +
    '\n' +
    ig_row(IG_BAU,  '@oleksandrhalushka.bau',  '#94a3b8', '#ffffff', pb='0')
)

sig_univ = card(
    card_id='sig-univ-table',
    subtitle='Fahrzeugberatung &amp; Innenausbau · Bayern',
    title_accent='#64748b',
    wa_color='#64748b',
    ig_rows_html=ig_both,
    border_color='#e2e8f0',
)

# ─────────────────────────────────────────────────────────────
# HTML wrapper page
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
      background: #f0f0f0;
      padding: 40px;
      display: flex;
      flex-direction: column;
      gap: 60px;
      max-width: 700px;
      margin: 0 auto;
    }}
    .label {{
      font-family: Arial, sans-serif;
      font-size: 13px;
      font-weight: bold;
      color: #666;
      margin-bottom: 12px;
      text-transform: uppercase;
      letter-spacing: 2px;
    }}
    .copy-btn {{
      background: #3b7dd8;
      color: white;
      border: none;
      padding: 12px 24px;
      font-size: 13px;
      font-weight: bold;
      border-radius: 6px;
      cursor: pointer;
      margin-top: 15px;
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

  <!-- SIGNATURE 1 — AUTO -->
  <div>
    <div class="label">📌 Signatur 1 — AUTO (Kfz-Kaufberatung)</div>
    <div style="display:block;">
      <!-- COPY FROM HERE -->
      {sig_auto}
      <!-- COPY TO HERE -->
    </div>
    <button class="copy-btn" onclick="copySignature('sig-auto-table')">
      <span>📋</span> Скопировать подпись для Gmail
    </button>
  </div>

  <!-- SIGNATURE 2 — BAU -->
  <div>
    <div class="label">🔨 Signatur 2 — BAU (Innenausbau)</div>
    <div style="display:block;">
      <!-- COPY FROM HERE -->
      {sig_bau}
      <!-- COPY TO HERE -->
    </div>
    <button class="copy-btn bau-btn" onclick="copySignature('sig-bau-table')">
      <span>🔨</span> Скопировать подпись для Gmail
    </button>
  </div>

  <!-- SIGNATURE 3 — UNIVERSAL -->
  <div>
    <div class="label">💼 Signatur 3 — UNIVERSAL (Allgemein)</div>
    <div style="display:block;">
      <!-- COPY FROM HERE -->
      {sig_univ}
      <!-- COPY TO HERE -->
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

print('email-signatures.html v13 — three white signatures — generated successfully!')
