#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int compare(int *p_a, int *p_b)
{
    int *p_a_i = (int *)p_a;
    int *p_b_i = (int *)p_b;
    return *p_a_i - *p_b_i;
}


// function that takes in a string and returns a double
double my_atof(char *str){
    int i = 0;
    int sign = 1;
    double result = 0;
    double decimal = 0;
    int decimal_flag = 0;
    int decimal_count = 0;
    while(str[i] != '\0'){
        if(str[i] == '-'){
            sign = -1;
        }
        else if(str[i] == '.'){
            decimal_flag = 1;
        }
        else if(decimal_flag == 0){
            result = result * 10 + (str[i] - '0');
        }
        else{
            decimal = decimal * 10 + (str[i] - '0');
            decimal_count++;
        }
        i++;
    }
    for(int i = 0; i < decimal_count; i++){
        decimal = decimal / 10;
    }
    return sign * (result + decimal);

}

// midterm 2016 Question 2:

int **initStructure(int r, int *a)
{
    int i, j;
    int **s = (int **)malloc(sizeof(int *) * r);
    for (i = 0; i < r; i++)
    {
        s[i] = (int *)malloc(sizeof(int) * a[i]);
        for (j = 0; j < a[i]; j++)
        { 
            s[i][j] = 0;
        }
    }
    return s;
}

typedef struct student
{
    char *name; 
    
    /* data */
}student;

int main()
{
    student s1;
    s1.name = (char *)malloc(sizeof(char) * 10);
    s1.name = "hello";
    printf("%s", s1.name);
    double d = my_atof("123.456");
    printf("%f", d);

    /*
    int c[] = {3, 4, 2};
    int **s = initStructure(3, c);
    int i, j;
    for (i = 0; i < 3; i++)
    {
    for (j = 0; j < c[i]; j++)
    {
        printf("%d ", s[i][j]);
    }
    printf("\n");
    }
    for (i = 0; i < 3; i++)
    {
        free(s[i]);
    }
    free(s);
    */
}
