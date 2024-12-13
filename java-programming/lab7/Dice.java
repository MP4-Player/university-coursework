import java.awt.*;
import javax.swing.*;

public class Dice extends JPanel {
    private int numDots = 1;
    private Color dotColor = Color.BLACK;
    private boolean buttonEnabled = true;
    private JButton changeButton;
    private JButton activateButton;

    public Dice() {
        setLayout(new BorderLayout());

        JPanel dicePanel = new JPanel() {
            @Override
            protected void paintComponent(Graphics g) {
                super.paintComponent(g);
                Graphics2D g2d = (Graphics2D) g;
                g2d.setRenderingHint(RenderingHints.KEY_ANTIALIASING, RenderingHints.VALUE_ANTIALIAS_ON);

                int size = Math.min(getWidth(), getHeight());
                int dotSize = size / 10;
                int padding = size / 10;

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
        };
        dicePanel.setPreferredSize(new Dimension(100, 100));
        dicePanel.setBackground(Color.WHITE);
        add(dicePanel, BorderLayout.NORTH);


        changeButton = new JButton("Изменить количество точек");
        changeButton.addActionListener(e -> {
            if (buttonEnabled) {
                numDots = (numDots % 6) + 1;
                dicePanel.repaint();
            }
        });

        activateButton = new JButton("Активировать/Деактивировать");
        activateButton.addActionListener(e -> {
            buttonEnabled = !buttonEnabled;
            changeButton.setEnabled(buttonEnabled);
            activateButton.setText(buttonEnabled ? "Деактивировать" : "Активировать");
        });


        JPanel buttonPanel = new JPanel();
        buttonPanel.add(changeButton);
        buttonPanel.add(activateButton);
        add(buttonPanel, BorderLayout.SOUTH);
    }

    private void drawDot(Graphics2D g2d, int x, int y, int size) {
        g2d.setColor(dotColor);
        g2d.fillOval(x - size / 2, y - size / 2, size, size);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Игральная кость");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new Dice());
        frame.pack();
        frame.setVisible(true);
    }
}
