#include <stdio.h>

void set0(int *p_a)
{
    *p_a = 10; 
}

void changechar(char* arr)
{
    arr[0] = 'c';
}

void sorting(int arr[], int n)
{

    int i = 1;
    while (i < n){
        int x = arr[i];
        int j = i - 1;
        while (j >= 0 && arr[j] > x){
            arr[j+1] = arr[j];
            j = j - 1;
        }
    arr[j+1] = x;
    i++;
    }
}


int lengthofstring(char* str)
{
    int a = 0;
    while(*str != '\0'){
        a++;
        str ++;
    }

    return a; 
}

void seq_replace(int arr1[], int m, int arr2[], int n){
    for (int i = 0; i<m; i++){
        for(int j = 0; j<n; j++){
            if(arr1[i] = arr2[j]){
                arr1[i] = 0;
            }
        }
    }

}
int main()
{
    int *a = 5;
    set0(&a);
    printf("%d\n", a);
    char arr3[3] = {'a', 'b', 'c', '\0'};
    changechar(arr3);
    printf("Print Char: %s\n", arr3);
    int arr1[4] = {4, 3, 2, 1};
    int arr10[4] = {4, 3, 2, 1};
    int c = 4;
    sorting(arr1, c);
    for(int i = 0; i<4; i++){
        printf("The number is: %d\n", arr1[i]);
    }
    char greeting[6] = {'H', 'e', 'l', 'l', 'o', '\0'};
    int num = lengthofstring(greeting);
    printf("%d", num);
    seq_replace(arr1, 4, arr10, 4);
    for(int i = 0; i<4; i++){
        printf("Sup: %d\n", arr1[i]);
    }





}