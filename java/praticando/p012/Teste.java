package praticando.p012;

public class Teste {
    public static void main(String[] args) {
        MinhaThread thread1 = new MinhaThread("Thread1", 1000);
        MinhaThread thread2 = new MinhaThread("Thread2", 500);
        MinhaThread thread3 = new MinhaThread("Thread3", 1200);
    }
}
