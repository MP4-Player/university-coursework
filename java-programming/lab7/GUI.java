import javax.swing.*;
import javax.swing.table.DefaultTableModel;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.util.Arrays;
import java.util.Enumeration;
import java.util.Locale; // Импортируем класс Enumeration (не используется в текущем коде, можно удалить)


public class GUI extends JFrame { 
    private JComboBox<String> lafComboBox; // Комбобокс для выбора Look and Feel
    private JLabel label; // Метка для отображения информации о выбранном LAF
    private JButton button; // Кнопка для применения выбранного LAF
    private JCheckBox independentCheckBox; // Независимый флажок (checkbox)
    private JRadioButton dependentRadioButton; // Зависимый флажок (radio button)
    private JRadioButton dependentRadioButton2;
    private JTable table; // Таблица для отображения данных
    private JTextArea textArea; // Текстовое поле для вывода информации о состоянии флажков

    public GUI() { // Конструктор класса GUI
        setTitle("Графический интерфейс"); // Устанавливаем заголовок окна
        setSize(800, 400); // Устанавливаем размер окна
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE); // Устанавливаем действие при закрытии окна (завершение программы)
        setLayout(new BorderLayout()); // Устанавливаем менеджер компоновки BorderLayout

        lafComboBox = new JComboBox<>(); // Создаем комбобокс
        UIManager.LookAndFeelInfo[] lafs = UIManager.getInstalledLookAndFeels(); // Получаем массив доступных Look and Feel
        for (UIManager.LookAndFeelInfo laf : lafs) { // Цикл для добавления каждого LAF в комбобокс
            lafComboBox.addItem(laf.getClassName()); // Добавляем имя класса LAF в комбобокс
        }
        lafComboBox.setSelectedIndex(0); // Устанавливаем выбранный элемент по умолчанию (первый)
        label = new JLabel("Выбранный LAF: " + UIManager.getLookAndFeel().getName()); // Создаем метку с информацией о текущем LAF

        button = new JButton("Применить LAF"); // Создаем кнопку
        button.addActionListener(new ActionListener() { // Добавляем обработчик событий для кнопки
            @Override
            public void actionPerformed(ActionEvent e) { // Метод, который вызывается при нажатии кнопки
                applyLookAndFeel(); // Вызываем метод для применения выбранного LAF
            }
        });

        independentCheckBox = new JCheckBox("Независимый флажок"); // Создаем независимый флажок
        independentCheckBox.addActionListener(e -> { // Добавляем обработчик событий для независимого флажка (лямбда-выражение)
            textArea.append("Независимый флажок: " + independentCheckBox.isSelected() + "\n"); // Добавляем информацию в текстовое поле
        });

        dependentRadioButton = new JRadioButton("Зависимый флажок"); // Создаем зависимый флажок (радиокнопка)
        dependentRadioButton2 = new JRadioButton("Зависимый флажок"); // Создаем зависимый флажок (радиокнопка)
        ButtonGroup rg=new ButtonGroup();
        rg.add(dependentRadioButton);
        rg.add(dependentRadioButton2);
        dependentRadioButton.addActionListener(e -> { // Добавляем обработчик событий для зависимого флажка (лямбда-выражение)
            textArea.append("Зависимый флажок: " + dependentRadioButton.isSelected() + "\n"); // Добавляем информацию в текстовое поле
        });

        table = new JTable(); // Создаем таблицу
        table.setModel(new DefaultTableModel( // Устанавливаем модель таблицы
                new Object[][]{
                        {"Си", "Деннис Ритчи", 1972},
                        {"C++", "Бьерн Страуструп", 1983},
                        {"Python", "Гвидо ван Россум", 1991},
                        {"Java", "Джеймс Гослинг", 1995},
                        {"JavaScript", "Брендон Айк", 1995},
                        {"C#", "Андерс Хейлсберг", 2001},
                        {"Scala", "Мартин Одерски", 2003}
                },
                new String[]{"Язык", "Автор", "Год"} // Заголовки столбцов
        ));

        textArea = new JTextArea(10, 30); // Создаем текстовое поле
        textArea.setEditable(false); // Делаем текстовое поле нередактируемым
        JScrollPane scrollPane = new JScrollPane(textArea); // Создаем JScrollPane для прокрутки текстового поля

        JPanel topPanel = new JPanel(new FlowLayout()); // Создаем панель для верхних компонентов
        topPanel.add(lafComboBox); // Добавляем комбобокс на панель
        topPanel.add(label); // Добавляем метку на панель
        topPanel.add(button); // Добавляем кнопку на панель
        add(topPanel, BorderLayout.NORTH); // Добавляем панель в северную область окна

        JPanel centerPanel = new JPanel(new FlowLayout()); // Создаем панель для центральных компонентов
        centerPanel.add(new JScrollPane(table)); // Добавляем таблицу в панель с прокруткой
        add(centerPanel, BorderLayout.CENTER); // Добавляем панель в центральную область окна

        JPanel bottomPanel = new JPanel(new FlowLayout()); // Создаем панель для нижних компонентов
        bottomPanel.add(independentCheckBox); // Добавляем независимый флажок на панель
        bottomPanel.add(dependentRadioButton);
        bottomPanel.add(dependentRadioButton2); // Добавляем зависимый флажок на панель
        add(bottomPanel, BorderLayout.SOUTH); // Добавляем панель в южную область окна

        add(scrollPane, BorderLayout.EAST); // Добавляем текстовое поле с прокруткой в восточную область окна

        setVisible(true); // Отображаем окно
    }

    private void applyLookAndFeel() { // Метод для применения выбранного LAF
        try {
            String lafClassName = lafComboBox.getSelectedItem().toString(); // Получаем имя класса LAF из комбобокса
            UIManager.setLookAndFeel(lafClassName); // Устанавливаем выбранный LAF
            SwingUtilities.updateComponentTreeUI(this); // Обновляем графический интерфейс
            label.setText("Выбранный LAF: " + UIManager.getLookAndFeel().getName()); // Обновляем метку с информацией о LAF
        } catch (ClassNotFoundException | InstantiationException | IllegalAccessException | UnsupportedLookAndFeelException e) { // Обработка возможных исключений
            JOptionPane.showMessageDialog(this, "Не удалось применить выбранный LAF: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE); // Отображение сообщения об ошибке
        }
    }

    public static void main(String[] args) { // Точка входа в программу
        SwingUtilities.invokeLater(new Runnable() { // Запуск в потоке Swing для обеспечения безопасности UI
            @Override
            public void run() { // Метод, который выполняется в потоке Swing
                new GUI(); // Создание и отображение окна GUI
            }
        });
    }
}
