package praticando.p016;

public class Ex04 {

    private static int busca1(int[] A, int k) {
        for (int i = 0; i < A.length; i++) {
            if (A[i] == k) {
                return i;
            }
        }
        return-1;
    }

    private static int busca2(int[] A, int k) {
        int inicio = 0, fim = A.length;
        while (inicio < fim) {
            int meio = (inicio + fim) / 2;
            if (A[meio] == k) {
                return meio;
            }
            if (A[meio] < k) {
                inicio = meio + 1;
            }
            else {
                fim = meio- 1;
            }
        }
        return-1;
    }
    public static void main(String[] args) {
        int[] A = {1, 3, 5, 7, 9, 11, 13, 15, 17, 19};
        int valor1 = busca1(A, 13);
        int valor2 = busca2(A, 13);
        System.out.println(valor1 + "- " + valor2);

        // RETORNA 6- 6 , pois as duas buscas retornam a posição quando é encontrado o valor alvo.
        
        // Não, a busca 1 pensando em performace, é mais lenta que a busca 2, pois para encontrar um valor alvo, é necessário percorrer diversos outros valores até chegar no valor de interresse.
    }
}
