#include <cs50.h>
#include <stdio.h>

int n;

int main(void)
{
    do
    {
        n = get_int("Height:");
    }
    while (n < 1 || n > 8);
    
 for (int i=0;i<n;i++)
    {
       for (int s=n-1; s>i; s--)
            {
                printf(" ");
            } 
       for (int h = -1; h < i; h++)
        {
            printf("#");
        } 
        printf("\n");
    }
}
