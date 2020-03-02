from nlp20 import load_json_gz
import re

#qiitaの記事見て別解やろうとしたけど意味わからなくなった
content = load_json_gz("jawiki-country.json.gz")["イギリス"]

parsed = [[]]
s = "foo"

parsed[-1].append(s)
print(parsed)

t = "{{"
parsed[-1].append([t])
parsed.append(parsed[-1][-1])
print(parsed)

u = "bar"

parsed[-1].append(u)
print(parsed)

v = "}}"

parsed[-1].append(v)
print(parsed)
parsed.remove(parsed[-1])
print(parsed)

w = "bar"

parsed[-1].append(w)
print(parsed)
