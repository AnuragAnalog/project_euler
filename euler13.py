#!/usr/bin/python3

"""
   Work out the first ten digits of the sum of the following one-hundred 50-digit numbers.
The hundred 50-digit numbers are present in the file euler13.txt
"""

def euler13() -> str:
    fhand = open("euler13.txt", "r")

    tot = 0
    i = 0
    for line in fhand:
        i = i + 1
        tmp = "".join(list(line[:-1]))
        tot = tot + int(tmp)

    return str(tot)[:10]

total = euler13()
print(total)
