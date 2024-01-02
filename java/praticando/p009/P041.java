package praticando.p009;

import java.util.ArrayList;

public class P041 {
    public static void main(String[] args) {
        ArrayList<String> bebidas = new ArrayList<String>();

        bebidas.add("água");
        bebidas.add("refrigerante");
        bebidas.add("suco");
        bebidas.add("chá");

        int tamanhoVetor = bebidas.size();
        String bebida1 = bebidas.get(2);
        String bebidaRemovida = bebidas.remove(0);

        System.out.printf("Tamanho do vetor: %d \nBebida escolhida: %s \nBebida removida: %s\n\n",  tamanhoVetor, bebida1, bebidaRemovida);

        // for-each loop
        for (String bebida: bebidas) {
            System.out.print(bebida + " ");
        }

    }
}
