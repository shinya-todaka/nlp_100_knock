str = "I am an NLPer"
#my_answer
def get_n_gram(n:int,str:str):
    n_gram = []
    for i in range(len(str) - n + 1):
        n_gram.append(str[i:n + i])
    return n_gram
#short_answer
def n_gram(target,n):
    return [target[i:n+i] for i in range(len(target) - n + 1)]


print(n_gram(str.split(),2))
print(get_n_gram(2,str))
