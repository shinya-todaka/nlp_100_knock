import re

with open("../hightemp.txt",'r') as f:
    str = f.read()
    with open("hightemp_11_py.txt","w") as f:
        new_str = re.sub(r'\t',' ',str)
        f.write(new_str)
