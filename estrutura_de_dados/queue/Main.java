package queue;

import java.util.LinkedList;
import java.util.Queue;

// Queue/Fila = FIFO (FIRST IN FIRST OUT)

// enqueue (add elements) --> offer()
// dequeue (remove elements) --> poll()

public class Main {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<String>();
        queue.offer("Teste");
        queue.offer("Mais outro");
        queue.poll();

        System.out.println(queue);
    }
}
