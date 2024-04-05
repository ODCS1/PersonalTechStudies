package praticando.p015;

public class Exemplo {
    public interface Animal {
        void fazerSom();
    }
    
    public abstract class Mamifero implements Animal {
        abstract void mover();
    }
    
    public class Cachorro extends Mamifero {
        @Override
        public void fazerSom() {
            System.out.println("Latido de cachorro: Woof! Woof!");
        }
    
        @Override
        public void mover() {
            System.out.println("Cachorro se movendo...");
        }
    }
    
}
