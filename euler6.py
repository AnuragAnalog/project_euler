#!/usr/bin/python3

"""
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)^2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
"""

def euler6() -> int:
    sumof_sq = 0
    sqof_sum = 0

    for i in range(1,101):
        sumof_sq = sumof_sq + i**2
        sqof_sum = sqof_sum + i

    return sqof_sum**2 - sumof_sq

num = euler6()
print(num)
