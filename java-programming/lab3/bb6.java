import java.util.Scanner;

public class bb6 {

    public static void tabulateFunction(double start, double end, double[] x, double[] y) {
        double step = (end - start) / (x.length - 1);
        for (int i = 0; i < x.length; i++) {
            x[i] = start + i * step;
            y[i] = Math.exp(x[i]) - Math.pow(x[i], 3);
        }

        // System.out.println(Arrays.toString(x));
    }

    public static double integrateLeftRectangles(double[] x, double[] y) {
        double sum = 0.0;
        for (int i = 0; i < x.length - 1; i++) {
            sum += y[i] * (x[i + 1] - x[i]);
        }
        return sum;
    }

    public static double analyticalIntegral(double a, double b) {
        return (Math.exp(b) - Math.pow(b, 4) / 4.0) - (Math.exp(a) - Math.pow(a, 4) / 4.0);
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите начальное значение интервала (a): ");
        double a = scanner.nextDouble();
        System.out.print("Введите конечное значение интервала (b): ");
        double b = scanner.nextDouble();

        int n = 101;
        double[] x = new double[n];
        double[] y = new double[n];

        tabulateFunction(a, b, x, y);

        double numericalResult = integrateLeftRectangles(x, y);

        double analyticalResult = analyticalIntegral(a, b);

        System.out.println("Численное значение интеграла: " + numericalResult);
        System.out.println("Аналитическое значение интеграла: " + analyticalResult);
        System.out.println("Разница между значениями: " + Math.abs(numericalResult - analyticalResult));
    }
}
