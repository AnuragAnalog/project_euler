using System;

namespace LargestPalindromeProduct
{
    partial  class Euler004
    {
        public static void Main()
        {
            int imax=999,imin=100,jmax=990,jmin=900;
            for(int i=imax;i>=imin;i--){
                for(int j=jmax;j>=jmin;j-=11)
                {
                    if (isPalindrome(i*j))
                    {
                        System.Console.WriteLine(i*j+" "+i+" "+j);
                        Environment.Exit(0);                            
                    }
                }   
            }
        }

        private static bool isPalindrome(int number)
        {
            bool result = false;
            int temp = number;
            int sum = 0,rem;
            while (temp>0)
            {
                rem=temp % 10;
                sum = (10 * sum) + rem;
                temp /= 10;
            }
            if (sum==number)
            {
                result = true;
            }    
            return result;
        }
    }
}
