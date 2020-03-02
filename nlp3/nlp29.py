from nlp20 import load_json_gz
import re
import urllib.parse
import urllib.request
import json

#nlp25
content = load_json_gz("jawiki-country.json.gz")["イギリス"]
pattern1 = re.compile(r"^\{\{基礎情報.*?$(.*?)^\}\}$",re.MULTILINE + re.VERBOSE + re.DOTALL)
basic_information = pattern1.findall(content)

pattern2 = re.compile(r"^\|(.+?)\s*=\s*(.+?)(?:(?=\n\|)|(?=\n$))", re.DOTALL + re.MULTILINE)
fields = pattern2.findall(basic_information[0])

#nlp26
def remove_emphasis(str):
    return re.sub(r"'{1,5}(.*?)'{1,5}",r"\1",str)

#nlp27
def remove_link(str):
    return re.sub(r"\[\[(?:([^\|]+?)|(?:(?:[^\|]+?)\|([^\|]+?)))\]\]",r"\1\2",str)

def get_flag_url(title):

    url = "https://ja.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "format": "json",
        "prop": "imageinfo",
        "titles": "File:" + urllib.parse.quote(title),
        "iiprop":"url"
    }

    req = urllib.request.Request("{}?{}".format(url,"&".join("%s=%s" % (k,v) for k,v in params.items())))
    with urllib.request.urlopen(req) as res:
        body = res.read()
        j = json.loads(body)
        flag_url = list(j["query"]["pages"].values())[0]["imageinfo"][0]["url"]
        print(flag_url)

dictionary = {}
removed_dictionary = {}
for item in fields:
    dictionary[item[0]] = item[1]
    removed_dictionary[item[0]] = remove_link(remove_emphasis(item[1]))

for k,v in removed_dictionary.items():
    if k == "国旗画像":
        get_flag_url(v)
