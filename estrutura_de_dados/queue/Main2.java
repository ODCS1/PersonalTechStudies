import java.util.LinkedList;
import java.util.Queue;

//package queue;

public class Main2 {
    public static void main(String[] args) {
        Queue<String> fila = new LinkedList<String>();

        fila.offer("Elemento1");
        fila.offer("Elemento2");
        fila.offer("elemento3");
        fila.poll();

        System.out.println(fila);
        System.out.println(fila.peek());
    }
}
