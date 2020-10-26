#include <stdio.h>
#include <math.h>

int main()
{
    int sq = 0, sum = 0;
    for (size_t i = 0; i < 101; i++)
    {
        sq = sq + pow(i,2);
        sum = sum + i;
    }
    printf("%.0f", pow(sum,2)-sq);
}