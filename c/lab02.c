#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/*Question 1;
void print_string(char **str, int *b)
{
    printf("Enter the amount of char that you will input: ");
    scanf("%d\n", *b);
    str = (*b)malloc(sizeof(char));
    for (int i = 0; i < *b; i++){
        printf("Enter a char in the string");
        scanf("%s\n", **str);
        str++;
    }
}
*/

// Question 2;
char *strcat(char *destination, const char *source)
{
    int i = 0;
    int j = 0;
    while (destination[i] != '\0')
    {
        i++;
    }
    while (source[i] != '\0')
    {
        i++;
        j++;
        destination[i] = source[j];
        
    }
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
   char str1[100] = "This is ", str2[] = "programiz.com";

   // concatenates str1 and str2
   // the resultant string is stored in str1.
   strcat(str1, str2);

   puts(str1);
   puts(str2);

   

   return 0;
}






