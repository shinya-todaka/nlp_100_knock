from nlp30 import make_morpheme
import pprint

n = 0
for l in make_morpheme():
    n += 1
    if n > 10:
        break
    pprint.pprint(l)
