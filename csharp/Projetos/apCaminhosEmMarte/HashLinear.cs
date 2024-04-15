using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace apCaminhosEmMarte
{
  public class HashLinear<Tipo> : ITabelaDeHash<Tipo>
    where Tipo : IRegistro<Tipo>
  {
    Tipo[] dados;
    const int TAM_MAXIMO = 131;
    int tamanho;
    

    public HashLinear()
    {
        tamanho = TAM_MAXIMO;
        dados = new Tipo[tamanho];
    }


    public int Hash(string chave)
    {
        long tot = 0;
        for (int i = 0; i < chave.Length; i++)
            tot += 37 * tot + (char)chave[i];

        tot = tot % tamanho;
        if (tot < 0)
            tot += tamanho;
        return (int)tot;
    }


    public List<Tipo> Conteudo()
    {
      List<Tipo> aux = new List<Tipo>();
      for (int i = 0; i < tamanho; i++)
        if (dados[i] != null)
            aux[i] = dados[i];

      return aux;
    }

    public bool Existe(Tipo item, out int onde)
    {
            onde = -1;
            for (int i = 0;i < tamanho; i++)
            {
                if (dados[i].Equals(item))
                    onde = i;
                    return true;
            }

            return false;


            // OU

            int pos = Hash(item.Chave);
            return dados[pos].Equals(item);
    }

        public void Inserir(Tipo item)
        {
            // TEM QUE VERIFICAR SE ESTÁ CHEIO


            int pos = Hash(item.Chave);
            while (true)
            {
                if (dados[pos] == null)
                {
                    dados[pos] = item;
                    break;
                }
                pos++;
            }
        }

        public bool Remover(Tipo item)
        {
            int onde = 0;
            if (!Existe(item, out onde))
                return false;

            dados[onde] = default(Tipo);
            return true;
        }
  }
}
