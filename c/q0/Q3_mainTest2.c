#include <stdio.h>
#include "list.h"

int LL_is_in_list(void *list, int data);
int main()
{
    void *list;
    int data[] = {3, 1, 2, 3};
    create_list_from_data(&list, data, 4);
    printf("%d\n", LL_is_in_list(list, 5));
}
