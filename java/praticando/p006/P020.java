package praticando.p006;

public class P020 {
    public static void main(String[] args) {
        // maior, menor e valor absoluto.
        double n1 = 3.1415;
        double n2 = -2;
        double maior = Math.max(n1, n2);
        double menor = Math.min(n1, n2);
        double valorAbsoluto = Math.abs(n2);
        System.out.printf("O maior número: %.4f \nO menor número: %.1f \nO valor absoluto: %.1f\n", maior, menor, valorAbsoluto);

        // raíz quadrada e exponenciação
        int num = 100;
        double raiz = Math.sqrt(num);
        double elevado = Math.pow(num, 2);
        System.out.printf("A raíz quadrada de %d é %.1f e 100 elevado a 2 é %.0f.", num, raiz, elevado);
    }
}
