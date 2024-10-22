import java.util.Scanner;

public class b6 {

    public static double leftRectangles(double[] x, double[] y, double step) {
        int n = x.length;
        double integral = 0;
        for (int i = 0; i < n - 1; i++) {
            integral += y[i] * step;
        }
        return integral;
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        // Задаем интервал интегрирования
        System.out.print("Введите начало интервала: ");
        double a = scanner.nextDouble();
        System.out.print("Введите конец интервала: ");
        double b = scanner.nextDouble();

        // Задаем шаг
        double step = (b - a) / 100;

        // Создаем массивы для x и y
        double[] x = new double[101];
        double[] y = new double[101];
        for (int i = 0; i < 101; i++) {
            x[i] = a + i * step;
            y[i] = Math.exp(x[i]) - Math.pow(x[i], 3);
        }

        // Вычисляем интеграл по методу левых прямоугольников
        double integralLeft = leftRectangles(x, y, step);

        // Вычисляем аналитическое значение интеграла
        double integralAnalytic = Math.exp(b) - Math.pow(b, 3) / 3 - (Math.exp(a) - Math.pow(a, 3) / 3);

        // Выводим результаты
        System.out.println("Интеграл по методу левых прямоугольников: " + integralLeft);
        System.out.println("Аналитическое значение интеграла: " + integralAnalytic);
    }
}

