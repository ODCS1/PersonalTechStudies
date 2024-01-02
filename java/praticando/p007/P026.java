package praticando.p007;
import java.util.Scanner;

public class P026 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite um inteiro entre 1-10: ");
        String numStr = input.nextLine();

        // do {
        //     System.out.println("teste");
        // } while (true);


        // VALIDADOR
        while (true) {
            if (numStr.matches("[0-9]+")) {
                int num = Integer.parseInt(numStr);
                if (num >= 1 && num <= 10) {
                    System.out.print("Número válido!");

                    break;
                } else {
                    System.out.print("Número inválido! Digite um inteiro entre 1-10: ");
                    numStr = input.nextLine();
                }
            } else {
                System.out.print("Entrada inválida! Digite um inteiro entre 1-10: ");
                numStr = input.nextLine();
            }
        }

        input.close();
    }

    public static void validador() {
        System.out.println();
    }

    /*
     * Matches é um método da classe String que
     * verifica se o valor da string corresponde
     * a uma determinada expressão regular
     * também conhecido como regex, que são
     * validadores para o que você precisar,
     * no caso [0,9] indica que para 1 dígito
     * deve estar dentro desse intervalo, com
     * o "+", indica que vai ser feito isso para
     * mais de 1 dígito.
     */

}

