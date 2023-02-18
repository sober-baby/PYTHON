#include <stdio.h>

int main()
{
    // store the number in pointer to a sum
    int *sum = 10;
    int total = 10;
    // add the value of sum to total
    total += *sum;
    printf("%d", total);

}