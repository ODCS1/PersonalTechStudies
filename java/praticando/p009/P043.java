package praticando.p009;

// Bubble Sort

public class P043 {
    public static void main(String[] args) {

        // ____________________________________________________________
        // DEFININDO O VETOR
        int vet[] = new int[5];
        vet[0] = 4;
        vet[1] = 12;
        vet[2] = 14;
        vet[3] = 44;
        vet[4] = 8;

        int n = vet.length;
        // ____________________________________________________________


        // ____________________________________________________________
        // MOSTRANDO O VETOR ORIGINAL COM A STRING txtVetor
        String txtVetor = "[";
        for (int ind = 0; ind < n; ind++) {
            if (ind < n - 1) {
                txtVetor += vet[ind] + ", ";
            } else {
                txtVetor += vet[ind] + "]";
            }
        }
        System.out.println("Vetor Original: " + txtVetor);
        // ____________________________________________________________


        // ____________________________________________________________
        // ORDENANDO
        int aux;
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (vet[i] > vet[j]) {
                    aux = vet[i];
                    vet[i] = vet[j];
                    vet[j] = aux;
                }
            }
        }
        // ____________________________________________________________


        // ____________________________________________________________
        // TXT DO VETOR ORDENADO
        String txtVetorOrdenado = "[";
        for (int indice = 0; indice < n; indice++) {
            if (indice < n - 1) {
                txtVetorOrdenado += vet[indice] + ", ";
            } else {
                txtVetorOrdenado += vet[indice] + "]";
            }
        }
        // ____________________________________________________________

        System.out.print("Vetor ordenado: " + txtVetorOrdenado);
    }
}
