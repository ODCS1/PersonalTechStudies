using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace apCaminhosEmMarte
{
  internal class Cidade : IRegistro<Cidade>
  {
    string nomeCidade;
    double x, y;

    public string Chave => nomeCidade;

    public void GravarDados(StreamWriter arquivo)
    {
      throw new NotImplementedException();
    }

    public void LerRegistro(StreamReader arquivo)
    {
      throw new NotImplementedException();
    }
  }
}
