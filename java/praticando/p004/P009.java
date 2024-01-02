package praticando.p004;
import java.util.Scanner;

public class P009 {
    public static void main(String[] args) {
        Scanner teclado = new Scanner(System.in);


        float nota = 7.68f;
        String nome = "Nome";

        // Formatando saída de dados
        System.out.printf("O aluno %s, tirou %.2f na prova. \n", nome, nota);


        // Outra forma
        System.out.format("O aluno %s, tirou %.2f na prova. \n", nome, nota);

        // Mais uma forma
        System.out.println(String.format("O aluno %s, tirou %.2f na prova.", nome, nota));

        // Trabalhando com entrada de dados
        

        System.out.print("Nome da professora: ");
        String nomeProfessora = teclado.nextLine();
        System.out.print("Idade da professora: ");
        int idadeProfessora = teclado.nextInt();
        System.out.print("Cr da aula: ");
        float crAula = teclado.nextFloat();

        teclado.close();


        System.out.printf("Nome Professora: %s %nIdade Professora: %d %nCr Aula: %.2f", nomeProfessora, idadeProfessora, crAula);

    }
}
