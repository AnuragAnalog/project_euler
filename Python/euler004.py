#!/usr/bin/python3

"""
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

def euler4() -> int:
    maxi = 0

    for i in range(999, 99, -1):
        for j in range(999, 99, -1):
            if str(i*j) == str(i*j)[::-1]:
                if i*j > maxi:
                    maxi = i*j
    return maxi

maxi = euler4()
print(maxi)
