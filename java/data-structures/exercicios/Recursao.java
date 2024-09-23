public class Recursao {
   // 1
    public static boolean ehNegativo(int numero) {
        if (numero == 0)
            return false;
        return ehNegativo(numero, numero);
    }

    public static boolean ehNegativo(int a, int d) {
        if (a == 0) return true;
        if (d == 0) return false;
        return ehNegativo(++a, --d);
    }

    // 2
    public static int soma(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;
        return soma(++a, --b);
    }

    // 3
    public static int sub(int a, int b) {
        if (a == 0) return b;
        if (b == 0) return a;
        return sub(--a, --b);
    }

    // 4
    public static int modulo(int a) {
        if (a == 0) return 0;
        if (ehNegativo(a))
            return modulo(-a);
        return a;
    }

    // 5
    public static int multi(int a, int b) {
        if (b == 0) return 0;
        return a + multi(a, b - 1);
    }

    public static void main(String[] args) {
        System.out.println("Exc 1: " + ehNegativo(5));
        System.out.println("Exc 2: " + soma(5, 3));
        System.out.println("Exc 3: " + sub(10, 2));
        System.out.println("Exc 4: " + modulo(-5));
        System.out.println("Exc 5: " + multi(10, 2));
    } 
}
