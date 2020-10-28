#!/usr/bin/python3

"""
    An irrational decimal fraction is created by concatenating the positive integers:

0.123456789101112131415161718192021...

It can be seen that the 12th digit of the fractional part is 1.

If dn represents the nth digit of the fractional part, find the value of the following expression.

d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000
"""

def euler40() -> int:
    i = 0
    limit = 1000000
    champ = ""
    while len(champ) < limit:
        i = i + 1
        champ = champ + str(i)
    p = 1
    for i in range(7):
        p = p * int(champ[10**i-1])
    return p

tot = euler40()
print(tot)
