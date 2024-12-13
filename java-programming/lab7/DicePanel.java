import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.util.Random;
import javax.swing.*;

public class DicePanel extends JPanel {
    private int numDots;
    private Color dotColor;
    private Color backgroundColor;
    private boolean active;
    private JButton activateButton;

    public DicePanel() {
        setPreferredSize(new Dimension(100, 100));
        setBackground(Color.WHITE);

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                if (active) {
                    roll();
                }
            }
        });

        activateButton = new JButton("Активировать/Деактивировать");
        activateButton.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                active = !active;
                repaint();
            }
        });

        add(activateButton);

        reset();
    }

    public void setDotColor(Color dotColor) {
        this.dotColor = dotColor;
        repaint();
    }

    public void setBackgroundColor(Color backgroundColor) {
        this.backgroundColor = backgroundColor;
        setBackground(backgroundColor);
        repaint();
    }

    public void reset() {
        numDots = 1;
        dotColor = Color.BLACK;
        backgroundColor = Color.RED;
        active = true;
        repaint();
    }

    private void roll() {
        Random random = new Random();
        numDots = random.nextInt(6) + 1;
        repaint();
    }

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

    private void drawDot(Graphics2D g2d, int x, int y, int size) {
        g2d.setColor(dotColor);
        g2d.fillOval(x - size / 2, y - size / 2, size, size);
    }

    public static void main(String[] args) {
        JFrame frame = new JFrame("Игральная кость");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.add(new DicePanel());
        frame.pack();
        frame.setVisible(true);
    }
}
