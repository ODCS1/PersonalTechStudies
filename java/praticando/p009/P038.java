package praticando.p009;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class P038 {
    public static void main(String[] args) {
        String string1 = "12345";
        String string2 = "abc123";

        String regex = "\\d+";

        Pattern pattern = Pattern.compile(regex);

        Matcher matcher1 = pattern.matcher(string1);
        boolean apenasDigitos1 = matcher1.matches();
        System.out.println("A string1 contém apenas dígitos? " + apenasDigitos1);

        Matcher matcher2 = pattern.matcher(string2);
        boolean apenasDigitos2 = matcher2.matches();
        System.out.println("A string2 contém apenas dígitos? " + apenasDigitos2);
    }
}
