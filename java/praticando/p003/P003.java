package praticando.p003;
import java.util.Scanner;

public class P003 {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.print("Digite um número inteiro: ");
            int num = scanner.nextInt();
            System.out.print("Diite a sua altura: ");
            double altura = scanner.nextDouble();
            System.out.print("Digite o seu nome: ");
            String nome = scanner.next();
            System.out.print("Inteiro digitado: " + num + "\nAltura: " + altura + "\nNome: " + nome);
        }
    }
}
