using System;

namespace EvenFibonacciNumbers
{
    partial  class Euler002
    {
        public static void Main()
        {
            long limit=4000000;
            long evenFibonacciSum = 2;
            for( 
                long termN=0, term0=0,term1=2; 
                termN<limit;
                termN = 4 * term1 + term0, term0=term1, term1=termN 
                )
            {
                evenFibonacciSum += termN;
            }
            Console.WriteLine(evenFibonacciSum);
        }
    }
}
