package praticando.p008;

public class P035 {
    public static void main(String[] args) {
        String[][] matriz = {
            {"A", "B", "C"},
            {"D", "E", "F"},
            {"G", "H", "I"},
        };
        
        // OUTPUT DOS DADOS
        for (int linha = 0; linha < matriz.length; linha++) {
            for (int coluna = 0; coluna < matriz[linha].length; coluna++) {
                System.out.println(matriz[linha][coluna]);
            }
        }
    }
}
