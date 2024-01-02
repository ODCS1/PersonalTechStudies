package praticando.p010;

import java.util.Scanner;

public class P045 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // ---------------------------------------------------------------------------
        // DEFININDO AS VARIÁVEIS
        String res = "s";
        int numAleatorio = (int) Math.random() * 10 + 1;
        int tentativas = 2;
        String numUserString;
        int numUser;
        int isClose;
        int rodada = 1;
        // ---------------------------------------------------------------------------

        // ---------------------------------------------------------------------------
        // JOGANDO
        while (res.equals("s") || res.equals("sim")) {
            System.out.println("\t\t--------------------------------------");
            System.out.println("\t\t|               Advinha              |");
            System.out.println("\t\t--------------------------------------");
            System.out.println("\tOBJETIVO DO JOGO SERÁ ADVINHAR O VALOR INTEIRO DE 1 A 10.");
            System.out.printf("\n\t\t\t\t%d RODADA\n", rodada);
            
            do {
                System.out.printf("\nTENTATIVAS RESTANTES[%d]: ", tentativas);
                numUserString = input.nextLine();
                
                // VERIFICANDO SE DIGITOU UM VALOR INTEIRO
                if (numUserString.matches("\\d+")) {
                    numUser = Integer.parseInt(numUserString);
    
                    // VERIFICANDO SE numUser ESTÁ NO VALOR SOLICITADO
                    if (numUser > 0 && numUser < 11) {
    
                        // VERIFICANDO SE ACERTOU
                        if (numUser == numAleatorio) {
                            System.out.println("PARABÉNS, você acertou com %d tentativas sobrando!");
                            break;
                        } else {
                            tentativas--;
                            isClose = Math.abs(numAleatorio - numUser);
                            if (isClose == 1) {
                                System.out.println("Está Tostando!!!");
                            } else if (isClose == 2) {
                                System.out.println("Está morno!");
                            } else {
                                System.out.println("Está frio!");
                            }
                        }
    
                    } else {
                        System.out.println("[ERRO] Digite números dentro do intervalo informado!");
                        break;
                    }
                } else {
                    System.out.println("[ERRO] Digite números válidos!");
                    break;
                }
            } while (tentativas > 0);
            
            System.out.print("Quer jogar novamente[s/n]: ");
        }

        System.out.println("SAINDO...");
        // ---------------------------------------------------------------------------
    
        input.close();
    }
}
