package praticando.p001;
public class Pratica {
    public static void main(String[] args) {
        int i = 1;
        while (i <= 10) {
            System.out.println("Hello, World! " + i);

            if (i % 2 == 0) {
                System.out.println("PAR! " + i);
            }
            i++ ;
        }
    }
}