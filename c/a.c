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

    dest[i] = '\0';

    // at this poiint dest is not a valid string -- not terminated with a NULL

    /*

    for (int i = 0; src[i] != '\0'; i++)
    {
        dest[i] = src[i];
    }

    */
   i = 0;
    do
    {
        dest[i] = src[i];
        i++; //runs at least once
    } while (src[i-1] != '\0'); 

    
}

// The expressoin x = y has a value and an effect
// the effect si put y into x
// the value is y
char* my_strcpy_fancy(char* dest, char* src)
{
    char *old_dest = dest; // save the original value of dest
    while(*dest++ = *src++); //might be on midterm
    return old_dest;
}

void get_int_arr_from_input(int **p_arr, int *p_n)
{
    int n;
    printf("Number of elements that are coming: ");
    scanf("%d", &n);
    
    *p_arr = (int*)malloc(n * sizeof(int));
    for (int i = 0; i < n; i++)
    {
        printf("Enter element %d: ", i);
        scanf("%d", &(*p_arr)[i]);
    }


    //get the number of integers n in the input
    // then get n intergeres from the input

}
int main()
{       
    int *my_arr;
    int n;
    get_int_arr_from_input(&my_arr, &n);

    for (int i = 0; i < n; i++)
    {
        printf("%d ", my_arr[i]);
    }

}
int main1()
{
    int a = 0;
    scanf("%d", &a);
    printf("You just inputted %d\n", a);

    char* p_a = (char*)malloc(100); 
    int* int_p_a  = (int*)malloc(sizeof(int)); 
    scanf("%s", p_a);


}
int main2()
{
    char s1[100];
    char s2[] = "abc";
    printf("%s", my_strcpy(s1, s2)); 

}