import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.Locale;


public class GUI extends JFrame {

    private JComboBox<String> lafComboBox;
    private JLabel label;
    private JButton button;
    private JCheckBox independentCheckBox;
    private JRadioButton dependentRadioButton;
    private JTable table;

    public GUI() {
        setTitle("Графический интерфейс");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new BorderLayout());

        lafComboBox = new JComboBox<>();
        // Получаем доступные LAF
        UIManager.LookAndFeelInfo[] lafs = UIManager.getInstalledLookAndFeels();
        for (UIManager.LookAndFeelInfo laf : lafs) {
            lafComboBox.addItem(laf.getClassName());
        }

        lafComboBox.setSelectedIndex(0);
        label = new JLabel("Выбранный LAF: " + UIManager.getLookAndFeel().getName());

        button = new JButton("Применить LAF");
        button.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                applyLookAndFeel();
            }
        });


        independentCheckBox = new JCheckBox("Независимый флажок");

        dependentRadioButton = new JRadioButton("Зависимый флажок");

        table = new JTable();
        table.setModel(new DefaultTableModel(
                new Object[][]{
                        {"Си", "Деннис Ритчи", 1972},
                        {"C++", "Бьерн Страуструп", 1983},
                        {"Python", "Гвидо ван Россум", 1991},
                        {"Java", "Джеймс Гослинг", 1995},
                        {"JavaScript", "Брендон Айк", 1995},
                        {"C#", "Андерс Хейлсберг", 2001},
                        {"Scala", "Мартин Одерски", 2003}
                },
                new String[]{"Язык", "Автор", "Год"}
        ));

        JPanel topPanel = new JPanel(new FlowLayout());
        topPanel.add(lafComboBox);
        topPanel.add(label);
        topPanel.add(button);
        add(topPanel, BorderLayout.NORTH);

        JPanel bottomPanel = new JPanel(new FlowLayout());
        bottomPanel.add(independentCheckBox);
        bottomPanel.add(dependentRadioButton);
        add(bottomPanel, BorderLayout.SOUTH);

        add(new JScrollPane(table), BorderLayout.CENTER);

        setVisible(true);
    }

    private void applyLookAndFeel() {
        try {
            String lafClassName = lafComboBox.getSelectedItem().toString();
            UIManager.setLookAndFeel(lafClassName);
            SwingUtilities.updateComponentTreeUI(this);
            label.setText("Выбранный LAF: " + UIManager.getLookAndFeel().getName());
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException e) {
            JOptionPane.showMessageDialog(this, "Не удалось применить выбранный LAF: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
        }
    }

    public static void main(String[] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                new GUI();
            }
        });
    }
}

