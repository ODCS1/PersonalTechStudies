package hashTable;
import java.util.Hashtable;

/*
 * HashTable is a data structure that stores
 * unique keys to values
 * 
 * Each key/value pair is known as an
 * Entry FAST insertion, look up, deletion
 * of key/value pairs not ideal for small
 * data sets, great with large data sets
 */

/*
 * HASHING = Takes a key and computes an integer
 * (formula will vary based on key & data type)
 * in a HashTable, we use tje hash % capacity to calculate an index number
 * 
 * key.hashCode() % capacity = index
 */


/*
 * BUCKET = An indexed storage location
 * for one or more Entries can store
 * multiple Entries in case of a collision
 * (Linked similarly a LinkedList)
 */

/*
 * COLLISION = Hash function generates the same index
 * for more than one key less collision
 *  = more efficiency
 */

/*
 * RunTime complexity
 * 
 * Best Case: O(1)
 * Worst Case O(n)
 */

public class Main {
    public static void main(String[] args) {
        Hashtable<Integer, String> tb = new Hashtable<>(10);


        // tb.put(0, "Primeiro");

        for (int i = 11; i < 1000; i += 126) {
            tb.put(i, "Valor " + Integer.toString(i));
            // System.out.println(i);
        }

        tb.remove(9);

        for (Integer key : tb.keySet()){
            System.out.println(key.hashCode() % 10 + "\t" + key + "\t" + tb.get(key));
        }
 
        // tb.put(10, "Valor");

        // System.out.println(tb.get(10));
    }
}