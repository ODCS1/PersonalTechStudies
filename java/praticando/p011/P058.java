package praticando.p011;

public class P058 {
    public static void main(String[] args) {
        Car carro1 = new Car("Palio", "Fiat", 60, 110);
        // carro1.nome = "NovoNome";
        // Observe que a linha acima aparece um erro, pois os atributos estão encapsulados
        carro1.status();
        carro1.acelerar(1.5f, 10);
        carro1.status();
        carro1.frenagem(2f, 37);
        carro1.status();
        carro1.parada();
        carro1.status();
    }
}
