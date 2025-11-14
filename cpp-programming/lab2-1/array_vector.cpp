#include <iostream>
#include <vector>
#include "arrays.h"

using namespace std;

void task1WithVector() {
    cout << "=== Задание 1 (vector) ===" << endl;
    cout << "Сумма отрицательных элементов массива" << endl;

    vector<int> arr(10);


    cout << "Массив: ";
    for (int i = 0; i < 10; i++) {
        arr[i] = generateRandomNumber(-50, 49);
        cout << arr[i] << " ";
    }
    cout << endl;

    int sum = 0;
    for (int num : arr) {
        if (num < 0) {
            sum += num; 
        }
    }

    cout << "Сумма отрицательных элементов: " << sum << endl;
}