import java.util.Locale;
import java.lang.Math;

public class b1 {

    public static void main(String[] args) {
        // Установка локали для формата вывода с точкой
        Locale.setDefault(Locale.ENGLISH); 

        // Начальное значение x
        double x = Math.PI / 15;
        // Шаг изменения x
        double step = Math.PI / 15;

        // Форматирование вывода
        String formatX = "%10.5f";  // Формат для x: 10 позиций, 5 знаков после запятой
        String formatFunction = "%15.7e"; // Формат для функций: 15 позиций, 7 знаков после запятой

        // Вывод заголовка таблицы
        //System.out.printf(formatX + " | " + sinX + " | " + expX + " | " x * lgX "\n");
        System.out.println("------- | -------- | -------- | --------");

        // Вывод значений в таблицу
        while (x <= Math.PI) {
            double sinX = Math.sin(x);
            double expX = Math.exp(x);
            double lgX = Math.log10(x); // Используем Math.log10 для lg
            double funcX = x * lgX;
            double finalX = expX/funcX;


            System.out.printf(formatX + " | " + formatFunction + " | " + formatFunction +" | " + formatFunction + " | " + formatFunction + "\n", 
                            x, sinX, expX, funcX,finalX);

            x += step;
        }
    }
}

