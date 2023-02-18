int f(int a)
{
    a = 5;
}

int g(int *p_a)
{
    *p_a = 5;
    p_a = 0; // does not have an effect outside the function
    printf("%d", *p_a); // error

}

typedef struct student1{
    char *name;
    int f;
}student1;

int main(){
    student1 s1;
    printf("%lu, %lu, %lu\n", 
                            (unsigned long)(&s1), 
                            (unsigned long)(&s1.name), 
                            (unsigned long)(&s1.f));

    printf("%lu\n", (unsigned long)sizeof(s1));
}
/*

int main()
{
    int b = 0;
    f(b);
    printf("%d\n", b);
    g(&b);
    printf("%d", b);
}

*/