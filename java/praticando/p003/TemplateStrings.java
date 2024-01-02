package praticando.p003;

public class TemplateStrings {
    public static void main(String[] args) {
        String nome = "Teste";
        int idade = 25;
        double altura = 1.75;

        // Primeira forma
        String mensagem = String.format("Olá, meu nome é %s. Tenho %d anos e minha altura é %.2f metros.", nome, idade, altura);
        System.out.println(mensagem);

        // Segunda Forma
        System.out.println(String.format("Nome: %s \nIdade é %d!", nome, idade));

    }
}
