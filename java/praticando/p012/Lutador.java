package praticando.p012;

public class Lutador implements iLutador {
    private String nome, nacionalidade, categoria;
    private int idade, vitorias, derrotas, empates;
    private float altura, peso;

    public Lutador (String nome, String nacionalidade, int idade, int vitorias, int derrotas, int empates, float altura, float peso) {
        setNome(nome);
        setNacionalidade(nacionalidade);
        setIdade(idade);
        setVitorias(vitorias);
        setDerrotas(derrotas);
        setEmpates(empates);
        setAltura(altura);
        setPeso(peso);
    }

    public void apresentar() {
        System.out.printf("E AGORA na categoria %s IREMOS VER EM AÇÃO O ATLETA %s, TEM %d ANOS DE IDADE, NASCEU EM %s E QUE POSSUI UM CARTEL DE %d VITÓRIAS, %d DERROTAS e %d EMPATES.\n", this.categoria, this.nome, this.idade, this.nacionalidade, this.vitorias, this.derrotas, this.empates);
    }

    public void status() {
        System.out.printf("Nome: %s \nVitórias: %d \nDerrotas: %d \nEmpates: %d \n", this.nome, this.vitorias, this.derrotas, this.empates);
    }

    public void ganharLuta() {
        setVitorias(this.vitorias + 1);
    }

    public void perderLuta() {
        setDerrotas(this.derrotas + 1);
    }

    public void empatarLuta() {
        setEmpates(this.empates + 1);
    }

    public String getNome() {
        return nome;
    }

    public String getNacionalidade() {
        return nacionalidade;
    }

    public String getCategoria() {
        return categoria;
    }

    public int getIdade() {
        return idade;
    }

    public int getVitorias() {
        return vitorias;
    }

    public int getDerrotas() {
        return derrotas;
    }

    public int getEmpates() {
        return empates;
    }

    public float getAltura() {
        return altura;
    }

    public float getPeso() {
        return peso;
    }

    public void setNome(String nome) {
        this.nome = nome;
    }

    public void setNacionalidade(String nacionalidade) {
        this.nacionalidade = nacionalidade;
    }

    private void setCategoria() {
        if (this.peso < 70) {
            this.categoria = "Leve";
        }else if (this.peso < 90) {
            this.categoria = "Médio";
        }else {
            this.categoria = "Pesado";
        }
    }

    public void setIdade(int idade) {
        this.idade = idade;
    }

    public void setVitorias(int vitorias) {
        this.vitorias = vitorias;
    }

    public void setDerrotas(int derrotas) {
        this.derrotas = derrotas;
    }

    public void setEmpates(int empates) {
        this.empates = empates;
    }

    public void setAltura(float altura) {
        this.altura = altura;
    }

    public void setPeso(float peso) {
        this.peso = peso;
        this.setCategoria();
    }
    
}