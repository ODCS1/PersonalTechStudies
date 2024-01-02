package praticando.p010;

public class P047 {
    public static void main(String[] args) {
        // INICIALIZAÇÃO
        String[][] vagasGaragem = new String[2][2];

        // ATRIBUIÇÃO DE VALORES
        vagasGaragem[0][0] = "Vaga 1";
        vagasGaragem[0][1] = "Vaga 2";
        vagasGaragem[1][0] = "Vaga 3";
        vagasGaragem[1][1] = "Vaga 4";

        // OUTPUT
        for (int linha = 0; linha < vagasGaragem.length; linha++) {
            for (int coluna = 0; coluna < vagasGaragem[linha].length; coluna++) {
                System.out.println(vagasGaragem[linha][coluna]);
            }
        }
    }
}
