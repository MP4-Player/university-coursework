import java.awt.Color;
import java.awt.FlowLayout;
import java.awt.Font;
import java.awt.Frame;
import java.awt.Label;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.event.WindowAdapter;
import java.awt.event.WindowEvent;
import java.util.Random;
/** Simple Frame with Label
@version 1.0
@author Mister X
*/
public class HelloFrame extends Frame {

/** Program entry point */
    public static void main(String[] args) throws Exception {
        HelloFrame hello = new HelloFrame();
        hello.setTitle("Hello!");
        hello.setBackground(Color.black);
        hello.setLayout(new FlowLayout());
        hello.setLabelAttributes(firstLabel);
        hello.setLabelAttributes(secondLabel);
        hello.add(firstLabel);
        hello.add(secondLabel);
        hello.addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                Random rnd = new Random();
                int idx = rnd.nextInt(4);
                secondLabel.setText(text[idx]);
            }
        });
        hello.addWindowListener(new WindowAdapter() {
            @Override
            public void windowClosing(WindowEvent we) {
            System.exit(0);
            }
        });
        hello.setBounds(300,300,260, 80);
        hello.setVisible(true);
    }
/** method that changes Label attributes
    @param label - concrete Label
    */
    private void setLabelAttributes(Label label) {
        Font font = new Font(Font.MONOSPACED, Font.PLAIN, 22);
        label.setFont(font);
        label.setBackground(Color.WHITE);
        label.setForeground(Color.PINK);
    }
    /** field - reference array of strings */
    private static String[] text = {"Word", "Lord", "Nord", "Sword"};

    /** field - Label for preamble */
    private static final Label firstLabel = new Label("Hello my");
    /** field - Label for variants of answers */
    private static final Label secondLabel = new Label(text[0]);
}
