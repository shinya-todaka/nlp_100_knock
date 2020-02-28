import re

with open("england.json") as f:
    content = f.read()
    pattern = r"\[\[Category:(.*?)(\|.*?)?\]\]"
    match = re.findall(pattern,content)
    for m in match:
        print(m[0])
