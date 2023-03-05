#include <stdio.h>
#include <stdlib.h>
#include <string.h>


/* const indicates that a value cannot be changed, changing it will cause a compile error

const int n = 42;
n = 43; // compile error

// const indicates that a pointer cannot be changed, changing it will cause a compile error
const char *p_c = (char*)(malloc(sizeof(char)));
*p_c = 0; // complie error 
p_c = "hello"; // fine, you can 


int * const p_n = (int*)(malloc(sizeof(int)));
p_n = 0; // compile error
*p_n = 42; // fine

*/

// Linked Lists

/*
Operation  Array   :  Linked List
Insert    O(n)     :  O(1)
remove   O(n)     :  O(1)
get    O(1)     :  O(n)(or O(1) if you have a pointer to the node you want to get)

The comlpexity listed for insert and remove for linked lists is only the time taken for the actual operation, not the time taken to find the node you want to insert/remove. 
*/

typedef struct node{
    int data;
    struct node *next;
}node;

typedef struct LL{
    struct node *head;
    int size;
}LL;

void create_node(node **p_n, int data)
{
    *p_n = (node*)malloc(sizeof(node));
    (*p_n)->data = data;
    (*p_n)->next = NULL;
}

// create a linked list that looks like data[0] -> data[1] -> data[2] -> ... -> data[size-1]
void create_LL_from_data(LL **p_LL, int *data_arr, int size)
{
    (*p_LL) = (LL*)malloc(sizeof(LL));
    (*p_LL)->size = 0;
    node *cur = (*p_LL)->head;
    for (int i = 0; i < size; i++)
    {
        node *n;
        create_node(&n, data_arr[i]); // n is a pointer to a node with data = data[i], next = NULL
        cur->next = n;
        cur = n;
        (*p_LL)->size++;
    }
}

void LL_append(LL *my_list, int new_ele)
{
    node *cur = my_list->head;
    while (cur->next != NULL)
    {
        cur = cur->next;
    }
    node *n;
    create_node(&n, new_ele);
    cur->next = n;
    my_list->size++;
}

int main()
{

}



