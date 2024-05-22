using System;
using System.Collections;
using System.Collections.Generic;

namespace apBucketHash
{
  class BucketHash
  {
    private const int SIZE = 131; // para gerar mais colisões; o ideal é primo > 100

    ArrayList[] dados;

    public BucketHash()
    {
      dados = new ArrayList[SIZE];
      for (int i = 0; i < SIZE; i++)
      {
        // coloca em cada posição do vetor, um arrayList vazio
        dados[i] = new ArrayList(1);
      }
    }

    public int Hash(string chave)
    {
      long tot = 0;
      for (int i = 0; i < chave.Length; i++)
        tot += 37 * tot + (char)chave[i];

      tot = tot % dados.Length;
      if (tot < 0)
        tot += dados.Length;
      return (int)tot;
    }

    public void Inserir(string item)
    {
      int valorDeHash = Hash(item);
      if (!dados[valorDeHash].Contains(item))
        dados[valorDeHash].Add(item);
    }

    public bool Remover(string item)
    {
      int onde = 0;
      if (!Existe(item, out onde))
         return false;

      dados[onde].Remove(item);
      return true;
    }

    public bool Existe(string chave, out int posicao)
    {
      posicao = Hash(chave);
      return dados[posicao].Contains(chave);
    }

    public List<string> Conteudo()
    {
      List<string> saida = new List<string>();
      for (int i = 0; i < dados.Length; i++)
        if (dados[i].Count > 0)
        {
          string linha = $"{i,5} : ";
          foreach (string chave in dados[i])
            linha += " | " + chave;
          saida.Add(linha);
        }
      return saida;
    }
  }
}
