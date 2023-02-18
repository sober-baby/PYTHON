#include <stdio.h>
#include <string.h>

typedef struct uoft_student
{

    char st_number_str[11];
    int faculty_num;

    /* data */
    // st number amd facilty number are fields

}uoft_student;

typedef struct waterloo_student{
    char *str_number_str;

}waterlooser;

void change_w_id(waterlooser w)
{
    w.str_number_str = (char *)malloc(5 * sizeof(char));
    strcpy(w.str_number_str, "666");
}

void print_uoft_student(struct uoft_student s)
{
    printf("student number is %s\n", s.st_number_str);
    printf("faulty number is %d\n", s.faculty_num);
}

void switch_faculty_wrong(uoft_student s)
{
    s.faculty_num = 1; // this is a local variable, it will not change the original one
    
}

void drop_to_artsci(uoft_student *p_s)
{
    (*p_s).faculty_num = 1;
    
}

void create_waterlooser(waterlooser **p_p_w)
{
    *p_p_w = (waterlooser *)malloc(sizeof(waterlooser));
    (*p_p_w)->str_number_str = (char *)malloc(5 * sizeof(char));
    strcpy((*p_p_w)->str_number_str, "123");
}


typedef int BOOL; // typedef is a keyword that allows you to create an alias for a data type
// STH* a;
// a->x === (a).x
int main(){
    waterlooser *p_w;
    BOOL t = 0;
    struct uoft_student s;
    s.faculty_num = 0;
    printf("faulty number is %d\n", s.faculty_num);
    strcpy(s.st_number_str, "456456");
    printf("student number is %s\n", s.st_number_str);
    printf("%d", s.faculty_num);

    char abc[5];
    abc[2] = 'x';
    strcpy(abc, "xyz");

    
}