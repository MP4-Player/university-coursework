import java.util.Scanner;

public class b5 {

    private double x1, y1, r1;
    private double x2, y2, r2;

    public b5(double x1, double y1, double r1, double x2, double y2, double r2) {
        this.x1 = x1;
        this.y1 = y1;
        this.r1 = r1;
        this.x2 = x2;
        this.y2 = y2;
        this.r2 = r2;
    }

    public IntersectionType checkIntersection() {
        // Расстояние между центрами окружностей
        double distance = Math.sqrt(Math.pow(x2 - x1, 2) + Math.pow(y2 - y1, 2));

 // Сравнение расстояния с суммой и разностью радиусов
        if (distance == r1 + r2) {
            return IntersectionType.TOUCH_ONE_POINT; // Касаются в одной точке
        } else if (distance == Math.abs(r1 - r2)) {
            return IntersectionType.TOUCH_ONE_POINT_INSIDE; // Касаются в одной точке (одна окружность вложена в другую)
        } else if (distance < r1 + r2 && distance > Math.abs(r1 - r2)) {
            return IntersectionType.INTERSECT_TWO_POINTS; // Пересекаются в двух точках
        } else if (distance < Math.abs(r1 - r2)) {
            if (r1 > r2) {
                return IntersectionType.INSIDE_FIRST; // Вторая окружность вложена в первую
            } else {
                return IntersectionType.INSIDE_SECOND; // Первая окружность вложена во вторую
            }
        } else {
            return IntersectionType.NO_INTERSECTION; // Не пересекаются
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

        b5 circles = new b5(x1, y1, r1, x2, y2, r2);
        IntersectionType intersectionType = circles.checkIntersection();

        System.out.println("Тип пересечения: " + intersectionType);
    }

    public enum IntersectionType {
        TOUCH_ONE_POINT,
        TOUCH_ONE_POINT_INSIDE,
        INTERSECT_TWO_POINTS,
        INSIDE_FIRST,
        INSIDE_SECOND,
        NO_INTERSECTION
    }
}

