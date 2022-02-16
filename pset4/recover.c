#include <stdio.h>
#include <stdlib.h>
#include <stdint.h>

#define BUFFER_SIZE 512

typedef uint8_t BYTE;
typedef enum {false, true} bool;


int main(int argc, char *argv[])
{
    // check for proper usage
    if (argc != 2)
    {
        printf("Usage: recover.c image");
        return 1;
    }

    //open memory card file
    FILE *ptr1 = fopen(argv[1], "r");

    // read 512 bytes into a buffer
    unsigned char buffer[BUFFER_SIZE];

    // set number of files
    int file_count = 0;

    // create a variable to check if a file is open
    bool file_open = false;

    // name of my image pointer
    FILE *img_ptr = NULL;

    while (fread(&buffer, BUFFER_SIZE, 1, ptr1) == 1)
    {
        //check if it's a jpeg
        if (buffer[0] == 0xff && buffer[1] == 0xd8 && buffer[2] == 0xff && (buffer[3] & 0xf0) == 0xe0)
        {
            // check if there's already a file open
            if (file_open == true)
            {
                fclose(img_ptr);
            }
            else
            {
                // new image
                file_open = true;
            }

            //create a new jpeg file
            char file_name[8];
            sprintf(file_name, "%03i.jpg", file_count);
            file_count++;
            img_ptr = fopen(file_name, "w");
        }

        if (file_open == true)
        {
            fwrite(&buffer, BUFFER_SIZE, 1, img_ptr);
        }
    }

    // close the files
    fclose(ptr1);
    fclose(img_ptr);

    return 0;
}
