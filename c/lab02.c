#include <stdio.h>
#include <stdlib.h>
#include <string.h>
char strcat(char *destination, char *source)
{
    int i = 0;
    int j = 0;
    while (destination[i] != '\0') //【】也是dereference
    {
        i++;
    }
    while (source[j] != '\0')
    {
        i++;
        j++;
        destination[i] = source[j];
    }
    return destination;
}

char *strcatt(char **str1, int l1, char **str2, int l2) {
    char *res = (char *)malloc((l1 + l2 + 1) * sizeof(char));
    for (int i = 0; i < l1; i++) {
        res[i] = (*str1)[i];
    }
    for (int i = 0; i < l2; i++) {
        res[l1 + i] = (*str2)[i];
    }
    res[l1 + l2] = '\0';
    return res;
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
    char *str2 = "World";
    char *a = strcat(&str1, &str2);
    printf("%s", a);

    
    return 0;



}






