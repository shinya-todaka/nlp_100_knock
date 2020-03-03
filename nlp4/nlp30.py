import MeCab
import pprint

def make_neko_txt_mecab():
    with open("neko.txt") as f:
        lines = f.read()
        m = MeCab.Tagger()
        with open("neko.txt.mecab","w") as f:
            f.write(m.parse(lines))

def make_morpheme() -> []:
    with open("neko.txt.mecab") as f:
        morpheme_list = []
        for line in f:
                surface = line.split()[0]
                other_list = line.split()[1].split(",")
                if (len(other_list) > 8):
                    dictionary = {}
                    dictionary["surface"] = surface
                    dictionary["base"] = other_list[7]
                    dictionary["pos"] = other_list[0]
                    dictionary["pos1"] = other_list[1]
                    morpheme_list.append(dictionary)
                    if surface == "。":
                        yield morpheme_list
                        morpheme_list = []
n = 0
for list in make_morpheme():
    n += 1
    pprint.pprint(list)
    if n > 30:
        break
