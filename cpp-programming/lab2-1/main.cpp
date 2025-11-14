#include <iostream>
#include <windows.h>
#include "arrays.h"
#include "strings.h"

using namespace std;

int main() {
    SetConsoleOutputCP(1251);
    SetConsoleCP(1251);

    cout << "Лабораторная работа 2" << endl;
    cout << "Вариант 3" << endl;

 
    arrayTasks();

    cout << endl;

    stringTasks();

    cout << "Все задания выполнены!" << endl;
    return 0;
}