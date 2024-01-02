package praticando.p009;

import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class P037 {
    public static void main(String[] args) {
        String regex = "aba";
        String texto = "abababa";

        Pattern pattern = Pattern.compile(regex);
        Matcher matcher = pattern.matcher(texto);

        System.out.println("texto: " + texto);
        System.out.println("Índice: 0123456789");
        System.out.println("Regex: " + regex);
        System.out.println("Posições encontradas");

        while (matcher.find()) {
            System.out.print("Posição: " + matcher.start() + " - Valor: " + matcher.group() + "\n");
        }
    }
}
