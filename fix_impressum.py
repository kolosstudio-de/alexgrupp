import os

filepath = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами/legal/impressum.html"
with open(filepath, "r", encoding="utf-8") as f:
    content = f.read()

replacements = [
    ("Unsere E-Mail-Adresse", "Meine E-Mail-Adresse"),
    ("Wir sind nicht bereit oder verpflichtet", "Ich bin nicht bereit oder verpflichtet"),
    ("Als Diensteanbieter sind wir gemäß", "Als Diensteanbieter bin ich gemäß"),
    ("Nach §§ 8 bis 10 TMG sind wir", "Nach §§ 8 bis 10 TMG bin ich"),
    ("Unser Angebot enthält Links", "Mein Angebot enthält Links"),
    ("auf deren Inhalte wir keinen Einfluss haben", "auf deren Inhalte ich keinen Einfluss habe"),
    ("können wir für diese fremden", "kann ich für diese fremden")
]

for old_str, new_str in replacements:
    content = content.replace(old_str, new_str)

with open(filepath, "w", encoding="utf-8") as f:
    f.write(content)

print("Updated impressum.html")
