//#include <stdio.h>
//#include <stdlib.h>
#include "list.h"

typedef struct myNode{
    int data;
    struct myNode *next;
} myNode;

typedef struct myLL{
    myNode *head;
    int size;
} myLL;

int LL_is_in_list(void *list, int elem)
{
    int size = ((myLL*)list)->size;
    myNode *cur = ((myLL*)list)->head;
    for(int i = 0; i < size; i++){
        if(cur->data == elem){
            return 1;
        }
        cur = cur->next;
    }
    return 0;
}

