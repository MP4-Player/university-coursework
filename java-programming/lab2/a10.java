import java.util.HashSet;
import java.util.Set;

public class a10 {

    public static void main(String[] args) {
        String str = "abcd";
        Set<String> permutations = a10(str);
        System.out.println("перестановки строки " + str + ":");
        for (String permutation : permutations) {
            System.out.println(permutation);
        }
    }

    public static Set<String> a10(String str) {
        Set<String> permutations = new HashSet<>();
        int length = str.length();

        for (int i = 0; i < length; i++) {
            String permutation =  str.substring(i) + str.substring(0,i) ;
            permutations.add(permutation);
        }

        return permutations;
    }
}
