import re

with open("index.html") as f:
    text = f.read()

matches = re.findall(r'(?:src|href|poster)=["\']([^"\']+)["\']', text)
for m in sorted(set(matches)):
    print(m)
