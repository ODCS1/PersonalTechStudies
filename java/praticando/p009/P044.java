package praticando.p009;

public class P044 {
    public static void main(String[] args) {
        // int vet[] = new int[3];
        // ____________________________________________________________
        // DEFININDO O VETOR
        String vet[] = new String[5];
        vet[0] = "D";
        vet[1] = "Abc";
        vet[2] = "abc";
        vet[3] = "Ebc";
        vet[4] = "Lbc";
        int n = vet.length;
        // ____________________________________________________________


        // ____________________________________________________________
        

        // ____________________________________________________________

        // ____________________________________________________________
        // STRING txtVet
        String txtVet = "[";
        for (int tx = 0; tx < n; tx++) {
            if (tx < n - 1) {
                txtVet += vet[tx] + ", ";
            } else {
                txtVet += vet[tx] + "]";
            }
        }
        // ____________________________________________________________


        // ____________________________________________________________
        // ORDENANDO O VETOR
        String aux = "";
        for (int i = 0; i < n - 1; i++) {
            for (int j = i + 1; j < n; j++) {
                if (vet[i] == vet[j]) {
                    aux = vet[i];
                }
            }
        }
        // ____________________________________________________________
    }
}
