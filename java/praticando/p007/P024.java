package praticando.p007;
import java.util.Scanner;
public class P024 {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);
        System.out.print("Digite a idade: ");
        int idade = input.nextInt();
        if (idade < 7) {
            System.out.printf("Com %d anos, está na infância.", idade);
        }else if (idade < 10) {
            System.out.printf("Com %d anos, está na segunda infância.", idade);
        }else if (idade < 15) {
            System.out.printf("Com %d anos, está na pré-adolescência.", idade);
        }else if (idade < 20) {
            System.out.printf("Com %d anos, está na adolescência.", idade);
        }else if (idade < 30) {
            System.out.printf("Com %d anos, está na juventude.", idade);
        }else if (idade < 60) {
            System.out.printf("Com %d anos, está na vida adulta.", idade);
        }else{
            System.out.printf("Com %d anos, está na velhice.", idade);
        }
        input.close();
    }
}
