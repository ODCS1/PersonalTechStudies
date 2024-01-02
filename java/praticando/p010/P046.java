package praticando.p010;

public class P046 {
    public static void main(String[] args) {
        float notas[] = new float[4];

        notas[0] = 7.2f;
        notas[1] = 4.9f;
        notas[2] = 8.0f;
        notas[3] = 9.2f;
        // Agora o vetor já possuí todas as 4 posições preenchidas.

        for (float nota: notas) {
            System.out.println(nota);
        }

        // Agora tentando adicionar mais um elemento em uma posição não definida
        notas[4] = 5.2f;
    }
}
