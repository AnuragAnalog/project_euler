#!/usr/bin/python3

"""
    Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

    1634 = 1^4 + 6^4 + 3^4 + 4^4
    8208 = 8^4 + 2^4 + 0^4 + 8^4
    9474 = 9^4 + 4^4 + 7^4 + 4^4

As 1 = 1^4 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
"""

def power5(n: int) -> int:
    return n**5

def euler30() -> int:
    tot = 0
    for i in range(2*2**5, 6*9**5):
        tmp = map(int, list(str(i)))
        sum5 = sum(map(power5, tmp))
        if sum5 == i:
            tot = tot + i
    return tot

tot = euler30()
print(tot)
