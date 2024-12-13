import java.awt.*;
import javax.swing.*;

public class ThreeLabelPanel extends JPanel {
    private JLabel upperLabel;
    private JLabel downLabel;
    private JLabel centerLabel;

    public ThreeLabelPanel() {
        Font upperDownFont = new Font("Dialog", Font.BOLD | Font.ITALIC, 10);
        Font centerFont = new Font("Dialog", Font.BOLD, 18);

        upperLabel = new JLabel("Текст верхней метки");
        upperLabel.setFont(upperDownFont);
        upperLabel.setHorizontalAlignment(SwingConstants.LEFT);

        downLabel = new JLabel("Текст нижней метки");
        downLabel.setFont(upperDownFont);
        downLabel.setHorizontalAlignment(SwingConstants.RIGHT);

        centerLabel = new JLabel("Текст центральной метки");
        centerLabel.setFont(centerFont);
        centerLabel.setHorizontalAlignment(SwingConstants.CENTER);

        setLayout(new BorderLayout());
        add(upperLabel, BorderLayout.NORTH);
        add(downLabel, BorderLayout.SOUTH);
        add(centerLabel, BorderLayout.CENTER);
    }

    // Метод для задания цвета фона панели
    public void setBackgroundColor(Color color) {
        setBackground(color);
    }

    // Методы для задания текста каждой метки
    public void setUpperLabelText(String text) {
        upperLabel.setText(text);
    }

    public void setDownLabelText(String text) {
        downLabel.setText(text);
    }

    public void setCenterLabelText(String text) {
        centerLabel.setText(text);
    }

    // Переопределение метода paintComponent для правильной прорисовки
    @Override
    protected void paintComponent(Graphics g) {
        super.paintComponent(g); // Вызываем paintComponent родительского класса
    }


    public static void main(String[] args) {
        JFrame frame = new JFrame("Three Label Panel");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setSize(400, 300);

        ThreeLabelPanel panel = new ThreeLabelPanel();
        panel.setBackgroundColor(Color.YELLOW); // Устанавливаем жёлтый фон
        panel.setUpperLabelText("посмотри вниз!");
        panel.setDownLabelText("Посмотри на верх!");
        panel.setCenterLabelText("ты солнышко");
        frame.add(panel);

        frame.setVisible(true);
    }
}
