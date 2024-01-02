package praticando.p011;

public class P056 {
    public static void main(String[] args) {
        String nome = "Carlos";
        String sobrenome = "Silva";

        mensagem(nome);

        System.out.println(mensagem(nome, sobrenome));
    }

    static void mensagem(String nome){
        System.out.println(nome + " é legal.");
    }

    static String mensagem(String nome, String sobrenome) {
        return nome + " " + sobrenome + " é legal.";
    }
}
