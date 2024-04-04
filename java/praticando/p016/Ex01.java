package praticando.p016;

public class Ex01 {
    public static void main(String[] args) {
        int vet[] = {83, 41, 5, 1, 59, 97};
        int n = 2;

        int[] res = funcao(vet, n);

        for(int i = 0; i < res.length; i++){
            System.out.print(res[i] + " ");
        }
    }

    public static int[] funcao(int[] A, int i) {
        A[1] = 17;
        A[i / 2] = 9;
        A[2 * i- 1] = 95;
        A[i- 1] = A[5] / 2;
        A[3] = A[i];
        A[i + 1] = A[i] + A[i- 1];
        A[A[2]- 2] = 78;
        A[A[i]- 1] = A[1] * A[i] / 5;
        A[A[2] % 2 + 2] = A[i + 6 / 2]- A[i- 1 * 2];
        return A;
    }
}
