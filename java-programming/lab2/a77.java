import java.util.Scanner;

public class a77 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String str = scanner.nextLine();
        int letter = 0;
        int lower = 0;
        int upper = 0;
        int digit = 0;
        int arab_digit = 0;
        int non_arab_digit = 0;
        int other = 0;

        for (char s : str.toCharArray()){
            if (Character.isLetter(s)) {
                letter++;
                if (Character.isLowerCase(s)) {
                    lower++;
                } else if (Character.isUpperCase(s)) {
                    upper++;
                }
            } else if (Character.isDigit(s)) {
                digit++;
                if (isArabicDigit(s)) {
                    arab_digit++;
                } else {
                    non_arab_digit++;
                }
            } else {
                other++;
            }

        }
        System.out.println("Общее количество символов: " + str.length());
        System.out.println("Букв: " + letter);
        System.out.println("Строчных букв: " + lower);
        System.out.println("Прописных букв: " + upper);
        System.out.println("Цифр: " + digit);
        System.out.println("Арабских цифр: " + arab_digit);
        System.out.println("Не арабских цифр: " + non_arab_digit);
        System.out.println("Другое: " + other);
    }
    public static boolean isArabicDigit(char c) {
        return c >= '0' && c <= '9';
    }

}
