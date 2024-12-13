import java.awt.*;
import javax.swing.*;

public class Main {
    public static void main(String[] args) {
        JFrame frame = new JFrame("Игральная кость");
        frame.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        frame.setLayout(new FlowLayout());

        DicePanel dicePanel = new DicePanel();
        dicePanel.setDotColor(Color.RED);
        dicePanel.setBackgroundColor(Color.YELLOW);

        frame.add(dicePanel);
        frame.pack();
        frame.setVisible(true);
    }
}
