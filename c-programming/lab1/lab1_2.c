#include <stdio.h>
#include <stdlib.h>

int main(void)                     
{                                  
   int count_numbers_in_array;
   
   printf("Enter the number of values in the array: ");
   scanf("%d", &count_numbers_in_array);

   // Выделение памяти для массива
   int *array = (int *)calloc(count_numbers_in_array * sizeof(int));

   if (array == NULL) {
       printf("Memory allocation failed\n");
       return 1;
   }

   printf("Enter %d numbers:\n", count_numbers_in_array);

   for (int i = 0; i < count_numbers_in_array; i++) {
       printf("Number %d: ", i + 1);
       scanf("%d", &array[i]);
   }

   printf("You have entered the following values:\n");
   for (int i = 0; i < count_numbers_in_array; i++) {
       printf("%d ", array[i]);
   }
   printf("\n");
   return 0;


}