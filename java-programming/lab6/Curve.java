import java.awt.*;
import java.awt.geom.Line2D;
import javax.swing.*;

public class Curve extends JPanel {
    // Массивы для хранения значений x и y
    private double[] x;
    private double[] y;

    // Диапазоны значений x и y
    private double minX, maxX;
    private double minY, maxY;

    // Ширина и высота графика
    private int width, height;

    public Curve() {
        // Устанавливаем начальные значения ширины и высоты
        width = 300;
        height = 300;
    }

    public void setData(double[] x, double[] y) {
    this.x = x;
    this.y = y;

    minX = x[0];
    maxX = x[x.length - 1];
    minY = -1.0; //  Устанавливаем minY = -1
    maxY = 1.0;  // Устанавливаем maxY = 1
    }


    public void setBounds(int width, int height) {
        // Устанавливаем ширину и высоту графика
        this.width = width;
        this.height = height;
    }

    @Override
    protected void paintComponent(Graphics g) {
        // Вызываем метод родительского класса для отрисовки фона
        super.paintComponent(g);

        // Получаем объект Graphics2D для более точного рисования
        Graphics2D g2d = (Graphics2D) g;

        // Включаем сглаживание для плавного отображения
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

        // Проверяем, есть ли данные для отрисовки
        if (x == null || y == null) return;

        // Вычисляем масштаб для осей x и y
        double xScale = (double) width / (maxX - minX);
        double yScale = (double) height / (maxY - minY);

        // Рисуем линии между точками
        for (int i = 0; i < x.length - 1; i++) {
            // Вычисляем координаты точек
            double x1 = (x[i] - minX) * xScale;
            double y1 = height - (y[i] - minY) * yScale;
            double x2 = (x[i + 1] - minX) * xScale;
            double y2 = height - (y[i + 1] - minY) * yScale;

            // Рисуем линию
            g2d.draw(new Line2D.Double(x1, y1, x2, y2));
        }
    }
}
