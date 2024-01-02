package praticando.p010;

public class Animal {
    // Atributos
    String especie;
    String nome;
    String cor;
    boolean fome;

    // Métodos
    void alimentar () {
        this.fome = false;
    }

    void brincar () {
        this.fome = true;
    }

    void mostrarDados () {
        System.out.printf("Nome: %s \nEspécie: %s \nCor: %s \nFome: %b", this.nome, this.especie, this.cor, this.fome);
    }
}
