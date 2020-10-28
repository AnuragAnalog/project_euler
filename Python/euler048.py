#!/usr/bin/python3

"""
    The series, 1^1 + 2^2 + 3^3 + ... + 10^10 = 10405071317.

Find the last ten digits of the series, 1^1 + 2^2 + 3^3 + ... + 1000^1000.
"""

def euler48() -> int:
    tot = 0
    for num in range(1, 1001):
        tot = tot + num**num
    return tot%(10**10)

tot = euler48()
print(tot)
