str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can."
numbers = [1,5,6,7,8,9,15,16,19]
#my_answer
def get_element_symbols(s: str):
    word = ""
    words = []
    dictionary = {}
    for c in s:
        if "a" <= c <= "z" or "A" <= c <= "Z":
            word += c
        else:
            if word != "":
                words.append(word)
                word = ""

    for index,element in enumerate(words):
        if index + 1 in numbers:
            dictionary[index + 1] = element[0]
        else:
            dictionary[index + 1] = element[0] + element[1]
    return dictionary
#short_answer
def short_answer(str:str):
    word = ""
    dictionary = {}
    count = 0
    for i in range(len(str)):
        if "A" <= str[i] <= "Z":
            count += 1
            if count in numbers:
                dictionary[count] = str[i]
            else:
                dictionary[count] = str[i:i+2]
    return dictionary

import re
#more short my_answer
def more_short_answer(str:str):
    return { word[0] if index + 1 in numbers else word[0:2]: index + 1 for index,word in enumerate(re.findall("[a-zA-Z]+",str))}
print(more_short_answer(str))
