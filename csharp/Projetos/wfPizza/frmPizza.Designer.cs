namespace wfPizza
{
    partial class frmPedido
    {
        /// <summary>
        ///  Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        ///  Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        ///  Required method for Designer support - do not modify
        ///  the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            label1 = new Label();
            label2 = new Label();
            label3 = new Label();
            grpPedido = new GroupBox();
            cbxRefri = new ComboBox();
            label4 = new Label();
            panel1 = new Panel();
            rdoRefriNao = new RadioButton();
            rdoRefriSim = new RadioButton();
            cbxSabor = new ComboBox();
            chkBorda = new CheckBox();
            lblSabor = new Label();
            gpbProposta = new GroupBox();
            btnEnviar = new Button();
            grpPedido.SuspendLayout();
            panel1.SuspendLayout();
            gpbProposta.SuspendLayout();
            SuspendLayout();
            // 
            // label1
            // 
            label1.AutoSize = true;
            label1.Font = new Font("Segoe UI", 12F, FontStyle.Bold | FontStyle.Italic);
            label1.Location = new Point(50, 29);
            label1.Margin = new Padding(5, 0, 5, 0);
            label1.Name = "label1";
            label1.Size = new Size(129, 21);
            label1.TabIndex = 0;
            label1.Text = "Escolher o Sabor";
            // 
            // label2
            // 
            label2.AutoSize = true;
            label2.Font = new Font("Segoe UI", 12F, FontStyle.Bold | FontStyle.Italic);
            label2.Location = new Point(50, 54);
            label2.Margin = new Padding(5, 0, 5, 0);
            label2.Name = "label2";
            label2.Size = new Size(227, 21);
            label2.TabIndex = 1;
            label2.Text = "Escolher se quer ou não borda";
            // 
            // label3
            // 
            label3.AutoSize = true;
            label3.Font = new Font("Segoe UI", 12F, FontStyle.Bold | FontStyle.Italic);
            label3.Location = new Point(50, 79);
            label3.Margin = new Padding(5, 0, 5, 0);
            label3.Name = "label3";
            label3.Size = new Size(379, 21);
            label3.TabIndex = 2;
            label3.Text = "Escolher se quer ou não refrigerante e, se sim, qual";
            // 
            // grpPedido
            // 
            grpPedido.Controls.Add(cbxRefri);
            grpPedido.Controls.Add(label4);
            grpPedido.Controls.Add(panel1);
            grpPedido.Controls.Add(cbxSabor);
            grpPedido.Controls.Add(chkBorda);
            grpPedido.Controls.Add(lblSabor);
            grpPedido.Font = new Font("Arial Narrow", 14.25F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point, 0);
            grpPedido.Location = new Point(23, 136);
            grpPedido.Name = "grpPedido";
            grpPedido.Size = new Size(470, 160);
            grpPedido.TabIndex = 3;
            grpPedido.TabStop = false;
            grpPedido.Text = "Dados do Pedido";
            // 
            // cbxRefri
            // 
            cbxRefri.FormattingEnabled = true;
            cbxRefri.Items.AddRange(new object[] { "Coca-Cola", "Coca-Cola Zero", "Fanta Laranja", "Guaraná" });
            cbxRefri.Location = new Point(298, 106);
            cbxRefri.Name = "cbxRefri";
            cbxRefri.Size = new Size(153, 31);
            cbxRefri.TabIndex = 6;
            cbxRefri.Visible = false;
            // 
            // label4
            // 
            label4.AutoSize = true;
            label4.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            label4.ForeColor = Color.FromArgb(64, 0, 64);
            label4.Location = new Point(26, 114);
            label4.Name = "label4";
            label4.Size = new Size(138, 23);
            label4.TabIndex = 5;
            label4.Text = "Quer refrigerante?";
            // 
            // panel1
            // 
            panel1.Controls.Add(rdoRefriNao);
            panel1.Controls.Add(rdoRefriSim);
            panel1.Location = new Point(161, 103);
            panel1.Name = "panel1";
            panel1.Size = new Size(131, 34);
            panel1.TabIndex = 4;
            // 
            // rdoRefriNao
            // 
            rdoRefriNao.AutoSize = true;
            rdoRefriNao.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            rdoRefriNao.ForeColor = Color.FromArgb(64, 0, 64);
            rdoRefriNao.Location = new Point(68, 7);
            rdoRefriNao.Name = "rdoRefriNao";
            rdoRefriNao.Size = new Size(57, 27);
            rdoRefriNao.TabIndex = 4;
            rdoRefriNao.TabStop = true;
            rdoRefriNao.Text = "Não";
            rdoRefriNao.UseVisualStyleBackColor = true;
            // 
            // rdoRefriSim
            // 
            rdoRefriSim.AutoSize = true;
            rdoRefriSim.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            rdoRefriSim.ForeColor = Color.FromArgb(64, 0, 64);
            rdoRefriSim.Location = new Point(6, 7);
            rdoRefriSim.Name = "rdoRefriSim";
            rdoRefriSim.Size = new Size(54, 27);
            rdoRefriSim.TabIndex = 3;
            rdoRefriSim.TabStop = true;
            rdoRefriSim.Text = "Sim";
            rdoRefriSim.UseVisualStyleBackColor = true;
            rdoRefriSim.CheckedChanged += radioButton1_CheckedChanged;
            // 
            // cbxSabor
            // 
            cbxSabor.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            cbxSabor.ForeColor = Color.FromArgb(64, 0, 64);
            cbxSabor.FormattingEnabled = true;
            cbxSabor.Location = new Point(88, 36);
            cbxSabor.Name = "cbxSabor";
            cbxSabor.Size = new Size(363, 31);
            cbxSabor.TabIndex = 2;
            // 
            // chkBorda
            // 
            chkBorda.AutoSize = true;
            chkBorda.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            chkBorda.ForeColor = Color.FromArgb(64, 0, 64);
            chkBorda.Location = new Point(31, 78);
            chkBorda.Name = "chkBorda";
            chkBorda.Size = new Size(148, 27);
            chkBorda.TabIndex = 1;
            chkBorda.Text = "Borda Recheada";
            chkBorda.UseVisualStyleBackColor = true;
            chkBorda.CheckedChanged += checkBox1_CheckedChanged;
            // 
            // lblSabor
            // 
            lblSabor.AutoSize = true;
            lblSabor.Font = new Font("Arial Narrow", 14.25F, FontStyle.Italic);
            lblSabor.ForeColor = Color.FromArgb(64, 0, 64);
            lblSabor.Location = new Point(26, 44);
            lblSabor.Name = "lblSabor";
            lblSabor.Size = new Size(56, 23);
            lblSabor.TabIndex = 0;
            lblSabor.Text = "Sabor:";
            // 
            // gpbProposta
            // 
            gpbProposta.Controls.Add(label1);
            gpbProposta.Controls.Add(label2);
            gpbProposta.Controls.Add(label3);
            gpbProposta.Font = new Font("Segoe UI", 12F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point, 0);
            gpbProposta.ForeColor = Color.Red;
            gpbProposta.Location = new Point(23, 12);
            gpbProposta.Name = "gpbProposta";
            gpbProposta.Size = new Size(470, 106);
            gpbProposta.TabIndex = 4;
            gpbProposta.TabStop = false;
            gpbProposta.Text = "Proposta";
            // 
            // btnEnviar
            // 
            btnEnviar.Font = new Font("Segoe UI", 14.25F, FontStyle.Italic, GraphicsUnit.Point, 0);
            btnEnviar.Location = new Point(321, 302);
            btnEnviar.Name = "btnEnviar";
            btnEnviar.Size = new Size(172, 37);
            btnEnviar.TabIndex = 5;
            btnEnviar.Text = "Enviar Pedido";
            btnEnviar.UseVisualStyleBackColor = true;
            // 
            // frmPedido
            // 
            AutoScaleDimensions = new SizeF(11F, 25F);
            AutoScaleMode = AutoScaleMode.Font;
            ClientSize = new Size(521, 358);
            Controls.Add(btnEnviar);
            Controls.Add(gpbProposta);
            Controls.Add(grpPedido);
            Font = new Font("Segoe UI", 14.25F, FontStyle.Bold | FontStyle.Italic, GraphicsUnit.Point, 0);
            ForeColor = Color.FromArgb(0, 0, 192);
            Margin = new Padding(5);
            Name = "frmPedido";
            Text = "Pedido de Pizza";
            grpPedido.ResumeLayout(false);
            grpPedido.PerformLayout();
            panel1.ResumeLayout(false);
            panel1.PerformLayout();
            gpbProposta.ResumeLayout(false);
            gpbProposta.PerformLayout();
            ResumeLayout(false);
        }

        #endregion

        private Label label1;
        private Label label2;
        private Label label3;
        private GroupBox grpPedido;
        private CheckBox chkBorda;
        private Label lblSabor;
        private ComboBox cbxSabor;
        private RadioButton rdoRefriSim;
        private Panel panel1;
        private RadioButton rdoRefriNao;
        private Label label4;
        private ComboBox cbxRefri;
        private GroupBox gpbProposta;
        private Button btnEnviar;
    }
}
