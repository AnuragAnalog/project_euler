#!/usr/bin/python3

"""
    2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.
What is the sum of the digits of the number 2^1000?
"""

def euler16() -> int:
    tot = sum(list(map(int, list(str(2**1000)))))

    return tot

total = euler16()
print(total)
