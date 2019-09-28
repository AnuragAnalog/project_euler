#!/usr/bin/python3

"""
    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.
Find the sum of all numbers which are equal to the sum of the factorial of their digits.
Note: as 1! = 1 and 2! = 2 are not sums they are not included.
"""

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * fact(n-1)

def euler34() -> int:
    tot = 0
    for i in range(1, 10**6):
        if i in [1, 2]:
            continue
        l = list(map(int, list(str(i))))
        if i == sum(list(map(fact, l))):
            tot = tot + i
    return tot

tot = euler34()
print(tot)
