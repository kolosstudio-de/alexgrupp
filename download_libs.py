import os
import urllib.request

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"
lib_dir = os.path.join(base_dir, "assets", "lib")
os.makedirs(lib_dir, exist_ok=True)
os.makedirs(os.path.join(lib_dir, "webfonts"), exist_ok=True)

# 1. Download AOS
aos_css_url = "https://unpkg.com/aos@next/dist/aos.css"
aos_js_url = "https://unpkg.com/aos@next/dist/aos.js"

print("Downloading AOS...")
urllib.request.urlretrieve(aos_css_url, os.path.join(lib_dir, "aos.css"))
urllib.request.urlretrieve(aos_js_url, os.path.join(lib_dir, "aos.js"))

# 2. Download Font Awesome 6.5.0
fa_css_url = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/css/all.min.css"
fa_fonts = [
    "fa-solid-900.woff2",
    "fa-solid-900.ttf",
    "fa-regular-400.woff2",
    "fa-regular-400.ttf",
    "fa-brands-400.woff2",
    "fa-brands-400.ttf",
    "fa-v4compatibility.woff2",
    "fa-v4compatibility.ttf"
]
fa_base = "https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.5.0/webfonts/"

print("Downloading Font Awesome CSS...")
urllib.request.urlretrieve(fa_css_url, os.path.join(lib_dir, "all.min.css"))

for font in fa_fonts:
    print(f"Downloading {font}...")
    try:
        urllib.request.urlretrieve(fa_base + font, os.path.join(lib_dir, "webfonts", font))
    except Exception as e:
        print(f"Failed to download {font}: {e}")

print("Done downloading libs.")
