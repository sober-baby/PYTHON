#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void set_int1(int x)
{
x = 42;
}

void set_int2(int *p_x)
{
*p_x = 42;
}

typedef struct student1{
char name[200];
char student_number[11];
int year;
} student1;

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
        printf("Error: name too long");
        return;
    }
    strcpy(p_s->name, p_name);
}

// function that frees all the memory used for student1

void free_block1(student1 **p_p_s)
{
    free((*p_p_s)->name);
    free((*p_p_s)->student_number);
    free((*p_p_s)->year);
    free(p_p_s);
}

int main()
{

    // Question 1
    int x = 0;
    set_int1(x);
    printf("Does not change: %d\n", x);
    set_int2(&x);
    printf("Does change %d\n", x);

    // Question 2
    student1 s1;
    strcpy(s1.name, "James");
    set_default_name(s1.name);
    strcpy(s1.student_number, "1234567890");
    s1.year = 1;
    printf("Name: %s\n", s1.name);
    printf("Student Number %d\n", s1.student_number);
    printf("Year: %d\n", s1.year);


    
}


