public class Main {
    public static void main(String[] args) {
        BinarySearchTree bst = new BinarySearchTree();

        // Inserindo valores
        bst.insert(50);
        bst.insert(30);
        bst.insert(70);
        bst.insert(20);
        bst.insert(40);
        bst.insert(60);
        bst.insert(80);

        // Percorrendo a árvore em ordem
        System.out.println("Árvore em ordem:");
        bst.inOrderTraversal(); // Saída: 20 30 40 50 60 70 80
    }
}
