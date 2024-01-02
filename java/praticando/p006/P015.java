package praticando.p006;
import java.util.Scanner;
public class P015{
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        System.out.print("Digite a sua idade: ");
        int idade = input.nextInt();

        if (idade < 16){
            System.out.printf("A sua idade é %d, portando você não pode votar!");
        } else if ((idade < 18) || (idade > 70)) {
            System.out.printf("A sua idade é %d, portando você pode votar!");
        } else{
            System.out.printf("A sua idade é %d, portando você é obrigado a votar!");
        }


        input.close();
    }
}