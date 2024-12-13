import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import javax.swing.*;

public class Dice extends JPanel { // Объявление класса Dice, который наследуется от JPanel (панель)
    private int numDots; // Переменная для хранения количества точек на кости (от 1 до 6)
    private Color dotColor; // Переменная для хранения цвета точек
    private Color backgroundColor; // Переменная для хранения цвета фона кости
    private boolean active; // Переменная для хранения состояния кости (активна/неактивна)
    private JButton activateButton; // Кнопка для переключения состояния кости

    public Dice() { // Конструктор класса Dice с параметрами по умолчанию
        this(1, Color.BLACK, Color.WHITE, true); // Вызов конструктора с параметрами по умолчанию
    }

    public Dice(int numDots, Color dotColor, Color backgroundColor, boolean active) { // Конструктор класса Dice с параметрами
        this.numDots = numDots; // Инициализация количества точек
        this.dotColor = dotColor; // Инициализация цвета точек
        this.backgroundColor = backgroundColor; // Инициализация цвета фона
        this.active = active; // Инициализация состояния кости
        setPreferredSize(new Dimension(100, 100)); // Установка предпочтительного размера кости
        setBackground(backgroundColor); // Установка цвета фона кости

        addMouseListener(new MouseAdapter() { // Добавление обработчика событий мыши
            @Override
            public void mouseClicked(MouseEvent e) { // Метод, вызываемый при клике мышью
                if (active) { // Проверка состояния кости
                    roll(); // Вызов метода roll для бросания кости, если она активна
                }
            }
        });

        activateButton = new JButton("Активировать/Деактивировать"); // Создание кнопки для активации/деактивации
        activateButton.addActionListener(e -> setActive(!active)); // Добавление обработчика событий для кнопки

        setLayout(new BoxLayout(this, BoxLayout.Y_AXIS)); // Установка менеджера компоновки BoxLayout для вертикального расположения
        add(Box.createRigidArea(new Dimension(0, 5))); // Добавление отступа
        /*add(this); // Добавление самой кости на панель*/
        add(Box.createRigidArea(new Dimension(0, 5))); // Добавление отступа
        add(activateButton); // Добавление кнопки на панель
    }

    public void roll() { // Метод для имитации бросания кости
        Random random = new Random(); // Создание объекта Random для генерации случайных чисел
        numDots = random.nextInt(6) + 1; // Генерация случайного числа от 1 до 6
        repaint(); // Перерисовка кости
    }

    public void setDotColor(Color dotColor) { // Метод для установки цвета точек
        this.dotColor = dotColor;
        repaint(); // Перерисовка кости
    }

    public void setBackgroundColor(Color backgroundColor) { // Метод для установки цвета фона
        this.backgroundColor = backgroundColor;
        setBackground(backgroundColor); // Установка цвета фона кости
        repaint(); // Перерисовка кости
    }

    public void setActive(boolean active) { // Метод для установки состояния кости (активна/неактивна)
        this.active = active; // Установка состояния кости
        activateButton.setText(active ? "Деактивировать" : "Активировать"); // Изменение текста кнопки в зависимости от состояния кости
    }

    public int getNumDots() { // Метод для получения количества точек на кости
        return numDots; // Возврат количества точек
    }

    @Override
    protected void paintComponent(Graphics g) { // Метод для отрисовки кости
        super.paintComponent(g); // Вызов метода paintComponent родительского класса
        Graphics2D g2d = (Graphics2D) g; // Преобразование Graphics в Graphics2D
        g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON); // Включение сглаживания

        int size = Math.min(getWidth(), getHeight()); // Определение минимального размера ширины и высоты
        int dotSize = size / 10; // Определение размера точки
        int padding = size / 10; // Определение отступа

        switch (numDots) { // Отрисовка точек в зависимости от количества
            case 1:
                drawDot(g2d, size / 2, size / 2, dotSize); // Рисование одной точки в центре
                break;
            case 2:
                drawDot(g2d, padding, padding, dotSize); // Рисование точки в левом верхнем углу
                drawDot(g2d, size - padding, size - padding, dotSize); // Рисование точки в правом нижнем углу
                break;
            case 3:
                drawDot(g2d, padding, padding, dotSize); // Рисование точки в левом верхнем углу
                drawDot(g2d, size / 2, size / 2, dotSize); // Рисование точки в центре
                drawDot(g2d, size - padding, size - padding, dotSize); // Рисование точки в правом нижнем углу
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

    private void drawDot(Graphics2D g2d, int x, int y, int size) { // Метод для рисования одной точки
        g2d.setColor(dotColor); // Установка цвета точки
        g2d.fillOval(x - size / 2, y - size / 2, size, size); // Рисование точки
    }

    public static void main(String[] args) { // Главный метод
        JFrame frame = new JFrame("Игральная кость"); // Создание фрейма
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Установка действия при закрытии фрейма
        frame.setLayout(new FlowLayout()); // Установка менеджера компоновки

        Dice dice = new Dice(); // Создание объекта Dice
        frame.add(dice); // Добавление кости на фрейм

        frame.pack(); // Упаковка фрейма
        frame.setVisible(true); // Отображение фрейма
    }
}
