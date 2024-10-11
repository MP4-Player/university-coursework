public class a5 {

    public static void main(String[] args) {
        if (args.length != 1) {
            System.err.println("Необходимо ввести одно целое число в качестве аргумента ");
            return;
        }

        try {
            int decimalNumber = Integer.parseInt(args[0]);

            System.out.println("Десятичное: " + decimalNumber);
            System.out.println("Двоичное: " + Integer.toBinaryString(decimalNumber));
            System.out.println("Восьмеричное: " + Integer.toOctalString(decimalNumber));
            System.out.println("Шестнадцатеричное: " + Integer.toHexString(decimalNumber));

        } catch (NumberFormatException e) {
            System.err.println("Некорректный формат числа. Введите целое десятичное число.");
        }
    }
}
