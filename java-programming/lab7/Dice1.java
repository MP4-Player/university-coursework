import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;

public class Dice extends JPanel {
    private int numDots; // Количество точек (от 1 до 6)
    private Color dotColor; // Цвет точек
    private Color backgroundColor; // Цвет фона
    private boolean active; // Активное/неактивное состояние

    public Dice() {
        this(1, Color.BLACK, Color.WHITE, true); // Вызов конструктора с параметрами по умолчанию
    }

    public Dice(int numDots, Color dotColor, Color backgroundColor, boolean active) {
        this.numDots = numDots;
        this.dotColor = dotColor;
        this.backgroundColor = backgroundColor;
        this.active = active;
        setPreferredSize(new Dimension(50, 50)); // Установка предпочтительного размера
        setBackground(backgroundColor); // Установка цвета фона

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (active) {
                    roll(); // Вызов метода roll при клике если кость активна
                }
            }
        });
    }

    // Метод для бросания кости
    public void roll() {
        Random random = new Random();
        numDots = random.nextInt(6) + 1;
        repaint(); // Перерисовка компонента
    }

    // Методы-сеттеры для изменения свойств
    public void setDotColor(Color dotColor) {
        this.dotColor = dotColor;
        repaint();
    }

    public void setBackgroundColor(Color backgroundColor) {
        this.backgroundColor = backgroundColor;
        setBackground(backgroundColor);
        repaint();
    }

    public void setActive(boolean active) {
        this.active = active;
    }

    public int getNumDots() {
        return numDots;
    }

    // Переопределение метода paintComponent для рисования точек
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON); // Сглаживание

        int size = Math.min(getWidth(), getHeight());
        int dotSize = size / 10; // Размер точки
        int padding = size / 10; // Отступ от краев

        switch (numDots) {
            case 1:
                drawDot(g2d, size / 2, size / 2, dotSize);
                break;
            case 2:
                drawDot(g2d, padding, padding, dotSize);
                drawDot(g2d, size - padding, size - padding, dotSize);
                break;
            case 3:
                drawDot(g2d, padding, padding, dotSize);
                drawDot(g2d, size / 2, size / 2, dotSize);
                drawDot(g2d, size - padding, size - padding, dotSize);
                break;
           
            case 4:
                drawDot(g2d, padding, padding, dotSize);
                drawDot(g2d, size - padding, padding, dotSize);
                drawDot(g2d, padding, size - padding, dotSize);
                drawDot(g2d, size - padding, size - padding, dotSize);
                break;
            case 5:
                drawDot(g2d, padding, padding, dotSize);
                drawDot(g2d, size - padding, padding, dotSize);
                drawDot(g2d, size / 2, size / 2, dotSize);
                drawDot(g2d, padding, size - padding, dotSize);
                drawDot(g2d, size - padding, size - padding, dotSize);
                break;
            case 6:
                drawDot(g2d, padding, padding, dotSize);
                drawDot(g2d, size - padding, padding, dotSize);
                drawDot(g2d, padding, size / 2, dotSize);
                drawDot(g2d, size - padding, size / 2, dotSize);
                drawDot(g2d, padding, size - padding, dotSize);
                drawDot(g2d, size - padding, size - padding, dotSize);
                break;
        }
    }

    // Метод для рисования одной точки
    private void drawDot(Graphics2D g2d, int x, int y, int size) {
        g2d.setColor(dotColor);
        g2d.fillOval(x - size / 2, y - size / 2, size, size);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Игральная кость");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        Dice dice = new Dice();
        frame.add(dice);

        frame.pack();
        frame.setVisible(true);
    }
}
