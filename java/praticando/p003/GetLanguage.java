package praticando.p003;

import java.util.Locale;

public class GetLanguage {
    public static void main(String[] args) {
        Locale loc = Locale.getDefault();

        // Primeira forma de mostrar (pt_BR)
        System.out.println("1° Resultado: " + loc);

        // Segunda forma de mostrar (português)
        System.out.println(String.format("2° Resultado: %s", loc.getDisplayLanguage()));

        // Terceira forma de mostrar (pt)
        System.out.println(String.format("3° Resultado: %s", loc.getLanguage()));
    }
}
