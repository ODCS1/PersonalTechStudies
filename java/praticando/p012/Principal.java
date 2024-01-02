package praticando.p012;

class Principal{
    public static void main(String[] args){
        Livro meuLivro = new Livro(1,"Java 20.4");
        Livro seuLivro = new Livro(2,"Java 20.4");

        if (meuLivro.equals("Java"))
                System.out.println("Iguais");
        else
              System.out.println("Diferentes");
    }
}