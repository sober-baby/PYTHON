#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Question 1

void print_string(char **str, int *n)
{
    printf("Enter the number of digits: ");
    scanf("%d", n);
    *str = (char *)malloc((*n + 1) * sizeof(char)); // and is this one pointer or double pointer
    for (int c = 0; c < *n; c++)
    {
        printf("Enter your letter:");
        fflush(stdin);
        scanf("%c", &((*str)[c]));
    }
    (*str)[*n] = '\0';
}

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
    res++;
    while (*s2 != '\0')
    {
        *res = *s2;
        res++;
        s2++;
    }
    res++;
    *res = '\0';
    return (res - i1 - i2);
}

// Question 3

int strcmp(char *s1, char *s2)
{
    if (s1[0] == '\0' && s2[0] == '\0')
    {
        return 0;
    }
    if (s1[0] != s2[0])
    {
        return 1;
    }
    return strcmp(s1 + 1, s2 + 1);
}

// function that  takes in a sorted list of integers and a target, and returns both the first and
// the last index where target appears.


int main()
{
    
    /* Question 1, not really working rip
    int n;
    char *str;
    print_string(&str, &n);
    printf("%s", str);
    
 

    // Question 2
    char *str1 = "Hello";
    char *str2 = "World";
    //char *a = con_index(&str1, 5, &str2, 5);
    char *b = con_pointer(str1, 5, str2, 5);
    //printf("%s\n", a);
    printf("%s\n", b);
    */

    // Question 3
    char *s1 = "he";
    char *s2 = "wo";
    int a = strcmp(s1, s2);
    printf("%d", a);
    return 0;



}






