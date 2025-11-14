#define _CRT_SECURE_NO_WARNINGS  

#include <iostream>
#include <string>
#include <cstring>   
#include <cctype>    
#include "strings.h"

using namespace std;


char changeCase(char c) {
    if (c >= 'A' && c <= 'Z') {
        return tolower(c);
    }
    if (c >= 'a' && c <= 'z') {
        return toupper(c);
    }

    if (c >= 'А' && c <= 'Я') {
        return c + 32;  
    }
    if (c >= 'а' && c <= 'я') {
        return c - 32; 
    }
    return c; 
}


void safeStrcpy(char* dest, const char* src, int maxLength) {
    int i;
    for (i = 0; i < maxLength - 1 && src[i] != '\0'; i++) {
        dest[i] = src[i];
    }
    dest[i] = '\0';  
}


void task1WithCharPtr() {
    cout << "=== Задание 1 (char*) ===" << endl;
    cout << "Смена регистра букв" << endl;

    char input[1000];  

    cout << "Введите строку: ";
    cin.ignore();  
    cin.getline(input, 1000);

    cout << "Исходная строка: " << input << endl;

    
    char* ptr = input;
    while (*ptr != '\0') {
        *ptr = changeCase(*ptr);
        ptr++;
    }

    cout << "Результат: " << input << endl;
}

void task1WithString() {
    cout << "=== Задание 1 (string) ===" << endl;
    cout << "Смена регистра букв" << endl;

    string input;

    cout << "Введите строку: ";
    getline(cin, input);

    cout << "Исходная строка: " << input << endl;

    for (int i = 0; i < input.length(); i++) {
        input[i] = changeCase(input[i]);
    }

    cout << "Результат: " << input << endl;
}


void task2WithCharPtr() {
    cout << "=== Задание 2 (char*) ===" << endl;
    cout << "Таблица слов" << endl;

    char input[1000];

    cout << "Введите текст: ";
    cin.getline(input, 1000);

    char words[100][100];  
    int counts[100] = { 0 };
    int wordCount = 0;

    char* ptr = input;
    char currentWord[100];
    int wordLen = 0;


    while (*ptr != '\0') {
        if (*ptr == ' ' || *ptr == ',' || *ptr == '.') {
            
            if (wordLen > 0) {
                currentWord[wordLen] = '\0';  

               
                bool found = false;
                for (int i = 0; i < wordCount; i++) {
                    if (strcmp(words[i], currentWord) == 0) {
                        counts[i]++;
                        found = true;
                        break;
                    }
                }

                
                if (!found) {
                    safeStrcpy(words[wordCount], currentWord, 100);
                    counts[wordCount] = 1;
                    wordCount++;
                }

                wordLen = 0;  
            }
        }
        else {
            
            if (wordLen < 99) { 
                currentWord[wordLen] = *ptr;
                wordLen++;
            }
        }
        ptr++;
    }

 
    if (wordLen > 0) {
        currentWord[wordLen] = '\0';
        bool found = false;
        for (int i = 0; i < wordCount; i++) {
            if (strcmp(words[i], currentWord) == 0) {
                counts[i]++;
                found = true;
                break;
            }
        }
        if (!found) {
            safeStrcpy(words[wordCount], currentWord, 100);
            counts[wordCount] = 1;
            wordCount++;
        }
    }

 
    cout << "Слово\tКоличество" << endl;
    for (int i = 0; i < wordCount; i++) {
        cout << words[i] << "\t" << counts[i] << endl;
    }
}

void task2WithString() {
    cout << "=== Задание 2 (string) ===" << endl;
    cout << "Таблица слов" << endl;

    string input;
    cout << "Введите текст: ";
    getline(cin, input);


    string words[100];
    int counts[100] = { 0 };
    int wordCount = 0;

    string currentWord = "";


    for (char c : input) {
        if (c == ' ' || c == ',' || c == '.') {
            if (!currentWord.empty()) {
                bool found = false;
                for (int i = 0; i < wordCount; i++) {
                    if (words[i] == currentWord) {
                        counts[i]++;
                        found = true;
                        break;
                    }
                }

                
                if (!found) {
                    words[wordCount] = currentWord;
                    counts[wordCount] = 1;
                    wordCount++;
                }

                currentWord = "";
            }
        }
        else {
            currentWord += c;
        }
    }


    if (!currentWord.empty()) {
        bool found = false;
        for (int i = 0; i < wordCount; i++) {
            if (words[i] == currentWord) {
                counts[i]++;
                found = true;
                break;
            }
        }
        if (!found) {
            words[wordCount] = currentWord;
            counts[wordCount] = 1;
            wordCount++;
        }
    }

    cout << "Слово\tКоличество" << endl;
    for (int i = 0; i < wordCount; i++) {
        cout << words[i] << "\t" << counts[i] << endl;
    }
}


void stringTasks() {
    cout << "*** ЗАДАНИЯ СО СТРОКАМИ ***" << endl;

    task1WithCharPtr();
    cout << endl;
    task1WithString();
    cout << endl;
    task2WithCharPtr();
    cout << endl;
    task2WithString();
}