#include <stdio.h>
#include <string.h>
#include <stdlib.h>


char** split(char* str, const char* sep, int* count) {
    char** words = NULL;
    char* token = strtok(str, sep);
    *count = 0;

    while (token != NULL) {
        words = realloc(words, (*count + 1) * sizeof(char*));
        words[*count] = token;
        (*count)++;
        token = NULL;
    }

    return words;
}

int main(void) {
    char str1[] = "hello, my friend";
    char str2[] = "hello, dogs";
    char sep[] = " ";

    int count1, count2;
    char** words1 = split(str1, sep, &count1);
    char** words2 = split(str2, sep, &count2);


    printf("Source string 1: %s\n", str1);
    printf("Source string 2: %s\n", str2);

    // Сравниваем слова из двух строк
    for (int i = 0; i < count1; i++) {
        for (int j = 0; j < count2; j++) {
            if (words1[i] == words2[j]) {
                printf("Common word: %s\n", words1[i]);
            }
        }
    }

    // Освобождаем память
    free(words1);
    free(words2);

    return 0;
}
