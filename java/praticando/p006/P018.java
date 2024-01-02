package praticando.p006;

import java.util.Scanner;

public class P018 {
	public static void main(String[] args) {

		// Criando o objeto de entrada de dados
		Scanner input = new Scanner(System.in);

		// Valor para n1
		System.out.print("Digite o 1° número: ");
		int n1 = input.nextInt();

		// Valor para n2
		System.out.print("Digite o 2° número: ");
		int n2 = input.nextInt();

		// teste_lógico ? caso_verdadeiro : caso_falso
	    String nome = n1 > n2  ? "sim" : "não";
		System.out.print(nome);

		// Fechando o objeto Scanner
		input.close();
	}
}


