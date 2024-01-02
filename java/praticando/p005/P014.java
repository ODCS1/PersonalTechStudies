package praticando.p005;

// Operador Unário (funcionamento igual no javascript)

public class P014 {
    public static void main(String[] args) {
        int num = 10;

        int n = 5 + num++;
        // Resultado de n é 15

        // int n2 = 5 + +num;
        // Resultado de n2 é 16

        int n2 = 5 + ++num;
        // Resultado de n2 é 17

        System.out.printf("num = %d \nn = %d \nn2 = %d", num, n, n2);
    }
}
