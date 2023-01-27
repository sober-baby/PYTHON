int strcmp(char *s1, char *s2)
{
    if (s1[0] == '\0' && s2[0] == '\0')
    {
        return 0;
    }
    if (s1[0] != s2[0])
    {
        return 1;
    }
    return strcmp(s1 + 1, s2 + 1);
}
int main()
{
    
    // Question 3
    char *s1 = "he";
    char *s2 = "wo";
    int a = strcmp(s1, s2);
    printf("%d", a);
    
    return 0;



}

