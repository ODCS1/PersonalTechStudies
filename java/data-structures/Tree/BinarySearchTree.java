// BST - BYNARI SEARCH TREE
// OS VALORES DOS NÓS NO LADO ESQUERDO SÃO MENORES QUE O NÓ RAIZ
// OS VALORES DOS NÓS DO LADO DIREITO SÃO MAIORES QUE O NÓ RAIZ


public class BinarySearchTree {
    Node root;

    // INSERT VALUE
    public void insert(int value){
        this.root = insertRec(root, value);
    }

    public Node insertRec(Node root, int newValue){
        if (root == null) {
            return new Node(newValue);
        }

        if (newValue < root.value) {
            root.left = insertRec(root.left, newValue);
        }else if (newValue > root.value) {
            root.right = insertRec(root.right, newValue);
        }

        return root;
    }

    // PERCORRER A ÁRVORE EM ORDEM (in-order)
    public void inOrderTraversal() {
        inOrderRec(root);
    }

    public void inOrderRec(Node root) {
        if (root != null) {
            inOrderRec(root.left);
            System.out.println(root.value + " ");
            inOrderRec(root.right);
        }
    }
}
