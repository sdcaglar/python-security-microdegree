#include <stdio.h>
#include "factorial_functs.h"

double pi_var = 3.14;

//factorial calculation
long long int factorial(long long int num)
{
   if(num <= 1)
     return 1;
   else
     return (num * factorial(num - 1));
}

//modulus retriever
int get_modulus(int num1, int num2)
{
   return (num1 % num2);
}

