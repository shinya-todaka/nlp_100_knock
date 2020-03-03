from nlp20 import load_json_gz
import re

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
    return re.sub(r"\[{1,2}(?:([^\|]+?)|(?:(?:[^\|]+?)\|([^\|]+?)))\]{1,2}",r"\1\2",str)

#nlp28
def remove_brackets(str):
    return re.sub(r"\{{1,2}(.*?)\}{1,2}",r"\1",str)

def remove_reftag(str):
    return re.sub(r"(^.+)?(?:<ref(?:[^>]+)?>.*</ref>|<[^/]+/>)",r"\1",str)

def new_remove_link(str):
    return re.sub(r"\[\[.+\|(.*?)\]\]",r"\1",str)

def new_remove_link_2(str):
    return re.sub(r"\[\[(.+)\]\]",r"\1",str)


dictionary = {}
removed_dictionary = {}
for item in fields:
    dictionary[item[0]] = item[1]
    removed_dictionary[item[0]] = new_remove_link_2(remove_reftag(remove_link(remove_brackets(remove_emphasis(item[1])))))

for k,v in removed_dictionary.items():
    print(k,v)
