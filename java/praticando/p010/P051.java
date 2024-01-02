package praticando.p010;

import java.util.ArrayList;

public class P051 {
    public static void main(String[] args) {
        int count = 2;
        ArrayList<ArrayList<Integer>> valores = new ArrayList<> (count);


        valores.get(0).add(1);
        valores.get(0).add(3);
        valores.get(1).add(50);

        System.out.println(valores);
        
    }
}
