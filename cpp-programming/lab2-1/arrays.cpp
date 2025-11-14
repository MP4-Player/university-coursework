#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include "arrays.h"

using namespace std;


void arrayTasks() {
    cout << "*** ÇÀÄÀÍÈß Ñ ÌÀÑÑÈÂÀÌÈ ***" << endl;

    srand(static_cast<unsigned int>(time(0))); 


    task1WithPointers();
    cout << endl;
    task1WithVector();
    cout << endl;


    task2WithPointers();
    cout << endl;
    task2WithVector();
}


void printDynamicArray(int* arr, int size) {
    cout << "Ìàññèâ: ";
    int* ptr = arr;
    for (int i = 0; i < size; i++) {
        cout << *ptr << " ";
        ptr++;
    }
    cout << endl;
}

void printVector(const vector<int>& vec) {
    cout << "Ìàññèâ: ";
    for (int element : vec) {
        cout << element << " ";
    }
    cout << endl;
}

int generateRandomNumber(int min, int max) {
    return rand() % (max - min + 1) + min;
}