public class b2 {

    public static void main(String[] args) {
        int[][] arr = {
                {1, 2, -3, 4},
                {5, -6, 7},
                {8, 9, 10, -11, -12},
                {-1, -2}
        };

        int largestNegative = findLargestNegative(arr);

        if (largestNegative != Integer.MIN_VALUE) {
            System.out.println("Наибольший отрицательный элемент: " + largestNegative);
        } else {
            System.out.println("В массиве нет отрицательных элементов.");
        }
    }

    public static int findLargestNegative(int[][] arr) {
        int largestNegative = Integer.MIN_VALUE; // Инициализируем наибольший отрицательный как минимальное значение

        for (int i = 0; i < arr.length; i++) {
            for (int j = 0; j < arr[i].length; j++) {
                if (arr[i][j] < 0 && arr[i][j] > largestNegative) {
                    largestNegative = arr[i][j];
                }
            }
        }

        return largestNegative;
    }
}



