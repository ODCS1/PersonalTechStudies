package praticando.p002;
import java.util.Scanner;

public class JogoAdvinha {
    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);
        int numeroAleatorio = (int) (Math.random() * 100) + 1;
        int tentativas = 0;
        int palpite = 0;

        System.out.println("Bem-vindo ao jogo de adivinhação!");
        System.out.println("Tente adivinhar o número entre 1 e 100.");

        while (palpite != numeroAleatorio) {
            System.out.print("Digite o seu palpite: ");
            palpite = scanner.nextInt();
            tentativas++;

            if (palpite < numeroAleatorio) {
                System.out.println("Tente um número maior!");
            } else if (palpite > numeroAleatorio) {
                System.out.println("Tente um número menor!");
            } else {
                System.out.println("Parabéns! Você acertou o número em " + tentativas + " tentativas!");
            }
        }

        scanner.close();
    }
}

