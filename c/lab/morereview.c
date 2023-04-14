#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int my_strncmp(char *str1, char *str2, int num){
     if(num == 0 || *str1 == '\0' || *str2 == '\0'){
        return 0;
     }

     if(*str1 > *str2){
        return 1;
     }

     if(*str1 < *str2){
        return -1;
     }

     return my_strncmp(str1 + 1, str2 + 1, num -1 );

}

int main(){
    printf("%d", my_strncmp("ESC180", "ESC190", 4));
}