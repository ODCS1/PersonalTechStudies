package java.praticando.p015;

public class Pessoa {
    private String nome;
    private int idade;
    private float altura;
    private boolean comendo;

    public Pessoa(){
        this("", 0, 0.0f);
    }

    public Pessoa(String nome){
        this(nome, 0, 0.0f);
    }

    public Pessoa(String nome, int idade){
        this(nome, idade, 0.0f);
    }

    public Pessoa(String nome, int idade, float altura){
        this.nome = nome;
        this.idade = idade;
        this.altura = altura;
    }

    public void Andar(int passos){
        if(passos <= 0){
            System.out.println("Você está parado");
        }else {
            System.out.printf("Andando %d passos!!!", passos);
        }
    }

    public boolean Comer(){
        comendo = true;
        return comendo;
    }

    public boolean pararDeComer(){
        comendo = false;
        return comendo;
    }

    public String getNome(){
        return this.nome;
    }

    public boolean getComendo(){
        return this.comendo;
    }

    public float getAltura(){
        return this.altura;
    }

    public int getIdade(){
        return this.idade;
    }

    public void setIdade(int idade){
        this.idade = idade;
    }

    @Override
    public boolean equals(Object obj) {
        // TODO Auto-generated method stub
        return super.equals(obj);
    }


    @Override
    public String toString() {
        // TODO Auto-generated method stub
        return super.toString();
    
    }
}