"""

Starting with the number 1 and moving to the right in a clockwise direction a 5 by 5 spiral is formed as follows:

                21 22 23 24 25
                20  7  8  9 10
                19  6  1  2 11
                18  5  4  3 12
                17 16 15 14 13

It can be verified that the sum of the numbers on the diagonals is 101.

What is the sum of the numbers on the diagonals in a 1001 by 1001 spiral formed in the same way?

"""


#----------------------------------------------------------------
#taking size as input, so that 2D matrix is of sizeXsize 
size=int(input())

# code for adding elements of diadonal 1
n,sumDiagonal1=1,1
for i in range(2,2*size,2):
    n=n+i
    sumDiagonal1+=n
#----------------------------------------------------------------



#----------------------------------------------------------------
# code for adding elements of diadonal 2
m,sumDiagonal2=1,0
count=1
while True:
    for j in range(4,(4*(size//2))+1,4):
        m=m+j
        sumDiagonal2+=m
        count+=1
        if count==size:
            break
        m=m+j
        sumDiagonal2+=m
        count+=1
        if count==size:
            break
    break
#-----------------------------------------------------------------



print(sumDiagonal1+sumDiagonal2)
