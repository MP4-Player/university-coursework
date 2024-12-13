import java.awt.*;
import java.awt.event.ComponentAdapter;
import java.awt.event.ComponentEvent;
import java.awt.event.MouseAdapter;
import java.awt.event.MouseEvent;
import java.awt.geom.AffineTransform;
import java.awt.image.BufferedImage;
import java.io.File;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.*;

public class ImageViewer extends JFrame {

    private BufferedImage image;
    private boolean flipped = false;

    public ImageViewer(String imagePath) {
        setTitle("Просмотр изображения");
        setSize(600, 400);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);

        try {
            image = ImageIO.read(new File(imagePath));
            if (image == null) {
                throw new IOException("Не удалось загрузить изображение");
            }
        } catch (IOException e) {
            JOptionPane.showMessageDialog(this, "Ошибка загрузки изображения: " + e.getMessage(), "Ошибка", JOptionPane.ERROR_MESSAGE);
            System.exit(1);
        }

        addMouseListener(new MouseAdapter() {
            @Override
            public void mouseClicked(MouseEvent e) {
                flipped = !flipped;
                repaint();
            }
        });

        // Обработчик изменения размера окна
        addComponentListener(new ComponentAdapter() {
            @Override
            public void componentResized(ComponentEvent e) {
                repaint(); // Перерисовываем изображение при изменении размера
            }
        });

        setVisible(true);
    }

    @Override
    public void paint(Graphics g) {
        super.paint(g);// Вызываем метод paint() суперкласса для отрисовки базовых элементов
        Graphics2D g2d = (Graphics2D) g;

        if (image == null) return;// Если изображение не загружено, выходим из метода

        int width = getWidth();// Получаем ширину и высоту компонента
        int height = getHeight();

        double imageAspect = (double) image.getWidth() / image.getHeight();// Вычисляем соотношение сторон окна
        double windowAspect = (double) width / height;

        int displayWidth, displayHeight;
        if (imageAspect > windowAspect) {
            displayWidth = width;// Устанавливаем ширину отображаемого изображения равной ширине окна
            displayHeight = (int) (width / imageAspect);
        } else {
            displayWidth = (int) (height * imageAspect);
            displayHeight = height;// Устанавливаем высоту отображаемого изображения равной высоте окна
        }

        int x = (width - displayWidth) / 2;// Вычисляем координату x у для центрирования изображения
        int y = (height - displayHeight) / 2;

        AffineTransform transform = new AffineTransform();
        if (flipped) {
            transform.translate(displayWidth, displayHeight);
            transform.scale(-1, -1);// Вычисляем координату x для центрирования изображения
        }

        g2d.drawImage(image, x, y, displayWidth, displayHeight, null);

    }

    public static void main(String[] args) {
        new ImageViewer("photo_2024-12-13_01-09-58.jpg");
    }
}



