


"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24. By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""


"""
NOTE: This code finds the correct answer, but it's heavily in need of optimization, as it takes a long time. Most probably in the checkSum function
"""

import math
l = 28123

def divisors(n):
    d=[1]
    for i in range (2, int((n**0.5))+1):
        if (n%i)==0:
            other=n//i
            if other ==i:
                pair=[i]
            else:
                pair= [i,other]
            d.extend(pair)
    return d

def check(n):
    return sum(divisors(n)) > n


abundantList=[]
for i in range (1,l):
    if check(i):
        abundantList.append(i)


def checkSum(nb):
    for a in abundantList:
        for b in abundantList:
            if a + b == nb:
                return False
            if a+b>nb:
                break
    return True


abundant_sum = 0
for i in range(12, l):
    if checkSum(i):
        abundant_sum += i
print(abundant_sum)
