#include <stdio.h>

struct Indices {
    int first;
    int last;
};

struct Indices find_indices(int lst[], int n, int target) { 
    struct Indices indices = {-1, -1};
    for (int i = 0; i < n; i++) { 
        if (lst[i] == target) { 
            if (indices.first == -1) {
                indices.first = i;
            }
            indices.last = i;
        }
    }
    return indices;
}
    

int main() {
    int lst[] = {1, 2, 2, 2, 3, 4, 5};
    int n = sizeof(lst) / sizeof(lst[0]);
    struct Indices indices = find_indices(lst, n, 2);
    printf("first: %d, last: %d\n", indices.first, indices.last); 
    return 0;
}