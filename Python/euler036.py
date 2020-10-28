#!/usr/bin/python3

"""
    The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.
Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.
(Please note that the palindromic number, in either base, may not include leading zeros.)
"""

import numpy as np

def euler36() -> int:
    tot = 0
    for i in range(1, 10**6, 2):
        if str(i) == str(i)[::-1] and bin(i)[2:] == bin(i)[2:][::-1]:
            tot = tot + i

    return tot

tot = euler36()
print(tot)
