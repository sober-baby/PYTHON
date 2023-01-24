#include <stdio.h>
#include <stdlib.h>
#include <string.h>

char* my_strcpy(char* dest, const char* src)
{
    // cope the string to the location dest
    // assume that there is enough space in dest to copy src + the trailing NULL
    int i = 0;
    while (src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }

    /*

    for (int i = 0; src[i] != '\0'; i++)
    {
        dest[i] = src[i];
    }

    */

    
}