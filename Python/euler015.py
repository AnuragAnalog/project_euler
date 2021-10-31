
#!/usr/bin/python3

"""
Starting at the top left corner of a 2×2 grid, there are 6 routes (without backtracking) to the bottom right corner.
How many routes are there through a 20×20 grid?
"""

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
        
def routes(n,m):
  return factorial(n+m) // factorial(n) // factorial(m)
 
 
print routes(20,20)
