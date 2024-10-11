import java.util.Scanner;

public class a9 {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        System.out.print("Введите строку: ");
        String str = scanner.nextLine();
        System.out.print("Введите подстроку: ");
        String pod_str = scanner.nextLine();

        int count = countPodStr(str, pod_str);

        System.out.println("Подстрока " + pod_str + " встречается " + count + " раз(а).");
    }

    public static int countPodStr(String str, String substring) {
        int count = 0;
        int index = str.indexOf(substring);

        while (index != -1) {
            count++;
            index = str.indexOf(substring, index + substring.length());
        }

        return count;
    }
}