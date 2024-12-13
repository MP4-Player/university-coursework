import java.util.Arrays;
import java.util.Scanner;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        // Создаем объект для ввода с консоли
        Scanner scanner = new Scanner(System.in);

        // Запрашиваем минимальное значение x
        System.out.println("Введите минимальное значение x:");
        double minX = scanner.nextDouble();

        // Запрашиваем максимальное значение x
        System.out.println("Введите максимальное значение x:");
        double maxX = scanner.nextDouble();

        // Запрашиваем количество точек
        System.out.println("Введите количество точек:");
        int numPoints = scanner.nextInt();

        // Создаем массивы для хранения значений x и y
        double[] x = new double[numPoints];
        double[] y = new double[numPoints];

        // Вычисляем шаг дискретизации
        double step = (maxX - minX) / (numPoints - 1);

        // Заполняем массивы данными функции y = sin(x)
        for (int i = 0; i < numPoints; i++) {
            x[i] = minX + i * step;
            y[i] = Math.sin(x[i]);
        }

        // Создаем объект класса Curve
        Curve curve = new Curve();

        // Заполняем объект данными
        curve.setData(x, y);

        // Устанавливаем размеры графика
        curve.setBounds(300, 300);

        // Создаем окно JFrame для отображения графика
        JFrame frame = new JFrame("График функции");

        // Устанавливаем поведение закрытия окна
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Добавляем объект Curve в окно
        frame.add(curve);

        // Устанавливаем размеры и отображаем окно
        frame.setSize(300, 300);
        frame.setVisible(true);

        // Выводим массивы x и y в консоль
        System.out.println("Массив x: " + Arrays.toString(x));
        System.out.println("Массив y: " + Arrays.toString(y));

        // Закрываем объект для ввода с консоли
        scanner.close();
    }
}
