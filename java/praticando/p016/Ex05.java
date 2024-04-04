package praticando.p016;


//  Escreva um programa em Java que embaralhe um arranjo A de n inteiros

public class Ex05 {
    public static void main(String[] args) {
        int[] arr = {1,3,5,7,9,5,2};
        embaralhar(arr);

        for (int i = 0; i < arr.length; i++){
            System.out.print(arr[i] + " ");
        }
    }
    
    public static int[] embaralhar(int[] a){

        int pos_aleatoria, aux;

        for (int i = 0; i < a.length; i++) {
            pos_aleatoria = (int) (Math.random() * (a.length));

            aux = a[pos_aleatoria];
            a[pos_aleatoria] = a[i];
            a[i] = aux;
        }

        return a;
    }
}
