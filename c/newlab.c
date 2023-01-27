#include <stdio.h>
#include <stdlib.h>
char *concat_index(char **str1, int l1, char **str2, int l2) {
    char *res = (char *)malloc((l1 + l2 + 1) * sizeof(char));
    for (int i = 0; i < l1; i++) {
        res[i] = (*str1)[i];
    }
    for (int i = 0; i < l2; i++) {
        res[l1 + i] = (*str2)[i];
    }
    res[l1 + l2] = '\0';
    return res;
}



int main() {
    // question 1: weird symbol at the end
    // question 2:
    char *str1 = "abcd";
    char *str2 = "abc";
    char *combined_1 = concat_index(&str1, 3, &str2, 3);
    // char *combined_2 = concat_pointer(&str1, 3, &str2, 3);
    // char *old_c2 = combined_2;
    printf("%s\n", combined_1);
    free(combined_1);

    // question 3:
    // str1 == str2: addresses of first letters the same?
    // *str1 == *str2: 'a' == 'd'?
    // strcmp(s1, s2): two strings are same?

    // question 4:
    int arr[8] = {13,2,3,10,10,10,12,12};
    // binary_search_deluxe(arr, 8, 10);
}