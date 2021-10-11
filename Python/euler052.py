#!/usr/bin/python3

"""
    It can be seen that the number, 125874, and its double, 251748, contain exactly the same digits, but in a different order.

Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x, contain the same digits.
"""

def same_digits(num: int) -> bool:
    for i in range(2, 6):
        if sorted(str(i*num)) != sorted(str((i+1)*num)):
            return False
    return True

def euler52() -> int:
    i = 1
    while True:
        if same_digits(i):
            break
        i = i + 1
    return i

tot = euler52()
print(tot)
