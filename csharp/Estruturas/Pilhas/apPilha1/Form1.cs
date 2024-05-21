using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace apPilha1
{
  public partial class FrmPilhas : Form
  {
    public FrmPilhas()
    {
      InitializeComponent();
    }
    void Exibir(PilhaVetor<char> pilha)
    {
      List<char> aPilha = pilha.Conteudo();
      dgvPilha.Rows.Clear();
      dgvPilha.RowCount = 2;
      dgvPilha.ColumnCount = pilha.Tamanho;

      for (int j = 0; j < pilha.Tamanho; j++)
      {
        dgvPilha.Columns[j].HeaderText = j.ToString();
        dgvPilha[j, 0].Value = aPilha[j];
        dgvPilha.Columns[j].Width = 30;
        Thread.Sleep(300);
        Application.DoEvents();
      }
    }

    private void btnAnalisar_Click(object sender, EventArgs e)
    {
      if (txtExpressao.Text == "")
        MessageBox.Show("Digite uma expressão com {[()]}!");
      else
      {
        var aPilha = new PilhaVetor<char>(txtExpressao.Text.Length);
        var dados = txtExpressao.Text;
        bool estaBalanceada = true;  // supomos ser balanceada
        for (int indice=0; indice < dados.Length && estaBalanceada; 
                 indice++) 
        {
          txtExpressao.SelectionStart = indice;
          txtExpressao.SelectionLength = 1;

          Thread.Sleep(300);
          Application.DoEvents();

          if (dados[indice] == '{' || dados[indice] == '(' ||
              dados[indice] == '[')
             aPilha.Empilhar(dados[indice]);
          else
          {
            char abertura = aPilha.Desempilhar();
            char fechamento = dados[indice];
            if (
                (abertura == '{' && fechamento != '}') ||
                (abertura == '[' && fechamento != ']') ||
                (abertura == '(' && fechamento != ')')
              )
              estaBalanceada = false;
          }
          Exibir(aPilha);
        }
        if (!aPilha.EstaVazia)
          estaBalanceada = false;

        chkBalanceada.Checked = estaBalanceada;

      }
    }

    private void txtExpressao_Enter(object sender, EventArgs e)
    {
      chkBalanceada.Checked = false;
    }
  }
}
