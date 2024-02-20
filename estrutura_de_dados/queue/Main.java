package queue;

import java.util.LinkedList;
import java.util.Queue;

// Queue/Fila = FIFO (FIRST IN FIRST OUT)
// A COLLECTION DESIGN FOR HOLDING ELEMENTS PRIOR TO PTOCESSING LINEAR DATA STRUCTURE

// enqueue (add elements) --> offer()
// dequeue (remove elements) --> poll()
// peek (see first element) --> peek()

// A INTERFACE QUEUE EXTENDE A INTERFACE "Collection", HERDANDO ASSIM AS PROPRIREDADES DEFINIDAS.

public class Main {
    public static void main(String[] args) {
        Queue<String> queue = new LinkedList<String>();

        System.out.println(queue.isEmpty());

        queue.offer("Teste");
        queue.offer("Mais outro");
        queue.offer("Terceiro");

        System.out.println(queue.peek());

        queue.poll();
        System.out.println("Tamanho da fila: " + queue.size());
        System.out.println("Tem Teste: " + queue.contains("Teste"));

        System.out.println(queue);
    }
}
