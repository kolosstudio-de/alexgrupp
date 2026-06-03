import base64

def get_b64(path):
    with open(path, 'rb') as f:
        return base64.b64encode(f.read()).decode('utf-8')

# Load the base64 assets
black_logo = get_b64('assets/logo-black-sig.png')
white_logo = get_b64('assets/logo-white-sig.png')
black_sig = get_b64('assets/extracted-real-black.png')
white_sig = get_b64('assets/extracted-real-white.png')

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
    .instruction {{
      font-family: Arial, sans-serif;
      font-size: 12px;
      color: #999;
      margin-top: 10px;
      line-height: 1.5;
    }}
  </style>
</head>
<body>

  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 1 — AUTO (Dark / Blue)               -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">📌 Signatur 1 — AUTO (Fahrzeugberatung)</div>

    <!-- COPY FROM HERE -->
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #0f0f0f; border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid rgba(255,255,255,0.05);">
      <tr>
        <td style="padding: 24px;">
          <!-- Main Content Block (Single Column) -->
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <!-- Header part: Name & Logo on Right -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <td style="vertical-align: top;">
                      <div style="font-size: 20px; font-weight: 800; color: #ffffff; letter-spacing: -0.4px; line-height: 1.2;">Oleksandr Halushka</div>
                      <div style="font-size: 10px; color: #3b7dd8; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;">Kfz-Kaufberatung · Bayern</div>
                      <div style="font-size: 9px; color: rgba(255,255,255,0.3); margin-top: 2px;">Einzelunternehmer</div>
                    </td>
                    <td style="vertical-align: top; text-align: right; width: 40px; padding-left: 10px;">
                      <img src="data:image/png;base64,{white_logo}" width="30" height="39" alt="OH Logo" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>

                <!-- Divider Line -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; margin-top: 12px; margin-bottom: 12px;">
                  <tr>
                    <td style="border-top: 1px solid rgba(255,255,255,0.07); height: 1px;"></td>
                  </tr>
                </table>

                <!-- Contacts & Signature side-by-side -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <!-- Contacts (Left - Width increased to 330px to prevent Bad Abbach wrapping) -->
                    <td style="vertical-align: top; width: 330px;">
                      <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Telefon</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="tel:+4916093409671" style="color: #ffffff; text-decoration: none; font-size: 12px; font-weight: 500;">+49 160 9340 9671</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">WhatsApp</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://wa.me/4916093409671" style="color: #3b7dd8; text-decoration: none; font-size: 12px; font-weight: 500;">Nachricht senden →</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">E-Mail</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="mailto:info@oleksandrhalushka.de" style="color: #ffffff; text-decoration: none; font-size: 12px; font-weight: 500;">info@oleksandrhalushka.de</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Adresse</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; color: rgba(255,255,255,0.6); font-size: 12px; white-space: nowrap;">Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach</td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 0; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Instagram</td>
                          <td style="vertical-align: middle; padding-bottom: 0; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color: rgba(255,255,255,0.5); text-decoration: none; font-size: 12px;">@oleksandrhalushka.auto</a>
                          </td>
                        </tr>
                      </table>
                    </td>

                    <!-- Handwritten Signature (Right) -->
                    <td style="vertical-align: bottom; text-align: right; padding-left: 10px; padding-bottom: 2px;">
                      <img src="data:image/png;base64,{white_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="background: #0a0a0a; padding: 10px 24px; border-top: 1px solid rgba(255,255,255,0.05);">
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <a href="https://www.oleksandrhalushka.de" style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 11px;">www.oleksandrhalushka.de</a>
              </td>
              <td style="text-align: right;">
                <a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color: rgba(255,255,255,0.25); text-decoration: none; font-size: 11px;">Impressum</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <!-- COPY TO HERE -->

    <div class="instruction">👆 Выдели блок выше → скопируй → вставь в Gmail (Signatur 1 «Auto»)</div>
  </div>


  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 2 — BAU (Light / Amber)              -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">🔨 Signatur 2 — BAU (Innenausbau)</div>

    <!-- COPY FROM HERE -->
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #ffffff; border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid #e2e8f0;">
      <tr>
        <td style="padding: 24px;">
          <!-- Main Content Block (Single Column) -->
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <!-- Header part: Name & Logo on Right -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <td style="vertical-align: top;">
                      <div style="font-size: 20px; font-weight: 800; color: #0f172a; letter-spacing: -0.4px; line-height: 1.2;">Oleksandr Halushka</div>
                      <div style="font-size: 10px; color: #d97706; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;">Innenausbau & Fliesenarbeiten · Bayern</div>
                      <div style="font-size: 9px; color: #94a3b8; margin-top: 2px;">Einzelunternehmer</div>
                    </td>
                    <td style="vertical-align: top; text-align: right; width: 40px; padding-left: 10px;">
                      <img src="data:image/png;base64,{black_logo}" width="30" height="39" alt="OH Logo" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>

                <!-- Divider Line -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; margin-top: 12px; margin-bottom: 12px;">
                  <tr>
                    <td style="border-top: 1px solid #e2e8f0; height: 1px;"></td>
                  </tr>
                </table>

                <!-- Contacts & Signature side-by-side -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <!-- Contacts (Left - Width increased to 330px to prevent Bad Abbach wrapping) -->
                    <td style="vertical-align: top; width: 330px;">
                      <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Telefon</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="tel:+4916093409671" style="color: #0f172a; text-decoration: none; font-size: 12px; font-weight: 500;">+49 160 9340 9671</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">WhatsApp</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://wa.me/4916093409671" style="color: #d97706; text-decoration: none; font-size: 12px; font-weight: 500;">Nachricht senden →</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">E-Mail</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="mailto:info@oleksandrhalushka.de" style="color: #0f172a; text-decoration: none; font-size: 12px; font-weight: 500;">info@oleksandrhalushka.de</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Adresse</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; color: #475569; font-size: 12px; white-space: nowrap;">Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach</td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 0; font-size: 9px; color: #94a3b8; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Instagram</td>
                          <td style="vertical-align: middle; padding-bottom: 0; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://www.instagram.com/oleksandrhalushka.bau/" style="color: #94a3b8; text-decoration: none; font-size: 12px;">@oleksandrhalushka.bau</a>
                          </td>
                        </tr>
                      </table>
                    </td>

                    <!-- Handwritten Signature (Right) -->
                    <td style="vertical-align: bottom; text-align: right; padding-left: 10px; padding-bottom: 2px;">
                      <img src="data:image/png;base64,{black_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="background: #f8fafc; padding: 10px 24px; border-top: 1px solid #e2e8f0;">
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <a href="https://www.oleksandrhalushka.de" style="color: #64748b; text-decoration: none; font-size: 11px;">www.oleksandrhalushka.de</a>
              </td>
              <td style="text-align: right;">
                <a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color: #94a3b8; text-decoration: none; font-size: 11px;">Impressum</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <!-- COPY TO HERE -->

    <div class="instruction">👆 Выдели блок выше → скопируй → вставь в Gmail (Signatur 2 «Bau»)</div>
  </div>


  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 3 — UNIVERSAL (Neutral / Dark)       -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">💼 Signatur 3 — UNIVERSAL (Allgemein)</div>

    <!-- COPY FROM HERE -->
    <table cellpadding="0" cellspacing="0" border="0" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #0f0f0f; border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid rgba(255,255,255,0.05);">
      <tr>
        <td style="padding: 24px;">
          <!-- Main Content Block (Single Column) -->
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <!-- Header part: Name & Logo on Right -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <td style="vertical-align: top;">
                      <div style="font-size: 20px; font-weight: 800; color: #ffffff; letter-spacing: -0.4px; line-height: 1.2;">Oleksandr Halushka</div>
                      <div style="font-size: 10px; color: #94a3b8; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;">Fahrzeugberatung & Innenausbau · Bayern</div>
                      <div style="font-size: 9px; color: rgba(255,255,255,0.3); margin-top: 2px;">Einzelunternehmer</div>
                    </td>
                    <td style="vertical-align: top; text-align: right; width: 40px; padding-left: 10px;">
                      <img src="data:image/png;base64,{white_logo}" width="30" height="39" alt="OH Logo" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>

                <!-- Divider Line -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%; margin-top: 12px; margin-bottom: 12px;">
                  <tr>
                    <td style="border-top: 1px solid rgba(255,255,255,0.07); height: 1px;"></td>
                  </tr>
                </table>

                <!-- Contacts & Signature side-by-side -->
                <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                  <tr>
                    <!-- Contacts (Left - Width increased to 330px to prevent Bad Abbach wrapping) -->
                    <td style="vertical-align: top; width: 330px;">
                      <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Telefon</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="tel:+4916093409671" style="color: #ffffff; text-decoration: none; font-size: 12px; font-weight: 500;">+49 160 9340 9671</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">WhatsApp</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://wa.me/4916093409671" style="color: #94a3b8; text-decoration: none; font-size: 12px; font-weight: 500;">Nachricht senden →</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">E-Mail</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="mailto:info@oleksandrhalushka.de" style="color: #ffffff; text-decoration: none; font-size: 12px; font-weight: 500;">info@oleksandrhalushka.de</a>
                          </td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Adresse</td>
                          <td style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; color: rgba(255,255,255,0.6); font-size: 12px; white-space: nowrap;">Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach</td>
                        </tr>
                        <tr>
                          <td style="vertical-align: middle; width: 78px; padding-bottom: 0; font-size: 9px; color: rgba(255,255,255,0.3); letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px;">Instagram</td>
                          <td style="vertical-align: middle; padding-bottom: 0; font-family: Arial, sans-serif; line-height: 16px;">
                            <a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color: rgba(255,255,255,0.5); text-decoration: none; font-size: 12px;">@oleksandrhalushka.auto</a>
                          </td>
                        </tr>
                      </table>
                    </td>

                    <!-- Handwritten Signature (Right) -->
                    <td style="vertical-align: bottom; text-align: right; padding-left: 10px; padding-bottom: 2px;">
                      <img src="data:image/png;base64,{white_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                    </td>
                  </tr>
                </table>
              </td>
            </tr>
          </table>
        </td>
      </tr>
      <tr>
        <td style="background: #0a0a0a; padding: 10px 24px; border-top: 1px solid rgba(255,255,255,0.05);">
          <table cellpadding="0" cellspacing="0" border="0" style="width: 100%;">
            <tr>
              <td>
                <a href="https://www.oleksandrhalushka.de" style="color: rgba(255,255,255,0.4); text-decoration: none; font-size: 11px;">www.oleksandrhalushka.de</a>
              </td>
              <td style="text-align: right;">
                <a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color: rgba(255,255,255,0.25); text-decoration: none; font-size: 11px;">Impressum</a>
              </td>
            </tr>
          </table>
        </td>
      </tr>
    </table>
    <!-- COPY TO HERE -->

    <div class="instruction">👆 Выдели блок выше → скопируй → вставь в Gmail (Signatur 3 «Allgemein»)</div>
  </div>

</body>
</html>
"""

with open('email-signatures.html', 'w') as f:
    f.write(html)

print('email-signatures.html successfully regenerated in final layout with fixed Bad Abbach wrapping!')
