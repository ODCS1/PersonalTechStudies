using System;
using System.Collections.Generic;
using static System.Console;

namespace apBucketHash
{
  class Program
  {
    static void Main(string[] args)
    {
      BucketHash balde = new BucketHash();

      string[] algunsNomes = new string[]
      {
        "David", "Jennifer", "Donnie", "Mayo", "Raymond",
        "Bernica", "Mike", "Clayton", "Beata", "Michael",
        "Felipe","Silvana","Michael","Lucia", "Guilherme",
        "Monica", "Amélia"
      };

      BackgroundColor = ConsoleColor.Blue;
      ForegroundColor = ConsoleColor.Yellow;
      Clear();

      WriteLine("Inserindo chaves");

      // for i in range(0, len(algunsNomes), 1):    PYTHON
      //    balde.Inserir(algunsNomes[i])

      for (int i = 0; i < algunsNomes.Length; i++)
        balde.Inserir(algunsNomes[i]);

      // for umNone in algunsNomes:     PYTHON
      //    balde.Inserir(umNome)
      //foreach (string umNome in algunsNomes)    C#
      //  balde.Inserir(umNome);  

      Exibir(balde.Conteudo());
      EsperarEnter();

      if (balde.Remover("David"))
        WriteLine("Removeu: David");
      else
        WriteLine("Não achou: David");
      Exibir(balde.Conteudo());
      EsperarEnter();

      if (balde.Remover("Chico"))
        WriteLine("Removeu: Chico");
      else
        WriteLine("Não achou: Chico");
      Exibir(balde.Conteudo());

      if (balde.Remover("Raymond"))
        WriteLine("Removeu: Raymond");
      else
        WriteLine("Não achou: Raymond");
      Exibir(balde.Conteudo());
      EsperarEnter();
    }

    static void Exibir(List<string> lista)
    {
      foreach (string item in lista)
        WriteLine(item);
    }
    static void EsperarEnter()
    {
      Write("Pressione [Enter]:");
      ReadLine();
      WriteLine();
    }

  }
}
