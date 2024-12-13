import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;

public class MouseCoordinates extends JFrame {

    private Color textColor = Color.BLACK; // Начальный цвет текста

    public MouseCoordinates() {
        setTitle("Координаты курсора");
        setSize(400, 300);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        // Добавляем обработчик событий мыши
        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                // Отрисовка координат в нужном месте
                repaint();
            }
        });

        addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyPressed(java.awt.event.KeyEvent evt) {
                // Обработка нажатий клавиш для изменения цвета
                char key = evt.getKeyChar();
                switch (key) {
                    case 'b':
                        textColor = Color.BLACK;
                        break;
                    case 'w':
                        textColor = Color.WHITE;
                        break;
                    case 'r':
                        textColor = Color.RED;
                        break;
                    case 'g':
                        textColor = Color.GREEN;
                        break;
                    case 'o':
                        textColor = Color.ORANGE;
                        break;
                    default:
                        break;
                }
                repaint(); // Перерисовка после смены цвета
            }
        });

        setVisible(true);
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);
        Graphics2D g2d = (Graphics2D) g;
        g2d.setColor(textColor);


        // Получение координат последнего клика мыши
        Point lastClick = MouseInfo.getPointerInfo().getLocation();
        Point relativeCoordinates = this.getLocationOnScreen();
        int x = lastClick.x - relativeCoordinates.x;
        int y = lastClick.y - relativeCoordinates.y;


        // Проверка на выход за пределы окна
        if (x >= 0 && x < getWidth() && y >= 0 && y < getHeight()){
            g2d.drawString("X: " + x + ", Y: " + y, x + 10, y + 10); // Отображение координат
        }

    }


    public static void main(String[] args) {
        new MouseCoordinates();
    }
}

