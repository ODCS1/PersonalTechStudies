package praticando.p010;

public class Caneta {
    // Definindo os atributos
    String cor;
    String marca;
    boolean tampado;
    boolean destampado;
    float ponta;
    int carga;

    // Métodos
    void status() {
        if (this.carga > 0 && this.destampado) {
            System.out.println("A caneta está pronta para ser usada.");
        } else if (this.carga > 0) {
            System.out.println("A caneta possuí carga, para utilizá-la, tire a tampa.");
        } else {
            System.out.println("Caneta sem carga.");
        }
    }

    void tampar () {
        this.tampado = true;
        this.destampado = false;
    }

    void destampar () {
        this.tampado = false;
        this.destampado = true;
    }

    void escrever () {
        if (this.destampado == true) {
            System.out.println("ESCREVENDO...");
        } else {
            System.out.println("Destampe a caneta para escrever.");
        }
        
    }

    void mostraAtributo () {
        System.out.printf("Cor: %s \nMarca: %s \nTampado: %b \nPonta: %f \nCarga: %d", this.cor, this.marca, this.tampado, this.ponta, this.carga);
    }
}
