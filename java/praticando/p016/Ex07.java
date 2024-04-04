package praticando.p016;
import java.util.HashMap;

public class Ex07 {
    public static void main(String[] args) {
        String[] lista = {"asd", "qwe", "qwe", "uio", "jkl","asd", "bnm"};
        
        System.out.println();
        System.out.println();

        String[] listaSemRepeticao = new String[lista.length];

        listaSemRepeticao = containDuplicate(lista);

        System.out.print("Lista com as repetições removidas: ");
        for (String string : listaSemRepeticao) {
            System.out.print(string + " ");
        }
        System.out.println();
        System.out.println();

        System.out.print("Lista Original: ");
        for (String string : lista) {
            System.out.print(string + " ");
        }
        System.out.println();
        System.out.println();
        

    }

    private static String[] containDuplicate(String[] names){
        HashMap<Integer, String> map = new HashMap<>();
        for(int i = 0; i < names.length; i++){
            if (map.containsValue(names[i])){
                names = removerElemento(names, i);
                i--;
            }else{
                map.put(i, names[i]);
            }

        }
        return names;
    }

    private static String[] removerElemento(String[] n,int posElemRepetido){

        String[] vetorNovo = new String[n.length - 1];

        for (int i = 0; i < vetorNovo.length; i++){
            if (i < posElemRepetido){
                vetorNovo[i] = n[i];
            }else if(i >= posElemRepetido) {
                vetorNovo[i] = n[i+1];
            }
        }

        return vetorNovo;
    }
}
