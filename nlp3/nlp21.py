import re

with open("england.json") as f:
    content = f.read()
    pattern = r'\[\[Category.*?\]\]'
    m = re.findall(pattern,content)
    for n in m:
        print(n)
