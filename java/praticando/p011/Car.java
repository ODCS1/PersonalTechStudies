package praticando.p011;

public class Car {
    private String nome, marca;
    private float vel, velMax;

    public Car (String nome, String marca, float vel, float velMax) {
        this.nome = nome;
        this.marca = marca;
        this.vel = vel;
        this.velMax = velMax;
    }
    
    void status () {
        System.out.printf("\nNOME: %s \nMARCA: %s \nVELOCIDADE ATUAL: %.1f km/h \nVELOCIDADE MÁXIMA: %.1f km/h\n", this.nome, this.marca, this.vel,this.velMax);
    }

    void acelerar (float aceleracao, int tempo) {
        if (this.vel + (aceleracao * tempo) < this.velMax) {
            this.vel += (aceleracao * tempo);
            System.out.println("\nACELERANDO...");
        } else {
            this.vel = this.velMax;
        }
    }

    void frenagem (float desaceleracao, int tempo) {
        if (this.vel - (desaceleracao * tempo) > 0) {
            this.vel -= (desaceleracao * tempo);
            System.out.println("\nFREANDO...");
        } else {
            this.vel = 0;
        }
    }

    void parada () {
        this.vel = 0;
        System.out.println("\nCARRO PARADO!");
    }

    public String toString() {
        String velString = Float.toString(this.vel);
        return velString;
    }
}
