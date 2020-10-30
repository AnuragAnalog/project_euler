#include <stdio.h>
#include <math.h>

int largestPrimeFactor(int n){ 
    if (n <= 1) {  
        return 0;  
    } 
    else {  
        int div = 2;  
    while (div < n) {  
        if (n % div != 0) {  
        div++;  
    } 
    else {  
        n = n / div;  
        div = 2;  
    }  
   }  
   return n;  
  }
}  

int main()
{
    int number;
    int result  = largestPrimeFactor(number);
    printf("tThe result is %d",number);

}

