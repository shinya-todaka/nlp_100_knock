import re
with open("../12/col1.txt") as f_1:
    with open("../12/col2.txt") as f_2:
        merge_col = [col1 + col2 for col1,col2 in zip([re.sub(r'\n','\t',l) for l in f_1],[l for l in f_2])]
with open("merge_col.txt","w") as f:
    for l in merge_col:
        f.write(l)
