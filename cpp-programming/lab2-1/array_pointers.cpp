#include <iostream>
#include <cstdlib>
#include <ctime>
#include "arrays.h"

using namespace std;

void task1WithPointers() {
    cout << "=== Задание 1 (указатели) ===" << endl;
    cout << "Сумма отрицательных элементов массива" << endl;

    int* arr = new int[10];

    cout << "Массив: ";
    int* ptr = arr;  
    for (int i = 0; i < 10; i++) {
        *ptr = generateRandomNumber(-50, 49);
        cout << *ptr << " ";
        ptr++;  
    }
    cout << endl;

    int sum = 0;
    ptr = arr;  
    for (int i = 0; i < 10; i++) {
        if (*ptr < 0) {
            sum += *ptr;  
        }
        ptr++;  
    }

    cout << "Сумма отрицательных элементов: " << sum << endl;


    delete[] arr;
}