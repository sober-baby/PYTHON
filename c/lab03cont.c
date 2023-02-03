#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <time.h>
int main(){
    char line[200];
    FILE *fp = fopen("testfile.txt", "r");
    for(int i = 0; i < 9; i++){
        //fgets(line, sizeof(line), fp); 
        //printf("%s", line);
    }
    int count = 0;
    int total = 0;
    while (fgets(line, sizeof(line), fp) != NULL)
    {
        printf("%s", line);
        total += atoi(line);
        count++;
    }

    printf("Average: %f", (float)total/count);
    fclose(fp); 
}