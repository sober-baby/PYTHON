#include <stdio.h>

void swap(int *p_a, int *p_b)
{
    int temp = *p_a;
    *p_a = *p_b;
    *p_a = temp;
}

void set0(int *p_a)
{
    *p_a = 0; 
    //printf("%ud", sizeof(p_a)); //prints 8
}

int *make_array_wrong()
{
    int arr[5] = {1, 2, 3, 4, 5};
    return arr; //must not access something arr[0] outside the function
    // accessing the actual adress arr is not a problem, but arr is not anymore the address of anything in particular
}

int main()
{

    // can allocate a block of memory on the heap (as opposed to the stack)
    // heap: somewhere in the memory table
    // stack: in the locals frame of the function

    int *a = (int *)malloc(sizeof(int)*12); // a is now a pointer to a block of memory of size 12 * sizeof(int) bytes
                                            // which is enough to store 12 int
    a[6] = 12;
    free(a);
    // not using free results in a "memory leak"
    // blocks of memory that the computer thinks are sitll in use remain
    //


}
int main_old()
{
    int a = 5;
    a = 6;

    int *p_a = &a;
    *p_a = 7;
    //printf("%d", *p_a);

    int x = 7;
    int y = 8;
    swap(&x, &y);

    char *str = "Hello";
    //printf("%c\n", str[1]);

    //pointer arithmetic
    str + 1;
    //printf("%c\n", *(str + 1)); // prints e
    //printf("%c\n", *(str + 3)); // prints l
    // set0(arr); 

    //an array is a block of momory contaiing a sequence of elements of the same type

    int arr[5] = {1, 2, 3, 4, 5}; //a array has a pre-specified size
    char arr1[4] = "abc";
    char arr2[4] = {'a', 'b', 'c', '\0'};
    char arr3[3] = {'a', 'b', 'c'};
    printf("%s\n", arr3);
    arr[2] = 6;
    //printf("%ud, %ud\n", sizeof(arr), sizeof(arr[0]));//prints 20,4
    //printf("The number of elements in arr is %d\n", sizeof(arr) / sizeof(arr[0]));
    
    //pointer arithmetic in C is conscious of the type of the pointer
    // char *a // = 32
    // a + 1 is 33

    //int *a // = 32
    // a + 1 is 36

    //*(arr+1) and arr[i] are equivalent

}