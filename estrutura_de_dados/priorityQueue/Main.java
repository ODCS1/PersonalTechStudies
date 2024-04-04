import java.util.PriorityQueue;
import java.util.Queue;

public class Main {
    public static void main(String[] args) {
        Queue<Integer> pq = new PriorityQueue<>();

        pq.offer(1);
        pq.offer(0);
        pq.offer(15);
        pq.offer(10);

        System.out.println(pq);
    }
}
