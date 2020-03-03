import MeCab
import pprint

def make_neko_txt_mecab():
    with open("neko.txt") as f:
        lines = f.read()
        m = MeCab.Tagger()
        with open("neko.txt.mecab","w") as f:
            f.write(m.parse(lines))

def make_morpheme():
    with open("neko.txt.mecab") as f:
        morpheme_list = []
        for line in f:
                if len(line.split()) < 2:
                    return
                surface = line.split()[0]
                other_list = line.split()[1].split(",")
                if (len(other_list) > 8):
                    dictionary = {}
                    dictionary["surface"] = surface
                    dictionary["base"] = other_list[6]
                    dictionary["pos"] = other_list[0]
                    dictionary["pos1"] = other_list[1]
                    morpheme_list.append(dictionary)
                    if surface == "。":
                        yield morpheme_list
                        morpheme_list = []

#qiitaでみたやり方
def parse_line(line):
    (surface,attr) = line.split('\t')
    arr = attr.split(',')
    return {
        "surface":surface,
        "base":arr[6],
        "pos":arr[0],
        "pos1":arr[1]
    }

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
# n = 0
# for list in read_mecab_file("neko.txt.mecab_unix"):
#     n += 1
#     pprint.pprint(list)
#     if n > 30:
#         break
