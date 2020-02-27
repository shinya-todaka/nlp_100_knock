import sys
import math
import numpy as np

n = int(sys.argv[1])
lines = sys.stdin


result = list(np.array_split([ l for l in lines],n))

for index,array in enumerate(result):
    filename = "nlp16.{0:02}".format(index)
    with open(filename,"w") as f:
        for l in array:
            f.write(l)
