str = "I am an NLPer"

def cipher1(str:str) -> str:
    new_str = ""
    for index,s in enumerate(str):
        if "a" <= s <= "z":
            new_str += chr(219 - ord(s))
        else:
            new_str += s
    return new_str
#short_answer
def cipher2(str:str) -> str:
    return "".join(chr(219 - ord(s)) if "a" <= s <= "z" else s for s in str)
print(cipher2(str))
