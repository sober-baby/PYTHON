# include <stdio.h>

void reverse(int *array, int n)
{ int t, *i = array, *j = array + n - 1;
while (*i < *j)
{ t = *i;
*i++ = *j;
*j-- = t;
} }
int main(void)
{ int *s, *e, test_array[] = {1, 2, 3, 4, 5};
reverse(test_array, (sizeof(test_array) / sizeof(test_array[0])));
s = test_array;
e = test_array + sizeof(test_array) / sizeof(test_array[0]);
while (*s < *e) printf("%d ", *s++);
printf("\n");
}
