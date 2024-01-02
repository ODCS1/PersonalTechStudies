package praticando.p009;

import java.util.ArrayList;
public class P042 {
    public static void main(String[] args) {
        ArrayList<Integer> lista =  new ArrayList<Integer>();

        lista.add(2);
        lista.add(395);
        lista.add(46);

        int valor = 2;
        lista.remove(Integer.valueOf(valor)); //Remove o valor pelo índice
        for (int i: lista) {
            System.out.println(i);
        }
    }    
}

