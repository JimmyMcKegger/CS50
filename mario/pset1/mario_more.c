#include <stdio.h>
#include <cs50.h>

int main(void)
{
    // get user's number
    int n;
    do
    {
        n = get_int("Height: ");
    }
    while (n < 1 || n > 8);

    int i = 1;

    while (i <= n)
    {
        //initial spaces

        for (int s = i; s < n; s++)
        {
            printf(" ");
        }

        //first side
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        //middle spaces
        for (int t = 0; t < 2; t++)
        {
            printf(" ");
        }

        //other side
        for (int j = 1; j <= i; j++)
        {
            printf("#");
        }

        printf("\n");
        i++;
    }
}
