#include <stdio.h>
#include <stdlib.h>

//write a function that uses recursion to print the factorial of a number
int factorial(int n)
{
    if (n == 0)
        return 1;
    else
        return n * factorial(n - 1);
}

int main()
{
    int* p_a = 0; 
    // *p_a = 1; crashes
    p_a = (int*)malloc(sizeof(int)); // p_a is now a pointer to a block of memory of size 12 * sizeof(int) bytes
                                             // which is enough to store 12 int
    printf("%d\n", *p_a); //could be anything (but won't crash)
    *p_a = 1;
    free(p_a); //if done after p_a = &b (1) will crash

    int b = 2;
    p_a = &b; //p_a is now a pointer to b
    *p_a = 3; //b is now 3, *p_a is 3
    b = 42; //b is now 42, *p_a is 42
    printf("%d", *p_a); //prints 42

    int c[] = {5 , 8 , 10};
    p_a = c;
    p_a[0]; //5
    p_a++; //p_a is now a pointer to c[1], adress to the next integer in the array
    p_a[0]; //8
    *(p_a - 1); //5

    *p_a = 9;
    &(*p_a); //adress of the integer pointed to by p_a

    int** p_p_a = 0; // a variable of type adress of adress of int
    p_p_a = (int*)malloc(sizeof(int*)); // p_p_a is now a pointer to a block of memory of size 12 * sizeof(int) bytes
                                             // which is enough to store 12 int
    // *p_p_a = 1; //will crash // same as *(*p_p_a) = 1
    *p_p_a = (int*)malloc(sizeof(int)); // valid adress
    **p_p_a = 1; // fine, same as p_p_a[0][0] = 1
    free(*p_p_a); //free the memory pointed to by p_p_a
    free(p_p_a); //free the memory pointed to by p_p_a
    // if we free p_p_a first, *p_p_a is not accessible anymore











}