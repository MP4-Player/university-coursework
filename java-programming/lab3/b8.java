import java.util.Scanner;

public class b8 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите степень полинома n: ");
        int n = scanner.nextInt();

        double[] coefficients = new double[n + 1];
        System.out.println("Введите коэффициенты полинома (от старшего к младшему):");
        for (int i = 0; i <= n; i++) {
            System.out.print("a" + (n - i) + ": ");
            coefficients[i] = scanner.nextDouble();
        }

        System.out.print("Введите значение x: ");
        double x = scanner.nextDouble();

        double result = evaluatePolynomial(coefficients, x, n);
        String polynomial = printPolynomial(coefficients);
        System.out.println("P(" + x + ") = " + polynomial + " = " + result);
    }

    public static double evaluatePolynomial(double[] coefficients, double x, int n) {

        double result = coefficients[n] * x + coefficients[n - 1];

        for (int i = n - 2; i >= 0; i--) {
            result = result * x + coefficients[i];
        }

        return result;
    }

    public static String printPolynomial(double[] coefficients) {
        StringBuilder polynomial = new StringBuilder();
        int n = coefficients.length - 1;

        for (int i = 0; i <= n; i++) {
            double coefficient = coefficients[i];
            if (coefficient != 0) {
                if (polynomial.length() > 0) {
                    polynomial.append(" + ");
                }
                if (n - i > 0) {
                    polynomial.append(coefficient).append("x^").append(n - i);
                } else {
                    polynomial.append(coefficient);
                }
            }
        }

        return polynomial.toString();
    }
}