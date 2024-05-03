using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace apCaminhosEmMarte
{
  public class HashDuplo<Tipo> : ITabelaDeHash<Tipo>
    where Tipo : IRegistro<Tipo>
  {
        Tipo[] dados;
        int qtd_elementos;
        const int TAM_MAXIMO = 131;


        public HashDuplo()
        {
            dados = new Tipo[TAM_MAXIMO];
        }


        public int Hash(string chave)
        {

            // ESSE LOOP É PARA ENCONTRAR O VALOR DE HASH PARA UMA CHAVE JÁ ARMAZENADA
            for (int i = 0; i < dados.Length; i++)
            {
                if ((dados[i] != null) && (chave.Equals(dados[i].Chave))) { return i; }
            }

            // PARA CHAVES AINDA NÃO ARMAZENADAS
            long tot = 0;
            for (int i = 0; i < chave.Length; i++)
                tot += 37 * tot + (char)chave[i];

            tot = tot % dados.Length;
            if (tot < 0)
                tot += dados.Length;

            int primeiraPosicao = (int)tot;
            long posicaoAtual = (long)primeiraPosicao;
            int contadorColisao = 0;


            // NESSE PONTO PARA INSERÇÃO DE UM NOVO ELEMENTO JÁ ESTÁ GARANTIDO QUE EXISTE UMA POSIÇÃO VAGA
            while ((dados[(int)posicaoAtual] != null) && ((int)posicaoAtual != primeiraPosicao || contadorColisao == 0))
            {
                // AQUI NO CALCULO DA NOVA POSIÇÃO É BUSCADO DE FORMA DUPLA PELO NÚMERO DE COLISÕES
                posicaoAtual = (posicaoAtual * 2) % dados.Length;
                contadorColisao++;
            }

            return (int)posicaoAtual;
        }


        public List<Tipo> Conteudo()
        {
            List<Tipo> aux = new List<Tipo>();
            for (int i = 0; i < dados.Length; i++)
            {
                if (dados[i] != null)
                {
                    aux.Add(dados[i]);
                }
            }
            return aux;
        }

        public bool Existe(Tipo item, out int onde)
        {
            onde = Hash(item.Chave);
            return dados[onde].Equals(item);
        }

        public void Inserir(Tipo item)
        {
            if (!EstaCheio())
            {
                int pos = Hash(item.Chave);
                dados[pos] = item;
                qtd_elementos++;
            }
        }

        public bool EstaCheio()
        {

            if (qtd_elementos == TAM_MAXIMO) { return true; }
            return false;
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
