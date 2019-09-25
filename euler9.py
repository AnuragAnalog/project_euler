#!/usr/bin/python3

"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,
a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.
There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

def euler9() -> int:
    for a in range(1, 1001):
        for b in range(a, 1001-a):
            if a**2 + b**2 == (1000-a-b)**2:
                c = 1000-a-b
                return a*b*c

prod = euler9()
print(prod)
