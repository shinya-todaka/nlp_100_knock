str1 = "paraparaparadise"
str2 = "paragraph"

def n_gram(n:int,str:str):
    return [str[index: index + n] for index in range(len(str) - n + 1)]

X = n_gram(2,str1)
Y = n_gram(2,str2)

set_x = set(X)
set_y = set(Y)
union = set_x.union(set_y)
difference = set_x.difference(set_y)
intersection = set_x.intersection(set_y)

print("se" in intersection)
