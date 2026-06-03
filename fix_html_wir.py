import os

replacements = {
    "bau/uber-uns.html": [
        ('content="Lernen Sie das Bau-Team von Oleksandr Halushka kennen — erfahrene Handwerker mit Leidenschaft für Details."',
         'content="Lernen Sie Oleksandr Halushka kennen — Handwerker für Innenausbau in Bayern."'),
        ('Erfahren Sie mehr über die Vision und das Team von Oleksandr Halushka',
         'Erfahren Sie mehr über die Arbeitsweise von Oleksandr Halushka'),
        ('alt="Oleksandr Halushka · Innenausbau Team"',
         'alt="Oleksandr Halushka · Innenausbau in Bayern"'),
        ('Unser Team aus erfahrenen Fliesenlegern, Renovierungsspezialisten und Umzugshelfern',
         'In meiner Arbeit verbinde ich Fliesenarbeiten, Renovierungen und Umzugsservice'),
        ('Als ukrainisches Team mit bayerischem Qualitätsanspruch legen wir größten Wert',
         'Als gebürtiger Ukrainer mit bayerischem Qualitätsanspruch lege ich größten Wert'),
        ('Wir legen Wert auf jede Fliese', 'Ich lege Wert auf jede Fliese'),
        ('Wir informieren Sie über den Fortschritt', 'Ich informiere Sie über den Fortschritt'),
        ('Wir kommen, wenn wir sagen, dass wir kommen. Und wir liefern, was wir versprechen.',
         'Ich komme, wenn ich es sage. Und ich liefere, was ich verspreche.'),
        ('Über uns', 'Über mich')
    ],
    "bau/index.html": [
        ('Wir liefern Ergebnisse', 'Ich liefere Ergebnisse'),
        ('Wir schützen Ihre Einrichtung', 'Ich schütze Ihre Einrichtung'),
        ('300+</h4>', 'Qualität</h4>'),
        ('Abgeschlossene Projekte', 'Zufriedene Kunden in Bayern'),
        ('10+</h4>', 'Tag 1</h4>'),
        ('Jahre Erfahrung', 'Persönliche Betreuung'),
        ('5★</h4>', '100%</h4>'),
        ('Kundenbewertung', 'Positive Rückmeldungen'),
        ('100%</h4>', 'Hoher</h4>'),
        ('Qualitätsgarantie', 'Qualitätsanspruch'),
        ('Über uns', 'Über mich')
    ],
    "bau/leistungen.html": [
        ('wir realisieren Ihr Projekt termingerecht', 'ich realisiere Ihr Projekt termingerecht'),
        ('Über uns', 'Über mich')
    ],
    "bau/kontakt.html": [
        ('Wir antworten innerhalb von einer Stunde', 'Ich antworte innerhalb von einer Stunde'),
        ('wir erstellen Ihnen ein kostenloses Angebot', 'ich erstelle Ihnen ein kostenloses Angebot'),
        ('sind für uns selbstverständlich', 'sind für mich selbstverständlich'),
        ('Wir arbeiten sowohl mit Festpreisen', 'Ich arbeite sowohl mit Festpreisen'),
        ('Ja, wir verlegen Fliesen', 'Ja, ich verlege Fliesen'),
        ('Über uns', 'Über mich')
    ],
    "auto/uber-uns.html": [
        ('content="Lernen Sie das Team von Oleksandr Halushka kennen — erfahrene KFZ-Meister',
         'content="Lernen Sie Oleksandr Halushka kennen — erfahrener Berater für Kauf und Verkauf'),
        ('alt="Beratungsteam Oleksandr Halushka"', 'alt="Oleksandr Halushka — KFZ-Berater in Bayern"'),
        ('2000+</h4>', 'Fokus</h4>'),
        ('Zufriedene Kunden', 'Zufriedene Kunden in Bayern'),
        ('Über uns', 'Über mich')
    ],
    "auto/index.html": [
        ('5+</h4>', 'Tag 1</h4>'),
        ('Jahre Erfahrung', 'Persönliche Betreuung'),
        ('2000+</h4>', 'Zufriedenheit</h4>'),
        ('Zufriedene Kunden', 'Kunden in ganz Bayern'),
        ('Erfahrene KFZ-Profis', 'Erfahrener KFZ-Berater'),
        ('Über uns', 'Über mich')
    ],
    "auto/leistungen.html": [
        ('Über uns', 'Über mich')
    ],
    "auto/kontakt.html": [
        ('Über uns', 'Über mich')
    ],
    "index.html": [
        ('Über uns', 'Über mich')
    ]
}

for filepath, reps in replacements.items():
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for old_s, new_s in reps:
            content = content.replace(old_s, new_s)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {filepath}")
    else:
        print(f"File {filepath} not found")

