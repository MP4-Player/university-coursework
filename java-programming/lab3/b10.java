import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class b10 {

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("Введите телефонный номер: ");
        String phoneNumber = scanner.nextLine();

        if (isValidPhoneNumber(phoneNumber)) {
            System.out.println("Номер валиден.");
        } else {
            System.out.println("Номер невалиден.");
        }

        // System.out.print("Введите строку для поиска номеров телефонов: ");
        // String text = scanner.nextLine();
        String text = "Мои номера 220-30-40 и 8904-378-16-61 не считая служебных";

        List<String> phoneNumbers = extractPhoneNumbers(text);
        System.out.println("Найденные номера телефонов: " + phoneNumbers);
    }

    public static boolean isValidPhoneNumber(String phoneNumber) {
        // Регулярное выражение для проверки телефонных номеров 
        // (мобильных и городских):
        String regex = "^(\\+7|8)[- ]?(\\(?\\d{3}\\)?|\\d{3})[- ]?\\d{3}[- ]?\\d{2}[- ]?\\d{2}$|" +
                       "^\\d{3}[- ]?\\d{2}[- ]?\\d{2}$|" +
                       "^\\d{7}$";
        
        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(phoneNumber);
        return matcher.matches();
    }

    public static List<String> extractPhoneNumbers(String text) {
        List<String> phoneNumbers = new ArrayList<>();
        // Регулярное выражение для извлечения телефонных номеров

        String regex = "(\\+7|8)[- ]?(\\(?\\d{3}\\)?|\\d{3})[- ]?\\d{3}[- ]?\\d{2}[- ]?\\d{2}|" +
                       "\\d{3}-\\d{2}-\\d{2}|" +
                       "\\d{7}";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(text);

        while (matcher.find()) {
            phoneNumbers.add(matcher.group());
        }

        return phoneNumbers;
    }
}

