#include <stdio.h>
#include <stdlib.h>
#include <math.h>

int triplet();

int main()
{
    int      prod;

    prod = triplet();
    printf("%d\n", prod);

    exit(0);
}

int triplet()
{
    int        a, b, c;

    for (a = 1; a < 1001; a++)
    {
        for (b = a + 1; b < 1001 - a; b++)
        {
            if (pow(a, 2) + pow(b, 2) == pow(1000-a-b, 2))
            {
                c = 1000 - a - b;
                return a*b*c;
            }
        }
    }

    return -1;
}