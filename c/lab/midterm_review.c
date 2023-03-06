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
double my_atof(const char *str)
{
    int i = 0;
    while(str[i] != "="){
        i++;
    }
    i++;

    double result = 0;
    int sign = 1;
    if(str[i] == "-"){
        sign = -1;
        i++;
    }
    while(str[i] != "."){
        result = result * 10 + (str[i] - '0');
        i++;
    }
    i++;
    double pow10 = 0.1;
    while(str[i] != "\n"){
        result += (str[i] - '0') * pow10;
        pow10 *= 0.1;
    }
    return result * sign;
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
