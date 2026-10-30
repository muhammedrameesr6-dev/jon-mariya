import os
import re

with open("index.html") as f:
    text = f.read()

paths = set()
# find url(...)
for m in re.findall(r'url\([\'"]?([a-zA-Z0-9_\-\./]+\.[a-zA-Z0-9]+)[\'"]?\)', text):
    paths.add(m)

# find src= or href= or poster=
for m in re.findall(r'(?:src|href|poster)=[\'"]([a-zA-Z0-9_\-\./]+\.[a-zA-Z0-9]+)[\'"]', text):
    paths.add(m)

# find JS variable assignments with relative file paths
for m in re.findall(r'[\'"]([a-zA-Z0-9_\-\./]+\.(?:mp3|mp4|jpg|jpeg|png|webp|svg|css|js))[\'"]', text):
    paths.add(m)

all_ok = True
for p in sorted(paths):
    if not p.startswith("http") and not p.startswith("#"):
        exists = os.path.exists(p)
        size = os.path.getsize(p) if exists else 0
        status = "OK" if exists and size > 0 else "MISSING!"
        if not exists:
            all_ok = False
        print(f"[{status}] {p} ({size} bytes)")

if all_ok:
    print("\nALL LOCAL ASSETS VERIFIED SUCCESSFULLY!")
else:
    print("\nSOME ASSETS ARE MISSING!")
