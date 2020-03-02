from nlp20 import load_json_gz
import re

#qiitaの記事からパクったやつ
content = load_json_gz("jawiki-country.json.gz")["イギリス"]
pattern1 = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$",re.MULTILINE + re.VERBOSE + re.DOTALL)
basic_information = pattern1.findall(content)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))", re.DOTALL + re.MULTILINE)
fields = pattern2.findall(basic_information[0])

dictionary = {}
for item in fields:
    dictionary[item[0]] = item[1]

for k,v in dictionary.items():
    print(k,v)
