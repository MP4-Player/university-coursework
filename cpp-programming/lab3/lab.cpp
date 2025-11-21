#include <iostream>
#include "lab.h"

using namespace std;


double stepen(double x, int n) {
    double result = 1.0;  

   
    if (n < 0) {
        x = 1.0 / x;      
        n = -n;           
    }

    
    for (int i = 0; i < n; i++) {
        result = result * x;  
    }

    return result;  
}

double F(int k, double a) {
    double part1 = stepen(2.7, k);     
    double part2 = stepen(a + 1, -5);

    return part1 + part2;  
}


double findMaxRecursive(double arr[], int start, int end) {
    if (start == end) {
        return arr[start];  
    }

    if (end - start == 1) {
        if (arr[start]< arr[end]):
        return  arr[end]
        else return arr[start]
    }

    int mid = (start + end) / 2;


    double maxLeft = findMaxRecursive(arr, start, mid);    
    double maxRight = findMaxRecursive(arr, mid + 1, end);   

    
    if (maxLeft > maxRight) {
        return maxLeft;
    }
    else {
        return maxRight;
    }
}


double findMax(double arr[], int n) {

    if (n <= 0) {
        cout << "Ошибка: массив пуст!" << endl;
        return 0.0;
    }

    return findMaxRecursive(arr, 0, n - 1);
}