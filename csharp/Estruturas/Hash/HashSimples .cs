using Microsoft.Win32;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class HashSimples
{
    const int tamanhoPadrao = 10007;
    string[] tabelaDeHash;

    public HashSimples(int tamanhoDesejado)
    {
        tabelaDeHash = new string[tamanhoDesejado];
    }

    public HashSimples() : this(tamanhoPadrao) { }

    // retorna índice da tabelaDeHash
    //private int Hash(string chave)   cálculo de hash simples
    //{
    //    int tot = 0;
    //    // for i in range(0, chave.Lenth, 1):
    //    for (int i = 0; i < chave.Length; i++)
    //        tot += (int)chave[i];
    //    return tot % tabelaDeHash.Length;
    //}

  private int HashAprimorado(string chave)
  {
    long tot = 0;
    // for i in range(0, chave.Lenth, 1):
    for (int i = 0; i < chave.Length; i++)
      tot += 37 * tot + (int)chave[i];
    tot = tot % tabelaDeHash.Length;
    if (tot < 0)
      tot += tabelaDeHash.Length;

    return (int) tot;
  }

    public string Incluir(string chave)
    {
        string saida = "";
        int valorDeHash = HashAprimorado(chave.Trim());   // posicao calculada para um registro
        
        if (tabelaDeHash[valorDeHash] != null)         // já há dado armazenado nessa posição
             saida = $"colisao na posicao {valorDeHash} entre " +
                     $"{tabelaDeHash[valorDeHash]} e {chave}";

        tabelaDeHash[valorDeHash] = chave;
        return saida;
    }
    public bool Existe(string s, out int posicao)
    {
        posicao = HashAprimorado(s);
        return tabelaDeHash[posicao] == s;
    }
    public List<string> Conteudo()
    {
        var saida = new List<string>();
        for (int i = 0; i < tabelaDeHash.Length; i++)
            if (tabelaDeHash[i] != null)
                saida.Add($"{i,5} : {tabelaDeHash[i]}");
        //else
        // saida.Add($"{i} ");
        return saida;
    }
    public void Limpar()
    {
        for (int i = 0; i < tabelaDeHash.Length; i++)
            tabelaDeHash[i] = null;
    }
  }


