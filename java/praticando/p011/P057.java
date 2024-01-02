package praticando.p011;

import java.util.ArrayList;

public class P057 {
    public static void main(String[] args) {
        ArrayList<Integer> lista =  new ArrayList<Integer>();


        lista.add(2);
        lista.add(395);
        lista.add(46);


        int valor = 2;
        lista.remove(Integer.valueOf(valor)); //Remove o elemento pelo valor
        for (int i: lista) {
            System.out.println(i);
        }
    }
}
