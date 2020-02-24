str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics."
#my_answer
def count_length_of_each_word(s: str):
    count_list = []
    count = 0
    symbol = False
    for s in str:
        if s == " " or s == "." or  s == "," :
            if not symbol:
                count_list.append(count)
                count = 0
                symbol = True
        else:
            count += 1
            symbol = False
    return count_list

print(count_length_of_each_word(str))
