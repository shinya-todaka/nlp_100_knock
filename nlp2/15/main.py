import sys

argv = sys.argv
n = int(argv[1])

def my_answer():
    with open("../hightemp.txt") as f:
        lines = f.readlines()
        for i in range(len(lines) - n,len(lines)):
            print(lines[i])

def tail():
    lines = list(sys.stdin)
    for line in lines[-n:]:
        print(line, end="")
tail()
