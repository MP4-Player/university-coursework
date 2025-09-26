
#include <iostream>
#include <climits>

using namespace std;

int main() {
    locale::global(locale("Russian_Russia.1251"));

    int choice;
    cout << "Выберите часть задания (1 или 2): ";
    cin >> choice;

    switch (choice) {
    case 1: {

        const int N = 5;
        int arr[N] = { 3, 1, 7, 2, 5 };

        int maxNeg = INT_MIN;
        bool found = false;

        for (int i = 0; i < N; i++) {
            if (arr[i] < 0) {
                if (!found || arr[i] > maxNeg) {
                    maxNeg = arr[i];
                    found = true;
                }
            }
        }

        if (found) {
            cout << "Максимальный среди отрицательных: " << maxNeg << endl;
        }
        else {
            cout << "Отрицательных элементов нет" << endl;
        }
        break;
    }

    case 2: {
        int M, N;
        cout << "Введите M это статический массив (максимум 10 элементов!): ";
        cin >> M;
        cout << "Введите N (максимум 10 элементов!) : ";
        cin >> N;

        int set[10];
        cout << "Введите " << M << " чисел  ";
        for (int i = 0; i < M; i++) {
            cin >> set[i];
        }

        int matrix[10][10]; 

        for (int j = 0; j < N; j++) {
            for (int i = 0; i < M; i++) {
                matrix[i][j] = set[i];
            }
        }
   
        cout << "Матрица " << M << "x" << N << ":" << endl;
        for (int i = 0; i < M; i++) {
            for (int j = 0; j < N; j++) {
                cout << matrix[i][j] << " ";
            }
            cout << endl;
        }
        break;
    }

    default:
        cout << "Неверный выбор" << endl;
    }

    return 0;
} 
