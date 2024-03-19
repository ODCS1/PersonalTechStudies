package praticando.p013;

public class Programa {
    public static void main(String[] args) {
        Funcionario gerente = new Gerente("Zé Bento", "123.456.789-12");
        gerente.setSalario(9000);
        Funcionario vendendor = new Vendendor("Cebolinha", "987.654.321-84", 5700);

        System.out.println(gerente.calcularBonificacao());
        System.out.println(vendendor.calcularBonificacao());
    }
}
