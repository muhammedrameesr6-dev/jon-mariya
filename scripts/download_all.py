import os
import urllib.request

downloads = [
    ("https://digiwed161-sys.github.io/arnoldwedsangel/og-thumb.png", "og-thumb.png"),
    ("https://digiwed161-sys.github.io/arnoldwedsangel/wedding-card.jpg", "wedding-card.jpg"),
    ("https://digiwed161-sys.github.io/arnoldwedsangel/assets/bg-ink-clouds-rose.jpg", "assets/bg-ink-clouds-rose.jpg"),
    ("https://digiwed161-sys.github.io/arnoldwedsangel/assets/bg-ink-clouds-wine.jpg", "assets/bg-ink-clouds-wine.jpg"),
    ("https://digiwed161-sys.github.io/arnoldwedsangel/assets/dance-couple-red.png", "assets/dance-couple-red.png"),
    ("https://imagedelivery.net/pXU-KzWtO2cgM-XrR20TQg/9aa4c918-902d-4d87-bcda-abdbeddd0a00/public", "assets/gate-cover.jpg"),
    ("https://imagedelivery.net/pXU-KzWtO2cgM-XrR20TQg/9655bda8-ee3e-40aa-78d7-2e6f061eaa00/w900", "assets/hero-poster.jpg"),
    ("https://pub-bc01cea1ca914ad8aba6c7541c55c7fb.r2.dev/digiwed-invitations-sahal-fasmina-2-video/hero-clouds-sound.mp4", "assets/hero-clouds-sound.mp4"),
    ("https://pub-bc01cea1ca914ad8aba6c7541c55c7fb.r2.dev/digiwed-invitations-arnold-angel-audio/bgm_track.mp3", "assets/bgm_track.mp3"),
    ("https://digiwed161-sys.github.io/digiwed-library/library.js", "assets/library.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js", "assets/html2canvas.min.js"),
    ("https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js", "assets/jspdf.umd.min.js"),
]

for url, dest in downloads:
    os.makedirs(os.path.dirname(dest) if os.path.dirname(dest) else ".", exist_ok=True)
    if os.path.exists(dest) and os.path.getsize(dest) > 0:
        print(f"Already exists: {dest} ({os.path.getsize(dest)} bytes)")
        continue
    print(f"Downloading {url} -> {dest} ...")
    try:
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
            f.write(resp.read())
        print(f"Downloaded: {dest} ({os.path.getsize(dest)} bytes)")
    except Exception as e:
        print(f"Failed {url}: {e}")
