import java.util.Scanner;

public class b4 {

    private double x1, y1, r1;
    private double x2, y2, r2;

    public b4(double x1, double y1, double r1, double x2, double y2, double r2) {
        this.x1 = x1;
        this.y1 = y1;
        this.r1 = r1;
        this.x2 = x2;
        this.y2 = y2;
        this.r2 = r2;
    }

    public int checkIntersection() {
        // Расстояние между центрами окружностей
        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

        // Сравнение расстояния с суммой и разностью радиусов
        if (r1==r2 && x1==x2 && y1==y2){
            return 7;// Halogenq
        } else if (distance == r1 + r2) {
            return 1; // Касаются в одной точке
        } else if (distance == Math.abs(r1 - r2)) {
            return 2; // Касаются в одной точке (одна окружность вложена в другую)
        } else if (distance < r1 + r2 && distance > Math.abs(r1 - r2)) {
            return 3; // Пересекаются в двух точках
        } else if (distance < Math.abs(r1 - r2)) {
            if (r1 > r2) {
                return 4; // Вторая окружность вложена в первую
            } else {
                return 5; // Первая окружность вложена во вторую
            }
        } else {
            return 6; // Не пересекаются
        }
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите координаты x1, y1 центра первой окружности: ");
        double x1 = scanner.nextDouble();
        double y1 = scanner.nextDouble();

        System.out.print("Введите радиус r1 первой окружности: ");
        double r1 = scanner.nextDouble();

        System.out.print("Введите координаты x2, y2 центра второй окружности: ");
        double x2 = scanner.nextDouble();
        double y2 = scanner.nextDouble();

        System.out.print("Введите радиус r2 второй окружности: ");
        double r2 = scanner.nextDouble();

        b4 circles = new b4(x1, y1, r1, x2, y2, r2);
        int intersectionType = circles.checkIntersection();

        switch (intersectionType) {
            case 1:
                System.out.println("Окружности касаются в одной точке.");
                break;
            case 2:
                System.out.println("Окружности касаются в одной точке (одна окружность вложена в другую).");
                break;
            case 3:
                System.out.println("Окружности пересекаются в двух точках.");
                break;
            case 4:
                System.out.println("Вторая окружность вложена в первую.");
                break;
            case 5:
                System.out.println("Первая окружность вложена во вторую.");
                break;
            case 6:
                System.out.println("Окружности не пересекаются.");
                break;
            case 7:
                System.out.println("Окружности наложены друг на друга.");
                break;
        }
    }
}
