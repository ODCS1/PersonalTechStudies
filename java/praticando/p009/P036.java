package praticando.p009;
import java.util.Random;

public class P036 {
    public static void main(String[] args) {
        Random aleatorio = new Random();
        int numero = aleatorio.nextInt(11) + 5;
        // intervalo entre [5, 10]
        System.out.println("Número aleatório: " + numero);
    }
}
