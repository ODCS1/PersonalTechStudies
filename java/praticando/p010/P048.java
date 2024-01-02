package praticando.p010;

public class P048 {
    public static void main(String[] args) {
        // Intância
        Caneta c1 = new Caneta();

        // Atributos
        c1.marca = "bic";
        c1.carga = 70;
        c1.cor = "Azul";
        c1.tampado = true;
        c1.destampado = false;
        c1.ponta = 0.5f;

        // Métodos
        c1.destampar();
        c1.escrever();
        c1.mostraAtributo();
    }
}
