package hashTable;

import java.util.Hashtable;

public class Main {
    public static void main(String[] args) {
        Hashtable<Integer, String> tb = new Hashtable<>(2);


        // tb.put(0, "Primeiro");

        for (int i = 0; i < 10; i++) {
            tb.put(i, "Valor " + Integer.toString(i));
            // System.out.println(i);
        }
 
        tb.put(10, "Valor");

        System.out.println(tb);
    }
}