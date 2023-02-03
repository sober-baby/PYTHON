#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include "header.h"

void set_int1(int x)
{
x = 42;
}

void set_int2(int *p_x)
{
*p_x = 42;
}


// function that sets the name to "Default"
void set_default_name(student1 *p_s)
{
    strcpy(p_s->name, "Default Name");
}   

// function that creates a block of memory for the students
void create_block1(student1 **p_p_s, int n_students)
{
    *p_p_s = (student1 *)malloc(n_students * sizeof(student1));
}

void set_name(student1 *p_s, char *p_name)
{
    if (strlen(p_name) > 199)
    {
        strncpy(p_s->name, p_name, 199);
        return;
    }
    strcpy(p_s->name, p_name);
}

// function that frees all the memory used for student1

void free_block1(student1 *p_p_s)
{
    free(p_p_s->name);
    free(p_p_s->student_number);
    free(p_p_s->year);
    free(p_p_s);
}

typedef struct student2{
    char *name;
    char *student_number;
    int year;
} student2;

void create_block2(student2 **p_p_s, int n_students)
{
    (*p_p_s)->name = 0;
    (*p_p_s)->student_number = 0;
}

void set_name2(student2 *p_p_s, char *p_name)
{
    (p_p_s)->name = (char *)malloc((strlen(p_name) + 1) * sizeof(char));
    strncpy((p_p_s)->name, p_name, strlen(p_name));
}

void destroy_block2(student2 *p_p_s)
{
    free(p_p_s->name);
    free(p_p_s->student_number);
    free(p_p_s->year);
    free(p_p_s);
}


int main()
{

    int x = 0;
    set_int1(x);
    //printf("Does not change: %d\n", x);
    set_int2(&x);
    //printf("Does change %d\n", x);

    // Question 2
    student1 s1;
    student2 s2;
    strcpy(s1.name, "James");
    set_default_name(&s1);
    strcpy(s1.student_number, "123450");
    s1.year = 1;
    printf("Name: %s\n", s1.name);
    printf("Student Number %s\n", s1.student_number);
    printf("Year: %d\n", s1.year);

    set_name(&s1, "Tyrone");
    //printf("Name: %s\n", s1.name);
    //set_name2(s2.name, "Tyrone");
    //printf("Name: %s\n", s2.name);





    
}


