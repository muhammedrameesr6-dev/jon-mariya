import os
import urllib.request
import urllib.error

base = "https://digiwed161-sys.github.io/arnoldwedsangel/"
files = [
    "favicon.ico", "robots.txt", "sitemap.xml", "manifest.json", 
    "og-thumb.png", "Arnold-and-Angel-Wedding-Card.jpg", "wedding-card.jpg",
    "assets/bg-ink-clouds-rose.jpg", "assets/bg-ink-clouds-wine.jpg", "assets/dance-couple-red.png",
    "assets/favicon.ico", "assets/favicon.png", "style.css", "script.js", "app.js"
]

for f in files:
    url = base + f
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        resp = urllib.request.urlopen(req)
        cl = resp.headers.get("Content-Length", "unknown")
        print(f"EXISTS: {f} ({resp.status}) - {cl} bytes")
    except urllib.error.HTTPError as e:
        print(f"NOT FOUND: {f} ({e.code})")
    except Exception as e:
        print(f"ERR: {f} {e}")
