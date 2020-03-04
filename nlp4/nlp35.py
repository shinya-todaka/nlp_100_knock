from nlp30 import make_morpheme
import pprint

n = 0

longest_array = []

def get_linked_noun(l):
    current_continuation = []
    for d in l:
        if d["pos"] == "名詞":
            current_continuation.append(d)
        else:
            if len(current_continuation) >= 2:
                yield "".join([d["surface"] for d in current_continuation])
            current_continuation = []

new_array = []
for l in make_morpheme():
    n += 1
    if n > 100:
        break
    for linked_noun in get_linked_noun(l):
        print(linked_noun)
