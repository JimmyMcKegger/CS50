#include "helpers.h"
#include <math.h>
#define MAX 1000

// Convert image to grayscale
void grayscale(int height, int width, RGBTRIPLE image[height][width])
{
    //nested loops to set red Green and Blue values are all the same (avg of the 3 values)
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            //find average
            float avg = ((round(r) + round(g) + round(b)) / 3);
            int a = round(avg);

            //reassign colours
            image[i][j].rgbtRed = a;
            image[i][j].rgbtGreen = a;
            image[i][j].rgbtBlue = a;
        }
    }
    return;
}

// Convert image to sepia
void sepia(int height, int width, RGBTRIPLE image[height][width])
{
    //nested loops
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int r = image[i][j].rgbtRed;
            int g = image[i][j].rgbtGreen;
            int b = image[i][j].rgbtBlue;

            //find sepia values
            int sepiaRed = round((0.393 * r) + (0.769 * g) + (0.189 * b));
            int sepiaGreen = round((0.349 * r) + (0.686 * g) + (0.168 * b));
            int sepiaBlue = round((0.272 * r) + (0.534 * g) + (0.131 * b));

            //Cap values at 255
            if (sepiaRed > 255)
            {
                sepiaRed = 255;
            }
            if (sepiaGreen > 255)
            {
                sepiaGreen = 255;
            }
            if (sepiaBlue > 255)
            {
                sepiaBlue = 255;
            }

            //Apply sepia
            image[i][j].rgbtRed = sepiaRed;
            image[i][j].rgbtGreen = sepiaGreen;
            image[i][j].rgbtBlue = sepiaBlue;
        }
    }
    return;
}

// Reflect image horizontally
void reflect(int height, int width, RGBTRIPLE image[height][width])
{
    //make arrays
    int r[MAX], g[MAX], b[MAX];
    //nested loops
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            r[j] = image[i][j].rgbtRed;
            g[j] = image[i][j].rgbtGreen;
            b[j] = image[i][j].rgbtBlue;
        }

        //set end position
        int w = 0;

        //loop back over re-assigning the new arrays
        for (int j = width - 1; j >= 0; j--)
        {
            image[i][j].rgbtRed = r[w];
            image[i][j].rgbtGreen = g[w];
            image[i][j].rgbtBlue = b[w];
            w++;
        }
    }
    return;
}

// Blur image
void blur(int height, int width, RGBTRIPLE image[height][width])
{
    // make a new image to prevent blurred tiles from throwing off the next count
    RGBTRIPLE blurImage[height][width];
    //nested loops
    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            int totalRed = 0;
            int totalBlue = 0;
            int totalGreen = 0;
            float counter = 0.0;

            blurImage[i][j] = image[i][j];

            //top left
            if (i - 1 >= 0 && j - 1 >= 0)
            {
                totalRed += image[i - 1][j - 1].rgbtRed;
                totalGreen += image[i - 1][j - 1].rgbtGreen;
                totalBlue += image[i - 1][j - 1].rgbtBlue;
                counter++;
            }

            //top center
            if (i - 1 >= 0)
            {
                totalRed += image[i - 1][j].rgbtRed;
                totalGreen += image[i - 1][j].rgbtGreen;
                totalBlue += image[i - 1][j].rgbtBlue;
                counter++;
            }

            //top right
            if (i - 1 >= 0 && j + 1 < width)
            {
                totalRed += image[i - 1][j + 1].rgbtRed;
                totalGreen += image[i - 1][j + 1].rgbtGreen;
                totalBlue += image[i - 1][j + 1].rgbtBlue;
                counter++;
            }

            //right
            if (j + 1 < width)
            {
                totalRed += image[i][j + 1].rgbtRed;
                totalGreen += image[i][j + 1].rgbtGreen;
                totalBlue += image[i][j + 1].rgbtBlue;
                counter++;
            }
            //bottom right
            if (i + 1 < height && j + 1 < width)
            {
                totalRed += image[i + 1][j + 1].rgbtRed;
                totalGreen += image[i + 1][j + 1].rgbtGreen;
                totalBlue += image[i + 1][j + 1].rgbtBlue;
                counter++;
            }
            //bottom center
            if (i + 1 < height)
            {
                totalRed += image[i + 1][j].rgbtRed;
                totalGreen += image[i + 1][j].rgbtGreen;
                totalBlue += image[i + 1][j].rgbtBlue;
                counter++;
            }
            //bottom left
            if (i + 1 < height && j - 1 >= 0)
            {
                totalRed += image[i + 1][j - 1].rgbtRed;
                totalGreen += image[i + 1][j - 1].rgbtGreen;
                totalBlue += image[i + 1][j - 1].rgbtBlue;
                counter++;
            }
            //left
            if (j - 1 >= 0)
            {
                totalRed += image[i][j - 1].rgbtRed;
                totalGreen += image[i][j - 1].rgbtGreen;
                totalBlue += image[i][j - 1].rgbtBlue;
                counter++;
            }

            //middle
            totalRed += image[i][j].rgbtRed;
            totalGreen += image[i][j].rgbtGreen;
            totalBlue += image[i][j].rgbtBlue;
            counter++;

            float rr, rg, rb;
            rr = totalRed / counter;
            rg = totalGreen / counter;
            rb = totalBlue / counter;


            blurImage[i][j].rgbtRed = round(rr);
            blurImage[i][j].rgbtGreen = round(rg);
            blurImage[i][j].rgbtBlue = round(rb);

        }
    }

    for (int i = 0; i < height; i++)
    {
        for (int j = 0; j < width; j++)
        {
            //re-assign the blurred pixels to the image
            image[i][j].rgbtRed = blurImage[i][j].rgbtRed;
            image[i][j].rgbtGreen = blurImage[i][j].rgbtGreen;
            image[i][j].rgbtBlue = blurImage[i][j].rgbtBlue;
        }
    }

    return;
}
