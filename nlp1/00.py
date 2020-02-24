str = "stressed"
str_reversed = list(reversed(str))
print(str_reversed)

new_str = ''.join(list(reversed(str)))
print(new_str)
#or
new_str2 = str[::-1]
print(new_str2)
