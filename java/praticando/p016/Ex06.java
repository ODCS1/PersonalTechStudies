package praticando.p016;
import java.util.HashMap;

public class Ex06 {
    public static void main(String[] args) {
        int[] arr = {3,4,5,1};
        int k = 9;
        int[] values = sumTwoNumber(arr, k);


        for (int i = 0; i < values.length; i++){
            System.out.print(values[i] + " ");
        }
    }

    private static int[] sumTwoNumber(int[] a, int k){
        HashMap<Integer, Integer> map = new HashMap<>();
        int[] numbers = new int[2];
        for (int i = 0; i < a.length; i++){
            int diff = k - a[i];
            if (map.containsValue(diff)){
                numbers[0] = diff;
                numbers[1] = a[i];
                break;
            }

            map.put(i, a[i]);
        }
        return numbers;
    }
}
