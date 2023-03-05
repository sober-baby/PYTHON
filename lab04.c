#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <ctype.h>
// code that reads from file in c and stores in array

int my_atoi(const char *str)
{
    int i = 0;
    int sign = 1;
if(str[i] == "-"){
    sign = -1;
    i++;
}
int result = 0;
    while(str[i] >= '0' && str[i] <= '9'){
        result = result * 10 + (str[i] - '0');
        i++;
}
return result * sign;
}

float my_atof(const char *str){
    int i = 0;
    int sign = 1;
    if(str[i] == "-"){
        sign = -1;
        i++;
    }
    int result = 0;
    while(str[i] >= '0' && str[i] <= '9'){
        result = result * 10 + (str[i] - '0');
        i++;
    }
    if(str[i] == "."){
        i++;
    }
    int after = 0;
    int count = 0;
    while(str[i] >= '0' && str[i] <= '9'){
        after = after * 10 + (str[i] - '0');
        i++;
        count++;
    }
    while(count > 0){
        after = after / 10;
        count--;
    }
    return (result + after) * sign;
}

int main()
{
    FILE *ptr;
    ptr = fopen("lab04testing.txt", "r");
    char name[100];
    char e;
    char num[100];
    int sum = 0;

    fscanf(ptr, "%s %c %s/n", &name, &e, &num);

    fscanf(ptr, "%s %c %s/n", &name, &e, &num); 

    // while(fscanf(ptr, "%s %c %s/n", &name, &e, &num) != NULL){
    //     printf("hi");
    //     sum += my_atoi(num);
    // }
    // printf("%d", sum);
}

