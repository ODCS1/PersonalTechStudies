package praticando.p009;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class P039 {
    public static void main(String[] args) {
        String email = "exemplo@dominio.com";
        String regex = "^[A-Za-z0-9+_.-]+@[A-Za-z0-9.-]+$";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(email);

        if (matcher.matches()) {
            System.out.println("O endereço de e-mail é válido.");
        } else {
            System.out.println("O endereço de e-mail é inválido.");
        }
    }
}
