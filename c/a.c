#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printstr(int *i, char **str) {
    printf("Enter the number of digits: ");
    scanf("%d", i);
    printf("%d", *i);
    *str = (char *)malloc((*i+1) * sizeof(char)); // and is this one pointer or double pointer
    for (int c = 0; c < *i; c++) {
        printf("Enter your letter:");
        fflush(stdin);
        scanf("%c", &((*str)[c]));
    }
    (*str)[*i] = '\0';
}
char* my_strcpy(char* dest, const char* src) 
{
    // cope the string to the location dest
    // assume that there is enough space in dest to copy src + the trailing NULL . 
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