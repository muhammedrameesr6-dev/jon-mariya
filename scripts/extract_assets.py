import re

with open("index.html") as f:
    text = f.read()

for ext in ["png", "jpg", "jpeg", "webp", "mp3", "mp4", "svg", "ico"]:
    pattern = rf'[\w\-\./:]+\.{ext}(?:\?[^\s"\'<>]*)?'
    matches = set(re.findall(pattern, text, re.IGNORECASE))
    print(ext, matches)
