str1 = "パトカー"
str2 = "タクシー"

#my_answer

def append_alternately(s1: str, s2: str):
    str = ""
    for i in range(len(s1)):
        str = str + s1[i] + s2[i]
    return str

#better_answer
str = ""
for s1,s2 in zip(str1,str2):
    str = str + s1 + s2
#short_answer
str = "".join(s1+s2 for s1,s2 in zip(str1,str2))
print(str)
