import sys

file = sys.stdin

for s in sorted(list(set([l.split()[0] for l in file]))):
    print(s,end="\n")
