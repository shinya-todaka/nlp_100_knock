from nlp20 import load_json_gz
import re

#このコードは見る価値なしです
content = load_json_gz("jawiki-country.json.gz")["イギリス"]

pattern = r"(\|.*?) = (.*?)\n"

matches = re.findall(pattern,content)
dictionary = {}
for match in matches:
    dictionary[match[0]] = match[1]

def my_answewr(dic):
    started_with_vertical_bar = True
    new_dictionary = {}
    key = ""
    s = ""

    for k,v in dic.items():
        # print("{0}      {1}".format(k,v))
        if k[0] == "|":
            if not started_with_vertical_bar:
                new_dictionary[key] = s
                s = ""
            #remove"[]" to easy to read
            new_dictionary[k[1:]] = re.sub(r"(?m)\[\[(.*?)\]\]",r"\1",v)
            key = k[1:]
            started_with_vertical_bar = True
        else:
            s += re.sub(r"(?m)\[\[(.*?)\]\]",r"\1",v)
            started_with_vertical_bar = False
    return new_dictionary

# for k,v in my_answewr(dictionary).items():
#     print("{0}  {1}".format(k,v))
