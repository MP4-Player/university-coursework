#include <iostream>
#include "arrays.h"

using namespace std;

void task2WithPointers() {
    cout << "=== Задание 2 (указатели) ===" << endl;

    int n;
    cout << "Введите размер массива: ";
    cin >> n;

    if (n <= 0) {
        cout << "Ошибка: размер должен быть положительным!" << endl;
        return;
    }

    int* arr = new int[n];

    cout << "Введите " << n << " элементов: ";
    int* ptr = arr;
    for (int i = 0; i < n; i++) {
        cin >> *ptr; 
        ptr++;  
    }

    // 1. Произведение элементов с четными номерами
    ptr = arr;  
    int product = 1;
    bool hasEven = false;
    for (int i = 0; i < n; i++) {
        if (i % 2 == 0) {  
            product *= *ptr;  
            hasEven = true;
        }
        ptr++; 
    }

    if (!hasEven) product = 0;
    cout << "1. Произведение элементов с четными номерами: " << product << endl;

    // 2. Сумма между первым и последним нулевыми элементами
    ptr = arr;
    int firstZero = -1;  
    int lastZero = -1;  

   
    for (int i = 0; i < n; i++) {
        if (*ptr == 0) {
            firstZero = i;  
            break;  
        }
        ptr++; 
    }

    
    ptr = arr + n - 1;  
    for (int i = n - 1; i >= 0; i--) {
        if (*ptr == 0) {
            lastZero = i;  
            break;  
        }
        ptr--;  
    }

    //сумму между нулями
    int sumBetween = 0;
    if (firstZero != -1 && lastZero != -1 && firstZero < lastZero) {
        ptr = arr + firstZero + 1; 
        for (int i = firstZero + 1; i < lastZero; i++) {
            sumBetween += *ptr; 
            ptr++;  
        }
    }
    cout << "2. Сумма между нулями: " << sumBetween << endl;

    // 3. Сначала положительные, потом отрицательные
  
    int* result = new int[n];
    int* resPtr = result;  

    
    ptr = arr; 
    for (int i = 0; i < n; i++) {
        if (*ptr >= 0) {  
            *resPtr = *ptr;  
            resPtr++;  
        }
        ptr++;  
    }

   
    ptr = arr; 
    for (int i = 0; i < n; i++) {
        if (*ptr < 0) {  
            *resPtr = *ptr;  
            resPtr++; 
        }
        ptr++;  
    }

    
    cout << "3. Преобразованный массив: ";
    printDynamicArray(result, n);

   
    delete[] arr;
    delete[] result;
}