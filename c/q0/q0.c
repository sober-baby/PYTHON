#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "list.h"
#include "linkedlist.c"
#include "math.h"
//Write a function named quadx for calculating the roots of the quadratic equation

//ax^2+bx+c=0

//assume there are two different real roots

void quad_x(double a, double b, double c, double *r1, double *r2){
    *r1 = (-b + sqrt(b*b - 4*a*c))/(2*a);
    *r2 = (-b - sqrt(b*b - 4*a*c))/(2*a);
}


//Write a function, count_letters, that counts the number occurrences of each alphabetical letter
//found in a string. The function has two parameters: a string (i.e., char *) and an array of integers.
//The string should not be modified and can be any length. You may assume that the string is nullterminated and all letters are lower case. The string may contain
//characters that are not part of the
//alphabet (e.g., 0, 1, !, &, etc). The integer array has a size of 26, one for each letter in the alphabet.
//The first index corresponds to the letter 'a', the second index to the letter 'b', and so on. You may
//assume that, initially, all 26 elements in the array have a value of zero.

void count_letters(char *s, int counts[]){
    for (int i = 0; i < strlen(s); i++){
        if (s[i] >= 'a' && s[i] <= 'z'){
            int temp = s[i] - 'a';
            counts[temp]++;
        }
    }
}


//Use list.h and linkedlist.c from Lab 5.

//Write a function LL_is_in_list that takes in an integer, and returns 1 if the integer is found in the list, and 0 otherwise. 
//You may not use LL_get or list_get
int LL_is_in_list(LL *my_list, int x){
    node *cur = my_list->head;
    while(cur != NULL){
        if (cur->data == x){
            return 1;
        }
        cur = cur->next;
    }
    return 0;
}

int main(){
    //Test quad_x
    //double r1, r2;
    //quad_x(1, 2, 1, &r1, &r2);
    //printf("%f %f", r1, r2);
    //Test count_letters
    char s[] = "hello world";
    int counts[26];
    for (int i = 0; i < 26; i++){
        counts[i] = 0;
    }
    count_letters(s, counts);
    for (int i = 0; i < 26; i++){
        printf("%d ", counts[i]);
    }
    //Test LL_is_in_list
    //LL *my_list;
    //int data[] = {1, 2, 3, 4, 5};
    //create_LL_from_data(&my_list, data, 5);
    //printf("%d" , LL_is_in_list(my_list, 6)); 
}