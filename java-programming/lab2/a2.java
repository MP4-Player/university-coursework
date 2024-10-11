public class a2 {

    public static void main(String[] args) {
        int[] arr = {1, 2, 3, -4, 5, -6, 7, -8, 9, -10,
                    -11, 12, -13, 14, 15, 16, 17, 18, 19, 20};

        double product = 1.0; 
        int count = 0; 

        
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] < 0) {
                product *= arr[i]; 
                count++; 
            }
        }

        
        if (count > 0) {
            
            double geometricmean = Math.pow(product, 1.0 / count);
            System.out.println("Среднее геом отрицательных элементов: " + geometricmean);
        } else {
            System.out.println("В массиве нет отриц элементов.");
        }
    }
}
