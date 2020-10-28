#!/usr/bin/python3

"""
    The number, 1406357289, is a 0 to 9 pandigital number because it is made up of each of the digits 0 to 9 in some order, but it also has a rather interesting sub-string divisibility property.

Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way, we note the following:

    * d2d3d4 = 406 is divisible by 2
    * d3d4d5 = 063 is divisible by 3
    * d4d5d6 = 635 is divisible by 5
    * d5d6d7 = 357 is divisible by 7
    * d6d7d8 = 572 is divisible by 11
    * d7d8d9 = 728 is divisible by 13
    * d8d9d10 = 289 is divisible by 17

Find the sum of all 0 to 9 pandigital numbers with this property.
"""

from itertools import permutations

def euler43() -> int:
    tot = 0
    permut = permutations(range(10), 10)
    for pandig in permut:
        val = "".join(map(str, pandig))
        if len(val) < 10:
            continue
        else:
            con1 = (int(val[1:4])%2 == 0)
            con2 = (int(val[2:5])%3 == 0)
            con3 = (int(val[3:6])%5 == 0)
            con4 = (int(val[4:7])%7 == 0)
            con5 = (int(val[5:8])%11 == 0)
            con6 = (int(val[6:9])%13 == 0)
            con7 = (int(val[7:10])%17 == 0)
            if con1 and con2 and con3 and con4 and con5 and con6 and con7:
                tot = tot + int(val)
    return tot

tot = euler43()
print(tot)
