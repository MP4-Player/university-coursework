public class a7 {

    public static void main(String[] args) {
        String inputString = "Привет, мир! 12345, арабские цифры - 123";

        // Подсчет символов
        int totalLetters = 0;
        int lowercaseLetters = 0;
        int uppercaseLetters = 0;
        int digits = 0;
        int arabicDigits = 0;
        int nonArabicDigits = 0;
        int otherChars = 0;

        // Анализ строки
        for (char c : inputString.toCharArray()) { //Метод java string toCharArray() преобразует эту строку в массив символов. Он возвращает вновь созданный массив символов, его длина аналогична этой строке и его содержимое инициализируется символами этой строки.
            if (Character.isLetter(c)) {
                totalLetters++;
                if (Character.isLowerCase(c)) {
                    lowercaseLetters++;
                } else {
                    uppercaseLetters++;
                }
            } else if (Character.isDigit(c)) {
                digits++;
                if (c >= '0' && c <= '9') {  // Проверка на арабские цифры
                    arabicDigits++;
                } else {
                    nonArabicDigits++;
                }
            } else {
                otherChars++;
            }
        }

        // Вывод результатов
        System.out.println("Статистика строки:");
        System.out.println("Общее количество символов: " + inputString.length());
        System.out.println("Количество букв: " + totalLetters);
        System.out.println("Количество строчных букв: " + lowercaseLetters);
        System.out.println("Количество прописных букв: " + uppercaseLetters);
        System.out.println("Количество цифр: " + digits);
        System.out.println("Количество арабских цифр: " + arabicDigits);
        System.out.println("Количество не арабских цифр: " + nonArabicDigits);
        System.out.println("Количество других символов: " + otherChars);
    }
}

