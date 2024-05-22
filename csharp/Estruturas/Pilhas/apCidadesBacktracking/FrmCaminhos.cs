using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace apCidadesBacktracking
{
  public partial class FrmCaminhos : Form
  {
    GrafoBacktracking oGrafo;

    public FrmCaminhos()
    {
      InitializeComponent();
    }

    private void label4_Click(object sender, EventArgs e)
    {

    }

    private void btnAbrirArquivo_Click(object sender, EventArgs e)
    {
      if (dlgAbrir.ShowDialog() == DialogResult.OK)
      {
        oGrafo = new GrafoBacktracking(dlgAbrir.FileName);
        if (oGrafo.TipoGrafo == 'l')
          rbLigacao.Checked = true;
        else
          rbDistancia.Checked = true;
        oGrafo.Exibir(dgvGrafo);
      }
    }

    private void btnBuscar_Click(object sender, EventArgs e)
    {
      int origem = int.Parse(txtOrigem.Text);
      int destino = int.Parse(txtDestino.Text);
      var pilhaCaminho = oGrafo.BuscarCaminho(origem, destino, 
                          lsbMovimentos, dgvGrafo, dgvPilha);
      if (pilhaCaminho.EstaVazia)
        MessageBox.Show("Não achou caminho");
      else
      {
        MessageBox.Show("Achou caminho");
        //pilhaCaminho.Exibir(dgvPilha);
        lsbMovimentos.Items.Add("");
        lsbMovimentos.Items.Add("Caminho encontrado");
        while (!pilhaCaminho.EstaVazia)
        {
          var mov = pilhaCaminho.Desempilhar();
          lsbMovimentos.Items.Add($"De {mov.Origem} para {mov.Destino}");
        }
      }
    }
  }
}
