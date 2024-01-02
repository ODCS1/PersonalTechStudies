package praticando.p012;

public class MinhaThread extends Thread {
    private String nome;
    private int tempo;

    public MinhaThread (String prenome, int tempo) {
        this.nome = prenome;
        this.tempo = tempo;
        start();
    }


    public void run () {
        try {
            for (int i = 0; i < 4; i++) {
                System.out.println(this.nome + " contador " + i);
                Thread.sleep(this.tempo);
            }
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
        System.out.println(this.nome + " terminou a execução!");
    }

    public String getNome () {
        return this.nome;
    }
}