package praticando.p007;

import java.util.Scanner;
public class P027 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        int n = 1;
        while (true){
            System.out.print("Digite [s/n]: ");
            String resposta = input.nextLine().toLowerCase();

            if (resposta.equals("s")) {
                System.out.println(n + "° resposta");
                n++;
                continue;
            }else {
                System.out.print("SAINDO...");
                break;
            }
        }
        input.close();
    }
}
