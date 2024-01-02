package praticando.p010;

public class P050 {
    public static void main(String[] args) {
        // Instância
        Animal a1 = new Animal();
        
        // Atributos
        a1.especie = "Cachorro";
        a1.cor = "Castanho claro";
        a1.nome = "Caramelo";
        a1.fome = false;

        // Métodos
        a1.alimentar();
        a1.brincar();
        a1.mostrarDados();
    }
}
