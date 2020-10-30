using System;

namespace LargestPrimeFactor
{
    partial  class Euler003
    {
        public static void Main()
        {
            long testCase=600851475143,largestFactor=0,temp;
            temp = testCase;
            for (long i = 2; i <= Math.Sqrt(temp); i++)
            {
                while (temp%i==0)
                {
                    temp /= i;
                    largestFactor = i;
                }
            }
            if(temp==1)
            {
                Console.WriteLine(largestFactor);
            }
            else
            {
                Console.WriteLine(temp);
            }
        }
    }
}
