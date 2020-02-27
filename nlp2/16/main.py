import sys
import math
import numpy as np

n = int(sys.argv[1])

lines = sys.stdin
l = [ l for l in lines]


result = list(np.array_split(l,n))


for index,array in enumerate(result):
    filename = "nlp16.{0:02}".format(index)
    with open(filename,"w") as f:
        for l in array:
            f.write(l)
