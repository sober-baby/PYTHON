#include <stdio.h>
void count_letters(char *s, int counts[]){
    for (int i = 0; i < 26; i++){
        counts[i] = 0;
    }
    for (int i = 0; i < strlen(s); i++){
        if (s[i] >= 'a' && s[i] <= 'z'){
            counts[s[i] - 'a']++;
        }
    }
}