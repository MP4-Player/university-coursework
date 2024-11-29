import java.util.InputMismatchException;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class c1 {

    /* Регистрационный может быть null*/
    private String registrationNumber;
    /* Марка автомобиля не может быть изменена */
    private final String make;
    /* Вид автомобиля (легковой, грузовой, автобус)не может быть изменен*/
    private final VehicleType type;
    /* Цвет автомобиля */
    private String color;
    /* Мощность двигателя */
    private int enginePower;
    /* Количество колес автомобиля не может быть изменена после создания объекта*/
    private final int numberOfWheels;

    /* типы для вида автомобиля*/
    public enum VehicleType {
        CAR, TRUCK, BUS
    }

    /* Конструктор класса c1 Задает начальные характеристики автомобиля*/
    public c1(String make, VehicleType type, String color, int enginePower, int numberOfWheels) {
        this.make = make; /* Инициализация марки */
        this.type = type; /* Инициализация типа */
        this.color = color; /*  цвета */
        this.enginePower = enginePower; /* мощности двигателя*/
        this.numberOfWheels = numberOfWheels; /* количества колес*/
    }

    /* Метод для установки регистрационного номера.  Проверяка корректности.*/
    public void setRegistrationNumber(String registrationNumber) {
        /* Регулярное выражение для проверки формата регистрационного номера */
        Pattern pattern = Pattern.compile("[ABEKMHOPCTYX]{1}\\d{3}[ABEKMHOPCTYX]{2}\\d{2,3}RUS");
        Matcher matcher = pattern.matcher(registrationNumber);
        if (matcher.matches()) {
            this.registrationNumber = registrationNumber; /* Установка номера, если он соответствует формату*/
        } else {
            System.out.println("Неверный формат регистрационного номера!"); 
        }
    }


    /* Метод для получения регистрационного номера.*/
    public String getRegistrationNumber() {
        return registrationNumber;
    }

    /* Метод для получения марки автомобиля.*/
    public String getMake() {
        return make;
    }

    /* Метод для получения типа автомобиля.*/
    public VehicleType getType() {
        return type;
    }
    /* Метод для изменения цвета автомобиля.*/
    public void setColor(String color) {
        this.color = color;
    }

    /* Метод для получения цвета автомобиля.*/
    public String getColor() {
        return color;
    }

    /* Метод для изменения мощности двигателя.*/
    public void setEnginePower(int enginePower) {
        this.enginePower = enginePower;
    }

    /* Метод для получения мощности двигателя.*/
    public int getEnginePower() {
        return enginePower;
    }

    /* Метод для получения количества колес.*/
    public int getNumberOfWheels() {
        return numberOfWheels;
    }


    /* Метод для вывода всех характеристик автомобиля на консоль.*/
    public void printCarInfo() {
        System.out.println("Марка: " + make);
        System.out.println("Тип: " + type);
        System.out.println("Цвет: " + color);
        System.out.println("Мощность двигателя: " + enginePower + " л.с.");
        System.out.println("Количество колес: " + numberOfWheels);
        System.out.println("Регистрационный номер: " + registrationNumber);
        System.out.println("--------------------");
    }

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in); /* Создаем объект Scanner для чтения ввода с консоли*/

        System.out.println("Введите марку автомобиля:");
        String make = scanner.nextLine();

        System.out.println("Введите тип автомобиля (CAR, TRUCK, BUS):");
        VehicleType type = VehicleType.valueOf(scanner.nextLine().toUpperCase()); /*  Обработка регистра*/

        System.out.println("Введите цвет автомобиля:");
        String color = scanner.nextLine();

        int enginePower = 0;
        while (enginePower <=0){
            try{
                System.out.println("Введите мощность двигателя (в л.с.):");
                enginePower = scanner.nextInt();
                if (enginePower <= 0){
                    System.out.println("Мощность двигателя должна быть больше 0!");
                }
            } catch (InputMismatchException e){
                System.out.println("Некорректный ввод. Введите целое число.");
                scanner.next(); /* Очистка буфера сканера*/
            }
        }
        scanner.nextLine(); /* Очистка буфера сканера*/


        System.out.println("Введите количество колес:");
        int numberOfWheels = scanner.nextInt();
        scanner.nextLine(); /* Очистка буфера сканера*/

        c1 myCar = new c1(make, type, color, enginePower, numberOfWheels);

        System.out.println("Начальные характеристики:");
        myCar.printCarInfo();


        System.out.println("Хотите изменить характеристики? (yes/no)");
        String change = scanner.nextLine();

        if (change.equalsIgnoreCase("yes")) {
            System.out.println("Введите новый цвет:");
            myCar.setColor(scanner.nextLine());

            int newEnginePower = 0;
            while (newEnginePower <=0){
                try{
                    System.out.println("Введите новую мощность двигателя (в л.с.):");
                    newEnginePower = scanner.nextInt();
                    if (newEnginePower <= 0){
                        System.out.println("Мощность двигателя должна быть больше 0!");
                    }
                    myCar.setEnginePower(newEnginePower);
                } catch (InputMismatchException e){
                    System.out.println("Некорректный ввод. Введите целое число.");
                    scanner.next(); /* Очистка буфера сканера*/
                }
            }
            scanner.nextLine(); /* Очистка буфера сканера*/

            System.out.println("Введите регистрационный номер (или нажмите Enter, чтобы пропустить):");
            String regNumber = scanner.nextLine();
            if (!regNumber.isEmpty()) {
                myCar.setRegistrationNumber(regNumber);
            }
        }

        System.out.println("\nОкончательные характеристики:");
        myCar.printCarInfo();

        scanner.close(); /* Закрываем Scanner*/
    }
}
