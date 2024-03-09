package praticando.p013;

public class Funcionario {
    private String cpf;
    private String nome;
    private double salario;

    public Funcionario(String cpf, String nome, double salario) {
        this.cpf = cpf;
        this.nome = nome;
        this.salario = salario;
    }

    public Funcionario(String cpf, String nome) {
        this.cpf = cpf;
        this.nome = nome;
    }

    public String getNome () {
        return this.nome;
    }

    public String getCpf() {
        return this.cpf;
    }

    public void setSalario(double salario){
        if (salario <= 0) {
            throw new IllegalArgumentException("O salário é inválido!");
        }
        this.salario = salario;
    }

    public double calcularBonificacao() {
        return this.salario * 0.10;
    }
}
