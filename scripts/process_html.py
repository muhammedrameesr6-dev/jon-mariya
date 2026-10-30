import re

with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

# 1. Remove anti-clone domain lock
anti_clone_pat = r"<!-- ===== DigiWed DOMAIN LOCK \(anti-clone\).*?</script>"
html, n1 = re.subn(anti_clone_pat, "<!-- DigiWed domain lock removed for independent hosting -->", html, flags=re.DOTALL)
print(f"Anti-clone script removed: {n1}")

# 2. Add local fonts stylesheet
font_link = '<link href="assets/fonts.css" rel="stylesheet">'
if font_link not in html:
    html = html.replace(
        '<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond',
        f'{font_link}\n<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond'
    )
    print("Added local fonts.css link")

# 3. Localize Firebase SDKs
html = html.replace("https://www.gstatic.com/firebasejs/9.23.0/firebase-app-compat.js", "assets/firebase-app-compat.js")
html = html.replace("https://www.gstatic.com/firebasejs/9.23.0/firebase-database-compat.js", "assets/firebase-database-compat.js")
print("Local Firebase scripts updated")

# 4. Localize poster & hero background
html = html.replace("https://imagedelivery.net/pXU-KzWtO2cgM-XrR20TQg/9655bda8-ee3e-40aa-78d7-2e6f061eaa00/w900", "assets/hero-poster.jpg")
html = html.replace("https://imagedelivery.net/pXU-KzWtO2cgM-XrR20TQg/9aa4c918-902d-4d87-bcda-abdbeddd0a00/public", "assets/gate-cover.jpg")
print("Gate cover & hero poster updated")

# 5. Localize DEFAULT_FILM & DEFAULT_BGM
html = html.replace(
    'var DEFAULT_FILM  = "https://pub-bc01cea1ca914ad8aba6c7541c55c7fb.r2.dev/digiwed-invitations-sahal-fasmina-2-video/hero-clouds-sound.mp4";',
    'var DEFAULT_FILM  = "assets/hero-clouds-sound.mp4";'
)
html = html.replace(
    'var DEFAULT_BGM      = "";',
    'var DEFAULT_BGM      = "assets/bgm_track.mp3";'
)
print("DEFAULT_FILM & DEFAULT_BGM updated")

# 6. Localize PDF & BGM libraries
html = html.replace("https://cdnjs.cloudflare.com/ajax/libs/html2canvas/1.4.1/html2canvas.min.js", "assets/html2canvas.min.js")
html = html.replace("https://cdnjs.cloudflare.com/ajax/libs/jspdf/2.5.1/jspdf.umd.min.js", "assets/jspdf.umd.min.js")
html = html.replace('var BGM_LIBRARY_URL = "https://digiwed161-sys.github.io/digiwed-library/library.js";', 'var BGM_LIBRARY_URL = "assets/library.js";')
print("PDF & BGM libraries updated")

# 7. Localize OG tags
html = html.replace("https://digiwed161-sys.github.io/arnoldwedsangel/og-thumb.png?v=2", "og-thumb.png")
html = html.replace("https://digiwed161-sys.github.io/arnoldwedsangel/", "./")
print("OG meta tags updated")

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("index.html successfully updated!")
