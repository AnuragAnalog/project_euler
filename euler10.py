#!/usr/bin/python3

"""
    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""

import numpy as np

def isprime(num: int) -> bool:
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def euler10() -> int:
    tot = 2
    i = 3
    while i < 2000000:
        if isprime(i):
            tot = tot + i
        i = i + 2
    return tot

tot = euler10()
print(tot)
