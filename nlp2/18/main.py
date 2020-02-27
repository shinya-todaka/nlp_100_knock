import sys
import pprint


for l in sorted(sys.stdin,key=lambda x: x.split()[2],reverse=True):
    print(l,end="")
