using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace apCaminhosEmMarte
{
    internal interface ITabelaDeHash<Tipo>
    {
        void Inserir(Tipo chave);
        bool Remover(Tipo chave);
        bool Existe(Tipo chave, out int onde);
        List<Tipo> Conteudo();
    }
}