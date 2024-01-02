package praticando.p005;
import java.util.Scanner;

public class P011 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite o primeiro número: ");
        int num = input.nextInt();

        System.out.print("Digite o segundo número: ");
        int num2 = input.nextInt();

        input.close();

        int soma = num + num2;
        int sub = num - num2;
        float div = (float) num / num2;
        float resto = (float) num % num2;

        System.out.printf("Soma: %d \nSubtração: %d \nDivisão: %.2f \nResto: %.2f", soma, sub, div, resto);
    }
}

