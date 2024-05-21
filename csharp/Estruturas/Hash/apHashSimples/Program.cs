using System;
using static System.Console;

namespace apHashSimples
{
  class Program
  {
    // atributos da classe Program
    static HashAprimorado tabela1;
    static string[] algunsNomes = new string[]
                {"David",   "Jennifer", "Donnie",  "Mayo",  "Raymond",
                 "Bernica", "Mike",     "Clayton", "Beata", "Michael",
                 "Felipe",  "Silvana",  "Igor",    "Lucia", "Guilherme",
                 "Monica",  "Amélia"};

    static void Main(string[] args)
    {
      int onde;
      string resultado;

      ForegroundColor = ConsoleColor.Black;
      BackgroundColor = ConsoleColor.White;
      Clear();

      WriteLine("Teste com tamanhos primo e não primo. Exemplo: 100, 131, 10007.");
      WriteLine($"Há {algunsNomes.Length} nomes no conjunto de testes.\nVocê pode " +
           "digitar um valor menor que esse, forçando colisões.");
      Write("\nQual o número de posições da Tabela de Hash?");
      int tamanho = int.Parse(ReadLine());

      tabela1 = new HashAprimorado(tamanho);

      WriteLine("\n-------------------------------------------------------------");
      WriteLine("Teste com hash inicial, sem uso da regra de Horner no cálculo");

      // for i in range(0,len(algunsNomes), 1)
      for (int i = 0; i < algunsNomes.Length; i++)
      {
        resultado = tabela1.Incluir(algunsNomes[i]);

        if (resultado != "")  // houve uma colisão no método Incluir()
           WriteLine(resultado);
      }

      WriteLine("Conteúdo da tabela");
      foreach (string item in tabela1.Conteudo())
        WriteLine(item);
      EsperarEnter();

      if (tabela1.Existe("Amélia", out onde))
        WriteLine($"Achou Amélia na posição {onde}");
      else
        WriteLine($"Não achou Amélia mas deveria estar na posição {onde}");

      if (tabela1.Existe("Raymond", out onde))
        WriteLine($"Achou Raymond na posição {onde}");
      else
        WriteLine($"Não achou Raymond mas deveria estar na posição {onde}");
      EsperarEnter();

      void EsperarEnter()
      {
        Write("\nPressione [Enter]");
        ReadLine();
      }
    }
  }
}
