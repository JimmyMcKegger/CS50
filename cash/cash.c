#include <cs50.h>
#include <stdio.h>
#include <math.h>

float f;
int n; //amount in cents
int coins;
int i; //counter

int main(void)
{
    do

    // get a float from the user
    {
    f = get_float("Amount paid:");
    }

    while(f <= 0);

coins = 0;


// convert f to an integer

n = round(f * 100);
// count out coins
if (n >= 1)
{
        for (i=0; n >= 25; coins++)
        {
            n = (n - 25);
        }
        
        for (i=0; n >= 10; coins++)
        {
            n = (n - 10);
        }
    
        for (i=0; n >= 5; coins++)
        {
            n = (n - 5);
        }
        for (i=0; n >= 1; coins++)
        {
            n = (n - 1);
        }
}
// print out the number of coins to return as change
printf("%i\n", coins);

}
