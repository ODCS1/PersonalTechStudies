package praticando.p011;

import java.util.Scanner;
import java.util.ArrayList;

public class P063 {
    public static void main(String[] args) {
        
    }

    public int[] getConcatenation(int[] nums) {
        ArrayList<Integer> numSum = new ArrayList<Integer>();
        Scanner input = new Scanner(System.in);
        
        int num;
        do {
            System.out.print("Digite o valor: ");
            num = input.nextInt();
            if (num == 0) {
                break;
            }
            numSum.add(num);
        } while (true);

        input.close();
        
        for (int i: numSum) {
            numSum.add(i);
        }
        int len  = numSum.size();
        int[] vet = new int[len];

        for (int i = 0; i < len; i++) {
            vet[i] = numSum.get(i);
        }
        
        return vet;
    }
}