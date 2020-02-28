import gzip
import json
import re

def load_json_gz(filename):
    dictionary = {}
    with gzip.open(filename,'rt', encoding="utf-8") as f:
            return {item["title"]: item["text"] for item
                    in [json.loads(line) for line in f]}

# article = load_json_gz("jawiki-country.json.gz")
#
# with open("england.json","w",encoding="utf-8") as f:
#     json.dump(article["イギリス"],f, indent=4,ensure_ascii=False)
