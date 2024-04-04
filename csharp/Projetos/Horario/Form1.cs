using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Windows.Forms;

namespace Horario
{
    public partial class Formulario : Form
    {
        Hora hora = new Hora();
        public Formulario()
        {
            InitializeComponent();
        }

        private void lblHoras_Click(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void Formulario_Load(object sender, EventArgs e)
        {

        }

        private void btn_addUmMinuto_Click(object sender, EventArgs e)
        {
            hora.AddUmMinuto(1);
            //hora.Minutos += 1;
            lblHoras.Text = hora.ToString();
        }

        private void btnAdicionarUmSegundo_Click(object sender, EventArgs e)
        {
            hora.AddUmSegundo(1);
            //hora.Segundos += 1;
            lblHoras.Text = hora.ToString();
        }

        private void btnDiminuirUmMinuto_Click(object sender, EventArgs e)
        {
            hora.RemoverUmMinuto(1);
            //hora.Minutos -= 1;
            lblHoras.Text = hora.ToString();
        }

        private void btnDiminuirUmSegundo_Click(object sender, EventArgs e)
        {
            hora.RemoverUmSegundo(1);
            //hora.Segundos -= 1;
            lblHoras.Text = hora.ToString();
        }

        private void btnFechar_Click(object sender, EventArgs e)
        {
            Close();
        }
    }
}
