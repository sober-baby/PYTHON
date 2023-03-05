#include <stdio.h>
#include <stdlib.h>
#include <string.h>

typedef struct student1{
char name[3];
int age;
} student1;

typedef struct student2{
    const char *name;
    const int *p_age;
} student2;

void change_name1_wrong(student1 s)
{
s.name[0] = 'b';
}
void change_name1_right_a(student1 *p_s)
{
p_s->name[0] = 'b'; // would not put a null character at the end
}
void change_name1_right_b(student1 *p_s)
{
strcpy(p_s->name, "b"); // would put a null character at the end
}
void change_name_python(student2 *p_s)
{
p_s->name = "b";
}

int main()
{
    student1 s = {"x", 20};
    change_name1_wrong(s);
    printf("%s", s.name);
    student2 *p_s = (student2*)malloc(sizeof(student2));
    int *p_age = (int*)malloc(sizeof(int));
    *p_age = 20;
    student2 temp = {"x", p_age};
    memcpy(p_s, &temp, sizeof(student2));
    change_name(p_s);

}


