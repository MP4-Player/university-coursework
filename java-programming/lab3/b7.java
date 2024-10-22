import java.util.Scanner;

public class b7 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите десятичное число: ");
        int decimalNumber = scanner.nextInt();

        System.out.print("Введите основание системы счисления (от 2 до 8): ");
        int base = scanner.nextInt();

        if (base < 2 || base > 8) {
            System.err.println("Некорректное основание системы счисления. Введите число от 2 до 8.");
            return;
        }

        String convertedNumber = convertToBase(decimalNumber, base);
        System.out.println("Число " + decimalNumber + " в системе счисления с основанием " + base + ": " + convertedNumber);
    }

    public static String convertToBase(int decimalNumber, int base) {
        StringBuilder result = new StringBuilder();

        if (decimalNumber == 0) {
            return "0";
        }

        while (decimalNumber > 0) {
            int remainder = decimalNumber % base;
            result.insert(0, remainder); // Вставляем остаток в начало строки
            decimalNumber /= base;
        }

        return result.toString();
    }
}

