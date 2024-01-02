package praticando.p011;

public class P054 {
    public static void main(String[] args) {
        escreveMensagem();

        int a = 3;
        int b = 2;

        
        int produto = multiplica(a,b);
        float quociente = divide(a,b);

        System.out.printf("Produto: %d \nQuociente: %d", produto, quociente);
    }

    static void escreveMensagem() {
        System.out.println("Olá, mundo!");
    }

    static int multiplica(int n1, int n2) {
        return n1 * n2;
    }

    static float divide(int n1, int n2) {
        return n1 / n2;
    }
}
