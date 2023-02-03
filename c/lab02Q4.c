#include <stdio.h>

struct a {
    int first;
    int last;
};

struct a find_num(int arr[], int n, int target) { 
    struct a num = {-1, -1};
    for (int i = 0; i < n; i++) { 
        if (arr[i] == target) { 
            if (num.first == -1) {
                num.first = i;
            }
            num.last = i;
        }
    }
    return num;
}
    

int main() {
    int arr[] = {1, 2, 2, 2, 3, 4, 5};
    struct a num = find_num(arr, 7, 2);
    printf("first: %d, last: %d\n", num.first, num.last); 
    return 0;
}