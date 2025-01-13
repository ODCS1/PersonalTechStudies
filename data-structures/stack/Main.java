package stack;

import java.util.Stack;

// Stack ou pilha é a estrutura LIFO (Last in first out)

// Adicona os elementos no topo de uma uma pilha vertival

// push() adiciona ao top
// pop() remove do top


public class Main {
    public static void main(String[] args) {
        Stack<String> stack = new Stack<String>();

        stack.push("Laranja");
        stack.push("Melancia");
        stack.push("Melão");

        String fruta = stack.pop();

        stack.push(fruta);

        System.out.println(stack.get(stack.size() - 1));

        System.out.println(stack.search("Melão"));
        System.out.println(stack);
        System.out.println(stack.peek());
        System.out.println(stack.isEmpty());
    }
}