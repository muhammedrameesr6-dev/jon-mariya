import re

with open("index.html") as f:
    text = f.read()

for m in re.finditer(r"cal-link", text):
    start = max(0, m.start() - 50)
    end = min(len(text), m.end() + 150)
    print("MATCH:", text[start:end])
