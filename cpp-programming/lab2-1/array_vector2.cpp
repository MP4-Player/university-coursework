#include <iostream>
#include <vector>
#include "arrays.h"

using namespace std;

void task2WithVector() {
    cout << "=== Задание 2 (vector) ===" << endl;

    int n;
    cout << "Введите размер массива: ";
    cin >> n;

    
    if (n <= 0) {
        cout << "Ошибка: размер должен быть положительным!" << endl;
        return;
    }

    
    vector<int> arr(n);

    
    cout << "Введите " << n << " элементов: ";
    for (int i = 0; i < n; i++) {
        cin >> arr[i];  
    }

    //  Произведение элементов с четными номерами
    int product = 1;
    bool hasEven = false;
    for (int i = 0; i < n; i += 2) {  
        product *= arr[i]; 
        hasEven = true;
    }

    if (!hasEven) product = 0;  
    cout << "1. Произведение элементов с четными номерами: " << product << endl;

    // Сумма между первым и последним нулевыми элементами
    int firstZero = -1;  
    int lastZero = -1;   

    
    for (int i = 0; i < n; i++) {
        if (arr[i] == 0) {
            firstZero = i;
            break;  
        }
    }

 
    for (int i = n - 1; i >= 0; i--) {
        if (arr[i] == 0) {
            lastZero = i;
            break;  
        }
    }

    int sumBetween = 0;
    if (firstZero != -1 && lastZero != -1 && firstZero < lastZero) {
        for (int i = firstZero + 1; i < lastZero; i++) {
            sumBetween += arr[i];  
        }
    }
    cout << "2. Сумма между нулями: " << sumBetween << endl;


    vector<int> result;  

    
    for (int num : arr) {
        if (num >= 0) {
            result.push_back(num);  
        }
    }

    
    for (int num : arr) {
        if (num < 0) {
            result.push_back(num);  
        }
    }

    cout << "3. Преобразованный массив: ";
    printVector(result);
}