import re
import gzip
import json

def load_json_gz(filename):
    dictionary = {}
    with gzip.open(filename,'rt', encoding="utf-8") as fp:
            for line in fp:
                item = json.loads(line)
                dictionary[item["title"]] = item["text"]
            return dictionary

england = load_json_gz("jawiki-country.json.gz")["イギリス"]

with open("england.json","r") as f:
    content = f.read()
    pattern = r"(=+)([^=]*?)\1\n"
    for key,v in re.findall(pattern,england):
        print("{0}   {1}".format(v,len(key)-1))
