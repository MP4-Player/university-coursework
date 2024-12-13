import java.awt.*; // Импорт класса JFrame для создания окна
import java.awt.geom.Line2D;     // Импорт класса Graphics для рисования
import javax.swing.*; // Импорт класса Line2D для рисования линий

public class SineGraph extends JPanel { // Класс SineGraph наследуется от JPanel для создания графического компонента

    private static final int WIDTH = 300; // Ширина окна
    private static final int HEIGHT = 300; // Высота окна
    private static final double PI = Math.PI; // Константа PI

    public SineGraph() { // Конструктор класса SineGraph
        setPreferredSize(new Dimension(WIDTH, HEIGHT)); // Установка предпочтительных размеров окна
    }

    @Override
    protected void paintComponent(Graphics g) { // Метод перерисовки компонента
        super.paintComponent(g); // Вызов метода перерисовки родительского класса
        Graphics2D g2d = (Graphics2D) g; // Приведение Graphics к Graphics2D для использования дополнительных возможностей
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON); // Включение сглаживания для более плавных линий

        // Масштабирование и сдвиг для отображения синусоиды в окне
        double scaleX = WIDTH / (2 * PI); // Масштаб по оси X
        double scaleY = HEIGHT / 2;     // Масштаб по оси Y
        double translateX = WIDTH / 2;  // Сдвиг по оси X
        double translateY = HEIGHT / 2;  // Сдвиг по оси Y


        // Оси координат
        g2d.setColor(Color.GRAY);     // Установка серого цвета для осей
        g2d.drawLine(0, (int)translateY, WIDTH, (int)translateY); // Рисование оси X
        g2d.drawLine((int)translateX, 0, (int)translateX, HEIGHT); // Рисование оси Y


        g2d.setColor(Color.BLUE);    // Установка синего цвета для графика
        double x1 = -PI;             // Начальное значение x
        double y1 = Math.sin(x1);    // Начальное значение y

        for (double x2 = -PI + 0.1; x2 <= PI; x2 += 0.1) { // Цикл для построения графика с шагом 0.1
            double y2 = Math.sin(x2);    // Вычисление значения y для текущего x
            g2d.draw(new Line2D.Double( // Рисование отрезка линии
                    x1 * scaleX + translateX, // Координата x первой точки
                    -y1 * scaleY + translateY, // Координата y первой точки (отрицательный знак для инверсии оси Y)
                    x2 * scaleX + translateX, // Координата x второй точки
                    -y2 * scaleY + translateY  // Координата y второй точки (отрицательный знак для инверсии оси Y)
            ));
            x1 = x2;                 // Обновление значения x1
            y1 = y2;                 // Обновление значения y1
        }
    }

    public static void main(String[] args) { // Основной метод
        JFrame frame = new JFrame("График синуса"); // Создание окна
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Установка действия при закрытии окна
        frame.add(new SineGraph()); // Добавление компонента SineGraph в окно
        frame.pack(); // Автоматическая настройка размеров окна
        frame.setLocationRelativeTo(null); // Размещение окна по центру экрана
        frame.setVisible(true); // Отображение окна
    }
}

