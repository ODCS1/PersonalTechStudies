using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace apCaminhosEmMarte
{
    public partial class FrmCaminhos : Form
    {
        public FrmCaminhos()
        {
            InitializeComponent();
        }

        ITabelaDeHash<Cidade> tabela;

        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {

        }

        private void btnLerArquivo_Click(object sender, EventArgs e)
        {
            if (dlgAbrir.ShowDialog() == DialogResult.OK)
            {
                if (rbBucketHash.Checked)
                    tabela = new BucketHash<Cidade>();
                else
                  if (rbHashLinear.Checked)
                    tabela = new HashLinear<Cidade>();
                else
                    if (rbHashQuadratico.Checked)
                    tabela = new HashQuadratico<Cidade>();
                else
                      if (rbHashDuplo.Checked)
                    tabela = new HashDuplo<Cidade>();

                var arquivo = new StreamReader(dlgAbrir.FileName);
                while (!arquivo.EndOfStream)
                {
                    Cidade umaCidade = new Cidade();
                    umaCidade.LerRegistro(arquivo);
                    tabela.Inserir(umaCidade);
                }
                lsbCidades.Items.Clear();  // limpa o listBox
                var asCidades = tabela.Conteudo();
                foreach (Cidade cid in asCidades)
                    lsbCidades.Items.Add(cid);
                arquivo.Close();
            }
        }

        private void FrmCaminhos_FormClosing(object sender, FormClosingEventArgs e)
        {
            // abrir o arquivo para saida, se houver um arquivo selecionado
            // obter todo o conteúdo da tabela de hash
            // percorrer o conteúdo da tabela de hash, acessando
            // cada cidade individualmente e usar esse objeto Cidade
            // para gravar seus próprios dados no arquivo
            // fechar o arquivo ao final do percurso
        }

        private void btnInserir_Click(object sender, EventArgs e)
        {
            string nome = txtCidade.Text.Trim();
            double x, y;

            if (string.IsNullOrEmpty(dlgAbrir.FileName))
            {
                MessageBox.Show("Por favor, abra um arquivo antes de inserir uma cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (string.IsNullOrEmpty(nome))
            {
                MessageBox.Show("Por favor, insira um nome válido para a cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }


            if (!double.TryParse(udX.Value.ToString(), out x) || !double.TryParse(udY.Value.ToString(), out y))
            {
                MessageBox.Show("Por favor, insira coordenadas válidas para a cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            Cidade novaCidade = new Cidade();
            novaCidade.NomeCidade = nome;
            novaCidade.X = x;
            novaCidade.Y = y;

            using (StreamWriter writer = File.AppendText(dlgAbrir.FileName))
            {
                //writer.WriteLine($"{nome}, {x}, {y}");
                int n = 16 - nome.Length;
                String espaco = "";
                for (int i = 1; i < n; i++)
                {
                    espaco += " ";
                }

                // A CIDADE JÁ É COLOCADA AQUI NO ARQUIVO, PARA CASO O USUÁRIO QUEIRA ABRIR O MESMO ARQUIVO EM OUTRA TÉCNICA DE HASH
                // APARECENDO A CIDADE INSERIDA NA TÉCNICA ANTERIOR DE HASH
                writer.WriteLine($"{nome}{espaco}{x}{y}");
            }

            tabela.Inserir(novaCidade);

            LimparCampos();
            AtualizarCidade();
        }


        private void LimparCampos()
        {
            txtCidade.Text = "";
            udX.Value = 0;
            udY.Value = 0;
        }

        private void AtualizarCidade()
        {
            lsbCidades.Items.Clear();
            var cidades = tabela.Conteudo();
            foreach (Cidade cidade in cidades)
            {
                lsbCidades.Items.Add(cidade);
            }
        }

        private void btnBuscar_Click(object sender, EventArgs e)
        {
            string nomeCidade = txtCidade.Text.Trim();

            if (string.IsNullOrEmpty(dlgAbrir.FileName))
            {
                MessageBox.Show("Por favor, abra um arquivo antes de pesquisar uma cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            List<Cidade> cidades = tabela.Conteudo();

            bool encontrada = false;

            foreach (Cidade cidade in cidades)
            {
                string nomeCidadeFormatado = cidade.NomeCidade.Trim();

                if (nomeCidade.Equals(nomeCidadeFormatado, StringComparison.OrdinalIgnoreCase))
                {
                    encontrada = true;

                    MessageBox.Show("Cidade localizada.", "Sucesso na busca", MessageBoxButtons.OK, MessageBoxIcon.Information);

                    txtCidade.Text = cidade.NomeCidade;
                    udX.Value = (decimal)cidade.X;
                    udY.Value = (decimal)cidade.Y;
                    break;
                }
            }

            if (!encontrada)
            {
                MessageBox.Show("Cidade não localizada.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnRemover_Click(object sender, EventArgs e)
        {
            string nomeCidade = txtCidade.Text.Trim();

            if (tabela == null)
            {
                MessageBox.Show("A tabela não foi inicializada corretamente.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            bool encontrada = false;
            foreach (Cidade cidade in tabela.Conteudo())
            {
                string nomeCidadeFormatado = cidade.NomeCidade.Trim();
                if (nomeCidade.Equals(nomeCidadeFormatado, StringComparison.OrdinalIgnoreCase))
                {
                    encontrada = true;
                    if (tabela.Remover(cidade))
                    {
                        string arquivo = dlgAbrir.FileName;
                        string[] linhas = File.ReadAllLines(arquivo);

                        List<String> lista = new List<String>();
                        foreach (string line in linhas)
                        {
                            if (!line.Contains(nomeCidade))
                            {
                                lista.Add(line);
                            }
                        }
                        File.WriteAllLines(arquivo, lista);

                        MessageBox.Show("Cidade removida com sucesso.", "Sucesso na Remoção", MessageBoxButtons.OK, MessageBoxIcon.Information);
                        LimparCampos();
                        AtualizarCidade();
                    }
                    else
                    {
                        MessageBox.Show("Erro ao remover a cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    }
                    break;
                }
            }
            if (!encontrada)
            {
                MessageBox.Show("Cidade não encontrada na tabela de hash.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void btnListar_Click(object sender, EventArgs e)
        {
            LimparCampos();
            lsbCidades.Items.Clear();
        }
    }
}
