package praticando.p011;

public class P055 {
    public static void main(String[] args) {
        int n1 = 12;
        int n2 = 3;
        int n3 = 1;
        float n4 = 2.3f;
        float n5 = 8.2f;

        soma(n1,n2);
        soma(n4,n5);
        soma(n1,n2,n3);

    }

    static void soma(int a, int b) {
        System.out.println(a+b);
    }

    static void soma(float a, float b) {
        System.out.println(a+b);
    }

    static void soma(int a, int b, int c) {
        System.out.println(a+b+c);
    }
}
