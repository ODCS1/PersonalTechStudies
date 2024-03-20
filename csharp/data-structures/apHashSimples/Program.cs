using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace apHashSimples
{
    class Program
    {
        static HashAprimorado tabela;
        static string[] algunsNomes = new string[] {"David", "Jennifer", "Donnie", "Mayo", "Raymond", "Bernica", "Mike", "Clayton", "Beata", "Michael", "Felipe", "Silvana", "Igor", "Lucia", "Guilherme", "Monica" ,"Amélia"};

        static void Main(string[] args)
        {
            int onde;
            string resultado;
            BackgroundColor = ConsoleColor.White;
            ForegroundColor = ConsoleColor.Black;

            Clear();
            WriteLine("Teste com tamanhos primo e não primo. Exemplo: 100, 131, 10007.");
            WriteLine($"Há {algunsNomes.Length} nomes no conjunto de testes.\nVocê pode digitar um valor menor que esse, forçando colisões.");

            Write("\nQual o número de posições da Tabela de Hash?");

            int tamanho = int.Parse(ReadLine());


            WriteLine("\
            n--------------------------------------------------------------");
            WriteLine("Teste com hash aprimorado, usando a regra de Horner no cálculo");

            tabela = new HashAprimorado(tamanho);
            for (int i = 0; i < algunsNomes.Length; i++)
                if ((resultado = tabela.Incluir(algunsNomes[i])) != "")
                    WriteLine(resultado);

            WriteLine("Conteúdo da tabela");
            foreach (string item in tabela.Conteudo())
                WriteLine(item);

            if (tabela.Existe("Amélia", out onde))
                WriteLine($"Achou Amélia na posição {onde}");
            else
                WriteLine($"Não achou Amélia mas deveria estar na posição {onde}");
            if (tabela.Existe("Raymond", out onde))
                WriteLine($"Achou Raymond na posição {onde}");
            else
                WriteLine($"Não achou Raymond mas deveria estar na posição {onde}");
                
            EsperarEnter();
        }

        static void EsperarEnter()
        {
            Write("\nPressione [Enter]");
            ReadLine();
        }
    }   
}