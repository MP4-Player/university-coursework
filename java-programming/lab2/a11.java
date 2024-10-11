import java.util.HashSet;
import java.util.Set;
public class a11 {

    public static void main(String[] args) {
        String str = "abcd";
        Set<String> permutations = a11(str);
        System.out.println("Циклические перестановки строки " + str + ":");
        for (String permutation : permutations) {
            System.out.println(permutation);
        }
    }

    public static Set<String> a11(String str) {
        Set<String> permutations = new HashSet<>();
        int length = str.length();

        for (int i = 0; i < length; i++) {
            String permutation = str.substring(length - i) + str.substring(0, length - i);
            permutations.add(permutation);
        }

        return permutations;
    }
}



