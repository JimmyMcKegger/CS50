#include <stdio.h>
#include <cs50.h>

int collatz(int n);
int steps;

int main(void)
{
  // ask for the number
  int n = get_int("number: ");
  
  steps = 0;
  // call function
  collatz(n);
  
  // print the results
  printf("Steps: %d\n", steps);

}

int collatz(int n)
{
  // base case
  if (n == 1)
  {
    return 0;
  }
  // even numbers
  else if ((n % 2) == 0)
  {
    steps++;
    return 1 + collatz (n / 2);
  }
  // odd numbers
  else
  {
    steps++;
    return 1 + collatz((3 * n) + 1);
  }
}