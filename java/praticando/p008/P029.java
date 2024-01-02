package praticando.p008;
import java.util.Scanner;

public class P029 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
         
        String resposta;
        int n = 1;
        do {
            System.out.print("Quer continuar [s/n]: ");
            resposta = input.nextLine();
            System.out.println(n + "° resposta");
            n++;
        } while (resposta.equals("s"));

        System.out.print("SAINDO...");

        input.close();

    }
}
