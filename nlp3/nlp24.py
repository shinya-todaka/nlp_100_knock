from nlp20 import load_json_gz
import re

england = load_json_gz("jawiki-country.json.gz")["イギリス"]

pattern = "ファイル:(.*?\.\w+)\|"
better_pattern = r"\[\[(ファイル|File):([^]|]+?)(\|.*?)\]\]"

matches = re.findall(better_pattern,england)
for match in matches:
    print(match[1])
