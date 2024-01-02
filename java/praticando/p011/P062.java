package praticando.p011;

import java.util.Scanner;

public class P062 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        final int NUM;
        System.out.print("Digite um valor inteiro: ");
        NUM = input.nextInt();
        
        System.out.println("NUM (int): " + NUM);
        input.close();


        final String NOME = "Juca";
        System.out.println("NOME (String): " + NOME);

        final double PI = 3.141592;
        System.out.println("PI (double): " + PI);
    }
}
