str = "I couldn't believe that I could actually understand what I was reading : the phenomenal power of the human mind ."

import random

#my_answer

def typoglycemia(str:str):
    str_list = []
    for s in str.split():
        if len(s) >= 4:
            middle = s[1:len(s) - 1]
            random_str = "".join(random.sample(middle,len(s) - 2))
            str_list.append(s[0] + random_str + s[-1])
        else:
            str_list.append(s)
    return " ".join(str_list)

#short_answer

def short_answer(str:str):
    return " ".join(s[0] + "".join(random.sample(s[1:-1],len(s) - 2)) + s[-1] if len(s) > 4 else s for s in str.split())

#best_answer
def typoglycemia(word :str) -> str:
    if len(word) < 5:
        return word
    else:
        while True:
            result = word[0] + "".join(random.sample(word[1:-1], len(word) - 2)) + word[-1]
            if result != word:
                return result

def typoglycemia_sentence(sentence:str) -> str:
    words = sentence.split()
    return " ".join([typoglycemia(word) for word in words])

print(typoglycemia_sentence(str))
