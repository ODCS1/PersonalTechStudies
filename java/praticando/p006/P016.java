package praticando.p006;
import java.util.Scanner;
// Praticando os laços de repetição

public class P016 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        // -----------------------------------------------------------
        // while - teste lógico no início
        int i = 1;
        while(i < 11) {
            System.out.println(i);
            i++;
        }
        // -----------------------------------------------------------
        // -----------------------------------------------------------
        // do while - teste lógico no final
        System.out.print("Você quer contar até quanto agora: ");
        int cont = input.nextInt();

        System.out.print("Começa em qual valor: ");
        int inicio = input.nextInt();

        do {
            System.out.print(inicio + " ");
            inicio++;
        } while (inicio <= cont);
        // -----------------------------------------------------------
        // -----------------------------------------------------------
        // for - loop para intervalos limitados
        for (int c = 0; c < 5; c++){
            System.out.println("\nUsando o for " + c);
        }

        input.close();

    }   
}
