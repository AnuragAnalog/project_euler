#!/usr/bin/python3

"""
    Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
"""

def sum_proper_divisors(num: int) -> int:
    tot = 0
    for i in range(1, int(num//2)+1):
        if num%i == 0:
            tot = tot + i
    return tot

def euler21() -> int:
    amicable = set()
    for i in range(1, 10001):
        a = i
        b = sum_proper_divisors(a)
        c = b
        d = sum_proper_divisors(c)
        if a == d and a != b:
            amicable.add(a)
            amicable.add(b)
    return sum(amicable)

tot = euler21()
print(tot)
