#include <stdio.h>
#include <cs50.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>
#include <ctype.h>

// algorithm: ci = (pi + k) % 26

int main(int argc, string argv[])
{
    //check there is a key
    if (argv[1] || argc == 2)
    {
        for (int i = 0, n = strlen(argv[1]); i < n; i++)
        {
            if (!isdigit(argv[1][i]))
            {
                printf("Usage: ./caesar key");
                return 1;
            }
        }
        //change into an integer
        int k = atoi(argv[1]);

        if (argc == 2 && k > 0)
        {
            //get plaintext
            string plaintext = get_string("plaintext: ");
            int len = strlen(plaintext);
            // Create an array of the same length for the ciphered characters
            char ct[len];
            //print cipher
            printf("ciphertext: ");
            for (int i = 0; i < len; i++)
            {
                char c = plaintext[i];
                if (isupper(plaintext[i]))
                {
                    ct[i] = ((plaintext[i] + k) - 65) % 26 + 65;
                }
                else if (islower(plaintext[i]))
                {
                    ct[i] = ((plaintext[i] + k) - 97) % 26 + 97;
                }
                else
                {
                    ct[i] = plaintext[i];
                }
                printf("%c", ct[i]);

            }

            //new line
            printf("\n");
            return 0;
        }
        else
        {
            printf("Usage: ./caesar key");
            return 1;
        }
    }

    else
    {
        printf("Usage: ./caesar key");
        return 1;
    }
}