#!/usr/bin/python3

"""
    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""

import numpy as np

def isprime(num: int) -> bool:
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def euler7() -> int:
    tot = 1
    i = 3
    while True:
        if isprime(i):
            tot = tot + 1
            if tot == 10001:
                break
        i = i + 2
    return i

tot = euler7()
print(tot)
