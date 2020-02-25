#my_answer
with open("../hightemp.txt","r") as f:
    str = f.read()
    col1 = []
    col2 = []
    for index,word in enumerate(str.split()):
        if index % 4 == 0:
            col1.append(word)
        elif index % 4 == 1:
            col2.append(word)

with open("col1.txt","w") as f:
        f.write("\n".join(col1))
with open("col2.txt","w")  as f:
        f.write("\n".join(col2))
#alternative_answer
def write_all(filename:str,col:int):
    with open("../hightemp.txt","r") as f:
            data = list(l.split() for l in f)
    with open(filename,"w") as f:
             lines = [words[col - 1] + "\n" for words in data]
             for line in lines:
                 f.write(line)
write_all("col1.txt",1)
write_all("col2.txt",2)
