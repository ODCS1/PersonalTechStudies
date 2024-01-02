package praticando.p006;

import java.util.Scanner;

public class P017 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        int n1 = 2;
        int n2 = 3;
        int n3 = 5;

        // float n4 = 12.5f;

        int n5 = n2 / n1;
        // Valor armazenado 1
        // float n6 = n2 / n1;
        // Valor armazenado 1.0
        // float n7 = (float) n2 / n1;
        // Valor armazenado 1.5

        int vet[] = {n1, n2, n3, n5};

        for (int i : vet) {
            System.out.print(i + " ");
        }

        System.out.println();

        String res = "s";
        int soma = 0;
        while (true) {
            if (!res.equals("n")) { // Correção: Usar equals para comparar strings
                System.out.print("Digite um valor inteiro: ");
                int number = input.nextInt();
                soma += number;
            } else {
                break;
            }

            input.nextLine(); // Consumir a nova linha pendente após a leitura do número

            System.out.print("Quer continuar [s/n]: ");
            res = input.nextLine();
        }

        System.out.println("Soma total dos valores digitados: " + soma);
        input.close();
    }
}

