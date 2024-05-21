using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace apFilaVetor
{
  public partial class FrmFilaVetor : Form
  {
    public FrmFilaVetor()
    {
      InitializeComponent();
    }

    FilaVetor<string> aFila;

    private void FrmFilaVetor_Load(object sender, EventArgs e)
    {
      aFila = new FilaVetor<string>(10);
    }

    private void btnEnfileirar_Click(object sender, EventArgs e)
    {
      aFila.Enfileirar(txtNome.Text);
      Exibir();
    }

    private void Exibir()
    {
      lsbFila.Items.Clear();
      var dadosDaFila = aFila.Conteudo();

      foreach (string umNome in dadosDaFila)
        lsbFila.Items.Add(umNome);
    }

    private void btnRetirar_Click(object sender, EventArgs e)
    {
      var umNome = aFila.Retirar();
      txtNome.Text = umNome;
      Exibir();
    }
  }
}
