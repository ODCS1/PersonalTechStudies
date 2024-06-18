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
using static System.Windows.Forms.VisualStyles.VisualStyleElement;

namespace apCaminhosEmMarte
{
    public partial class FrmCaminhos : Form
    {
        public FrmCaminhos()
        {
            InitializeComponent();

            dgvCaminhos.Columns.Add("CidadeOrigem", "Cidade Origem");
            dgvCaminhos.Columns.Add("CidadeDestino", "Cidade Destino");
            dgvCaminhos.Columns.Add("Distancia", "Distância");
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


            if (string.IsNullOrEmpty(dlgAbrir.FileName))
            {
                MessageBox.Show("[ERRO] Abra um arquivo antes de tentar remover uma cidade.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

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
            cbxOrigem.Items.Clear();
            cbxDestino.Items.Clear();


            if (!string.IsNullOrEmpty(dlgAbrir.FileName))
            {
                dlgAbrir.FileName = "";
            }
        }

        Cidade[] asCidades;
        int quantasCidades;   // tamanho lógico

        private void tpCaminhos_Enter(object sender, EventArgs e)
        {
            
            try
            {
                if ((cbxOrigem.Items.Count == 0) && (cbxDestino.Items.Count == 0))
                {
                    asCidades = new Cidade[25];
                    quantasCidades = 0;
                    // abrir o arquivo de cidades
                    var arquivo = new StreamReader(dlgAbrir.FileName);

                    // enquanto o arquivo de cidades não acabar
                    while (!arquivo.EndOfStream)
                    {
                        //    instancie um objeto da classe cidade
                        Cidade cidadeAtual = new Cidade();

                        //    faça esse objeto ler um registro de cidade
                        cidadeAtual.LerRegistro(arquivo);

                        //    adicione esse registro de cidade após a última posição usada do vetor de cidades
                        asCidades[quantasCidades] = cidadeAtual;


                        //    incremente quantasCidades
                        quantasCidades++;

                    }



                    // fechar o arquivo de cidades
                    arquivo.Close();

                    // ordenar o vetor de cidades pelo atributo nome
                    for (int i = 0; i < quantasCidades; i++)
                    {
                        for (int j = 0; j < quantasCidades - i - 1; j++)
                        {
                            if (string.Compare(asCidades[j].NomeCidade, asCidades[j + 1].NomeCidade) > 0)
                            {
                                Cidade aux = asCidades[j];
                                asCidades[j] = asCidades[j + 1];
                                asCidades[j + 1] = aux;
                            }
                        }
                    }


                    // copiar os nomes de cada cidades nos cbxOrigem e cbxDestino
                    for (int i = 0; i < quantasCidades; i++)
                    {
                        cbxOrigem.Items.Add(asCidades[i].NomeCidade);
                        cbxDestino.Items.Add(asCidades[i].NomeCidade);
                    }
                }
            }
            catch
            {
                MessageBox.Show("Abra um arquivo antes!", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                tabControl1.SelectedTab = tpCidades;
            }
        }

        private void cbxOrigem_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cbxDestino.SelectedItem != null)
            {
                string selectedItem = cbxOrigem.SelectedItem.ToString();
                string selectedItem2 = cbxDestino.SelectedItem.ToString();

                MessageBox.Show("Você selecionou: " + selectedItem);
                MessageBox.Show("Você selecionou(2): " + selectedItem2);
            }
            
        }

        private void cbxDestino_SelectedIndexChanged(object sender, EventArgs e)
        {
            if (cbxOrigem.SelectedItem != null)
            {
                string selectedItem = cbxOrigem.SelectedItem.ToString();
                string selectedItem2 = cbxDestino.SelectedItem.ToString();

                MessageBox.Show("Você selecionou: " + selectedItem);
                MessageBox.Show("Você selecionou(2): " + selectedItem2);
            }
        }

        private int[,] matrizAdjacente;
        private Dictionary<string, int> indiceCidades;
        private int numeroTotalCidades;

        private void CarregarArquivoDistancias(string caminhoArquivo)
        {
            try
            {
                using (StreamReader sr = new StreamReader(caminhoArquivo))
                {
                    indiceCidades = new Dictionary<string, int>();
                    numeroTotalCidades = 0;

                    while (!sr.EndOfStream)
                    {
                        string linha = sr.ReadLine();
                        if (linha != null)
                        {
                            string[] partes = linha.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                            if (partes.Length == 3)
                            {
                                string cidadeOrigem = partes[0];
                                string cidadeDestino = partes[1];

                                if (!indiceCidades.ContainsKey(cidadeOrigem))
                                {
                                    indiceCidades.Add(cidadeOrigem, numeroTotalCidades++);
                                }
                                if (!indiceCidades.ContainsKey(cidadeDestino))
                                {
                                    indiceCidades.Add(cidadeDestino, numeroTotalCidades++);
                                }
                            }
                        }
                    }

                    matrizAdjacente = new int[numeroTotalCidades, numeroTotalCidades];

                    sr.BaseStream.Seek(0, SeekOrigin.Begin);
                    while (!sr.EndOfStream)
                    {
                        string linha = sr.ReadLine();
                        if (linha != null)
                        {
                            string[] partes = linha.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                            if (partes.Length == 3)
                            {
                                string cidadeOrigem = partes[0];
                                string cidadeDestino = partes[1];
                                int distancia = int.Parse(partes[2]);

                                int indiceOrigem = indiceCidades[cidadeOrigem];
                                int indiceDestino = indiceCidades[cidadeDestino];

                                matrizAdjacente[indiceOrigem, indiceDestino] = distancia;
                                matrizAdjacente[indiceDestino, indiceOrigem] = distancia;
                            }
                        }
                    }
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Erro ao carregar o arquivo de distâncias: {ex.Message}", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        string caminhoArquivo;
        private void btnAbrirArquivoCaminhos_Click(object sender, EventArgs e)
        {
            if (dlgAbrirCaminhos.ShowDialog() == DialogResult.OK)
            {
                caminhoArquivo = dlgAbrirCaminhos.FileName;

                //CarregarArquivoDistancias(caminhoArquivo);

                dgvCaminhos.Rows.Clear();

                /*try
                {
                    using (StreamReader sr = new StreamReader(caminhoArquivo))
                    {
                        string linha;
                        while ((linha = sr.ReadLine()) != null)
                        {
                            string[] partes = linha.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                            if (partes.Length == 3)
                            {
                                dgvCaminhos.Rows.Add(partes[0], partes[1], partes[2]);
                            }
                        }

                        MessageBox.Show("Dados carregados com sucesso!", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
                    }
                }
                catch (Exception ex)
                {
                    MessageBox.Show($"Erro ao abrir o arquivo: {ex.Message}", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }*/
            }
        }



        //GrafoBacktracking grafo;
        private void btnMostrarCaminhos_Click(object sender, EventArgs e)
        {
            GrafoBacktracking grafo = new GrafoBacktracking(caminhoArquivo);
            
            if (dlgAbrirCaminhos != null)
            {
                GrafoBacktracking grafo = new GrafoBacktracking(caminhoArquivo, quantasCidades);
                

                if ((cbxOrigem.SelectedItem != null) && (cbxDestino.SelectedItem != null))
                {
                    string selectedItem = cbxOrigem.SelectedItem.ToString();
                    string selectedItem2 = cbxDestino.SelectedItem.ToString();

                    MessageBox.Show("Você selecionou: " + selectedItem);
                    MessageBox.Show("Você selecionou(2): " + selectedItem2);
                }
                else
                {
                    MessageBox.Show("Selecione as duas cidades! Para coseguir ver os caminhos.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                }
            }
            else
            {
                MessageBox.Show("Abra um arquivo de distâncias antes!", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void openFileDialogCaminhos_FileOk(object sender, CancelEventArgs e)
        {

        }

        private void btnIncluirCaminho_Click(object sender, EventArgs e)
        {
            string origem = cbxOrigem.Text.Trim();
            string destino = cbxDestino.Text.Trim();
            int distancia;

            if (string.IsNullOrEmpty(origem) || string.IsNullOrEmpty(destino))
            {
                MessageBox.Show("Insira uma cidade de origem e destino válidas para adicionar um caminho.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            if (!int.TryParse(udDistancia.Value.ToString(), out distancia) || distancia <= 0)
            {
                MessageBox.Show("Insira uma distância válida para o caminho.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                return;
            }

            dgvCaminhos.Rows.Add(origem, destino, distancia);

            MessageBox.Show($"Caminho adicionado com sucesso entre {origem} e {destino} com distância {distancia}.", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
        }

        /*private void AdicionarNoArquivoDistancias(string novaOrigem, string novoDestino, int novaDistancia)
        {
            try
            {
                string caminhoArquivo = dlgAbrirCaminhos.FileName;

                using (StreamWriter writer = File.AppendText(caminhoArquivo))
                {
                    string linhaFormatada = $"{novaOrigem.PadRight(15)}{novoDestino.PadRight(16)}{novaDistancia}";
                    writer.WriteLine(linhaFormatada);
                }
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Erro ao adicionar ao arquivo de distâncias: {ex.Message}", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }*/

        private void btnExcluirCaminho_Click(object sender, EventArgs e)
        {
            if (dgvCaminhos.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dgvCaminhos.SelectedRows[0];
                string origem = selectedRow.Cells["CidadeOrigem"].Value.ToString();
                string destino = selectedRow.Cells["CidadeDestino"].Value.ToString();
                int distancia = Convert.ToInt32(selectedRow.Cells["Distancia"].Value);

                dgvCaminhos.Rows.Remove(selectedRow);

                MessageBox.Show($"Caminho entre {origem} e {destino} com distância {distancia} removido com sucesso.", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Selecione um caminho na lista para remoção.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        /*private void RemoverDoArquivoDistancias(string origem, string destino, int distancia)
        {
            try
            {
                string caminhoArquivo = dlgAbrirCaminhos.FileName;
                string[] linhas = File.ReadAllLines(caminhoArquivo);

                List<string> novasLinhas = new List<string>();
                foreach (string linha in linhas)
                {
                    string[] partes = linha.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                    if (partes.Length == 3 && partes[0] == origem && partes[1] == destino && int.Parse(partes[2]) == distancia)
                    {
                        continue;
                    }
                    novasLinhas.Add(linha);
                }

                File.WriteAllLines(caminhoArquivo, novasLinhas);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Erro ao remover do arquivo de distâncias: {ex.Message}", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }*/

        private void btnAlterarCaminho_Click(object sender, EventArgs e)
        {
            if (dgvCaminhos.SelectedRows.Count > 0)
            {
                DataGridViewRow selectedRow = dgvCaminhos.SelectedRows[0];
                string origemAntiga = selectedRow.Cells["CidadeOrigem"].Value.ToString();
                string destinoAntigo = selectedRow.Cells["CidadeDestino"].Value.ToString();
                int distanciaAntiga = Convert.ToInt32(selectedRow.Cells["Distancia"].Value);

                string novaOrigem = cbxOrigem.Text.Trim();
                string novoDestino = cbxDestino.Text.Trim();
                int novaDistancia;

                if (string.IsNullOrEmpty(novaOrigem) || string.IsNullOrEmpty(novoDestino))
                {
                    MessageBox.Show("Insira uma cidade de origem e destino válidas para alterar um caminho.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                if (!int.TryParse(udDistancia.Value.ToString(), out novaDistancia) || novaDistancia <= 0)
                {
                    MessageBox.Show("Insira uma distância válida para o caminho.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
                    return;
                }

                selectedRow.Cells["CidadeOrigem"].Value = novaOrigem;
                selectedRow.Cells["CidadeDestino"].Value = novoDestino;
                selectedRow.Cells["Distancia"].Value = novaDistancia;

                MessageBox.Show($"Caminho entre {origemAntiga} e {destinoAntigo} com distância {distanciaAntiga} alterado para {novaOrigem}, {novoDestino}, {novaDistancia}.", "Sucesso", MessageBoxButtons.OK, MessageBoxIcon.Information);
            }
            else
            {
                MessageBox.Show("Selecione um caminho na lista para alteração.", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }

        private void dgvMelhorCaminho_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }

        /*private void AtualizarArquivoDistancias(string origemAntiga, string destinoAntigo, int distanciaAntiga, string novaOrigem, string novoDestino, int novaDistancia)
        {
            try
            {
                string caminhoArquivo = dlgAbrirCaminhos.FileName;
                string[] linhas = File.ReadAllLines(caminhoArquivo);

                List<string> novasLinhas = new List<string>();
                foreach (string linha in linhas)
                {
                    string[] partes = linha.Split(new char[] { ' ', '\t' }, StringSplitOptions.RemoveEmptyEntries);
                    if (partes.Length == 3 && partes[0] == origemAntiga && partes[1] == destinoAntigo && int.Parse(partes[2]) == distanciaAntiga)
                    {
                        novasLinhas.Add($"{novaOrigem.PadRight(15)}{novoDestino.PadRight(15)}{novaDistancia}");
                    }
                    else
                    {
                        novasLinhas.Add(linha);
                    }
                }

                File.WriteAllLines(caminhoArquivo, novasLinhas);
            }
            catch (Exception ex)
            {
                MessageBox.Show($"Erro ao atualizar o arquivo de distâncias: {ex.Message}", "Erro", MessageBoxButtons.OK, MessageBoxIcon.Error);
            }
        }*/
    }
}
