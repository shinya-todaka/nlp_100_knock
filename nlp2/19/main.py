import collections
import sys

content = sys.stdin

def my_answer():

    lines = content.readlines()
    collection = collections.Counter([l.split()[0] for l in lines])

    for l in sorted(collection.items(),key=lambda pair: pair[1],reverse=True):
        print("{} {}".format(l[1],l[0]))

def other_answer():

    data = {}
    for line in content:
        key = line.split()[0]
        data[key] = data.get(key,0) + 1

    sorted_dictionary = sorted(data.items(), key=lambda pair:pair[1],reverse=True)

    for index,value in sorted_dictionary:
        print(value,index)

other_answer()
