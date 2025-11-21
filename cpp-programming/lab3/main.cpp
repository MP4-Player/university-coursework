#include <iostream>
#include "lab.h"

using namespace std;

int main() {

    setlocale(LC_ALL, "Russian");

    cout << "Лабораторная работа №3" << endl;
    cout << "Вариант 3" << endl;
    cout << "==========================" << endl;


    cout << "ЗАДАНИЕ 1: Функции stepen и F" << endl;
    cout << "==========================" << endl;

    double x;
    int n;
    int k;
    double a;


    cout << "Введите число x (основание степени): ";
    cin >> x;

    cout << "Введите степень n (целое число): ";
    cin >> n;


    double powerResult = stepen(x, n);
    cout << x << " в степени " << n << " = " << powerResult << endl;


    cout << endl;
    cout << "Введите значение k (целое число): ";
    cin >> k;

    cout << "Введите значение a (вещественное число): ";
    cin >> a;


    double fResult = F(k, a);
    cout << "F(" << k << ", " << a << ") = 2.7^" << k << " + (" << a << " + 1)^-5 = " << fResult << endl;

    cout << endl;

    cout << "ЗАДАНИЕ 2: Рекурсивный поиск максимума в массиве" << endl;
    cout << "==========================" << endl;

    int size;
    cout << "Введите размер массива: ";
    cin >> size;

  
    if (size <= 0) {
        cout << "Ошибка: размер массива должен быть положительным!" << endl;
        return 1;
    }


    double* arr = new double[size];

    
    cout << "Введите " << size << " элементов массива:" << endl;
    for (int i = 0; i < size; i++) {
        cout << "Элемент " << i + 1 << ": ";
        cin >> arr[i];
    }

 
    cout << "Введенный массив: ";
    for (int i = 0; i < size; i++) {
        cout << arr[i] << " ";
    }
    cout << endl;

 
    double maxElement = findMax(arr, size);
    cout << "Максимальный элемент в массиве: " << maxElement << endl;


    delete[] arr;

    cout << endl;
    cout << "Программа завершена успешно!" << endl;

    return 0;
}