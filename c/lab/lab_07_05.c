#include <stdio.h>
// implement heap in c using an array list
typedef struct{
    int *data;
    int size;
    int capacity;
} heap;

void get_left_child_index(heap *h, int parent_index){
    return 2 * parent_index
}


int main(){
    int initial_capacity = 10;
    heap *h = malloc(sizeof(heap));
    h->data = malloc(initial_capacity * sizeof(int));
    h->size = 0;
    h->capacity = initial_capacity;

    
    
}
