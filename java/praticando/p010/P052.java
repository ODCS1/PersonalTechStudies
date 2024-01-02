package praticando.p010;

import java.util.ArrayList;

public class P052 {
    public static void main(String[] args) {
        // ArrayList 2d
        ArrayList<ArrayList<String>> mercado = new ArrayList<>();

        // ArrayList 1
        ArrayList<String> doces = new ArrayList<String>();
        doces.add("Chocolate");
        doces.add("Goiabada");
        doces.add("Pudim");

        // ArrayList 2
        ArrayList<String> bebidas = new ArrayList<String>();
        bebidas.add("Água");
        bebidas.add("Suco");
        bebidas.add("Refrigerante");

        // ArrayList 3
        ArrayList<String> alimentos = new ArrayList<String>();
        alimentos.add("Pão");
        alimentos.add("Manteiga");
        alimentos.add("Arroz");

        // Adicionando os elementos
        mercado.add(0, doces);
        mercado.add(1, bebidas);
        mercado.add(2, alimentos);

        System.out.println(mercado);

        String elemento1 = mercado.get(0).get(0);
        String elemento2 = mercado.get(1).get(2);
        String juncao = elemento1 + " e " + elemento2;

        System.out.printf("\nElemento [0][0]: %s \nElemento [1][2]: %s\n", elemento1, elemento2);
        System.out.printf("Junção: %s", juncao);
    }
}
