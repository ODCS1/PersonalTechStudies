package praticando.p013;

public class Gerente extends Funcionario{
        private int numeroDeFuncionariosGerenciados = 0;
        private Funcionario funci;

        public Gerente (String nome, String cpf, double salario) {
            super(nome,cpf, salario);
        }

        public Gerente (String cpf, String nome){
            super(nome, cpf);
        }

        public Gerente(String nome, String cpf, int numeroDeFuncionariosGerenciados) {
            super(nome, cpf, numeroDeFuncionariosGerenciados);

            if (numeroDeFuncionariosGerenciados == 0) {
                throw new IllegalArgumentException("O número de funcionários não pode ser zero!");
            }
            this.numeroDeFuncionariosGerenciados = numeroDeFuncionariosGerenciados;
        }

        @Override
        public double calcularBonificacao() {
            return 0.0;
        }


        public int getNumeroDeFuncionariosGerenciados(){
            return this.numeroDeFuncionariosGerenciados;
        }

}
