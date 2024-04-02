package praticando.p016;

public class Ex10 {
    private static int interpolationSearch(int[] arr, int x) {
        int low = 0;
        int high = arr.length - 1;

        while (low <= high && x >= arr[low] && x <= arr[high]) {
            // FUNÇÃO PARA CALCULAR A POSIÇÃO ATUAL POR INTERPOLAÇÃO
            int pos = low + (((high - low) / (arr[high] - arr[low])) * (x - arr[low]));
            // (high - low) É A FAIXA DA QUANTIDADE DE VALORES

            // (arr[high] - arr[low]) É A DIFERENÇA ENTRE O ELEMENTO MÁXIMO E MÍNIMO

            // ((high - low) / (arr[high] - arr[low])) ESSA EXPRESSÃO (QUANTIDADE DE ELEMENTOS) / (VALOR MÉDIO)
            // MOSTRA VALORES ENTRE O E 1 PARA ONDE PODE ESTAR O VALOR BUSCADO.

            // (x - arr[low]) CALCULA A DIFERENÇA ENTRE O VALOR BUSCADO E O VALOR MÍNINO, SABENDO O QUÃO DISTANTE ESTÁ DO ELEMENTO NA POSIÇÃO 0.

            // (((high - low) / (arr[high] - arr[low])) * (x - arr[low]))  COM ESSE PRODUTO DÁ PRA TER UMA IDEIA ONDE O ELEMNTO PODE ESTAR NA FAIXA DE VALORES

            // low + (((high - low) / (arr[high] - arr[low])) * (x - arr[low])) AGORA É ADICIONADO O LOW PARA REMOVER OS ELEMENTOS ANTERIORES QUE FORAM DESCARTADOS

            if (arr[pos] == x) {
                return pos;
            } else if (arr[pos] < x) {
                low = pos + 1;
            } else {
                high = pos - 1;
            }
        }
        
        return -1;
    }

    public static void main(String[] args) {
        int[] arr = {10, 20, 30, 40, 50, 60, 70, 80, 90, 100};
        int x = 50;
        int index = interpolationSearch(arr, x);
        if (index != -1) {
            System.out.println("Elemento encontrado na posição: " + index);
        } else {
            System.out.println("Elemento não encontrado.");
        }
    }
}