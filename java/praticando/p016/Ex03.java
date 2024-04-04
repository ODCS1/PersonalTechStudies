package praticando.p016;

public class Ex03 {
    public static void main(String[] args) {
        int n[] = {3, 1, 4, 7, 2, 10, 5};
        int n_ordenado[] = ordena(n);

        for (int i : n_ordenado) {
            System.out.print(i + " ");
        }
    }

    public static int[] ordena(int[] A) {
        int i, j, chave;
        for (i = 1; i < A.length; i++)
        {
            chave = A[i];
            j = i- 1;
            while (j >= 0 && A[j] < chave) {
                A[j + 1] = A[j];
                j = j- 1;
            }
            A[j + 1] = chave;
        }
        return A;
    }
}
