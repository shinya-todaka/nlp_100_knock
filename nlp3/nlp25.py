from nlp20 import load_json_gz
import re

content = load_json_gz("jawiki-country.json.gz")["イギリス"]

pattern = r"\|(.*?) = (.*?)\n"

matches = re.findall(pattern,content)

dictionary = {}
for match in matches:
    dictionary[match[0]] = match[1]

for k,v in dictionary.items():
    print(k,v)
