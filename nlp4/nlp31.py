from nlp30 import make_morpheme
import pprint

n = 0
for l in make_morpheme():
    n += 1
    if n > 100:
        break
    for d in l:
        if d["pos"] == "動詞":
            print(d["surface"])
