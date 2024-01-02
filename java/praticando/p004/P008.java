package praticando.p004;

public class P008 {
    public static void main(String[] args) {
        byte numPequeno = 127;
        int inteiro = 10;
        float num = 12.4f;
        double numMaior = 24.8;
        char letra = 'L';
        String nome = "Nome";

        System.out.println(String.format("byte: %d \nint: %d \nfloat: %f \ndouble: %f \nchar: %s \nString: %s", numPequeno,inteiro, num, numMaior, letra, nome));
    }
}
