#include<stdio.h>  
 int main()    
{    
    int n,sum=0,m;    
    n = pow(2,1000);
    while(n>0)    
    {    
        m=n%10;    
        sum=sum+m;    
        n=n/10;    
    }    
    printf("%d",sum);    
    return 0;  
}   