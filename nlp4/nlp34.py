from nlp30 import make_morpheme
from nlp30 import parse_line
import pprint

n = 0
one_before = ""

def a_no_b(morpheme_list):
    if len(morpheme_list) > 2:
        a = morpheme_list[0]
        d = morpheme_list[1]
        new_array = []
        for b in morpheme_list[2:]:
                if a["pos"] ==  "名詞" and b["pos"] == "名詞" and d["surface"] == "の":
                    new_array.append(a)
                    new_array.append(d)
                    new_array.append(b)
                    yield new_array
                    new_array = []
                a = d
                d = b

#”の”のpos1が連体化って事を追加したほうがいいかも
def using_while(morpheme_list):
    i = 0
    str = ""
    for i in range(len(morpheme_list)):
        if morpheme_list[i]["pos"] == "名詞" and morpheme_list[i + 1]["surface"] == "の" and morpheme_list[i + 2]["pos"] == "名詞":
            yield "".join([d["surface"] for d in morpheme_list[i:i+3]])
            str = ""


for l in make_morpheme():
    n += 1
    if n > 100:
        break
    for b_of_a in using_while(l):
        print(b_of_a)

def read_mecab_file(filename) -> [[{}]]:
    sentence = []
    with open(filename,mode='rt',encoding='utf-8') as f:
        for line in f:
            line = line.rstrip('\n')
            if line == "EOS":
                yield sentence
                sentence = []
            else:
                sentence.append(parse_line(line))
