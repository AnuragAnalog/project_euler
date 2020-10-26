"""

2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

"""


num=int(input('"Entre number" to find smallest multiple from 1 to  '))
multiple=num-1
for n in range(num-1 ,1,-1) :
    if multiple%n != 0:
        multiple=multiple*n

print(multiple)
