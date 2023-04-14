/*
#if !defined(PYINTEGER_H)
#define PYINTEGER_H
// Q5

// Implement pyinteger ADT
// add
// plusplus
// suppport an arbitrary number of digits
// just non-negative integers

typedef struct pyinteger {
    int *digits;
    int num_digits;
    int capacity;
} pyinteger;

void plusplus(pyinteger *pyint);
void add(pyinteger *pyint1, pyinteger *pyint2);
void create_integer(pyinteger **pyint, int num);
#endif

*/

#include "pyinteger.h"
void create_integer(pyinteger **pyint, int n){
    // figure how many digits
    // allocate that many digits
    // put n into the digits
    *pyint = (pyinteger *)malloc(sizeof(pyinteger));
    (*pyint) -> capacity = int(log10(n)+0.5) + 1;
    (*pyint) -> digits = (int *)malloc(sizeof(int) * (*pyint) -> capacity);
    for(int loc = (*pyint) -> capacity - 1; loc >= 0; loc--){
        (*pyint) -> digits[loc] = n % 10;
        n = n / 10;
    }

void plusplus(pyinteger *pyint){
    for(int loc = pyint -> num_digits - 1; loc >= 0; loc--){
        if(pyint -> digits[loc] == 9){
            pyint -> digits[loc] = 0;
        }
        else{
            pyint -> digits[loc] += 1;
            break;
        }
    }
    if(loc == -1){
        pyint -> num_digits += 1;
        if(pyint->num_digits > pyint->capacity){
            pyint->capacity *= 2;
            pyint->digits = (int *)realloc(pyint->digits, sizeof(int) * pyint->capacity);
        }
    }
void add(pyinteger *n1, pyinteger *n2)
{
    int carry = 0;
    int loc = 0;
    if(n1 -> num_digits < n2 -> num_digits){
        pyinteger *temp = n1;
        n1 = n2;
        n2 = temp;
    }

    int offset = n1 -> num_digits - n2 -> num_digits;
}


}
