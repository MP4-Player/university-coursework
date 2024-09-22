#include <stdio.h>
#include <stdbool.h>
#include <ctype.h>
#include <wchar.h>
#include <locale.h>

bool is_russian_letter(wchar_t c) {
    return (c >= L'А' && c <= L'Я') || (c >= L'а' && c <= L'я');
}

bool is_latin_letter(wchar_t c) {
    return iswalpha(c) && !is_russian_letter(c);
}

bool is_digit(wchar_t c) {
    return iswdigit(c);
}

int main() {
    
    setlocale(LC_ALL, "en_US.UTF-8");

    wchar_t S[] = L"ПриветHello12345";

    wchar_t A[100] = {0}; // Русские буквы
    wchar_t B[100] = {0}; // Латинские буквы
    wchar_t C[100] = {0}; // Цифры

    int a_count = 0, b_count = 0, c_count = 0;


    for (int i = 0; S[i] != L'\0'; i++) {
        wchar_t c = S[i];

        if (is_russian_letter(c)) {
            A[a_count] = c;
            a_count++;
        } else if (is_latin_letter(c)) {
            B[b_count] = c;
            b_count++;
        } else if (is_digit(c)) {
            C[c_count] = c;
            c_count++;
        }
    }

    wprintf(L"Русские буквы: %ls\n", A);
    wprintf(L"Латинские буквы: %ls\n", B);
    wprintf(L"Цифры: %ls\n", C);

    return 0;
}