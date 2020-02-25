count = 0
with open("../hightemp.txt") as f:
    for s_line in f:
        count += 1
print(count)
