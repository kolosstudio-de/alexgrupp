# Direct permanent CDN links for the signature assets (hosted on Catbox permanent CDN)
white_logo = 'https://files.catbox.moe/wk8vd5.png'
black_logo = 'https://files.catbox.moe/r9vk5r.png'
white_sig = 'https://files.catbox.moe/3aiesg.png'
black_sig = 'https://files.catbox.moe/8qnrz6.png'

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
      box-shadow: 0 4px 6px rgba(0,0,0,0.05);
    }}
    .copy-btn:hover {{
      background: #2b63b0;
    }}
    .copy-btn:active {{
      transform: scale(0.98);
    }}
    .copy-btn.bau-btn {{
      background: #d97706;
    }}
    .copy-btn.bau-btn:hover {{
      background: #b45309;
    }}
  </style>
  <script>
    function copySignature(tableId) {{
      var table = document.getElementById(tableId);
      var html = table.outerHTML;
      var text = table.innerText;
      
      // Use the modern rich-text Clipboard API to copy HTML safely
      var htmlBlob = new Blob([html], {{ type: 'text/html' }});
      var textBlob = new Blob([text], {{ type: 'text/plain' }});
      
      var data = [new ClipboardItem({{
        'text/html': htmlBlob,
        'text/plain': textBlob
      }})];
      
      navigator.clipboard.write(data).then(function() {{
        alert("Подпись успешно скопирована! Перейдите в настройки Gmail, поставьте курсор в поле подписи и нажмите 'Вставить' (Cmd+V / Ctrl+V)");
      }}).catch(function(err) {{
        alert("Не удалось скопировать автоматически. Пожалуйста, попробуйте выделить карточку вручную.");
      }});
    }}
  </script>
</head>
<body>

  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 1 — AUTO (Dark / Blue)               -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">📌 Signatur 1 — AUTO (Fahrzeugberatung)</div>

    <div style="display: block;">
      <!-- COPY FROM HERE -->
      <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #0f0f0f; background-image: linear-gradient(#0f0f0f, #0f0f0f); border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid rgba(255,255,255,0.05);" id="sig-auto-table">
        <tr>
          <td bgcolor="#0f0f0f" style="padding: 24px; background-image: linear-gradient(#0f0f0f, #0f0f0f); background-color: #0f0f0f;">
            <!-- Main Content Block (Single Column) -->
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
              <tr>
                <td bgcolor="#0f0f0f" style="background-color: #0f0f0f;">
                  <!-- Header part: Name & Logo on Right -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                    <tr>
                      <td bgcolor="#0f0f0f" style="vertical-align: top; background-color: #0f0f0f;">
                        <div style="font-size: 20px; font-weight: 800; color: #ffffff !important; letter-spacing: -0.4px; line-height: 1.2;" data-ogsc="color: #ffffff;">Oleksandr Halushka</div>
                        <div style="font-size: 10px; color: #3b7dd8 !important; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;" data-ogsc="color: #3b7dd8;">Kfz-Kaufberatung · Bayern</div>
                        <div style="font-size: 9px; color: rgba(255,255,255,0.3) !important; margin-top: 2px;" data-ogsc="color: rgba(255,255,255,0.3);">Einzelunternehmer</div>
                      </td>
                      <td bgcolor="#0f0f0f" style="vertical-align: top; text-align: right; width: 45px; padding-left: 10px; background-color: #0f0f0f;">
                        <img src="{white_logo}" width="34" height="44" alt="OH Logo" style="display: inline-block; border: 0;" />
                      </td>
                    </tr>
                  </table>

                  <!-- Divider Line -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; margin-top: 12px; margin-bottom: 12px; background-color: #0f0f0f;">
                    <tr>
                      <td bgcolor="#0f0f0f" style="border-top: 1px solid rgba(255,255,255,0.07); height: 1px; background-color: #0f0f0f;"></td>
                    </tr>
                  </table>

                  <!-- Contacts & Signature side-by-side -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                    <tr>
                      <!-- Contacts (Left - Width increased to 330px to prevent Bad Abbach wrapping) -->
                      <td bgcolor="#0f0f0f" style="vertical-align: top; width: 330px; background-color: #0f0f0f;">
                        <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Telefon</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="tel:+4916093409671" style="color: #ffffff !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #ffffff;">+49 160 9340 9671</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">WhatsApp</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="https://wa.me/4916093409671" style="color: #3b7dd8 !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #3b7dd8;">Nachricht senden →</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">E-Mail</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="mailto:info@oleksandrhalushka.de" style="color: #ffffff !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #ffffff;">info@oleksandrhalushka.de</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Adresse</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; color: rgba(255,255,255,0.6) !important; font-size: 12px; white-space: nowrap; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.6);">Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach</td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 0; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Instagram</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 0; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color: rgba(255,255,255,0.5) !important; text-decoration: none; font-size: 12px;" data-ogsc="color: rgba(255,255,255,0.5);">@oleksandrhalushka.auto</a>
                            </td>
                          </tr>
                        </table>
                      </td>

                      <!-- Handwritten Signature (Right) -->
                      <td bgcolor="#0f0f0f" style="vertical-align: bottom; text-align: right; padding-left: 10px; padding-bottom: 2px; background-color: #0f0f0f;">
                        <img src="{white_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td bgcolor="#0a0a0a" style="background: #0a0a0a; background-image: linear-gradient(#0a0a0a, #0a0a0a); padding: 10px 24px; border-top: 1px solid rgba(255,255,255,0.05);">
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0a0a0a" style="width: 100%; background-color: #0a0a0a;">
              <tr>
                <td bgcolor="#0a0a0a" style="background-color: #0a0a0a;">
                  <a href="https://www.oleksandrhalushka.de" style="color: rgba(255,255,255,0.4) !important; text-decoration: none; font-size: 11px;" data-ogsc="color: rgba(255,255,255,0.4);">www.oleksandrhalushka.de</a>
                </td>
                <td bgcolor="#0a0a0a" style="text-align: right; background-color: #0a0a0a;">
                  <a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color: rgba(255,255,255,0.25) !important; text-decoration: none; font-size: 11px;" data-ogsc="color: rgba(255,255,255,0.25);">Impressum</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <!-- COPY TO HERE -->
    </div>

    <button class="copy-btn" onclick="copySignature('sig-auto-table')">
      <span>📋</span> Скопировать подпись для Gmail
    </button>
  </div>


  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 2 — BAU (Light / Amber)              -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">🔨 Signatur 2 — BAU (Innenausbau)</div>

    <div style="display: block;">
      <!-- COPY FROM HERE -->
      <table cellpadding="0" cellspacing="0" border="0" bgcolor="#ffffff" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #ffffff; background-image: linear-gradient(#ffffff, #ffffff); border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid #e2e8f0;" id="sig-bau-table">
        <tr>
          <td bgcolor="#ffffff" style="padding: 24px; background-image: linear-gradient(#ffffff, #ffffff);">
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
                      <td style="vertical-align: top; text-align: right; width: 45px; padding-left: 10px;">
                        <img src="{black_logo}" width="34" height="44" alt="OH Logo" style="display: inline-block; border: 0;" />
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
                        <img src="{black_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td bgcolor="#f8fafc" style="background: #f8fafc; background-image: linear-gradient(#f8fafc, #f8fafc); padding: 10px 24px; border-top: 1px solid #e2e8f0;">
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
    </div>

    <button class="copy-btn bau-btn" onclick="copySignature('sig-bau-table')">
      <span>🔨</span> Скопировать подпись для Gmail
    </button>
  </div>


  <!-- ═══════════════════════════════════════════════ -->
  <!-- SIGNATURE 3 — UNIVERSAL (Neutral / Dark)       -->
  <!-- ═══════════════════════════════════════════════ -->
  <div>
    <div class="label">💼 Signatur 3 — UNIVERSAL (Allgemein)</div>

    <div style="display: block;">
      <!-- COPY FROM HERE -->
      <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="font-family: Arial, Helvetica, sans-serif; font-size: 13px; line-height: 1.5; background: #0f0f0f; background-image: linear-gradient(#0f0f0f, #0f0f0f); border-radius: 10px; overflow: hidden; max-width: 540px; width: 100%; border: 1px solid rgba(255,255,255,0.05);" id="sig-univ-table">
        <tr>
          <td bgcolor="#0f0f0f" style="padding: 24px; background-image: linear-gradient(#0f0f0f, #0f0f0f); background-color: #0f0f0f;">
            <!-- Main Content Block (Single Column) -->
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
              <tr>
                <td bgcolor="#0f0f0f" style="background-color: #0f0f0f;">
                  <!-- Header part: Name & Logo on Right -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                    <tr>
                      <td bgcolor="#0f0f0f" style="vertical-align: top; background-color: #0f0f0f;">
                        <div style="font-size: 20px; font-weight: 800; color: #ffffff !important; letter-spacing: -0.4px; line-height: 1.2;" data-ogsc="color: #ffffff;">Oleksandr Halushka</div>
                        <div style="font-size: 10px; color: #94a3b8 !important; font-weight: 600; letter-spacing: 1px; text-transform: uppercase; margin-top: 4px;" data-ogsc="color: #94a3b8;">Fahrzeugberatung & Innenausbau · Bayern</div>
                        <div style="font-size: 9px; color: rgba(255,255,255,0.3) !important; margin-top: 2px;" data-ogsc="color: rgba(255,255,255,0.3);">Einzelunternehmer</div>
                      </td>
                      <td bgcolor="#0f0f0f" style="vertical-align: top; text-align: right; width: 45px; padding-left: 10px; background-color: #0f0f0f;">
                        <img src="{white_logo}" width="34" height="44" alt="OH Logo" style="display: inline-block; border: 0;" />
                      </td>
                    </tr>
                  </table>

                  <!-- Divider Line -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; margin-top: 12px; margin-bottom: 12px; background-color: #0f0f0f;">
                    <tr>
                      <td bgcolor="#0f0f0f" style="border-top: 1px solid rgba(255,255,255,0.07); height: 1px; background-color: #0f0f0f;"></td>
                    </tr>
                  </table>

                  <!-- Contacts & Signature side-by-side -->
                  <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                    <tr>
                      <!-- Contacts (Left - Width increased to 330px to prevent Bad Abbach wrapping) -->
                      <td bgcolor="#0f0f0f" style="vertical-align: top; width: 330px; background-color: #0f0f0f;">
                        <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0f0f0f" style="width: 100%; background-color: #0f0f0f;">
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Telefon</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="tel:+4916093409671" style="color: #ffffff !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #ffffff;">+49 160 9340 9671</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">WhatsApp</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="https://wa.me/4916093409671" style="color: #94a3b8 !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #94a3b8;">Nachricht senden →</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">E-Mail</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="mailto:info@oleksandrhalushka.de" style="color: #ffffff !important; text-decoration: none; font-size: 12px; font-weight: 500;" data-ogsc="color: #ffffff;">info@oleksandrhalushka.de</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Adresse</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; color: rgba(255,255,255,0.6) !important; font-size: 12px; white-space: nowrap; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.6);">Industriestraße 22, 93077&nbsp;Bad&nbsp;Abbach</td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 6px; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Instagram</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 6px; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="https://www.instagram.com/oleksandrhalushka.auto/" style="color: rgba(255,255,255,0.5) !important; text-decoration: none; font-size: 12px;" data-ogsc="color: rgba(255,255,255,0.5);">@oleksandrhalushka.auto</a>
                            </td>
                          </tr>
                          <tr>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; width: 78px; padding-bottom: 0; font-size: 9px; color: rgba(255,255,255,0.3) !important; letter-spacing: 1px; text-transform: uppercase; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;" data-ogsc="color: rgba(255,255,255,0.3);">Instagram</td>
                            <td bgcolor="#0f0f0f" style="vertical-align: middle; padding-bottom: 0; font-family: Arial, sans-serif; line-height: 16px; background-color: #0f0f0f;">
                              <a href="https://www.instagram.com/oleksandrhalushka.bau/" style="color: rgba(255,255,255,0.5) !important; text-decoration: none; font-size: 12px;" data-ogsc="color: rgba(255,255,255,0.5);">@oleksandrhalushka.bau</a>
                            </td>
                          </tr>
                        </table>
                      </td>

                      <!-- Handwritten Signature (Right) -->
                      <td bgcolor="#0f0f0f" style="vertical-align: bottom; text-align: right; padding-left: 10px; padding-bottom: 2px; background-color: #0f0f0f;">
                        <img src="{white_sig}" height="42" alt="Handwritten Signature" style="display: inline-block; border: 0;" />
                      </td>
                    </tr>
                  </table>
                </td>
              </tr>
            </table>
          </td>
        </tr>
        <tr>
          <td bgcolor="#0a0a0a" style="background: #0a0a0a; background-image: linear-gradient(#0a0a0a, #0a0a0a); padding: 10px 24px; border-top: 1px solid rgba(255,255,255,0.05);">
            <table cellpadding="0" cellspacing="0" border="0" bgcolor="#0a0a0a" style="width: 100%; background-color: #0a0a0a;">
              <tr>
                <td bgcolor="#0a0a0a" style="background-color: #0a0a0a;">
                  <a href="https://www.oleksandrhalushka.de" style="color: rgba(255,255,255,0.4) !important; text-decoration: none; font-size: 11px;" data-ogsc="color: rgba(255,255,255,0.4);">www.oleksandrhalushka.de</a>
                </td>
                <td bgcolor="#0a0a0a" style="text-align: right; background-color: #0a0a0a;">
                  <a href="https://www.oleksandrhalushka.de/legal/impressum.html" style="color: rgba(255,255,255,0.25) !important; text-decoration: none; font-size: 11px;" data-ogsc="color: rgba(255,255,255,0.25);">Impressum</a>
                </td>
              </tr>
            </table>
          </td>
        </tr>
      </table>
      <!-- COPY TO HERE -->
    </div>

    <button class="copy-btn" onclick="copySignature('sig-univ-table')">
      <span>💼</span> Скопировать подпись для Gmail
    </button>
  </div>

</body>
</html>
"""

with open('email-signatures.html', 'w') as f:
    f.write(html)

print('email-signatures.html successfully regenerated in final compatible version!')
