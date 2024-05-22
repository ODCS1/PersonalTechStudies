using Newtonsoft.Json.Linq;
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace WinFormGetAPI
{
    public partial class FormGetAPI : Form
    {
        public FormGetAPI()
        {
            InitializeComponent();
        }

        private void btnClose_Click(object sender, EventArgs e)
        {
            this.Close();
        }

        private void btnRequest_Click(object sender, EventArgs e)
        {

            // Criar o RestClient
            RestClient restClient = new RestClient();

            // Setar o endPoint dele psrs a URI desejada

            restClient.endPoint = "https://opencep.com/v1/13020060";

            // Fazer a chamada do método que executa o request
            var end = restClient.makeRequest();

            // atualizar a tela com a resposta do usuário

            string txtResponse = end.ToString();
            string cep = "";
            string logradouro = "";
            string complemento = "";
            string bairro = "";
            string cidade = "";
            string uf = "";
            string ibge = "";

            /*MessageBox.Show(txtResponse.Length.ToString());*/

            //DE MANEIRA ESTÁTICA

            /*for (int i = 0; i < txtResponse.Length; i++)
                if ((i > 11) && (i < 21))
                {
                    cep += txtResponse[i];
                }else if ((i > 40) && (i < 60))
                {
                    logradouro += txtResponse[i];
                }else if ((i > 80) && (i < 92))
                {
                    complemento += txtResponse[i];
                }
                else if ((i > 107) && (i < 116))
                {
                    bairro += txtResponse[i];
                }
                else if ((i > 135) && (i < 144))
                {
                    cidade += txtResponse[i];
                }
                else if ((i > 155) && (i < 158))
                {
                    uf += txtResponse[i];
                }
                else if ((i > 171) && (i < 179))
                {
                    ibge += txtResponse[i];
                }*/

            // DE MANEIRA DINÂMICA
            JObject jsOb = JObject.Parse(end);
            cep = (string)jsOb["cep"];
            logradouro = (string)jsOb["logradouro"];
            bairro = (string)jsOb["bairro"];
            cidade = (string)jsOb["localidade"];
            uf = (string)jsOb["uf"];
            complemento = (string)jsOb["complemento"];
            ibge = (string)jsOb["ibge"];


            txtBoxCep.Text = cep;
            txtBoxBairro.Text = bairro;
            txtBoxCidade.Text = cidade;
            txtBoxComplemento.Text = complemento;
            txtBoxUf.Text = uf;
            txtBoxIbge.Text = ibge;
            txtBoxLogradouro.Text = logradouro;
        }
    }
}
