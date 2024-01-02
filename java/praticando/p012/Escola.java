package praticando.p012;

public class Escola {
    private int qtd_alunos;
    private int qtd_turmas;


    public Escola () {
        this(0, 0);
    }

    public Escola ( int qtd_alunos) {
        this(qtd_alunos, 1);
    }

    public Escola (int qtd_alunos, int qtd_turmas) {
        this.qtd_alunos = qtd_alunos;
        this.qtd_turmas = qtd_turmas;
    }

    public int getQtdAlunos () {
        return this.qtd_alunos;
    }

    public int getQtdTurmas () {
        return this.qtd_turmas;
    }

    public void setQtdAlunos (int novaQtdAlunos) {
        this.qtd_alunos = novaQtdAlunos;
    }

    public void setQtdTurmas (int novaQtdTurmas) {
        this.qtd_turmas = novaQtdTurmas;
    }
}
