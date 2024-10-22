import java.util.Arrays;

public class b3{

    public static void main(String[] args) {
        int[][] matrix = {
                {5, 2, 8},
                {10, 3, 9, 4},
                {6, 7, 1, 2}
        };

        System.out.println("Матрица до сортировки:");
        printMatrix(matrix);

        sortMatrixRows(matrix);

        System.out.println("\nМатрица после сортировки:");
        printMatrix(matrix);
    }

    public static void sortMatrixRows(int[][] matrix) {
        for (int i = 0; i < matrix.length; i++) {
            Arrays.sort(matrix[i]); // Сортировка каждой строки
        }
    }

    public static void printMatrix(int[][] matrix) {
        for (int[] row : matrix) {
            for (int element : row) {
                System.out.print(element + " ");
            }
            System.out.println();
        }
    }
}

