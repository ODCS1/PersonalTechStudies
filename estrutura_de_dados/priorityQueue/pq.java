package priorityQueue;

import java.util.Queue;
import java.util.Collections;
import java.util.PriorityQueue;

public class pq {
    public static void main(String args[]) {
        Queue<String> nomes = new PriorityQueue<>(Collections.reverseOrder());

        nomes.offer("Castro");
        nomes.offer("Reginaldo");
        nomes.offer("Ana");


        for (int i = 0; i <= nomes.size(); i++) {
            System.out.println(nomes.poll());
        }
    
    }
}