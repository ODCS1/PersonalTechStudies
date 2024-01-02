package praticando.p007;
import java.util.Random;

public class P022 {
    public static void main(String[] args) {
        Random randon = new Random();

        int num = randon.nextInt(5) + 1;
        double n = randon.nextDouble();
        boolean confirma = randon.nextBoolean();

        System.out.println(num);
        System.out.println(n);
        System.out.print(confirma);
    }
}
