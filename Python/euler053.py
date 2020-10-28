#!/usr/bin/python3

"""
    There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, 5C3 = 10.

In general, nCr = n!/r!(n−r)!, where r≤n, n! = n × (n−1) × ... × 3 × 2 × 1, and 0! = 1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr)
for 1 ≤ n ≤ 100, are greater than one-million?
"""

def fact(n: int) -> list:
    fac = [0 for i in range(101)]
    fac[0] = 1
    fac[1] = 1
    for i in range(2, n+1):
        fac[i] = i * fac[i-1]
    return fac

def euler53() -> int:
    tot = 0
    for n in range(1, 101):
        fac = fact(n)
        for r in range(1, n+1):
            if fac[n]/(fac[r]*fac[n-r]) > 1000000:
                tot = tot + 1
    return tot

tot = euler53()
print(tot)
