"""

The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?

"""

from math import sqrt
def bigPrime(n):
    for i in range(int(sqrt(n)),1,-1):
        for j in range(2,int(sqrt(i)) +1):
            if i%j == 0 :
                break
        else:
            # arr.append(i)
            if n%i==0:
                print(i)
                return

num=int(input())
bigPrime(num)
