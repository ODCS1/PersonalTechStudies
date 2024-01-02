package praticando.p005;

import java.util.Scanner;

public class P012 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite uma valor: ");
        int valor = input.nextInt();

        float raiz = (float) Math.sqrt(valor);
        int elevado = (int) Math.pow(valor, 2);

        System.out.printf("A raíz quadrada de %d, é %.2f.", valor, raiz);

        System.out.printf("\nE %d ao quadrado é %d.", valor, elevado);
        input.close();
    }
}
