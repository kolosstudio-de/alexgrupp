import os

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"

# 1. Update i18n.js to prefetch all locales
i18n_path = os.path.join(base_dir, "js", "i18n.js")
with open(i18n_path, "r", encoding="utf-8") as f:
    i18n = f.read()

prefetch_code = """
// Prefetch all languages in the background for instant switching
window.addEventListener('load', () => {
    setTimeout(() => {
        LANGS.forEach(({ code }) => {
            if (code !== getLang() && !_cache[code]) {
                fetch(BASE_PATH + code + '.json')
                    .then(r => r.json())
                    .then(data => {
                        _cache[code] = data;
                        localStorage.setItem('ag-i18n-' + code, JSON.stringify(data));
                    }).catch(() => {});
            }
        });
    }, 1000); // 1 second after load
});
"""

if "Prefetch all languages" not in i18n:
    i18n += "\n" + prefetch_code
    with open(i18n_path, "w", encoding="utf-8") as f:
        f.write(i18n)
    print("Added prefetch to i18n.js")

# 2. Preload Hero images in HTML
html_updates = {
    "index.html": [
        ('</title>', '</title>\n    <link rel="preload" as="image" href="assets/auto-bg.webp">\n    <link rel="preload" as="image" href="assets/bau-bg.webp">')
    ],
    "auto/index.html": [
        ('</title>', '</title>\n    <link rel="preload" as="image" href="../assets/auto-hero.webp">')
    ],
    "auto/uber-uns.html": [
        ('</title>', '</title>\n    <link rel="preload" as="image" href="../assets/auto_hero_v2.webp">')
    ],
    "bau/index.html": [
        ('</title>', '</title>\n    <link rel="preload" as="image" href="../assets/bau-hero.webp">')
    ],
    "bau/uber-uns.html": [
        ('</title>', '</title>\n    <link rel="preload" as="image" href="../assets/bau_hero.webp">')
    ],
}

for rel_path, replacements in html_updates.items():
    filepath = os.path.join(base_dir, rel_path)
    if os.path.exists(filepath):
        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()
        for old, new in replacements:
            if new not in content:
                content = content.replace(old, new)
        with open(filepath, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Added preloads to {rel_path}")

print("Done optimizing performance.")
