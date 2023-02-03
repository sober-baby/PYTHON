#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Question 1
void print_string(char **str, int *b)
{
    printf("Enter the amount of char that you will input: ");
    scanf("%d\n", b);
    *str = (char*)malloc((*b+1) * sizeof(char));
    for (int i = 0; i < *b; i++){
        printf("Enter a char in the string");
        scanf("%c", *str[i]);
    }
}
*/

// Question 2
char *strcat(char **destination, char **source)
{
    int i = 0;
    int j = 0;
    while (*destination[i] != '\0') //【】也是dereference
    {
        i++;
    }
    while (*source[j] != '\0')
    {
        i++;
        j++;
        *destination[i] = *source[j];
    }
    return *destination;
}

// Question 2
char *my_strcpy(char *dest, const char *src) 
{
    int i = 0;
    while (src[i] != '\0')
    {
        dest[i] = src[i];
        i++;
    }
}


int main()
{
    
    /*
    // Question 1, not really working rip
    printf("Hello world");
    int n;
    char *str;
    print_string(&str, &n);
    printf("%s", str);
    free(str);
*/

    // Question 2
    char *str1 = "Hello";
    char *str2 = "World";s
    char *str3 = strcat(&str1, &str2);
    printf("%s", str3);
    free(str3);
    
    return 0;



}






