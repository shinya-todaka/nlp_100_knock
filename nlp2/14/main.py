import sys

args = sys.argv

with open("../hightemp.txt") as f:
    lines = f.readlines()
    for i in range(int(args[1])):
        print(lines[i])
