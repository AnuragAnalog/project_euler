#include <stdio.h>

int main()
{
    int a = 1, b = 2, c = 0, total = 0;
    while (a < 4000000)
    {
        if (a % 2 == 0)
        {
            total = total + a;
        }
        c = a + b;
        a = b;
        b = c;
    }
    printf("%d", total);
}