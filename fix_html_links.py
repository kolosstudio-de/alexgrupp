import os
import re

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"

# Fix global.css
global_css_path = os.path.join(base_dir, "styles", "global.css")
if os.path.exists(global_css_path):
    with open(global_css_path, "r", encoding="utf-8") as f:
        css = f.read()
    # Replace google font import
    css = re.sub(r"@import url\('https://fonts\.googleapis\.com[^']+'\);", "@import url('../assets/fonts/fonts.css');", css)
    with open(global_css_path, "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated global.css")

# Fix HTML files
for root, dirs, files in os.walk(base_dir):
    if "node_modules" in root or ".git" in root or ".agents" in root or "audit" in root:
        continue
    for file in files:
        if file.endswith(".html") and not file.startswith("._"):
            filepath = os.path.join(root, file)
            # relative path to assets
            rel_depth = len(os.path.relpath(root, base_dir).split(os.sep))
            if os.path.relpath(root, base_dir) == ".":
                assets_prefix = "assets"
            else:
                assets_prefix = "../assets"
            
            with open(filepath, "r", encoding="utf-8") as f:
                html = f.read()
                
            # Remove preconnects
            html = re.sub(r'<link rel="preconnect" href="https://fonts\.googleapis\.com">\s*', '', html)
            html = re.sub(r'<link rel="preconnect" href="https://fonts\.gstatic\.com" crossorigin>\s*', '', html)
            
            # Replace AOS
            html = html.replace("https://unpkg.com/aos@next/dist/aos.css", f"{assets_prefix}/lib/aos.css")
            html = html.replace("https://unpkg.com/aos@next/dist/aos.js", f"{assets_prefix}/lib/aos.js")
            
            # Replace Font Awesome
            html = html.replace("https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css", f"{assets_prefix}/lib/all.min.css")
            
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(html)
            print(f"Updated {filepath}")

print("Done updating HTML links.")
