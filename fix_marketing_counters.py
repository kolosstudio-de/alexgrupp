import os
import re

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"

# Fix auto/index.html
auto_idx = os.path.join(base_dir, "auto/index.html")
with open(auto_idx, "r", encoding="utf-8") as f:
    auto_content = f.read()
auto_content = auto_content.replace('<span class="count">5+</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-handshake"></i></span>')
auto_content = auto_content.replace('<span class="count">Bayern</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-map-marker-alt"></i></span>')
auto_content = auto_content.replace('<span class="count">100%</span>\n            <span class="label" data-i18n="auto-counter-quality">', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-star"></i></span>\n            <span class="label" data-i18n="auto-counter-quality">')
auto_content = auto_content.replace('<span class="count">100%</span>\n            <span class="label" data-i18n="auto-counter-transparency">', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-search"></i></span>\n            <span class="label" data-i18n="auto-counter-transparency">')
with open(auto_idx, "w", encoding="utf-8") as f:
    f.write(auto_content)


# Fix bau/index.html
bau_idx = os.path.join(base_dir, "bau/index.html")
with open(bau_idx, "r", encoding="utf-8") as f:
    bau_content = f.read()
bau_content = bau_content.replace('<span class="count">10+</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-hammer"></i></span>')
bau_content = bau_content.replace('<span class="count">300+</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-users"></i></span>')
bau_content = bau_content.replace('<span class="count">5★</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-star"></i></span>')
bau_content = bau_content.replace('<span class="count">100%</span>', '<span class="count" style="font-size: 2.2rem"><i class="fas fa-shield-alt"></i></span>')
with open(bau_idx, "w", encoding="utf-8") as f:
    f.write(bau_content)

# Fix auto/uber-uns.html
auto_uber = os.path.join(base_dir, "auto/uber-uns.html")
with open(auto_uber, "r", encoding="utf-8") as f:
    auto_uber_content = f.read()
auto_uber_content = auto_uber_content.replace('Heute: 2000+ zufriedene Kunden', 'Heute: Ein verlässlicher Partner')
with open(auto_uber, "w", encoding="utf-8") as f:
    f.write(auto_uber_content)

print("Marketing counters fixed.")
