package praticando.p016;
import java.util.HashMap;

public class Ex07 {
    public static void main(String[] args) {
        String[] lista = {"asd", "qwe", "qwe", "uio", "jkl","asd", "bnm"};

        containDuplicate(lista);


        for (String string : lista) {
            System.out.print(string + " ");
        }

    }

    private static void containDuplicate(String[] names){
        HashMap<Integer, String> map = new HashMap<>();
        int namesLen = names.length;
        for(int i = 0; i < namesLen; i++){
            if (map.containsValue(names[i])){
                names = removerElemento(names, names[i]);
            }else{
                map.put(i, names[i]);
            }

        }
    }

    private static String[] removerElemento(String[] n, String elemento){
        String[] vetorNovo = new String[n.length - 1];


        for (int i = 0; i < vetorNovo.length; i++){
            if (!n[i].equals(elemento)){
                vetorNovo[i] = n[i];
            }
        }
        return vetorNovo;
    }
}
