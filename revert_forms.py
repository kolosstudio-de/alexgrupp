import os

base_dir = "/Volumes/Extreme SSD/ AI Prrojects /alexgruppweb-бекап-2026-05-04-перед-аудит-фіксами"

bau_file = os.path.join(base_dir, "bau/kontakt.html")
with open(bau_file, "r", encoding="utf-8") as f:
    bau = f.read()
bau = bau.replace("""<form action="https://api.web3forms.com/submit" method="POST" id="bookingFormBau">
                    <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
                    <input type="hidden" name="subject" value="Neue Anfrage über die Website (Bau)">
                    <input type="hidden" name="redirect" value="https://oleksandrhalushka.de/bau/kontakt.html?success=true">""", '<form action="#" method="POST" id="bookingFormBau">')
with open(bau_file, "w", encoding="utf-8") as f:
    f.write(bau)

auto_file = os.path.join(base_dir, "auto/kontakt.html")
with open(auto_file, "r", encoding="utf-8") as f:
    auto = f.read()
auto = auto.replace("""<form action="https://api.web3forms.com/submit" method="POST" id="bookingFormAuto">
                    <input type="hidden" name="access_key" value="YOUR_ACCESS_KEY_HERE">
                    <input type="hidden" name="subject" value="Neue Anfrage über die Website (Auto)">
                    <input type="hidden" name="redirect" value="https://oleksandrhalushka.de/auto/kontakt.html?success=true">""", '<form action="#" method="POST" id="bookingFormAuto">')
with open(auto_file, "w", encoding="utf-8") as f:
    f.write(auto)

print("Reverted to original form actions.")
