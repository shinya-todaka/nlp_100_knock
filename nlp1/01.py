str = 'パタトクカシーー'
#my_answer
new_str = ""
for index,value in enumerate(str):
    if(index % 2 == 0):
        new_str += value
print(new_str)
#easy way
print(str[0::2])
