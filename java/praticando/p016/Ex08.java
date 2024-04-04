package praticando.p016;

public class Ex08 {
    public static void main(String[] args) {
        int[] arr = {5,2,-5,7,-1,6};

        int[] arr2 = ordernar(arr);

        for (int i : arr2) {
            System.out.println(i);
        }
    }

    private static int[] ordernar(int[] a){
        int aux = 0;
        for (int i = 0; i < a.length - 1; i++){
            for (int j = i+1; j < a.length; j++){
                if (a[i] > a[j]) {
                    aux = a[i];
                    a[i] = a[j];
                    a[j] = aux;
                }
            }
        }
        
        return a;
    }
}
