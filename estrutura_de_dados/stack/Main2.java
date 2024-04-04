package stack;

import java.util.Stack;

public class Main2 {
    public static void main(String[] args) {
        Stack<String> nomes = new Stack<String>();

        nomes.push("Melancia");
        nomes.push("Limão");
        nomes.push("Maça");
        nomes.push("Uva");

        nomes.pop();
        System.out.println(nomes.get(nomes.size()-1));
        System.out.println(nomes.peek());
        System.out.println(nomes.search("Limão"));
    }
}