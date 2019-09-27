#!/usr/bin/python3

"""
    The number, 197, is called a circular prime because all rotations of the digits: 197, 971, and 719, are themselves prime.
There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37, 71, 73, 79, and 97.
How many circular primes are there below one million?
"""

import numpy as np

def isprime(num: int) -> bool:
    for i in range(2, int(np.sqrt(num))+1):
        if num%i == 0:
            return False
    return True

def rotate(num: int) -> set:
    rot = {num}
    length = len(str(num))
    k = 0
    while k < length:
        tmp = list(str(num))
        dig = tmp[0]
        tmp[:] = tmp[1:]
        tmp.append(dig)
        num = ''.join(tmp)
        rot.add(int(num))
        k = k + 1

    return rot

def euler35() -> int:
    tot = 0
    c_primes = [2]
    flag = False
    for i in range(3, 10**6, 2):
        if isprime(i):
            flag = True
            tmp = set()
            cps = rotate(i)
            for x in cps:
                if isprime(x):
                    tmp.add(x)
                else:
                    flag = False
                    break
        if flag:
            c_primes.extend(list(tmp))

    return len(set(c_primes))

tot = euler35()
print(tot)
