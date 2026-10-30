import os
import re
import urllib.request

with open("assets/fonts.css", "r") as f:
    css = f.read()

os.makedirs("assets/fonts", exist_ok=True)

font_urls = re.findall(r'url\((https://fonts.gstatic.com/[^\)]+)\)', css)
print(f"Found {len(font_urls)} fonts")

for url in font_urls:
    fname = os.path.basename(url)
    dest = os.path.join("assets/fonts", fname)
    if not os.path.exists(dest):
        print(f"Downloading {fname}...")
        try:
            req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
            with urllib.request.urlopen(req) as r, open(dest, "wb") as f:
                f.write(r.read())
        except Exception as e:
            print("Err:", e)
    css = css.replace(url, f"fonts/{fname}")

with open("assets/fonts.css", "w") as f:
    f.write(css)

print("Updated assets/fonts.css successfully!")
