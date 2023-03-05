#include <stdio.h>
#include <stdlib.h>
#include <string.h>
// Question 2

char *con_index(char **s1, int i1, char **s2, int i2)
{
    char *res = (char *)malloc((i1 + i2 + 1) * sizeof(char));
    for (int i = 0; i < i1; i++)
    {
        res[i] = (*s1)[i];
    }
    for (int i = 0; i < i2; i++)
    {
        res[i1 + i] = (*s2)[i];
    }
    res[i1 + i2] = '\0';
    return res;   
}

char *con_pointer(char *s1, int i1, char *s2, int i2)
{
    char *res = (char *)malloc((i1 + i2 + 1) * sizeof(char));
    while (*s1 != '\0')
    {
        *res = *s1;
        res++;
        s1++;
    }
    while (*s2 != '\0')
    {
        *res = *s2;
        res++;
        s2++;
    }
    *res = '\0';
    return (res - i1 - i2 - 1);
}

// a , b ,c, d   


int main()
{
     // Question 2
    char *str1 = "Hello";
    char *str2 = "World";
    char *a = con_index(&str1, 5, &str2, 5);
    char *b = con_pointer(str1, 5, str2, 5);
    printf("%s\n", a);
    printf("%s\n", b);
}