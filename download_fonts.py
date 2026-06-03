import os
import re
import urllib.request

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"
fonts_dir = os.path.join(base_dir, "assets", "fonts")
os.makedirs(fonts_dir, exist_ok=True)

css_url = "https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;600;700&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&display=swap"

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

req = urllib.request.Request(css_url, headers=headers)
with urllib.request.urlopen(req) as response:
    css_content = response.read().decode('utf-8')

# Find all url(https://...)
urls = re.findall(r'url\((https://[^)]+)\)', css_content)

downloaded = {}
counter = 1

for url in set(urls):
    filename = f"font-{counter}.woff2"
    filepath = os.path.join(fonts_dir, filename)
    print(f"Downloading {filename} from {url}...")
    try:
        urllib.request.urlretrieve(url, filepath)
        downloaded[url] = filename
        counter += 1
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Replace URLs in CSS
for url, filename in downloaded.items():
    css_content = css_content.replace(url, f"../assets/fonts/{filename}")

# Save the local CSS
with open(os.path.join(fonts_dir, "fonts.css"), "w", encoding="utf-8") as f:
    f.write(css_content)

print("Google Fonts downloaded and fonts.css created.")
