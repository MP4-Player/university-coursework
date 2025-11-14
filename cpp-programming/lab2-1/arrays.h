#ifndef ARRAYS_H
#define ARRAYS_H

#include <vector> 

void arrayTasks();           


void task1WithPointers(); 
void task1WithVector(); 

  
void task2WithPointers();    
void task2WithVector();  

void printDynamicArray(int* arr, int size); 
void printVector(const std::vector<int>& vec); 
int generateRandomNumber(int min, int max);

#endif