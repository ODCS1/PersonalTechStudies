public class Recursao {
    // 1
    public static boolean ehNegativo(int numero) {
        if (numero == 0)
            return false;
        return ehNegativo(numero, numero);
    }

    public static boolean ehNegativo(int a, int d) {
        if (a == 0)
            return true;
        if (d == 0)
            return false;
        return ehNegativo(++a, --d);
    }

    // 2
    public static int soma(int a, int b) {
        boolean aEhNegativo = ehNegativo(a);

        if (a == 0)
            return b;

        if (aEhNegativo) {
            return soma(++a, --b);
        }

        return soma(--a, ++b);
    }

    // 3
    public static int sub(int a, int b) {

        if (b == 0)
            return a;

        if (ehNegativo(b))
            return sub(++a, ++b);

        return sub(--a, --b);
    }

    // 4
    public static int modulo(int a) {

        if (ehNegativo(a))
            return soma(1, modulo(soma(1, a)));

        return a;
    }

    // 5
    public static int multi(int a, int b) {

        if (b == 0) {
            return 0;
        }

        if (ehNegativo(b)) {

            return sub(0, soma(a, multi(a, sub(modulo(b), 1))));
        }

        return soma(multi(a, sub(b, 1)), a);
    }

    // 6
    public static int poten(int a, int b) {
        if (ehNegativo(b)) {
            throw new IllegalArgumentException("O expoente não pode ser negativo!!!");
        }

        if (b == 0) {
            return 1;
        }

        return multi(poten(a, sub(b, 1)), a);

    }

    // 7
    public static int div(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("O divisor não pode ser 0!!!");
        }

        if (ehNegativo(sub(modulo(a), modulo(b)))) {
            return 0;
        }

        if (ehNegativo(a)) {
            if (ehNegativo(b)) {
                return soma(1, div(sub(a, b), b));
            }

            return sub(0, div(a, multi(b, -1)));
        }

        if (ehNegativo(b)) {
            return sub(0, div(a, multi(b, -1)));
        }

        return soma(1, div(sub(a, b), b));
    }

    // 8
    public static int resto(int a, int b) {
        if (b == 0) {
            throw new IllegalArgumentException("O divisor não pode ser 0!!!");
        }

        if (ehNegativo(sub(modulo(a), modulo(b)))) {
            return modulo(a);
        }

        return resto(sub(modulo(a), modulo(b)), modulo(b));
    }

    // 9
    public static boolean primeiroEhMenor(int a, int b) {
        if (a == 0) {
            if (b == 0) { return false; }
            
            return true;
        }

        if (b == 0) { return false; }

        
        // if (ehNegativo(b)){}
        
        return primeiroEhMenor(sub(a, 1), sub(b, 1));
    }

    
    // 10
    public static boolean primeiroEhMenorOuIgual(int a, int b) {

        return false;
    }

    // 11
    public static boolean primeiroEhMaior(int a, int b) {

        return false;
    }

    // 12
    public static boolean primeiroEhMaiorOuIgual(int a, int b) {

        return false;
    }

    // 13
    public static boolean primeiroEhDiferenteDoSegundo(int a, int b) {

        return false;
    }

    public static void main(String[] args) {
        // System.out.println("Exercício 1: " + ehNegativo(5));
        // System.out.println("Exercício 2: " + soma(7, 3));
        // System.out.println("Exercício 3: " + sub(-5, -3));
        // System.out.println("Exercício 4: " + modulo(5));
        // System.out.println("Exercício 5: " + multi(-2, -8));
        // System.out.println("Exercício 6: " + poten(-2, 3));
        // System.out.println("Exercício 7: " + div(10, 5));
        // System.out.println("Exercício 8: " + resto(17, -3));
        System.out.println("Exercício 9: " + primeiroEhMenor(4, 4));
    }
}
