#include <stdio.h>
#include <cs50.h>
#include <math.h>

long long num;
int numLength;
int digits[16];
int checkSum;

bool valid = false;

char buffer[16];

int main(void)
{
    //get the card number
    num = get_long("Enter a credit card number: ");

    //check the length
    numLength = floor(log10(num)) + 1;

    if (numLength > 16)
    {
        printf("INVALID\n");
        return 0;
    }

    //turn the number into an array of digits
    sprintf(buffer, "%lld", num);

    //convert the buffer into an array of integers
    for (int i = 0; i < numLength; i++)
    {
        digits[i] = buffer[i] - '0';
    }

    //Use Luhn’s Algorithm to find checksum
    for (int i = numLength - 2; i > -1; i -= 2)
    {
        int d = digits[i] * 2;

        if (d > 9)
        {
            checkSum += d - 9;
        }
        else
        {
            checkSum += d;
        }
    }

    for (int i = numLength - 1; i > -1; i -= 2)
    {
        checkSum += digits[i];
    }

    if (checkSum % 10 == 0)
    {
        valid = true;
    }

    // AmEx: starts with 34 or 37, and len = 15
    // VISA: starts with 4 and len = 13 || 16
    // MasterCard: starts with 51, 52, 53, 54, or 55 and len = 16
    if (valid)
    {
        if (numLength == 15)
        {
            if (digits[0] == 3)
            {
                if (digits[1] == 4 || digits[1] == 7)
                {
                    printf("AMEX\n");
                    return 0;
                }
            }
        }
        else if (digits[0] == 4)
        {
            if (numLength == 13 || numLength == 16)
            {
                printf("VISA\n");
                return 0;
            }
        }
        else if (digits[0] == 5)
        {
            if (numLength == 16)
            {
                if (digits[1] > 0 && digits[1] < 6)
                {
                    printf("MASTERCARD\n");
                    return 0;
                }
            }
        }
    }

    printf("INVALID\n");
    return 0;
}
